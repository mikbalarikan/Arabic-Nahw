"""Scenes for the lesson video "Question words" (Stage 3, unit 5; lesson id s3-questions).

Loaded by build_composition.py (lesson_for). Every block is the site's own HTML from lesson.json
(content/stage3/u5_questions.py rendered by content/course.py render_notes), styled by the site's CSS.
This file only adds the 1920x1080 sizes and the cue animations.
Scene ids and cues: video/lessons/s3-questions/SCRIPT_SPEC.md.
"""
import html, re

import build_composition as BC

# scene id -> lesson block indices shown in it (see SCRIPT_SPEC.md)
SCENES = {
    "c01-table": [3], "c01-rule": [4], "c01-tips": [5, 6, 7],
    "c02-examples": [10], "c02-cols": [11], "c02-tip": [12],
    "c03-examples": [15], "c03-tip": [16],
    "c04-rule": [18], "c04-examples": [19],
    "c05-table": [21], "summary": [22],
}
KIND = {"table": "qtable", "rule": "rulebox", "tip": "tips", "examples": "exlist", "cols": "cols", "summary": "summary"}
HL_BG = "rgba(245,200,75,.42)"

CSS = r"""
/* chapter titles: the lesson's paragraph is the grey sub-line */
.k-chapter .sub .ab { font-size: 1.3em; }
.k-chapter h2 .ab { font-size: 1.15em; }
.chead h2 .ab { font-size: 1.1em; }
.k-chapter .stagebody > .view { max-width: 700px; }

/* tables */
/* rows are added one by one (display none -> table-row), so the table grows downward from a fixed top */
.k-qtable .stagebody { justify-content: flex-start; }
.k-qtable .stagebody > .view:last-child { --z: 1.5; width: fit-content; margin-top: 88px; }
.k-qtable .tblwrap { margin: 0; overflow: visible; }
.k-qtable table.glance { font-size: 15px; clip-path: inset(0 round 12px); }
.k-qtable table.glance tr:not(:first-child) { display: none; }
.k-qtable .glance th.tar { text-align: right; }
.k-qtable .glance th { font-size: 14px; padding: 7px 16px; }
.k-qtable .glance td { padding: 4px 16px; transition: none; }
.k-qtable .s0t td.tar { font-size: 25px; line-height: 1.75; }
.k-qtable .glance td .ab { font-size: 1.45em; line-height: 1.6; }
.k-qtable .stagebody > .view.t9 { --z: 1.45; min-width: 680px; margin-top: 90px; }
.k-qtable .t9 .glance th { padding: 7px 24px; }
.k-qtable .t9 .glance td { padding: 5px 24px; font-size: 16px; }
.k-qtable .t9 .s0t td.tar { font-size: 24px; line-height: 1.5; }
.k-qtable .t9 .glance td .ab { font-size: 1.2em; line-height: 1.5; }

/* rule box and tips */
.k-rulebox .stagebody > .view:last-child { --z: 2.15; width: 760px; }
.k-rulebox .rbox { font-size: 16px; line-height: 1.75; padding: 18px 22px; margin: 0; }
.k-rulebox .rbox .ab, .k-tips .tipbox .ab, .k-cols .ab, .k-summary .ab { font-size: 1.3em; }
.k-tips .stagebody > .view:last-child { --z: 2.0; width: 800px; display: flex; flex-direction: column; gap: 14px; margin-top: 40px; }
.k-tips .tipbox { font-size: 15.5px; line-height: 1.75; padding: 14px 20px; margin: 0; }
.k-tips .stagebody > .view.one { --z: 2.2; width: 720px; margin-top: 0; }
.k-tips .one .tipbox { font-size: 16px; padding: 18px 22px; }

/* example lines */
.k-exlist .stagebody > .view:last-child { --z: 1.6; width: 1040px; margin-top: 30px; }
.k-exlist .stagebody > .view.n3 { --z: 1.8; width: 920px; }
.k-exlist .exlist { gap: 12px; margin: 0; }
.k-exlist .exl { position: relative; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr); column-gap: 30px; padding: 10px 20px; }
.k-exlist .exa { font-size: 30px; text-align: center; }
.k-exlist .exe { font-size: 16px; }
.k-exlist .exn { font-size: 14px; color: #5f6672; }
.k-exlist .exn .ab { font-size: 1.6em; }
.k-exlist .exl .sayf { position: absolute; inset: -3px; border: 3px solid var(--gold); border-radius: 13px;
  box-shadow: 0 0 16px rgba(245,200,75,.5); opacity: 0; pointer-events: none; }

/* two cards */
.k-cols .stagebody > .view:last-child { --z: 2.0; width: 860px; }
.k-cols .kkgrid { gap: 16px; }
.k-cols .kk { padding: 14px 18px; }
.k-cols .kkt { font-size: 17px; }
.k-cols .kkar { font-size: 21px; }
.k-cols .s0cols .kkd { font-size: 15px; line-height: 1.7; margin-top: 6px; }

/* summary */
.k-summary .stagebody > .view { --z: 1.9; width: 860px; }
.k-summary .three { margin: 0; }
.k-summary .three h3 { font-size: 21px; }
.k-summary .three ol { font-size: 15.5px; line-height: 2.25; }

/* your turn */
.k-yourturn .stagebody > .view { --z: 1.9; width: 900px; }
.k-yourturn .ptar { line-height: 2.0; }
.k-yourturn .pten { font-style: normal; color: var(--ink); font-size: 14px; }

/* poster */
.qtiles { display: flex; flex-wrap: wrap; justify-content: center; gap: 14px; }
.qtile { font-family: var(--arabic); font-size: 46px; line-height: 1.6; padding: 4px 22px; border: 2.5px solid #e0a10b;
  background: #fff5d6; border-radius: 12px; color: var(--ink); }
.hlm { background-image: linear-gradient(transparent 52%, rgba(245,200,75,.75) 52%); background-repeat: no-repeat; background-size: 0% 100%; }
/* on Arabic the marker is a bar under the letters, so no mark is covered */
.ab .hlm, .exa .hlm { background-image: linear-gradient(transparent 86%, rgba(245,200,75,.95) 86%); }
"""

