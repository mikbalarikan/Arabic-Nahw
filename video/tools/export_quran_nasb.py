#!/usr/bin/env python3
"""Export the lesson "Iʿrāb in the Qur'an" (id quran-nasb) to video/lessons/quran-nasb/lesson.json.

Source: content/quran.py (QN.build(), QN.VERSES, QN.key) and the Arabic title in content/course.py.
Nothing is typed by hand. The site's own HTML fragments are kept, so the video reuses its markup and CSS.

Usage: python3 video/tools/export_quran_nasb.py
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "video" / "lessons" / "quran-nasb" / "lesson.json"
sys.path.insert(0, str(ROOT / "content"))
import lesson as L  # noqa: E402
import quran as QN  # noqa: E402  (importing quran also patches L.word_html for fixed owners)

full = QN.build()
YOUR_TURN = f'<div class="pb">{L.h2(4, "Your turn", "nomt")}</div>'
intro = full[:full.index(YOUR_TURN)]

# ---- split the intro into hero + numbered chapters
H2 = re.compile(r'<h2 class="[^"]*"><span class="num">(\d+)</span>(.*?)</h2>', re.S)
marks = list(H2.finditer(intro))
hero_html = intro[:marks[0].start()].strip()
sections = []
for i, m in enumerate(marks):
    end = marks[i + 1].start() if i + 1 < len(marks) else len(intro)
    body = intro[m.end():end].strip()
    sub = re.search(r'<p class="sub">(.*?)</p>', body, re.S)
    sections.append(dict(num=int(m.group(1)), title=m.group(2), sub=sub.group(1) if sub else None, html=body))

# ---- chapter 1 pieces: three note cards and the "Also" tip
s1 = sections[0]["html"]
notes = re.findall(r'<div class="rr".*?</p></div>', s1, re.S)
also = re.search(r'<div class="tipbox">.*?</div>', s1, re.S).group(0)
overview = re.search(r'<table class="glance vt">.*?</table>', sections[2]["html"], re.S).group(0)

# ---- the 10 verses
verses = []
for i, v in enumerate(QN.VERSES, 1):
    shown = [w for g in v["g"] for w in g["ws"] if w["k"] != "hidden"]
    pieces = [w["t"] for w in shown]                      # every piece, as boxed (رَبَّـ | ـهُ)
    words = QN.join(pieces)                               # as written (رَبَّهُ), the overview's text
    key_html = QN.key(i, v)
    key_lines = re.findall(r'<div class="rl">.*?</span></div>', key_html, re.S)
    hidden = [w["t"] for g in v["g"] for w in g["ws"] if w["k"] == "hidden"]
    verses.append(dict(
        num=str(i), ref_ar=v["ref"], ref_en=v["en"], tr=v["tr"], groups=v["g"],
        sentence=" ".join(words), words=words, pieces=pieces,
        hidden_doer=hidden[0] if hidden else None,
        jobs=QN.jobs_of(v),
        boxes_html=L.boxes(v["g"]),
        key_lines=key_lines,
        key_lines_text=[re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", l)).strip() for l in key_lines],
        key_html=key_html,
        card_html=QN.card(i, v),
    ))

course_src = (ROOT / "content" / "course.py").read_text(encoding="utf-8")
t = re.search(r'id="quran-nasb",\s*stage=2,\s*title="([^"]+)",\s*ar="([^"]+)"', course_src)

data = dict(
    id="quran-nasb", stage=2, title=t.group(1), ar_title=t.group(2),
    tabs=["Intro", "Verses"],
    roles={k: dict(en=x[0], ar=x[1], border=x[2], bg=x[3], text=x[4], short=x[5]) for k, x in L.R.items()},
    hero_html=hero_html,
    sections=sections,
    notes=notes, also=also, overview=overview,
    fragments=dict(colour_key=L.colour_key()),
    verses=verses,
    your_turn_heading=YOUR_TURN,
)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}: {len(sections)} chapters, {len(notes)} notes, {len(verses)} verses, "
      f"{sum(len(v['key_lines']) for v in verses)} key lines")
