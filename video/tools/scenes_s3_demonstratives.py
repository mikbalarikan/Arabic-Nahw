"""Scenes for the lesson video "Pointing words" (lesson id s3-demonstratives, Stage 3 unit 3).

Loaded by build_composition.py (lesson_for). Every block's markup comes from lesson.json, i.e. from
content/stage3/u3_demonstratives.py rendered by the site's own course.render_notes(), and is styled by the
site's CSS. This file only maps blocks to scenes, adds 1920x1080 sizes and the cue animations.
Scene ids and cues: video/lessons/s3-demonstratives/SCRIPT_SPEC.md.

Run directly to print the scene inventory (blocks and the numbered Arabic "marks" of every scene):
  python3 video/tools/scenes_s3_demonstratives.py
"""
import html as H, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_composition as BC  # noqa: E402

# scene id -> (kind, [lesson block numbers i, as in UNIT["notes"]])
SCENES = {
    "hero":         ("hero", [0]),
    "c01-title":    ("chapter", [2]),
    "c01-table":    ("table", [3]),
    "c01-words":    ("words", [4, 5]),
    "c01-rule":     ("box", [6]),
    "c01-tip":      ("box", [7]),
    "c02-title":    ("chapter", [9]),
    "c02-table":    ("table", [10]),
    "c02-tip":      ("box", [11]),
    "c03-title":    ("chapter", [13]),
    "c03-cols":     ("cols", [14]),
    "c03-examples": ("examples", [15]),
    "c03-tips":     ("tips", [16, 17]),
    "c04-title":    ("chapter", [19]),
    "c04-examples": ("examples", [20]),
    "c05-title":    ("chapter", [22]),
    "c05-examples": ("examples", [23]),
    "c05-cols":     ("cols", [24]),
    "c06-title":    ("chapter", []),
    "c06-rule":     ("box", [26]),
    "c06-table":    ("table", [27]),
    "summary":      ("summary", [28]),
    "outro-yourturn": ("yourturn", []),
}

# elements that hold Arabic, numbered in document order inside a scene's content (not the heading)
MARK_RE = re.compile(r'<(bdi) class="ab">|<(td) class="tar">|<(div) class="(exa|wta)"[^>]*>|<(span) class="(kkar)">')

