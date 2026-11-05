# -*- coding: utf-8 -*-
"""Stage 2 · Naṣb Quiz: 15 sentences, past and order verbs, naṣb by fatha only.

Same PRACTICE format as content/lesson.py: dict(en=..., g=[groups]).
Small boxes always carry ref= (the word they depend on) for the answer-key reasons.
"""
from lesson import W, G, V, HID, DAMMA, DAMMATAN, FATHA, FATHATAN, KASRA
from nasb_exercise import intro

P = "particle"

PRACTICE = [
 dict(en="The man drank the coffee.",
      g=[V("شَرِبَ"), G("doer", W("الرَّجُلُ", v=DAMMA)), G("obj", W("القَهْوَةَ", v=FATHA))]),
 dict(en="Carry the bag!",
      g=[V("اِحْمِلِ", True), HID, G("obj", W("الحَقِيبَةَ", v=FATHA))]),
 dict(en="The child slept at noon.",
      g=[V("نَامَ"), G("doer", W("الطِّفْلُ", v=DAMMA)), G("when", W("ظُهْرًا", v=FATHATAN))]),
 dict(en="The boy stood up out of respect for the imam.",
      g=[V("وَقَفَ"), G("doer", W("الوَلَدُ", v=DAMMA)), G("purp", W("احْتِرَامًا", v=FATHATAN), W("لِلإِمَامِ", "prep", KASRA, ref="لِ"))]),
 dict(en="The girl came back happy.",
      g=[V("رَجَعَتِ"), G("doer", W("البِنْتُ", v=DAMMA)), G("state", W("فَرِحَةً", v=FATHATAN))]),
 dict(en="The student heard a beautiful voice.",
      g=[V("سَمِعَ"), G("doer", W("الطَّالِبُ", v=DAMMA)), G("obj", W("صَوْتًا", v=FATHATAN), W("جَمِيلًا", "adj", FATHATAN, ref="صَوْتًا"))]),
 dict(en="Write the answer on the board!",
      g=[V("اُكْتُبِ", True), HID, G("obj", W("الجَوَابَ", v=FATHA)), G("prep", W("عَلَى", P), W("السَّبُّورَةِ", "prep", KASRA, ref="عَلَى"))]),
 dict(en="The imam sat under the big tree.",
      g=[V("جَلَسَ"), G("doer", W("الإِمَامُ", v=DAMMA)),
         G("when", W("تَحْتَ", v=FATHA), W("الشَّجَرَةِ", "owner", KASRA, ref="تَحْتَ"), W("الكَبِيرَةِ", "adj", KASRA, ref="الشَّجَرَةِ"))]),
 dict(en="The headmaster opened the school door in the morning.",
      g=[V("فَتَحَ"), G("doer", W("المُدِيرُ", v=DAMMA)), G("obj", W("بَابَ", v=FATHA), W("المَدْرَسَةِ", "owner", KASRA, ref="بَابَ")),
         G("when", W("صَبَاحًا", v=FATHATAN))]),
 dict(en="The hardworking student studied the lesson in the evening.",
      g=[V("دَرَسَ"), G("doer", W("الطَّالِبُ", v=DAMMA), W("المُجْتَهِدُ", "adj", DAMMA, ref="الطَّالِبُ")), G("obj", W("الدَّرْسَ", v=FATHA)),
         G("when", W("مَسَاءً", v=FATHATAN))]),
 dict(en="The father and the mother visited the teacher.",
      g=[V("زَارَ"), G("doer", W("الأَبُ", v=DAMMA), W("وَالأُمُّ", "and", DAMMA, ref="الأَبُ")), G("obj", W("المُدَرِّسَ", v=FATHA))]),
 dict(en="The guest ate the bread and the cheese.",
      g=[V("أَكَلَ"), G("doer", W("الضَّيْفُ", v=DAMMA)), G("obj", W("الخُبْزَ", v=FATHA), W("وَالجُبْنَ", "and", FATHA, ref="الخُبْزَ"))]),
 dict(en="Sit between the student and the teacher!",
      g=[V("اِجْلِسْ", True), HID,
         G("when", W("بَيْنَ", v=FATHA), W("الطَّالِبِ", "owner", KASRA, ref="بَيْنَ"), W("وَالمُدَرِّسِ", "and", KASRA, ref="الطَّالِبِ"))]),
 dict(en="The man entered the room silent.",
      g=[V("دَخَلَ"), G("doer", W("الرَّجُلُ", v=DAMMA)), G("obj", W("الغُرْفَةَ", v=FATHA)), G("state", W("صَامِتًا", v=FATHATAN))]),
 dict(en="The student attended the lesson on Saturday, wanting knowledge.",
      g=[V("حَضَرَ"), G("doer", W("الطَّالِبُ", v=DAMMA)), G("obj", W("الدَّرْسَ", v=FATHA)),
         G("when", W("يَوْمَ", v=FATHA), W("السَّبْتِ", "owner", KASRA, ref="يَوْمَ")),
         G("purp", W("رَغْبَةً", v=FATHATAN), W("فِي", P), W("العِلْمِ", "prep", KASRA, ref="فِي"))]),
]

def notes():
    return intro('Naṣb <span class="gold">quiz</span>:<br>15 sentences', "QUIZ · STAGE 2 · ONE STUDENT, ONE SENTENCE",
                 "Each student comes to the table and gives the full iʿrāb of one sentence: every word gets its ending and its job.",
                 [("Come to the table", "Take your card. Read the sentence aloud first."),
                  ("Verb and doer", "Who did it? In an order, the doer is a hidden “you”."),
                  ("Every other word", "What? Why? When or where? How? Then the small boxes."),
                  ("Explain and check", "Say the reason for each ending, then press Check.")])
