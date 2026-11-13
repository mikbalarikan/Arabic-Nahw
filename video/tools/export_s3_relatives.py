#!/usr/bin/env python3
"""Export the lesson "Relative pronouns" (id s3-relatives) to video/lessons/s3-relatives/lesson.json.

Source: content/stage3/u4_relatives.py (UNIT["notes"]), rendered block by block with the site's own
course.render_notes(), so the video reuses the lesson page's markup and CSS. Nothing is typed by hand.

Each block keeps its raw source fields (for the script writers) and its HTML. h2 blocks get the running
chapter number the lesson page shows.

Usage: python3 video/tools/export_s3_relatives.py
"""
import json, os, re, runpy, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = "content/stage3/u4_relatives.py"
OUT = ROOT / "video" / "lessons" / "s3-relatives" / "lesson.json"
sys.path.insert(0, str(ROOT / "content"))
cwd = os.getcwd(); os.chdir(ROOT / "content")
try:
    import course  # noqa: E402
finally:
    os.chdir(cwd)

U = runpy.run_path(str(ROOT / SRC))["UNIT"]

blocks, chapters, n = [], [], 0
for i, b in enumerate(U["notes"]):
    h = course.render_notes([b])
    if b["t"] == "h2":
        n += 1
        h = h.replace('<span class="num">1</span>', f'<span class="num">{n}</span>', 1)
        chapters.append(dict(num=n, title=b["text"], title_html=re.sub(r"^<h2>|</h2>$", "", h), block=i))
    blocks.append(dict(i=i, t=b["t"], chapter=n, html=h, src=b))

assert sum(1 for b in blocks if b["t"] == "h2") == len(chapters)

data = dict(
    id=U["id"], stage=3, title=U["title"], ar_title=U["ar"], blurb=U["blurb"],
    tabs=["Lesson", "Practice"],
    sources=[SRC],
    hero_html=blocks[0]["html"],
    chapters=chapters,
    blocks=blocks,
    practice_count=len(U["practice"]),
)
# the full page must be exactly the blocks joined (same renderer, same order)
full = course.render_notes(U["notes"])
assert full == "".join(b["html"] for b in blocks), "block split does not match the lesson page"

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}: {len(blocks)} blocks, {len(chapters)} chapters, "
      f"{sum(len(b['src'].get('items', [])) for b in blocks if b['t'] == 'examples')} examples")
