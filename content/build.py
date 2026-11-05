# -*- coding: utf-8 -*-
"""I'rab table quiz v2: full iʿrāb of every word in 15 sentences."""
import html

DAMMA, DAMMATAN, KASRA, KASRATAN = "ُ", "ٌ", "ِ", "ٍ"
MARKS = (DAMMA, DAMMATAN, KASRA, KASRATAN)
VNAME = {DAMMA: "damma", DAMMATAN: "damma + tanween", KASRA: "kasra", KASRATAN: "kasra + tanween"}
CASE = {DAMMA: "rafʿ", DAMMATAN: "rafʿ", KASRA: "jarr", KASRATAN: "jarr"}

ROLES = {
    "topic": ("Topic", "مُبْتَدَأ", "#e0a10b", "#fff5d6", "#a87805"),
    "info": ("Information", "خَبَر", "#e04a3a", "#fde7e4", "#b8322a"),
    "prep": ("After a preposition", "بَعْدَ حَرْفِ الجَرّ", "#22a05a", "#e2f5e9", "#17803f"),
    "owner": ("Ownership", "إِضَافَة", "#7b4fd6", "#efe8fc", "#5f36b8"),
    "adj": ("Adjective", "صِفَة", "#7d858e", "#eef0f2", "#5a626b"),
    "and": ("After وَ (and)", "مَعْطُوف", "#2f7fe0", "#e3eefc", "#1f64bd"),
}
FIXED = ("Fixed / particle", "#9aa0a8", "#f4f4f2", "#5f6672")
CHIP = [("topic", "Topic"), ("info", "Info"), ("prep", "Prep"), ("owner", "Owner"),
        ("adj", "Adj"), ("and", "After وَ"), ("fixed", "Fixed")]

# word: (text, kind, vowel, ref)   kind: head | fixed | particle | prep | owner | adj | and
# ref = the word it depends on (preposition, owned noun, described noun, word before وَ)
P = "particle"
Q = [
 dict(en="The book is new.", lvl=1,
      topic=[("الكِتَابُ","head",DAMMA)], info=[("جَدِيدٌ","head",DAMMATAN)]),
 dict(en="The boy is in the house.", lvl=1,
      topic=[("الوَلَدُ","head",DAMMA)], info=[("فِي",P,None),("البَيْتِ","prep",KASRA,"فِي")]),
 dict(en="The pen is on the desk.", lvl=1,
      topic=[("القَلَمُ","head",DAMMA)], info=[("عَلَى",P,None),("المَكْتَبِ","prep",KASRA,"عَلَى")]),
 dict(en="He is a teacher.", lvl=1,
      topic=[("هُوَ","fixed",None)], info=[("مُدَرِّسٌ","head",DAMMATAN)]),
 dict(en="The teacher's house is big.", lvl=2,
      topic=[("بَيْتُ","head",DAMMA),("المُدَرِّسِ","owner",KASRA,"بَيْتُ")], info=[("كَبِيرٌ","head",DAMMATAN)]),
 dict(en="Zayd's book is new.", lvl=2,
      topic=[("كِتَابُ","head",DAMMA),("زَيْدٍ","owner",KASRATAN,"كِتَابُ")], info=[("جَدِيدٌ","head",DAMMATAN)]),
 dict(en="The pen is in a bag.", lvl=2,
      topic=[("القَلَمُ","head",DAMMA)], info=[("فِي",P,None),("حَقِيبَةٍ","prep",KASRATAN,"فِي")]),
 dict(en="Zayd and Ali are in the mosque.", lvl=2,
      topic=[("زَيْدٌ","head",DAMMATAN),("وَعَلِيٌّ","and",DAMMATAN,"زَيْدٌ")],
      info=[("فِي",P,None),("المَسْجِدِ","prep",KASRA,"فِي")]),
 dict(en="The hardworking student is in the class.", lvl=2,
      topic=[("الطَّالِبُ","head",DAMMA),("المُجْتَهِدُ","adj",DAMMA,"الطَّالِبُ")],
      info=[("فِي",P,None),("الصَّفِّ","prep",KASRA,"فِي")]),
 dict(en="The father and the mother are in the garden.", lvl=2,
      topic=[("الأَبُ","head",DAMMA),("وَالأُمُّ","and",DAMMA,"الأَبُ")],
      info=[("فِي",P,None),("الحَدِيقَةِ","prep",KASRA,"فِي")]),
 dict(en="The door of the house is open.", lvl=3,
      topic=[("بَابُ","head",DAMMA),("البَيْتِ","owner",KASRA,"بَابُ")], info=[("مَفْتُوحٌ","head",DAMMATAN)]),
 dict(en="Muhammad is the Messenger of Allah.", lvl=3,
      topic=[("مُحَمَّدٌ","head",DAMMATAN)], info=[("رَسُولُ","head",DAMMA),("اللَّهِ","owner",KASRA,"رَسُولُ")]),
 dict(en="The bag is in the new car.", lvl=3,
      topic=[("الحَقِيبَةُ","head",DAMMA)],
      info=[("فِي",P,None),("السَّيَّارَةِ","prep",KASRA,"فِي"),("الجَدِيدَةِ","adj",KASRA,"السَّيَّارَةِ")]),
 dict(en="Zayd's and Ali's book is on the desk.", lvl=3,
      topic=[("كِتَابُ","head",DAMMA),("زَيْدٍ","owner",KASRATAN,"كِتَابُ"),("وَعَلِيٍّ","and",KASRATAN,"زَيْدٍ")],
      info=[("عَلَى",P,None),("المَكْتَبِ","prep",KASRA,"عَلَى")]),
 dict(en="The Arabic teacher's pen is beautiful.", lvl=3,
      topic=[("قَلَمُ","head",DAMMA),("مُدَرِّسِ","owner",KASRA,"قَلَمُ"),("العَرَبِيَّةِ","owner",KASRA,"مُدَرِّسِ")],
      info=[("جَمِيلٌ","head",DAMMATAN)]),
]

