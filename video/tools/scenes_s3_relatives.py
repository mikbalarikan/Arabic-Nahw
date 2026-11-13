"""Scenes for the lesson video "Relative pronouns" (lesson id s3-relatives, Stage 3 unit 4).

Loaded by build_composition.py (lesson_for). Every block's markup comes from lesson.json, i.e. from
content/stage3/u4_relatives.py rendered by the site's own course.render_notes(), and is styled by the site's
CSS. This file only adds the 1920x1080 sizes and the cue animations.
Scene ids and cues: video/lessons/s3-relatives/SCRIPT_SPEC.md.
"""
import re

import build_composition as BC

# scene id -> (kind, lesson.json block indices). Chapter title scenes take the chapter's opening paragraph
# as their grey sub-line.
SCENES = {
    "hero": ("hero", [0]),
    "c01-title": ("chapter", [1]),
    "c01-table": ("table", [2]),
    "c01-cols": ("cols", [3]),
    "c01-tip": ("box", [4]),
    "c01-rule": ("box", [5]),
    "c02-title": ("chapter", [6, 7]),
    "c02-ex": ("examples", [8]),
    "c02-tip": ("box", [9]),
    "c03-title": ("chapter", [10, 11]),
    "c03-ex": ("examples", [12]),
    "c03-tips": ("boxes", [13, 14]),
    "c04-title": ("chapter", [15, 16]),
    "c04-ex": ("examples", [17]),
    "c05-title": ("chapter", [18, 19]),
    "c05-ex": ("examples", [20]),
    "c05-tip": ("box", [21]),
    "c06-title": ("chapter", [22]),
    "c06-forms": ("boxes", [23, 24]),
    "summary": ("summary", [25]),
}

AR = "؀-ۿ"

CSS = r"""
/* every Arabic item a cue can light up (ar:<n>) */
/* the glow is a band inside the text's own line (Noto Sans Arabic's line box is much taller than the letters),
   so it never spills into the row, card or line around it. --g (0..1) is tweened by the ar cue. */
.arit { --g: 0; border-radius: 4px; background-repeat: no-repeat;
  background-image: linear-gradient(transparent 22%, rgba(245,200,75,calc(var(--g) * .5)) 22%, rgba(245,200,75,calc(var(--g) * .5)) 86%, transparent 86%); }
/* on the dark "In short" panel a see-through gold turns olive (the course's colour for "state"): use a solid gold bar under the word */
.k-summary .arit { background-image: linear-gradient(transparent 84%, rgba(245,200,75,var(--g)) 84%, rgba(245,200,75,var(--g)) 93%, transparent 93%); }
/* the dual table: centre the Arabic cells under their headers */
.k-boxes .s0t th:not(:first-child), .k-boxes .s0t td.tar { text-align: center; }
.kkar, .wm, .arh { font-family: var(--arabic); }
/* poster: the hero's watermark (with its shadda) fits inside the short hero */
.thumb .hero .wm { font-size: 76px; top: 2px; line-height: 1.5; }
.hl { background-image: linear-gradient(transparent 58%, rgba(245,200,75,.75) 58%); background-repeat: no-repeat; background-size: 0% 100%; }

/* chapter title with the chapter's opening paragraph */
.k-chapter .stagebody > .view { max-width: 720px; }
.k-chapter .sub { color: var(--muted); }
.k-chapter .sub .ab { color: var(--ink); }
.k-chapter h2 .arh { font-size: 1.12em; }

/* the table to learn, and the dual table */
.k-table .stagebody > .view:last-child { --z: 1.95; width: 880px; margin-top: 36px; }
.k-table .tblwrap { margin: 0; overflow: visible; }
.k-table table.s0t { font-size: 15px; }
.k-table .s0t th { font-size: 13px; padding: 9px 14px; }
.k-table .s0t td { padding: 8px 14px; vertical-align: middle; }
.k-table .s0t td.tar { font-size: 24px; white-space: nowrap; }
.k-table .s0t td .ab { font-size: 1.3em; }

/* two "General" cards */
.k-cols .stagebody > .view:last-child { --z: 2.05; width: 860px; margin-top: 40px; }
.k-cols .kk { padding: 16px 18px; }
.k-cols .kkt { font-size: 17px; align-items: center; }
.k-cols .kkar { font-size: 30px; line-height: 1.5; }
.k-cols .kkd { font-size: 15px; line-height: 1.9; margin-top: 6px; }
.k-cols .kkd .ab { font-size: 1.35em; }

/* one tip or rule box */
.k-box .stagebody > .view:last-child { --z: 2.25; width: 720px; margin-top: 40px; }
.k-box .tipbox, .k-box .rbox { font-size: 16px; line-height: 1.85; padding: 18px 22px; margin: 0; }
.k-box .ab { font-size: 1.3em; }

/* two boxes (two tips; the dual rule and its table) */
.k-boxes .stagebody > .view:last-child { --z: 2.0; width: 780px; margin-top: 56px; display: flex; flex-direction: column; gap: 16px; }
.k-boxes .tipbox, .k-boxes .rbox { font-size: 15px; line-height: 1.8; padding: 15px 20px; margin: 0; }
.k-boxes .ab { font-size: 1.3em; }
.k-boxes .tblwrap { margin: 0; overflow: visible; }
.k-boxes table.s0t { font-size: 15px; }
.k-boxes .s0t th { font-size: 13px; padding: 8px 14px; }
.k-boxes .s0t td { padding: 6px 14px; vertical-align: middle; }
.k-boxes .s0t td.tar { font-size: 26px; }

/* example lists */
.k-examples .stagebody > .view:last-child { --z: 1.9; width: 900px; margin-top: 60px; }
.k-examples .exlist { margin: 0; gap: 9px; }
.k-examples .exl { padding: 8px 18px; grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); gap: 18px; }
.k-examples .exa { font-size: 27px; line-height: 1.75; }
.k-examples .exe { font-size: 15px; }
.k-examples .exn { font-size: 13.5px; margin-top: 3px; color: #5f6672; }
.k-examples .exn .ab { font-size: 1.25em; color: var(--ink); }

/* In short */
.k-summary .stagebody > .view:last-child { --z: 1.95; width: 860px; }
.k-summary .three { margin: 0; padding: 26px 34px 24px; }
.k-summary .three h3 { font-size: 21px; }
.k-summary .three ol { font-size: 15.5px; line-height: 2.2; }
.k-summary .three .ab { font-size: 1.3em; }
"""

