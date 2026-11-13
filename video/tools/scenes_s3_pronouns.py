"""Scenes for the lesson video "Separate pronouns" (lesson id s3-pronouns, Stage 3 unit 1).

Loaded by build_composition.py (lesson_for). The markup of every block is the site's own (lesson.json keeps
the HTML of content/course.py render_notes), styled by the site's CSS. This file only picks the blocks of each
scene, adds the 1920x1080 sizes and the cue animations. Scene ids and cues: video/lessons/s3-pronouns/SCRIPT_SPEC.md.
"""
import html, re

import build_composition as BC

# scene -> (kind, section, slice of that section's blocks, block types expected). Checked at build time.
SCENES = {
    "c01-why": ("why", 1, 0, 4, ["p", "p", "p", "words"]),
    "c02-cols": ("cols", 2, 0, 1, ["cols"]),
    "c03-table": ("table", 3, 0, 2, ["p", "table"]),
    "c03-tip1": ("tip", 3, 2, 3, ["tip"]),
    "c03-tip2": ("tip", 3, 3, 4, ["tip"]),
    "c04-groups": ("groups", 4, 0, 1, ["cols"]),
    "c04-tip1": ("tip", 4, 1, 2, ["tip"]),
    "c04-tip2": ("tip", 4, 2, 3, ["tip"]),
    "c05-rule": ("rule", 5, 0, 2, ["p", "rule"]),
    "c05-steps": ("steps", 5, 2, 4, ["p", "table"]),
    "c05-tip": ("tip", 5, 4, 5, ["tip"]),
    "c06-examples": ("examples", 6, 0, 2, ["p", "examples"]),
    "c06-tip": ("tip", 6, 2, 3, ["tip"]),
    "summary": ("summary", 6, 3, 4, ["summary"]),
}