CSS = r"""
/* shared: the gold "being read" highlight on Arabic */
.am { border-radius: 6px; background-color: rgba(245,200,75,0); box-shadow: 0 0 0 0 rgba(245,200,75,0); }
/* inline Arabic: a box no taller than its own line, so the highlight never covers the lines above or below */
.stagebody bdi.am { display: inline-block; line-height: 1.25; vertical-align: baseline; }
td.am { box-shadow: inset 0 0 0 0 rgba(245,200,75,0); }
.k-chapter .sub .ab, .k-box .ab, .k-tips .ab, .k-summary .ab, .k-words .ab, .k-table .ab { font-size: 1.3em; }
.stagebody .ab { line-height: 1.5; }
.stagebody bdi.ab { white-space: nowrap; }   /* an Arabic phrase never breaks across lines (reading order) */

/* chapter title + its first paragraph as the sub-line */
.k-chapter .sub { font-size: 16px; }

/* tables */
.k-table .stagebody > .view:last-child { --z: 2.0; width: 800px; margin-top: 40px; }
.k-table .tblwrap { margin: 0; overflow: visible; }
.k-table table.glance { display: table !important; font-size: 15px; }
.k-table .glance th { font-size: 13.5px; padding: 10px 14px; }
.k-table .glance td { padding: 10px 14px; vertical-align: middle; }
.k-table .s0t td.tar { font-size: 28px; line-height: 1.6; }
.k-table .glance td .ab { font-size: 1.75em; margin-right: 6px; }
.k-table .t-c02 .glance td .ab { font-size: 1.35em; margin: 0 2px; }
.k-table .stagebody > .view.t-c02 { --z: 1.75; width: 960px; }
.k-table .stagebody > .view.t-c06 { --z: 2.3; width: 620px; }
.k-table .t-c06 .s0t td.tar { font-size: 32px; text-align: center; }
.k-table .t-c06 .glance th { text-align: center; }
.k-table .t-c06 .glance th:first-child { text-align: left; }

/* words + paragraph */
.k-words .stagebody > .view:last-child { --z: 2.2; width: 720px; margin-top: 30px; }
.k-words .wtiles { justify-content: center; gap: 22px; margin: 0 0 22px; }
.k-words .wt0 { min-width: 150px; padding: 10px 20px 12px; }
.k-words .wta { font-size: 40px; }
.k-words .wtl { font-size: 15px; } .k-words .wts { font-size: 14px; }
.k-words .s0p { font-size: 16px; line-height: 1.8; max-width: none; margin: 0; text-align: center; }

/* rule and tip boxes */
.k-box .stagebody > .view:last-child { --z: 2.15; width: 760px; margin-top: 30px; }
.k-box .rbox, .k-box .tipbox { font-size: 16.5px; line-height: 1.95; padding: 20px 24px; margin: 0; }
.k-tips .stagebody > .view:last-child { --z: 2.0; width: 820px; margin-top: 50px; }
.k-tips .tipbox { font-size: 16px; line-height: 1.9; padding: 16px 22px; margin: 0 0 16px; }
.hl { background-image: linear-gradient(transparent 58%, rgba(245,200,75,.75) 58%); background-repeat: no-repeat; background-size: 0% 100%; }

/* two or three coloured cards */
.k-cols .stagebody > .view:last-child { --z: 2.0; width: 820px; margin-top: 40px; }
.k-cols .kkgrid { margin: 0; gap: 14px; }
.k-cols .kk { padding: 14px 16px; }
.k-cols .kkt { font-size: 15px; }
.k-cols .kkar { font-size: 26px; }
.k-cols .kkd { font-size: 14px; line-height: 1.7; }
.k-cols .c3 .kkgrid { grid-template-columns: 1fr 1fr 1fr; }
.k-cols .c3 .kkt { flex-direction: column; align-items: flex-start; gap: 6px; }
.k-cols .c3 .kkar { white-space: nowrap; align-self: flex-end; font-size: 30px; margin-bottom: 10px; }

/* example lists */
.k-examples .stagebody > .view:last-child { --z: 1.85; width: 900px; margin-top: 56px; }
.k-examples .exlist { margin: 0; gap: 9px; }
.k-examples .exl { padding: 8px 18px; grid-template-columns: minmax(0, 1fr) minmax(0, 1.05fr); }
.k-examples .exa { font-size: 27px; line-height: 1.65; }
.k-examples .exa.am { padding: 0 8px; }
.k-examples .exe { font-size: 14.5px; }
.k-examples .exn { font-size: 13px; color: #5f6672; }
.k-examples .exn .ab { font-size: 1.3em; }
.k-examples .stagebody > .view.n5 { --z: 1.62; width: 980px; }

/* summary */
.k-summary .stagebody > .view { --z: 2.0; width: 820px; }
.k-summary .three { margin: 0; }
.k-summary .three h3 { font-size: 20px; }
.k-summary .three ol { font-size: 15.5px; line-height: 2.0; }

/* your turn */
.k-yourturn .stagebody > .view { --z: 1.8; width: 900px; }
.k-yourturn .ptgrid { grid-template-columns: 1fr 1fr; }
.k-yourturn .pt { grid-template-columns: auto 1fr; padding: 12px 16px; }
.k-yourturn .pt .qn { font-size: 13px; grid-row: auto; }
.k-yourturn .ptt { font-size: 16px; font-weight: 600; }

/* poster / thumbnail: the hero over the table to learn */
.thumb .th-tbl .tblwrap { margin: 0; overflow: visible; }
.thumb .th-tbl table.glance { display: table !important; font-size: 15px; background: var(--card); }
.thumb .th-tbl .glance th { font-size: 13.5px; padding: 8px 14px; }
.thumb .th-tbl .glance td { padding: 6px 14px; vertical-align: middle; }
.thumb .th-tbl .glance td .ab { font-size: 1.9em; margin-right: 6px; }
"""

HIDE = {
    "chapter": ["h2", ".sub"],
    "table": ["table.glance tr:not(:first-child)"],
    "words": [".wt0", ".s0p"],
    "box": [".stagebody > .view:last-child > *"],
    "tips": [".tipbox"],
    "cols": [".kk"],
    "examples": [".exl"],
    "summary": [".three li"],
    "yourturn": [".stagebody > .view > *"],
}


def norm_ar(s):
    return re.sub(r"[\s.،؟?!\"]+", " ", s).strip()


