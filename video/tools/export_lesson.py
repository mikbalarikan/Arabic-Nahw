#!/usr/bin/env python3
"""Export the Naṣb lesson (content/lesson.py) to video/lessons/nasb/lesson.json.

Nothing here is typed by hand: every Arabic string, colour and English line comes from
content/lesson.py (and the Arabic title from content/course.py). The lesson's own HTML
fragments are kept as well, so the video can reuse the site's markup and CSS exactly.

Usage: python3 video/tools/export_lesson.py
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "video" / "lessons" / "nasb" / "lesson.json"
sys.path.insert(0, str(ROOT / "content"))
import lesson as L  # noqa: E402

# ---- capture every example() call while lesson() runs ----
captured = []
_orig = L.example
def _capture(num, en, groups, lines, tip=None):
    html = _orig(num, en, groups, lines, tip)
    words = [w["t"] for g in groups for w in g["ws"] if w["k"] != "hidden"]
    captured.append(dict(
        num=str(num), en=en, groups=groups,
        lines=[dict(role=r, text=t) for r, t in lines], tip=tip,
        sentence=" ".join(words),
        hidden_doer=any(w["k"] == "hidden" for g in groups for w in g["ws"]),
        html=html))
    return html
L.example = _capture
lesson_html = L.lesson()
L.example = _orig

# ---- split the lesson HTML into its chapters (by the numbered h2 headings) ----
H2 = re.compile(r'<h2 class="[^"]*"><span class="num">(\d+)</span>(.*?)</h2>', re.S)
marks = list(H2.finditer(lesson_html))
hero_html = lesson_html[:marks[0].start()].strip()
sections = []
for i, m in enumerate(marks):
    end = marks[i + 1].start() if i + 1 < len(marks) else len(lesson_html)
    body = lesson_html[m.end():end].strip()
    sub = re.search(r'<p class="sub">(.*?)</p>', body, re.S)
    nums = [x["num"] for x in captured if x["html"] in body]
    sections.append(dict(num=int(m.group(1)), title=m.group(2), sub=sub.group(1) if sub else None,
                         examples=nums, html=body))

# ---- Arabic title from course.py (id="nasb") ----
course_src = (ROOT / "content" / "course.py").read_text(encoding="utf-8")
t = re.search(r'id="nasb",\s*stage=2,\s*title="([^"]+)",\s*ar="([^"]+)"', course_src)

data = dict(
    id="nasb", stage=2, title=t.group(1), ar_title=t.group(2),
    roles={k: dict(en=v[0], ar=v[1], border=v[2], bg=v[3], text=v[4], short=v[5]) for k, v in L.R.items()},
    nasb_roles=L.NASB,
    hero_html=hero_html,
    sections=sections,
    examples=[{k: v for k, v in x.items()} for x in captured],
    practice=[dict(en=p["en"], groups=p["g"],
                   sentence=" ".join(w["t"] for g in p["g"] for w in g["ws"] if w["k"] != "hidden"),
                   stems=[L.stem(w) for w in L.flat(p["g"])])
              for p in L.PRACTICE],
    practice_heading=re.search(r'<h2 class="nomt">.*?</h2><p class="sub">.*?</p>', L.practice(), re.S).group(0),
    fragments=dict(cases=L.cases(), sign_rules=L.sign_rules(), colour_key=L.colour_key(), glance=L.glance()),
)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
tips = sum(1 for x in captured if x["tip"])
print(f"wrote {OUT.relative_to(ROOT)}: {len(sections)} chapters, {len(captured)} examples, {tips} example tips, "
      f"{len(data['practice'])} practice sentences")
