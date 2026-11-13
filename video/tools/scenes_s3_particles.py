"""Scenes for the lesson video "Particles" (Stage 3, unit 7; lesson id s3-particles).

Loaded by build_composition.py (lesson_for). Markup comes from lesson.json, i.e. from the `notes` blocks of
content/stage3/u7_particles.py rendered by the site's own renderer (course.render_notes), and is styled by the
site's own CSS. This file only adds the 1920x1080 sizes and the cue animations.
Scene ids and cues: video/lessons/s3-particles/SCRIPT_SPEC.md.
"""
import re

import build_composition as BC

CSS = r"""
/* a chapter title with the lesson paragraph under it as its grey sub-line */
.k-chapter .stagebody > .view { max-width: 700px; }
.k-chapter .sub.s0p { font-size: 15px; line-height: 1.6; max-width: 640px; margin: 0 auto; color: var(--muted); }
.k-chapter .sub .ab { font-size: 1.25em; }

/* rule and tip boxes; the marker band sits lower in an Arabic line box (Noto Sans Arabic boxes are tall) */
.ab .hl { background-image: linear-gradient(transparent 48%, rgba(245,200,75,.75) 48%, rgba(245,200,75,.75) 80%, transparent 80%); }
.k-rulebox .rbox .ab, .k-tip .tipbox .ab { font-size: 1.3em; }
.k-tip .stagebody > .view:last-child { --z: 2.2; width: 720px; }
.k-tip .tipbox { font-size: 16px; line-height: 1.75; padding: 18px 22px; margin: 0; }

/* the five kinds of particles */
.k-cols .stagebody > .view:last-child { --z: 1.9; width: 860px; margin-top: 60px; }
.k-cols .kkgrid { grid-template-columns: 1fr 1fr; gap: 10px; }
.k-cols .kk { padding: 11px 16px; }
.k-cols .kk:last-child { grid-column: 1 / -1; width: calc(50% - 5px); justify-self: center; }
.k-cols .kkt { font-size: 15px; align-items: center; }
.k-cols .kkar { font-family: var(--arabic); font-size: 19px; }
.k-cols .s0cols .kkd { font-size: 14px; margin-top: 4px; }
.k-cols .kkd .ab { font-size: 1.6em; }
/* the card's line is all Arabic (a list of ḥarfs): read it right to left, like the Arabic heading above it */
.k-cols .s0cols .kkd { direction: rtl; text-align: right; }

/* tables: the site's table, bigger; the row being talked about gets a soft gold wash */
.k-table .stagebody > .view:last-child { width: fit-content; margin-top: 64px; }
.k-table .tblwrap { margin: 0; overflow: hidden; border-radius: 12px; width: fit-content; }
.k-table table.glance { font-size: 14px; width: auto; min-width: 640px; }
.k-table .glance th { font-size: 13px; padding: 7px 16px; }
.k-table .glance td { padding: 3px 16px; box-shadow: inset 0 0 0 999px rgba(245,200,75,0); }
.k-table .s0t td.tar { font-size: 25px; line-height: 1.75; }
.k-table .glance td .ab { font-size: 1.55em; line-height: 1.6; }

/* the two worked examples */
.k-exlist .stagebody > .view:last-child { --z: 2.0; width: 820px; margin-top: 50px; }
.k-exlist .exlist { gap: 14px; margin: 0; }
.k-exlist .exl { padding: 12px 22px; grid-template-columns: 330px minmax(0, 1fr); gap: 30px; }
.k-exlist .exa { font-size: 32px; }
.k-exlist .exe { font-size: 15.5px; }
.k-exlist .exn { font-size: 14px; margin-top: 6px; color: #5f6672; }
.k-exlist .exn .ab { font-size: 1.35em; }

/* the watermark word is read aloud in the hero: it lights up while it is read */
.k-hero .wm { color: rgba(255,255,255,.13); }

/* summary */
.k-summary .stagebody > .view { --z: 1.95; width: 820px; }
.k-summary .three { margin: 0; }
.k-summary .three h3 { font-size: 20px; }
.k-summary .three ol { font-size: 15px; line-height: 2.3; }
.k-summary .three .ab { font-size: 1.3em; }
"""

HIDE = {
    "tip": [".stagebody > .view:last-child > *"],
    "cols": [".kk"],
    "table": ["table.glance tr:not(:first-child)"],
    "exlist": [".exl", ".exn"],
    "summary": [".three li"],
}

# table zoom by number of data rows (fits under the chapter heading at 1080p)
def table_zoom(n):
    return round(min(2.3, 820 / (52 + 50 * n)), 3)


