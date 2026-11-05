# -*- coding: utf-8 -*-
"""Naṣb in the Qur'an: 10 verse fragments, combined rafʿ / naṣb / jarr practice."""
import lesson as L
from lesson import (W, G, R, e, ar, pill, boxes, flat, stem, MARKS6, CHIPS, CHIPLAB, h2,
                    DAMMA, DAMMATAN, FATHA, FATHATAN, KASRA, KASRATAN, VFULL, CASE)

P = "particle"
_wh = L.word_html
def _word_html(w, role):
    if w["k"] == "owner" and w["v"] is None:
        b, t = R["owner"][2], R["owner"][4]
        return (f'<div class="kw small" style="border-color:{b}"><div class="kt">{e(w["t"])}</div>'
                f'<div class="vc" style="border-color:{b};color:{t}">—</div><div class="klab" style="color:{t}">fixed · owner</div></div>')
    return _wh(w, role)
L.word_html = _word_html
def V(t, pre=None):
    ws = ([W(pre, P)] if pre else []) + [W(t, "fixed", lab="fixed · past")]
    return G("verb", *ws)
def HID(t): return G("doer", W(t, "hidden"))
def PRON(t, ref): return W(t, "owner", None, ref=ref)   # attached pronoun: fixed owner

# Uthmani spelling simplified to standard vowelled script; fragments, not full verses.
VERSES = [
 dict(ref="طه · ١٢١", en="Ta-Ha 20:121", tr="And Adam disobeyed his Lord.",
      g=[V("عَصَى", "وَ"), G("doer", W("آدَمُ", v=DAMMA)), G("obj", W("رَبَّـ", v=FATHA), PRON("ـهُ", "رَبَّ"))]),
 dict(ref="هود · ٤٢", en="Hud 11:42", tr="And Nuh called out to his son.",
      g=[V("نَادَى", "وَ"), G("doer", W("نُوحٌ", v=DAMMATAN)), G("obj", W("ابْنَـ", v=FATHA), PRON("ـهُ", "ابْنَ"))]),
 dict(ref="النمل · ١٦", en="An-Naml 27:16", tr="And Sulayman inherited from Dawud.",
      g=[V("وَرِثَ", "وَ"), G("doer", W("سُلَيْمَانُ", v=DAMMA)), G("obj", W("دَاوُودَ", v=FATHA))]),
 dict(ref="يوسف · ٢٣", en="Yusuf 12:23", tr="And she closed the doors.",
      g=[V("غَلَّقَتِ", "وَ"), HID("(هِيَ)"), G("obj", W("الأَبْوَابَ", v=FATHA))]),
 dict(ref="يوسف · ٢٥", en="Yusuf 12:25", tr="And she tore his shirt from the back.",
      g=[V("قَدَّتْ", "وَ"), HID("(هِيَ)"), G("obj", W("قَمِيصَـ", v=FATHA), PRON("ـهُ", "قَمِيصَ")),
         G("prep", W("مِنْ", P), W("دُبُرٍ", v=KASRATAN, ref="مِنْ"))]),
 dict(ref="البقرة · ٢٢", en="Al-Baqarah 2:22", tr="And He sent down water from the sky.",
      g=[V("أَنْزَلَ", "وَ"), HID("(هُوَ)"), G("prep", W("مِنَ", P), W("السَّمَاءِ", v=KASRA, ref="مِنَ")),
         G("obj", W("مَاءً", v=FATHATAN))]),
 dict(ref="الإسراء · ١", en="Al-Isra 17:1", tr="(Who) took His servant by night.",
      g=[V("أَسْرَى"), HID("(هُوَ)"), G("prep", W("بِـ", P), W("عَبْدِ", v=KASRA, ref="بِـ"), PRON("ـهِ", "عَبْدِ")),
         G("when", W("لَيْلًا", v=FATHATAN))]),
 dict(ref="الفجر · ٢٢", en="Al-Fajr 89:22", tr="And your Lord came, and the angels, row after row.",
      g=[V("جَاءَ", "وَ"), G("doer", W("رَبُّـ", v=DAMMA), PRON("ـكَ", "رَبُّ"), W("وَالمَلَكُ", "and", DAMMA, ref="رَبُّ")),
         G("state", W("صَفًّا", v=FATHATAN), W("صَفًّا", v=FATHATAN))]),
 dict(ref="القصص · ١٥", en="Al-Qasas 28:15", tr="And he entered the city at a time when its people were unaware.",
      g=[V("دَخَلَ", "وَ"), HID("(هُوَ)"), G("obj", W("المَدِينَةَ", v=FATHA)),
         G("prep", W("عَلَى", P), W("حِينِ", v=KASRA, ref="عَلَى"), W("غَفْلَةٍ", "owner", KASRATAN, ref="حِينِ"),
           W("مِنْ", P), W("أَهْلِ", "prep", KASRA, ref="مِنْ"), PRON("ـهَا", "أَهْلِ"))]),
 dict(ref="النمل · ١٩", en="An-Naml 27:19", tr="So he smiled, laughing at her words.",
      g=[V("تَبَسَّمَ", "فَ"), HID("(هُوَ)"), G("state", W("ضَاحِكًا", v=FATHATAN)),
         G("prep", W("مِنْ", P), W("قَوْلِ", v=KASRA, ref="مِنْ"), PRON("ـهَا", "قَوْلِ"))]),
]

