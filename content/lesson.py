# -*- coding: utf-8 -*-
"""Naṣb lesson: colour-guide chapter (past + order verbs only, naṣb by fatha only)."""
import html, re

DAMMA, DAMMATAN, FATHA, FATHATAN, KASRA, KASRATAN = "ُ", "ٌ", "َ", "ً", "ِ", "ٍ"
VN = {DAMMA: "damma", DAMMATAN: "damma", FATHA: "fatha", FATHATAN: "fatha", KASRA: "kasra", KASRATAN: "kasra"}
VFULL = {DAMMA: "damma", DAMMATAN: "damma + tanween", FATHA: "fatha", FATHATAN: "fatha + tanween",
         KASRA: "kasra", KASRATAN: "kasra + tanween"}
CASE = {DAMMA: "rafʿ", DAMMATAN: "rafʿ", FATHA: "naṣb", FATHATAN: "naṣb", KASRA: "jarr", KASRATAN: "jarr"}

# role: (English, Arabic, border, background, text, short)
R = {
 "verb":  ("Verb", "فِعْل", "#3a5a85", "#e8eef6", "#2b4668", "verb"),
 "doer":  ("Doer", "فَاعِل", "#ea7a10", "#fff0df", "#b05705", "doer"),
 "obj":   ("Object", "مَفْعُولٌ بِهِ", "#d63384", "#fde6f1", "#a61e62", "object"),
 "purp":  ("Purpose", "مَفْعُولٌ لِأَجْلِهِ", "#0f9d9a", "#dcf4f3", "#0a7471", "purpose"),
 "when":  ("Time / place", "مَفْعُولٌ فِيهِ", "#a0612b", "#f5e9dd", "#7b471c", "time/place"),
 "state": ("State", "حَال", "#6b8e23", "#edf4dc", "#4c6810", "state"),
 "topic": ("Topic", "مُبْتَدَأ", "#e0a10b", "#fff5d6", "#a87805", "topic"),
 "info":  ("Information", "خَبَر", "#e04a3a", "#fde7e4", "#b8322a", "info"),
 "prep":  ("After a preposition", "بَعْدَ حَرْفِ الجَرّ", "#22a05a", "#e2f5e9", "#17803f", "prep"),
 "owner": ("Ownership", "إِضَافَة", "#7b4fd6", "#efe8fc", "#5f36b8", "owner"),
 "adj":   ("Adjective", "صِفَة", "#7d858e", "#eef0f2", "#5a626b", "adj"),
 "and":   ("After وَ (and)", "مَعْطُوف", "#2f7fe0", "#e3eefc", "#1f64bd", "and"),
}
NASB = ["obj", "purp", "when", "state"]

e = html.escape
def ar(s):  # inline Arabic markup {...} -> isolated Arabic
    return re.sub(r"\{(.+?)\}", lambda m: f'<bdi class="ab">{e(m.group(1))}</bdi>', s)

def W(t, k="head", v=None, lab=None, ref=None):
    return dict(t=t, k=k, v=v, lab=lab, ref=ref)
def G(role, *ws): return dict(role=role, ws=list(ws))
def V(t, order=False): return G("verb", W(t, "fixed", lab="fixed · order" if order else "fixed · past"))
HID = G("doer", W("(أَنْتَ)", "hidden"))

# ---------------- sentence boxes ----------------
def word_html(w, role):
    k = w["k"]
    if k == "particle":
        return f'<div class="kw plain"><div class="kt">{e(w["t"])}</div><div class="klab muted">particle</div></div>'
    if k == "hidden":
        _, _, b, bg, t, _ = R["doer"]
        return (f'<div class="kw ghost" style="border-color:{b}"><div class="kt" style="color:{t}">{e(w["t"])}</div>'
                f'<div class="klab" style="color:{t};margin-top:3px">hidden doer</div></div>')
    if k == "fixed":
        _, _, b, bg, t, _ = R[role]
        return (f'<div class="kw plain"><div class="kt">{e(w["t"])}</div>'
                f'<div class="vc" style="border-color:{b};color:{t}">—</div><div class="klab" style="color:{t}">{e(w["lab"] or "fixed")}</div></div>')
    if k == "head":
        _, _, b, bg, t, sh = R[role]
        return (f'<div class="kw plain"><div class="kt">{e(w["t"])}</div>'
                f'<div class="vc" style="border-color:{b};color:{t}">ـ{w["v"]}</div><div class="klab" style="color:{t}">{VN[w["v"]]} · {sh}</div></div>')
    _, _, b, bg, t, sh = R[k]
    return (f'<div class="kw small" style="border-color:{b}"><div class="kt">{e(w["t"])}</div>'
            f'<div class="vc" style="border-color:{b};color:{t}">ـ{w["v"]}</div><div class="klab" style="color:{t}">{VN[w["v"]]} · {sh}</div></div>')

