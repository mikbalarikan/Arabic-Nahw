#!/usr/bin/env python3
"""Export the Stage 3 lesson "Fixed verbs: past and order" (id s3-verbs) to video/lessons/s3-verbs/lesson.json.

Source: content/stage3/u6_verbs.py (its `notes` blocks are the lesson page). Nothing is typed by hand.
Every block keeps its raw data and the site's own HTML (course.render_notes), so the video reuses the
site's markup and CSS. Blocks are grouped into chapters by their h2 headings (chapter 0 = the hero).

Usage: python3 video/tools/export_s3_verbs.py
"""
import json, re, runpy, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = "content/stage3/u6_verbs.py"
OUT = ROOT / "video" / "lessons" / "s3-verbs" / "lesson.json"
sys.path.insert(0, str(ROOT / "content"))
import course as C  # noqa: E402
import lesson as L  # noqa: E402

U = runpy.run_path(str(ROOT / SRC))["UNIT"]


def plain(s):
    """Visible text of a {Arabic}-marked string."""
    return re.sub(r"[{}]", "", s or "")


chapters, cur = [], None
for b in U["notes"]:
    if b["t"] == "hero":
        cur = dict(num=0, title=None, blocks=[])
        chapters.append(cur)
    elif b["t"] == "h2":
        cur = dict(num=len(chapters), title=b["text"], title_html=C.tx(b["text"]), blocks=[])
        chapters.append(cur)
        continue
    html = C.render_notes([b])
    cur["blocks"].append(dict(t=b["t"], data=b, html=html))

# the Arabic words / sentences the video may read aloud, straight from the blocks
sentences = []
for ch in chapters:
    for blk in ch["blocks"]:
        b = blk["data"]
        if b["t"] == "examples":
            sentences += [dict(sentence=it["ar"]) for it in b["items"]]
        if b["t"] == "table":
            for r in b["rows"]:
                sentences += [dict(sentence=c) for c in r if re.search(r"[؀-ۿ]", c) and not re.search(r"[A-Za-z{]", c)]

data = dict(
    id=U["id"], stage=3, title=U["title"], ar_title=U["ar"], blurb=U["blurb"],
    sources=[SRC],
    tabs=["Lesson", "Practice"],
    roles={k: dict(en=x[0], ar=x[1], border=x[2], bg=x[3], text=x[4], short=x[5]) for k, x in L.R.items()},
    chapters=chapters,
    examples=sentences,   # check_arabic.py reads `examples[].sentence`
    practice_titles=[p["title"] for p in U["practice"]],
)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}: {len(chapters) - 1} chapters, "
      f"{sum(len(c['blocks']) for c in chapters)} blocks, {len(sentences)} readable Arabic strings")
for c in chapters:
    print(f"  {c['num']:2d} {c['title'] or '(hero)'}: " + ", ".join(b["t"] for b in c["blocks"]))
