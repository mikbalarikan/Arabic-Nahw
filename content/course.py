# -*- coding: utf-8 -*-
"""All course data: Stage 0 units (stage0/*.py) and the Stage 1/2 sets. Imported by tools/build_site.py."""

import json, re, html
import build as B, build_ex as X, lesson as L, quran as QN, quran_nominal as N

e = html.escape
DASH = "—"

# ---------- colours / chip sets ----------
COL = {}
for k, v in B.ROLES.items():
    COL[k] = dict(b=v[2], bg=v[3], t=v[4])
for k, v in L.R.items():
    COL[k] = dict(b=v[2], bg=v[3], t=v[4])
COL["fixed"] = COL["particle"] = dict(b="#9aa0a8", bg="#f4f4f2", t="#5f6672")

AC_JOBS = [("topic", "Topic"), ("info", "Info"), ("prep", "Prep"), ("owner", "Owner"),
           ("adj", "Adj"), ("and", "After وَ"), ("fixed", "Fixed")]
NOM_JOBS = AC_JOBS[:-1] + [("fixed", "Fixed / particle")]
NASB_JOBS = [(k, L.CHIPLAB[k]) for k in L.CHIPS] + [("particle", "Particle")]
AC_ENDS = [B.DAMMA, B.DAMMATAN, B.KASRA, B.KASRATAN, DASH]
NASB_ENDS = [L.DAMMA, L.DAMMATAN, L.FATHA, L.FATHATAN, L.KASRA, L.KASRATAN, DASH]

def jobset(lst):
    return [dict(k=k, label=lab, **COL[k]) for k, lab in lst]

# ---------- helpers ----------
def join_map(pieces):
    toks, idx = [], []
    for t in pieces:
        if toks and (toks[-1].endswith("ـ") or t.startswith("ـ") or toks[-1] in ("وَ", "فَ")):
            toks[-1] = toks[-1].rstrip("ـ") + t.lstrip("ـ")
        else:
            toks.append(t)
        idx.append(len(toks) - 1)
    return toks, idx

def disp(t):
    return t.strip("ـ") if len(t) > 1 else t

def make_card(n, head, rows, key_html, note=""):
    stems = [r[0] for r in rows]
    toks, idx = join_map(stems)
    return dict(n=n, head=head, note=note, toks=toks, key=key_html,
                rows=[dict(s=disp(s), end=end, job=job, tok=idx[i]) for i, (s, end, job) in enumerate(rows)])

def strip_page(h):
    h = re.sub(r'<div class="foot">.*?</div>', "", h, flags=re.S)
    return h.replace('class="page"', 'class="sheet"').replace('class="page cards"', 'class="sheet"')

def stars(n):
    return "★" * n + "☆" * (3 - n)

def hidden_of(groups):
    for g in groups:
        for w in g["ws"]:
            if w["k"] == "hidden":
                return w["t"]
    return None

# ---------- lesson builders ----------
def ac_rows(q):
    rows = []
    for w in B.words(q):
        rows.append((B.stem(w), w["v"] or DASH, B.job_of(w)))
    return rows

def nasb_rows(groups, stemf):
    rows = []
    for w in L.flat(groups):
        k = w["k"]
        if k == "particle": job = "particle"
        elif k == "fixed": job = "verb"
        elif k in ("prep", "owner", "adj", "and"): job = k
        else: job = w["role"]
        rows.append((stemf(w), w["v"] or DASH, job))
    return rows

def nom_rows(v):
    rows = []
    for w in N.pieces(v):
        k = w["k"]
        if k in ("particle", "fixed"): job = "fixed"
        elif k in ("prep", "owner", "adj", "and"): job = k
        else: job = w["role"]
        rows.append((QN.qstem(w), w["v"] or DASH, job))
    return rows

def hidden_note(groups):
    h = hidden_of(groups)
    return f"The doer is hidden: {h}. Say it aloud." if h else ""

YOUR_TURN = f'<div class="pb">{L.h2(4, "Your turn", "nomt")}</div>'

