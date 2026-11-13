#!/usr/bin/env python3
"""Export the Stage 3 lesson "Pointing words" (id s3-demonstratives) to video/lessons/s3-demonstratives/lesson.json.

Source: content/stage3/u3_demonstratives.py (UNIT["notes"], the lesson page) rendered with the site's own
course.render_notes(), one block at a time, so the video reuses the site's markup and CSS. Nothing is typed by hand.

Usage: python3 video/tools/export_s3_demonstratives.py
"""
import json, os, re, runpy, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = "content/stage3/u3_demonstratives.py"
OUT = ROOT / "video" / "lessons" / "s3-demonstratives" / "lesson.json"
sys.path.insert(0, str(ROOT / "content"))
cwd = os.getcwd(); os.chdir(ROOT / "content")
try:
    import course  # noqa: E402  (render_notes, as tools/build_site.py uses it)
finally:
    os.chdir(cwd)

U = runpy.run_path(str(ROOT / SRC))["UNIT"]
plain = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).replace("&quot;", '"').replace("&#x27;", "'").strip()

hero, sections, cur = None, [], None
for i, b in enumerate(U["notes"]):
    html = course.render_notes([b])
    if b["t"] == "hero":
        hero = html
        continue
    if b["t"] == "h2":
        cur = dict(num=len(sections) + 1, title=course.tx(b["text"]), title_text=b["text"], blocks=[])
        sections.append(cur)
        continue
    cur["blocks"].append(dict(i=i, t=b["t"], src=b, html=html, text=plain(html)))

data = dict(
    id=U["id"], stage=3, title=U["title"], ar_title=U["ar"], blurb=U["blurb"],
    tabs=["Lesson", "Practice"],
    sources=[SRC],
    roles={},
    hero=U["notes"][0], hero_html=hero,
    sections=sections,
    practice_cards=[dict(n=f"P{k}", title=c["title"], rows=len(c["rows"])) for k, c in enumerate(U["practice"], 1)],
    homework_cards=[dict(n=f"H{k}", title=c["title"], rows=len(c["rows"])) for k, c in enumerate(U.get("homework", []), 1)],
)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}: {len(sections)} chapters, "
      f"{sum(len(s['blocks']) for s in sections)} blocks, {len(data['practice_cards'])} practice cards")