def group_html(g):
    en, arr, b, bg, t, _ = R[g["role"]]
    return (f'<div class="kg" style="border-color:{b};background:{bg}"><div class="kgl" style="color:{t}"><b>{e(en)}</b> {e(arr)}</div>'
            f'<div class="kgw" dir="rtl">{"".join(word_html(w, g["role"]) for w in g["ws"])}</div></div>')

def boxes(groups):
    return f'<div class="sbox" dir="rtl">{"".join(group_html(g) for g in groups)}</div>'

def pill(role):
    en, _, b, bg, t, _ = R[role]
    return f'<span class="pill" style="border-color:{b};background:{bg};color:{t}">{e(en)}</span>'

def example(num, en, groups, lines, tip=None):
    ls = "".join(f'<div class="xl">{pill(r)}<span>{ar(txt)}</span></div>' for r, txt in lines)
    tp = f'<div class="tipbox in"><b>Tip:</b> {ar(tip)}</div>' if tip else ""
    return (f'<div class="ex"><div class="exh"><span class="qn">{num}</span><i>“{e(en)}”</i></div>'
            f'{boxes(groups)}<div class="xls">{ls}</div>{tp}</div>')

# ---------------- practice cards ----------------
MARKS6 = [DAMMA, DAMMATAN, FATHA, FATHATAN, KASRA, KASRATAN]
CHIPS = ["verb", "doer", "obj", "purp", "when", "state", "prep", "owner", "adj", "and"]
CHIPLAB = {"verb": "Verb", "doer": "Doer", "obj": "Object", "purp": "Purpose", "when": "Time/place",
           "state": "State", "prep": "Prep", "owner": "Owner", "adj": "Adj", "and": "After وَ"}

def flat(groups):
    out = []
    for g in groups:
        for i, w in enumerate(g["ws"]):
            if w["k"] == "hidden":
                continue
            owned = i + 1 < len(g["ws"]) and g["ws"][i + 1]["k"] == "owner"
            out.append(dict(w, role=g["role"], owned=owned))
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
    if w["k"] in ("fixed", "particle"): return w["t"]
    return strip_end(w["t"])

def practice_card(i, p):
    ws = flat(p["g"])
    sent = " ".join(f'<span class="sw">{e(stem(w))}</span>' for w in ws)
    hid = any(w["k"] == "hidden" for g in p["g"] for w in g["ws"])
    rows = []
    for n, w in enumerate(ws, 1):
        ends = "".join(f'<span class="ec">ـ{m}</span>' for m in MARKS6) + '<span class="ec">—</span>'
        chips = "".join(
            f'<span class="jc" style="border-color:{R[k][2]};background:{R[k][3]};color:{R[k][4]}">{e(CHIPLAB[k])}</span>'
            for k in CHIPS) + '<span class="jc" style="border-color:#9aa0a8;background:#f4f4f2;color:#5f6672">Particle</span>'
        rows.append(f'<tr><td class="wn">{n}</td><td class="wd"><bdi>{e(stem(w))}</bdi><span class="wb"></span></td>'
                    f'<td><div class="ends">{ends}</div><div class="jobs2">{chips}</div></td></tr>')
    hidnote = ' This is an order: write its hidden doer.' if hid else ''
    return f'''
<div class="card pc">
  <div class="chead"><span class="qn">E{i}</span><span class="en">“{e(p["en"])}”</span></div>
  <div class="sent" dir="rtl">{sent}</div>
  <div class="step"><span class="sn">1</span><b>Big boxes:</b> find the verb and the doer first, then box every other job.{hidnote}</div>
  <div class="step"><span class="sn">2</span><b>Every word:</b> circle its ending (— = fixed) and its job. Write the reason in your notebook.</div>
  <table class="wt wt2">{"".join(rows)}</table>
</div>'''

