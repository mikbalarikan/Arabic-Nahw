#!/usr/bin/env python3
"""Generate one WAV per script segment: video/lessons/<id>/audio/raw/<segment>.wav

Voices (English and Arabic can differ):
  supertonic:<STYLE>   Supertonic 3 (Supertone, OpenRAIL-M), ONNX on CPU, same voice in both
                       languages. STYLE is F1..F5 or M1..M5.
  kokoro:<VOICE>       Kokoro-82M (Apache-2.0), English only, e.g. am_michael, af_heart, bm_george.
  nabra:<SID>          Nabra-82M (Apache-2.0, Kokoro fine-tune for MSA), Arabic only, fed with
                       IPA from ar_g2p.py so every word keeps the ending written in the
                       lesson (no pause form).
  files:<DIR>          WAVs made elsewhere (e.g. a cloud GPU notebook), named <segment>.wav.

Supertonic samples noise, so every clip is made with a fixed seed. With --verify, each Arabic
clip is retried with small variations until check_endings.py hears the right last vowel; the
winning variation is saved in audio/choices_<voice>.json so the same clip comes back next time.

Usage:
  python3 video/tools/tts_generate.py --en supertonic:M3 --ar supertonic:M3 \\
      --verify ~/Projects/nasb-tts/models/phoneme [--lesson nasb] [--only id,id] [--scenes c06-] [--force]
Models are looked for in --models (default ~/Projects/nasb-tts/models).
"""
import argparse, json, re, shutil, sys
from pathlib import Path

import numpy as np
import soundfile as sf

sys.path.insert(0, str(Path(__file__).parent))
from tts_text import speak_ar, speak_en  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]

# attempts for an Arabic Supertonic clip, in order: (text suffix, speed, seed).
ATTEMPTS = [(" -", 0.7, 0), ("!", 0.7, 0), (" -", 0.7, 1), (" -", 0.8, 0), ("!", 0.7, 1),
            ("", 0.75, 0), (" -", 0.7, 2), ("!", 0.8, 2), (" -", 0.72, 3), ("،", 0.7, 3),
            (" -", 0.7, 4), ("!", 0.7, 5)] + [(sfx, 0.7 + 0.05 * (k % 3), 6 + k) for k in range(12) for sfx in (" -", "!")][:12]


def apply_say(text, say):
    """Optional lessons/<id>/say.json {written word: spoken word}: how the voice should say a word (e.g. the
    hidden long a of هَذَا, given as هٰذَا). Voice input only; a word may carry a leading وَ / فَ."""
    out = []
    for w in text.split():
        core = w.rstrip(".،؟!")
        tail = w[len(core):]
        pre = core[:2] if core[:2] in ("\u0648\u064E", "\u0641\u064E") and core[2:] in say else ""
        core = core[len(pre):]
        out.append(pre + say.get(core, core) + tail)
    return " ".join(out)


def respell(text):
    """Last resort for a voice that drops the ending of the LAST word: spell the ending out for the voice
    only (the screen text is unchanged). Tanween -> the vowel + نْ (صَفًّا -> صَفَّنْ, نُوحٌ -> نُوحُنْ);
    a final short vowel -> hāʾ al-sakt, which keeps the vowel in pause (هُوَ -> هُوَهْ)."""
    words = text.split()
    w = words[-1]
    end = w[len(w.rstrip("؟،؛.!?…,")):]   # keep a final question mark or comma after the respelled ending
    w = w[:len(w) - len(end)]
    tan = {"\u064B": "\u064E", "\u064C": "\u064F", "\u064D": "\u0650"}
    m = re.search("([\u064B-\u064D])(\u0651?)\u0627?$|(\u0651?)([\u064B-\u064D])\u0627?$", w)
    if m:
        t = m.group(1) or m.group(4)
        w = w[:m.start()] + (m.group(2) or m.group(3) or "") + tan[t] + "\u0646\u0652"
    elif re.search("[\u064E-\u0650]$", w):
        w += "\u0647\u0652"
    return " ".join(words[:-1] + [w + end])


