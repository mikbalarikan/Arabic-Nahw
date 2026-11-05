# -*- coding: utf-8 -*-
"""Stage 1 lesson notes: the Iʿrāb Colour Guide (rafʿ + jarr), rebuilt from the class PDF."""
import build as B
import lesson as L
from lesson import W, G, R, e, ar, h2, example, DAMMA, DAMMATAN, KASRA, KASRATAN

P = "particle"
def FX(t): return W(t, "fixed", lab="fixed")

def cases_html():
    items = [("A", DAMMA, "رَفْع", "rafʿ · damma", "In this lesson", "now"),
             ("B", "َ", "نَصْب", "naṣb · fatha", "Stage 2", "later"),
             ("C", KASRA, "جَرّ", "jarr · kasra", "In this lesson", "now"),
             ("D", "ْ", "جَزْم", "jazm · sukūn", "Verbs only", "later")]
    out = "".join(f'<div class="case {c}"><span class="cl">{l}</span><div class="cm">ـ{m}</div><div class="ca">{a}</div>'
                  f'<div class="ce">{en}</div><div class="cs">{st}</div></div>' for l, m, a, en, st, c in items)
    return f'<div class="cases">{out}</div>'

def notes():
    S = [f'''
<div class="hero">
  <div class="eyebrow">LESSON NOTES · COLOUR-CODED EXAMPLES</div>
  <h1>Iʿrāb: why does the end<br>of a word <span class="gold">change</span>?</h1>
  <p>Every word has a job in the sentence. The job gives it a colour, and the colour tells you its last vowel.</p>
  <div class="wm">الإِعْرَاب</div>
</div>
{h2(1, "Fixed or flexible?")}
<div class="rule">
  <div class="rr" style="border-color:#9aa0a8"><b style="color:#5f6672">Fixed · مَبْنِيّ</b>
    <p>The ending never changes: <bdi class="ab">أَنَا · هُوَ · فِي · عَلَى</bdi></p></div>
  <div class="rr" style="border-color:#0f5257"><b style="color:#0f5257">Flexible · مُعْرَب</b>
    <p>The ending changes with the word's job. There are four cases:</p></div>
</div>
{cases_html()}
{h2(2, "Colour key")}
<p class="sub">We use these colours in every example. Big box = the word's job in the sentence. Small box = a word with its own rule.</p>
<div class="kkgrid">{B.keybox()}</div>
{h2(3, "Topic + Information: the simplest sentence")}
<p class="sub">Arabic has no word for “is” here. Say the topic, add the information, and the sentence is complete. Both take rafʿ (damma).</p>
<div class="pair">
{example("A", "I am a student.", [G("topic", FX("أَنَا")), G("info", W("طَالِبٌ", v=DAMMATAN))],
  [("topic", "{أَنَا} is the topic. It is a fixed word: its ending never changes."), ("info", "{طَالِبٌ} is the information → rafʿ, damma (ـٌ).")])}
{example("B", "He is a doctor.", [G("topic", FX("هُوَ")), G("info", W("طَبِيبٌ", v=DAMMATAN))],
  [("topic", "{هُوَ} is the topic, a fixed word."), ("info", "{طَبِيبٌ} is the information → rafʿ, damma (ـٌ).")])}
</div>
{h2(4, "Lesson examples")}
<p class="sub">Look at the big boxes first (topic or information?), then at the rule in each small box.</p>
{example(1, "Zayd is the teacher of Arabic.", [G("topic", W("زَيْدٌ", v=DAMMATAN)), G("info", W("مُدَرِّسُ", v=DAMMA), W("العَرَبِيَّةِ", "owner", KASRA))],
  [("topic", "{زَيْدٌ} topic → damma."), ("info", "{مُدَرِّسُ} information → damma."), ("owner", "{العَرَبِيَّةِ} “teacher of Arabic”: ownership → jarr, kasra.")],
  tip="The first word of an ownership pair ({مُدَرِّسُ}) never takes tanween: a single damma is enough.")}
{example(2, "The student's book is on the desk.", [G("topic", W("كِتَابُ", v=DAMMA), W("الطَّالِبِ", "owner", KASRA)), G("info", W("عَلَى", P), W("المَكْتَبِ", "prep", KASRA))],
  [("topic", "{كِتَابُ الطَّالِبِ} topic → the first word takes damma."), ("owner", "{الطَّالِبِ} “book of the student”: ownership → kasra."),
   ("info", "{عَلَى المَكْتَبِ} information (where is it?)."), ("prep", "{المَكْتَبِ} comes after the preposition {عَلَى} → kasra.")])}
{example(3, "Zayd and Ali are at the university.", [G("topic", W("زَيْدٌ", v=DAMMATAN), W("وَعَلِيٌّ", "and", DAMMATAN)), G("info", W("فِي", P), W("الجَامِعَةِ", "prep", KASRA))],
  [("topic", "{زَيْدٌ} topic → damma."), ("and", "{عَلِيٌّ} comes after {وَ} → copies {زَيْدٌ}: damma."), ("prep", "{الجَامِعَةِ} after the preposition {فِي} → kasra.")])}
{example(4, "The hardworking student is in the big class.", [G("topic", W("الطَّالِبُ", v=DAMMA), W("المُجْتَهِدُ", "adj", DAMMA)), G("info", W("فِي", P), W("الصَّفِّ", "prep", KASRA), W("الكَبِيرِ", "adj", KASRA))],
  [("topic", "{الطَّالِبُ} topic → damma."), ("adj", "{المُجْتَهِدُ} adjective, follows {الطَّالِبُ} → damma."),
   ("prep", "{الصَّفِّ} after {فِي} → kasra."), ("adj", "{الكَبِيرِ} adjective, follows {الصَّفِّ} → kasra.")],
  tip="Two adjectives, two different endings. An adjective has no rule of its own: it always copies its noun.")}
{example(5, "The door of the big class is broken.", [G("topic", W("بَابُ", v=DAMMA), W("الصَّفِّ", "owner", KASRA), W("الكَبِيرِ", "adj", KASRA)), G("info", W("مَكْسُورٌ", v=DAMMATAN))],
  [("topic", "{بَابُ} topic → damma."), ("owner", "{الصَّفِّ} “door of the class”: ownership → kasra."),
   ("adj", "{الكَبِيرِ} describes {الصَّفِّ} → copies its kasra."), ("info", "{مَكْسُورٌ} information → damma.")])}
{example(6, "The hardworking student's new book is on the desk.", [G("topic", W("كِتَابُ", v=DAMMA), W("الطَّالِبِ", "owner", KASRA), W("المُجْتَهِدِ", "adj", KASRA), W("الجَدِيدُ", "adj", DAMMA)), G("info", W("عَلَى", P), W("المَكْتَبِ", "prep", KASRA))],
  [("owner", "{الطَّالِبِ} ownership → kasra."), ("adj", "{المُجْتَهِدِ} “hardworking” describes the student → kasra."),
   ("adj", "{الجَدِيدُ} “new” describes the book → damma, like {كِتَابُ}."), ("prep", "{المَكْتَبِ} after {عَلَى} → kasra.")],
  tip="First ask “which noun does this adjective describe?”, then copy that noun's ending.")}
{example(7, "Muhammad, the trustworthy, is the Messenger of Allah.", [G("topic", W("مُحَمَّدٌ", v=DAMMATAN), W("الأَمِينُ", "adj", DAMMA)), G("info", W("رَسُولُ", v=DAMMA), W("اللَّهِ", "owner", KASRA))],
  [("topic", "{مُحَمَّدٌ} topic → damma."), ("adj", "{الأَمِينُ} “the trustworthy” describes Muhammad → damma."),
   ("info", "{رَسُولُ} information → damma."), ("owner", "{اللَّهِ} “Messenger of Allah”: ownership → kasra.")])}
{h2(5, "More examples")}
<p class="sub">New sentences, same rules. Cover the explanations and try to give the reason for each ending yourself.</p>
{example(8, "The new pen is in the bag.", [G("topic", W("القَلَمُ", v=DAMMA), W("الجَدِيدُ", "adj", DAMMA)), G("info", W("فِي", P), W("الحَقِيبَةِ", "prep", KASRA))],
  [("topic", "{القَلَمُ} topic → damma."), ("adj", "{الجَدِيدُ} describes {القَلَمُ} → damma."), ("prep", "{الحَقِيبَةِ} after {فِي} → kasra.")])}
{example(9, "The teacher's car is beautiful.", [G("topic", W("سَيَّارَةُ", v=DAMMA), W("المُدَرِّسِ", "owner", KASRA)), G("info", W("جَمِيلَةٌ", v=DAMMATAN))],
  [("topic", "{سَيَّارَةُ} topic → damma (no tanween: it is owned)."), ("owner", "{المُدَرِّسِ} “car of the teacher”: ownership → kasra."), ("info", "{جَمِيلَةٌ} information → damma.")])}
{example(10, "The father and the mother are in the house.", [G("topic", W("الأَبُ", v=DAMMA), W("وَالأُمُّ", "and", DAMMA)), G("info", W("فِي", P), W("البَيْتِ", "prep", KASRA))],
  [("topic", "{الأَبُ} topic → damma."), ("and", "{الأُمُّ} comes after {وَ} → copies {الأَبُ}: damma."), ("prep", "{البَيْتِ} after {فِي} → kasra.")])}
{example(11, "The small boy is the teacher's son.", [G("topic", W("الوَلَدُ", v=DAMMA), W("الصَّغِيرُ", "adj", DAMMA)), G("info", W("ابْنُ", v=DAMMA), W("المُدَرِّسِ", "owner", KASRA))],
  [("topic", "{الوَلَدُ} topic → damma."), ("adj", "{الصَّغِيرُ} describes {الوَلَدُ} → damma."), ("info", "{ابْنُ} information → damma."), ("owner", "{المُدَرِّسِ} “son of the teacher”: ownership → kasra.")])}
{example(12, "Zayd's pen and Ali's book are on the big desk.", [G("topic", W("قَلَمُ", v=DAMMA), W("زَيْدٍ", "owner", KASRATAN), W("وَكِتَابُ", "and", DAMMA), W("عَلِيٍّ", "owner", KASRATAN)), G("info", W("عَلَى", P), W("المَكْتَبِ", "prep", KASRA), W("الكَبِيرِ", "adj", KASRA))],
  [("topic", "{قَلَمُ} topic → damma."), ("owner", "{زَيْدٍ} and {عَلِيٍّ} are owners → kasra ({ـٍ} with a name)."), ("and", "{كِتَابُ} comes after {وَ} → copies {قَلَمُ}: damma."),
   ("prep", "{المَكْتَبِ} after {عَلَى} → kasra."), ("adj", "{الكَبِيرِ} describes {المَكْتَبِ} → kasra.")],
  tip="This one uses every colour. Work box by box: big boxes first, then the small ones.")}
<div class="three">
  <h3>Iʿrāb in three questions</h3>
  <ol>
    <li><b>What is its job?</b> Topic or information? → both take <span class="wc">ـُ</span></li>
    <li><b>Is there a preposition or an owner relationship?</b> → <span class="wc">ـِ</span></li>
    <li><b>Is it an adjective, or after وَ?</b> → copy the word it follows <span class="wc">=</span></li>
  </ol>
</div>''']
    return "".join(S)