class SceneLesson(BC.Lesson):
    css = CSS
    hide = HIDE

    def __init__(self, data):
        self.d = data
        self.R = data["roles"]
        self.sec = {s["num"]: s for s in data["sections"]}
        self.ex = {}
        self.blocks = data["blocks"]
        self.scenes = {s["id"]: s for s in data["scenes"]}

    def chapter_of(self, scene):
        m = re.match(r"c(\d\d)-", scene)
        return int(m.group(1)) if m else None

    def chapter_name(self, scene, kind):
        if scene == "hero":
            return "Introduction"
        if kind == "chapter":
            ch = self.chapter_of(scene)
            return f'{ch} {re.sub("<.*?>", "", self.sec[ch]["title"])}'
        if kind == "summary":
            return re.sub("<.*?>", "", self.blocks[self.scenes[scene]["blocks"][0]]["data"]["title"])
        return None

    def thumbnail_html(self):
        """Poster: the hero over the five kinds of particles."""
        b = next(b for b in self.blocks if b["t"] == "cols")
        return f'<div class="k-cols">{b["html"]}</div>'

    @staticmethod
    def _hl(fragment, segs):
        for n, phrase in enumerate(c for s in segs for c in s["cues"] if c.startswith("hl:")):
            fragment = BC.wrap_phrase(fragment, phrase[3:], f"hl{n}")
        return fragment

    def body(self, scene, segs):
        sc = self.scenes.get(scene)
        if sc is None:
            raise SystemExit(f"no scene {scene} in lesson.json")
        html = [self.blocks[i]["html"] for i in sc["blocks"]]
        kind = sc["kind"]
        if kind == "hero":
            return "hero", f'<div class="view">{html[0]}</div>'
        if kind == "summary":
            return "summary", f'<div class="view">{html[0]}</div>'
        ch = sc["chapter"]
        if kind == "chapter":
            sub = html[1].replace('<p class="s0p">', '<p class="sub s0p">') if len(html) > 1 else ""
            return "chapter", f'<div class="view chap">{html[0]}{self._hl(sub, segs) if sub else ""}</div>'
        head = f'<div class="view chead">{self.h2(ch)}</div>'
        if kind == "rule":
            return "rulebox", head + f'<div class="view">{self._hl(html[0], segs)}</div>'
        if kind == "tip":
            return "tip", head + f'<div class="view">{self._hl(html[0], segs)}</div>'
        if kind == "cols":
            return "cols", head + f'<div class="view">{html[0]}</div>'
        if kind == "table":
            n = len(self.blocks[sc["blocks"][0]]["data"]["rows"])
            return "table", head + f'<div class="view" style="--z:{table_zoom(n)}">{html[0]}</div>'
        if kind == "examples":
            return "exlist", head + f'<div class="view">{html[0]}</div>'
        raise SystemExit(f"no renderer for scene {scene} ({kind})")

    def prep(self, scene, kind, inner):
        inner = re.sub(r'(<b style="[^"]*">)([^<]*?)([\u0600-\u06ff][\u0600-\u06ff\s]*[\u0600-\u06ff])',
                       r'\1\2<bdi class="ab">\3</bdi>', inner)
        if kind == "table":
            sc = self.scenes[scene]
            rows = self.blocks[sc["blocks"][0]]["data"]["rows"]
            ar_only = lambda c: re.search(r"[\u0600-\u06ff]", c) and not re.search(r"[A-Za-z]", c)
            heads = iter(range(len(rows[0])))
            def th(m):
                i = next(heads)
                return '<th style="text-align:right">' if all(ar_only(r[i]) for r in rows) else m.group(0)
            inner = re.sub(r"<th>", th, inner)
        # Noto Sans Arabic's glyph boxes are taller than the site's line boxes; nothing visible overflows
        # (checked on snapshots), so tell the layout audit these Arabic text boxes are fine as they are.
        inner = inner.replace('<td class="tar"', '<td data-layout-allow-overflow class="tar"')
        inner = inner.replace('<div class="exa"', '<div data-layout-allow-overflow class="exa"')
        inner = inner.replace('<bdi class="ab">', '<bdi data-layout-allow-overflow class="ab">')
        inner = inner.replace('<span class="kkar">', '<span data-layout-allow-overflow class="kkar">')
        inner = inner.replace('<div class="wm"', '<div data-layout-allow-overflow class="wm"')
        return inner

    def cue(self, tl, scene, kind, S, name, arg, t, seg_len, state):
        if kind == "hero" and name == "wm":
            tl.add(f'tl.to("{S} .wm", {{color:"rgba(245,200,75,0.95)", duration:0.4}}, {t:.3f});')
            tl.add(f'tl.to("{S} .wm", {{color:"rgba(255,255,255,0.13)", duration:0.6}}, {t + max(seg_len, 1.0) + 0.3:.3f});')
            return True
        if kind == "cols" and name == "col":
            tl.fade_up(f"{S} .kk:nth-child({arg})", t, 18, 0.42)
            return True
        if kind == "table":
            if name == "row":
                tl.fade_up(f"{S} table.glance tr:nth-child({int(arg) + 1})", t, 8)
                return True
            if name == "rows":
                tl.add(f'tl.fromTo("{S} table.glance tr:not(:first-child)", {{opacity:0, y:8}}, '
                       f'{{opacity:1, y:0, duration:0.3, stagger:0.12, ease:"power2.out"}}, {t:.3f});')
                return True
            if name == "mark":
                prev = state.get("mark")
                if prev:
                    tl.add(f'tl.to("{S} table.glance tr:nth-child({prev + 1}) td", '
                           f'{{boxShadow:"inset 0 0 0 999px rgba(245,200,75,0)", duration:0.3}}, {t:.3f});')
                n = int(arg)
                if n:
                    tl.add(f'tl.to("{S} table.glance tr:nth-child({n + 1}) td", '
                           f'{{boxShadow:"inset 0 0 0 999px rgba(245,200,75,0.30)", duration:0.35}}, {t:.3f});')
                state["mark"] = n or None
                return True
        if kind == "exlist":
            if name == "ex":
                tl.fade_up(f"{S} .exl:nth-child({arg})", t, 14, 0.4)
                return True
            if name == "note":
                tl.fade_up(f"{S} .exl:nth-child({arg}) .exn", t, 8)
                return True
        if kind == "tip" and name == "show":
            tl.fade_up(f"{S} .stagebody > .view:last-child > *", t)
            return True
        return False
