#!/usr/bin/env python3
"""s3-verbs only: whole-clip check of every Arabic clip, and re-making the ones that fail.

check_endings.py only listens to the LAST sound of a clip. In this lesson the voice also dropped whole pieces
in the middle or at the end of a word that still ended in the right vowel (مَا كَتَبْتُهُ read as "mā katabtu":
the ـهُ "it" was gone) and read the helping alif of the order verbs with the wrong vowel (اُكْتُبْ as "aktub").
Chapter 7 teaches exactly that vowel. So every clip is compared with the expected sounds:

  - similarity: the clip's phonemes (phonemes.py) against ar_g2p.py's reading of the text, both reduced to
    coarse sound classes (vowel length, glottal stops and doubled letters ignored; the recogniser is not
    that precise), Levenshtein similarity >= MIN_SIM;
  - start: a clip that starts with اُ / اِ must start with a u-like / i-like vowel;
  - ending: check_endings.judge, unchanged, and the last four sound classes close to the expected ones.

With --fix, a failing clip is made again with the attempts of tts_generate.py (and, for اُ / اِ, a bare
hamza with the vowel as the voice input, ءُكْتُبْ, which M4 reads right where اُكْتُبْ and أُكْتُبْ give
"aktub"), keeping the first attempt that passes all three, else the best one. The winning voice input and
attempt are stored in audio/choices_supertonic_M4.json under "<id>|clip" (tts_generate.py ignores that key;
re-run this tool, not tts_generate --force, to remake these clips).

Usage: python3 video/tools/check_clips_s3_verbs.py MODEL_DIR [--fix [--redo]] [--only id,id]
"""
import json, re, sys
from pathlib import Path

import soundfile as sf

sys.path.insert(0, str(Path(__file__).parent))
from ar_g2p import g2p  # noqa: E402
from check_endings import expected, judge  # noqa: E402
from phonemes import Phonemizer  # noqa: E402
from tts_text import speak_ar  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
LID = "s3-verbs"
D = ROOT / "video" / "lessons" / LID
MIN_SIM = 0.72
START = {"اُ": ("U", "ءُ"), "اِ": ("I", "ءِ")}   # اُ -> ءُ, اِ -> ءِ

CLS = {}
for k in "a aː ɑ ɑː æ ɐ ʌ ɛ ə ɚ".split(): CLS[k] = "A"
for k in "u uː ʊ o oː ɔ y ø œ".split(): CLS[k] = "U"
for k in "i iː ɪ e eː ɨ".split(): CLS[k] = "I"
for k, v in {"ʔ": "", "ʕ": "", "ð": "d", "θ": "t", "t̪": "t", "ɹ": "r", "χ": "x", "ħ": "h", "dʒ": "j", "ɣ": "g",
             "aɪ": "AI", "aʊ": "AU", "ʃ": "S", "q": "k"}.items():
    CLS[k] = v
TOK = re.compile(r"dʒ|t̪|aɪ|aʊ|[^\sˈː]ː?")


def classes(tokens):
    out = []
    for t in tokens:
        c = CLS.get(t, CLS.get(t.rstrip("ː"), t.rstrip("ː")))
        for ch in ([c] if len(c) <= 1 else list(c)):
            if ch and (not out or out[-1] != ch):
                out.append(ch)
    return out


def ref(text):
    return classes(TOK.findall(g2p(text).replace("ˈ", "")))


def heard(phones):
    return classes(phones.split())


def sim(a, b):
    m, n = len(a), len(b)
    d = list(range(n + 1))
    for i in range(1, m + 1):
        prev, d[0] = d[0], i
        for j in range(1, n + 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1, prev + (a[i - 1] != b[j - 1]))
            prev = cur
    return 1 - d[n] / max(m, n, 1)


def verdict(text, phones):
    h, r = heard(phones), ref(text)
    s = sim(r, h)
    last = text.split()[-1]
    end_ok = judge(expected(last), phones, last)[0]
    # the last word must be whole: its last four sound classes (catches كَتَبْتُهُ read as "katabtu")
    end_ok = end_ok and sim(r[-4:], h[-4:]) >= 0.75
    start_ok = True
    if text[:2] in START:
        # the first vowel; one click / stray consonant before it is allowed ("b ʊ x r uː dʒ")
        v = [c for c in h[:2] if c in "AIU"]
        start_ok = bool(v) and v[0] == START[text[:2]][0]
    return s, start_ok, end_ok, s >= MIN_SIM and start_ok and end_ok


def main():
    args = sys.argv[1:]
    fix = "--fix" in args
    redo = "--redo" in args          # with --only: make these clips again even if they pass
    args = [a for a in args if a not in ("--fix", "--redo")]
    only = None
    if "--only" in args:
        k = args.index("--only"); only = set(args[k + 1].split(",")); del args[k:k + 2]
    ph = Phonemizer(args[0])
    segs = [s for s in json.loads((D / "script.json").read_text(encoding="utf-8"))["segments"]
            if s["lang"] == "ar" and (not only or s["id"] in only)]
    raw = D / "audio" / "raw"
    cpath = D / "audio" / "choices_supertonic_M4.json"
    choices = json.loads(cpath.read_text()) if cpath.exists() else {}
    tts = None
    bad = []
    for s in segs:
        text = speak_ar(s["text"])
        out = raw / f"{s['id']}.wav"
        p = ph(out)
        sc, st, en, ok = verdict(text, p)
        line = f"{s['id']:<16} sim {sc:.2f} start {'ok' if st else 'NO'} end {'ok' if en else 'NO'}  {s['text']}  [{p}]"
        if (ok and not redo) or not fix:
            print(("ok   " if ok else "BAD  ") + line, flush=True)
            if not ok:
                bad.append(s["id"])
            continue
        if tts is None:
            import tts_generate as TG
            tts = TG.Supertonic(Path.home() / "Projects/nasb-tts/models", "M4", 16)
            attempts = TG.ATTEMPTS
        inputs = [text]
        if text[:2] in START:
            inputs = [START[text[:2]][1] + text[2:]]
        if "؟" in text or "،" in text:
            inputs.append(text.replace("؟", "،"))     # a question mark inside a reading invites a pause form
        best = None
        for vin in inputs:
            for att in attempts:
                sf.write(out, tts.ar(vin, att), tts.sr)
                p = ph(out)
                sc, st, en, ok = verdict(text, p)
                key = (ok, st and en, sc)
                if best is None or key > best[0]:
                    best = (key, vin, att, p)
                if ok:
                    break
            if best[0][0]:
                break
        (ok, _, sc), vin, att, p = best
        sf.write(out, tts.ar(vin, att), tts.sr)
        choices[f"{s['id']}|clip"] = [vin] + list(att)
        print(("FIXED" if ok else "BEST ") + f" {s['id']:<16} sim {sc:.2f} {s['text']}  [{p}]  {att} {vin != text and 'voice input: ' + vin or ''}",
              flush=True)
        if not ok:
            bad.append(s["id"])
    if fix:
        cpath.write_text(json.dumps(choices, ensure_ascii=False, indent=1))
    print(f"{len(segs)} Arabic clips, {len(bad)} not passing: {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