e = html.escape
def b(s): return f"<bdi>{e(s)}</bdi>"

def words(q):
    out = []
    for g in ("topic", "info"):
        lst = q[g]
        for i, w in enumerate(lst):
            owned = i + 1 < len(lst) and lst[i + 1][1] == "owner"
            out.append(dict(text=w[0], kind=w[1], v=w[2], ref=w[3] if len(w) > 3 else None,
                            group=g, owned=owned))
    return out


_COMB = set("\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652")
_M6 = set("\u064B\u064C\u064D\u064E\u064F\u0650")
def strip_end(t):
    tat = t.endswith("\u0640")
    if tat: t = t[:-1]
    if t.endswith("\u0627") and "\u064B" in t[-4:-1]: t = t[:-1]
    i = len(t)
    while i > 0 and t[i-1] in _COMB: i -= 1
    t = t[:i] + "".join(c for c in t[i:] if c not in _M6)
    return t + ("\u0640" if tat else "")

def stem(w):
    if w["kind"] in ("fixed", P):
        return w["text"]
    return strip_end(w["text"])

def job_of(w):
    return w["group"] if w["kind"] == "head" else ("fixed" if w["kind"] in ("fixed", P) else w["kind"])

def reason(w):
    k, v = w["kind"], w["v"]
    if k == P: return "particle: no iʿrāb change"
    if k == "fixed": return "fixed word: its ending never changes"
    tail = f"{CASE[v]}, {VNAME[v]}"
    if k == "head":
        r = ("topic" if w["group"] == "topic" else "information") + f" → {tail}"
    elif k == "prep": r = f"after {b(w['ref'])} → {tail}"
    elif k == "owner": r = f"owner of {b(w['ref'])} → {tail}"
    elif k == "adj": r = f"describes {b(w['ref'])} → copies: {VNAME[v]}"
    elif k == "and": r = f"after وَ → copies {b(w['ref'])}: {VNAME[v]}"
    if w["owned"]:
        r += " (owned: no tanween)"
    return r

def points(q):
    return len(words(q)) + 1

def stars(n):
    return "".join('<span class="st on">★</span>' if i < n else '<span class="st">★</span>' for i in range(3))

def chip_color(k):
    if k == "fixed": return FIXED[1], FIXED[2], FIXED[3]
    _, _, bo, bg, t = ROLES[k]; return bo, bg, t

# ---------- problem card ----------
def card(i, q):
    ws = words(q)
    sent = " ".join(f'<span class="sw">{e(stem(w))}</span>' for w in ws)
    rows = []
    for n, w in enumerate(ws, 1):
        ends = "".join(f'<span class="ec">ـ{e(m)}</span>' for m in MARKS) + '<span class="ec">—</span>'
        jobs = "".join(
            f'<span class="jc" style="border-color:{chip_color(k)[0]};background:{chip_color(k)[1]};color:{chip_color(k)[2]}">{e(lab)}</span>'
            for k, lab in CHIP)
        rows.append(f'<tr><td class="wn">{n}</td><td class="wd"><bdi>{e(stem(w))}</bdi><span class="wb"></span></td>'
                    f'<td class="ends">{ends}</td><td class="jobs">{jobs}</td></tr>')
    return f'''
<div class="card">
  <div class="chead">
    <span class="qn">Q{i}</span><span class="en">“{e(q["en"])}”</span>
    <span class="lvl">{stars(q["lvl"])}</span>
  </div>
  <div class="sent" dir="rtl">{sent}</div>
  <div class="step"><span class="sn">1</span><b>Big boxes:</b> draw a <span class="hy">yellow</span> box around the Topic and a <span class="hr">red</span> box around the Information.</div>
  <div class="step"><span class="sn">2</span><b>Every word:</b> circle its ending (— = no change) and its job. Say the reason aloud.</div>
  <table class="wt">{"".join(rows)}</table>
  <div class="pts">Big boxes 1 + 1 per word (ending and job) = <b>{points(q)} points</b></div>
</div>'''