def reason(w):
    k, v, role = w["k"], w["v"], w["role"]
    if k == "particle": return "particle: never changes"
    if k == "fixed":
        return "order verb: fixed" if "order" in (w["lab"] or "") else "past verb: fixed"
    tail = f"{CASE[v]}, {VFULL[v]}"
    if k == "head":
        q = {"doer": "doer", "obj": "object (what?)", "purp": "purpose (why?)",
             "when": "time/place (when? where?)", "state": "state (how?)"}[role]
        r = f"{q} → {tail}"
    elif k == "prep": r = f"after {{{w['ref']}}} → {tail}"
    elif k == "owner": r = f"owner of {{{w['ref']}}} → {tail}"
    elif k == "adj": r = f"describes {{{w['ref']}}} → copies: {VFULL[v]}"
    elif k == "and": r = f"after وَ → copies {{{w['ref']}}}: {VFULL[v]}"
    if w["owned"]: r += " (owned: no tanween)"
    return ar(r)

def key_card(i, p):
    lines = []
    for w in flat(p["g"]):
        role = w["k"] if w["k"] in ("prep", "owner", "adj", "and") else w["role"]
        pl = pill(role) if w["k"] != "particle" else '<span class="pill" style="border-color:#9aa0a8;background:#f4f4f2;color:#5f6672">Particle</span>'
        lines.append(f'<div class="rl"><span class="rw"><bdi>{e(w["t"])}</bdi></span>{pl}<span class="rt">{reason(w)}</span></div>')
    if any(w["k"] == "hidden" for g in p["g"] for w in g["ws"]):
        lines.append(f'<div class="rl"><span class="rw"><bdi>(أَنْتَ)</bdi></span>{pill("doer")}<span class="rt">hidden doer of the order: “you”</span></div>')
    return (f'<div class="kcard"><div class="khead"><span class="qn">E{i}</span><span class="en">“{e(p["en"])}”</span></div>'
            f'<div class="kbody"><div class="kleft">{"".join(lines)}</div><div class="kright">{boxes(p["g"])}</div></div></div>')

# ---------------- content ----------------
def h2(n, t, cls=""):
    return f'<h2 class="{cls}"><span class="num">{n}</span>{t}</h2>'

def cases():
    items = [("A", DAMMA, "رَفْع", "rafʿ · damma", "Learned ✓", "done"),
             ("B", FATHA, "نَصْب", "naṣb · fatha", "Today", "now"),
             ("C", KASRA, "جَرّ", "jarr · kasra", "Learned ✓", "done"),
             ("D", "ْ", "جَزْم", "jazm · sukūn", "Later (verbs)", "later")]
    out = []
    for l, m, a, en, st, c in items:
        out.append(f'<div class="case {c}"><span class="cl">{l}</span><div class="cm">ـ{m}</div><div class="ca">{a}</div>'
                   f'<div class="ce">{en}</div><div class="cs">{st}</div></div>')
    return f'<div class="cases">{"".join(out)}</div>'

def colour_key():
    new = [("verb", "fixed —", "The action. Past and order verbs never change."),
           ("doer", "ـُ / ـٌ  رَفْع", "Who did the action."),
           ("obj", "ـَ / ـً  نَصْب", "What? Whom? The thing the action falls on."),
           ("purp", "ـَ / ـً  نَصْب", "Why? The reason for the action."),
           ("when", "ـَ / ـً  نَصْب", "When? Where? With no preposition."),
           ("state", "ـَ / ـً  نَصْب", "How? The state of the doer or object.")]
    cards = "".join(
        f'<div class="kk" style="border-left-color:{R[k][2]};background:{R[k][3]}"><div class="kkt"><span style="color:{R[k][4]}">'
        f'<span class="dot" style="background:{R[k][2]}"></span>{e(R[k][0])}</span><span class="kkar">{e(R[k][1])}</span></div>'
        f'<div class="kkr" style="color:{R[k][4]}">{e(rule)}</div><div class="kkd">{e(d)}</div></div>' for k, rule, d in new)
    old = "".join(f'<span class="oldc" style="border-color:{R[k][2]};background:{R[k][3]};color:{R[k][4]}">{e(R[k][0])}</span>'
                  for k in ("prep", "owner", "adj", "and"))
    return f'<div class="kkgrid">{cards}</div><div class="oldrow"><b>Small boxes from last lesson still work:</b> {old}</div>'