class SceneLesson(BC.Lesson):
    css = CSS
    hide = HIDE

    def __init__(self, data):
        self.d = data
        self.R = data.get("roles", {})
        self.sec = {s["num"]: s for s in data["sections"]}
        self.blk = {b["i"]: b for s in data["sections"] for b in s["blocks"]}
        self.marks = {}   # scene -> [plain text of mark k]

    # ---- helpers
    def h2(self, n):
        s = self.sec[n]
        return f'<h2><span class="num">{n}</span>{s["title"]}</h2>'

    def chapter_name(self, scene, kind):
        if scene == "hero":
            return "Introduction"
        if kind == "chapter":
            ch = self.chapter_of(scene)
            return f'{ch} {H.unescape(re.sub("<.*?>", "", self.sec[ch]["title"]))}'
        if kind == "summary":
            return "In short"
        if kind == "yourturn":
            return "Your turn"
        return None

    def thumbnail_html(self):
        b = self.blk[3]["html"]   # the table to learn
        return f'<div class="th-tbl">{b}</div>'

    def number_marks(self, scene, content):
        """Give every Arabic element of the scene's content a class am<k>; remember its text."""
        texts, tags, out, last = [], [], [], 0
        for m in MARK_RE.finditer(content):
            k = len(texts)
            tag = m.group(0)
            new = tag.replace('class="', f'class="am am{k} ', 1)
            out.append(content[last:m.start()]); out.append(new); last = m.end()
            # the element's text: up to its closing tag
            name = m.group(1) or m.group(2) or m.group(3) or m.group(5)
            end = content.index(f"</{name}>", m.end())
            tags.append(name)
            texts.append(H.unescape(re.sub(r"<[^>]+>", "", content[m.end():end])).strip())
        out.append(content[last:])
        self.marks[scene] = texts
        self.mtags = getattr(self, "mtags", {})
        self.mtags[scene] = tags
        return "".join(out)

    # ---- scenes
    def body(self, scene, segs):
        if scene not in SCENES:
            raise SystemExit(f"no renderer for scene {scene}")
        kind, blocks = SCENES[scene]
        if kind == "hero":
            return "hero", f'<div class="view">{self.d["hero_html"]}</div>'
        ch = self.chapter_of(scene)
        if kind == "chapter":
            sub = ""
            if blocks:
                p = self.blk[blocks[0]]["html"]
                sub = self.number_marks(scene, p.replace('<p class="s0p">', '<p class="sub">'))
            out = "chapter", f'<div class="view chap">{self.h2(ch)}{sub}</div>'
        elif kind == "yourturn":
            cards = "".join(f'<div class="pt"><span class="qn">{p["n"]}</span><div class="ptt">{BC.esc(p["title"])}</div></div>'
                            for p in self.d["practice_cards"])
            out = "yourturn", (f'<div class="view yt"><h2>Your turn</h2><p class="sub">Open the Practice tab. '
                               f'Six cards, then the homework.</p><div class="ptgrid">{cards}</div></div>')
        else:
            content = "".join(self.blk[i]["html"] for i in blocks)
            content = self.number_marks(scene, content)
            if kind == "box":
                for n, phrase in enumerate(c[3:] for s in segs for c in s["cues"] if c.startswith("hl:")):
                    content = BC.wrap_phrase(content, phrase, f"hl{n}")
            head = f'<div class="view chead">{self.h2(6 if scene == "summary" else ch)}</div>' if kind != "summary" else ""
            out = kind, head + f'<div class="view {self.view_class(scene, kind)}">{content}</div>'
        self.auto_marks(scene, segs)
        return out

    def auto_marks(self, scene, segs):
        """An Arabic reading without a mark cue lights the first element of the scene that holds exactly its text."""
        texts = [norm_ar(t) for t in self.marks.get(scene, [])]
        for s in segs:
            if s["lang"] != "ar" or any(c.startswith("mark:") for c in s["cues"]):
                continue
            t = norm_ar(s["text"])
            if t in texts:
                s["cues"] = list(s["cues"]) + [f"mark:{texts.index(t)}"]

    def prep(self, scene, kind, inner):
        # Noto Sans Arabic's glyph boxes are taller than the site's line boxes; nothing visible overflows
        # (checked on snapshots), so tell the layout audit these text boxes are fine as they are.
        inner = re.sub(r'<(bdi|td|div|span) class="am ', r'<\1 data-layout-allow-overflow class="am ', inner)
        inner = inner.replace('<div class="wm"', '<div data-layout-allow-overflow class="wm"')
        return inner

    def view_class(self, scene, kind):
        extra = []
        if kind == "table":
            extra.append(f"t-{scene[:3]}")
        if kind == "cols" and len(re.findall('class="kk"', self.blk[SCENES[scene][1][0]]["html"])) == 3:
            extra.append("c3")
        if kind == "examples":
            extra.append(f'n{len(self.blk[SCENES[scene][1][0]]["src"]["items"])}')
        return " ".join(extra)

    def cue(self, tl, scene, kind, S, name, arg, t, seg_len, state):
        if name == "mark":
            k = int(arg)
            if k >= len(self.marks.get(scene, [])):
                raise SystemExit(f"{scene}: mark:{k} out of range ({len(self.marks.get(scene, []))} marks)")
            sel = f"{S} .am{k}"
            tag = self.mtags[scene][k]
            if kind == "summary":    # dark panel: solid gold with dark text
                on, off = 'backgroundColor:"rgba(245,200,75,0.95)", color:"#10302f"', 'backgroundColor:"rgba(245,200,75,0)", color:"#ffffff"'
            elif tag == "bdi":       # inline: fill only (no spread over the neighbouring lines)
                on, off = 'backgroundColor:"rgba(245,200,75,0.55)"', 'backgroundColor:"rgba(245,200,75,0)"'
            elif tag == "td":        # table cell: inset ring stays inside the table
                on = 'backgroundColor:"rgba(245,200,75,0.45)", boxShadow:"inset 0 0 0 3px rgba(245,200,75,0.8)"'
                off = 'backgroundColor:"rgba(245,200,75,0)", boxShadow:"inset 0 0 0 0px rgba(245,200,75,0)"'
            else:
                on = 'backgroundColor:"rgba(245,200,75,0.55)", boxShadow:"0 0 0 3px rgba(245,200,75,0.55)"'
                off = 'backgroundColor:"rgba(245,200,75,0)", boxShadow:"0 0 0 0px rgba(245,200,75,0)"'
            tl.add(f'tl.to("{sel}", {{{on}, duration:0.25, ease:"power1.out"}}, {t:.3f});')
            tl.add(f'tl.to("{sel}", {{{off}, duration:0.35}}, {t + max(seg_len, 0.8) + 0.35:.3f});')
            return True
        if kind == "chapter" and name == "sub":
            tl.fade_up(f"{S} .sub", t)
            return True
        if kind == "table" and name == "row":
            tl.fade_up(f"{S} table.glance tr:nth-child({int(arg) + 1})", t, 8)
            return True
        if kind == "words" and name == "word":
            tl.fade_up(f"{S} .wt0:nth-child({arg})", t, 14)
            return True
        if kind == "words" and name == "p":
            tl.fade_up(f"{S} .s0p", t, 10)
            return True
        if kind == "tips" and name == "tip":
            tl.fade_up(f"{S} .tipbox:nth-of-type({arg})", t, 12)
            return True
        if kind == "cols" and name == "col":
            tl.fade_up(f"{S} .kk:nth-child({arg})", t, 18, 0.42)
            return True
        if kind == "examples" and name == "ex":
            tl.fade_up(f"{S} .exl:nth-child({arg})", t, 10)
            return True
        if kind == "summary" and name == "item":
            tl.fade_up(f"{S} .three li:nth-child({arg})", t, 10)
            return True
        if kind == "yourturn" and name == "show":
            return True   # the Your turn page fades in by itself
        if kind in ("hero", "chapter") and name in ("title", "sub"):
            return False  # shared hero / chapter cues
        if kind == "box" and name in ("show", "hl"):
            return False  # shared: whole box fades up; hl highlights a phrase
        raise SystemExit(f"{scene}: unknown cue {name}:{arg} for kind {kind}")


def inventory():
    """Print, per scene, its blocks and its numbered Arabic marks (for script writers)."""
    root = Path(__file__).resolve().parents[1]
    data = json.loads((root / "lessons" / "s3-demonstratives" / "lesson.json").read_text(encoding="utf-8"))
    L = SceneLesson(data)
    for sc, (kind, blocks) in SCENES.items():
        L.body(sc, [])
        print(f"## {sc}  (kind {kind}; blocks {blocks})")
        for i in (b for b in blocks if b in L.blk):
            print(f"   block {i} [{L.blk[i]['t']}]: {L.blk[i]['text']}")
        for k, t in enumerate(L.marks.get(sc, [])):
            print(f"   mark:{k}  {t}")


if __name__ == "__main__":
    inventory()