def lessons():
    out = []
    qpages = B.build()
    teacher = strip_page(qpages[1])
    teacher = teacher[:teacher.index('<h3 class="sh">')] + "</div>"
    out.append(dict(
        id="quiz", stage=1, title="Iʿrāb Table Quiz", ar="اخْتِبَارُ الطَّاوِلَةِ",
        blurb="15 noun sentences, one student per card at the table. Full iʿrāb of every word.",
        intro=strip_page(qpages[0]), teacher=teacher, ends=AC_ENDS, jobs=jobset(AC_JOBS),
        cards=[make_card(f"Q{i}", dict(en=q["en"], tag=stars(q["lvl"])), ac_rows(q), B.key_card(i, q))
               for i, q in enumerate(B.Q, 1)],
        lvl=[q["lvl"] for q in B.Q]))
    out.append(dict(
        id="exercise", stage=1, title="Iʿrāb Class Exercise", ar="تَمْرِينُ الصَّفِّ",
        blurb="15 new noun sentences for practice in class, with partner checking.",
        intro=strip_page(X.build()[0]), ends=AC_ENDS, jobs=jobset(AC_JOBS),
        cards=[make_card(f"Q{i}", dict(en=q["en"], tag=stars(q["lvl"])), ac_rows(q), X.key_card(i, q))
               for i, q in enumerate(X.Q, 1)]))
    nh = N.build()
    out.append(dict(
        id="quran-nouns", stage=1, title="Rafʿ and Jarr in the Qur'an", ar="الرَّفْعُ وَالجَرُّ فِي القُرْآنِ",
        blurb="10 noun-sentence verses. Topic, information, prepositions and owners only.",
        intro=nh[:nh.index(YOUR_TURN)], ends=AC_ENDS, jobs=jobset(NOM_JOBS),
        cards=[make_card(str(i), dict(en=v["tr"], tag=f'{v["en"]} · {v["ref"]}'), nom_rows(v), N.key(i, v))
               for i, v in enumerate(N.VERSES, 1)]))
    out.append(dict(
        id="nasb", stage=2, title="Naṣb Colour Guide", ar="النَّصْبُ بِالفَتْحَةِ",
        blurb="The verb sentence, the fatha sign, and the four naṣb jobs, with 21 colour-boxed examples.",
        intro=L.lesson(), introLabel="Lesson", ends=NASB_ENDS, jobs=jobset(NASB_JOBS),
        cards=[make_card(f"E{i}", dict(en=p["en"], tag=""), nasb_rows(p["g"], L.stem), L.key_card(i, p),
                         hidden_note(p["g"])) for i, p in enumerate(L.PRACTICE, 1)]))
    qh = QN.build()
    out.append(dict(
        id="quran-nasb", stage=2, title="Iʿrāb in the Qur'an", ar="الإِعْرَابُ فِي القُرْآنِ",
        blurb="10 verses with a past verb and a naṣb noun, mixed with rafʿ and jarr.",
        intro=qh[:qh.index(YOUR_TURN)], ends=NASB_ENDS, jobs=jobset(NASB_JOBS),
        cards=[make_card(str(i), dict(en=v["tr"], tag=f'{v["en"]} · {v["ref"]}'), nasb_rows(v["g"], QN.qstem),
                         QN.key(i, v), hidden_note(v["g"])) for i, v in enumerate(QN.VERSES, 1)]))
    return out

# ---------- css ----------
def strip_at_page(css):
    out, i = [], 0
    while True:
        j = css.find("@page", i)
        if j < 0:
            out.append(css[i:]); break
        out.append(css[i:j])
        k = css.index("{", j); depth = 0
        while True:
            if css[k] == "{": depth += 1
            elif css[k] == "}":
                depth -= 1
                if depth == 0: break
            k += 1
        i = k + 1
    return "".join(out)

def base_css():
    css = "".join(open(f, encoding="utf-8").read() for f in ("style.css", "lesson.css", "quran.css"))
    css = strip_at_page(css)
    css = css.replace('"DejaVu Sans", sans-serif', "var(--font)").replace('"DejaVu Sans"', "var(--font)")
    return css


