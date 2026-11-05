# -*- coding: utf-8 -*-
"""Stage 2 · Naṣb Class Exercise: 15 sentences, past and order verbs, naṣb by fatha only.

Same PRACTICE format as content/lesson.py: dict(en=..., g=[groups]).
Small boxes always carry ref= (the word they depend on) for the answer-key reasons.
"""
import lesson as L
from lesson import W, G, V, HID, R, e, h2, DAMMA, DAMMATAN, FATHA, FATHATAN, KASRA

P = "particle"

PRACTICE = [
 dict(en="The student wrote the letter.",
      g=[V("كَتَبَ"), G("doer", W("الطَّالِبُ", v=DAMMA)), G("obj", W("الرِّسَالَةَ", v=FATHA))]),
 dict(en="The girl washed the garment.",
      g=[V("غَسَلَتِ"), G("doer", W("البِنْتُ", v=DAMMA)), G("obj", W("الثَّوْبَ", v=FATHA))]),
 dict(en="Write the lesson!",
      g=[V("اُكْتُبِ", True), HID, G("obj", W("الدَّرْسَ", v=FATHA))]),
 dict(en="The father came back at night.",
      g=[V("رَجَعَ"), G("doer", W("الأَبُ", v=DAMMA)), G("when", W("لَيْلًا", v=FATHATAN))]),
 dict(en="The boy sat behind the door.",
      g=[V("جَلَسَ"), G("doer", W("الوَلَدُ", v=DAMMA)), G("when", W("خَلْفَ", v=FATHA), W("البَابِ", "owner", KASRA, ref="خَلْفَ"))]),
 dict(en="The merchant travelled seeking a livelihood.",
      g=[V("سَافَرَ"), G("doer", W("التَّاجِرُ", v=DAMMA)), G("purp", W("طَلَبًا", v=FATHATAN), W("لِلرِّزْقِ", "prep", KASRA, ref="لِ"))]),
 dict(en="The mother entered the kitchen in a hurry.",
      g=[V("دَخَلَتِ"), G("doer", W("الأُمُّ", v=DAMMA)), G("obj", W("المَطْبَخَ", v=FATHA)), G("state", W("مُسْرِعَةً", v=FATHATAN))]),
 dict(en="The boy ate the apple happily.",
      g=[V("أَكَلَ"), G("doer", W("الوَلَدُ", v=DAMMA)), G("obj", W("التُّفَّاحَةَ", v=FATHA)), G("state", W("فَرِحًا", v=FATHATAN))]),
 dict(en="Open the window in the morning!",
      g=[V("اِفْتَحِ", True), HID, G("obj", W("النَّافِذَةَ", v=FATHA)), G("when", W("صَبَاحًا", v=FATHATAN))]),
 dict(en="The student read a useful book.",
      g=[V("قَرَأَ"), G("doer", W("الطَّالِبُ", v=DAMMA)), G("obj", W("كِتَابًا", v=FATHATAN), W("مُفِيدًا", "adj", FATHATAN, ref="كِتَابًا"))]),
 dict(en="Zayd visited the mosque on Friday.",
      g=[V("زَارَ"), G("doer", W("زَيْدٌ", v=DAMMATAN)), G("obj", W("المَسْجِدَ", v=FATHA)),
         G("when", W("يَوْمَ", v=FATHA), W("الجُمُعَةِ", "owner", KASRA, ref="يَوْمَ"))]),
 dict(en="The doctor came out of the house in a hurry.",
      g=[V("خَرَجَ"), G("doer", W("الطَّبِيبُ", v=DAMMA)), G("prep", W("مِنَ", P), W("البَيْتِ", "prep", KASRA, ref="مِنَ")),
         G("state", W("مُسْرِعًا", v=FATHATAN))]),
 dict(en="The teacher wrote the lesson and the question.",
      g=[V("كَتَبَ"), G("doer", W("المُدَرِّسُ", v=DAMMA)), G("obj", W("الدَّرْسَ", v=FATHA), W("وَالسُّؤَالَ", "and", FATHA, ref="الدَّرْسَ"))]),
 dict(en="The girl sat in front of the teacher, silent.",
      g=[V("جَلَسَتِ"), G("doer", W("البِنْتُ", v=DAMMA)), G("when", W("أَمَامَ", v=FATHA), W("المُدَرِّسَةِ", "owner", KASRA, ref="أَمَامَ")),
         G("state", W("صَامِتَةً", v=FATHATAN))]),
 dict(en="The merchant opened the shop in the morning, wanting profit.",
      g=[V("فَتَحَ"), G("doer", W("التَّاجِرُ", v=DAMMA)), G("obj", W("الدُّكَّانَ", v=FATHA)), G("when", W("صَبَاحًا", v=FATHATAN)),
         G("purp", W("رَغْبَةً", v=FATHATAN), W("فِي", P), W("الرِّبْحِ", "prep", KASRA, ref="فِي"))]),
]

def intro(title_html, eyebrow, blurb, steps, wm="النَّصْب"):
    how = "".join(f'<div class="hw"><div class="hn">{i}</div><b>{e(t)}</b><p>{e(d)}</p></div>' for i, (t, d) in enumerate(steps, 1))
    return f'''
<div class="hero">
  <div class="eyebrow">{e(eyebrow)}</div>
  <h1>{title_html}</h1>
  <p>{e(blurb)}</p>
  <div class="wm">{e(wm)}</div>
</div>
{h2(1, "How it works")}
<div class="how">{how}</div>
{h2(2, "Colour key")}
<p class="sub">Same colours as the naṣb lesson. Verb and doer first, then ask what, why, when, where or how.</p>
{L.colour_key()}
<div class="tipbox"><b>Watch the endings.</b> A past verb and an order verb never change. The doer takes rafʿ (damma).
The object, purpose, time or place, and state take naṣb (fatha). With ال or when owned: one fatha. Otherwise fatha + tanween (ـًا, no extra alif after ة).</div>
<div class="three">
  <h3>Iʿrāb in five questions</h3>
  <ol>
    <li><b>Is it a verb or a particle?</b> → fixed, it never changes <span class="wc">—</span></li>
    <li><b>Topic, information, or doer?</b> → <span class="wc">ـُ</span></li>
    <li><b>Does it answer what? why? when? where? how?</b> → <span class="wc">ـَ</span></li>
    <li><b>Is there a preposition or an owner relationship?</b> → <span class="wc">ـِ</span></li>
    <li><b>Is it an adjective, or after وَ?</b> → copy the word it follows <span class="wc">=</span></li>
  </ol>
</div>'''

def notes():
    return intro('Naṣb <span class="gold">practice</span>:<br>15 sentences', "CLASS EXERCISE · STAGE 2",
                 "Every ending is missing. Give the full iʿrāb: find the verb and the doer, then the job of every other word.",
                 [("Read aloud", "Read the whole sentence and the English meaning."),
                  ("Verb and doer", "Who did it? In an order, the doer is a hidden “you”."),
                  ("Ask the question", "What? Why? When or where? How? The answer gives the job."),
                  ("Check", "Compare with a partner, then press Check.")])
