#!/usr/bin/env python3
"""Build the HyperFrames project for a lesson video.

Reads   video/lessons/<id>/lesson.json   (exported from content/, see export_lesson.py)
        video/lessons/<id>/script.json   (segments + cues, see SCRIPT_SPEC.md)
        video/lessons/<id>/timings.json  (measured audio length per segment; optional:
                                          without it, lengths are estimated from the text)
Writes  video/build/<id>/<part>/         (one HyperFrames project per part: index.html, the
                                          site's CSS, local fonts and GSAP)
        video/build/<id>/plan.json       (absolute times of every part, scene and segment;
                                          used by the audio mixer, subtitles and chapters)

The look is the site's own: the lesson HTML from content/lesson.py and the CSS the site
build uses (site/_shell.css + course.base_css() + site/_extra.css). Only sizes for a
1920x1080 frame and the animation states are added here.

Usage: python3 video/tools/build_composition.py [lesson_id] [--only PART_ID]
"""
import html, json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIDEO = ROOT / "video"
sys.path.insert(0, str(ROOT / "content"))

FPS = 30
LEAD = 0.7          # silence before the first segment of a part
TAIL = 1.0          # hold after the last segment of a part
SCENE_PRE = 0.35    # a scene starts this long before its first segment
XFADE = 0.45        # cross-fade between scenes
CUE_LEAD = 0.12     # visuals land slightly before the voice

# Parts are rendered (and can be published) separately; chapters follow the lesson.
PARTS = [
    ("p01-intro", ["hero", "c01-"]),
    ("p02-verb-sentence", ["c02-"]),
    ("p03-sign", ["c03-"]),
    ("p04-colour-key", ["c04-"]),
    ("p05-glance", ["c05-"]),
    ("p06-object", ["c06-"]),
    ("p07-purpose", ["c07-"]),
    ("p08-time-place", ["c08-"]),
    ("p09-state", ["c09-"]),
    ("p10-old-rules", ["c10-"]),
    ("p11-all-together", ["c11-", "outro-"]),
]


# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(s, quote=True)

def rgba(hexc, a):
    h = hexc.lstrip("#")
    return f"rgba({int(h[0:2], 16)},{int(h[2:4], 16)},{int(h[4:6], 16)},{a})"

def est_len(seg):
    """Rough spoken length when no audio exists yet."""
    if seg["lang"] == "ar":
        return 0.55 + 0.75 * len(seg["text"].split())
    return 0.35 + len(seg["text"].split()) / 2.45

def site_css():
    import os
    import course  # noqa: imported for base_css(), exactly as tools/build_site.py does
    cwd = os.getcwd(); os.chdir(ROOT / "content")
    try:
        base = course.base_css()
    finally:
        os.chdir(cwd)
    shell = (ROOT / "site" / "_shell.css").read_text(encoding="utf-8")
    css = shell.replace("/*BASE_CSS*/", base)
    css += (ROOT / "site" / "_extra.css").read_text(encoding="utf-8")
    return css

def brand_html():
    idx = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
    m = re.search(r'<button class="brand"[^>]*>(.*?)</button>', idx, re.S)
    return m.group(1)

def wrap_phrase(fragment, phrase, cls):
    """Wrap `phrase` (matched on the visible text) in <span class=cls>, even across tags."""
    parts = re.split(r"(<[^>]+>)", fragment)
    text, owners = "", []
    for pi, p in enumerate(parts):
        if p.startswith("<"):
            continue
        t = html.unescape(p)
        for ci in range(len(t)):
            owners.append((pi, ci))
        text += t
    i = text.find(phrase)
    if i < 0:
        i = text.lower().find(phrase.lower())
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
        parts[pi] = esc(t[:a]) + f'<span class="hl {cls}">' + esc(t[a:b]) + "</span>" + esc(t[b:])
    return "".join(parts)