HIDE = {
    "table": ["table.s0t tr:not(:first-child)"],
    "cols": [".kk"],
    "box": [".stagebody > .view:last-child > *"],
    "boxes": [".stagebody > .view:last-child > *"],
    "examples": [".exl", ".exn"],
    "summary": [".three li"],
}

# the Arabic items of a block, in page order: inline {Arabic} (bdi.ab), the cards' big word (.kkar),
# an example sentence (.exa) and an Arabic-only table cell without inline markup (td.tar)
ITEM = re.compile(r'<bdi class="ab">.*?</bdi>|<span class="kkar">.*?</span>|<div class="exa" dir="rtl">.*?</div>'
                  r'|<td class="tar">[^<]*</td>', re.S)


def number_items(html, start=0):
    n = [start]

    def one(m):
        s, k = m.group(0), n[0]
        n[0] += 1
        if s.startswith("<bdi"):
            return s.replace('<bdi class="ab">', f'<bdi class="ab arit ar{k}">', 1)
        if s.startswith('<span class="kkar">'):
            return s.replace('<span class="kkar">', f'<span data-layout-allow-overflow class="kkar arit ar{k}">', 1)
        if s.startswith("<div class=\"exa\""):
            inner = s[len('<div class="exa" dir="rtl">'):-len("</div>")]
            return f'<div class="exa" dir="rtl"><span class="arit ar{k}">{inner}</span></div>'
        inner = s[len('<td class="tar">'):-len("</td>")]
        return f'<td class="tar"><span class="arit ar{k}">{inner}</span></td>'
    return ITEM.sub(one, html), n[0]


def ar_heading(title_html, start=0):
    """Arabic words written straight into a chapter heading (no {} markup): give them an item number too."""
    n = [start]

    def one(m):
        k = n[0]; n[0] += 1
        return f'<span data-layout-allow-overflow class="arh arit ar{k}">{m.group(0)}</span>'
    return re.sub(f"[{AR}]+(?: [{AR}]+)*", one, title_html), n[0]


