#!/usr/bin/env python3
"""Export the Stage 3 lesson "Particles" (id s3-particles) to video/lessons/s3-particles/lesson.json.

Source: content/stage3/u7_particles.py (its `notes` blocks are the lesson page). Each block is rendered with
the site's own renderer (content/course.py render_notes), so the video reuses the site's markup and CSS.
Nothing is typed by hand.

The blocks are grouped into scenes: a chapter title (h2, with the paragraph right after it as its grey
sub-line) and then one scene per block (rule, tip, cols, table, examples, summary). Scene ids are
`c<NN>-<kind>` (a second block of the same kind in a chapter gets `-2`), `hero` and `summary`.

Usage: python3 video/tools/export_s3_particles.py
"""
import json, runpy, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = "content/stage3/u7_particles.py"
OUT = ROOT / "video" / "lessons" / "s3-particles" / "lesson.json"
sys.path.insert(0, str(ROOT / "content"))
import os  # noqa: E402
_cwd = os.getcwd(); os.chdir(ROOT / "content")
try:
    import course as C  # noqa: E402
finally:
    os.chdir(_cwd)
import lesson as L  # noqa: E402

U = runpy.run_path(str(ROOT / SRC))["UNIT"]
blocks, scenes = [], []
ch = 0
for i, b in enumerate(U["notes"]):
    t = b["t"]
    if t == "h2":
        ch += 1
        html = f'<h2><span class="num">{ch}</span>{C.tx(b["text"])}</h2>'
    else:
        html = C.render_notes([b])
    blocks.append(dict(i=i, t=t, chapter=ch, data=b, html=html))
    if t == "hero":
        scenes.append(dict(id="hero", kind="hero", blocks=[i]))
    elif t == "h2":
        scenes.append(dict(id=f"c{ch:02d}-title", kind="chapter", chapter=ch, blocks=[i]))
    elif t == "p" and scenes and scenes[-1]["kind"] == "chapter" and len(scenes[-1]["blocks"]) == 1:
        scenes[-1]["blocks"].append(i)          # the paragraph under a heading is the chapter's sub-line
    elif t == "summary":
        scenes.append(dict(id="summary", kind="summary", chapter=ch, blocks=[i]))
    else:
        base = f"c{ch:02d}-{t}"
        n = sum(1 for s in scenes if s["id"] == base or s["id"].startswith(base + "-"))
        scenes.append(dict(id=base if n == 0 else f"{base}-{n + 1}", kind=t, chapter=ch, blocks=[i]))

sections = [dict(num=b["chapter"], title=C.tx(b["data"]["text"]), sub=None) for b in blocks if b["t"] == "h2"]

data = dict(
    id=U["id"], stage=3, title=U["title"], ar_title=U["ar"], blurb=U["blurb"],
    sources=[SRC],
    tabs=["Lesson", "Practice"],
    roles={k: dict(en=x[0], ar=x[1], border=x[2], bg=x[3], text=x[4], short=x[5]) for k, x in L.R.items()},
    hero_html=blocks[0]["html"],
    sections=sections,
    blocks=blocks,
    scenes=scenes,
)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}: {len(blocks)} blocks, {len(sections)} chapters, {len(scenes)} scenes")
for s in scenes:
    print(f"  {s['id']:14s} {s['kind']:9s} blocks {s['blocks']}")