class Supertonic:
    def __init__(self, models, style, steps):
        from supertonic import TTS
        self.tts = TTS(model="supertonic-3", model_dir=str(models / "supertonic-3"))
        self.style = self.tts.get_voice_style(style)
        self.steps, self.sr = steps, self.tts.sample_rate

    def en(self, text, speed):
        np.random.seed(0)
        w, _ = self.tts.synthesize(text, voice_style=self.style, lang="en", speed=speed, total_steps=self.steps)
        return np.asarray(w).squeeze().astype("float32")

    def ar(self, text, attempt):
        suffix, speed, seed = attempt
        if suffix.endswith("|respell"):
            suffix = suffix[:-len("|respell")]
            text = respell(text)
        if suffix.endswith("|noalif"):
            suffix = suffix[:-len("|noalif")]
            text = re.sub("\u064B\u0627(?=\\s|$)", "\u064B", text)
        np.random.seed(seed)
        w, _ = self.tts.synthesize(text + suffix, voice_style=self.style, lang="ar", speed=speed, total_steps=self.steps)
        return np.asarray(w).squeeze().astype("float32")


class Kokoro:
    def __init__(self, models, voice):
        from kokoro_onnx import Kokoro as K
        self.k = K(str(models / "kokoro-v1.0.onnx"), str(models / "voices-v1.0.bin"))
        self.voice, self.sr = voice, 24000
        self.lang = "en-gb" if voice.startswith("b") else "en-us"

    def en(self, text, speed):
        a, self.sr = self.k.create(text, voice=self.voice, speed=speed, lang=self.lang)
        return np.asarray(a, dtype="float32")


# ---- Arabic phonemes for Nabra --------------------------------------------------------
SHADDA, VOWELS = "ّ", "ًٌٍَُِ"
END_IPA = {"َ": "a", "ُ": "u", "ِ": "i", "ً": "an", "ٌ": "un", "ٍ": "in"}
IPA_V = "aiuɑæɐəeɛoɔʊɪ"


def word_ending(w):
    w = w.rstrip("ـ")
    if w.endswith("ا") and "ً" in w[-3:]:
        return "an"
    tail = ""
    for c in reversed(w):
        if "ً" <= c <= "ْ":
            tail = c + tail
        else:
            break
    for m in "ًٌٍَُِ":
        if m in tail:
            return END_IPA[m]
    return ""


class Nabra:
    def __init__(self, models, sid):
        import sherpa_onnx
        from piper.phonemize_espeak import EspeakPhonemizer
        d = models / "nabra-82m-arabic-int8"
        self.tts = sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
            kokoro=sherpa_onnx.OfflineTtsKokoroModelConfig(model=str(d / "model.int8.onnx"), voices=str(d / "voices.bin"),
                                                           tokens=str(d / "tokens.txt")),
            num_threads=4, provider="cpu")))
        self.vocab = set(l.rsplit(" ", 1)[0] for l in (d / "tokens.txt").read_text(encoding="utf-8").split("\n") if l)
        self.esp = EspeakPhonemizer()
        self.sid, self.sr = int(sid), 24000

    def ipa_word(self, w, first):
        t = re.sub(f"([{VOWELS}]){SHADDA}", SHADDA + r"\1", w)           # shadda before its vowel
        ph = "".join("".join(s) for s in self.esp.phonemize("ar", t))
        ph = re.sub(r"[.ˌˈˤ]", "", ph).replace(" ", "")
        if not first and w.startswith("ا"):                         # hamzat al-wasl: no glottal stop inside the sentence
            ph = re.sub(r"^ʔ?[aiu]?", "", ph)
        end = word_ending(w)
        if end:
            core = re.sub(f"[{IPA_V}ː]*n?$", "", ph) if end.endswith("n") else re.sub(f"[{IPA_V}]$", "", ph)
            ph = core + end                                               # the ending exactly as written
        return ph

    def phonemes(self, text):
        from ar_g2p import g2p
        return g2p(text)

    def ar(self, text, attempt):
        import sherpa_onnx
        ph = self.phonemes(text) + attempt[0]
        g = sherpa_onnx.GenerationConfig(); g.sid = self.sid; g.speed = attempt[1]
        g.tokens = [[c for c in ph if c in self.vocab]]
        a = self.tts.generate("", g)
        self.sr = a.sample_rate
        return np.asarray(a.samples, dtype="float32")


