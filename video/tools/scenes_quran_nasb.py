"""Scenes for the lesson video "Iʿrāb in the Qur'an" (lesson id quran-nasb).

Loaded by build_composition.py (lesson_for). Markup comes from lesson.json, i.e. from content/quran.py,
and is styled by the site's own CSS. This file only adds the 1920x1080 sizes and the cue animations.
Scene ids and cues: video/lessons/quran-nasb/SCRIPT_SPEC.md.
"""
import json, re
from pathlib import Path

import build_composition as BC

CREDIT = Path(__file__).resolve().parents[1] / "lessons" / "quran-nasb" / "recitation.json"

CSS = r"""
/* chapter 1: the three notes and the Also tip */
.k-notes .stagebody > .view:last-child { --z: 1.95; width: 900px; margin-top: 30px; }
.k-notes .rule3 { gap: 12px; margin: 0; }
.k-notes .rr { font-size: 13px; padding: 12px 14px; }
.k-notes .rr b { font-size: 14px; }
.k-notes .ab { font-size: 1.35em; }
.k-also .stagebody > .view:last-child { --z: 2.3; width: 700px; }
.k-also .tipbox { font-size: 16px; padding: 18px 22px; margin: 0; line-height: 1.7; }
.k-also .ab { font-size: 1.3em; }

/* chapter 3: the 10-verse table */
.k-overview .stagebody > .view:last-child { --z: 1.62; width: fit-content; margin-top: 64px; }
.k-overview table.glance { display: table !important; }
.k-overview .vt td { padding: 4px 10px; }
.k-overview .vt .vx { font-size: 21px; }
.k-overview .vt .vr { font-size: 11px; }
.k-overview .vt .pill { font-size: 12px; }  /* >= 19px bold on screen: WCAG large text */

/* verse scenes: the example card of the Naṣb video, plus the reference and the key lines */
.k-verse .stagebody > .view:not(.chead) { margin-top: 70px; }
.k-verse .ex { padding: 20px 26px 16px; margin: 0; border-radius: 16px; }
.k-verse .exh { font-size: 17px; margin-bottom: 14px; }
.k-verse .exh .qn { font-size: 15px; padding: 4px 11px; }
.k-verse .exh .qref { margin-left: auto; font-size: 13px; }
.k-verse .exh .qref bdi { font-size: 16px; }
.k-verse .qbox { position: relative; width: fit-content; margin: 0 auto; }
.k-verse .qglow { position: absolute; inset: -6px -10px; border: 3px solid var(--gold); border-radius: 16px;
  box-shadow: 0 0 18px rgba(245,200,75,.55); opacity: 0; pointer-events: none; }
.k-verse .ex .sbox { gap: 10px; overflow: visible; padding-top: 6px; justify-content: center; }
.k-verse .ex .kt { font-size: 40px; line-height: 1.55; }
.k-verse .ex .kw { min-width: 84px; padding: 2px 6px 6px; position: relative; }
.k-verse .ex .vc { width: 34px; height: 34px; font-size: 23px; }
.k-verse .ex .klab { font-size: 11px; margin-top: 3px; white-space: nowrap; }
.k-verse .ex .klab.muted { margin-top: 37px; }
.k-verse .ex .kgl { font-size: 12px; }
.k-verse .kg { position: relative; border-width: 2.5px; padding: 4px 8px 8px; }
.k-verse .kw.ghost .kt { font-size: 27px !important; }
.k-verse .kt { position: relative; }
.k-verse .xls.qkl { margin-top: 12px; padding-top: 8px; display: grid; grid-auto-flow: column; column-gap: 34px; }
.k-verse .qkl .rl { font-size: 13px; margin: 5px 0; gap: 8px; }
.k-verse .qkl .rw { width: 92px; font-size: 21px; }
.k-verse .qkl .rl .pill { min-width: 112px; font-size: var(--pf, 11px); padding: 2px 6px; }
/* the site's muted grey label is too faint for video; use the site's other secondary grey (particle pill text) */
.k-verse .klab.muted { color: #5f6672; }
.k-verse .qkl .ab { font-size: 1.25em; }
.reciter { position: absolute; right: 56px; top: 132px; font-size: 19px; color: var(--muted); opacity: 0; }
.reciter b { color: var(--ink); font-weight: 600; }

/* your turn */
.k-yourturn .ptgrid { grid-template-columns: 1fr 1fr; }
.k-yourturn .pt .qn { font-size: 12px; }
.k-yourturn .ptar { line-height: 2.3; }
.k-yourturn .ptar .sw { line-height: 2.25; padding-top: 1px; }
"""