# ---------------------------------------------------------------- scene bodies
class Lesson:
    def __init__(self, data):
        self.d = data
        self.R = data["roles"]
        self.sec = {s["num"]: s for s in data["sections"]}
        self.ex = {x["num"]: x for x in data["examples"]}

    def h2(self, n):
        s = self.sec[n]
        return f'<h2><span class="num">{n}</span>{s["title"]}</h2>'

    def chapter_of(self, scene):
        m = re.match(r"c(\d\d)-", scene)
        return int(m.group(1)) if m else None

    def piece(self, n, pattern):
        m = re.search(pattern, self.sec[n]["html"], re.S)
        if not m:
            raise SystemExit(f"chapter {n}: fragment not found: {pattern}")
        return m.group(0)

    # each returns (kind, inner_html)
    def body(self, scene, segs):
        ch = self.chapter_of(scene)
        kind = scene.split("-", 1)[1] if ch else scene
        if scene == "hero":
            return "hero", f'<div class="view">{self.d["hero_html"]}</div>'
        if scene.startswith("outro"):
            stems = "".join(
                f'<div class="pt"><span class="qn">E{i}</span><div class="ptar" dir="rtl">'
                + " ".join(f'<span class="sw">{esc(w)}</span>' for w in p["stems"])
                + f'</div><div class="pten">“{esc(p["en"])}”</div></div>'
                for i, p in enumerate(self.d["practice"], 1))
            return "yourturn", f'<div class="view yt">{self.d["practice_heading"]}<div class="ptgrid">{stems}</div></div>'
        if kind == "title":
            sub = self.sec[ch]["sub"]
            subh = f'<p class="sub">{sub}</p>' if sub else ""
            return "chapter", f'<div class="view chap">{self.h2(ch)}{subh}</div>'
        head = f'<div class="view chead">{self.h2(ch)}</div>'
        if kind == "cases":
            return "cases", head + f'<div class="view">{self.d["fragments"]["cases"]}</div>'
        if kind == "scope":
            sc = self.piece(1, r"<div class=.scope.>.*?</div>").replace("ـَ / ـً", '<bdi class="bigmark">ـَ</bdi> / <bdi class="bigmark">ـً</bdi>')
            return "scope", head + f'<div class="view">{sc}</div>'
        if kind == "rules":
            return "rules", head + f'<div class="view">{self.piece(2, r"<div class=.rule.>.*?</div></div>")}</div>'
        if kind == "careful":
            return "careful", head + f'<div class="view">{self.piece(2, r"<div class=.tipbox.><b>Careful.*?</div>")}</div>'
        if kind == "signs":
            sg = re.sub(r"<b>(ـ[^<]*)</b>", r'<b class="bigmark">\1</b>', self.d["fragments"]["sign_rules"])
            return "signs", head + f'<div class="view">{sg}</div>'
        if kind == "key":
            return "colourkey", head + f'<div class="view">{self.d["fragments"]["colour_key"]}</div>'
        if kind == "glance":
            return "glance", head + f'<div class="view">{self.d["fragments"]["glance"]}</div>'
        if kind == "rule":
            rb = self.piece(ch, r'<div class="rbox".*?</div>')
            for k, seg in enumerate(s for s in segs):
                pass
            for n, phrase in enumerate(hl for s in segs for hl in s["cues"] if hl.startswith("hl:")):
                rb = wrap_phrase(rb, phrase[3:], f"hl{n}")
            return "rulebox", head + f'<div class="view">{rb}</div>'
        if kind == "five":
            return "five", f'<div class="view">{self.piece(11, r"<div class=.three.>.*?</div>")}</div>'
        m = re.match(r"ex(\w+)$", kind)
        if m:
            x = self.ex[m.group(1)]
            return "example", head + f'<div class="view">{x["html"]}</div>'
        raise SystemExit(f"no renderer for scene {scene}")


# ---------------------------------------------------------------- timeline
class TL:
    def __init__(self):
        self.lines = []

    def add(self, js):
        self.lines.append(js)

    def fade_up(self, sel, t, dy=14, d=0.38):
        self.add(f'tl.fromTo({sel!r}, {{opacity:0, y:{dy}}}, {{opacity:1, y:0, duration:{d}, ease:"power2.out"}}, {t:.3f});')

    def fade_in(self, sel, t, d=0.35):
        self.add(f'tl.fromTo({sel!r}, {{opacity:0}}, {{opacity:1, duration:{d}, ease:"power1.out"}}, {t:.3f});')