HIDE = {
    "qtable": ["table.glance tr:not(:first-child)"],
    "rulebox": [".stagebody > .view:last-child > *"],
    "tips": [".tipbox"],
    "exlist": [".exl"],
    "cols": [".kk"],
    "summary": [".three", ".three li"],
}


def visible_wrap(fragment, phrase, cls, start=0):
    """Wrap the first `phrase` at or after visible-text offset `start` in <span class=cls> (even across tags).
    Returns (new_fragment, end offset)."""
    parts = re.split(r"(<[^>]+>)", fragment)
    text, owners = "", []
    for pi, p in enumerate(parts):
        if p.startswith("<"):
            continue
        t = html.unescape(p)
        owners += [(pi, ci) for ci in range(len(t))]
        text += t
    i = text.find(phrase, start)
    if i < 0:
        i = text.find(phrase)
    if i < 0:
        raise SystemExit(f"highlight phrase not found: {phrase!r}")
    j = i + len(phrase)
    spans = {}
    for k in range(i, j):
        pi, ci = owners[k]
        a, b = spans.get(pi, (ci, ci))
        spans[pi] = (min(a, ci), max(b, ci + 1))
    for pi, (a, b) in spans.items():
        t = html.unescape(parts[pi])
        parts[pi] = BC.esc(t[:a]) + f'<span class="hlm {cls}">' + BC.esc(t[a:b]) + "</span>" + BC.esc(t[b:])
    return "".join(parts), j


