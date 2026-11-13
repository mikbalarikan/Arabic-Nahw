"""Scenes for the lesson video "Attached pronouns" (Stage 3 unit 2, lesson id s3-attached).

Loaded by build_composition.py (lesson_for). Every scene shows blocks of the lesson page exactly as the site
renders them (lesson.json, made by export_s3_attached.py from content/stage3/u2_attached.py) and styled by the
site's CSS. This file only adds the 1920x1080 sizes and the cue animations.
Scene ids and cues: video/lessons/s3-attached/SCRIPT_SPEC.md.
"""
import html, re

import build_composition as BC

# scene id -> (kind, lesson block indices shown in the scene, view width px, zoom)
SCENES = {
    "hero":        ("hero", [0], None, None),
    "c01-title":   ("chapter", [1], None, None),
    "c01-intro":   ("page", [2], 760, 2.15),
    "c01-table":   ("page", [3], 860, 1.42),
    "c01-tip":     ("page", [4], 760, 2.1),
    "c02-title":   ("chapter", [5], None, None),
    "c02-owner":   ("page", [6, 7], 900, 1.75),
    "c02-rule":    ("page", [8], 760, 2.15),
    "c02-endings": ("page", [9, 10], 900, 1.75),
    "c02-tip":     ("page", [11], 760, 2.15),
    "c03-title":   ("chapter", [12], None, None),
    "c03-hidden":  ("page", [13, 14], 900, 1.85),
    "c03-rule":    ("page", [15], 760, 2.15),
    "c04-title":   ("chapter", [16], None, None),
    "c04-prep":    ("page", [17, 18], 900, 1.75),
    "c04-forms":   ("page", [19, 20], 820, 1.7),
    "c04-rule":    ("page", [21], 780, 2.1),
    "c05-title":   ("chapter", [22], None, None),
    "c05-rule":    ("page", [23], 780, 2.1),
    "c05-ex":      ("page", [24, 25], 900, 1.8),
    "c05-tip":     ("page", [26], 760, 2.15),
    "c06-title":   ("chapter", [27], None, None),
    "c06-intro":   ("page", [28], 780, 2.1),
    "c06-ex":      ("page", [29], 900, 1.6),
    "c06-tips":    ("page", [30, 31], 780, 2.0),
    "c07-title":   ("chapter", [32], None, None),
    "c07-table":   ("page", [33], 900, 1.75),
    "c07-summary": ("page", [34], 900, 1.65),
}

CSS = r"""
/* page scenes: blocks of the lesson page, one under the other */
.k-page .stagebody > .view:last-child { zoom: var(--z, 1.8); margin-top: calc(60px / var(--z, 1.8)); }
.k-page .blk + .blk { margin-top: 14px; }
.k-page .blk > * { margin-top: 0 !important; margin-bottom: 0 !important; }
.k-page .s0p { max-width: none; font-size: 16px; line-height: 1.9; }
.k-page .rbox { font-size: 16px; line-height: 2.0; padding: 16px 20px; }
.k-page .tipbox { font-size: 15.5px; line-height: 2.0; padding: 16px 20px; }
.k-page .ab { font-size: 1.22em; }
.k-page .exlist { gap: 10px; }
.k-page .exl { padding: 10px 18px; grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr); }
.k-page .exa { font-size: 30px; line-height: 1.75; }
.k-page .exe { font-size: 15px; }
.k-page .exn { font-size: 14px; color: #4f5660; margin-top: 4px; line-height: 1.6; }
.k-page .tblwrap { overflow: visible; }
.k-page table.glance { font-size: 14px; }
.k-page .glance th { font-size: 13px; padding: 8px 12px; }
.k-page .glance td { padding: 5px 12px; }
.k-page .s0t td.tar { font-size: 25px; line-height: 1.6; }
.k-page .three { margin: 0; }
.k-page .three h3 { font-size: 20px; }
.k-page .three ol { font-size: 15px; line-height: 2.2; }
.k-page .three .ab { font-size: 1.25em; }
.k-hero .hero .ab { font-size: 1.2em; }
/* the 12-row pronoun table: tighter rows so all 13 fit under the heading */
#s-c01-table .s0t td { padding: 2px 12px; }
#s-c01-table .s0t td.tar { font-size: 23px; line-height: 1.45; }
/* the reading mark (a gold frame, drawn inside the box, while a word is read) */
.ab, .exs { border-radius: 6px; }
.ab { padding: 0 3px; }
.exs { display: inline-block; padding: 0 8px; }
.k-hero .hero p { line-height: 2.0; }
/* table headers line up with their Arabic cells (the site's headers are left-aligned, its Arabic cells right-aligned) */
#s-c04-forms .s0t th, #s-c04-forms .s0t td.tar { text-align: center; }
#s-c01-table .s0t th:nth-child(1), #s-c01-table .s0t th:nth-child(3), #s-c07-table .s0t th:nth-child(4) { text-align: right; }
/* poster (build_thumbnail): the lesson hero over the "Three places" table */
.thumb .sumtbl table.glance { display: table !important; font-size: 15px; }
.thumb .sumtbl .glance th { font-size: 14px; padding: 8px 14px; }
.thumb .sumtbl .glance td { padding: 6px 14px; }
.thumb .sumtbl td.tar { font-size: 26px; line-height: 1.5; }
.thumb .sumtbl th:nth-child(4) { text-align: right; }
.hl { background-image: linear-gradient(transparent 58%, rgba(245,200,75,.75) 58%); background-repeat: no-repeat; background-size: 0% 100%; }
"""

