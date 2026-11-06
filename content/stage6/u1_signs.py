# Stage 6, Unit 1: The signs of jarr (عَلَامَاتُ الجَرِّ)

KAS = {"k": "kas", "label": "Kasra · كَسْرَةٌ", "color": "green"}
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
DAM = {"k": "dam", "label": "Damma · ضَمَّةٌ", "color": "red"}
ALIF = {"k": "alif", "label": "Alif · الأَلِفُ", "color": "teal"}
WAW = {"k": "waw", "label": "Wāw · الوَاوُ", "color": "blue"}
YA = {"k": "ya", "label": "Yāʾ · اليَاءُ", "color": "purple"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}
JSIGNS = [KAS, YA, FAT, HID]

RAF = {"k": "raf", "label": "Rafʿ · رَفْعٌ", "color": "red"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ", "color": "green"}

PREP = {"k": "prep", "label": "After a preposition · اِسْمٌ مَجْرُورٌ", "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
AND = {"k": "and", "label": "After وَ (and) · مَعْطُوفٌ", "color": "blue"}
JOBS = [PREP, OWNER, ADJ, AND]

SING = {"k": "sing", "label": "Singular · مُفْرَدٌ", "color": "grey"}
DUAL = {"k": "dual", "label": "Dual · مُثَنًّى", "color": "teal"}
SMP = {"k": "smp", "label": "Sound m. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ", "color": "blue"}
DIP = {"k": "dip", "label": "Diptote · مَمْنُوعٌ مِنَ الصَّرْفِ", "color": "orange"}
FIVE = {"k": "five", "label": "Five nouns · الأَسْمَاءُ الخَمْسَةُ", "color": "gold"}
HIDV = {"k": "hidv", "label": "Hidden vowel", "color": "brown"}
KINDS = [SING, DUAL, SMP, DIP, FIVE, HIDV]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abc", labels)]


UNIT = {
    "id": "s6-signs",
    "order": 1,
    "title": "The signs of jarr",
    "ar": "عَلَامَاتُ الجَرِّ",
    "blurb": "Three jobs put a noun in jarr. Four signs show it: kasra, yāʾ, fatha for diptotes, and a hidden kasra.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 6 · UNIT 1", "title": "Three jobs, four signs",
         "text": "A noun in jarr has one of three jobs. It shows jarr with one of four signs. This stage drills them all.",
         "wm": "الجَرُّ"},

        {"t": "h2", "text": "Three jobs that give jarr"},
        {"t": "p", "text": "In Stage 5 you met the jobs of rafʿ. Jarr has only three jobs."},
        {"t": "cols", "items": [
            {"color": "green", "title": "After a preposition", "ar": "اِسْمٌ مَجْرُورٌ", "text": "{فِي البَيْتِ} in the house"},
            {"color": "purple", "title": "Owner", "ar": "مُضَافٌ إِلَيْهِ", "text": "{كِتَابُ الطَّالِبِ} the student's book"},
            {"color": "grey", "title": "Follower", "ar": "تَابِعٌ", "text": "{فِي بَيْتٍ كَبِيرٍ} in a big house"},
        ]},
        {"t": "p", "text": "A follower copies a jarr noun before it. It is an adjective, a word after {وَ}, an emphasis word or a substitute. Unit 5 drills them."},
        {"t": "rule", "color": "teal", "title": "Job → case → sign",
         "text": "Find the job. The job gives the case. The kind of noun gives the sign."},

        {"t": "h2", "text": "The four signs of jarr"},
        {"t": "cols", "items": [
            {"color": "green", "title": "Kasra", "ar": "كَسْرَةٌ", "text": "The original sign. {فِي البَيْتِ}"},
            {"color": "purple", "title": "Yāʾ", "ar": "اليَاءُ", "text": "A letter sign. {عَلَى المُسْلِمِينَ}"},
            {"color": "pink", "title": "Fatha", "ar": "فَتْحَةٌ", "text": "For a diptote. {بِأَحْمَدَ}"},
            {"color": "brown", "title": "Hidden kasra", "ar": "مُقَدَّرَةٌ", "text": "Original, but hidden. {إِلَى المُسْتَشْفَى}"},
        ]},
        {"t": "table", "head": ["Kind of noun", "Jarr shape", "Sign"], "rows": [
            ["Singular", "فِي البَيْتِ", "Kasra"],
            ["Broken plural", "فِي البُيُوتِ", "Kasra"],
            ["Sound f. plural", "إِلَى المُدَرِّسَاتِ", "Kasra"],
            ["Dual", "بِالقَلَمَيْنِ", "Yāʾ"],
            ["Sound m. plural", "عَلَى المُسْلِمِينَ", "Yāʾ"],
            ["Five nouns (owned)", "إِلَى أَبِيكَ", "Yāʾ"],
            ["Diptote (no {ال}, not owned)", "فِي مَسَاجِدَ", "Fatha"],
            ["Maqṣūr", "إِلَى المُسْتَشْفَى", "Hidden kasra"],
            ["Manqūṣ", "فِي النَّادِي", "Hidden kasra"],
            ["Noun + {ـي} \"my\"", "فِي بَيْتِي", "Hidden kasra"],
        ]},
        {"t": "tip", "text": "A diptote takes kasra again when it has {ال} or an owner: {فِي المَسَاجِدِ}، {فِي مَسَاجِدِ المَدِينَةِ}. Unit 4 drills this."},

        {"t": "h2", "text": "From rafʿ to jarr"},
        {"t": "p", "text": "You know the rafʿ shapes from Stage 5. Here is what changes in jarr."},
        {"t": "table", "head": ["Kind of noun", "Rafʿ", "Jarr", "What changes"], "rows": [
            ["Singular", "البَيْتُ", "البَيْتِ", "damma → kasra"],
            ["Broken plural", "البُيُوتُ", "البُيُوتِ", "damma → kasra"],
            ["Sound f. plural", "المُسْلِمَاتُ", "المُسْلِمَاتِ", "damma → kasra"],
            ["Dual", "المُسْلِمَانِ", "المُسْلِمَيْنِ", "alif → yāʾ"],
            ["Sound m. plural", "المُسْلِمُونَ", "المُسْلِمِينَ", "wāw → yāʾ"],
            ["Five nouns", "أَبُوكَ", "أَبِيكَ", "wāw → yāʾ"],
            ["Diptote", "مَسَاجِدُ", "مَسَاجِدَ", "damma → fatha"],
            ["Maqṣūr", "الفَتَى", "الفَتَى", "nothing you can see"],
            ["Manqūṣ", "القَاضِي", "القَاضِي", "nothing you can see"],
        ]},
        {"t": "tip", "text": "Dual and plural both use {ي} in jarr. Look at the vowel before it. Dual: fatha, {ـَيْنِ}. Sound m. plural: kasra, {ـِينَ}."},
        {"t": "tip", "text": "The vowel on the {ن} of the dual and the plural never changes. It is not a sign."},

        {"t": "h2", "text": "Worked examples: the full iʿrāb"},
        {"t": "p", "text": "Say the job, then the case, then the sign. Add the reason when the sign is a branch sign."},
        {"t": "examples", "items": [
            {"ar": "ذَهَبْتُ إِلَى المَسْجِدِ.", "en": "I went to the mosque.",
             "note": "{المَسْجِدِ}: اِسْمٌ مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الكَسْرَةُ. After a preposition, jarr, kasra."},
            {"ar": "سَلَّمْتُ عَلَى المُعَلِّمِينَ.", "en": "I greeted the teachers.",
             "note": "{المُعَلِّمِينَ}: اِسْمٌ مَجْرُورٌ بِعَلَى وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ."},
            {"ar": "هَذَا كِتَابُ أَحْمَدَ.", "en": "This is Ahmad's book.",
             "note": "{أَحْمَدَ}: مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الفَتْحَةُ نِيَابَةً عَنِ الكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ."},
            {"ar": "نَظَرْتُ إِلَى كِتَابِ الطَّالِبَيْنِ.", "en": "I looked at the book of the two students.",
             "note": "{الطَّالِبَيْنِ}: مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ مُثَنًّى."},
            {"ar": "ذَهَبَ الطَّبِيبُ إِلَى المُسْتَشْفَى.", "en": "The doctor went to the hospital.",
             "note": "{المُسْتَشْفَى}: اِسْمٌ مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ الكَسْرَةُ المُقَدَّرَةُ عَلَى الأَلِفِ."},
            {"ar": "جَلَسْتُ فِي بَيْتٍ كَبِيرٍ.", "en": "I sat in a big house.",
             "note": "{كَبِيرٍ}: نَعْتٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ. It copies {بَيْتٍ}."},
        ]},

        {"t": "h2", "text": "The hidden kasra"},
        {"t": "p", "text": "Three kinds of noun hide the kasra. The case is jarr. The sign is still kasra, only we cannot see it."},
        {"t": "table", "head": ["Kind", "Example", "Why it is hidden"], "rows": [
            ["Maqṣūr", "إِلَى المُسْتَشْفَى", "An alif cannot carry a vowel."],
            ["Manqūṣ", "فِي النَّادِي", "Kasra is too heavy on this {ي}."],
            ["Manqūṣ, no {ال}", "سَلَّمْتُ عَلَى قَاضٍ", "The {ي} drops. Its kasra is hidden."],
            ["Noun + {ـي} \"my\"", "فِي بَيْتِي", "The letter before {ـي} must have kasra for the {ي}."],
        ]},
        {"t": "tip", "text": "In {قَاضٍ} the tanween is not the sign. A {ي} was dropped there. Say: {مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ المُقَدَّرَةُ عَلَى اليَاءِ المَحْذُوفَةِ}."},
        {"t": "tip", "text": "In {فِي بَيْتِي} you see a kasra on the {ت}. It is there because of the {ي}. The real sign of jarr is hidden under it."},
        {"t": "p", "text": "A fixed word in a jarr job does not change. It is in the place of jarr (Stage 3): {عَلَيْهِ}، {كِتَابُهُ}."},

        {"t": "summary", "title": "In short", "items": [
            "Three jarr jobs: after a preposition, owner, follower.",
            "Kasra: singular, broken plural, sound f. plural.",
            "Yāʾ: dual {ـَيْنِ}، sound m. plural {ـِينَ}، five nouns {أَبِيكَ}.",
            "Fatha: a diptote with no {ال} and no owner: {بِأَحْمَدَ}.",
            "Hidden kasra: maqṣūr, manqūṣ, and a noun with {ـي} \"my\".",
            "Say it in full: {اِسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Which sign of jarr?",
            "fields": [{"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "فِي [البَيْتِ]", "gloss": "in the house", "ans": {"sign": "kas"},
                 "why": "A singular noun: {اِسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}."},
                {"s": "عَلَى [المُسْلِمِينَ]", "gloss": "on the Muslims", "ans": {"sign": "ya"},
                 "why": "A sound m. plural: {ـِينَ}. The sign is the {ي}."},
                {"s": "إِلَى [المُسْتَشْفَى]", "gloss": "to the hospital", "ans": {"sign": "hid"},
                 "why": "Maqṣūr. The alif cannot carry the kasra: hidden kasra."},
                {"s": "مِنَ [المَدِينَتَيْنِ]", "gloss": "from the two cities", "ans": {"sign": "ya"},
                 "why": "A dual: {ـَيْنِ}. The sign is the {ي}."},
                {"s": "سَلَّمْتُ عَلَى [أَحْمَدَ]", "gloss": "I greeted Ahmad", "ans": {"sign": "fat"},
                 "why": "{أَحْمَدُ} is a diptote with no {ال}: fatha in place of kasra."},
                {"s": "إِلَى [المُدَرِّسَاتِ]", "gloss": "to the female teachers", "ans": {"sign": "kas"},
                 "why": "A sound f. plural takes kasra in jarr: {ـَاتِ}."},
            ],
        },
        {
            "title": "Find the jarr job and the sign",
            "prompt": "سَلَّمْتُ عَلَى مُدَرِّسِ المَدْرَسَةِ وَالطُّلَّابِ المُجْتَهِدِينَ.",
            "en": "I greeted the school's teacher and the hard-working students.",
            "fields": [{"key": "job", "label": "Job", "options": JOBS},
                       {"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "مُدَرِّسِ", "gloss": "teacher", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {عَلَى}. A singular: {اِسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}."},
                {"s": "المَدْرَسَةِ", "gloss": "the school", "ans": {"job": "owner", "sign": "kas"},
                 "why": "It owns {مُدَرِّسِ}: {مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}."},
                {"s": "الطُّلَّابِ", "gloss": "the students", "ans": {"job": "and", "sign": "kas"},
                 "why": "After {وَ}, it copies jarr. A broken plural takes kasra."},
                {"s": "المُجْتَهِدِينَ", "gloss": "the hard-working", "ans": {"job": "adj", "sign": "ya"},
                 "why": "It describes {الطُّلَّابِ}. A sound m. plural: {نَعْتٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ}."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "ذَهَبْتُ إِلَى ___", "gloss": "to the two teachers", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُدَرِّسَانِ", "المُدَرِّسَيْنِ", "المُدَرِّسِينَ")},
                 "why": "A dual in jarr: {ـَيْنِ}. {المُدَرِّسِينَ} is a plural."},
                {"s": "سَلَّمْتُ عَلَى ___", "gloss": "the engineers", "ans": {"pick": "a"},
                 "opts": {"pick": pick("المُهَنْدِسِينَ", "المُهَنْدِسُونَ", "المُهَنْدِسَيْنِ")},
                 "why": "A sound m. plural in jarr: {ـِينَ}. {ـُونَ} is rafʿ."},
                {"s": "هَذَا بَيْتُ ___", "gloss": "your father", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَبُوكَ", "أَبَاكَ", "أَبِيكَ")},
                 "why": "The owner is in jarr. A five noun takes {ي}: {أَبِيكَ}."},
                {"s": "صَلَّيْتُ فِي ___ كَثِيرَةٍ", "gloss": "in many mosques", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَسَاجِدَ", "مَسَاجِدٍ", "مَسَاجِدُ")},
                 "why": "A diptote with no {ال} and no owner: fatha, no tanween."},
                {"s": "ذَهَبْتُ إِلَى ___", "gloss": "the female students", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الطَّالِبَاتُ", "الطَّالِبَاتِ", "الطَّالِبَاتَ")},
                 "why": "A sound f. plural in jarr: kasra, {ـَاتِ}."},
            ],
        },
        {
            "title": "Review: rafʿ or jarr?",
            "fields": [{"key": "case", "label": "Case", "options": [RAF, JARR]},
                       {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, KAS, YA, FAT]}],
            "rows": [
                {"s": "[المُعَلِّمُونَ] فِي الفَصْلِ.", "gloss": "The teachers are in the classroom.",
                 "ans": {"case": "raf", "sign": "waw"},
                 "why": "Topic, rafʿ. A sound m. plural shows rafʿ with {و}."},
                {"s": "سَلَّمْتُ عَلَى [المُعَلِّمِينَ].", "gloss": "I greeted the teachers.",
                 "ans": {"case": "jarr", "sign": "ya"},
                 "why": "After {عَلَى}, jarr. A sound m. plural shows jarr with {ي}."},
                {"s": "[الطَّالِبَانِ] فِي المَكْتَبَةِ.", "gloss": "The two students are in the library.",
                 "ans": {"case": "raf", "sign": "alif"},
                 "why": "Topic, rafʿ. A dual shows rafʿ with alif."},
                {"s": "ذَهَبْتُ إِلَى [أَبِيكَ].", "gloss": "I went to your father.",
                 "ans": {"case": "jarr", "sign": "ya"},
                 "why": "After {إِلَى}, jarr. A five noun shows jarr with {ي}."},
                {"s": "هَذِهِ [مَسَاجِدُ].", "gloss": "These are mosques.",
                 "ans": {"case": "raf", "sign": "dam"},
                 "why": "Information, rafʿ. A diptote takes one damma, no tanween."},
                {"s": "صَلَّيْتُ فِي [مَسَاجِدَ] كَثِيرَةٍ.", "gloss": "I prayed in many mosques.",
                 "ans": {"case": "jarr", "sign": "fat"},
                 "why": "After {فِي}, jarr. A diptote with no {ال} and no owner: fatha."},
            ],
        },
        {
            "title": "Find the jarr job and the sign",
            "prompt": "قَرَأْتُ كِتَابَ أَخِي وَصَدِيقِهِ فِي غُرْفَةٍ صَغِيرَةٍ.",
            "en": "I read the book of my brother and his friend in a small room.",
            "fields": [{"key": "job", "label": "Job", "options": JOBS},
                       {"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "أَخِي", "gloss": "my brother", "ans": {"job": "owner", "sign": "hid"},
                 "why": "It owns {كِتَابَ}. With {ـي} \"my\" the kasra is hidden."},
                {"s": "صَدِيقِهِ", "gloss": "his friend", "ans": {"job": "and", "sign": "kas"},
                 "why": "After {وَ}, it copies {أَخِي} in jarr. A singular: kasra."},
                {"s": "غُرْفَةٍ", "gloss": "a room", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {فِي}: {اِسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}."},
                {"s": "صَغِيرَةٍ", "gloss": "small", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {غُرْفَةٍ}: {نَعْتٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}."},
            ],
        },
        {
            "title": "Which kind of noun? Which sign?",
            "fields": [{"key": "kind", "label": "Kind", "options": KINDS},
                       {"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "سَلَّمْتُ عَلَى [القَاضِي]", "gloss": "I greeted the judge", "ans": {"kind": "hidv", "sign": "hid"},
                 "why": "Manqūṣ: it ends in {ي} after kasra. The kasra is hidden."},
                {"s": "مِنَ [الطَّالِبَتَيْنِ]", "gloss": "from the two female students", "ans": {"kind": "dual", "sign": "ya"},
                 "why": "Fatha before {ي}: {ـَيْنِ}. A dual: {مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
                {"s": "جَاءَتْ رِسَالَةٌ مِنْ [أَصْدِقَاءَ]", "gloss": "A letter came from friends", "ans": {"kind": "dip", "sign": "fat"},
                 "why": "{أَصْدِقَاءُ} is a diptote. No {ال}, no owner: fatha in place of kasra."},
                {"s": "عَلَى [الكُرْسِيِّ]", "gloss": "on the chair", "ans": {"kind": "sing", "sign": "kas"},
                 "why": "The {ي} has shadda, so it carries the kasra. A normal singular."},
                {"s": "إِلَى [أَخِيكَ]", "gloss": "to your brother", "ans": {"kind": "five", "sign": "ya"},
                 "why": "A five noun with an owner: {ي} in jarr."},
                {"s": "عَنِ [المُسْلِمِينَ]", "gloss": "about the Muslims", "ans": {"kind": "smp", "sign": "ya"},
                 "why": "Kasra before {ي}: {ـِينَ}. A sound m. plural."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Which sign of jarr?",
            "fields": [{"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "فِي [السَّيَّارَاتِ]", "gloss": "in the cars", "ans": {"sign": "kas"},
                 "why": "A sound f. plural takes kasra in jarr: {ـَاتِ}."},
                {"s": "عَنِ [المُهَنْدِسِينَ]", "gloss": "about the engineers", "ans": {"sign": "ya"},
                 "why": "A sound m. plural: {ـِينَ}. The sign is the {ي}."},
                {"s": "أَخَذْتُ الكِتَابَ مِنْ [مُوسَى]", "gloss": "I took the book from Musa", "ans": {"sign": "hid"},
                 "why": "Maqṣūr: it ends in alif. The kasra is hidden."},
                {"s": "دَرَسْتُ فِي [مَدَارِسَ] كَثِيرَةٍ", "gloss": "I studied in many schools", "ans": {"sign": "fat"},
                 "why": "{مَدَارِسُ} is a diptote. No {ال}, no owner: fatha."},
                {"s": "سَلَّمْتُ عَلَى [أَبِيهِ]", "gloss": "I greeted his father", "ans": {"sign": "ya"},
                 "why": "A five noun with the owner {هِ}: {ي} in jarr."},
                {"s": "جَلَسْتُ فِي [غُرْفَتِي]", "gloss": "I sat in my room", "ans": {"sign": "hid"},
                 "why": "With {ـي} \"my\" the kasra is hidden. The kasra on {ت} is there for the {ي}."},
            ],
        },
        {
            "title": "Find the jarr job and the sign",
            "prompt": "نَظَرْتُ إِلَى سَيَّارَةِ المُهَنْدِسَيْنِ الجَدِيدَةِ وَبَيْتِهِمَا.",
            "en": "I looked at the new car of the two engineers and at their house.",
            "fields": [{"key": "job", "label": "Job", "options": JOBS},
                       {"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "سَيَّارَةِ", "gloss": "car", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {إِلَى}. A singular: kasra."},
                {"s": "المُهَنْدِسَيْنِ", "gloss": "the two engineers", "ans": {"job": "owner", "sign": "ya"},
                 "why": "It owns {سَيَّارَةِ}. Fatha before {ي}: a dual. {مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
                {"s": "الجَدِيدَةِ", "gloss": "the new", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It is feminine, so it describes {سَيَّارَةِ}. It copies jarr with kasra."},
                {"s": "بَيْتِهِمَا", "gloss": "their house", "ans": {"job": "and", "sign": "kas"},
                 "why": "After {وَ}, it copies {سَيَّارَةِ} in jarr. A singular: kasra."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "هَذَا قَلَمُ ___", "gloss": "the two female teachers", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُدَرِّسَتَانِ", "المُدَرِّسَتَيْنِ", "المُدَرِّسَاتِ")},
                 "why": "The owner is in jarr. A dual: {ـَيْنِ}."},
                {"s": "سَأَلْتُ عَنِ ___", "gloss": "the Muslims", "ans": {"pick": "a"},
                 "opts": {"pick": pick("المُسْلِمِينَ", "المُسْلِمُونَ", "المُسْلِمَيْنِ")},
                 "why": "A sound m. plural in jarr: {ـِينَ}."},
                {"s": "سَلَّمْتُ عَلَى ___ زَيْدٍ", "gloss": "Zayd's brother", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَخُو", "أَخَا", "أَخِي")},
                 "why": "After {عَلَى}, jarr. A five noun with an owner: {أَخِي زَيْدٍ}."},
                {"s": "جَلَسْنَا فِي ___", "gloss": "the mosques", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المَسَاجِدَ", "المَسَاجِدِ", "مَسَاجِدِ")},
                 "why": "A diptote with {ال} takes kasra again: {المَسَاجِدِ}."},
                {"s": "مَرَرْتُ بِـ ___", "gloss": "Fatima", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فَاطِمَةَ", "فَاطِمَةٍ", "فَاطِمَةِ")},
                 "why": "{فَاطِمَةُ} is a diptote. No {ال}, no owner: fatha, no tanween."},
                {"s": "هَذِهِ سَيَّارَةُ ___", "gloss": "the judge", "ans": {"pick": "a"},
                 "opts": {"pick": pick("القَاضِي", "القَاضِيِ", "القَاضٍ")},
                 "why": "Manqūṣ with {ال}: the {ي} stays and the kasra is hidden."},
            ],
        },
        {
            "title": "From rafʿ to jarr: pick the jarr form",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "أَبُوكَ → هَذَا بَيْتُ ___", "gloss": "This is your father's house.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَبُوكَ", "أَبِيكَ", "أَبَاكَ")},
                 "why": "Owner, jarr. A five noun changes {و} to {ي}."},
                {"s": "المُدَرِّسَاتُ → سَلَّمْتُ عَلَى ___", "gloss": "I greeted the female teachers.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُدَرِّسَاتَ", "المُدَرِّسَاتِ", "المُدَرِّسَاتُ")},
                 "why": "After {عَلَى}, jarr. A sound f. plural changes damma to kasra."},
                {"s": "المُهَنْدِسَانِ → سَأَلْتُ عَنِ ___", "gloss": "I asked about the two engineers.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("المُهَنْدِسَيْنِ", "المُهَنْدِسِينَ", "المُهَنْدِسَانِ")},
                 "why": "A dual changes alif to {ي}, with fatha before it: {ـَيْنِ}."},
                {"s": "زَيْنَبُ → هَذَا كِتَابُ ___", "gloss": "This is Zaynab's book.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("زَيْنَبٍ", "زَيْنَبِ", "زَيْنَبَ")},
                 "why": "{زَيْنَبُ} is a diptote with no {ال}: damma becomes fatha."},
                {"s": "الفَتَى → سَلَّمْتُ عَلَى ___", "gloss": "I greeted the young man.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الفَتَى", "الفَتِي", "الفَتَا")},
                 "why": "Maqṣūr: the word does not change. The kasra is hidden."},
                {"s": "سَيَّارَاتٌ → جَلَسْنَا فِي ___", "gloss": "We sat in cars.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("سَيَّارَاتٍ", "سَيَّارَاتَ", "سَيَّارَاتٌ")},
                 "why": "A sound f. plural in jarr: kasra with tanween, {ـَاتٍ}."},
            ],
        },
        {
            "title": "Find the jarr job and the sign",
            "prompt": "كَتَبَ الطَّالِبُ رِسَالَةً إِلَى أَبِيهِ وَأُمِّهِ فِي مَدِينَةٍ بَعِيدَةٍ.",
            "en": "The student wrote a letter to his father and his mother in a far city.",
            "fields": [{"key": "job", "label": "Job", "options": JOBS},
                       {"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "أَبِيهِ", "gloss": "his father", "ans": {"job": "prep", "sign": "ya"},
                 "why": "After {إِلَى}. A five noun with an owner: {اِسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ}."},
                {"s": "أُمِّهِ", "gloss": "his mother", "ans": {"job": "and", "sign": "kas"},
                 "why": "After {وَ}, it copies {أَبِيهِ} in jarr. {أُمٌّ} is a normal singular: kasra."},
                {"s": "مَدِينَةٍ", "gloss": "a city", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {فِي}. A singular: kasra."},
                {"s": "بَعِيدَةٍ", "gloss": "far", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {مَدِينَةٍ}. It copies jarr with kasra."},
            ],
        },
        {
            "title": "Which kind of noun? Which sign?",
            "fields": [{"key": "kind", "label": "Kind", "options": KINDS},
                       {"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "سَلَّمْتُ عَلَى [قَاضٍ]", "gloss": "I greeted a judge", "ans": {"kind": "hidv", "sign": "hid"},
                 "why": "Manqūṣ with no {ال}: the {ي} drops. The kasra is hidden on it. The tanween is not the sign."},
                {"s": "فِي [الفَصْلَيْنِ]", "gloss": "in the two classrooms", "ans": {"kind": "dual", "sign": "ya"},
                 "why": "Fatha before {ي}: {ـَيْنِ}. A dual."},
                {"s": "مِنَ [المُعَلِّمِينَ]", "gloss": "from the teachers", "ans": {"kind": "smp", "sign": "ya"},
                 "why": "Kasra before {ي}: {ـِينَ}. A sound m. plural."},
                {"s": "سَافَرْتُ إِلَى [مَكَّةَ]", "gloss": "I travelled to Makkah", "ans": {"kind": "dip", "sign": "fat"},
                 "why": "A feminine place name is a diptote. No {ال}: fatha."},
                {"s": "سَلَّمْتُ عَلَى رَجُلٍ [ذِي] عِلْمٍ", "gloss": "I greeted a man of knowledge", "ans": {"kind": "five", "sign": "ya"},
                 "why": "{ذُو} is one of the five nouns. In jarr it is {ذِي}."},
                {"s": "فِي [دَفَاتِرَ] كَثِيرَةٍ", "gloss": "in many notebooks", "ans": {"kind": "dip", "sign": "fat"},
                 "why": "{دَفَاتِرُ} is a diptote on {مَفَاعِلُ}. No {ال} and no owner: fatha in place of kasra."},
            ],
        },
    ],
}
