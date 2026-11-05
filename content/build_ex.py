# -*- coding: utf-8 -*-
"""I'rab class exercise: 15 new sentences, same card format as the table quiz, no scoring."""
import re
import build as B
from build import DAMMA, DAMMATAN, KASRA, KASRATAN, P, e

Q = [
 dict(en="The mosque is big.", lvl=1,
      topic=[("المَسْجِدُ","head",DAMMA)], info=[("كَبِيرٌ","head",DAMMATAN)]),
 dict(en="I am a student.", lvl=1,
      topic=[("أَنَا","fixed",None)], info=[("طَالِبٌ","head",DAMMATAN)]),
 dict(en="The girl is in the school.", lvl=1,
      topic=[("البِنْتُ","head",DAMMA)], info=[("فِي",P,None),("المَدْرَسَةِ","prep",KASRA,"فِي")]),
 dict(en="The chair is in the room.", lvl=1,
      topic=[("الكُرْسِيُّ","head",DAMMA)], info=[("فِي",P,None),("الغُرْفَةِ","prep",KASRA,"فِي")]),
 dict(en="The girl's pen is beautiful.", lvl=2,
      topic=[("قَلَمُ","head",DAMMA),("البِنْتِ","owner",KASRA,"قَلَمُ")], info=[("جَمِيلٌ","head",DAMMATAN)]),
 dict(en="The big house is new.", lvl=2,
      topic=[("البَيْتُ","head",DAMMA),("الكَبِيرُ","adj",DAMMA,"البَيْتُ")], info=[("جَدِيدٌ","head",DAMMATAN)]),
 dict(en="Ali is a hardworking student.", lvl=2,
      topic=[("عَلِيٌّ","head",DAMMATAN)], info=[("طَالِبٌ","head",DAMMATAN),("مُجْتَهِدٌ","adj",DAMMATAN,"طَالِبٌ")]),
 dict(en="The car key is on the desk.", lvl=2,
      topic=[("مِفْتَاحُ","head",DAMMA),("السَّيَّارَةِ","owner",KASRA,"مِفْتَاحُ")],
      info=[("عَلَى",P,None),("المَكْتَبِ","prep",KASRA,"عَلَى")]),
 dict(en="The doctor and the teacher are in the mosque.", lvl=2,
      topic=[("الطَّبِيبُ","head",DAMMA),("وَالمُدَرِّسُ","and",DAMMA,"الطَّبِيبُ")],
      info=[("فِي",P,None),("المَسْجِدِ","prep",KASRA,"فِي")]),
 dict(en="The boy is in a small room.", lvl=2,
      topic=[("الوَلَدُ","head",DAMMA)],
      info=[("فِي",P,None),("غُرْفَةٍ","prep",KASRATAN,"فِي"),("صَغِيرَةٍ","adj",KASRATAN,"غُرْفَةٍ")]),
 dict(en="Ali's house is in the city.", lvl=3,
      topic=[("بَيْتُ","head",DAMMA),("عَلِيٍّ","owner",KASRATAN,"بَيْتُ")],
      info=[("فِي",P,None),("المَدِينَةِ","prep",KASRA,"فِي")]),
 dict(en="The student's new book is on the chair.", lvl=3,
      topic=[("كِتَابُ","head",DAMMA),("الطَّالِبِ","owner",KASRA,"كِتَابُ"),("الجَدِيدُ","adj",DAMMA,"كِتَابُ")],
      info=[("عَلَى",P,None),("الكُرْسِيِّ","prep",KASRA,"عَلَى")]),
 dict(en="The little girl's bag is in the car.", lvl=3,
      topic=[("حَقِيبَةُ","head",DAMMA),("البِنْتِ","owner",KASRA,"حَقِيبَةُ"),("الصَّغِيرَةِ","adj",KASRA,"البِنْتِ")],
      info=[("فِي",P,None),("السَّيَّارَةِ","prep",KASRA,"فِي")]),
 dict(en="The mother and the girl are in Zayd's house.", lvl=3,
      topic=[("الأُمُّ","head",DAMMA),("وَالبِنْتُ","and",DAMMA,"الأُمُّ")],
      info=[("فِي",P,None),("بَيْتِ","prep",KASRA,"فِي"),("زَيْدٍ","owner",KASRATAN,"بَيْتِ")]),
 dict(en="The teacher of the big school is a kind man.", lvl=3,
      topic=[("مُدَرِّسُ","head",DAMMA),("المَدْرَسَةِ","owner",KASRA,"مُدَرِّسُ"),("الكَبِيرَةِ","adj",KASRA,"المَدْرَسَةِ")],
      info=[("رَجُلٌ","head",DAMMATAN),("طَيِّبٌ","adj",DAMMATAN,"رَجُلٌ")]),
]