HIDE = {
    "notes": [".rr"],
    "also": [".stagebody > .view:last-child > *"],
    "overview": ["table.glance tr:not(:first-child)"],
    # small pieces (attached pronouns, words after wa ...) stay visible: the verse must be whole while it is
    # recited. Only their frame waits for the group colour (shared example_dom_prep / group cue).
    "verse": [".exh", ".sbox", ".rl", ".kgl", ".vc", ".klab", ".kw.ghost", ".reciter"],
}


class SceneLesson(BC.Lesson):
    css = CSS
    hide = HIDE

    def __init__(self, data):
        self.d = data
        self.R = data["roles"]
        self.sec = {s["num"]: s for s in data["sections"]}
        self.v = {f'v{int(v["num"]):02d}': v for v in data["verses"]}
        self.ex = {}
        cr = json.loads(CREDIT.read_text(encoding="utf-8")) if CREDIT.exists() else {}
        self.credit = cr.get("credit", "Recitation: <b>source to be confirmed</b>")

    def chapter_name(self, scene, kind):
        if scene == "hero":
            return "Introduction"
        if kind == "chapter":
            ch = self.chapter_of(scene)
            return f'{ch} {re.sub("<.*?>", "", self.sec[ch]["title"])}'
        if kind == "verse":
            v = self.v[scene]
            return f'Verse {v["num"]} · {v["ref_en"]}'
        return None

    def thumbnail_html(self):
        """For the poster / thumbnail: verse 1 in its coloured boxes, under the lesson hero."""
        return f'<div class="ex"><div class="exh"></div>{self.d["verses"][0]["boxes_html"]}</div>'

    def body(self, scene, segs):
        if scene == "hero":
            return "hero", f'<div class="view">{self.d["hero_html"]}</div>'
        ch = self.chapter_of(scene)
        if ch and scene.endswith("-title"):
            sub = self.sec[ch]["sub"]
            subh = f'<p class="sub">{sub}</p>' if sub else ""
            return "chapter", f'<div class="view chap">{self.h2(ch)}{subh}</div>'
        head = f'<div class="view chead">{self.h2(ch)}</div>' if ch else ""
        if scene == "c01-notes":
            return "notes", head + f'<div class="view"><div class="rule3">{"".join(self.d["notes"])}</div></div>'
        if scene == "c01-also":
            return "also", head + f'<div class="view">{self.d["also"]}</div>'
        if scene == "c02-key":
            return "colourkey", head + f'<div class="view">{self.d["fragments"]["colour_key"]}</div>'
        if scene == "c03-overview":
            return "overview", head + f'<div class="view">{self.d["overview"]}</div>'
        if scene in self.v:
            v = self.v[scene]
            hdr = (f'<div class="exh"><span class="qn">{v["num"]}</span><i>“{BC.esc(v["tr"])}”</i>'
                   f'<span class="qref">{BC.esc(v["ref_en"])} · <bdi>{BC.esc(v["ref_ar"])}</bdi></span></div>')
            card = (f'<div class="ex">{hdr}<div class="qbox"><span class="qglow"></span>{v["boxes_html"]}</div>'
                    f'<div class="xls qkl">{"".join(v["key_lines"])}</div></div>')
            return "verse", f'<div class="view chead">{self.h2(3)}</div>' + f'<div class="view">{card}</div>' \
                + f'<div class="reciter">{self.credit}</div>'
        if scene.startswith("outro"):
            h = re.search(r"<h2.*?</h2>", self.d["your_turn_heading"], re.S).group(0)
            rows = []
            for v in self.d["verses"]:
                sent = re.search(r'<div class="sent" dir="rtl">(.*?)</div>', v["card_html"], re.S).group(1)
                rows.append(f'<div class="pt"><span class="qn">{v["num"]}</span><div class="ptar" dir="rtl">{sent}</div>'
                            f'<div class="pten">“{BC.esc(v["tr"])}”</div></div>')
            return "yourturn", f'<div class="view yt">{h}<div class="ptgrid">{"".join(rows)}</div></div>'
        raise SystemExit(f"no renderer for scene {scene}")

    def prep(self, scene, kind, inner):
        if kind != "verse":
            return inner
        v = self.v[scene]
        # neutral boxes, "?" marks and reading underlines: the same hooks as the Naṣb examples
        self.ex[v["num"]] = dict(groups=v["groups"], lines=[], tip=None)
        inner = BC.example_dom_prep(inner, self, v["num"])
        # size: widest of the box row and the key lines; height from the key-line rows
        letters = lambda w: len([c for c in w if not ("ً" <= c <= "ْ")])
        row = 52 + 10 * (len(v["groups"]) - 1)
        for g in v["groups"]:
            row += 22 + sum(max(98, 21 * letters(w["t"]) + 30) + 6 for w in g["ws"])
        n = len(v["key_lines"])
        cols = 1 if n <= 5 else 2
        rows = -(-n // cols)
        longest = max(len(t) for t in v["key_lines_text"])
        line_w = 92 + 150 + 30 + 7.2 * longest
        W = int(max(760, row, cols * line_w + 34 * (cols - 1) + 60))
        H = 40 + 50 + 190 + 24 + rows * 33
        z = round(min(2.1, 800 / H, 1800 / W), 3)
        inner = re.sub(r'<div class="view" style="--z:[^"]*">', "<div class=\"view\">", inner)
        k = inner.rfind('<div class="view"><div class="ex">')
        pf = round(max(11, 19.5 / z), 2)   # pills stay >= 19.5px bold on screen (WCAG large text)
        inner = inner[:k] + f'<div class="view" style="--z:{z};width:{W}px;--pf:{pf}px">' + inner[k + len('<div class="view">'):]
        inner = inner.replace('<div class="xls qkl">',
                              f'<div class="xls qkl" style="grid-template-rows:repeat({rows},auto)">')
        # Noto Sans Arabic's glyph boxes are taller than the site's line boxes; nothing visible overflows
        # (checked on snapshots), so tell the layout audit these two text boxes are fine as they are.
        inner = inner.replace('<div class="kt"', '<div data-layout-allow-overflow class="kt"')
        inner = inner.replace('<div class="vc"', '<div data-layout-allow-overflow class="vc"')
        return inner

    def cue(self, tl, scene, kind, S, name, arg, t, seg_len, state):
        if kind == "notes" and name == "note":
            tl.fade_up(f"{S} .rr:nth-child({arg})", t, 20, 0.42)
            return True
        if kind == "overview" and name == "row":
            tl.fade_up(f"{S} table.glance tr:nth-child({int(arg) + 1})", t, 8)
            return True
        if kind == "overview" and name == "rows":
            tl.add(f'tl.fromTo("{S} table.glance tr:not(:first-child)", {{opacity:0, y:8}}, '
                   f'{{opacity:1, y:0, duration:0.3, stagger:0.12, ease:"power2.out"}}, {t:.3f});')
            state["rows"] = True
            return True
        if kind == "yourturn" and name == "show":
            return True  # the Your turn page fades in by itself
        if kind != "verse":
            return False
        if name == "recite":
            # .qglow starts at opacity 0 in CSS, so plain to() tweens give a stable baseline for both recitations
            tl.add(f'tl.to("{S} .qglow", {{opacity:1, duration:0.4, ease:"power1.out"}}, {t:.3f});')
            tl.add(f'tl.to("{S} .qglow", {{opacity:0, duration:0.5}}, {t + max(seg_len, 1.0) + 0.2:.3f});')
            if not state.get("credit"):
                tl.fade_in(f"{S} .reciter", t)
                state["credit"] = True
            return True
        if name == "line":
            tl.fade_up(f"{S} .qkl .rl:nth-child({int(arg) + 1})", t, 8)
            return True
        if name == "vowel":
            # pulse the circle of the group's head word: the first piece that has an ending
            # (a jarr group starts with its particle, which has no circle)
            g = int(arg)
            ws = self.v[scene]["groups"][g]["ws"]
            i = next(k for k, w in enumerate(ws) if w["k"] not in ("particle", "fixed", "hidden") and w["v"])
            sel = f"{S} .kg:nth-child({g + 1}) .kgw > .kw:nth-child({i + 1}) .vc"
            tl.add(f'tl.to("{sel}", {{scale:1.22, duration:0.2, yoyo:true, repeat:3, ease:"sine.inOut"}}, {t + 0.35:.3f});')
            return True
        if name == "group":
            # the shared group cue also gives the small boxes their colour (example_dom_prep sets --sb)
            BC.cue_js(tl, None, scene, "example", S[1:], f"group:{arg}", t, seg_len, None, state)
            if any(w["k"] == "hidden" for w in self.v[scene]["groups"][int(arg)]["ws"]):
                # the hidden doer's box is not part of the recited verse: it appears with its group
                tl.add(f'tl.to("{S} .kg:nth-child({int(arg) + 1}) .kw.ghost", {{opacity:1, duration:0.4, ease:"power2.out"}}, {t + 0.08:.3f});')
            return True
        if name in ("en", "sentence", "ask", "read"):
            BC.cue_js(tl, None, scene, "example", S[1:], f"{name}:{arg}" if arg else name, t, seg_len, None, state)
            return True
        raise SystemExit(f"{scene}: unknown cue {name}:{arg}")