def cue_js(tl, lesson, scene, kind, sid, cue, t, seg_len, segs_after, state):
    S = f"#{sid}"
    name, _, arg = cue.partition(":")
    if kind == "hero":
        if name == "title":
            tl.fade_up(f"{S} .hero h1", t, 18, 0.5)
        elif name == "sub":
            tl.fade_up(f"{S} .hero p", t)
        return
    if name == "title":
        tl.fade_up(f"{S} h2", t, 16, 0.45)
        return
    if name == "sub":
        tl.fade_up(f"{S} .sub", t)
        return
    if name == "show":
        tl.fade_up(f"{S} .stagebody > .view:last-child > *", t)
        return
    if name == "case":
        tl.fade_up(f"{S} .case:nth-child({'ABCD'.index(arg) + 1})", t, 20, 0.42)
        return
    if name == "scope":
        if arg == "1":
            tl.fade_up(f"{S} .scope", t)
        tl.fade_up(f"{S} .scope li:nth-child({arg})", t + 0.1)
        return
    if name == "rule":
        tl.fade_up(f"{S} .rr:nth-child({1 if arg == 'verb' else 2})", t)
        return
    if name == "sign":
        tl.fade_up(f"{S} .sg:nth-child({arg})", t, 20, 0.42)
        return
    if name == "key":
        order = ["verb", "doer", "obj", "purp", "when", "state"]
        tl.fade_up(f"{S} .kk:nth-child({order.index(arg) + 1})", t)
        return
    if name == "old":
        tl.fade_up(f"{S} .oldrow", t)
        return
    if name == "row":
        order = ["obj", "purp", "when", "state"]
        tl.fade_up(f"{S} table.glance tr:nth-child({order.index(arg) + 2})", t, 8)
        return
    if name == "q":
        tl.fade_up(f"{S} .three li:nth-child({arg})", t, 10)
        return
    if name == "hl":
        n = state.setdefault("hl", 0)
        state["hl"] = n + 1
        tl.add(f'tl.fromTo("{S} .hl{n}", {{backgroundSize:"0% 100%"}}, {{backgroundSize:"100% 100%", duration:0.45, ease:"power2.out"}}, {t:.3f});')
        return
    # ---- example cues
    if name == "en":
        tl.fade_up(f"{S} .exh", t)
        return
    if name == "sentence":
        tl.fade_up(f"{S} .sbox", t, 10, 0.45)
        return
    if name == "group":
        g = int(arg)
        sel = f"{S} .kg:nth-child({g + 1})"
        tl.add(f'tl.to("{sel}", {{borderColor:"var(--gb)", backgroundColor:"var(--gbg)", duration:0.4, ease:"power2.out"}}, {t:.3f});')
        tl.add(f'tl.to("{sel} .kgl, {sel} .vc, {sel} .klab, {sel} .kw.ghost .kt", {{opacity:1, duration:0.4, ease:"power2.out"}}, {t + 0.08:.3f});')
        tl.add(f'tl.to("{sel} .kw.small", {{borderColor:"var(--sb)", duration:0.4, ease:"power2.out"}}, {t + 0.08:.3f});')
        if state.get("ask") == g:
            tl.add(f'tl.to("{sel} .askq", {{opacity:0, scale:0.6, duration:0.25}}, {t:.3f});')
            state["ask"] = None
        return
    if name == "ask":
        g = int(arg)
        sel = f"{S} .kg:nth-child({g + 1})"
        tl.add(f'tl.fromTo("{sel} .askq", {{opacity:0, scale:0.6}}, {{opacity:1, scale:1, duration:0.3, ease:"back.out(2)"}}, {t:.3f});')
        state["ask"] = g
        return
    if name == "vowel":
        g = int(arg)
        sel = f"{S} .kg:nth-child({g + 1}) .kw:first-child .vc"
        tl.add(f'tl.to("{sel}", {{scale:1.22, duration:0.2, yoyo:true, repeat:3, ease:"sine.inOut"}}, {t + 0.35:.3f});')
        return
    if name == "read":
        w = int(arg)
        sel = f"{S} .rw{w}"
        tl.add(f'tl.fromTo("{sel}", {{scaleX:0, opacity:1}}, {{scaleX:1, opacity:1, duration:0.3, ease:"power2.out", immediateRender:false}}, {t:.3f});')
        tl.add(f'tl.to("{sel}", {{opacity:0, duration:0.3}}, {t + max(seg_len, 0.8) + 0.4:.3f});')
        return
    if name == "line":
        tl.fade_up(f"{S} .xl:nth-child({int(arg) + 1})", t, 10)
        return
    if name == "tip":
        tl.fade_up(f"{S} .ex .tipbox", t)
        return
    raise SystemExit(f"{scene}: unknown cue {cue}")


