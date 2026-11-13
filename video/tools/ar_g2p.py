#!/usr/bin/env python3
"""Fully vowelled Arabic (MSA) -> IPA phonemes, reading every written ending.

espeak-ng reads the last word of a phrase in pause form and mishandles shadda, so the
Arabic voice (Nabra-82M, which was trained on espeak-style IPA) gets its phonemes from
here instead. The rules are the plain rules of vowelled MSA:
  - every haraka is read; sukūn = no vowel; shadda = doubled consonant;
  - tanween = vowel + n; the alif after fatha + tanween is silent;
  - ا after fatha, و after damma, ي after kasra (with no mark of their own) lengthen the vowel;
  - hamzat al-wasl (ال, and a word-initial ا) is silent inside the sentence, read ʔ + vowel at the start;
  - the ل of ال is silent before a sun letter (that letter carries shadda in the text);
  - a long vowel before a wasl word is shortened; tanween before a wasl word adds i.
  - stress: superheavy final > heavy penult > antepenult (> penult), mark ˈ before the vowel.
Emphatic consonants are written without ˤ, as in the voice's training data.

Usage: python3 video/tools/ar_g2p.py "كَتَبَ الطَّالِبُ الدَّرْسَ"
"""
import sys

FATHA, DAMMA, KASRA, SUKUN, SHADDA = "َ", "ُ", "ِ", "ْ", "ّ"
FATHATAN, DAMMATAN, KASRATAN = "ً", "ٌ", "ٍ"
MARKS = {FATHA, DAMMA, KASRA, SUKUN, SHADDA, FATHATAN, DAMMATAN, KASRATAN, "ٰ"}
VOW = {FATHA: "a", DAMMA: "u", KASRA: "i"}
TAN = {FATHATAN: "a", DAMMATAN: "u", KASRATAN: "i"}
CONS = {
    "ب": "b", "ت": "t", "ث": "θ", "ج": "dʒ", "ح": "ħ", "خ": "χ", "د": "d", "ذ": "ð", "ر": "r",
    "ز": "z", "س": "s", "ش": "ʃ", "ص": "s", "ض": "d", "ط": "t", "ظ": "ð", "ع": "ʕ", "غ": "ɣ",
    "ف": "f", "ق": "q", "ك": "k", "ل": "l", "م": "m", "ن": "n", "ه": "h", "و": "w", "ي": "j",
    "ء": "ʔ", "أ": "ʔ", "إ": "ʔ", "ؤ": "ʔ", "ئ": "ʔ", "ة": "t",
}
ALIF, WAW, YA, MAQSURA, MADDA = "ا", "و", "ي", "ى", "آ"


def letters(word):
    """[(letter, set_of_marks)] with tatweel and brackets removed."""
    out = []
    for c in word:
        if c in "ـ()":
            continue
        if c == "ٱ":
            c = ALIF
        if c in MARKS and out:
            out[-1][1].add(c)
        else:
            out.append((c, set()))
    return out


def word_units(word, utter_start):
    """Units: ('C', sym) or ('V', 'a'/'aː'...). Returns (units, starts_with_wasl, ends_in_tanween)."""
    L = letters(word)
    u, wasl, tan, art_at = [], False, False, None
    for k, (c, m) in enumerate(L):
        nxt = L[k + 1] if k + 1 < len(L) else None
        last_v = u[-1][1] if u and u[-1][0] == "V" else None
        if c == MADDA:
            u += [("C", "ʔ"), ("V", "aː")]; continue
        if c == ALIF:
            v = next((VOW[x] for x in m if x in VOW), None)
            if k == 0:                                   # hamzat al-wasl
                if utter_start:
                    is_al = nxt is not None and nxt[0] == "ل"
                    u += [("C", "ʔ"), ("V", v or ("a" if is_al else "i"))]
                else:
                    wasl = True
                continue
            if (not m and k == 1 and L[0][0] in "وفبك" and nxt is not None and nxt[0] == "ل"
                    and k + 2 < len(L) and not (nxt[1] & (set(VOW) | set(TAN) | {SHADDA}))):
                art_at = k                               # ال after a prefix (وَال...): silent wasl
                continue
            if last_v == "a" and not m:
                u[-1] = ("V", "aː")                     # long ā
            continue                                     # alif after fatha+tanween, or other silent alif
        if c == MAQSURA:
            if last_v == "a":
                u[-1] = ("V", "aː")
            continue
        if c in (WAW, YA) and not m and last_v == ("u" if c == WAW else "i"):
            u[-1] = ("V", last_v + "ː")                  # long ū / ī
            continue
        sym = CONS.get(c)
        if sym is None:
            continue
        if c == "ل" and k >= 1 and (L[k - 1][0] == ALIF or (L[k - 1][0] == "ل" and KASRA in L[k - 1][1] and k <= 2)) \
                and not (m & set(VOW)) and nxt and SHADDA in nxt[1]:
            continue                                     # the lam of al- before a sun letter
        u.append(("C", sym))
        if SHADDA in m:
            u.append(("C", sym))
        v = next((VOW[x] for x in m if x in VOW), None)
        t = next((TAN[x] for x in m if x in TAN), None)
        if "ٰ" in m and v in (None, "a"):
            u.append(("V", "aː"))
        elif v:
            u.append(("V", v))
        elif t:
            u += [("V", t), ("C", "n")]
            tan = True
    return u, wasl, tan


def stress(units):
    vi = [i for i, (k, _) in enumerate(units) if k == "V"]
    units = [x for x in units]
    if not vi:
        return units
    syl = []
    for n, i in enumerate(vi):
        end = (vi[n + 1] - 1) if n + 1 < len(vi) else len(units)
        coda = sum(1 for k, _ in units[i + 1:end] if k == "C") if n + 1 < len(vi) else sum(1 for k, _ in units[i + 1:] if k == "C")
        long_v = units[i][1].endswith("ː")
        syl.append(dict(v=i, w=(2 if long_v else 1) + coda))
    if len(syl) == 1:
        s = 0
    elif syl[-1]["w"] >= 3:
        s = len(syl) - 1
    elif syl[-2]["w"] >= 2 or len(syl) == 2:
        s = len(syl) - 2
    else:
        s = len(syl) - 3
    out = list(units)
    out.insert(syl[s]["v"], ("S", "ˈ"))
    return out


def g2p(text):
    words = text.split()
    res = []
    for n, w in enumerate(words):
        u, wasl, _ = word_units(w, n == 0)
        if wasl and res:
            pu, pw, ptan = res[-1]
            if pu and pu[-1][0] == "V" and pu[-1][1].endswith("ː"):
                pu[-1] = ("V", pu[-1][1][0])              # fī l- -> fi l-
            elif ptan or (pu and pu[-1][0] == "C"):
                bare = "".join(ch for ch in words[n - 1] if ch not in MARKS)
                hv = "i"
                if not ptan:
                    if bare in ("من", "ومن", "فمن"):
                        hv = "a"
                    elif bare == "مذ" or bare.endswith(("هم", "كم", "تم")):
                        hv = "u"
                pu.append(("E", hv))                     # helping vowel before wasl
        res.append([u, wasl, word_units(w, False)[2]])
    out = []
    for u, _, _ in res:
        out.append("".join(s for _, s in stress(u)))
    return " ".join(out)


if __name__ == "__main__":
    for t in sys.argv[1:]:
        print(t, "->", g2p(t))