def make(spec, models, steps):
    kind, _, arg = spec.partition(":")
    if kind == "supertonic":
        return Supertonic(models, arg, steps)
    if kind == "kokoro":
        return Kokoro(models, arg)
    if kind == "nabra":
        return Nabra(models, arg)
    sys.exit(f"unknown voice {spec}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--en", required=True, help="English voice, e.g. supertonic:M3 or kokoro:am_michael")
    ap.add_argument("--ar", required=True, help="Arabic voice, e.g. supertonic:M3 or nabra:0")
    ap.add_argument("--lesson", default="nasb")
    ap.add_argument("--only", default=None)
    ap.add_argument("--scenes", default=None, help="comma-separated scene prefixes")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--out", default=None, help="output folder (default: lessons/<id>/audio/raw)")
    ap.add_argument("--models", default=str(Path.home() / "Projects/nasb-tts/models"))
    ap.add_argument("--en-speed", type=float, default=1.0)
    ap.add_argument("--ar-speed", type=float, default=0.8)
    ap.add_argument("--steps", type=int, default=16)
    ap.add_argument("--verify", default=None, help="phoneme model dir: retry Arabic clips until the ending check passes")
    a = ap.parse_args()

    d = ROOT / "video" / "lessons" / a.lesson
    raw = Path(a.out) if a.out else d / "audio" / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    segs = json.loads((d / "script.json").read_text(encoding="utf-8"))["segments"]
    # "qr" segments are Qur'an recitation: a real recording, cut into audio/raw/ by cut_recitation.py.
    # They are never synthesised (not even with --force).
    segs = [s for s in segs if s["lang"] != "qr"]
    if a.only:
        keep = set(a.only.split(","))
        segs = [s for s in segs if s["id"] in keep]
    if a.scenes:
        segs = [s for s in segs if s["scene"].startswith(tuple(a.scenes.split(",")))]
    todo = [s for s in segs if a.force or not (raw / f"{s['id']}.wav").exists()]
    spath = d / "say.json"
    say = {k: v for k, v in json.loads(spath.read_text(encoding="utf-8")).items() if not k.startswith("_")} if spath.exists() else {}
    models = Path(a.models).expanduser()
    (raw.parent / "voice.json").write_text(json.dumps(vars(a), indent=1))

    if a.en.startswith("files:") or a.ar.startswith("files:"):
        src = Path((a.en if a.en.startswith("files:") else a.ar).split(":", 1)[1])
        for s in todo:
            shutil.copy(src / f"{s['id']}.wav", raw / f"{s['id']}.wav")
        print(f"copied {len(todo)} clips"); return

    en = make(a.en, models, a.steps)
    ar = en if a.ar == a.en else make(a.ar, models, a.steps)
    checker = None
    if a.verify:
        from check_endings import expected, judge
        from phonemes import Phonemizer
        checker = Phonemizer(a.verify)
    cpath = raw.parent / f"choices_{a.ar.replace(':', '_')}.json"
    choices = json.loads(cpath.read_text()) if cpath.exists() else {}
    flagged = []
    for i, s in enumerate(todo, 1):
        out = raw / f"{s['id']}.wav"
        if s["lang"] == "en":
            sf.write(out, en.en(speak_en(s["text"]), a.en_speed), en.sr)
        else:
            text = apply_say(speak_ar(s["text"]), say)
            if isinstance(ar, Nabra):
                # deterministic model: vary the closing punctuation and the speed instead of a seed
                tries = [(p, sp, 0) for sp in (a.ar_speed, a.ar_speed + 0.1, a.ar_speed - 0.1) for p in (".", "!", "…", "", ",")]
                if s["id"] in choices:
                    tries = [tuple(choices[s["id"]])] + tries
            else:
                tries = list(ATTEMPTS)
                if s["id"] in choices:
                    tries = [tuple(choices[s["id"]])] + tries
            if not isinstance(ar, Nabra) and re.search("\u064B\u0627(?=\\s|$)", text):
                # fallback: some voices read the silent alif after fatha-tanween ("-ana");
                # the same attempts again with that alif left out of the TTS input (screen text unchanged)
                tries += [(t[0] + "|noalif", t[1], t[2]) for t in ATTEMPTS[:8]]
            if not isinstance(ar, Nabra) and respell(text) != text:
                # last resort: the ending spelled out for the voice only (see respell)
                tries += [(t[0] + "|respell", t[1], t[2]) for t in ATTEMPTS[:10]]
            first = None
            for att in tries:
                sf.write(out, ar.ar(text, att), ar.sr)
                if checker is None:
                    break
                ok, _ = judge(expected(text.split()[-1]), checker(out), text.split()[-1])
                first = first or att
                if ok:
                    choices[s["id"]] = list(att)
                    break
            else:
                flagged.append(s["id"])
                sf.write(out, ar.ar(text, first), ar.sr)    # keep the first attempt; a person must listen
        if i % 25 == 0:
            print(f"{i}/{len(todo)}", flush=True)
    cpath.write_text(json.dumps(choices, ensure_ascii=False, indent=1))
    print(f"generated {len(todo)} clips (en {a.en}, ar {a.ar})"
          + (f"; {len(flagged)} Arabic clips never passed the ending check: {flagged}" if flagged else ""))


if __name__ == "__main__":
    main()
