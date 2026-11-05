# -*- coding: utf-8 -*-
"""Rafʿ and jarr in the Qur'an: 10 noun-sentence fragments (no verbs, no naṣb)."""
import quran as QN            # patches word_html for fixed pronoun owners
import build as B
from lesson import W, G, R, e, ar, pill, boxes, h2, DAMMA, DAMMATAN, KASRA, KASRATAN, VFULL, CASE
from quran import join, qstem

P = "particle"
def PRON(t, ref): return W(t, "owner", None, ref=ref)

VERSES = [
 dict(ref="الفاتحة · ٢", en="Al-Fatihah 1:2", tr="All praise is for Allah.",
      g=[G("topic", W("الحَمْدُ", v=DAMMA)), G("info", W("لِـ", P), W("لَّهِ", "prep", KASRA, ref="لِـ"))]),
 dict(ref="الإخلاص · ٢", en="Al-Ikhlas 112:2", tr="Allah is the Eternal Refuge.",
      g=[G("topic", W("اللَّهُ", v=DAMMA)), G("info", W("الصَّمَدُ", v=DAMMA))]),
 dict(ref="الفتح · ٢٩", en="Al-Fath 48:29", tr="Muhammad is the Messenger of Allah.",
      g=[G("topic", W("مُحَمَّدٌ", v=DAMMATAN)), G("info", W("رَسُولُ", v=DAMMA), W("اللَّهِ", "owner", KASRA, ref="رَسُولُ"))]),
 dict(ref="إبراهيم · ٥٢", en="Ibrahim 14:52", tr="This is a message for the people.",
      g=[G("topic", W("هَذَا", "fixed", lab="fixed")), G("info", W("بَلَاغٌ", v=DAMMATAN), W("لِـ", P), W("لنَّاسِ", "prep", KASRA, ref="لِـ"))]),
 dict(ref="الشورى · ١٩", en="Ash-Shura 42:19", tr="Allah is Kind to His servants.",
      g=[G("topic", W("اللَّهُ", v=DAMMA)), G("info", W("لَطِيفٌ", v=DAMMATAN), W("بِـ", P), W("عِبَادِ", "prep", KASRA, ref="بِـ"), PRON("ـهِ", "عِبَادِ"))]),
 dict(ref="البقرة · ١٦٣", en="Al-Baqarah 2:163", tr="And your God is one God.",
      g=[G("topic", W("وَ", P), W("إِلَهُـ", v=DAMMA), PRON("ـكُمْ", "إِلَهُ")), G("info", W("إِلَهٌ", v=DAMMATAN), W("وَاحِدٌ", "adj", DAMMATAN, ref="إِلَهٌ"))]),
 dict(ref="آل عمران · ١٨٥", en="Al Imran 3:185", tr="Every soul will taste death.",
      g=[G("topic", W("كُلُّ", v=DAMMA), W("نَفْسٍ", "owner", KASRATAN, ref="كُلُّ")), G("info", W("ذَائِقَةُ", v=DAMMA), W("المَوْتِ", "owner", KASRA, ref="ذَائِقَةُ"))]),
 dict(ref="القدر · ٣", en="Al-Qadr 97:3", tr="The Night of Decree is better than a thousand months.",
      g=[G("topic", W("لَيْلَةُ", v=DAMMA), W("القَدْرِ", "owner", KASRA, ref="لَيْلَةُ")),
         G("info", W("خَيْرٌ", v=DAMMATAN), W("مِنْ", P), W("أَلْفِ", "prep", KASRA, ref="مِنْ"), W("شَهْرٍ", "owner", KASRATAN, ref="أَلْفِ"))]),
 dict(ref="البقرة · ٢٨٤", en="Al-Baqarah 2:284", tr="And Allah has power over all things.",
      g=[G("topic", W("وَ", P), W("اللَّهُ", v=DAMMA)),
         G("info", W("عَلَى", P), W("كُلِّ", "prep", KASRA, ref="عَلَى"), W("شَيْءٍ", "owner", KASRATAN, ref="كُلِّ"), W("قَدِيرٌ", v=DAMMATAN))]),
 dict(ref="النور · ٣٥", en="An-Nur 24:35", tr="Allah is the Light of the heavens and the earth.",
      g=[G("topic", W("اللَّهُ", v=DAMMA)),
         G("info", W("نُورُ", v=DAMMA), W("السَّمَاوَاتِ", "owner", KASRA, ref="نُورُ"), W("وَالأَرْضِ", "and", KASRA, ref="السَّمَاوَاتِ"))]),
]