HIDE = {
    "page": [".blk", ".exl", ".exn", "table.glance tr:not(:first-child)", ".three li"],
}

MARK_OFF = "inset 0 0 0 0px rgba(224,161,11,0), inset 0 0 0 999px rgba(245,200,75,0)"
MARK_ON = "inset 0 0 0 3px rgba(224,161,11,1), inset 0 0 0 999px rgba(245,200,75,0.30)"


def norm(s):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", s)).replace(".", "").split())


class SceneLesson(BC.Lesson):
    css = CSS
    hide = HIDE

    def __init__(self, data):
        self.d = data
        self.b = data["blocks"]
        self.ex = {}

    def chapter_of(self, scene):
        m = re.match(r"c(\d\d)-", scene)
        return int(m.group(1)) if m else None

    def chapter_name(self, scene, kind):
        if scene == "hero":
            return "Introduction"
        if kind == "chapter":
            ch = self.chapter_of(scene)
            return f'{ch} {self.d["chapters"][str(ch)]}'
        if scene == "c07-summary":
            return "In short"
        return None

    def thumbnail_html(self):
        """Poster: the lesson hero over the "Three places, one table" table."""
        return f'<div class="sumtbl">{self.b[33]["html"]}</div>'

    def h2(self, ch):
        return next(b["html"] for b in self.b if b["t"] == "h2" and b["chapter"] == ch)

    # ---- scene body
    def body(self, scene, segs):
        if scene not in SCENES:
            raise SystemExit(f"no renderer for scene {scene}")
        kind, idx, width, z = SCENES[scene]
        if kind == "hero":
            inner = f'<div class="view">{self.d["hero_html"]}</div>'
        elif kind == "chapter":
            inner = f'<div class="view chap">{self.b[idx[0]]["html"]}</div>'
        else:
            ch = self.chapter_of(scene)
            blocks = "".join(f'<div class="blk">{self.b[i]["html"]}</div>' for i in idx)
            inner = (f'<div class="view chead">{self.h2(ch)}</div>'
                     f'<div class="view" style="--z:{z};width:{width}px">{blocks}</div>')
        # an example sentence is marked on its text only (span.exs), and the two sides of an arrow example
        # (كِتَابُ زَيْدٍ ← كِتَابُهُ) one by one
        inner = re.sub(r'(<div class="exa" dir="rtl">)(.*?)(</div>)',
                       lambda m: m.group(1) + " ← ".join(f'<span class="exs">{p.strip()}</span>' for p in m.group(2).split("←"))
                       + m.group(3), inner)
        # persistent highlights, numbered in cue order
        n = 0
        for s in segs:
            for c in s["cues"]:
                if c.startswith("hl:"):
                    k = inner.rfind('<div class="view')  # only inside the content, never in the chapter heading
                    inner = inner[:k] + BC.wrap_phrase(inner[k:], c[3:], f"hl{n}")
                    n += 1
        # Noto Sans Arabic's glyph boxes are taller than the site's line boxes (nothing visible overflows)
        inner = re.sub(r'<(bdi|td|div|span) class="(ab|tar|exa|exs)"', r'<\1 data-layout-allow-overflow class="\2"', inner)
        inner = add_mark_attrs(inner)
        self._check(scene, kind, inner, segs)
        return kind, inner

    def prep(self, scene, kind, inner):
        return inner

    def _check(self, scene, kind, inner, segs):
        """Every piece of the scene must be revealed by a cue (coverage)."""
        cues = [c for s in segs for c in s["cues"]]
        k = inner.rfind('<div class="view')
        body = inner[k:]
        need = []
        need += [f"b:{i}" for i in range(body.count('<div class="blk">'))]
        need += [f"ex:{i}" for i in range(body.count('class="exl"'))]
        need += [f"note:{i}" for i in range(body.count('class="exn"'))]
        need += [f"li:{i}" for i in range(body.count("<li>"))]
        rows = body.count("<tr>") - body.count("<table")
        if "rows" not in cues:
            need += [f"row:{i}" for i in range(rows)]
        missing = [c for c in need if c not in cues] if kind == "page" else []
        for c in cues:  # every ar: cue must find its element
            if c.startswith("ar:"):
                text, _, nth = c[3:].partition("#")
                if f'data-mark="{html.escape(norm(text), quote=True)}#{int(nth or 1)}"' not in inner:
                    raise SystemExit(f"{scene}: cue {c}: no element with exactly this text")
        if missing:
            raise SystemExit(f"{scene}: never shown: {missing}")

    # ---- cues
    def cue(self, tl, scene, kind, S, name, arg, t, seg_len, state):
        if kind == "hero":
            if name == "ar":
                self._mark(tl, S, arg, t, seg_len, state)
                return True
            return False
        if kind == "chapter":
            if name == "title":
                tl.fade_up(f"{S} h2", t, 16, 0.45)
                return True
            if name == "ar":
                self._mark(tl, S, arg, t, seg_len, state)
                return True
            raise SystemExit(f"{scene}: unknown cue {name}:{arg}")
        if name == "b":
            tl.fade_up(f"{S} .stagebody > .view:last-child > .blk:nth-child({int(arg) + 1})", t)
            return True
        if name == "ex":
            tl.fade_up(f"{S} .exl:nth-child({int(arg) + 1})", t, 10)
            return True
        if name == "note":
            tl.fade_up(f"{S} .exl:nth-child({int(arg) + 1}) .exn", t, 8)
            return True
        if name == "row":
            tl.fade_up(f"{S} table.glance tr:nth-child({int(arg) + 2})", t, 8)
            return True
        if name == "rows":
            tl.add(f'tl.fromTo("{S} table.glance tr:not(:first-child)", {{opacity:0, y:8}}, '
                   f'{{opacity:1, y:0, duration:0.3, stagger:0.12, ease:"power2.out"}}, {t:.3f});')
            return True
        if name == "li":
            tl.fade_up(f"{S} .three li:nth-child({int(arg) + 1})", t, 10)
            return True
        if name == "hl":
            n = state.setdefault("hl", 0)
            state["hl"] = n + 1
            tl.add(f'tl.fromTo("{S} .hl{n}", {{backgroundSize:"0% 100%"}}, {{backgroundSize:"100% 100%", duration:0.45, ease:"power2.out"}}, {t:.3f});')
            return True
        if name == "ar":
            self._mark(tl, S, arg, t, seg_len, state)
            return True
        raise SystemExit(f"{scene}: unknown cue {name}:{arg}")

    def _mark(self, tl, S, arg, t, seg_len, state):
        """A gold frame on the element whose text is exactly `arg` (`text#n`: its n-th match), while it is read."""
        text, _, nth = arg.partition("#")
        nth = int(nth or 1)
        sel = f'{S} [data-mark="{html.escape(norm(text), quote=True)}#{nth}"]'
        open_ = state.setdefault("marks_open", {})
        if sel in open_ and t <= open_[sel][1] + 0.4:
            # the same word is still framed (named, then read): keep the frame on, end it after this segment
            tl.lines[open_[sel][0]] = "// frame kept on"
        else:
            tl.add(f'tl.fromTo({sel!r}, {{boxShadow:"{MARK_OFF}"}}, {{boxShadow:"{MARK_ON}", duration:0.25, ease:"power2.out", immediateRender:false}}, {t:.3f});')
        off = t + max(seg_len, 0.8) + 0.35
        tl.add(f'tl.to({sel!r}, {{boxShadow:"{MARK_OFF}", duration:0.35}}, {off:.3f});')
        open_[sel] = (len(tl.lines) - 1, off)


def add_mark_attrs(inner):
    """data-mark="<text>#<n>" on every markable element (n counts equal texts in DOM order).
    Example sentences and the halves of an arrow example (span.exs) first, then words in {}, then table cells."""
    seen = {}

    def rep(m):
        t = norm(m.group(4))
        seen[t] = seen.get(t, 0) + 1
        return (f'<{m.group(1)} data-layout-allow-overflow data-mark="{html.escape(t, quote=True)}#{seen[t]}" '
                f'class="{m.group(2)}"{m.group(3)}>{m.group(4)}</{m.group(1)}>')
    for tags in ("span", "bdi", "td"):
        inner = re.sub(rf'<({tags}) data-layout-allow-overflow class="(ab|tar|exs)"([^>]*)>((?:(?!<\1[ >]).)*?)</\1>',
                       rep, inner, flags=re.S)
    return inner