CSS = r"""
.k-chapter h2 .num { flex: none; }
.ab { font-size: 1.25em; white-space: nowrap; }
.hl { padding: 0 .08em; }
.three .hl { background-image: linear-gradient(transparent 84%, rgba(245,200,75,.95) 84%); }
/* Arabic line boxes are tall (Noto Sans Arabic): a band at letter height, not one that hangs into the next line */
.hl.hlar { background-image: linear-gradient(transparent 52%, rgba(245,200,75,.75) 52%, rgba(245,200,75,.75) 74%, transparent 74%); }
.three .hl.hlar { background-image: linear-gradient(transparent 70%, rgba(245,200,75,.95) 70%, rgba(245,200,75,.95) 76%, transparent 76%); }

/* chapter 1: three paragraphs and four word tiles */
.k-why .stagebody > .view:last-child { --z: 2.1; width: 780px; margin-top: 70px; }
.k-why .s0p { font-size: 15.5px; line-height: 1.6; margin: 0 0 12px; max-width: none; }
.k-why .s0p .ab { font-size: 1.3em; }
.k-why .wtiles { justify-content: center; gap: 16px; margin: 18px 0 0; }
.k-why .wt0 { min-width: 120px; padding: 6px 18px 10px; }
.k-why .wta { font-size: 38px; line-height: 1.55; }
.k-why .wts { font-size: 14px; color: #5f6672; }

/* chapter 2: fixed / flexible cards */
.k-cols .stagebody > .view:last-child { --z: 2.25; width: 760px; }
.k-cols .kkgrid { gap: 14px; }
.k-cols .kk { padding: 14px 16px 16px; }
.k-cols .kkt { font-size: 17px; align-items: baseline; }
.k-cols .kkar { font-size: 26px; font-family: var(--arabic); line-height: 1.5; }
.k-cols .kkd { font-size: 14.5px; line-height: 1.7; margin-top: 6px; color: #3d434d; }
.k-cols .kkd .ab { font-size: 1.4em; }

/* chapter 3: the table of twelve */
.k-table .stagebody > .view:last-child { --z: 1.76; width: 800px; margin-top: 66px; }
.k-table .s0p { font-size: 14.5px; margin: 0 0 8px; text-align: center; max-width: none; }
.k-table .tblwrap { margin: 0; overflow: visible; }
.k-table table.glance { font-size: 13px; }
.k-table .glance th { font-size: 12px; padding: 5px 12px; }
.k-table .glance td { padding: 1px 12px; }
.k-table .s0t td.tar { font-size: 21px; line-height: 1.45; text-align: center; }
.k-table .glance td, .k-steps .glance td { background-color: #ffffff; }
/* rows appear one by one: no empty white table box before them */
.k-table table.glance, .k-steps table.glance { background: transparent; border-color: transparent; }

/* tips (one per scene) */
.k-tip .stagebody > .view:last-child { --z: 2.3; width: 700px; }
.k-tip .tipbox { font-size: 16px; padding: 18px 22px; margin: 0; line-height: 1.75; }
.k-tip .tipbox .ab { font-size: 1.4em; }

/* chapter 4: three groups, stacked */
.k-groups .stagebody > .view:last-child { --z: 2.1; width: 800px; margin-top: 40px; }
.k-groups .kkgrid { grid-template-columns: 1fr; gap: 12px; }
.k-groups .kk { padding: 10px 18px 12px; }
.k-groups .kkt { font-size: 16px; align-items: baseline; }
.k-groups .kkar { font-size: 24px; font-family: var(--arabic); line-height: 1.5; }
.k-groups .kkd { font-size: 14px; margin-top: 6px; direction: rtl; text-align: right; }
.k-groups .kkd .ab { font-size: 2em; line-height: 1.5; margin: 0 .15em; }

/* chapter 5: the place of rafʿ */
.k-rule .stagebody > .view:last-child { --z: 2.1; width: 780px; margin-top: 30px; }
.k-rule .s0p, .k-steps .s0p { font-size: 15.5px; line-height: 1.6; margin: 0 0 16px; max-width: none; }
.k-rule .rbox { font-size: 16px; line-height: 1.85; padding: 16px 20px; margin: 0; }
.k-rule .rbox .ab { font-size: 1.4em; }
.k-steps .stagebody > .view:last-child { --z: 2.05; width: 800px; }
.k-steps .tblwrap { margin: 0; overflow: visible; }
.k-steps table.glance { font-size: 15px; }
.k-steps .glance th { font-size: 13px; padding: 7px 14px; }
.k-steps .glance td { padding: 8px 14px; }
.k-steps .glance td .ab { font-size: 1.7em; }

/* chapter 6: six example sentences */
.k-examples .stagebody > .view:last-child { --z: 1.66; width: 1020px; margin-top: 64px; }
.k-examples .s0p { font-size: 15px; margin: 0 0 8px; text-align: center; max-width: none; }
.k-examples .exlist { gap: 7px; margin: 0; }
.k-examples .exl { grid-template-columns: 340px minmax(0, 1fr); padding: 5px 18px 8px; gap: 20px; }
.k-examples .exa { font-size: 29px; line-height: 1.6; }
.k-examples .exe { font-size: 15px; }
.k-examples .exn { font-size: 13.5px; color: #5f6672; line-height: 1.55; }
.k-examples .exn .ab { font-size: 1.3em; }

/* in short */
.k-summary .stagebody > .view:last-child { --z: 1.85; width: 900px; }
.k-summary .three { margin: 0; padding: 22px 30px 18px; }
.k-summary .three h3 { font-size: 20px; }
.k-summary .three ol { font-size: 15px; line-height: 1.75; }
.k-summary .three li { margin: 6px 0; }
.k-summary .three .ab { font-size: 1.3em; }

/* practice */
.k-yourturn .stagebody > .view { --z: 1.9; width: 820px; }
.k-yourturn .ptgrid { grid-template-columns: 1fr 1fr; }
.k-yourturn .pt { grid-template-columns: auto 1fr; padding: 12px 16px; }
.k-yourturn .pt .qn { grid-row: auto; font-size: 13px; }
.k-yourturn .ptt { font-size: 15px; font-weight: 600; }
.k-yourturn .hw { margin-top: 14px; font-size: 14px; color: #5f6672; text-align: center; }

/* thumbnail: the four word tiles under the hero */
.thumb .th-ex .wtiles { justify-content: center; gap: 18px; margin: 0; }
.thumb .th-ex .wt0 { min-width: 150px; }
.thumb .th-ex .wta { font-size: 46px; }
.thumb .th-ex .wts { font-size: 15px; }
"""

HIDE = {
    "why": [".s0p", ".wt0"],
    "cols": [".kk"],
    "table": [".s0p", "table.glance tr"],
    "tip": [".stagebody > .view:last-child > *"],
    "groups": [".kk"],
    "rule": [".s0p", ".rbox"],
    "steps": [".s0p", "table.glance tr"],
    "examples": [".s0p", ".exl", ".exn"],
    "summary": [".three li"],
    "yourturn": [".stagebody > .view > *"],
}

GOLD = "#fdf0c6"   # the soft gold "now" band (opaque, over the white row)
CLEAR = "#ffffff"