class SceneLesson(BC.Lesson):
    css = CSS
    hide = HIDE

    def __init__(self, data):
        self.d = data
        self.R = data.get("roles", {})
        self.sec = {s["num"]: s for s in data["sections"]}
        self.blocks = data["blocks"]
        self.ex = {}

    def chapter_of(self, scene):
        m = re.match(r"c(\d\d)-", scene)
        return int(m.group(1)) if m else None

    def chapter_name(self, scene, kind):
        if scene == "hero":
            return "Introduction"
        if kind == "chapter":
            ch = self.chapter_of(scene)
            return f'{ch} {re.sub(r"[{}]", "", self.sec[ch]["title_text"])}'
        if scene == "c01-rule":
            return re.sub(r"[{}]", "", self.blocks[4]["src"]["title"])   # "Learn the last vowel"
        if scene == "summary":
            return "In short"
        if scene.startswith("outro"):
            return "Your turn"
        return None

    def thumbnail_html(self):
        """Poster: the question words of the first table as gold word tiles, under the lesson hero."""
        rows = self.blocks[3]["src"]["rows"]
        words = [w for r in rows for w in re.findall(r"\{([^}]+)\}", r[0])]
        tiles = "".join(f'<span class="qtile">{BC.esc(w)}</span>' for w in words)
        return f'<div class="qtiles" dir="rtl">{tiles}</div>'

    def body(self, scene, segs):
        if scene == "hero":
            return "hero", f'<div class="view">{self.d["hero_html"]}</div>'
        ch = self.chapter_of(scene)
        if ch and scene.endswith("-title"):
            sec = self.sec[ch]
            sub = ""
            ps = [self.blocks[i] for i in sec["blocks"] if self.blocks[i]["t"] == "p"]
            if ps and sec["blocks"][0] == ps[0]["i"]:
                sub = f'<p class="sub">{re.sub(r"^<p[^>]*>|</p>$", "", ps[0]["html"])}</p>'
            return "chapter", f'<div class="view chap">{self.h2(ch)}{sub}</div>'
        if scene.startswith("outro"):
            return "yourturn", self.your_turn()
        idx = SCENES[scene]
        kind = KIND[self.blocks[idx[0]]["t"]]
        inner = "".join(self.blocks[i]["html"] for i in idx)
        # highlight phrases, in cue order; a repeated phrase takes the next match
        pos = 0
        for n, phrase in enumerate(c[3:] for s in segs for c in s["cues"] if c.startswith("hl:")):
            inner, pos = visible_wrap(inner, phrase, f"hl{n}", pos)
        if kind == "qtable":
            inner = self.align_heads(inner)
        if kind == "exlist":
            inner = inner.replace('<div class="exl">', '<div class="exl"><span class="sayf"></span>')
        head = f'<div class="view chead">{self.h2(ch)}</div>' if ch else ""
        var = ""
        if kind == "qtable" and len(self.blocks[idx[0]]["src"]["rows"]) > 7:
            var = " t9"
        if kind == "tips" and len(idx) == 1:
            var = " one"
        if kind == "exlist" and len(self.blocks[idx[0]]["src"]["items"]) <= 3:
            var = " n3"
        return kind, head + f'<div class="view{var}">{inner}</div>'

    @staticmethod
    def align_heads(table):
        """A header over a column of Arabic cells gets the cells' right alignment."""
        rows = re.findall(r"<tr>(.*?)</tr>", table, re.S)
        cells = [re.findall(r'<td class="([^"]*)"', r) for r in rows[1:]]
        heads = re.split(r"(?=<th>)", rows[0])[1:]
        out = "".join(h.replace("<th>", '<th class="tar">', 1) if all(len(r) > c and r[c] == "tar" for r in cells) else h
                      for c, h in enumerate(heads))
        return table.replace(rows[0], out, 1)

    def your_turn(self):
        rows = "".join(
            f'<div class="pt"><span class="qn">{p["n"]}</span><div class="pten">{BC.esc(p["title"])}</div></div>'
            for p in self.d["practice_cards"])
        return (f'<div class="view yt"><h2>Your turn</h2>'
                f'<p class="sub">Practice tab: {len(self.d["practice_cards"])} cards. Homework tab: {len(self.d["homework_cards"])} more.</p>'
                f'<div class="ptgrid">{rows}</div></div>')

    def prep(self, scene, kind, inner):
        # Noto Sans Arabic's glyph boxes are taller than the site's line boxes; nothing visible overflows
        # (checked on snapshots), so tell the layout audit these Arabic text boxes are fine as they are.
        for cls in ("exa", "kkar", "wm"):
            inner = inner.replace(f'<div class="{cls}"', f'<div data-layout-allow-overflow class="{cls}"')
        inner = inner.replace('<td class="tar">', '<td data-layout-allow-overflow class="tar">')
        inner = inner.replace('<bdi class="ab"', '<bdi data-layout-allow-overflow class="ab"')
        return inner

    def cue(self, tl, scene, kind, S, name, arg, t, seg_len, state):
        if kind in ("hero", "chapter"):
            return False
        if name == "hl":
            n = state.setdefault("hl", 0)
            state["hl"] = n + 1
            self._unhl(tl, state, t)
            tl.add(f'tl.fromTo("{S} .hl{n}", {{backgroundSize:"0% 100%"}}, {{backgroundSize:"100% 100%", duration:0.45, ease:"power2.out", immediateRender:false}}, {t:.3f});')
            state["hl_on"] = f"{S} .hl{n}"
            return True
        if name in ("tip", "col", "item", "ex", "say", "show"):
            self._unhl(tl, state, t)
        if name == "show":
            if kind == "tips":
                tl.fade_up(f"{S} .tipbox:nth-child(1)", t)
            elif kind == "summary":
                tl.fade_up(f"{S} .three", t)
            elif kind == "yourturn":
                pass  # the Your turn page fades in by itself
            else:
                tl.fade_up(f"{S} .stagebody > .view:last-child > *", t)
            return True
        if name == "row":
            sel = f"{S} table.glance tr:nth-child({int(arg) + 1})"
            tl.add(f'tl.set("{sel}", {{display:"table-row"}}, {t:.3f});')
            tl.fade_up(sel, t, 8)
            return True
        if name == "cell":
            r, c = arg.split(".")
            sel = f"{S} table.glance tr:nth-child({int(r) + 1}) td:nth-child({c})"
            self._unmark(tl, state, t)
            tl.add(f'tl.to("{sel}", {{backgroundColor:"{HL_BG}", duration:0.3, ease:"power1.out"}}, {t:.3f});')
            state["cell"] = sel
            return True
        if name == "tip":
            tl.fade_up(f"{S} .tipbox:nth-child({arg})", t)
            return True
        if name == "ex":
            self._unmark(tl, state, t)
            tl.fade_up(f"{S} .exl:nth-child({arg})", t, 10)
            return True
        if name == "say":
            self._unmark(tl, state, t)
            sel = f"{S} .exl:nth-child({arg}) .sayf"
            tl.add(f'tl.to("{sel}", {{opacity:1, duration:0.35, ease:"power1.out"}}, {t:.3f});')
            state["say"] = sel
            return True
        if name == "col":
            tl.fade_up(f"{S} .kk:nth-child({arg})", t, 16)
            return True
        if name == "item":
            k = int(arg)
            if k > 1:   # the point being read stays bright, the earlier ones step back
                tl.add(f'tl.to("{S} .three li:nth-child(-n+{k - 1})", {{opacity:0.5, duration:0.35}}, {t:.3f});')
            tl.fade_up(f"{S} .three li:nth-child({k})", t, 10)
            return True
        if name == "title":
            return False
        raise SystemExit(f"{scene}: unknown cue {name}:{arg}")

    @staticmethod
    def _unhl(tl, state, t):
        if state.get("hl_on"):
            tl.add(f'tl.to("{state["hl_on"]}", {{backgroundSize:"0% 100%", duration:0.3, ease:"power1.in"}}, {t:.3f});')
            state["hl_on"] = None

    @staticmethod
    def _unmark(tl, state, t):
        if state.get("cell"):
            tl.add(f'tl.to("{state["cell"]}", {{backgroundColor:"rgba(245,200,75,0)", duration:0.3}}, {t:.3f});')
            state["cell"] = None
        if state.get("say"):
            tl.add(f'tl.to("{state["say"]}", {{opacity:0, duration:0.3}}, {t:.3f});')
            state["say"] = None