CH = [("topic", "Topic"), ("info", "Info"), ("prep", "Prep"), ("owner", "Owner"), ("adj", "Adj"), ("and", "After وَ")]
ENDS = [DAMMA, DAMMATAN, KASRA, KASRATAN]
GREY = 'border-color:#9aa0a8;background:#f4f4f2;color:#5f6672'

def pieces(v):
    out = []
    for g in v["g"]:
        for i, w in enumerate(g["ws"]):
            owned = i + 1 < len(g["ws"]) and g["ws"][i + 1]["k"] == "owner"
            out.append(dict(w, role=g["role"], owned=owned))
    return out

def card(i, v):
    ws = pieces(v)
    sent = " ".join(f'<span class="sw">{e(t)}</span>' for t in join([qstem(w) for w in ws]))
    rows = []
    for n, w in enumerate(ws, 1):
        ends = "".join(f'<span class="ec">ـ{m}</span>' for m in ENDS) + '<span class="ec">—</span>'
        chips = "".join(f'<span class="jc" style="border-color:{R[k][2]};background:{R[k][3]};color:{R[k][4]}">{e(l)}</span>' for k, l in CH)
        chips += f'<span class="jc" style="{GREY}">Fixed / particle</span>'
        rows.append(f'<tr><td class="wn">{n}</td><td class="wd"><bdi>{e(qstem(w))}</bdi></td>'
                    f'<td><div class="ends">{ends}</div><div class="jobs2">{chips}</div></td></tr>')
    return f'''
<div class="card pc qc">
  <div class="chead"><span class="qn">{i}</span><span class="en">“{e(v["tr"])}”</span><span class="lvl qref">{e(v["en"])} · <bdi>{e(v["ref"])}</bdi></span></div>
  <div class="sent" dir="rtl">{sent}</div>
  <div class="step"><span class="sn">1</span><b>Big boxes:</b> draw a <span class="hy">yellow</span> box around the Topic and a <span class="hr">red</span> box around the Information.</div>
  <div class="step"><span class="sn">2</span><b>Every piece:</b> circle its ending (— = fixed) and its job.</div>
  <table class="wt wt2">{"".join(rows)}</table>
</div>'''

def reason(w):
    k, v = w["k"], w["v"]
    if k == P: return "particle: never changes"
    if k == "fixed": return "fixed word: its ending never changes"
    if k == "owner" and v is None: return ar(f"owner of {{{w['ref']}}}: attached pronoun, fixed")
    tail = f"{CASE[v]}, {VFULL[v]}"
    if k == "head": r = ("topic" if w["role"] == "topic" else "information") + f" → {tail}"
    elif k == "prep": r = f"after {{{w['ref']}}} → {tail}"
    elif k == "owner": r = f"owner of {{{w['ref']}}} → {tail}"
    elif k == "adj": r = f"describes {{{w['ref']}}} → copies: {VFULL[v]}"
    elif k == "and": r = f"after وَ → copies {{{w['ref']}}}: {VFULL[v]}"
    if w["owned"]: r += " (owned: no tanween)"
    return ar(r)

def key(i, v):
    lines = []
    for w in pieces(v):
        if w["k"] in (P, "fixed"):
            pl = f'<span class="pill" style="{GREY}">{"Particle" if w["k"] == P else "Fixed"}</span>'
        else:
            pl = pill(w["k"] if w["k"] in ("prep", "owner", "adj", "and") else w["role"])
        lines.append(f'<div class="rl"><span class="rw"><bdi>{e(w["t"])}</bdi></span>{pl}<span class="rt">{reason(w)}</span></div>')
    return (f'<div class="kcard"><div class="khead"><span class="qn">{i}</span><span class="en">“{e(v["tr"])}”</span>'
            f'<span class="kp">{e(v["en"])}</span></div>'
            f'<div class="kbody"><div class="kleft">{"".join(lines)}</div><div class="kright">{boxes(v["g"])}</div></div></div>')