# ---------------- v2 ----------------

import glob, runpy, os
import colour_guide as CG

e = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))

PAL = {
 "blue": ("#2f7fe0", "#e3eefc", "#1f64bd"), "pink": ("#d63384", "#fde6f1", "#a61e62"),
 "gold": ("#e0a10b", "#fff5d6", "#a87805"), "navy": ("#3a5a85", "#e8eef6", "#2b4668"),
 "teal": ("#0f9d9a", "#dcf4f3", "#0a7471"), "green": ("#22a05a", "#e2f5e9", "#17803f"),
 "red": ("#e04a3a", "#fde7e4", "#b8322a"), "purple": ("#7b4fd6", "#efe8fc", "#5f36b8"),
 "orange": ("#ea7a10", "#fff0df", "#b05705"), "brown": ("#a0612b", "#f5e9dd", "#7b471c"),
 "grey": ("#7d858e", "#eef0f2", "#5a626b"), "olive": ("#6b8e23", "#edf4dc", "#4c6810"),
}
NEUTRAL = ("#0f5257", "#f2f8f8", "#0f5257")

def tx(s):
    """English text with {Arabic} markup -> safe HTML."""
    return L.ar(e(s or ""))

def colour(name):
    b, bg, t = PAL.get(name, NEUTRAL)
    return dict(b=b, bg=bg, t=t)

# ---------------- iʿrāb fields (Stage 1 / 2) ----------------
def end_field(ends):
    return dict(key="end", label="", type="end", options=[dict(k=m, label=(m if m == DASH else "ـ" + m)) for m in ends])
def job_field(jobs):
    return dict(key="job", label="", type="chip", options=[dict(k=j["k"], label=j["label"], b=j["b"], bg=j["bg"], t=j["t"])
                                                           for j in [dict(k=k, label=lab, **COL[k]) for k, lab in jobs]])

def irab_card(n, head, rows, key_html, note=""):
    toks, idx = join_map([r[0] for r in rows])
    return dict(n=n, head=head, note=note, toks=toks, key=key_html,
                rows=[dict(s=disp(s), ans=dict(end=end, job=job), tok=idx[i]) for i, (s, end, job) in enumerate(rows)])

def irab_set(sid, label, ends, jobs, cards):
    return dict(id=sid, label=label, fields=[end_field(ends), job_field(jobs)], cards=cards, colourField="job")

