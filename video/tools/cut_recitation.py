#!/usr/bin/env python3
"""Cut each verse fragment out of a real recitation recording (lesson quran-nasb).

Input:  video/lessons/<id>/audio/recitation/<vNN>_ayah.wav   one ayah (plus ~1 s either side), from
        a licensed recording (see recitation.json for source and licence)
        video/lessons/<id>/lesson.json                       the fragment text (verse "sentence")
Output: video/lessons/<id>/audio/recitation/<vNN>.wav        the fragment only
        video/lessons/<id>/audio/raw/<segment>.wav           a copy for every "qr" segment of that verse
        video/lessons/<id>/audio/recitation/cuts.json        cut times and the matched phonemes, for review

How: the phoneme model (phonemes.py) gives a phoneme per 20 ms frame. The fragment's Arabic text is turned
into a rough phoneme string, and a local alignment (Smith-Waterman) finds where it sits in the ayah.
The cut is then moved to the quietest point nearby (or set by hand: "manual" in cuts.json), and the clip
is brought to RECITE_LUFS, the narration's level. Always listen to the result: the cut is a proposal.

Usage: PY video/tools/cut_recitation.py MODEL_DIR [lesson_id] [--only v01,v02]
"""
import json, shutil, subprocess, sys
from pathlib import Path
import numpy as np
import soundfile as sf

sys.path.insert(0, str(Path(__file__).parent))
from phonemes import Phonemizer  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
FRAME = 0.02  # wav2vec2: 320 samples at 16 kHz

F, D, K, FT, DT, KT, SK, SH = "َ", "ُ", "ِ", "ً", "ٌ", "ٍ", "ْ", "ّ"
CONS = {"ب": "b", "ت": "t", "ة": "t", "ث": "s", "ج": "j", "ح": "h", "خ": "x", "د": "d", "ذ": "z", "ر": "r",
        "ز": "z", "س": "s", "ش": "S", "ص": "s", "ض": "d", "ط": "t", "ظ": "z", "ع": "Q", "غ": "G", "ف": "f",
        "ق": "q", "ك": "k", "ل": "l", "م": "m", "ن": "n", "ه": "h", "أ": "?", "إ": "?", "ء": "?", "ؤ": "?",
        "ئ": "?", "آ": "?"}
SUN = set("تثدذرزسشصضطظلن")


def text_phones(text):
    """Very rough phoneme classes of vowelled Arabic: consonants (coarse) and a/i/u (long = doubled)."""
    out = []
    words = text.replace("ـ", "").split()
    for wi, w in enumerate(words):
        i = 0
        if w.startswith("ال"):
            if wi == 0:
                out.append("a")          # al at the start is said "a(l)"
            nxt = w[2] if len(w) > 2 else ""
            if nxt not in SUN:
                out.append("l")
            i = 2
            if i < len(w) and w[i] == SK:
                i += 1
        while i < len(w):
            c = w[i]
            if c == "ا":
                if out and out[-1] == "a":
                    out.append("a")      # long a
                elif i == 0:
                    pass                 # hamzat al-wasl inside the phrase
            elif c == "ى":
                if out and out[-1] == "a":
                    out.append("a")
            elif c == "و":
                if out and out[-1] == "u":
                    out.append("u")
                else:
                    out.append("w")
            elif c == "ي":
                if out and out[-1] == "i":
                    out.append("i")
                else:
                    out.append("y")
            elif c in CONS:
                out.append(CONS[c])
            elif c == F: out.append("a")
            elif c == D: out.append("u")
            elif c == K: out.append("i")
            elif c == FT: out += ["a", "n"]
            elif c == DT: out += ["u", "n"]
            elif c == KT: out += ["i", "n"]
            i += 1
        if w.endswith("ا") and FT in w[-3:]:
            pass  # the written alif after fatha + tanween is not said
    return out


def model_class(p):
    p = p.replace("ˤ", "").replace("ˈ", "").replace("ː", ":")
    long_ = p.endswith(":")
    p = p.rstrip(":")
    m = {"a": "a", "ɑ": "a", "æ": "a", "ɐ": "a", "ʌ": "a", "ə": "a", "ɛ": "a", "e": "i", "i": "i", "ɪ": "i",
         "ɨ": "i", "u": "u", "ʊ": "u", "o": "u", "ɔ": "u", "y": "u",
         "θ": "s", "s": "s", "ʃ": "S", "dʒ": "j", "ʒ": "j", "ħ": "h", "h": "h", "x": "x", "χ": "x", "ð": "z", "z": "z",
         "ʕ": "Q", "ɣ": "G", "ʁ": "G", "ʔ": "?", "q": "q", "k": "k", "g": "j", "ɡ": "j", "j": "y", "w": "w", "r": "r", "ɾ": "r",
         "b": "b", "t": "t", "d": "d", "f": "f", "l": "l", "m": "m", "n": "n", "ŋ": "n"}.get(p, p)
    return [m, m] if long_ and m in "aiu" else [m]