def overview():
    rows = []
    for i, v in enumerate(VERSES, 1):
        seen = []
        for g in v["g"]:
            for k in [g["role"]] + [w["k"] for w in g["ws"]]:
                if k in R and k not in seen: seen.append(k)
        full = " ".join(join([w["t"] for g in v["g"] for w in g["ws"]]))
        rows.append(f'<tr><td class="c"><b>{i}</b></td><td class="vx" dir="rtl">{e(full)}</td>'
                    f'<td class="vr">{e(v["en"])}</td><td>{"".join(pill(k) + " " for k in seen)}</td></tr>')
    return f'<table class="glance vt"><tr><th></th><th>Verse (fragment)</th><th>Reference</th><th>Jobs inside</th></tr>{"".join(rows)}</table>'

def build():
    head = f'''
<div class="hero">
  <div class="eyebrow">PRACTICE · QUR'AN · RAFʿ AND JARR</div>
  <h1>Noun sentences in the <span class="gold">Qur'an</span>:<br>10 verses</h1>
  <p>Only Topic and Information, with the rafʿ and jarr rules we know. No verbs and no naṣb yet.</p>
  <div class="wm">القُرْآن</div>
</div>
{h2(1, "Three small notes for these verses")}
<div class="rule3">
  <div class="rr" style="border-color:{R["owner"][2]}"><b style="color:{R["owner"][4]}">Attached pronouns are fixed</b>
    <p>ـهِ “his”, ـكُمْ “your” join the noun before them. They are the owner, and fixed. We split them off: <bdi class="ab">عِبَادِ | ـهِ</bdi>.</p></div>
  <div class="rr" style="border-color:{R["prep"][2]}"><b style="color:{R["prep"][4]}">Some prepositions are joined</b>
    <p><bdi class="ab">لِـ</bdi> “for” and <bdi class="ab">بِـ</bdi> “to, with” join the next word: <bdi class="ab">لِلَّهِ</bdi> = <bdi class="ab">لِـ</bdi> + <bdi class="ab">اللَّهِ</bdi>. The noun after them still takes kasra.</p></div>
  <div class="rr" style="border-color:{R["topic"][2]}"><b style="color:{R["topic"][4]}">هَذَا is fixed</b>
    <p><bdi class="ab">هَذَا</bdi> “this” works like <bdi class="ab">هُوَ</bdi> and <bdi class="ab">أَنَا</bdi>: it can be the Topic, but its ending never changes.</p></div>
</div>
<div class="tipbox"><b>Also:</b> the Information can start with a preposition: <bdi class="ab">لِلَّهِ</bdi> (verse 1), <bdi class="ab">عَلَى كُلِّ شَيْءٍ قَدِيرٌ</bdi> (verse 9). Box the whole part in red, then give each word inside its own rule.</div>
{h2(2, "Colour key")}
<div class="kkgrid">{B.keybox()}</div>
<div class="three">
  <h3>Iʿrāb in three questions</h3>
  <ol>
    <li><b>What is its job?</b> Topic or information? → both take <span class="wc">ـُ</span></li>
    <li><b>Is there a preposition or an owner relationship?</b> → <span class="wc">ـِ</span></li>
    <li><b>Is it an adjective, or after وَ?</b> → copy the word it follows <span class="wc">=</span></li>
  </ol>
</div>
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
           + open("quran.css", encoding="utf-8").read()
           + '@page { @bottom-left { content: "Arabic · Rafʿ and Jarr in the Qur\'an"; } }')
    doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body class="flow">{build()}</body></html>'
    open("quran_nominal.html", "w", encoding="utf-8").write(doc)
    print("ok")