# ---------------- Stage 0 ----------------
def render_notes(blocks):
    out, n = [], 0
    for b in blocks:
        t = b["t"]
        if t == "hero":
            out.append(f'<div class="hero"><div class="eyebrow">{e(b.get("eyebrow",""))}</div><h1>{tx(b["title"])}</h1>'
                       f'<p>{tx(b.get("text",""))}</p><div class="wm" aria-hidden="true">{e(b.get("wm",""))}</div></div>')
        elif t == "h2":
            n += 1
            out.append(f'<h2><span class="num">{n}</span>{tx(b["text"])}</h2>')
        elif t == "p":
            out.append(f'<p class="s0p">{tx(b["text"])}</p>')
        elif t == "rule":
            c = colour(b.get("color"))
            out.append(f'<div class="rbox" style="border-color:{c["b"]};background:{c["bg"]}"><b style="color:{c["t"]}">{tx(b.get("title",""))}.</b> {tx(b.get("text",""))}</div>')
        elif t == "tip":
            out.append(f'<div class="tipbox"><b>Tip:</b> {tx(b["text"])}</div>')
        elif t == "cols":
            items = "".join(
                f'<div class="kk" style="border-left-color:{colour(it.get("color"))["b"]};background:{colour(it.get("color"))["bg"]}">'
                f'<div class="kkt"><span style="color:{colour(it.get("color"))["t"]}"><span class="dot" style="background:{colour(it.get("color"))["b"]}"></span>{tx(it.get("title",""))}</span>'
                f'<span class="kkar">{e(it.get("ar",""))}</span></div><div class="kkd">{tx(it.get("text",""))}</div></div>'
                for it in b["items"])
            out.append(f'<div class="kkgrid s0cols">{items}</div>')
        elif t == "words":
            items = "".join(
                f'<div class="wt0" style="border-color:{colour(it.get("color"))["b"]};background:{colour(it.get("color"))["bg"]}">'
                f'<div class="wta">{e(it["ar"])}</div>'
                + (f'<div class="wtl" style="color:{colour(it.get("color"))["t"]}">{tx(it["label"])}</div>' if it.get("label") else "")
                + (f'<div class="wts">{tx(it["sub"])}</div>' if it.get("sub") else "") + '</div>'
                for it in b["items"])
            out.append(f'<div class="wtiles">{items}</div>')
        elif t == "examples":
            items = "".join(
                f'<div class="exl"><div class="exa" dir="rtl">{e(it["ar"])}</div><div class="exe">{tx(it.get("en",""))}'
                + (f'<div class="exn">{tx(it["note"])}</div>' if it.get("note") else "") + '</div></div>'
                for it in b["items"])
            out.append(f'<div class="exlist">{items}</div>')
        elif t == "table":
            head = "".join(f"<th>{tx(h)}</th>" for h in b["head"])
            rows = "".join("<tr>" + "".join(
                f'<td class="{"tar" if re.search(r"[؀-ۿ]", c) and not re.search(r"[A-Za-z]", c) else ""}">{tx(c)}</td>' for c in r) + "</tr>"
                for r in b["rows"])
            out.append(f'<div class="tblwrap"><table class="glance s0t"><tr>{head}</tr>{rows}</table></div>')
        elif t == "summary":
            lis = "".join(f"<li>{tx(i)}</li>" for i in b["items"])
            out.append(f'<div class="three"><h3>{tx(b.get("title","Summary"))}</h3><ol>{lis}</ol></div>')
    return "".join(out)

def choice_card(n, c):
    fields = []
    for f in c["fields"]:
        opts = [dict(k=o["k"], label=o["label"], **(colour(o["color"]) if o.get("color") else {})) for o in f.get("options", [])]
        fields.append(dict(key=f["key"], label=f.get("label", ""), type="chip", options=opts))
    rows = []
    for r in c["rows"]:
        row = dict(s=r["s"], ans=r["ans"], why=tx(r.get("why", "")))
        if r.get("gloss"): row["gloss"] = r["gloss"]
        if r.get("opts"):
            row["opts"] = {k: [dict(k=o["k"], label=o["label"], **(colour(o["color"]) if o.get("color") else {})) for o in v]
                           for k, v in r["opts"].items()}
        rows.append(row)
    card = dict(n=n, head=dict(en=c["title"], tag=""), fields=fields, rows=rows)
    if c.get("prompt"):
        card["prompt"] = c["prompt"]; card["promptEn"] = c.get("en", "")
    return card

def stage0():
    units = []
    for path in sorted(glob.glob(os.path.join(HERE, "stage0", "u*.py"))):
        U = runpy.run_path(path)["UNIT"]
        units.append(U)
    units.sort(key=lambda u: u["order"])
    out = []
    for U in units:
        sets = [dict(id="practice", label="Practice" if U["id"] != "s0-checkup" else "Check-up",
                     cards=[choice_card(f"P{i}", c) for i, c in enumerate(U["practice"], 1)]),
                dict(id="homework", label="Homework", cards=[choice_card(f"H{i}", c) for i, c in enumerate(U["homework"], 1)])]
        out.append(dict(id=U["id"], stage=0, order=U["order"], title=U["title"], ar=U["ar"], blurb=U["blurb"],
                        intro=render_notes(U["notes"]), introLabel="Lesson", sets=sets))
    return out