COMB = set("\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652")
def strip_end(t):
    tat = t.endswith("ـ")
    if tat: t = t[:-1]
    if t.endswith("ا") and FATHATAN in t[-4:-1]: t = t[:-1]
    i = len(t)
    while i > 0 and t[i-1] in COMB: i -= 1
    t = t[:i] + "".join(c for c in t[i:] if c not in MARKS6)
    return t + ("ـ" if tat else "")

def qstem(w):
    if w["k"] in ("fixed", P) or w["v"] is None: return w["t"]
    return strip_end(w["t"])

def join(pieces):
    out = []
    for t in pieces:
        if out and (out[-1].endswith("ـ") or t.startswith("ـ") or out[-1] in ("وَ", "فَ")):
            out[-1] = out[-1].rstrip("ـ") + t.lstrip("ـ")
        else:
            out.append(t)
    return out

def jobs_of(v):
    seen = []
    for g in v["g"]:
        for k in [g["role"]] + [w["k"] for w in g["ws"]]:
            if k in R and k not in seen: seen.append(k)
    return seen

def card(i, v):
    ws = flat(v["g"])
    sent = " ".join(f'<span class="sw">{e(t)}</span>' for t in join([qstem(w) for w in ws]))
    rows = []
    for n, w in enumerate(ws, 1):
        ends = "".join(f'<span class="ec">ـ{m}</span>' for m in MARKS6) + '<span class="ec">—</span>'
        chips = "".join(f'<span class="jc" style="border-color:{R[k][2]};background:{R[k][3]};color:{R[k][4]}">{e(CHIPLAB[k])}</span>'
                        for k in CHIPS) + '<span class="jc" style="border-color:#9aa0a8;background:#f4f4f2;color:#5f6672">Particle</span>'
        rows.append(f'<tr><td class="wn">{n}</td><td class="wd"><bdi>{e(qstem(w))}</bdi></td>'
                    f'<td><div class="ends">{ends}</div><div class="jobs2">{chips}</div></td></tr>')
    hid = any(w["k"] == "hidden" for g in v["g"] for w in g["ws"])
    note = " The doer is hidden: write it." if hid else ""
    return f'''
<div class="card pc qc">
  <div class="chead"><span class="qn">{i}</span><span class="en">“{e(v["tr"])}”</span><span class="lvl qref">{e(v["en"])} · <bdi>{e(v["ref"])}</bdi></span></div>
  <div class="sent" dir="rtl">{sent}</div>
  <div class="step"><span class="sn">1</span><b>Big boxes:</b> verb and doer first, then box every other job.{note}</div>
  <div class="step"><span class="sn">2</span><b>Every piece:</b> circle its ending (— = fixed) and its job.</div>
  <table class="wt wt2">{"".join(rows)}</table>
</div>'''

def reason(w):
    k, v, role = w["k"], w["v"], w["role"]
    if k == P: return "particle: never changes"
    if k == "fixed": return "past verb: fixed"
    if k == "owner" and v is None: return ar(f"owner of {{{w['ref']}}}: attached pronoun, fixed")
    tail = f"{CASE[v]}, {VFULL[v]}"
    if k == "head":
        q = {"doer": "doer", "obj": "object (what? whom?)", "when": "time (when?)",
             "state": "state (how?)", "prep": f"after {{{w['ref']}}}"}[role]
        r = f"{q} → {tail}"
    elif k == "prep": r = f"after {{{w['ref']}}} → {tail}"
    elif k == "owner": r = f"owner of {{{w['ref']}}} → {tail}"
    elif k == "and": r = f"after وَ → copies {{{w['ref']}}}: {VFULL[v]}"
    if w["owned"]: r += " (owned: no tanween)"
    return ar(r)