class SceneLesson(BC.Lesson):
    css = CSS
    hide = HIDE

    def __init__(self, data):
        self.d = data
        self.R = {}
        self.ex = {}
        self.blocks = data["blocks"]
        self.chap = {c["num"]: c for c in data["chapters"]}

    def chapter_of(self, scene):
        m = re.match(r"c(\d\d)-", scene)
        return int(m.group(1)) if m else None

    def h2(self, n, items=True):
        """The chapter heading. With items=False (the small heading over a content scene) its Arabic gets the
        Arabic font but no item number: there, the numbers belong to the scene's blocks."""
        t, k = ar_heading(self.chap[n]["title_html"])
        if not items:
            t = re.sub(r' arit ar\d+', "", t)
        # h2 is a flex row: keep the title text in one item, so its Arabic words do not become gapped flex items
        t = re.sub(r'^(<span class="num">\d+</span>)(.*)$', r'\1<span class="h2t">\2</span>', t, flags=re.S)
        return f"<h2>{t}</h2>", k

    def chapter_name(self, scene, kind):
        if scene == "hero":
            return "Introduction"
        if kind == "chapter":
            c = self.chap[self.chapter_of(scene)]
            return f'{c["num"]} {c["title"]}'
        if scene == "summary":
            return "In short"
        return None

    def thumbnail_html(self):
        """Poster: the lesson hero over "The table to learn"."""
        return self.blocks[2]["html"]

    def items(self, scene):
        """Numbered Arabic items of a scene, as shown (for SCRIPT_SPEC.md)."""
        kind, inner = self.body(scene, [])
        inner = self.prep(scene, kind, inner)
        out = {}
        for m in re.finditer(r'class="[^"]*\barit ar(\d+)"[^>]*>(.*?)</(?:bdi|span)>', inner, re.S):
            out[int(m.group(1))] = re.sub(r"<[^>]+>", "", m.group(2))
        return [out[k] for k in sorted(out)]

    def body(self, scene, segs):
        if scene not in SCENES:
            raise SystemExit(f"no renderer for scene {scene}")
        kind, idx = SCENES[scene]
        ch = self.chapter_of(scene)
        if kind == "hero":
            return "hero", f'<div class="view">{self.d["hero_html"]}</div>'
        if kind == "chapter":
            h, _ = self.h2(ch)
            sub = ""
            if len(idx) > 1:
                p = self.blocks[idx[1]]
                assert p["t"] == "p"
                sub = '<p class="sub">' + re.sub(r'^<p class="s0p">|</p>$', "", p["html"]) + "</p>"
            return "chapter", f'<div class="view chap">{h}{sub}</div>'
        head = f'<div class="view chead">{self.h2(ch, items=False)[0]}</div>' if ch else ""
        inner = "".join(self.blocks[i]["html"] for i in idx)
        for n, phrase in enumerate(hl for s in segs for hl in s["cues"] if hl.startswith("hl:")):
            inner = BC.wrap_phrase(inner, phrase[3:], f"hl{n}")
        return kind, head + f'<div class="view">{inner}</div>'

    def prep(self, scene, kind, inner):
        if kind == "hero":
            return inner
        # the chapter heading at the top of a content scene is not numbered: items belong to the block(s)
        k = inner.find('<div class="view">') if kind != "chapter" else 0
        head, rest = inner[:k], inner[k:]
        if kind == "chapter":
            n = len(re.findall(r"\barit ar\d+", rest))   # the heading's own Arabic comes first
            pre, sep, sub = rest.partition('<p class="sub">')
            return pre + sep + number_items(sub, n)[0] if sep else rest
        rest, _ = number_items(rest)
        # Noto Sans Arabic's glyph boxes are taller than the site's line boxes; nothing visible overflows
        rest = rest.replace('<div class="exa"', '<div data-layout-allow-overflow class="exa"')
        rest = rest.replace('<td class="tar"', '<td data-layout-allow-overflow class="tar"')
        return head + rest

    def cue(self, tl, scene, kind, S, name, arg, t, seg_len, state):
        V = f"{S} .stagebody > .view:last-child"
        if name == "ar":
            sel = f"{S} .ar{int(arg)}"
            tl.add(f'tl.to("{sel}", {{"--g":1, duration:0.25, ease:"power1.out"}}, {t:.3f});')
            tl.add(f'tl.to("{sel}", {{"--g":0, duration:0.3, ease:"power1.in"}}, {t + max(seg_len, 0.6) + 0.1:.3f});')
            return True
        if name == "row":
            tl.fade_up(f"{S} table.s0t tr:nth-child({int(arg) + 1})", t, 8)
            return True
        if name == "col":
            tl.fade_up(f"{S} .kk:nth-child({int(arg)})", t, 16, 0.42)
            return True
        if name == "ex":
            tl.fade_up(f"{S} .exl:nth-child({int(arg)})", t, 10)
            return True
        if name == "note":
            tl.fade_in(f"{S} .exl:nth-child({int(arg)}) .exn", t)
            return True
        if name == "li":
            tl.fade_up(f"{S} .three li:nth-child({int(arg)})", t, 10)
            return True
        if name == "show":
            tl.fade_up(f"{V} > *:nth-child({int(arg) if arg else 1})", t)
            return True
        if name == "practice":
            tl.add(f'tl.to("{S} .vbar .tab:nth-child(1)", {{backgroundColor:"rgba(0,0,0,0)", borderColor:"rgba(255,255,255,.25)", color:"#e6f0f0", duration:0.4}}, {t:.3f});')
            tl.add(f'tl.to("{S} .vbar .tab:nth-child(2)", {{backgroundColor:"#f5c84b", borderColor:"#f5c84b", color:"#1f2430", duration:0.4}}, {t:.3f});')
            return True
        return False  # title, sub, hl: the shared cues