def frame_phones(ph, wav):
    """(class, start_s, end_s) for every phoneme the model hears, in order."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(wav), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                         check=True, capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.float32)
    a = (a - a.mean()) / (a.std() + 1e-7)
    names = [i.name for i in ph.sess.get_inputs()]
    feed = {names[0]: a[None, :]}
    if "attention_mask" in names:
        feed["attention_mask"] = np.ones((1, len(a)), dtype=np.int64)
    ids = ph.sess.run(None, feed)[0][0].argmax(-1)
    out, prev, start = [], None, 0
    for f, i in enumerate(list(ids) + [ph.blank]):
        if i != prev:
            if prev is not None and prev != ph.blank:
                t = ph.inv.get(int(prev), "")
                if not t.startswith("<"):
                    for c in model_class(t):
                        out.append((c, start * FRAME, f * FRAME))
            start = f
        prev = i
    return out


def local_align(target, heard):
    """Smith-Waterman: best local match of the whole-ish target inside heard. Returns (i0, i1) in heard."""
    n, m = len(target), len(heard)
    H = np.zeros((n + 1, m + 1)); P = np.zeros((n + 1, m + 1), dtype=np.int8)
    vow = set("aiu")
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a, b = target[i - 1], heard[j - 1][0]
            s = 2 if a == b else (0 if (a in vow) == (b in vow) else -1)
            opts = (0, H[i - 1, j - 1] + s, H[i - 1, j] - 1, H[i, j - 1] - 1)
            k = int(np.argmax(opts)); H[i, j] = opts[k]; P[i, j] = k
    # the fragment must be matched to its end: take the best cell in the last target row
    i, j = n, int(np.argmax(H[n]))
    score, j1 = H[i, j], j - 1
    while i > 0 and j > 0 and P[i, j] != 0:
        k = P[i, j]
        if k == 1: i, j = i - 1, j - 1
        elif k == 2: i -= 1
        else: j -= 1
    return j, j1, float(score), i


def quiet_point(x, sr, t, before, after):
    """Time of the lowest 20 ms energy between t-before and t+after."""
    w = int(0.02 * sr)
    a, b = max(0, int((t - before) * sr)), min(len(x) - w, int((t + after) * sr))
    if b <= a:
        return t
    e = [float(np.mean(x[k:k + w] ** 2)) for k in range(a, b, w // 2)]
    return (a + int(np.argmin(e)) * (w // 2) + w / 2) / sr


RECITE_LUFS = -24.0   # about the narration's level (English ~ -25, Arabic TTS words ~ -23 LUFS); the
                      # raw recording is ~6-8 dB louder and would jump out of the mix


def loudness(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", "ebur128", "-f", "null", "-"],
                       capture_output=True, text=True)
    return float(r.stderr.rsplit("I:", 1)[1].split("LUFS")[0])


def main():
    args = sys.argv[1:]
    only = None
    if "--only" in args:
        k = args.index("--only"); only = set(args[k + 1].split(",")); del args[k:k + 2]
    model_dir = args[0]
    lid = args[1] if len(args) > 1 else "quran-nasb"
    d = ROOT / "video" / "lessons" / lid
    rec, raw = d / "audio" / "recitation", d / "audio" / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    data = json.loads((d / "lesson.json").read_text(encoding="utf-8"))
    script = json.loads((d / "script.json").read_text(encoding="utf-8"))
    cuts_path = rec / "cuts.json"
    cuts = json.loads(cuts_path.read_text(encoding="utf-8")) if cuts_path.exists() else {}
    ph = Phonemizer(model_dir)
    for v in data["verses"]:
        vid = f'v{int(v["num"]):02d}'
        src = rec / f"{vid}_ayah.wav"
        if (only and vid not in only) or not src.exists():
            continue
        x, sr = sf.read(src, dtype="float32")
        target = text_phones(v["sentence"])
        heard = frame_phones(ph, src)
        j0, j1, score, left = local_align(target, heard)
        t0, t1 = heard[j0][1], heard[j1][2]
        manual = cuts.get(vid, {}).get("manual")       # [start, end] in seconds, set by hand after listening
        if manual:
            s, e = manual
        else:
            s = quiet_point(x, sr, t0 - 0.03, 0.25, 0.04)
            e = quiet_point(x, sr, t1 + 0.06, 0.04, 0.22)
        clip = x[int(s * sr):int(e * sr)].copy()
        fi, fo = int(0.02 * sr), int(0.06 * sr)
        clip[:fi] *= np.linspace(0, 1, fi); clip[-fo:] *= np.linspace(1, 0, fo)
        sf.write(rec / f"{vid}.wav", clip, sr)
        gain = 10 ** ((RECITE_LUFS - loudness(rec / f"{vid}.wav")) / 20)
        clip = clip * min(gain, 0.89 / (np.max(np.abs(clip)) or 1))   # never above -1 dBFS sample peak
        sf.write(rec / f"{vid}.wav", clip, sr)
        segs = [sg["id"] for sg in script["segments"] if sg["scene"] == vid and sg["lang"] == "qr"]
        for sid in segs:
            shutil.copy(rec / f"{vid}.wav", raw / f"{sid}.wav")
        heard_str = " ".join(h[0] for h in heard[j0:j1 + 1])
        cuts[vid] = dict(cuts.get(vid, {}), start=round(s, 3), end=round(e, 3), score=score,
                         unmatched_target_head=left, target=" ".join(target), heard=heard_str,
                         context_before=" ".join(h[0] for h in heard[max(0, j0 - 8):j0]),
                         context_after=" ".join(h[0] for h in heard[j1 + 1:j1 + 9]), segments=segs)
        print(f"{vid} {s:6.2f}-{e:6.2f}s ({e - s:4.1f}s) score {score:5.1f} miss-head {left}\n"
              f"   target: {' '.join(target)}\n   heard : [{cuts[vid]['context_before']}] {heard_str} [{cuts[vid]['context_after']}]")
    cuts_path.write_text(json.dumps(cuts, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