# ---------- answer key ----------
def kword(w):
    text, kind, v, g = w["text"], w["kind"], w["v"], w["group"]
    if kind == P:
        return f'<div class="kw plain"><div class="kt">{e(text)}</div><div class="klab muted">particle</div></div>'
    if kind == "fixed":
        bo, t = ROLES["topic"][2], ROLES["topic"][4]
        return (f'<div class="kw plain"><div class="kt">{e(text)}</div>'
                f'<div class="vc" style="border-color:{bo};color:{t}">—</div><div class="klab" style="color:{t}">fixed</div></div>')
    if kind == "head":
        _, _, bo, bg, t = ROLES[g]
        lab = "topic" if g == "topic" else "info"
        return (f'<div class="kw plain"><div class="kt">{e(text)}</div>'
                f'<div class="vc" style="border-color:{bo};color:{t}">ـ{v}</div><div class="klab" style="color:{t}">{lab}</div></div>')
    _, _, bo, bg, t = ROLES[kind]
    return (f'<div class="kw small" style="border-color:{bo}"><div class="kt">{e(text)}</div>'
            f'<div class="vc" style="border-color:{bo};color:{t}">ـ{v}</div><div class="klab" style="color:{t}">{kind}</div></div>')

def kgroup(q, g):
    _, ar, bo, bg, t = ROLES[g]
    en = "Topic" if g == "topic" else "Information"
    ws = [w for w in words(q) if w["group"] == g]
    return (f'<div class="kg" style="border-color:{bo};background:{bg}">'
            f'<div class="kgl" style="color:{t}"><b>{en}</b> {e(ar)}</div>'
            f'<div class="kgw" dir="rtl">{"".join(kword(w) for w in ws)}</div></div>')

def key_card(i, q):
    lines = []
    for w in words(q):
        k = job_of(w)
        bo, bg, t = chip_color(k)
        lab = dict(CHIP)[k] if k != "fixed" else ("Particle" if w["kind"] == P else "Fixed")
        lines.append(f'<div class="rl"><span class="rw"><bdi>{e(w["text"])}</bdi></span>'
                     f'<span class="pill" style="border-color:{bo};background:{bg};color:{t}">{e(lab)}</span>'
                     f'<span class="rt">{reason(w)}</span></div>')
    return f'''
<div class="kcard">
  <div class="khead"><span class="qn">Q{i}</span><span class="en">“{e(q["en"])}”</span><span class="kp">{points(q)} pts</span></div>
  <div class="kbody">
    <div class="kleft">{"".join(lines)}</div>
    <div class="kright" dir="rtl">{kgroup(q, "topic")}{kgroup(q, "info")}</div>
  </div>
</div>'''

def footer(n, N):
    return f'<div class="foot"><span>Arabic · Iʿrāb Table Quiz</span><span>{n} / {N}</span></div>'

def keybox():
    rule = {"topic": "ـُ / ـٌ  رَفْع", "info": "ـُ / ـٌ  رَفْع", "prep": "ـِ / ـٍ  جَرّ",
            "owner": "ـِ / ـٍ  جَرّ", "adj": "copies =", "and": "copies ="}
    out = []
    for k, (en, ar, bo, bg, t) in ROLES.items():
        out.append(f'<div class="kk" style="border-left-color:{bo};background:{bg}">'
                   f'<div class="kkt"><span style="color:{t}"><span class="dot" style="background:{bo}"></span>{e(en)}</span>'
                   f'<span class="kkar">{e(ar)}</span></div><div class="kkr" style="color:{t}">{e(rule[k])}</div></div>')
    return "".join(out)

