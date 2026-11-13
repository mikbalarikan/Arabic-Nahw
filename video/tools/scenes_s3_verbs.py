"""Scenes for the lesson video "Fixed verbs: past and order" (lesson id s3-verbs, Stage 3 unit 6).

Loaded by build_composition.py (lesson_for). Every block on screen is the site's own HTML for that notes
block (course.render_notes, exported to lesson.json by export_s3_verbs.py), styled by the site's CSS.
This file only picks the blocks for each scene, adds 1920x1080 sizes and the cue animations.
Scene ids and cues: video/lessons/s3-verbs/SCRIPT_SPEC.md.
"""
import html, re

import build_composition as BC

AR = "\u0600-\u06FF"
GOLD_ROW = "#fdefc9"   # the site gold at 32% on the white table
NO_ROW = "#ffffff"

CSS = r"""
/* chapter title: the h2 and the chapter's first paragraph under it */
.k-chapter .stagebody > .view { max-width: 700px; }
.k-chapter .sub .ab { font-size: 1.3em; }
.k-chapter .sub bdi, .k-chapter h2 bdi { font-family: var(--arabic); }

/* block scenes sit under the small chapter heading */
.k-cols .stagebody > .view:last-child, .k-tip .stagebody > .view:last-child, .k-tips .stagebody > .view:last-child,
.k-rule .stagebody > .view:last-child, .k-words .stagebody > .view:last-child, .k-examples .stagebody > .view:last-child,
.k-table .stagebody > .view:last-child { margin-top: 20px; }
.ab { font-size: 1.25em; }
.k-cols .kkd, .rbox, .tipbox, .exe, .exn, .three li { text-wrap: pretty; }
.k-rule .ab, .k-tip .ab, .k-tips .ab, .k-examples .exn .ab { white-space: nowrap; }

/* cards (cols) */
.k-cols .stagebody > .view:last-child { --z: 2.0; width: 880px; }
.k-cols .kkgrid { margin: 0; gap: 14px; grid-template-columns: repeat(3, minmax(0, 1fr)); }
.k-cols .kk { padding: 14px 16px; }
.k-cols .kkt { font-size: 14.5px; gap: 2px; flex-direction: column; align-items: stretch; }
.k-cols .kkt .kkar { align-self: flex-end; }
.k-cols .kkar { font-family: var(--arabic); font-size: 24px; line-height: 1.6; }
.k-cols .s0cols .kkd { font-size: 14px; line-height: 1.55; }

/* tips and rules */
.k-tip .stagebody > .view:last-child, .k-tips .stagebody > .view:last-child { --z: 2.25; width: 720px; }
.k-tip .tipbox, .k-tips .tipbox { font-size: 16px; line-height: 1.75; padding: 18px 22px; margin: 0; }
.k-tips .tipbox + .tipbox { margin-top: 18px; }
.k-rule .stagebody > .view:last-child { --z: 2.2; width: 740px; }
.k-rule .rbox { font-size: 16px; line-height: 1.75; padding: 18px 22px; margin: 0; }
/* the grey rule title (#5a626b on #eef0f2) is the faintest text on screen: one step darker in the video */
.k-rule .rbox > b.dk { color: #40464d !important; }
.rbox > b .arr { font-family: var(--arabic); font-size: 1.25em; }
.hl { background-image: linear-gradient(transparent 58%, rgba(245,200,75,.75) 58%); background-repeat: no-repeat; background-size: 0% 100%; }
/* on an Arabic word the Latin underline hangs below the glyphs: a soft marker behind the whole word instead */
.exa .hl { background-image: linear-gradient(rgba(245,200,75,.5), rgba(245,200,75,.5)); border-radius: 6px; }

/* doer-ending tiles */
.k-words .stagebody > .view:last-child { --z: 2.1; width: 760px; }
.k-words .wtiles { margin: 0; gap: 14px; justify-content: center; }
.k-words .wt0 { min-width: 150px; padding: 8px 14px 12px; }
.k-words .wta { font-size: 46px; line-height: 1.7; }
.k-words .wts { font-size: 15px; color: var(--ink); }

/* examples */
.k-examples .stagebody > .view:last-child { --z: 1.9; width: 900px; }
.k-examples .exlist { margin: 0; gap: 12px; }
.k-examples .exl { padding: 12px 18px; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr); }
.k-examples .exa { font-size: 30px; }
.k-examples .exe { font-size: 15.5px; }
.k-examples .exn { font-size: 13.5px; color: #5f6672; margin-top: 4px; }

/* tables (the site's .glance s0t) */
.k-table .stagebody > .view:last-child { --z: 1.9; width: 860px; }
.k-table .tblwrap { margin: 0; overflow: visible; }
/* the table frame grows with its rows: no table background or border, each cell is white */
.k-table table.glance { background: transparent; border: 0; border-radius: 0; overflow: visible; }
.k-table .s0t td { background: #fff; }
.k-table .s0t td:first-child { border-left: 1px solid #ddd8cb; }
.k-table .s0t td:last-child { border-right: 1px solid #ddd8cb; }
.k-table .s0t tr:last-child td { border-bottom: 1px solid #ddd8cb; }
.k-table .s0t th:first-child { border-top-left-radius: 12px; }
.k-table .s0t th:last-child { border-top-right-radius: 12px; }
.k-table .s0t tr:last-child td:first-child { border-bottom-left-radius: 12px; }
.k-table .s0t tr:last-child td:last-child { border-bottom-right-radius: 12px; }
/* headers of the Arabic columns sit right, over their right-aligned Arabic */
#s-c02-table th:nth-child(2), #s-c02-table th:nth-child(3), #s-c04-table th:nth-child(3),
#s-c05-table th:nth-child(1), #s-c05-table th:nth-child(2), #s-c06-table th:nth-child(2),
#s-c07-table th:nth-child(1), #s-c07-table th:nth-child(2) { text-align: right; }
/* order table, Doer column: "hidden أَنْتَ" and the endings in one alignment and size */
#s-c06-table .s0t td:nth-child(4) { text-align: left; direction: ltr; font-family: var(--font); font-size: 14.5px; }
#s-c06-table .s0t td:nth-child(4) .ab { font-size: 1.8em; }
.k-table .s0t { font-size: 14.5px; }
.k-table .s0t th { font-size: 13.5px; padding: 8px 14px; }
.k-table .s0t td { padding: 6px 14px; }
.k-table .s0t td.tar { font-size: 25px; line-height: 1.6; }
.k-table .s0t td .ab { font-size: 1.3em; }
.k-table .s0t .arr { font-family: var(--arabic); font-size: 1.45em; line-height: 1.2; }
/* the 14-person past table: tall, so smaller and tighter */
#s-c02-table .stagebody > .view:last-child { --z: 1.5; width: 820px; margin-top: 66px; }
#s-c02-table .s0t td { padding: 1px 14px; }
#s-c02-table .s0t td.tar { font-size: 23px; line-height: 1.5; }
#s-c04-table .stagebody > .view:last-child { width: 880px; }
#s-c07-table .stagebody > .view:last-child { --z: 2.0; width: 780px; margin-top: 76px; }
.k-table .stagebody > .view:last-child { margin-top: 56px; }
#s-c07-table .s0t td { padding: 3px 14px; }

/* summary */
.k-summary .stagebody > .view:last-child { --z: 2.25; width: 760px; margin-top: 30px; }
.k-summary .three { margin: 0; padding: 20px 28px 16px; }
.k-summary .three h3 { font-size: 20px; margin: 0 0 6px; }
.k-summary .three ol { font-size: 15px; line-height: 1.95; }
.k-summary .three .ab { font-size: 1.3em; }

/* your turn: the Practice tab's cards */
.k-yourturn .stagebody > .view { --z: 1.9; width: 820px; }
.k-yourturn h2 { margin: 0 0 6px !important; font-size: 24px; }
.k-yourturn .sub { font-size: 15px; margin-bottom: 16px; }
.k-yourturn .pt { grid-template-columns: auto 1fr; padding: 10px 14px; }
.k-yourturn .pt .qn { grid-row: auto; }
.k-yourturn .pten { font-size: 15px; color: var(--ink); font-style: normal; }
"""

