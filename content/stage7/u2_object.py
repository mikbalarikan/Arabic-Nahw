# Stage 7, Unit 2: The object (الْمَفْعُولُ بِهِ)

# Canonical options (STAGES_5_8_SPEC.md), copied exactly.
DAM = {"k": "dam", "label": "Damma · ضَمَّةٌ", "color": "red"}
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
KAS = {"k": "kas", "label": "Kasra · كَسْرَةٌ", "color": "green"}
ALIF = {"k": "alif", "label": "Alif · الأَلِفُ", "color": "teal"}
WAW = {"k": "waw", "label": "Wāw · الوَاوُ", "color": "blue"}
YA = {"k": "ya", "label": "Yāʾ · اليَاءُ", "color": "purple"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}

RAF = {"k": "raf", "label": "Rafʿ · رَفْعٌ", "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ", "color": "pink"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ", "color": "green"}

VERB = {"k": "verb", "label": "Verb · فِعْلٌ", "color": "navy"}
DOER = {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"}
OBJ = {"k": "obj", "label": "Object · مَفْعُولٌ بِهِ", "color": "pink"}
PREP = {"k": "prep", "label": "After a preposition · اِسْمٌ مَجْرُورٌ", "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
WHEN = {"k": "when", "label": "Time/place · مَفْعُولٌ فِيهِ", "color": "brown"}
STATE = {"k": "state", "label": "State · حَالٌ", "color": "olive"}

NASB_SIGNS = [FAT, ALIF, YA, KAS, HID]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s7-object",
    "order": 2,
    "title": "The object",
    "ar": "الْمَفْعُولُ بِهِ",
    "blurb": "The object is always in naṣb. Practise its sign with every noun group, verbs with two objects, and pronoun objects.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 7 · UNIT 2", "title": "The one the action falls on",
         "text": "The object ({المَفْعُولُ بِهِ}) is the noun the action is done to. It is always in naṣb. Its group decides the sign.",
         "wm": "المَفْعُولُ بِهِ"},

        {"t": "h2", "text": "What is the object?"},
        {"t": "p", "text": "Ask the verb \"what?\" or \"whom?\". The answer is the object. In {قَرَأَ الطَّالِبُ الكِتَابَ} \"The student read the book\", the student did the reading. The book had the reading done to it."},
        {"t": "rule", "color": "pink", "title": "The object is naṣb",
         "text": "{مَفْعُولٌ بِهِ مَنْصُوبٌ}. Always. Only the sign changes from group to group."},
        {"t": "cols", "items": [
            {"color": "navy", "title": "Verb", "ar": "قَرَأَ", "text": "the action"},
            {"color": "orange", "title": "Doer", "ar": "الطَّالِبُ", "text": "rafʿ"},
            {"color": "pink", "title": "Object", "ar": "الكِتَابَ", "text": "naṣb"},
        ]},

        {"t": "h2", "text": "The object with every group"},
        {"t": "table", "head": ["Group", "Example", "Meaning", "Sign"], "rows": [
            ["Singular", "قَرَأَ الطَّالِبُ الكِتَابَ.", "The student read the book.", "Fatha"],
            ["Broken plural", "زَارَ المُدِيرُ الطُّلَّابَ.", "The headmaster visited the students.", "Fatha"],
            ["Diptote", "شَكَرْتُ زَيْنَبَ.", "I thanked Zaynab.", "Fatha, no tanween"],
            ["Dual", "رَأَيْتُ الوَلَدَيْنِ.", "I saw the two boys.", "Yāʾ"],
            ["Sound m. plural", "رَأَيْتُ المُعَلِّمِينَ.", "I saw the teachers.", "Yāʾ"],
            ["Sound f. plural", "شَكَرْتُ المُعَلِّمَاتِ.", "I thanked the female teachers.", "Kasra in place of fatha"],
            ["Five nouns", "زُرْتُ أَبَاكَ.", "I visited your father.", "Alif"],
            ["Manqūṣ", "رَأَيْتُ القَاضِيَ.", "I saw the judge.", "Fatha (it shows)"],
            ["Maqṣūr", "رَأَيْتُ الفَتَى.", "I saw the young man.", "Hidden fatha"],
            ["Noun + ـي", "قَرَأْتُ كِتَابِي.", "I read my book.", "Hidden fatha"],
        ]},
        {"t": "tip", "text": "An owned dual or sound m. plural drops its {ن}: {رَأَيْتُ مُعَلِّمِي المَدْرَسَةِ} \"I saw the school's teachers\". The yāʾ stays, and it is still the sign."},

        {"t": "h2", "text": "The full iʿrāb"},
        {"t": "examples", "items": [
            {"ar": "رَأَيْتُ المُعَلِّمِينَ.", "en": "I saw the teachers.",
             "note": "{مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
            {"ar": "رَأَيْتُ الوَلَدَيْنِ.", "en": "I saw the two boys.",
             "note": "{مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
            {"ar": "شَكَرْتُ المُعَلِّمَاتِ.", "en": "I thanked the female teachers.",
             "note": "{مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الكَسْرَةُ نِيَابَةً عَنِ الفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ}."},
            {"ar": "زُرْتُ أَبَاكَ.", "en": "I visited your father.",
             "note": "{أَبَا}: {مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الأَلِفُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ}. {ـكَ} is the owner, fixed, in the place of jarr."},
            {"ar": "رَأَيْتُ الفَتَى.", "en": "I saw the young man.",
             "note": "{مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ عَلَى الأَلِفِ}."},
        ]},

        {"t": "h2", "text": "The ending decides the job"},
        {"t": "p", "text": "The object usually comes after the doer. It may also come before it. The ending still tells you who did what."},
        {"t": "examples", "items": [
            {"ar": "زَارَ الطَّبِيبُ المَرِيضَ.", "en": "The doctor visited the patient.", "note": "Doer, then object."},
            {"ar": "زَارَ المَرِيضَ الطَّبِيبُ.", "en": "The doctor visited the patient.", "note": "Same meaning. {المَرِيضَ} has fatha, so it is still the object."},
        ]},
        {"t": "rule", "color": "brown", "title": "When both signs are hidden",
         "text": "In {زَارَ مُوسَى عِيسَى} we see no sign on either noun. Then the order decides: the first is the doer, the second is the object. \"Musa visited ʿIsa.\""},

        {"t": "h2", "text": "A verb with two objects"},
        {"t": "p", "text": "Some verbs take two objects. The first is the person who receives. The second is the thing. Both are in naṣb. Common verbs: {أَعْطَى} \"gave\", {مَنَحَ} \"granted\", {كَسَا} \"clothed\"."},
        {"t": "examples", "items": [
            {"ar": "أَعْطَى المُدَرِّسُ الطَّالِبَ كِتَابًا.", "en": "The teacher gave the student a book.",
             "note": "{الطَّالِبَ}: first object. {كِتَابًا}: second object. Both fatha."},
            {"ar": "أَعْطَتِ الأُمُّ البِنْتَيْنِ تُفَّاحَتَيْنِ.", "en": "The mother gave the two girls two apples.",
             "note": "Two duals, both objects: {مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
            {"ar": "مَنَحَ المُدِيرُ المُعَلِّمَاتِ جَوَائِزَ.", "en": "The headmaster gave the female teachers prizes.",
             "note": "{المُعَلِّمَاتِ}: kasra in place of fatha. {جَوَائِزَ}: a diptote, fatha with no tanween."},
        ]},

        {"t": "h2", "text": "A pronoun as the object"},
        {"t": "p", "text": "An attached pronoun on a verb can be the object. It is fixed, so we say it is in the place of naṣb: {فِي مَحَلِّ نَصْبٍ}."},
        {"t": "table", "head": ["Sentence", "Meaning", "The object"], "rows": [
            ["رَأَيْتُهُ.", "I saw him.", "{ـهُ}, in the place of naṣb"],
            ["شَكَرَكَ المُعَلِّمُ.", "The teacher thanked you.", "{ـكَ}, in the place of naṣb"],
            ["زَارَهُمْ أَبُوكَ.", "Your father visited them.", "{ـهُمْ}, in the place of naṣb"],
            ["اُكْتُبْهُ.", "Write it.", "{ـهُ}, in the place of naṣb"],
        ]},
        {"t": "p", "text": "In {رَأَيْتُهُ} there are two pronouns. {تُ} is the doer (place of rafʿ). {ـهُ} is the object (place of naṣb)."},
        {"t": "tip", "text": "Watch {نَا}. With sukūn before it, it is the doer: {شَكَرْنَا المُعَلِّمَ} \"We thanked the teacher\". With fatha before it, it is the object: {شَكَرَنَا المُعَلِّمُ} \"The teacher thanked us\"."},
        {"t": "tip", "text": "A noun after a preposition is not an object. In {ذَهَبْتُ إِلَى السُّوقِ}، {السُّوقِ} is jarr after {إِلَى}."},

        {"t": "summary", "title": "In short", "items": [
            "The object answers \"what?\" or \"whom?\". It is always naṣb.",
            "Fatha: singular, broken plural, diptote, manqūṣ. Yāʾ: dual and sound m. plural. Kasra: sound f. plural. Alif: five nouns. Hidden fatha: maqṣūr and noun + ـي.",
            "The ending shows the object, even when it comes before the doer. If both signs are hidden, the first noun is the doer.",
            "{أَعْطَى}، {مَنَحَ}، {كَسَا} take two objects, both naṣb.",
            "An attached pronoun object is fixed, in the place of naṣb: {رَأَيْتُهُ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Job and sign",
            "prompt": "زَارَ المُهَنْدِسُونَ أَبَاكَ فِي المُسْتَشْفَى.",
            "en": "The engineers visited your father in the hospital.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, OWNER, PREP]},
                {"key": "sign", "label": "Sign", "options": [FAT, WAW, ALIF, YA, HID, FIXED]},
            ],
            "rows": [
                {"s": "زَارَ", "gloss": "visited", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb. It is fixed on fatha."},
                {"s": "المُهَنْدِسُونَ", "gloss": "the engineers", "ans": {"job": "doer", "sign": "waw"},
                 "why": "Doer, rafʿ. Sound m. plural: wāw."},
                {"s": "أَبَا", "gloss": "father, in أَبَاكَ", "ans": {"job": "obj", "sign": "alif"},
                 "why": "Object, naṣb. Five noun: alif."},
                {"s": "ـكَ", "gloss": "your", "ans": {"job": "owner", "sign": "fixed"},
                 "why": "Owner. A fixed pronoun in the place of jarr."},
                {"s": "المُسْتَشْفَى", "gloss": "the hospital", "ans": {"job": "prep", "sign": "hid"},
                 "why": "After {فِي}, jarr. A maqṣūr: hidden kasra."},
            ],
        },
        {
            "title": "The object's sign",
            "fields": [{"key": "sign", "label": "Sign", "options": NASB_SIGNS}],
            "rows": [
                {"s": "رَأَيْتُ [المُسَافِرِينَ]", "gloss": "I saw the travellers.", "ans": {"sign": "ya"},
                 "why": "Sound m. plural, kasra before the ي: yāʾ."},
                {"s": "سَاعَدْنَا [الجَارَتَيْنِ]", "gloss": "We helped the two (female) neighbours.", "ans": {"sign": "ya"},
                 "why": "Dual, fatha before the ي: yāʾ."},
                {"s": "رَأَيْتُ [الفَتَى]", "gloss": "I saw the young man.", "ans": {"sign": "hid"},
                 "why": "Maqṣūr: hidden fatha on the alif."},
                {"s": "زُرْتُ [القَاضِيَ]", "gloss": "I visited the judge.", "ans": {"sign": "fat"},
                 "why": "Manqūṣ: in naṣb the fatha shows."},
                {"s": "شَكَرْتُ [المُدَرِّسَاتِ]", "gloss": "I thanked the female teachers.", "ans": {"sign": "kas"},
                 "why": "Sound f. plural: kasra in place of fatha."},
                {"s": "قَابَلْتُ [أَخَاكَ]", "gloss": "I met your brother.", "ans": {"sign": "alif"},
                 "why": "Five noun: alif."},
            ],
        },
        {
            "title": "Choose the object",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "شَكَرَ المُدِيرُ ___", "gloss": "the engineers (three or more men)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُهَنْدِسُونَ", "المُهَنْدِسِينَ", "المُهَنْدِسَيْنِ")},
                 "why": "Object: {ـِينَ}. {ـُونَ} is rafʿ. {ـَيْنِ} means two."},
                {"s": "رَأَيْتُ ___", "gloss": "two girls", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بِنْتَيْنِ", "بِنْتَانِ", "بَنَاتٍ")},
                 "why": "Dual object: {بِنْتَيْنِ}. {بِنْتَانِ} is rafʿ. {بَنَاتٍ} is three or more."},
                {"s": "زَارَ الطَّبِيبُ ___", "gloss": "your brother", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَخُوكَ", "أَخِيكَ", "أَخَاكَ")},
                 "why": "Five noun in naṣb: alif, {أَخَاكَ}."},
                {"s": "رَأَيْتُ ___", "gloss": "female students (no the)", "ans": {"pick": "c"},
                 "opts": {"pick": pick("طَالِبَاتٌ", "طَالِبَاتًا", "طَالِبَاتٍ")},
                 "why": "Sound f. plural in naṣb: kasra with tanween."},
                {"s": "سَأَلْتُ ___", "gloss": "the lawyer", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُحَامِي", "المُحَامِيَ", "المُحَامِيُ")},
                 "why": "Manqūṣ in naṣb: the fatha shows, {المُحَامِيَ}."},
                {"s": "رَأَيْتُ ___", "gloss": "Ahmad", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَحْمَدَ", "أَحْمَدًا", "أَحْمَدُ")},
                 "why": "Diptote: fatha, no tanween."},
            ],
        },
        {
            "title": "Two objects",
            "prompt": "أَعْطَتِ المُعَلِّمَةُ الطَّالِبَاتِ جَوَائِزَ.",
            "en": "The (female) teacher gave the female students prizes.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, OWNER]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, YA, FIXED]},
            ],
            "rows": [
                {"s": "أَعْطَتِ", "gloss": "gave", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed. The {ت} shows the doer is feminine."},
                {"s": "المُعَلِّمَةُ", "gloss": "the teacher (f.)", "ans": {"job": "doer", "sign": "dam"},
                 "why": "Doer, rafʿ. Singular: damma."},
                {"s": "الطَّالِبَاتِ", "gloss": "the female students", "ans": {"job": "obj", "sign": "kas"},
                 "why": "First object, naṣb. Sound f. plural: kasra in place of fatha."},
                {"s": "جَوَائِزَ", "gloss": "prizes", "ans": {"job": "obj", "sign": "fat"},
                 "why": "Second object, naṣb. A diptote: fatha with no tanween."},
            ],
        },
        {
            "title": "Which job is the attached pronoun?",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, OBJ, OWNER]},
                {"key": "case", "label": "Place of", "options": [RAF, NASB, JARR]},
            ],
            "rows": [
                {"s": "رَأَيْتُهُ", "gloss": "I saw him. Which: تُ", "ans": {"job": "doer", "case": "raf"},
                 "why": "{تُ} \"I\" did the seeing. Doer, in the place of rafʿ."},
                {"s": "رَأَيْتُهُ", "gloss": "I saw him. Which: ـهُ", "ans": {"job": "obj", "case": "nasb"},
                 "why": "{ـهُ} \"him\" was seen. Object, in the place of naṣb."},
                {"s": "كِتَابُكَ جَدِيدٌ", "gloss": "Your book is new. Which: ـكَ", "ans": {"job": "owner", "case": "jarr"},
                 "why": "On a noun, the pronoun is the owner, in the place of jarr."},
                {"s": "شَكَرَنَا المُعَلِّمُ", "gloss": "The teacher thanked us. Which: نَا", "ans": {"job": "obj", "case": "nasb"},
                 "why": "Fatha before {نَا}, and {المُعَلِّمُ} is the doer. So {نَا} is the object."},
                {"s": "شَكَرْنَا المُعَلِّمَ", "gloss": "We thanked the teacher. Which: نَا", "ans": {"job": "doer", "case": "raf"},
                 "why": "Sukūn before {نَا}: it is the doer. {المُعَلِّمَ} is the object."},
                {"s": "زَارَهُمْ أَبُوكَ", "gloss": "Your father visited them. Which: ـهُمْ", "ans": {"job": "obj", "case": "nasb"},
                 "why": "{أَبُوكَ} is the doer. {ـهُمْ} is the object, in the place of naṣb."},
            ],
        },
        {
            "title": "Object or not?",
            "fields": [{"key": "job", "label": "Job", "options": [DOER, OBJ, PREP]}],
            "rows": [
                {"s": "ذَهَبْتُ إِلَى [السُّوقِ]", "gloss": "I went to the market.", "ans": {"job": "prep"},
                 "why": "After {إِلَى}: jarr. Not an object."},
                {"s": "اِشْتَرَيْتُ [خُبْزًا]", "gloss": "I bought bread.", "ans": {"job": "obj"},
                 "why": "What did I buy? Bread. Object, fatha."},
                {"s": "جَاءَ [المُعَلِّمُونَ]", "gloss": "The teachers came.", "ans": {"job": "doer"},
                 "why": "They did the coming. Doer, wāw."},
                {"s": "زَارَ [المَرِيضَ] الطَّبِيبُ", "gloss": "The doctor visited the patient.", "ans": {"job": "obj"},
                 "why": "It comes first, but it has fatha. {الطَّبِيبُ} with damma is the doer."},
                {"s": "زَارَ مُوسَى [عِيسَى]", "gloss": "Musa visited ʿIsa.", "ans": {"job": "obj"},
                 "why": "Both signs are hidden, so the order decides. The second noun is the object."},
                {"s": "فَتَحَ [البَابَ] الوَلَدُ", "gloss": "The boy opened the door.", "ans": {"job": "obj"},
                 "why": "Fatha on {البَابَ}: the object. {الوَلَدُ} is the doer."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Job and sign",
            "prompt": "أَعْطَى المُحَامِي أَخَاكَ مِفْتَاحَيْنِ.",
            "en": "The lawyer gave your brother two keys.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, OBJ, OWNER, ADJ]},
                {"key": "sign", "label": "Sign", "options": [FAT, ALIF, YA, HID, FIXED]},
            ],
            "rows": [
                {"s": "المُحَامِي", "gloss": "the lawyer", "ans": {"job": "doer", "sign": "hid"},
                 "why": "Doer, rafʿ. A manqūṣ: hidden damma on the ي."},
                {"s": "أَخَا", "gloss": "brother, in أَخَاكَ", "ans": {"job": "obj", "sign": "alif"},
                 "why": "First object, naṣb. Five noun: alif."},
                {"s": "ـكَ", "gloss": "your", "ans": {"job": "owner", "sign": "fixed"},
                 "why": "Owner, a fixed pronoun in the place of jarr."},
                {"s": "مِفْتَاحَيْنِ", "gloss": "two keys", "ans": {"job": "obj", "sign": "ya"},
                 "why": "Second object, naṣb. Dual: yāʾ."},
            ],
        },
        {
            "title": "The object's sign",
            "fields": [{"key": "sign", "label": "Sign", "options": NASB_SIGNS}],
            "rows": [
                {"s": "كَسَا الأَبُ [ابْنَهُ] ثَوْبًا", "gloss": "The father dressed his son in a robe.", "ans": {"sign": "fat"},
                 "why": "First object. A singular with an owner pronoun: fatha, {ابْنَهُ}."},
                {"s": "حَمَلْتُ [حَقِيبَتَيْكَ]", "gloss": "I carried your two bags.", "ans": {"sign": "ya"},
                 "why": "A dual with an owner: the {ن} drops, the yāʾ stays as the sign."},
                {"s": "شَكَرَ المُدِيرُ [مُعَلِّمِي] المَدْرَسَةِ", "gloss": "The headmaster thanked the school's teachers.", "ans": {"sign": "ya"},
                 "why": "A sound m. plural with an owner: {ن} drops, sign yāʾ."},
                {"s": "رَأَيْتُ [مُصْطَفَى]", "gloss": "I saw Mustafa.", "ans": {"sign": "hid"},
                 "why": "Ends in alif: maqṣūr. Hidden fatha."},
                {"s": "سَأَلْتُ [أَخَا] فَاطِمَةَ", "gloss": "I asked Fatima's brother.", "ans": {"sign": "alif"},
                 "why": "Five noun with an owner: alif."},
                {"s": "حَفِظْتُ [أَبْيَاتًا] مِنَ الشِّعْرِ", "gloss": "I learned some lines of poetry by heart.", "ans": {"sign": "fat"},
                 "why": "{أَبْيَاتٌ} is the broken plural of {بَيْتٌ}. The {ت} is part of the root: fatha."},
            ],
        },
        {
            "title": "Choose the object",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "أَكْرَمَ الأَبُ ___", "gloss": "his two sons", "ans": {"pick": "b"},
                 "opts": {"pick": pick("ابْنَاهُ", "ابْنَيْهِ", "ابْنَيْنِهِ")},
                 "why": "Dual in naṣb with an owner: {ن} drops, {ابْنَيْهِ}. {ابْنَاهُ} is rafʿ."},
                {"s": "شَكَرْتُ ___", "gloss": "Fatima", "ans": {"pick": "c"},
                 "opts": {"pick": pick("فَاطِمَةً", "فَاطِمَةِ", "فَاطِمَةَ")},
                 "why": "A diptote: fatha, no tanween."},
                {"s": "رَأَيْتُ ___", "gloss": "a judge", "ans": {"pick": "a"},
                 "opts": {"pick": pick("قَاضِيًا", "قَاضٍ", "قَاضِيٍ")},
                 "why": "Manqūṣ in naṣb: the fatha shows with tanween, {قَاضِيًا}."},
                {"s": "سَاعَدْتُ ___", "gloss": "the Muslim women", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُسْلِمَاتَ", "المُسْلِمَاتِ", "المُسْلِمَاتُ")},
                 "why": "Sound f. plural in naṣb: kasra."},
                {"s": "زُرْنَا ___ المَدِينَةِ", "gloss": "the city's engineers (m.)", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُهَنْدِسُو", "مُهَنْدِسِينَ", "مُهَنْدِسِي")},
                 "why": "Naṣb with yāʾ, and the {ن} drops before the owner: {مُهَنْدِسِي}."},
                {"s": "رَأَيْتُ ___", "gloss": "Zayd's father", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَبُو زَيْدٍ", "أَبَا زَيْدٍ", "أَبِي زَيْدٍ")},
                 "why": "Five noun in naṣb: alif, {أَبَا زَيْدٍ}."},
            ],
        },
        {
            "title": "Two objects",
            "prompt": "كَسَتِ الأُمُّ البِنْتَيْنِ ثَوْبَيْنِ جَدِيدَيْنِ.",
            "en": "The mother dressed the two girls in two new dresses.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, OBJ, ADJ, OWNER]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, ALIF, YA]},
            ],
            "rows": [
                {"s": "الأُمُّ", "gloss": "the mother", "ans": {"job": "doer", "sign": "dam"},
                 "why": "Doer, rafʿ. Singular: damma."},
                {"s": "البِنْتَيْنِ", "gloss": "the two girls", "ans": {"job": "obj", "sign": "ya"},
                 "why": "First object (who received). Dual: yāʾ."},
                {"s": "ثَوْبَيْنِ", "gloss": "two dresses", "ans": {"job": "obj", "sign": "ya"},
                 "why": "Second object (the thing). Dual: yāʾ."},
                {"s": "جَدِيدَيْنِ", "gloss": "new", "ans": {"job": "adj", "sign": "ya"},
                 "why": "Adjective of {ثَوْبَيْنِ}. It copies its naṣb, and it is a dual too: yāʾ."},
            ],
        },
        {
            "title": "Which job is the attached pronoun?",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, OBJ, OWNER]},
                {"key": "case", "label": "Place of", "options": [RAF, NASB, JARR]},
            ],
            "rows": [
                {"s": "أَعْطَيْتُهُ كِتَابًا", "gloss": "I gave him a book. Which: ـهُ", "ans": {"job": "obj", "case": "nasb"},
                 "why": "{ـهُ} received the book: the first object, in the place of naṣb."},
                {"s": "أَعْطَيْتُهُ كِتَابًا", "gloss": "I gave him a book. Which: تُ", "ans": {"job": "doer", "case": "raf"},
                 "why": "{تُ} \"I\" did the giving: doer, in the place of rafʿ."},
                {"s": "شَكَرَكَ المُدِيرُ", "gloss": "The headmaster thanked you. Which: ـكَ", "ans": {"job": "obj", "case": "nasb"},
                 "why": "On a verb, with {المُدِيرُ} as the doer: object."},
                {"s": "زُرْتُ بَيْتَهَا", "gloss": "I visited her house. Which: ـهَا", "ans": {"job": "owner", "case": "jarr"},
                 "why": "{بَيْتَ} is the object. {ـهَا} is on a noun: its owner, in the place of jarr."},
                {"s": "أَكْرَمَنَا الجَارُ", "gloss": "The neighbour honoured us. Which: نَا", "ans": {"job": "obj", "case": "nasb"},
                 "why": "Fatha before {نَا}, and {الجَارُ} is the doer: {نَا} is the object."},
                {"s": "زَارُوا المَرِيضَ", "gloss": "They visited the patient. Which: و", "ans": {"job": "doer", "case": "raf"},
                 "why": "The {و} \"they\" is the doer. {المَرِيضَ} is the object."},
            ],
        },
        {
            "title": "Object or another job?",
            "fields": [{"key": "job", "label": "Job", "options": [DOER, OBJ, WHEN, STATE]}],
            "rows": [
                {"s": "سَافَرَ أَبِي [يَوْمًا]", "gloss": "My father travelled for a day.", "ans": {"job": "when"},
                 "why": "It answers \"for how long?\". It does not answer \"what?\". Time, naṣb."},
                {"s": "جَاءَ الوَلَدُ [مُسْرِعًا]", "gloss": "The boy came hurrying.", "ans": {"job": "state"},
                 "why": "It answers \"how did he come?\". State, naṣb."},
                {"s": "أَكَلَ [الطَّعَامَ] الضَّيْفُ", "gloss": "The guest ate the food.", "ans": {"job": "obj"},
                 "why": "What did he eat? Fatha on {الطَّعَامَ}: object, before the doer."},
                {"s": "كَتَبَ [الطَّالِبَانِ] الدَّرْسَ", "gloss": "The two students wrote the lesson.", "ans": {"job": "doer"},
                 "why": "Alif of the dual in rafʿ. They did the writing."},
                {"s": "أَعْطَى الأَبُ ابْنَهُ [قَلَمًا]", "gloss": "The father gave his son a pen.", "ans": {"job": "obj"},
                 "why": "The thing given: the second object of {أَعْطَى}."},
                {"s": "رَأَى مُوسَى [الفَتَى]", "gloss": "Musa saw the young man.", "ans": {"job": "obj"},
                 "why": "Both signs hidden. The order decides: the second noun is the object."},
            ],
        },
    ],
}