def sign_rules():
    return '''
<div class="signs">
  <div class="sg"><div class="sgt">With ال, or owned</div><div class="sga"><bdi>الدَّرْسَ</bdi> · <bdi>كِتَابَ المُدَرِّسِ</bdi></div><div class="sgd">One fatha only: <b>ـَ</b></div></div>
  <div class="sg"><div class="sgt">No ال</div><div class="sga"><bdi>كِتَابًا</bdi> · <bdi>صَبَاحًا</bdi></div><div class="sgd">Fatha + tanween <b>ـً</b>, written with an extra alif <b>ـًا</b></div></div>
  <div class="sg"><div class="sgt">Except after ة or ـاء</div><div class="sga"><bdi>رَغْبَةً</bdi> · <bdi>مَسَاءً</bdi></div><div class="sgd">Fatha + tanween, <b>no</b> extra alif</div></div>
</div>'''

def glance():
    rows = [("obj", "What? Whom?", "The thing the action falls on.", "كَتَبَ الطَّالِبُ الدَّرْسَ"),
            ("purp", "Why?", "The reason. Usually an action noun with tanween.", "وَقَفَ الطَّالِبُ احْتِرَامًا"),
            ("when", "When? Where?", "A time or place word, with no preposition.", "سَافَرَ زَيْدٌ صَبَاحًا"),
            ("state", "How?", "The state of the doer or object. No ال.", "جَاءَ زَيْدٌ مُسْرِعًا")]
    trs = "".join(f'<tr><td>{pill(k)}<div class="garr">{e(R[k][1])}</div></td><td><b>{q}</b><div class="gd">{d}</div></td>'
                  f'<td class="gex" dir="rtl">{e(x)}</td></tr>' for k, q, d, x in rows)
    return f'<table class="glance"><tr><th>Job</th><th>Ask</th><th>Example</th></tr>{trs}</table>'