def key(i, v):
    lines = []
    for g in v["g"]:
        for idx, w0 in enumerate(g["ws"]):
            if w0["k"] == "hidden":
                lines.append(f'<div class="rl"><span class="rw"><bdi>{e(w0["t"])}</bdi></span>{pill("doer")}<span class="rt">hidden doer</span></div>')
                continue
            owned = idx + 1 < len(g["ws"]) and g["ws"][idx + 1]["k"] == "owner"
            w = dict(w0, role=g["role"], owned=owned)
            role = w["k"] if w["k"] in ("prep", "owner", "adj", "and") else w["role"]
            pl = pill(role) if w["k"] != P else '<span class="pill" style="border-color:#9aa0a8;background:#f4f4f2;color:#5f6672">Particle</span>'
            lines.append(f'<div class="rl"><span class="rw"><bdi>{e(w["t"])}</bdi></span>{pl}<span class="rt">{reason(w)}</span></div>')
    return (f'<div class="kcard"><div class="khead"><span class="qn">{i}</span><span class="en">“{e(v["tr"])}”</span>'
            f'<span class="kp">{e(v["en"])}</span></div>'
            f'<div class="kbody"><div class="kleft">{"".join(lines)}</div><div class="kright">{boxes(v["g"])}</div></div></div>')

def overview():
    rows = []
    for i, v in enumerate(VERSES, 1):
        chips = "".join(pill(k) + " " for k in jobs_of(v))
        full = " ".join(join([w["t"] for g in v["g"] for w in g["ws"] if w["k"] != "hidden"]))
        rows.append(f'<tr><td class="c"><b>{i}</b></td><td class="vx" dir="rtl">{e(full)}</td>'
                    f'<td class="vr">{e(v["en"])}</td><td>{chips}</td></tr>')
    return f'<table class="glance vt"><tr><th></th><th>Verse (fragment)</th><th>Reference</th><th>Jobs inside</th></tr>{"".join(rows)}</table>'

def build():
    head = f'''
<div class="hero">
  <div class="eyebrow">COMBINED PRACTICE · QUR'AN</div>
  <h1>Iʿrāb in the <span class="gold">Qur'an</span>:<br>10 verses</h1>
  <p>Real verses with a past verb, a naṣb noun, and the rafʿ and jarr rules we already know. Same colours, same method.</p>
  <div class="wm">القُرْآن</div>
</div>
{h2(1, "Three small notes for these verses")}
<div class="rule3">
  <div class="rr" style="border-color:{R["owner"][2]}"><b style="color:{R["owner"][4]}">Attached pronouns are fixed</b>
    <p>ـهُ “his”, ـهَا “her”, ـكَ “your” join the noun before them. They are the owner, and fixed. We split them off so you can see the noun's ending: <bdi class="ab">رَبَّـ | ـهُ</bdi>.</p></div>
  <div class="rr" style="border-color:{R["doer"][2]}"><b style="color:{R["doer"][4]}">A past verb can hide its doer</b>
    <p>Like an order hides “you”, a past verb can hide “he” <bdi class="ab">(هُوَ)</bdi> or “she” <bdi class="ab">(هِيَ)</bdi>. The ـتْ in <bdi class="ab">قَدَّتْ</bdi> tells us the doer is “she”.</p></div>
  <div class="rr" style="border-color:{R["verb"][2]}"><b style="color:{R["verb"][4]}">Some names never take tanween</b>
    <p><bdi class="ab">آدَمُ</bdi>, <bdi class="ab">سُلَيْمَانُ</bdi>, <bdi class="ab">دَاوُودَ</bdi>: one damma or one fatha only. (Names like <bdi class="ab">نُوحٌ</bdi> do take it.)</p></div>
</div>
<div class="tipbox"><b>Also:</b> a past verb ending in ـتْ takes a small kasra before ال, just like an order verb: <bdi class="ab">غَلَّقَتِ الأَبْوَابَ</bdi>. It is still fixed.</div>
{h2(2, "Colour key")}
{L.colour_key()}
{h2(3, "The 10 verses", "pb")}
<p class="sub">Read each verse aloud with your teacher first. Then solve the cards: every ending is missing.</p>
{overview()}
'''
    cards = "".join(card(i + 1, v) for i, v in enumerate(VERSES))
    keyh = f'<div class="pb">{h2(5, "Answer key", "nomt")}<p class="sub">Full iʿrāb of every piece. Big boxes first, then the small ones.</p></div>'
    keys = "".join(key(i + 1, v) for i, v in enumerate(VERSES))
    return head + f'<div class="pb">{h2(4, "Your turn", "nomt")}</div>' + cards + keyh + keys

if __name__ == "__main__":
    css = (open("style.css", encoding="utf-8").read() + open("lesson.css", encoding="utf-8").read()
           + open("quran.css", encoding="utf-8").read())
    doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body class="flow">{build()}</body></html>'
    open("quran.html", "w", encoding="utf-8").write(doc)
    print("ok")
