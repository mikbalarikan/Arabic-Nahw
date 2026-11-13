#!/usr/bin/env python3
"""Join the script parts (video/lessons/<id>/parts/p*.json) into script.json, in file-name order.

Usage: python3 video/tools/assemble_script.py [lesson_id]
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
lid = sys.argv[1] if len(sys.argv) > 1 else "nasb"
d = ROOT / "video" / "lessons" / lid
segs = []
for p in sorted((d / "parts").glob("p*.json")):
    segs += json.loads(p.read_text(encoding="utf-8"))["segments"]
ids = [s["id"] for s in segs]
dups = {i for i in ids if ids.count(i) > 1}
if dups:
    sys.exit(f"duplicate ids: {sorted(dups)}")
scenes = list(dict.fromkeys(s["scene"] for s in segs))
(d / "script.json").write_text(json.dumps(dict(lesson=lid, scenes=scenes, segments=segs), ensure_ascii=False, indent=1),
                               encoding="utf-8")
print(f"script.json: {len(scenes)} scenes, {len(segs)} segments "
      f"({sum(s['lang'] == 'ar' for s in segs)} Arabic)")