def lesson():
    S = []
    S.append(f'''
<div class="hero">
  <div class="eyebrow">LESSON NOTES · COLOUR-CODED EXAMPLES</div>
  <h1>Naṣb: when does a word<br>end in <span class="gold">fatha</span>?</h1>
  <p>Some words in a verb sentence answer a question about the action: what, why, when, where, how. Those words take naṣb.</p>
  <div class="wm">النَّصْب</div>
</div>
{h2(1, "Where we are")}
<p class="sub">Four cases. We know two. Today we add the third.</p>
{cases()}
<div class="scope"><b>Today we keep it simple.</b>
  <ul><li>Only <b>past verbs</b> (كَتَبَ) and <b>order verbs</b> (اُكْتُبْ). Present verbs come later.</li>
  <li>Only one sign of naṣb: the <b>fatha</b> ـَ / ـً. The other signs come later, one chapter for each group (dual, plurals).</li></ul></div>
{h2(2, "A new sentence: the verb sentence")}
<p class="sub">Last lesson the sentence started with a noun (Topic + Information). Now it starts with a verb: <b>Verb + Doer</b>.</p>
<div class="rule"><div class="rr" style="border-color:{R["verb"][2]}"><b style="color:{R["verb"][4]}">Verb · fixed</b>
  <p>A past verb and an order verb are fixed (مَبْنِيّ): their ending never changes. Past: fatha <bdi class="ab">كَتَبَ</bdi>. Order: sukūn <bdi class="ab">اُكْتُبْ</bdi>.</p></div>
  <div class="rr" style="border-color:{R["doer"][2]}"><b style="color:{R["doer"][4]}">Doer · rafʿ</b>
  <p>The doer is who did the action. It takes rafʿ: damma, like the Topic. In an order the doer is “you”, hidden inside the verb.</p></div></div>
<div class="pair">
{example("A", "Zayd wrote.", [V("كَتَبَ"), G("doer", W("زَيْدٌ", v=DAMMATAN))],
         [("verb", "{كَتَبَ} past verb: fixed. Its fatha never changes."), ("doer", "{زَيْدٌ} the doer → rafʿ, damma.")])}
{example("B", "Write!", [V("اُكْتُبْ", True), HID],
         [("verb", "{اُكْتُبْ} order verb: fixed on sukūn."), ("doer", "The doer is “you” {(أَنْتَ)}, hidden.")])}
</div>
<div class="tipbox"><b>Careful:</b> the fatha on <bdi class="ab">كَتَبَ</bdi> is <b>not</b> naṣb. A past verb ends in fatha in every sentence: it is fixed. Naṣb is for nouns.</div>
{h2(3, "The sign of naṣb: fatha", "pb")}
<p class="sub">It works exactly like damma and kasra: one vowel with ال or when owned, tanween otherwise.</p>
{sign_rules()}
{h2(4, "Colour key: the new jobs")}
<p class="sub">Big box = the word's job in the sentence. Small box = a word with its own rule.</p>
{colour_key()}
{h2(5, "The four naṣb jobs at a glance")}
<p class="sub">Find the verb and the doer. For every other noun, ask the question. The one it answers is its job.</p>
{glance()}
''')
    # Object
    S.append(f'''{h2(6, "Object · مَفْعُولٌ بِهِ", "pb")}
<div class="rbox" style="border-color:{R["obj"][2]};background:{R["obj"][3]}"><b>Rule.</b> The object is the thing the action falls on. Ask <b>“what?”</b> or <b>“whom?”</b> after the verb. Object → naṣb, fatha.</div>
{example(1, "The student wrote the lesson.", [V("كَتَبَ"), G("doer", W("الطَّالِبُ", v=DAMMA)), G("obj", W("الدَّرْسَ", v=FATHA))],
  [("doer", "{الطَّالِبُ} who wrote? → doer → damma."), ("obj", "{الدَّرْسَ} what did he write? → object → fatha.")])}
{example(2, "Zayd read a book.", [V("قَرَأَ"), G("doer", W("زَيْدٌ", v=DAMMATAN)), G("obj", W("كِتَابًا", v=FATHATAN))],
  [("obj", "{كِتَابًا} what did he read? → object. No ال → fatha + tanween, with an extra alif.")])}
{example(3, "Open the door!", [V("اِفْتَحِ", True), HID, G("obj", W("البَابَ", v=FATHA))],
  [("verb", "{اِفْتَحِ} order verb: fixed. The kasra is only a bridge to ال, not iʿrāb."), ("obj", "{البَابَ} open what? → object → fatha.")])}
{example(4, "The student read the teacher's book.", [V("قَرَأَ"), G("doer", W("الطَّالِبُ", v=DAMMA)), G("obj", W("كِتَابَ", v=FATHA), W("المُدَرِّسِ", "owner", KASRA))],
  [("obj", "{كِتَابَ} object → fatha. It is owned → no tanween."), ("owner", "{المُدَرِّسِ} “book of the teacher”: owner → kasra.")],
  tip="An order verb ending in sukūn takes a small kasra before ال: {اِفْتَحِ البَابَ}, {اِشْرَبِ المَاءَ}. The verb is still fixed.")}
''')
    # Purpose
    S.append(f'''{h2(7, "Purpose · مَفْعُولٌ لِأَجْلِهِ")}
<div class="rbox" style="border-color:{R["purp"][2]};background:{R["purp"][3]}"><b>Rule.</b> The purpose gives the reason for the action. Ask <b>“why?”</b>. It is usually an action noun (respect, desire, seeking) with tanween. Purpose → naṣb, fatha.</div>
{example(5, "The student stood up out of respect.", [V("وَقَفَ"), G("doer", W("الطَّالِبُ", v=DAMMA)), G("purp", W("احْتِرَامًا", v=FATHATAN))],
  [("purp", "{احْتِرَامًا} why did he stand? → purpose → fatha + tanween.")])}
{example(6, "Zayd studied out of desire for success.", [V("دَرَسَ"), G("doer", W("زَيْدٌ", v=DAMMATAN)), G("purp", W("رَغْبَةً", v=FATHATAN), W("فِي", "particle"), W("النَّجَاحِ", "prep", KASRA))],
  [("purp", "{رَغْبَةً} why did he study? → purpose → fatha + tanween. After ة: no extra alif."), ("prep", "{النَّجَاحِ} after {فِي} → kasra.")])}
{example(7, "Ali travelled seeking knowledge.", [V("سَافَرَ"), G("doer", W("عَلِيٌّ", v=DAMMATAN)), G("purp", W("طَلَبًا", v=FATHATAN), W("لِلْعِلْمِ", "prep", KASRA))],
  [("purp", "{طَلَبًا} why did he travel? → purpose → fatha + tanween."), ("prep", "{لِلْعِلْمِ} = {لِ} “for” + {العِلْمِ}: after a preposition → kasra.")],
  tip="Object or purpose? {قَرَأَ زَيْدٌ كِتَابًا}: “what did he read?” → object. {وَقَفَ زَيْدٌ احْتِرَامًا}: “why did he stand?” → purpose.")}
''')
    # Time / place
    S.append(f'''{h2(8, "Time / place · مَفْعُولٌ فِيهِ")}
<div class="rbox" style="border-color:{R["when"][2]};background:{R["when"][3]}"><b>Rule.</b> A word of time or place that tells us when or where the action happened, <b>with no preposition</b>. Ask <b>“when?”</b> or <b>“where?”</b>. Time/place → naṣb, fatha.</div>
{example(8, "Zayd travelled in the morning.", [V("سَافَرَ"), G("doer", W("زَيْدٌ", v=DAMMATAN)), G("when", W("صَبَاحًا", v=FATHATAN))],
  [("when", "{صَبَاحًا} when did he travel? → time → fatha + tanween.")])}
{example(9, "The boy came back in the evening.", [V("رَجَعَ"), G("doer", W("الوَلَدُ", v=DAMMA)), G("when", W("مَسَاءً", v=FATHATAN))],
  [("when", "{مَسَاءً} when? → time → fatha + tanween. Ends in ـاء: no extra alif.")])}
{example(10, "The student sat in front of the teacher.", [V("جَلَسَ"), G("doer", W("الطَّالِبُ", v=DAMMA)), G("when", W("أَمَامَ", v=FATHA), W("المُدَرِّسِ", "owner", KASRA))],
  [("when", "{أَمَامَ} where did he sit? → place → fatha. It is owned → no tanween."), ("owner", "{المُدَرِّسِ} “in front of the teacher”: owner → kasra.")])}
{example(11, "Sit under the tree!", [V("اِجْلِسْ", True), HID, G("when", W("تَحْتَ", v=FATHA), W("الشَّجَرَةِ", "owner", KASRA))],
  [("when", "{تَحْتَ} sit where? → place → fatha, owned."), ("owner", "{الشَّجَرَةِ} owner → kasra.")])}
{example(12, "Ali went out on Friday.", [V("خَرَجَ"), G("doer", W("عَلِيٌّ", v=DAMMATAN)), G("when", W("يَوْمَ", v=FATHA), W("الجُمُعَةِ", "owner", KASRA))],
  [("when", "{يَوْمَ} when? → time → fatha, owned (“the day of Friday”)."), ("owner", "{الجُمُعَةِ} owner → kasra.")],
  tip="No preposition = naṣb. {جَلَسَ زَيْدٌ أَمَامَ البَيْتِ}: {أَمَامَ} → fatha. {جَلَسَ زَيْدٌ فِي البَيْتِ}: there is a preposition, so {البَيْتِ} → kasra.")}
''')
    # State
    S.append(f'''{h2(9, "State · حَال")}
<div class="rbox" style="border-color:{R["state"][2]};background:{R["state"][3]}"><b>Rule.</b> The state tells us how the doer (or the object) was during the action. Ask <b>“how?”</b>. It has <b>no ال</b>, so it almost always takes tanween. State → naṣb, fatha.</div>
{example(13, "Zayd came hurrying.", [V("جَاءَ"), G("doer", W("زَيْدٌ", v=DAMMATAN)), G("state", W("مُسْرِعًا", v=FATHATAN))],
  [("state", "{مُسْرِعًا} how did he come? → state → fatha + tanween.")])}
{example(14, "The boy came back happy.", [V("رَجَعَ"), G("doer", W("الوَلَدُ", v=DAMMA)), G("state", W("فَرِحًا", v=FATHATAN))],
  [("state", "{فَرِحًا} how did he come back? → state → fatha + tanween.")])}
{example(15, "The student entered the class smiling.", [V("دَخَلَ"), G("doer", W("الطَّالِبُ", v=DAMMA)), G("obj", W("الصَّفَّ", v=FATHA)), G("state", W("مُبْتَسِمًا", v=FATHATAN))],
  [("obj", "{الصَّفَّ} entered what? → object → fatha."), ("state", "{مُبْتَسِمًا} how did he enter? → state → fatha + tanween.")])}
{example(16, "Drink the water cold!", [V("اِشْرَبِ", True), HID, G("obj", W("المَاءَ", v=FATHA)), G("state", W("بَارِدًا", v=FATHATAN))],
  [("obj", "{المَاءَ} drink what? → object → fatha."), ("state", "{بَارِدًا} the state of the water → state → fatha + tanween.")],
  tip="State or adjective? {جَاءَ الطَّالِبُ المُسْرِعُ} “the hurrying student came”: adjective, has ال, copies damma. {جَاءَ الطَّالِبُ مُسْرِعًا} “the student came hurrying”: state, no ال, naṣb.")}
''')
    # Copying + all together
    S.append(f'''{h2(10, "Old rules, new ending")}
<p class="sub">An adjective and a word after وَ still copy. Now they can copy a fatha.</p>
{example(17, "Zayd read a new book.", [V("قَرَأَ"), G("doer", W("زَيْدٌ", v=DAMMATAN)), G("obj", W("كِتَابًا", v=FATHATAN), W("جَدِيدًا", "adj", FATHATAN))],
  [("obj", "{كِتَابًا} object → fatha + tanween."), ("adj", "{جَدِيدًا} describes {كِتَابًا} → copies: fatha + tanween.")])}
{example(18, "The student wrote the lesson and the homework.", [V("كَتَبَ"), G("doer", W("الطَّالِبُ", v=DAMMA)), G("obj", W("الدَّرْسَ", v=FATHA), W("وَالوَاجِبَ", "and", FATHA))],
  [("obj", "{الدَّرْسَ} object → fatha."), ("and", "{الوَاجِبَ} comes after وَ → copies {الدَّرْسَ}: fatha.")])}
{h2(11, "All together")}
{example(19, "The teacher opened the door in the morning.", [V("فَتَحَ"), G("doer", W("المُدَرِّسُ", v=DAMMA)), G("obj", W("البَابَ", v=FATHA)), G("when", W("صَبَاحًا", v=FATHATAN))],
  [("doer", "{المُدَرِّسُ} who opened? → doer → damma."), ("obj", "{البَابَ} opened what? → object → fatha."), ("when", "{صَبَاحًا} when? → time → fatha + tanween.")])}
{example(20, "Ali travelled at night seeking knowledge.", [V("سَافَرَ"), G("doer", W("عَلِيٌّ", v=DAMMATAN)), G("when", W("لَيْلًا", v=FATHATAN)), G("purp", W("طَلَبًا", v=FATHATAN), W("لِلْعِلْمِ", "prep", KASRA))],
  [("when", "{لَيْلًا} when? → time → fatha + tanween."), ("purp", "{طَلَبًا} why? → purpose → fatha + tanween."), ("prep", "{لِلْعِلْمِ} after {لِ} → kasra.")])}
{example(21, "The hardworking student sat in front of the teacher, smiling.", [V("جَلَسَ"), G("doer", W("الطَّالِبُ", v=DAMMA), W("المُجْتَهِدُ", "adj", DAMMA)), G("when", W("أَمَامَ", v=FATHA), W("المُدَرِّسِ", "owner", KASRA)), G("state", W("مُبْتَسِمًا", v=FATHATAN))],
  [("doer", "{الطَّالِبُ} doer → damma."), ("adj", "{المُجْتَهِدُ} describes the doer → copies damma."), ("when", "{أَمَامَ} where? → place → fatha, owned."), ("owner", "{المُدَرِّسِ} owner → kasra."), ("state", "{مُبْتَسِمًا} how? → state → fatha + tanween.")],
  tip="This one uses almost every colour. Verb and doer first, then ask what / why / when / where / how for the rest.")}
<div class="three">
  <h3>Iʿrāb in five questions</h3>
  <ol>
    <li><b>Is it a verb or a particle?</b> → fixed, it never changes <span class="wc">—</span></li>
    <li><b>Topic, information, or doer?</b> → <span class="wc">ـُ</span></li>
    <li><b>Does it answer what? why? when? where? how?</b> → <span class="wc">ـَ</span></li>
    <li><b>Is there a preposition or an owner relationship?</b> → <span class="wc">ـِ</span></li>
    <li><b>Is it an adjective, or after وَ?</b> → copy the word it follows <span class="wc">=</span></li>
  </ol>
</div>
''')
    return "".join(S)