# "Your turn" E1–E5, in the table-quiz format so the same card engine and key renderer apply
Q = [
 dict(en="The door is open.", lvl=1, topic=[("البَابُ", "head", DAMMA)], info=[("مَفْتُوحٌ", "head", DAMMATAN)]),
 dict(en="The book is on the chair.", lvl=1, topic=[("الكِتَابُ", "head", DAMMA)],
      info=[("عَلَى", "particle", None), ("الكُرْسِيِّ", "prep", KASRA, "عَلَى")]),
 dict(en="Zayd's house is big.", lvl=2, topic=[("بَيْتُ", "head", DAMMA), ("زَيْدٍ", "owner", KASRATAN, "بَيْتُ")],
      info=[("كَبِيرٌ", "head", DAMMATAN)]),
 dict(en="The boy and the girl are in the class.", lvl=2,
      topic=[("الوَلَدُ", "head", DAMMA), ("وَالبِنْتُ", "and", DAMMA, "الوَلَدُ")],
      info=[("فِي", "particle", None), ("الصَّفِّ", "prep", KASRA, "فِي")]),
 dict(en="The red pen is new.", lvl=2, topic=[("القَلَمُ", "head", DAMMA), ("الأَحْمَرُ", "adj", DAMMA, "القَلَمُ")],
      info=[("جَدِيدٌ", "head", DAMMATAN)]),
]
