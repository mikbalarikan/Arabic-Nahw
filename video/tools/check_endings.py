#!/usr/bin/env python3
"""Check that every Arabic clip ends with the vowel the lesson teaches.

For each "ar" segment, the expected ending of the LAST word is read from its marks
(fatha -a, damma -u, kasra -i, tanween -an/-un/-in, sukūn = no vowel). The clip is turned
into phonemes (phonemes.py) and its last sounds are compared. Pausal reading (waqf),
which drops the ending, is exactly the error this lesson cannot have.

Usage: python3 video/tools/check_endings.py MODEL_DIR AUDIO_DIR [script.json] [--only id,id]
       AUDIO_DIR holds <segment id>.wav
Prints one line per clip and a summary; exit code 1 if any clip fails.
"""
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from phonemes import Phonemizer  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
F, D, K, FT, DT, KT, SK, SH = "َ", "ُ", "ِ", "ً", "ٌ", "ٍ", "ْ", "ّ"
A_LIKE = {"a", "aː", "ɑ", "ɑː", "æ", "ɐ", "ʌ", "ɛ"}
U_LIKE = {"u", "uː", "ʊ", "o", "oː", "ɔ", "y"}
I_LIKE = {"i", "iː", "ɪ", "e", "eː", "ɨ"}
N_LIKE = {"n", "m", "ŋ"}

PUNCT = "؟،؛.!?…,"   # a question mark or comma after the last word is not part of its ending

def expected(word):
    """Ending taught by the marks on the LAST letter (marks after the last base letter only)."""
    w = word.rstrip(PUNCT).rstrip("\u0640")
    if w.endswith("\u0627") and FT in w[-3:]:
        return "an"
    tail = ""
    for c in reversed(w):
        if "\u064B" <= c <= "\u0652":
            tail = c + tail
        else:
            break
    for m, e in ((FT, "an"), (DT, "un"), (KT, "in"), (F, "a"), (D, "u"), (K, "i"), (SK, "-")):
        if m in tail:
            return e
    return "?"   # no mark on the last letter (the lesson writes it in pause form): nothing to check

def vclass(p):
    p = p.replace("[", "").replace("ˈ", "")
    if p in ("ə", "ɚ"): return "x"   # schwa: could be any short vowel
    if p in A_LIKE: return "a"
    if p in U_LIKE: return "u"
    if p in I_LIKE: return "i"
    if p in N_LIKE: return "n"
    return "c"

def judge(exp, phones, word=""):
    word = word.rstrip(PUNCT)
    seq = [vclass(p) for p in phones.split()]
    if not seq:
        return False, "no speech"
    last, prev = seq[-1], (seq[-2] if len(seq) > 1 else "")
    if exp in ("a", "u", "i"):
        # a short vowel after a consonant: "b a", not the long "aː" of a dropped final letter
        # a long final vowel is fine for -u/-i; for -a it usually means a dropped last letter ("b aː" of al-baab)
        # A long final -aː is fine ("darsaː"), except when the word has ā before its last letter
        # (al-bāba, al-māʔa, amāma): there "b aː" may be the ā of a word whose ending was dropped.
        base = "".join(c for c in word if not ("\u064B" <= c <= "\u0652"))
        alif_before_last = len(base) >= 3 and base[-2] == "\u0627"
        short = "ː" not in phones.split()[-1] or exp != "a" or not alif_before_last
        # a one-letter word read alone (أَ, لِ): the phoneme model often drops the glottal onset of أَ ("a"),
        # so only its vowel is judged
        onset = prev in ("c", "n") or (len(base) == 1 and len(seq) == 1)
        return last in (exp, "x") and short and onset, f"ends …{' '.join(phones.split()[-3:])}"
    if exp in ("an", "un", "in"):
        ok = last == "n" and prev in (exp[0], "x")
        return ok, f"ends …{' '.join(phones.split()[-3:])}"
    ph = phones.split()
    tail = f"ends …{' '.join(ph[-3:])}"
    if exp == "?":
        # no mark on the last letter: the lesson writes the pause form. Judge it by its written shape:
        # a final long vowel letter (فِي) ends in a vowel, anything else ends in a consonant.
        base = "".join(c for c in word if not ("\u064B" <= c <= "\u0652"))
        if base.endswith(("\u064A", "\u0648", "\u0627", "\u0649")) and not word.endswith("\u0651"):   # ى: long ā (مَتَى)
            return True, "no mark (long vowel)"
        exp = "-"
    if exp == "-":
        # ends in a consonant, and no echo of it after an extra vowel ("b uː b" = uktubūb)
        echo = len(ph) >= 3 and seq[-2] in "aiux" and ph[-1] == ph[-3]
        return (last in ("c", "n")) and not echo, tail
    return True, "no mark"

def main():
    args = sys.argv[1:]
    only = None
    if "--only" in args:
        k = args.index("--only"); only = set(args[k + 1].split(",")); del args[k:k + 2]
    model_dir, audio_dir = args[0], Path(args[1])
    script = json.loads(Path(args[2] if len(args) > 2 else ROOT / "video/lessons/nasb/script.json").read_text(encoding="utf-8"))
    ph = Phonemizer(model_dir)
    fails, n = [], 0
    for s in script["segments"]:
        if s["lang"] != "ar" or (only and s["id"] not in only):
            continue
        wav = audio_dir / f"{s['id']}.wav"
        if not wav.exists():
            continue
        n += 1
        last = s["text"].replace("(", "").replace(")", "").split()[-1]
        exp = expected(last)
        phones = ph(wav)
        ok, why = judge(exp, phones, last)
        print(f"{'ok  ' if ok else 'FAIL'} {s['id']:<16} {last:<14} expect -{exp:<3} {why}   [{phones}]")
        if not ok:
            fails.append(s["id"])
    print(f"{n} clips: {n - len(fails)} ok, {len(fails)} fail")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