PRACTICE = [
 dict(en="The boy drank the milk.", g=[V("شَرِبَ"), G("doer", W("الوَلَدُ", v=DAMMA)), G("obj", W("الحَلِيبَ", v=FATHA))]),
 dict(en="Read a book!", g=[V("اِقْرَأْ", True), HID, G("obj", W("كِتَابًا", v=FATHATAN))]),
 dict(en="Zayd went out in the evening.", g=[V("خَرَجَ"), G("doer", W("زَيْدٌ", v=DAMMATAN)), G("when", W("مَسَاءً", v=FATHATAN))]),
 dict(en="The boy stood up out of respect.", g=[V("وَقَفَ"), G("doer", W("الوَلَدُ", v=DAMMA)), G("purp", W("احْتِرَامًا", v=FATHATAN))]),
 dict(en="The teacher entered the class smiling.", g=[V("دَخَلَ"), G("doer", W("المُدَرِّسُ", v=DAMMA)), G("obj", W("الصَّفَّ", v=FATHA)), G("state", W("مُبْتَسِمًا", v=FATHATAN))]),
 dict(en="Sit in front of the teacher!", g=[V("اِجْلِسْ", True), HID, G("when", W("أَمَامَ", v=FATHA), W("المُدَرِّسِ", "owner", KASRA, ref="أَمَامَ"))]),
 dict(en="The student read a new book.", g=[V("قَرَأَ"), G("doer", W("الطَّالِبُ", v=DAMMA)), G("obj", W("كِتَابًا", v=FATHATAN), W("جَدِيدًا", "adj", FATHATAN, ref="كِتَابًا"))]),
 dict(en="Zayd and Ali sat under the tree.", g=[V("جَلَسَ"), G("doer", W("زَيْدٌ", v=DAMMATAN), W("وَعَلِيٌّ", "and", DAMMATAN, ref="زَيْدٌ")), G("when", W("تَحْتَ", v=FATHA), W("الشَّجَرَةِ", "owner", KASRA, ref="تَحْتَ"))]),
]