# ---------------------------------------------------------------- page
VIDEO_CSS = r"""
@font-face { font-family: "Noto Sans"; src: url("fonts/noto-sans-latin-wght-normal.woff2") format("woff2"); font-weight: 100 900; font-style: normal; unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD, U+2190-21FF; }
@font-face { font-family: "Noto Sans"; src: url("fonts/noto-sans-latin-ext-wght-normal.woff2") format("woff2"); font-weight: 100 900; font-style: normal; unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }
@font-face { font-family: "Noto Sans"; src: url("fonts/noto-sans-latin-wght-italic.woff2") format("woff2"); font-weight: 100 900; font-style: italic; }
@font-face { font-family: "Noto Sans Arabic"; src: url("fonts/noto-sans-arabic-arabic-wght-normal.woff2") format("woff2"); font-weight: 100 900; }

html, body { margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: var(--paper); }
#root { position: relative; width: 1920px; height: 1080px; background: var(--paper); }
.scene { position: absolute; inset: 0; opacity: 0; background: var(--paper); }

/* site top bar, as on arabic-nahw.pages.dev */
.vbar { position: absolute; left: 0; right: 0; top: 0; height: 78px; background: var(--teal); color: #fff;
  display: flex; align-items: center; gap: 22px; padding: 0 56px; font-size: 22px; }
.vbar .brand { display: flex; align-items: center; gap: 14px; background: none; border: 0; padding: 0; color: #fff; }
.vbar .brand b { font-size: 24px; }
.vbar .brand .mk { font-size: 30px; }
.vbar .crumb { font-size: 21px; }
.vbar .tabs { margin-left: auto; display: flex; gap: 8px; }
.vbar .tab { font-size: 19px; padding: 7px 22px; }

.stagebody { position: absolute; left: 0; right: 0; top: 78px; bottom: 0; display: flex; flex-direction: column;
  align-items: center; justify-content: center; }
.stagebody > .view { zoom: var(--z, 1.8); width: 900px; max-width: none; margin: 0; }
.stagebody > .view.chead { position: absolute; top: 24px; left: 50%; transform: translateX(-50%); zoom: 1.6; }
.chead h2 { margin: 0 !important; font-size: 19px; }

/* hero */
.k-hero .stagebody > .view { --z: 2.0; width: 880px; }
.k-hero .hero { padding: 40px 44px 38px; }
.k-hero .hero h1 { font-size: 40px; }
.k-hero .hero p { font-size: 16px; max-width: 520px; }
.k-hero .wm { font-size: 92px; right: 44px; top: 34px; }

/* chapter title */
.k-chapter .stagebody > .view { --z: 2.6; width: fit-content; max-width: 660px; text-align: center; }
.k-chapter h2 { justify-content: center; }
.k-chapter .sub { text-wrap: balance; margin: 0 auto; }
.k-chapter h2 { font-size: 30px; margin: 0 0 14px !important; gap: 16px; }
.k-chapter h2 .num { width: 44px; height: 44px; font-size: 22px; flex: none; }
.k-chapter .sub { font-size: 15.5px; line-height: 1.5; margin: 0; max-width: 680px; }

.k-cases .stagebody > .view:last-child { --z: 2.0; }
.k-cases .case { padding: 14px 12px 16px; }
.k-cases .cm { font-size: 30px; } .k-cases .ca { font-size: 30px; } .k-cases .ce { font-size: 13px; } .k-cases .cs { font-size: 13px; }
.k-scope .stagebody > .view:last-child { --z: 2.1; width: 760px; }
.k-scope .scope { font-size: 15px; padding: 16px 20px; }
.k-rules .stagebody > .view:last-child { --z: 2.0; }
.k-rules .rr { font-size: 14.5px; padding: 14px 18px; }
.k-careful .stagebody > .view:last-child { --z: 2.2; width: 720px; }
.k-careful .tipbox { font-size: 16px; padding: 18px 22px; margin: 0; }
.k-signs .stagebody > .view:last-child { --z: 2.0; }
.k-signs .sg { padding: 16px 14px; }
.k-signs .sgd { text-wrap: balance; }
.bigmark { font-size: 2.2em; line-height: 1; vertical-align: -0.12em; } .k-signs .sgt { font-size: 14px; } .k-signs .sga { font-size: 28px; margin: 10px 0; } .k-signs .sgd { font-size: 13px; }
.k-colourkey .stagebody > .view:last-child { --z: 1.75; margin-top: 50px; }
.k-colourkey .kk { padding: 11px 14px; }
.k-colourkey .kkd { font-size: 12px; }
.k-colourkey .oldrow { font-size: 12.5px; } .k-colourkey .oldc { font-size: 12px; }
.k-glance .stagebody > .view:last-child { --z: 1.8; margin-top: 50px; }
.k-glance table.glance { display: table !important; font-size: 13px; }
.k-glance .glance td { padding: 11px 14px; } .k-glance .gex { font-size: 24px; } .k-glance .garr { font-size: 15px; } .k-glance .gd { font-size: 12px; }
.k-glance .glance .pill { font-size: 12px; }
.k-rulebox .stagebody > .view:last-child { --z: 2.15; width: 760px; }
.k-rulebox .rbox { font-size: 16px; line-height: 1.7; padding: 18px 22px; margin: 0; }
.hl { background-image: linear-gradient(transparent 58%, rgba(245,200,75,.75) 58%); background-repeat: no-repeat; background-size: 0% 100%; }
.k-five .stagebody > .view { --z: 2.0; width: 800px; }
.k-five .three { margin: 0; }
.k-five .three h3 { font-size: 20px; }
.k-five .wc { width: 32px; height: 32px; font-size: 24px; } .k-five .three ol { font-size: 15px; line-height: 2.2; }

/* examples */
.k-example .stagebody > .view:last-child { margin-top: 60px; }
.k-example .ex { padding: 22px 26px 18px; margin: 0; border-radius: 16px; }
.k-example .exh { font-size: 17px; margin-bottom: 14px; }
.k-example .exh .qn { font-size: 15px; padding: 4px 11px; }
.k-example .ex .sbox { gap: 10px; overflow: visible; padding-top: 6px; }
.k-example .ex .kt { font-size: 42px; line-height: 1.45; }
.k-example .ex .kw { min-width: 96px; padding: 12px 8px 6px; }
.k-example .ex .vc { width: 36px; height: 36px; font-size: 24px; }
.k-example .ex .klab { font-size: 11.5px; margin-top: 3px; }
.k-example .ex .klab.muted { margin-top: 39px; }
.k-example .ex .kgl { font-size: 12.5px; }
.k-example .kg { position: relative; border-width: 2.5px; padding: 4px 8px 8px; }
.k-example .kw.ghost .kt { font-size: 28px !important; }
.k-example .kw.ghost .kt { opacity: .35; }
.k-example .ex .vc { margin-top: 8px; }
.k-example .kw.small { background: transparent; }
.k-example .xls { margin-top: 14px; padding-top: 10px; }
.k-example .xl { font-size: 14.5px; margin: 7px 0; }
.k-example .xl .pill { min-width: 128px; font-size: 12px; }
.k-example .tipbox.in { font-size: 14.5px; margin-top: 12px; }
.k-example .ab { font-size: 1.15em; }
/* the reading underline and the question mark */
.k-example .kw { position: relative; }
.k-example .kt { position: relative; }
.rwl { position: absolute; left: 6%; right: 6%; bottom: 2px; height: 5px; border-radius: 2px; background: var(--gold); transform: scaleX(0); transform-origin: right center; }
.askq { position: absolute; top: -26px; left: calc(50% - 17px); width: 34px; height: 34px; border-radius: 50%; background: var(--gold); color: var(--ink);
  font: 700 20px/34px var(--font); text-align: center; opacity: 0; z-index: 2; }

/* your turn */
.k-yourturn .stagebody > .view { --z: 1.55; width: 1080px; }
.k-yourturn h2 { margin: 0 0 6px !important; font-size: 22px; }
.k-yourturn .sub { font-size: 14px; margin-bottom: 16px; }
.ptgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.pt { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 10px 14px; display: grid; grid-template-columns: auto 1fr; gap: 2px 10px; align-items: center; }
.pt .qn { grid-row: span 2; font-size: 12px; padding: 3px 8px; }
.ptar { font-family: var(--arabic); font-size: 25px; line-height: 1.7; text-align: right; }
.ptar .sw { border-bottom: 2px dashed var(--teal); padding: 0 3px; margin: 0 4px; display: inline-block; }
.pten { font-size: 12.5px; color: var(--muted); font-style: italic; }
"""