def footer(n, N):
    return f'<div class="foot"><span>Arabic · Iʿrāb Class Exercise</span><span>{n} / {N}</span></div>'

def card(i, q):
    c = B.card(i, q)
    c = re.sub(r'<div class="pts">.*?</div>', '', c, flags=re.S)
    return c.replace("Say the reason aloud.", "Write the reason in your notebook.")

def key_card(i, q):
    return re.sub(r'<span class="kp">.*?</span>', '', B.key_card(i, q))

def build():
    KEY_PER = 4
    N = 1 + 8 + -(-15 // KEY_PER)
    pages = [f'''
<div class="page">
  <div class="hero">
    <div class="eyebrow">CLASS EXERCISE · FULL IʿRĀB</div>
    <h1>Iʿrāb <span class="gold">practice</span>:<br>15 sentences</h1>
    <p>Every ending is missing. Draw the big boxes, then give every word its ending and its job. Work alone first, then check with a partner.</p>
    <div class="wm">الإِعْرَاب</div>
  </div>
  <h2><span class="num">1</span>How to work</h2>
  <div class="how">
    <div class="hw"><div class="hn">1</div><b>Read aloud</b><p>Read the whole sentence and the English meaning.</p></div>
    <div class="hw"><div class="hn">2</div><b>Big boxes first</b><p>Where does the Topic end and the Information start?</p></div>
    <div class="hw"><div class="hn">3</div><b>Word by word</b><p>Fixed or particle? If not: preposition, owner, adjective, after وَ?</p></div>
    <div class="hw"><div class="hn">4</div><b>Check</b><p>Compare with a partner, then with the answer key.</p></div>
  </div>
  <h2><span class="num">2</span>Colour key</h2>
  <p class="sub">Same colours as the lesson. The job gives the colour, the colour gives the ending.</p>
  <div class="kkgrid">{B.keybox()}</div>
  <div class="tipbox"><b>Watch the tanween.</b> A word with ال, or a word that is owned (the first word of “the book <i>of</i> …”), never takes tanween: a single vowel only. Particles like فِي and عَلَى, and fixed words like أَنَا, never change: circle —.</div>
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
    pn = 2
    for k in range(0, 15, 2):
        c1 = card(k + 1, Q[k])
        c2 = card(k + 2, Q[k + 1]) if k + 1 < 15 else '''
<div class="card done"><div class="donein"><div class="big">✎</div><b>Make your own</b>
<p>Write one sentence of your own with a Topic, an owner and a preposition. Swap with a partner and give the full iʿrāb of each other's sentence.</p>
<div class="line" style="margin-top:8mm"></div><div class="line"></div></div></div>'''
        pages.append(f'<div class="page cards">{c1}<div class="cut"><span>✂</span></div>{c2}{footer(pn, N)}</div>')
        pn += 1
    for k in range(0, 15, KEY_PER):
        head = ('<h2 style="margin-top:0"><span class="num">3</span>Answer key</h2>'
                '<p class="sub">Full iʿrāb of each sentence. Big boxes first, then the small ones.</p>') if k == 0 else ""
        cards = "".join(key_card(i + 1, Q[i]) for i in range(k, min(k + KEY_PER, 15)))
        pages.append(f'<div class="page">{head}{cards}{footer(pn, N)}</div>')
        pn += 1
    return pages

if __name__ == "__main__":
    pages = build()
    doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{B.CSS}</style></head><body>{"".join(pages)}</body></html>'
    open("exercise.html", "w", encoding="utf-8").write(doc)
    print("pages:", len(pages))
