#!/usr/bin/env python3
"""Export the Stage 3 unit "Question words" (id s3-questions) to video/lessons/s3-questions/lesson.json.

Source: content/stage3/u5_questions.py (UNIT["notes"] is the lesson page). Every block is rendered with the
site's own renderer (content/course.py render_notes), so the video reuses the page's markup and CSS.
Nothing is typed by hand.

Usage: python3 video/tools/export_s3_pronouns.py
"""
import json, os, re, runpy, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = "content/stage3/u5_questions.py"
OUT = ROOT / "video" / "lessons" / "s3-questions" / "lesson.json"
sys.path.insert(0, str(ROOT / "content"))
cwd = os.getcwd(); os.chdir(ROOT / "content")
try:
    import course as C  # noqa: E402  (render_notes, the site's Stage 0/3 note renderer)
finally:
    os.chdir(cwd)

U = runpy.run_path(str(ROOT / SRC))["UNIT"]
assert U["id"] == "s3-questions"

blocks, sections, hero_html, n = [], [], None, 0
for i, b in enumerate(U["notes"]):
    h = C.render_notes([b])
    if b["t"] == "h2":
        n += 1
        h = h.replace('<span class="num">1</span>', f'<span class="num">{n}</span>', 1)
        sections.append(dict(num=n, title=C.tx(b["text"]), title_text=b["text"], sub=None, blocks=[]))
    elif b["t"] == "hero":
        hero_html = h
    elif sections:
        sections[-1]["blocks"].append(i)
    blocks.append(dict(i=i, t=b["t"], section=n or None, html=h, src=b))

data = dict(
    id=U["id"], stage=3, title=U["title"], ar_title=U["ar"], blurb=U["blurb"],
    tabs=["Lesson", "Practice"],
    sources=[SRC],
    roles={},
    hero_html=hero_html,
    sections=sections,
    blocks=blocks,
    practice_cards=[dict(n=f"P{k}", title=c["title"]) for k, c in enumerate(U["practice"], 1)],
    homework_cards=[dict(n=f"H{k}", title=c["title"]) for k, c in enumerate(U.get("homework", []), 1)],
)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}: {len(blocks)} blocks, {len(sections)} sections, "
      f"{len(data['practice_cards'])} practice + {len(data['homework_cards'])} homework cards")
for b in blocks:
    print(f'  {b["i"]:2d} s{b["section"] or 0} {b["t"]:8s} {re.sub("<[^>]+>", " ", b["html"])[:90]}')