HIDE = {
    "cols": [".kk"],
    "tip": [".tipbox"],
    "tips": [".tipbox"],
    "rule": [".rbox"],
    "words": [".wt0"],
    "examples": [".exl", ".exn"],
    "table": ["table tr:not(:first-child)"],
    "summary": [".three li"],
}

KIND = {"cols": "cols", "tip": "tip", "tips": "tips", "rule": "rule", "words": "words",
        "examples": "examples", "table": "table"}


class SceneLesson(BC.Lesson):
    css = CSS
    hide = HIDE

    def __init__(self, data):
        self.d = data
        self.R = data["roles"]
        self.ch = {c["num"]: c for c in data["chapters"]}
        self.ex = {}
        data["hero_html"] = self.ch[0]["blocks"][0]["html"]   # the hero card, also used by the thumbnail

    # ---- helpers
    def h2(self, n):
        return f'<h2><span class="num">{n}</span>{self.ch[n]["title_html"]}</h2>'

    def blocks(self, scene):
        """The notes blocks a scene shows."""
        if scene == "sum":
            return [b for c in self.d["chapters"] for b in c["blocks"] if b["t"] == "summary"]
        n = self.chapter_of(scene)
        name = scene.split("-", 1)[1]
        want = "tip" if name == "tips" else name
        bl = [b for b in self.ch[n]["blocks"] if b["t"] == want]
        if name != "tips" and len(bl) != 1:
            raise SystemExit(f"{scene}: expected one {want} block in chapter {n}, found {len(bl)}")
        return bl

    def chapter_name(self, scene, kind):
        if scene == "hero":
            return "Introduction"
        if kind == "chapter":
            n = self.chapter_of(scene)
            return f'{n} {html.unescape(re.sub("<.*?>", "", self.ch[n]["title_html"]))}'
        if kind == "summary":
            return "In short"
        if kind == "yourturn":
            return "Your turn"
        return None

    def thumbnail_html(self):
        """Poster / thumbnail: the doer-ending tiles of chapter 3 under the lesson hero."""
        tiles = next(b["html"] for b in self.ch[3]["blocks"] if b["t"] == "words")
        return tiles.replace('<div class="wtiles">', '<div class="wtiles" style="justify-content:center">', 1)

    # ---- scene bodies
    def body(self, scene, segs):
        if scene == "hero":
            return "hero", f'<div class="view">{self.d["hero_html"]}</div>'
        if scene.startswith("outro"):
            rows = "".join(f'<div class="pt"><span class="qn">P{i}</span><div class="pten">{BC.esc(t)}</div></div>'
                           for i, t in enumerate(self.d["practice_titles"], 1))
            return "yourturn", (f'<div class="view yt"><h2>Your turn</h2><p class="sub">The Practice tab: '
                                f'{len(self.d["practice_titles"])} cards</p><div class="ptgrid">{rows}</div></div>')
        n = self.chapter_of(scene)
        if scene.endswith("-title"):
            first = self.ch[n]["blocks"][0]
            sub = re.sub(r'^<p class="s0p">(.*)</p>$', r"\1", first["html"], flags=re.S) if first["t"] == "p" else ""
            subh = f'<p class="sub">{sub}</p>' if sub else ""
            return "chapter", f'<div class="view chap">{self.h2(n)}{subh}</div>'
        if scene == "sum":
            b = self.blocks(scene)[0]
            return "summary", f'<div class="view">{b["html"]}</div>'
        name = scene.split("-", 1)[1]
        if name not in KIND:
            raise SystemExit(f"no renderer for scene {scene}")
        inner = "".join(b["html"] for b in self.blocks(scene))
        for k, phrase in enumerate(c[3:] for s in segs for c in s["cues"] if c.startswith("hl:")):
            inner = BC.wrap_phrase(inner, phrase, f"hl{k}")
        head = f'<div class="view chead">{self.h2(n)}</div>'
        return KIND[name], head + f'<div class="view">{inner}</div>'

    def prep(self, scene, kind, inner):
        # Noto Sans Arabic's glyph boxes are taller than the site's line boxes; nothing visible overflows
        # (checked on snapshots), so the layout audit is told these Arabic text boxes are fine as they are.
        for cls in ("wta", "exa", "kkar"):
            inner = inner.replace(f'<div class="{cls}"', f'<div data-layout-allow-overflow class="{cls}"')
            inner = inner.replace(f'<span class="{cls}"', f'<span data-layout-allow-overflow class="{cls}"')
        inner = inner.replace('<td class="tar"', '<td data-layout-allow-overflow class="tar"')
        # plain Arabic inside an English table cell (ـتْ, ـا, the ن of "dropping the ن") is set in the
        # Latin font at body size on the site; in the video it gets the Arabic font, a little larger
        def cell(m):
            parts = re.split(r"(<[^>]+>)", m.group(2))
            depth = 0
            for i, p in enumerate(parts):
                if p.startswith("<"):
                    depth += -1 if p.startswith("</") else (0 if p.endswith("/>") else 1)
                elif depth == 0:
                    parts[i] = re.sub(f"[{AR}]+(?:[ ،]+[{AR}]+)*", lambda a: f'<span class="arr">{a.group(0)}</span>', p)
            return m.group(1) + "".join(parts) + "</td>"
        inner = re.sub(r'(<td class="">)(.*?)</td>', cell, inner, flags=re.S)
        inner = inner.replace('<b style="color:#5a626b">', '<b class="dk" style="color:#5a626b">')
        inner = re.sub(r'(<div class="rbox"[^>]*><b[^>]*>)(.*?)</b>',
                       lambda m: m.group(1) + re.sub(f"[{AR}]+", lambda a: f'<span class="arr">{a.group(0)}</span>', m.group(2)) + "</b>",
                       inner, flags=re.S)
        return inner

    # ---- cues
    def cue(self, tl, scene, kind, S, name, arg, t, seg_len, state):
        V = f"{S} .stagebody > .view:last-child"
        if kind in ("hero", "chapter") and name in ("title", "sub"):
            return False   # the shared hero / chapter cues
        if kind == "yourturn" and name == "show":
            return True    # the Your turn page fades in by itself
        if name == "show" and kind in ("tip", "rule"):
            tl.fade_up(f"{V} > *", t)
            return True
        if name == "hl":
            return False   # shared: marks .hl0, .hl1 ... in order
        if name == "tip" and kind == "tips":
            tl.fade_up(f"{V} > .tipbox:nth-child({int(arg) + 1})", t)
            return True
        if name == "item":
            sel = {"cols": ".kk", "words": ".wt0", "summary": ".three li"}[kind]
            tl.fade_up(f"{V} {sel}:nth-child({int(arg) + 1})", t, 16, 0.4)
            return True
        if kind == "table":
            tr = lambda r: f"{V} table tr:nth-child({int(r) + 2})"
            def mark(r):
                prev = state.get("row")
                if prev is not None and prev != r:
                    tl.add(f'tl.to("{tr(prev)} td", {{backgroundColor:"{NO_ROW}", duration:0.3}}, {t:.3f});')
                if r is not None:
                    tl.add(f'tl.fromTo("{tr(r)} td", {{backgroundColor:"{NO_ROW}"}}, '
                           f'{{backgroundColor:"{GOLD_ROW}", duration:0.3, immediateRender:false}}, {t:.3f});')
                state["row"] = r
            if name == "row":
                tl.fade_up(tr(arg), t, 8, 0.32)
                if state.get("cell"):     # a ring from the previous row goes with its highlight
                    tl.add(f'tl.to("{state.pop("cell")}", {{boxShadow:"inset 0 0 0 0 rgba(245,200,75,0)", duration:0.25}}, {t:.3f});')
                mark(arg)
                return True
            if name == "hlrow":
                mark(arg)
                return True
            if name == "unhl":
                mark(None)
                if state.get("cell"):
                    tl.add(f'tl.to("{state.pop("cell")}", {{boxShadow:"inset 0 0 0 0 rgba(245,200,75,0)", duration:0.25}}, {t:.3f});')
                return True
            if name == "rows":
                tl.add(f'tl.fromTo("{V} table tr:not(:first-child)", {{opacity:0, y:8}}, '
                       f'{{opacity:1, y:0, duration:0.3, stagger:0.1, ease:"power2.out"}}, {t:.3f});')
                return True
            if name == "cell":
                r, c = arg.split(":")
                sel = f"{tr(r)} td:nth-child({int(c) + 1})"
                tl.add(f'tl.fromTo("{sel}", {{boxShadow:"inset 0 0 0 0 rgba(245,200,75,0)"}}, '
                       f'{{boxShadow:"inset 0 0 0 3px rgba(214,160,20,.9)", duration:0.3, immediateRender:false}}, {t:.3f});')
                state["cell"] = sel     # taken off by the next row cue, or by unhl
                return True
        if kind == "examples":
            line = f"{V} .exl:nth-child({int(arg) + 1})"
            if name == "ex":
                tl.fade_up(line, t, 12, 0.4)
                return True
            if name == "note":
                tl.fade_up(f"{line} .exn", t, 6, 0.35)
                return True
            if name == "read":
                tl.add(f'tl.fromTo("{line}", {{borderColor:"#e6e1d3", boxShadow:"0 0 0 0px rgba(245,200,75,0)"}}, '
                       f'{{borderColor:"#d6a014", boxShadow:"0 0 0 3px rgba(245,200,75,.85)", duration:0.3, immediateRender:false}}, {t:.3f});')
                tl.add(f'tl.to("{line}", {{borderColor:"#e6e1d3", boxShadow:"0 0 0 0px rgba(245,200,75,0)", duration:0.4}}, '
                       f'{t + max(seg_len, 1.0) + 0.35:.3f});')
                return True
        raise SystemExit(f"{scene}: unknown cue {name}:{arg} for kind {kind}")
