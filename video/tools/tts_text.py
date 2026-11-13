#!/usr/bin/env python3
"""Turn script segments into the exact text a TTS model should read.

The script keeps the site's spelling (rafʿ, naṣb, sukūn, al, wa ...). Most TTS models read
those badly, so English segments get a small pronunciation lexicon here. Arabic segments
keep every vowel mark; only the brackets of the hidden doer (أَنْتَ) are dropped.

Usage: python3 video/tools/tts_text.py video/lessons/nasb/script.json > requests.jsonl
"""
import json, re, sys

# whole-word replacements for English narration (spoken form)
LEXICON = [
    (r"\brafʿ\b", "raf"),
    (r"\bnaṣb\b", "nasb"),
    (r"\bNaṣb\b", "Nasb"),
    (r"\bsukūn\b", "sukoon"),
    (r"\bIʿrāb\b", "Ee-raab"),
    (r"\biʿrāb\b", "ee-raab"),
    (r"\btanween\b", "tanween"),
    (r"\bjarr\b", "jarr"),
    (r"\bjazm\b", "jazm"),
    (r"\biḍāfa\b", "idaafa"),
    (r"\bZayd\b", "Zayd"),
    (r"\bal\b", "al"),
    (r"\bwa\b", "wa"),
    (r"→", ", "),
    (r"/", " or "),
    (r"\s*·\s*", ", "),
]

def speak_en(text):
    t = text
    for pat, rep in LEXICON:
        t = re.sub(pat, rep, t)
    # remaining diacritics on Latin letters (e.g. ā, ʿ) -> plain
    t = t.replace("ʿ", "").replace("ā", "aa").replace("ī", "ee").replace("ū", "oo").replace("ṣ", "s").replace("ḥ", "h")
    return re.sub(r"\s+", " ", t).strip()

def speak_ar(text):
    t = re.sub(r"[()]", "", text).strip()
    # a word written in pause form with a final shadda and no vowel (مَبْنِيّ): add sukūn for the voice,
    # so it is read "mabniyy", not with an invented vowel. Only the spoken input changes.
    return re.sub("(?<=[\u0621-\u064A])\u0651(?=\\s|$)", "\u0651\u0652", t)

def requests(script):
    for s in script["segments"]:
        yield dict(id=s["id"], lang=s["lang"],
                   text=speak_ar(s["text"]) if s["lang"] == "ar" else speak_en(s["text"]))

if __name__ == "__main__":
    script = json.load(open(sys.argv[1], encoding="utf-8"))
    for r in requests(script):
        print(json.dumps(r, ensure_ascii=False))