def build():
    KEY_PER = 4
    nkey = -(-15 // KEY_PER)
    N = 2 + 8 + nkey
    total = sum(points(q) for q in Q)
    pages = [f'''
<div class="page">
  <div class="hero">
    <div class="eyebrow">QUIZ · ONE STUDENT, ONE SENTENCE</div>
    <h1>Iʿrāb at the <span class="gold">table</span>:<br>15 sentences</h1>
    <p>Every ending is missing. Give the full iʿrāb of your sentence: draw the big boxes, then give every word its ending and its job.</p>
    <div class="wm">الإِعْرَاب</div>
  </div>
  <h2><span class="num">1</span>How it works</h2>
  <div class="how">
    <div class="hw"><div class="hn">1</div><b>Come to the table</b><p>Take your card. Read the whole sentence aloud first.</p></div>
    <div class="hw"><div class="hn">2</div><b>Big boxes first</b><p>Where does the Topic end and the Information start?</p></div>
    <div class="hw"><div class="hn">3</div><b>Word by word</b><p>Fixed or particle? If not: preposition, owner, adjective, after وَ?</p></div>
    <div class="hw"><div class="hn">4</div><b>Ending and reason</b><p>Circle the ending and the job, and say why for each word.</p></div>
  </div>
  <h2><span class="num">2</span>Colour key</h2>
  <p class="sub">Same colours as the lesson. The job gives the colour, the colour gives the ending.</p>
  <div class="kkgrid">{keybox()}</div>
  <div class="tipbox"><b>Watch the tanween.</b> A word with ال, or a word that is owned (the first word of “the book <i>of</i> …”), never takes tanween: a single vowel only. Particles like فِي and عَلَى, and fixed words like هُوَ, never change: circle —.</div>
  <div class="three">
    <h3>Iʿrāb in three questions</h3>
    <ol>
      <li><b>What is its job?</b> Topic or information? → both take <span class="wc">ـُ</span></li>
      <li><b>Is there a preposition or an owner relationship?</b> → <span class="wc">ـِ</span></li>
      <li><b>Is it an adjective, or after وَ?</b> → copy the word it follows <span class="wc">=</span></li>
    </ol>
  </div>
  {footer(1, N)}
</div>''']

    rows = "".join(
        f'<tr><td class="c">Q{i}</td><td class="c">{stars(q["lvl"])}</td><td class="c">{len(words(q))}</td><td></td>'
        f'<td class="c"><span class="sq"></span></td><td class="c">&nbsp;/ {points(q)}</td></tr>'
        for i, q in enumerate(Q, 1))
    pages.append(f'''
<div class="page">
  <h2 style="margin-top:0"><span class="num">3</span>Teacher run sheet · 60 minutes</h2>
  <div class="timeline">
    <div class="tl" style="flex:5"><b>0–5</b><span>Warm-up</span></div>
    <div class="tl main" style="flex:45"><b>5–50</b><span>15 students × 3 min at the table</span></div>
    <div class="tl" style="flex:10"><b>50–60</b><span>Review the traps</span></div>
  </div>
  <div class="split">
    <div class="tcol"><b>Each 3-minute turn</b>
      <ol><li><b>1 min</b> draw the big boxes, fill every word alone</li><li><b>1½ min</b> explain word by word: job → rule → ending</li><li><b>½ min</b> class agrees or corrects</li></ol></div>
    <div class="tcol"><b>Handing out cards</b>
      <p>Sentences grow from 2 to 5 words. ★ Q1–4, ★★ Q5–10, ★★★ Q11–15. Print pages 3–10, cut on the dashed line, and match the level to the student.</p></div>
  </div>
  <div class="tipbox"><b>Traps for the review:</b> Q11, Q12 (owned word in the big box: بَابُ, رَسُولُ, no tanween) · Q13 (الجَدِيدَةِ copies السَّيَّارَةِ, not the topic) · Q14 (وَعَلِيٍّ copies زَيْدٍ, not كِتَابُ) · Q15 (مُدَرِّسِ is owner and owned at once).</div>
  <h3 class="sh">Score sheet · {total} points in total</h3>
  <table class="score">
    <tr><th>Card</th><th>Level</th><th>Words</th><th class="name">Student</th><th>Big boxes</th><th>Score</th></tr>
    {rows}
  </table>
  {footer(2, N)}
</div>''')

    pn = 3
    for k in range(0, 15, 2):
        c1 = card(k + 1, Q[k])
        c2 = card(k + 2, Q[k + 1]) if k + 1 < 15 else '''
<div class="card done"><div class="donein"><div class="big">✓</div><b>All 15 sentences done</b>
<p>Bonus for early finishers: take any card and add one word (an adjective, or وَ + a noun). What ending does the new word take, and why?</p></div></div>'''
        pages.append(f'<div class="page cards">{c1}<div class="cut"><span>✂</span></div>{c2}{footer(pn, N)}</div>')
        pn += 1

    for k in range(0, 15, KEY_PER):
        head = ('<h2 style="margin-top:0"><span class="num">4</span>Answer key</h2>'
                '<p class="sub">Full iʿrāb of each sentence. Big boxes first, then the small ones.</p>') if k == 0 else ""
        cards = "".join(key_card(i + 1, Q[i]) for i in range(k, min(k + KEY_PER, 15)))
        pages.append(f'<div class="page">{head}{cards}{footer(pn, N)}</div>')
        pn += 1
    return pages

CSS = open(__file__.replace("build.py", "style.css"), encoding="utf-8").read()

if __name__ == "__main__":
    pages = build()
    doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
    open(__file__.replace("build.py", "quiz.html"), "w", encoding="utf-8").write(doc)
    print("pages:", len(pages))