def wrap_nth(fragment, phrase, cls, nth=1):
    """Like build_composition.wrap_phrase, but for the nth occurrence of `phrase` in the visible text."""
    parts = re.split(r"(<[^>]+>)", fragment)
    text, owners = "", []
    for pi, p in enumerate(parts):
        if p.startswith("<"):
            continue
        t = html.unescape(p)
        for ci in range(len(t)):
            owners.append((pi, ci))
        text += t
    i = -1
    for _ in range(nth):
        i = text.find(phrase, i + 1)
        if i < 0:
            raise SystemExit(f"highlight phrase not found (occurrence {nth}): {phrase!r}")
    j = i + len(phrase)
    spans = {}
    for k in range(i, j):
        pi, ci = owners[k]
        a, b = spans.get(pi, (ci, ci))
        spans[pi] = (min(a, ci), max(b, ci + 1))
    for pi, (a, b) in spans.items():
        t = html.unescape(parts[pi])
        ar = " hlar" if re.search("[\u0600-\u06ff]", phrase) else ""
        parts[pi] = BC.esc(t[:a]) + f'<span class="hl{ar} {cls}">' + BC.esc(t[a:b]) + "</span>" + BC.esc(t[b:])
    return "".join(parts)


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
            return f'{ch} {self.sec[ch]["title_text"]}'
        if kind == "summary":
            return "In short"
        if kind == "yourturn":
            return "Practice"
        return None

    def thumbnail_html(self):
        return next(b["html"] for b in self.blocks if b["t"] == "words")

    def scene_blocks(self, scene):
        kind, sec, i, j, types = SCENES[scene]
        bl = [self.blocks[k] for k in self.sec[sec]["blocks"][i:j]]
        if [b["t"] for b in bl] != types:
            raise SystemExit(f"{scene}: expected blocks {types}, got {[b['t'] for b in bl]}")
        return kind, bl

    def body(self, scene, segs):
        if scene == "hero":
            return "hero", f'<div class="view">{self.d["hero_html"]}</div>'
        ch = self.chapter_of(scene)
        if ch and scene.endswith("-title"):
            return "chapter", f'<div class="view chap">{self.h2(ch)}</div>'
        if scene.startswith("outro"):
            cards = "".join(f'<div class="pt"><span class="qn">{p["n"]}</span><div class="ptt">{BC.esc(p["title"])}</div></div>'
                            for p in self.d["practice_cards"])
            hw = f'<div class="hw">Then {len(self.d["homework_cards"])} more cards for homework.</div>' if self.d.get("homework_cards") else ""
            return "yourturn", (f'<div class="view yt"><h2><span class="num">✎</span>Your turn</h2>'
                                f'<p class="sub">The Practice tab: {len(self.d["practice_cards"])} cards.</p>'
                                f'<div class="ptgrid">{cards}</div>{hw}</div>')
        kind, bl = self.scene_blocks(scene)
        inner = "".join(b["html"] for b in bl)
        # highlighter strokes, in cue order (build_composition's hl cue numbers them hl0, hl1 ...)
        hls = [c[3:] for s in segs for c in s["cues"] if c.startswith("hl:")]
        for n, ph in enumerate(hls):
            phrase, _, occ = ph.partition("@")
            inner = wrap_nth(inner, phrase, f"hl{n}", int(occ) if occ else 1)
        head = f'<div class="view chead">{self.h2(ch)}</div>' if ch else ""
        return kind, head + f'<div class="view">{inner}</div>'

    def prep(self, scene, kind, inner):
        # Noto Sans Arabic's glyph boxes are taller than the site's line boxes; nothing visible overflows
        # (checked on snapshots), so tell the layout audit that these Arabic text boxes are fine as they are.
        for cls in ("wta", "exa", "kkar"):
            inner = inner.replace(f'<div class="{cls}"', f'<div data-layout-allow-overflow class="{cls}"')
            inner = inner.replace(f'<span class="{cls}"', f'<span data-layout-allow-overflow class="{cls}"')
        inner = inner.replace('<td class="tar">', '<td data-layout-allow-overflow class="tar">')
        return inner

    def cue(self, tl, scene, kind, S, name, arg, t, seg_len, state):
        V = f"{S} .stagebody > .view:last-child"
        if kind == "yourturn" and name == "show":
            return True  # the page fades in by itself
        if name == "p":
            tl.fade_up(f"{V} p.s0p:nth-of-type({int(arg)})", t)
            return True
        if name == "word":
            tl.fade_up(f"{V} .wt0:nth-child({int(arg)})", t, 18, 0.42)
            return True
        if name == "col":
            tl.fade_up(f"{V} .kk:nth-child({int(arg)})", t, 18, 0.42)
            return True
        if name == "head":
            tl.fade_up(f"{V} table.glance tr:first-child", t, 8)
            return True
        if name == "row":
            n = int(arg)
            row = f"{V} table.glance tr:nth-child({n + 1})"
            tl.fade_up(row, t, 8, 0.32)
            prev = state.get("row")
            if prev:
                tl.add(f'tl.to("{V} table.glance tr:nth-child({prev + 1}) td", {{backgroundColor:"{CLEAR}", duration:0.3}}, {t:.3f});')
            tl.add(f'tl.to("{row} td", {{backgroundColor:"{GOLD}", duration:0.3}}, {t:.3f});')
            state["row"] = n
            return True
        if name == "unmark":
            if state.get("row"):
                tl.add(f'tl.to("{V} table.glance tr:nth-child({state["row"] + 1}) td", {{backgroundColor:"{CLEAR}", duration:0.4}}, {t:.3f});')
                state["row"] = None
            return True
        if name == "rule":
            tl.fade_up(f"{V} .rbox", t, 14, 0.42)
            return True
        if name == "ex":
            tl.fade_up(f"{V} .exl:nth-child({int(arg)})", t, 10)
            return True
        if name == "note":
            tl.fade_up(f"{V} .exl:nth-child({int(arg)}) .exn", t, 6)
            return True
        if name == "li":
            tl.fade_up(f"{V} .three li:nth-child({int(arg)})", t, 10)
            return True
        if name == "show" and kind == "tip":
            tl.fade_up(f"{V} > *", t)
            return True
        return False  # title, sub, hl: the shared handlers