# ---------------- Stage 1 / 2 ----------------
def stage12():
    out = []
    cg_cards = [irab_card(f"E{i}", dict(en=q["en"], tag=stars(q["lvl"])), ac_rows(q), B.key_card(i, q).replace(f">Q{i}<", f">E{i}<"))
                for i, q in enumerate(CG.Q, 1)]
    out.append(dict(id="colour-guide", stage=1, title="Iʿrāb Colour Guide", ar="دَلِيلُ الأَلْوَانِ",
                    blurb="The Stage 1 lesson: topic and information, prepositions, owners, adjectives and وَ, with 12 colour-boxed examples.",
                    intro=CG.notes(), introLabel="Lesson",
                    sets=[irab_set("practice", "Your turn", AC_ENDS, AC_JOBS, cg_cards)]))
    qpages = B.build()
    teacher = strip_page(qpages[1]); teacher = teacher[:teacher.index('<h3 class="sh">')] + "</div>"
    out.append(dict(id="quiz", stage=1, title="Iʿrāb Table Quiz", ar="اخْتِبَارُ الطَّاوِلَةِ",
                    blurb="15 noun sentences, one student per card at the table. Full iʿrāb of every word.",
                    intro=strip_page(qpages[0]), teacher=teacher,
                    sets=[irab_set("cards", "Quiz", AC_ENDS, AC_JOBS,
                                   [irab_card(f"Q{i}", dict(en=q["en"], tag=stars(q["lvl"])), ac_rows(q), B.key_card(i, q)) for i, q in enumerate(B.Q, 1)])]))
    out.append(dict(id="exercise", stage=1, title="Iʿrāb Class Exercise", ar="تَمْرِينُ الصَّفِّ",
                    blurb="15 new noun sentences for practice in class, with partner checking.", intro=strip_page(X.build()[0]),
                    sets=[irab_set("cards", "Exercise", AC_ENDS, AC_JOBS,
                                   [irab_card(f"Q{i}", dict(en=q["en"], tag=stars(q["lvl"])), ac_rows(q), X.key_card(i, q)) for i, q in enumerate(X.Q, 1)])]))
    nh = N.build()
    out.append(dict(id="quran-nouns", stage=1, title="Rafʿ and Jarr in the Qur'an", ar="الرَّفْعُ وَالجَرُّ فِي القُرْآنِ",
                    blurb="10 noun-sentence verses. Topic, information, prepositions and owners only.", intro=nh[:nh.index(YOUR_TURN)],
                    sets=[irab_set("cards", "Verses", AC_ENDS, NOM_JOBS,
                                   [irab_card(str(i), dict(en=v["tr"], tag=f'{v["en"]} · {v["ref"]}'), nom_rows(v), N.key(i, v)) for i, v in enumerate(N.VERSES, 1)])]))
    out.append(dict(id="nasb", stage=2, title="Naṣb Colour Guide", ar="النَّصْبُ بِالفَتْحَةِ",
                    blurb="The verb sentence, the fatha sign, and the four naṣb jobs, with 21 colour-boxed examples.",
                    intro=L.lesson(), introLabel="Lesson",
                    sets=[irab_set("cards", "Practice", NASB_ENDS, NASB_JOBS,
                                   [irab_card(f"E{i}", dict(en=p["en"], tag=""), nasb_rows(p["g"], L.stem), L.key_card(i, p), hidden_note(p["g"])) for i, p in enumerate(L.PRACTICE, 1)])]))
    qh = QN.build()
    out.append(dict(id="quran-nasb", stage=2, title="Iʿrāb in the Qur'an", ar="الإِعْرَابُ فِي القُرْآنِ",
                    blurb="10 verses with a past verb and a naṣb noun, mixed with rafʿ and jarr.", intro=qh[:qh.index(YOUR_TURN)],
                    sets=[irab_set("cards", "Verses", NASB_ENDS, NASB_JOBS,
                                   [irab_card(str(i), dict(en=v["tr"], tag=f'{v["en"]} · {v["ref"]}'), nasb_rows(v["g"], QN.qstem), QN.key(i, v), hidden_note(v["g"])) for i, v in enumerate(QN.VERSES, 1)])]))
    return out

