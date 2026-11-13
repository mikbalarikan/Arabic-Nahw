#!/usr/bin/env python3
"""Export the Stage 3 unit "Attached pronouns" (id s3-attached) to video/lessons/s3-attached/lesson.json.

Source: content/stage3/u2_attached.py (its `notes` blocks are the lesson page). Every block keeps its raw
data and the site's own HTML (course.render_notes), so the video reuses the site's markup and CSS.
Nothing is typed by hand.

Usage: python3 video/tools/export_s3_attached.py
"""
import json, re, runpy, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "content" / "stage3" / "u2_attached.py"
OUT = ROOT / "video" / "lessons" / "s3-attached" / "lesson.json"
sys.path.insert(0, str(ROOT / "content"))
import course as C  # noqa: E402

U = runpy.run_path(str(SRC))["UNIT"]
blocks, n = [], 0
for i, b in enumerate(U["notes"]):
    h = C.render_notes([b])
    if b["t"] == "h2":
        n += 1
        h = h.replace('<span class="num">1</span>', f'<span class="num">{n}</span>', 1)
    blocks.append(dict(i=i, t=b["t"], chapter=n, html=h, src=b))

# the whole page, exactly as the site renders it (for reference and checks)
page = C.render_notes(U["notes"])
assert "".join(b["html"] for b in blocks) == page, "per-block HTML differs from the site's page"

data = dict(
    id=U["id"], stage=3, title=U["title"], ar_title=U["ar"], blurb=U["blurb"],
    tabs=["Lesson", "Practice"],
    source=str(SRC.relative_to(ROOT)),
    sources=[str(SRC.relative_to(ROOT))],   # check_arabic.py allows the Arabic of these files
    hero_html=blocks[0]["html"],
    chapters={b["chapter"]: re.sub(r"<.*?>", "", b["html"].split("</span>", 1)[1]) for b in blocks if b["t"] == "h2"},
    blocks=blocks,
    page_html=page,
)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}: {len(blocks)} blocks, {n} chapters")