def practice():
    out = [f'<div class="pb">{h2(12, "Your turn", "nomt")}<p class="sub">Eight sentences. Every ending is missing. Work alone, then check with a partner and the answer key.</p></div>']
    cards = [practice_card(i + 1, p) for i, p in enumerate(PRACTICE)]
    # first page has heading: 1 card, then pairs
    out.append(f'<div class="cardpage first">{cards[0]}</div>')
    rest = cards[1:]
    for k in range(0, len(rest), 2):
        pair = rest[k:k + 2]
        out.append(f'<div class="cardpage">{pair[0]}' + (f'<div class="cut"><span>✂</span></div>{pair[1]}' if len(pair) > 1 else "") + '</div>')
    out.append(f'<div class="pb">{h2(13, "Answer key", "nomt")}<p class="sub">Full iʿrāb of each practice sentence.</p></div>')
    out.append("".join(key_card(i + 1, p) for i, p in enumerate(PRACTICE)))
    return "".join(out)

if __name__ == "__main__":
    css = open("style.css", encoding="utf-8").read() + open("lesson.css", encoding="utf-8").read()
    doc = (f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head>'
           f'<body class="flow">{lesson()}{practice()}</body></html>')
    open("lesson.html", "w", encoding="utf-8").write(doc)
    print("ok")