def example_dom_prep(inner, lesson, num):
    """Initial (un-boxed) state for an example, plus hooks for the cues."""
    x = lesson.ex[num]
    # group colours as CSS variables, boxes start neutral
    kg = list(re.finditer(r'<div class="kg" style="border-color:(#[0-9a-f]{6});background:(#[0-9a-f]{6})">', inner))
    out, last = [], 0
    for m in kg:
        b, bg = m.group(1), m.group(2)
        out.append(inner[last:m.start()])
        out.append(f'<div class="kg" style="--gb:{b};--gbg:{bg};border-color:{rgba(b, 0)};background:{rgba(bg, 0)}">')
        last = m.end()
    out.append(inner[last:])
    inner = "".join(out)
    # small boxes (owner, after a preposition, adjective, after wa) start without colour
    inner = re.sub(r'<div class="kw small" style="border-color:(#[0-9a-f]{6})">',
                   lambda m: f'<div class="kw small" style="--sb:{m.group(1)};border-color:{rgba(m.group(1), 0)}">', inner)
    # reading underline under every visible word, numbered in reading order
    n = [0]
    def kt(m):
        if 'class="kw ghost"' in m.group(1):
            return m.group(0)
        i = n[0]; n[0] += 1
        return f'{m.group(1)}<div class="kt">{m.group(2)}<span class="rwl rw{i}"></span></div>'
    inner = re.sub(r'(<div class="kw[^"]*"[^>]*>)<div class="kt">(.*?)</div>', kt, inner)
    # the question bubble sits on the group's first (head) word
    inner = re.sub(r'(<div class="kgw" dir="rtl"><div class="kw[^"]*"[^>]*>)', r'\1<span class="askq">?</span>', inner)
    # size the card to its content: big Arabic for short sentences, still fitting long ones
    letters = lambda w: len([c for c in w if not ("\u064B" <= c <= "\u0652")])
    row = 52 + 10 * (len(x["groups"]) - 1)
    for g in x["groups"]:
        row += 22 + sum(max(112, 22 * letters(w["t"]) + 34) + 6 for w in g["ws"])
    W = max(720, row)
    wrap = lambda chars, width: max(1, -(-chars * 7.6 // width))
    H = 40 + 52 + 178 + 26
    H += sum(31 * wrap(len(re.sub(r"[{}]", "", l["text"])), W - 200) for l in x["lines"])
    if x["tip"]:
        H += 36 + 23 * wrap(len(re.sub(r"[{}]", "", x["tip"])) + 6, W - 60)
    z = round(min(2.25, 790 / H, 1820 / W), 3)
    k = inner.rfind('<div class="view">')
    inner = inner[:k] + f'<div class="view" style="--z:{z};width:{W}px">' + inner[k + len('<div class="view">'):]
    return inner


def initial_css(sid, kind):
    S = f"#{sid}"
    hide = {
        "hero": [".hero h1", ".hero p"],
        "chapter": ["h2", ".sub"],
        "cases": [".case"],
        "scope": [".scope", ".scope li"],
        "rules": [".rr"],
        "careful": [".stagebody > .view:last-child > *"],
        "signs": [".sg"],
        "colourkey": [".kk", ".oldrow"],
        "glance": ["table.glance tr:not(:first-child)"],
        "rulebox": [".stagebody > .view:last-child > *"],
        "five": [".three li"],
        "yourturn": [".stagebody > .view > *"],
        "example": [".exh", ".sbox", ".xl", ".tipbox", ".kgl", ".vc", ".klab"],
    }[kind]
    return f'{", ".join(f"{S} {h}" for h in hide)} {{ opacity: 0; }}'


THUMB_CSS = r"""
.thumb { position: absolute; inset: 0; background: var(--paper); display: flex; flex-direction: column; }
.thumb .stagebody { top: 78px; justify-content: center; gap: 34px; }
.thumb .view.th-ex .ex { margin: 0; }
.thumb .view.th-hero .hero { margin: 0; }
.thumb .stagebody > .view.th-hero { --z: 1.75; width: 1000px; }
.thumb .hero { padding: 26px 36px 24px; }
.thumb .hero h1 { font-size: 44px; margin: 6px 0 0; }
.thumb .hero p { display: none; }
.thumb .wm { font-size: 100px; right: 36px; top: 16px; }
.thumb .stagebody > .view.th-ex { --z: 1.75; width: 1000px; }
.thumb .ex { padding: 16px 26px 14px; border-radius: 16px; }
.thumb .exh, .thumb .xls { display: none; }
.thumb .ex .kt { font-size: 50px; line-height: 1.45; }
.thumb .ex .kw { min-width: 110px; padding: 12px 10px 6px; }
.thumb .ex .vc { width: 40px; height: 40px; font-size: 26px; }
.thumb .ex .klab { font-size: 12px; margin-top: 3px; }
.thumb .ex .kgl { font-size: 13px; }
.thumb .kg { border-width: 2.5px; padding: 4px 8px 8px; }
"""


def build_thumbnail(out, data, lesson, brand):
    """A still in the site's style: the lesson hero over example 1 with its boxes lit."""
    pdir = out / "thumbnail"
    if pdir.exists():
        shutil.rmtree(pdir)
    pdir.mkdir(parents=True)
    shutil.copytree(out / "assets", pdir / "assets")
    (pdir / "assets" / "thumb.css").write_text(THUMB_CSS, encoding="utf-8")
    shutil.copy(out / "hyperframes.json", pdir / "hyperframes.json")
    (pdir / "meta.json").write_text(json.dumps({"id": "thumbnail", "name": "thumbnail"}))
    first = data["examples"][2]  # example 1 (after A and B)
    bar = (f'<div class="vbar"><span class="brand">{brand}</span><span class="crumb">{esc(data["title"])}</span>'
           f'<span class="tabs"><span class="tab" aria-current="true">Lesson</span><span class="tab" aria-current="false">Practice</span></span></div>')
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1920, height=1080">
<link rel="stylesheet" href="assets/site.css"><link rel="stylesheet" href="assets/video.css"><link rel="stylesheet" href="assets/thumb.css">
<script src="assets/js/gsap.min.js"></script></head>
<body><div id="root" data-composition-id="thumbnail" data-start="0" data-duration="1" data-width="1920" data-height="1080">
<section class="scene clip thumb k-example" data-start="0" data-duration="1" style="opacity:1">{bar}
<div class="stagebody"><div class="view th-hero">{data["hero_html"]}</div><div class="view th-ex">{first["html"]}</div></div></section>
</div><script>window.__timelines = window.__timelines || {{}}; const tl = gsap.timeline({{paused:true}}); tl.set({{}}, {{}}, 1);
window.__timelines["thumbnail"] = tl; tl.seek(0);</script></body></html>
"""
    (pdir / "index.html").write_text(page, encoding="utf-8")


def build(lid="nasb", only=None):
    ldir = VIDEO / "lessons" / lid
    data = json.loads((ldir / "lesson.json").read_text(encoding="utf-8"))
    script = json.loads((ldir / "script.json").read_text(encoding="utf-8"))
    tpath = ldir / "timings.json"
    timings = json.loads(tpath.read_text(encoding="utf-8")) if tpath.exists() else {}
    lesson = Lesson(data)
    out = VIDEO / "build" / lid
    if out.exists() and only is None:
        shutil.rmtree(out)
    (out / "assets" / "fonts").mkdir(parents=True, exist_ok=True)
    (out / "assets" / "js").mkdir(parents=True, exist_ok=True)
    nm = VIDEO / "node_modules"
    for f in ["noto-sans-latin-wght-normal.woff2", "noto-sans-latin-ext-wght-normal.woff2", "noto-sans-latin-wght-italic.woff2"]:
        shutil.copy(nm / "@fontsource-variable/noto-sans/files" / f, out / "assets/fonts" / f)
    shutil.copy(nm / "@fontsource-variable/noto-sans-arabic/files/noto-sans-arabic-arabic-wght-normal.woff2", out / "assets/fonts")
    shutil.copy(nm / "gsap/dist/gsap.min.js", out / "assets/js/gsap.min.js")
    (out / "assets" / "site.css").write_text(site_css(), encoding="utf-8")
    (out / "assets" / "video.css").write_text(VIDEO_CSS, encoding="utf-8")
    (out / "hyperframes.json").write_text(json.dumps({"paths": {"assets": "assets"}}, indent=1))
    (out / "meta.json").write_text(json.dumps({"id": lid, "name": f"{lid}-lesson-video"}))
    brand = brand_html()

    segs = script["segments"]
    plan = dict(lesson=lid, fps=FPS, parts=[], estimated=not timings)
    estimated = 0
    for pid, prefixes in PARTS:
        psegs = [s for s in segs if any(s["scene"].startswith(p) for p in prefixes)]
        if not psegs:
            continue
        # ---- times
        t = LEAD
        for s in psegs:
            ln = timings.get(s["id"], {}).get("dur")
            if ln is None:
                ln = est_len(s); estimated += 1
            s["_t"], s["_len"] = round(t, 3), round(ln, 3)
            t += ln + s.get("pause", 0.25)
        dur = round(t + TAIL, 3)
        dur = round(round(dur * FPS) / FPS, 3)
        scenes = list(dict.fromkeys(s["scene"] for s in psegs))
        starts = []
        for i, sc in enumerate(scenes):
            first = next(s for s in psegs if s["scene"] == sc)
            starts.append(0.0 if i == 0 else round(first["_t"] - SCENE_PRE, 3))
        tl, sections, css_init = TL(), [], []
        chapter_names = []
        for i, sc in enumerate(scenes):
            st = starts[i]
            en = starts[i + 1] + XFADE if i + 1 < len(scenes) else dur
            ssegs = [s for s in psegs if s["scene"] == sc]
            kind, inner = lesson.body(sc, ssegs)
            if kind == "example":
                inner = example_dom_prep(inner, lesson, re.match(r".*-ex(\w+)$", sc).group(1))
            sid = "s-" + sc
            bar = (f'<div class="vbar"><span class="brand">{brand}</span><span class="crumb">{esc(data["title"])}</span>'
                   f'<span class="tabs"><span class="tab" aria-current="{"false" if kind == "yourturn" else "true"}">Lesson</span>'
                   f'<span class="tab" aria-current="{"true" if kind == "yourturn" else "false"}">Practice</span></span></div>')
            sections.append(f'<section id="{sid}" class="scene clip k-{kind}" data-start="{st:.3f}" data-duration="{en - st:.3f}">'
                            f'{bar}<div class="stagebody">{inner}</div></section>')
            css_init.append(initial_css(sid, kind))
            tl.add(f'tl.to("#{sid}", {{opacity:1, duration:{XFADE if i else 0.5}, ease:"power1.inOut"}}, {st:.3f});')
            if kind in ("hero", "chapter") and i == 0 or kind == "chapter":
                pass
            state = {}
            if kind not in ("hero", "chapter", "example", "yourturn", "rulebox", "careful"):
                pass
            for s in ssegs:
                ct = max(st + (0.25 if i else 0.4), s["_t"] - CUE_LEAD)
                for c in s["cues"]:
                    cue_js(tl, lesson, sc, kind, sid, c, ct, s["_len"], None, state)
            if kind == "yourturn":
                tl.fade_up(f"#{sid} .stagebody > .view > h2", st + 0.3)
                tl.fade_up(f"#{sid} .stagebody > .view > .sub", st + 0.7)
                tl.fade_up(f"#{sid} .ptgrid", st + 1.2)
            if kind in ("hero",) and not any(s["cues"] for s in ssegs):
                tl.fade_up(f"#{sid} .hero h1", st + 0.4)
            ch = lesson.chapter_of(sc)
            if kind == "chapter" or (sc == "hero"):
                chapter_names.append((st, "Introduction" if sc == "hero" else f'{ch} {re.sub("<.*?>", "", lesson.sec[ch]["title"])}'))
            elif kind == "five":
                chapter_names.append((st, re.sub("<.*?>", "", re.search(r"<h3>(.*?)</h3>", inner).group(1))))
            elif kind == "yourturn":
                chapter_names.append((st, re.sub("<.*?>", "", re.search(r"</span>(.*?)</h2>", data["practice_heading"]).group(1))))
        page = f"""<!doctype html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1920, height=1080">
<link rel="stylesheet" href="assets/site.css"><link rel="stylesheet" href="assets/video.css">
<style>{chr(10).join(css_init)}</style>
<script src="assets/js/gsap.min.js"></script></head>
<body><div id="root" data-composition-id="{pid}" data-start="0" data-duration="{dur:.3f}" data-width="1920" data-height="1080">
{chr(10).join(sections)}
</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(tl.lines)}
tl.set({{}}, {{}}, {dur:.3f});
window.__timelines["{pid}"] = tl;
tl.seek(0);
</script></body></html>
"""
        if only is None or only == pid:
            pdir = out / pid
            if (pdir / "assets").exists():
                shutil.rmtree(pdir / "assets")
            pdir.mkdir(parents=True, exist_ok=True)
            shutil.copytree(out / "assets", pdir / "assets")
            for f in ("hyperframes.json",):
                shutil.copy(out / f, pdir / f)
            (pdir / "meta.json").write_text(json.dumps({"id": pid, "name": pid}))
            (pdir / "index.html").write_text(page, encoding="utf-8")
        plan["parts"].append(dict(
            id=pid, duration=dur, chapters=[dict(t=t0, title=n) for t0, n in chapter_names],
            scenes=[dict(id=sc, start=starts[i]) for i, sc in enumerate(scenes)],
            segments=[dict(id=s["id"], t=s["_t"], len=s["_len"], lang=s["lang"], text=s["text"]) for s in psegs]))
    if only is None:
        build_thumbnail(out, data, lesson, brand)
    (out / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
    total = sum(p["duration"] for p in plan["parts"])
    print(f"built {out.relative_to(ROOT)}: {len(plan['parts'])} parts, {total / 60:.1f} min"
          + (f" ({estimated} segment lengths estimated)" if estimated else ""))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    only = None
    if "--only" in args:
        k = args.index("--only"); only = args[k + 1]; del args[k:k + 2]
    build(args[0] if args else "nasb", only)
