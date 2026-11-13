#!/usr/bin/env python3
"""Check that every Arabic string in a video script comes from the lesson source.

An Arabic run is allowed when it appears, word for word, inside
  - a string literal of content/lesson.py, or the Arabic title in content/course.py, or
  - a full example / practice sentence built from the lesson's own word boxes (lesson.json).
It also warns when a word in an Arabic ("ar") segment has no vowel mark on its last letter.

Usage: python3 video/tools/check_arabic.py video/lessons/nasb/script.json
Exit code 0 = no errors.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AR_CHAR = "؀-ۿݐ-ݿࢠ-ࣿ"
AR_RUN = re.compile(f"[{AR_CHAR}]+(?:[ ()]*[{AR_CHAR}]+)*")
HARAKAT = set("ًٌٍَُِّْ")
TATWEEL = "ـ"

def norm(s):
    return " ".join(s.split())

def allowed_strings(lesson_json):
    out = []
    for f in ("content/lesson.py", "content/course.py"):
        src = (ROOT / f).read_text(encoding="utf-8")
        out += [norm(m.group(0)) for m in AR_RUN.finditer(src)]
    data = json.loads(Path(lesson_json).read_text(encoding="utf-8"))
    out += [norm(x["sentence"]) for x in data["examples"]]
    out += [norm(x["sentence"]) for x in data["practice"]]
    return out

def is_allowed(run, allowed):
    run = norm(run)
    pat = re.compile(r"(?<![" + AR_CHAR + r"])" + re.escape(run) + r"(?![" + AR_CHAR + r"])")
    return any(pat.search(a) for a in allowed)

def strings(obj, path="$"):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from strings(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from strings(v, f"{path}[{i}]")

def main(script_path, lesson_json=ROOT / "video/lessons/nasb/lesson.json"):
    allowed = allowed_strings(lesson_json)
    script = json.loads(Path(script_path).read_text(encoding="utf-8"))
    errors, warns, n = [], [], 0
    for path, s in strings(script):
        for m in AR_RUN.finditer(s):
            n += 1
            if not is_allowed(m.group(0), allowed):
                errors.append(f"{path}: not in lesson source: {m.group(0)}")
    segs = script.get("segments", script if isinstance(script, list) else [])
    for seg in segs:
        if isinstance(seg, dict) and seg.get("lang") == "ar":
            for w in seg["text"].replace("(", " ").replace(")", " ").split():
                w = w.rstrip(TATWEEL)
                if w.endswith("\u0627") and w[-2:-1] == "\u064B":
                    continue  # fatha + tanween written with the extra alif
                last = w.rstrip("".join(HARAKAT))
                if w == last:
                    warns.append(f"{seg.get('id')}: no final vowel on {w}")
    for e in errors: print("ERROR", e)
    for w in warns: print("WARN ", w)
    print(f"{n} Arabic strings checked: {len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
