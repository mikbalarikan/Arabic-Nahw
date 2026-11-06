# Stage 7, Unit 7: The exception (المُسْتَثْنَى)

# Canonical options (copied from STAGES_5_8_SPEC.md)
DAM = {"k": "dam", "label": "Damma · ضَمَّةٌ", "color": "red"}
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
KAS = {"k": "kas", "label": "Kasra · كَسْرَةٌ", "color": "green"}
ALIF = {"k": "alif", "label": "Alif · الأَلِفُ", "color": "teal"}
WAW = {"k": "waw", "label": "Wāw · الوَاوُ", "color": "blue"}
YA = {"k": "ya", "label": "Yāʾ · اليَاءُ", "color": "purple"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}

VERB = {"k": "verb", "label": "Verb · فِعْلٌ", "color": "navy"}
DOER = {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"}
PREP = {"k": "prep", "label": "After a preposition · اِسْمٌ مَجْرُورٌ", "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}
OBJ = {"k": "obj", "label": "Object · مَفْعُولٌ بِهِ", "color": "pink"}
EXC = {"k": "exc", "label": "Exception · مُسْتَثْنًى", "color": "red"}
PART = {"k": "part", "label": "Particle · حَرْفٌ", "color": "grey"}
STATE = {"k": "state", "label": "State · حَالٌ", "color": "olive"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s7-exception",
    "order": 7,
    "title": "The exception",
    "ar": "المُسْتَثْنَى",
    "blurb": "Everyone came except one: the word after إِلَّا is in naṣb. With غَيْرَ and سِوَى the excepted word is an owner in jarr.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 7 · UNIT 7", "title": "Everyone, except one",
         "text": "You name a group, then you take one part out of it with {إِلَّا} \"except\". The part you take out is the exception ({المُسْتَثْنَى}).",
         "wm": "المُسْتَثْنَى"},

        {"t": "h2", "text": "Three parts"},
        {"t": "p", "text": "An exception sentence has three parts. First the group. Then the tool {إِلَّا}. Then the exception."},
        {"t": "cols", "items": [
            {"color": "orange", "title": "The group", "ar": "المُسْتَثْنَى مِنْهُ", "text": "The whole group: {الطُّلَّابُ}. It keeps its own job."},
            {"color": "grey", "title": "The tool", "ar": "إِلَّا", "text": "\"except\". A particle. It is fixed."},
            {"color": "red", "title": "The exception", "ar": "المُسْتَثْنَى", "text": "The part taken out: {زَيْدًا}. It is in naṣb."},
        ]},
        {"t": "examples", "items": [
            {"ar": "جَاءَ الطُّلَّابُ إِلَّا زَيْدًا.", "en": "The students came, except Zayd.",
             "note": "{الطُّلَّابُ} is the doer, rafʿ. {زَيْدًا} is the exception, naṣb."},
        ]},

        {"t": "h2", "text": "The rule: complete and positive gives naṣb"},
        {"t": "rule", "color": "red", "title": "Group named + no negative = naṣb",
         "text": "When the group is named before {إِلَّا} and the sentence has no negative, the exception is in naṣb. The job of the group does not matter."},
        {"t": "examples", "items": [
            {"ar": "حَضَرَ المُعَلِّمُونَ إِلَّا مُعَلِّمَيْنِ.", "en": "The teachers came, except two teachers.",
             "note": "The group is a doer, rafʿ. The exception is naṣb."},
            {"ar": "رَأَيْتُ الطُّلَّابَ إِلَّا خَالِدًا.", "en": "I saw the students, except Khālid.",
             "note": "The group is an object, naṣb. The exception is naṣb."},
            {"ar": "سَلَّمْتُ عَلَى الضُّيُوفِ إِلَّا رَجُلًا.", "en": "I greeted the guests, except one man.",
             "note": "The group is after a preposition, jarr. The exception is still naṣb."},
            {"ar": "فَشَرِبُوا مِنْهُ إِلَّا قَلِيلًا مِنْهُمْ", "en": "So they drank from it, except a few of them. (al-Baqara 2:249)",
             "note": "{قَلِيلًا} is the exception, naṣb with fatha."},
        ]},
        {"t": "tip", "text": "After a negative the rule can change. In {مَا جَاءَ أَحَدٌ إِلَّا زَيْدٌ} \"No one came except Zayd\" the exception may copy the case of the group. You will study this later. In this unit every sentence is positive."},

        {"t": "h2", "text": "The exception with every group"},
        {"t": "p", "text": "The job gives naṣb. The kind of noun gives the sign."},
        {"t": "table", "head": ["Group", "Example", "Sign of naṣb"], "rows": [
            ["Singular", "جَاءَ الطُّلَّابُ إِلَّا زَيْدًا", "fatha"],
            ["Broken plural", "حَضَرَ النَّاسُ إِلَّا الأَطْفَالَ", "fatha"],
            ["Diptote", "جَاءَ الطُّلَّابُ إِلَّا أَحْمَدَ", "fatha, no tanween"],
            ["Manqūṣ", "حَضَرَ الضُّيُوفُ إِلَّا القَاضِيَ", "fatha, it shows on the {ي}"],
            ["Dual", "حَضَرَ المُعَلِّمُونَ إِلَّا مُعَلِّمَيْنِ", "yāʾ"],
            ["Sound m. plural", "حَضَرَ المُوَظَّفُونَ إِلَّا المُهَنْدِسِينَ", "yāʾ"],
            ["Sound f. plural", "خَرَجَتِ النِّسَاءُ إِلَّا المُدَرِّسَاتِ", "kasra in place of fatha"],
            ["Five nouns", "جَاءَ الرِّجَالُ إِلَّا أَخَاكَ", "alif"],
            ["Maqṣūr", "جَاءَ الأَوْلَادُ إِلَّا مُوسَى", "hidden fatha"],
            ["Noun + ـي \"my\"", "قَرَأْتُ الكُتُبَ إِلَّا كِتَابِي", "hidden fatha"],
        ]},

        {"t": "h2", "text": "Full iʿrāb"},
        {"t": "p", "text": "Say the job, the case and the sign, as you did for the doer and the object."},
        {"t": "examples", "items": [
            {"ar": "زَيْدًا: مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ.",
             "en": "Zaydan: exception, in naṣb, its sign is the fatha that shows.",
             "note": "From {جَاءَ الطُّلَّابُ إِلَّا زَيْدًا}."},
            {"ar": "مُعَلِّمَيْنِ: مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى.",
             "en": "muʿallimayni: exception, in naṣb, its sign is the yāʾ because it is a dual."},
            {"ar": "المُدَرِّسَاتِ: مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الكَسْرَةُ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.",
             "en": "al-mudarrisāti: exception, in naṣb, its sign is the kasra because it is a sound feminine plural."},
            {"ar": "أَخَاكَ: مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الأَلِفُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ.",
             "en": "akhāka: exception, in naṣb, its sign is the alif because it is one of the five nouns."},
            {"ar": "مُوسَى: مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ عَلَى الأَلِفِ.",
             "en": "Mūsā: exception, in naṣb, its sign is a fatha hidden on the alif."},
            {"ar": "إِلَّا: حَرْفُ اسْتِثْنَاءٍ مَبْنِيٌّ عَلَى السُّكُونِ.",
             "en": "illā: a particle of exception, fixed on sukūn."},
        ]},

        {"t": "h2", "text": "غَيْرَ and سِوَى: \"other than\""},
        {"t": "p", "text": "You can use {غَيْرَ} or {سِوَى} in place of {إِلَّا}. These two words are nouns. They take the naṣb of the exception. The word after them is their owner, so it is in jarr."},
        {"t": "table", "head": ["Sentence", "غَيْرَ / سِوَى", "The word after it"], "rows": [
            ["جَاءَ الطُّلَّابُ غَيْرَ زَيْدٍ", "{غَيْرَ}: exception, naṣb, fatha", "{زَيْدٍ}: owner, jarr, kasra"],
            ["حَضَرَ المُعَلِّمُونَ سِوَى مُعَلِّمٍ", "{سِوَى}: exception, naṣb, hidden fatha", "{مُعَلِّمٍ}: owner, jarr, kasra"],
            ["جَاءَ الطُّلَّابُ غَيْرَ أَحْمَدَ", "{غَيْرَ}: exception, naṣb, fatha", "{أَحْمَدَ}: owner, jarr, fatha (diptote)"],
            ["حَضَرَ الضُّيُوفُ غَيْرَ أَبِيكَ", "{غَيْرَ}: exception, naṣb, fatha", "{أَبِيكَ}: owner, jarr, yāʾ"],
        ]},
        {"t": "rule", "color": "purple", "title": "Compare",
         "text": "{إِلَّا زَيْدًا}: {زَيْدًا} is the exception, naṣb. {غَيْرَ زَيْدٍ}: {غَيْرَ} is the exception, naṣb, and {زَيْدٍ} is its owner, jarr."},
        {"t": "tip", "text": "{سِوَى} ends in an alif, like {مُوسَى}. Its fatha is hidden. {غَيْرَ} shows its fatha."},

        {"t": "summary", "title": "In short", "items": [
            "Group + {إِلَّا} + exception: {جَاءَ الطُّلَّابُ إِلَّا زَيْدًا}.",
            "Group named and no negative: the exception is in naṣb, whatever the job of the group.",
            "Signs: fatha, yāʾ (dual and sound m. plural), kasra (sound f. plural), alif (five nouns), hidden fatha (maqṣūr, noun + ـي).",
            "Formula: {مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ ...}",
            "{غَيْرَ} and {سِوَى} take the naṣb themselves. The word after them is an owner in jarr.",
        ]},
    ],

    "practice": [
        {
            "title": "Job and sign",
            "prompt": "جَاءَ الطُّلَّابُ إِلَّا زَيْدًا.",
            "en": "The students came, except Zayd.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, EXC, PART]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, YA, FIXED]},
            ],
            "rows": [
                {"s": "جَاءَ", "gloss": "came", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb. It is fixed on fatha."},
                {"s": "الطُّلَّابُ", "gloss": "the students", "ans": {"job": "doer", "sign": "dam"},
                 "why": "The group is the doer: {فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}. A broken plural takes damma."},
                {"s": "إِلَّا", "gloss": "except", "ans": {"job": "part", "sign": "fixed"},
                 "why": "The tool of exception. A particle, fixed on sukūn."},
                {"s": "زَيْدًا", "gloss": "Zayd", "ans": {"job": "exc", "sign": "fat"},
                 "why": "Group named, no negative: {مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "حَضَرَ المُعَلِّمُونَ إِلَّا ___", "gloss": "two teachers", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُعَلِّمَانِ", "مُعَلِّمَيْنِ", "مُعَلِّمِينَ")},
                 "why": "Exception, naṣb. A dual in naṣb takes yāʾ: {مُعَلِّمَيْنِ}. {مُعَلِّمِينَ} means teachers, three or more."},
                {"s": "جَاءَ الرِّجَالُ إِلَّا ___", "gloss": "your brother", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَخُوكَ", "أَخِيكَ", "أَخَاكَ")},
                 "why": "Exception, naṣb. A five noun in naṣb takes alif: {أَخَاكَ}."},
                {"s": "خَرَجَتِ النِّسَاءُ إِلَّا ___", "gloss": "the female teachers", "ans": {"pick": "a"},
                 "opts": {"pick": pick("المُدَرِّسَاتِ", "المُدَرِّسَاتَ", "المُدَرِّسَاتُ")},
                 "why": "Exception, naṣb. A sound feminine plural takes kasra in naṣb, never fatha."},
                {"s": "سَافَرَ الأَصْدِقَاءُ إِلَّا ___", "gloss": "Zayd", "ans": {"pick": "b"},
                 "opts": {"pick": pick("زَيْدٌ", "زَيْدًا", "زَيْدٍ")},
                 "why": "Group named, no negative: naṣb with fatha. {زَيْدٌ} copies the doer by mistake."},
                {"s": "حَضَرَ الضُّيُوفُ إِلَّا ___", "gloss": "the judge", "ans": {"pick": "a"},
                 "opts": {"pick": pick("القَاضِيَ", "القَاضِي", "القَاضِ")},
                 "why": "A manqūṣ noun shows its fatha in naṣb: {القَاضِيَ}."},
            ],
        },
        {
            "title": "Which sign does the exception take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, KAS, ALIF, YA, HID]}],
            "rows": [
                {"s": "حَضَرَ الطُّلَّابُ إِلَّا [أَحْمَدَ]", "gloss": "except Aḥmad", "ans": {"sign": "fat"},
                 "why": "A diptote in naṣb takes fatha with no tanween."},
                {"s": "نَجَحَ الطُّلَّابُ إِلَّا [طَالِبَيْنِ]", "gloss": "except two students", "ans": {"sign": "ya"},
                 "why": "{مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
                {"s": "جَاءَتِ النِّسَاءُ إِلَّا [الطَّالِبَاتِ]", "gloss": "except the female students", "ans": {"sign": "kas"},
                 "why": "{مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الكَسْرَةُ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ}."},
                {"s": "جَاءَ الأَوْلَادُ إِلَّا [مُوسَى]", "gloss": "except Mūsā", "ans": {"sign": "hid"},
                 "why": "A maqṣūr noun. The fatha is hidden on the alif."},
                {"s": "حَضَرَ المُوَظَّفُونَ إِلَّا [المُهَنْدِسِينَ]", "gloss": "except the engineers", "ans": {"sign": "ya"},
                 "why": "{مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "سَافَرَ أَهْلُ القَرْيَةِ إِلَّا [أَبَاكَ]", "gloss": "except your father", "ans": {"sign": "alif"},
                 "why": "One of the five nouns: alif in naṣb."},
            ],
        },
        {
            "title": "Find the job",
            "prompt": "سَلَّمَ المُدِيرُ عَلَى الطُّلَّابِ إِلَّا خَالِدًا.",
            "en": "The headmaster greeted the students, except Khālid.",
            "fields": [{"key": "job", "label": "Job", "options": [DOER, PREP, OBJ, EXC]}],
            "rows": [
                {"s": "المُدِيرُ", "gloss": "the headmaster", "ans": {"job": "doer"},
                 "why": "He did the greeting. Doer, rafʿ."},
                {"s": "الطُّلَّابِ", "gloss": "the students", "ans": {"job": "prep"},
                 "why": "After {عَلَى}, so jarr. This is the group."},
                {"s": "خَالِدًا", "gloss": "Khālid", "ans": {"job": "exc"},
                 "why": "Taken out of the group by {إِلَّا}. Naṣb, even though the group is in jarr."},
            ],
        },
        {
            "title": "Job and sign with غَيْرَ",
            "prompt": "جَاءَ الضُّيُوفُ غَيْرَ زَيْدٍ.",
            "en": "The guests came, other than Zayd.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OWNER, EXC]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, FIXED]},
            ],
            "rows": [
                {"s": "جَاءَ", "gloss": "came", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "الضُّيُوفُ", "gloss": "the guests", "ans": {"job": "doer", "sign": "dam"},
                 "why": "The group is the doer. A broken plural in rafʿ takes damma."},
                {"s": "غَيْرَ", "gloss": "other than", "ans": {"job": "exc", "sign": "fat"},
                 "why": "{غَيْرَ} takes the job of the exception: {مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
                {"s": "زَيْدٍ", "gloss": "Zayd", "ans": {"job": "owner", "sign": "kas"},
                 "why": "The owner of {غَيْرَ}: {مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}."},
            ],
        },
        {
            "title": "إِلَّا or غَيْرَ: which form?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "جَاءَ الطُّلَّابُ ___ زَيْدٍ", "gloss": "other than Zayd", "ans": {"pick": "b"},
                 "opts": {"pick": pick("غَيْرُ", "غَيْرَ", "غَيْرِ")},
                 "why": "{غَيْرَ} is the exception, so it is in naṣb."},
                {"s": "جَاءَ الطُّلَّابُ غَيْرَ ___", "gloss": "Zayd", "ans": {"pick": "c"},
                 "opts": {"pick": pick("زَيْدًا", "زَيْدٌ", "زَيْدٍ")},
                 "why": "After {غَيْرَ} the word is its owner, in jarr."},
                {"s": "جَاءَ الطُّلَّابُ إِلَّا ___", "gloss": "Zayd", "ans": {"pick": "a"},
                 "opts": {"pick": pick("زَيْدًا", "زَيْدٌ", "زَيْدٍ")},
                 "why": "After {إِلَّا} the word itself is the exception, in naṣb."},
                {"s": "حَضَرَ النَّاسُ غَيْرَ ___", "gloss": "the children", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الأَطْفَالَ", "الأَطْفَالِ", "الأَطْفَالُ")},
                 "why": "Owner of {غَيْرَ}, jarr. A broken plural takes kasra."},
                {"s": "حَضَرَ النَّاسُ إِلَّا ___", "gloss": "the children", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الأَطْفَالَ", "الأَطْفَالِ", "الأَطْفَالُ")},
                 "why": "After {إِلَّا}: exception, naṣb with fatha."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Job and sign",
            "prompt": "نَجَحَ التَّلَامِيذُ إِلَّا تِلْمِيذَيْنِ.",
            "en": "The pupils passed, except two pupils.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, EXC, PART]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, ALIF, YA, FIXED]},
            ],
            "rows": [
                {"s": "نَجَحَ", "gloss": "passed", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "التَّلَامِيذُ", "gloss": "the pupils", "ans": {"job": "doer", "sign": "dam"},
                 "why": "The group is the doer. {التَّلَامِيذُ} is a broken plural: damma in rafʿ."},
                {"s": "إِلَّا", "gloss": "except", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A particle of exception, fixed."},
                {"s": "تِلْمِيذَيْنِ", "gloss": "two pupils", "ans": {"job": "exc", "sign": "ya"},
                 "why": "{مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}. Not alif: alif is the dual in rafʿ."},
            ],
        },
        {
            "title": "Job and sign: the group is an object",
            "prompt": "قَرَأْتُ الكُتُبَ إِلَّا كِتَابَ النَّحْوِ.",
            "en": "I read the books, except the grammar book.",
            "fields": [
                {"key": "job", "label": "Job", "options": [OBJ, EXC, OWNER, PART]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, HID, FIXED]},
            ],
            "rows": [
                {"s": "الكُتُبَ", "gloss": "the books", "ans": {"job": "obj", "sign": "fat"},
                 "why": "The group is the object: {مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
                {"s": "إِلَّا", "gloss": "except", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A particle of exception, fixed."},
                {"s": "كِتَابَ", "gloss": "book (of)", "ans": {"job": "exc", "sign": "fat"},
                 "why": "The exception, naṣb with fatha. It is owned, so it has no tanween."},
                {"s": "النَّحْوِ", "gloss": "grammar", "ans": {"job": "owner", "sign": "kas"},
                 "why": "The owner of {كِتَابَ}: jarr with kasra."},
            ],
        },
        {
            "title": "Which sign does the exception take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, KAS, ALIF, YA, HID]}],
            "rows": [
                {"s": "حَضَرَ الضُّيُوفُ إِلَّا [قَاضِيًا]", "gloss": "except one judge", "ans": {"sign": "fat"},
                 "why": "A manqūṣ noun shows its fatha in naṣb, here with tanween: {قَاضِيًا}."},
                {"s": "نَامَ الأَوْلَادُ إِلَّا [عِيسَى]", "gloss": "except ʿĪsā", "ans": {"sign": "hid"},
                 "why": "A maqṣūr name. The fatha is hidden on the alif."},
                {"s": "غَابَ الطُّلَّابُ إِلَّا [ابْنِي]", "gloss": "except my son", "ans": {"sign": "hid"},
                 "why": "Noun + ـي \"my\": the fatha is hidden before the {ي}."},
                {"s": "خَرَجَ النَّاسُ إِلَّا [الفَلَّاحِينَ]", "gloss": "except the farmers", "ans": {"sign": "ya"},
                 "why": "{مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "جَلَسَتِ النِّسَاءُ إِلَّا [المُعَلِّمَاتِ]", "gloss": "except the female teachers", "ans": {"sign": "kas"},
                 "why": "A sound feminine plural: kasra in place of fatha."},
                {"s": "حَضَرَ أَهْلُ البَيْتِ إِلَّا [أَبَاهُ]", "gloss": "except his father", "ans": {"sign": "alif"},
                 "why": "One of the five nouns: {مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الأَلِفُ}."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "نَجَحَتِ الطَّالِبَاتُ إِلَّا ___", "gloss": "two female students", "ans": {"pick": "b"},
                 "opts": {"pick": pick("طَالِبَتَانِ", "طَالِبَتَيْنِ", "طَالِبَاتٍ")},
                 "why": "Exception, naṣb. A dual takes yāʾ: {طَالِبَتَيْنِ}."},
                {"s": "غَابَ العُمَّالُ إِلَّا ___", "gloss": "one worker", "ans": {"pick": "a"},
                 "opts": {"pick": pick("عَامِلًا", "عَامِلٌ", "عَامِلٍ")},
                 "why": "Exception, naṣb with fatha and tanween."},
                {"s": "رَجَعَ المُسَافِرُونَ إِلَّا ___", "gloss": "your brother", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَخُوكَ", "أَخِيكَ", "أَخَاكَ")},
                 "why": "A five noun in naṣb takes alif: {أَخَاكَ}."},
                {"s": "حَضَرَ الضُّيُوفُ إِلَّا ___", "gloss": "the female doctors", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الطَّبِيبَاتُ", "الطَّبِيبَاتَ", "الطَّبِيبَاتِ")},
                 "why": "A sound feminine plural in naṣb takes kasra: {الطَّبِيبَاتِ}."},
                {"s": "سَافَرَ العُلَمَاءُ إِلَّا ___", "gloss": "the scholar Aḥmad", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَحْمَدَ", "أَحْمَدًا", "أَحْمَدُ")},
                 "why": "A diptote takes fatha in naṣb, never tanween: {أَحْمَدَ}."},
            ],
        },
        {
            "title": "Job and sign with سِوَى",
            "prompt": "سَافَرَ المُعَلِّمُونَ سِوَى مُوسَى.",
            "en": "The teachers travelled, other than Mūsā.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OWNER, EXC]},
                {"key": "sign", "label": "Sign", "options": [WAW, FAT, HID, FIXED]},
            ],
            "rows": [
                {"s": "سَافَرَ", "gloss": "travelled", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "المُعَلِّمُونَ", "gloss": "the teachers", "ans": {"job": "doer", "sign": "waw"},
                 "why": "{فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "سِوَى", "gloss": "other than", "ans": {"job": "exc", "sign": "hid"},
                 "why": "{سِوَى} is the exception, in naṣb. It ends in alif, so the fatha is hidden."},
                {"s": "مُوسَى", "gloss": "Mūsā", "ans": {"job": "owner", "sign": "hid"},
                 "why": "The owner of {سِوَى}, in jarr. {مُوسَى} is maqṣūr and a diptote: the hidden sign is a fatha in place of kasra."},
            ],
        },
        {
            "title": "After غَيْرَ: which sign?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, KAS, ALIF, YA, HID]}],
            "rows": [
                {"s": "جَاءَ القَوْمُ [غَيْرَ] خَالِدٍ", "gloss": "other than Khālid", "ans": {"sign": "fat"},
                 "why": "{غَيْرَ} is the exception, naṣb with fatha."},
                {"s": "جَاءَ الطُّلَّابُ غَيْرَ [عُمَرَ]", "gloss": "other than ʿUmar", "ans": {"sign": "fat"},
                 "why": "Owner, jarr. {عُمَرُ} is a diptote, so it takes fatha in jarr."},
                {"s": "حَضَرَ الضُّيُوفُ غَيْرَ [أَبِيكَ]", "gloss": "other than your father", "ans": {"sign": "ya"},
                 "why": "Owner, jarr. A five noun in jarr takes yāʾ."},
                {"s": "نَجَحَ الطُّلَّابُ غَيْرَ [الطَّالِبَيْنِ]", "gloss": "other than the two students", "ans": {"sign": "ya"},
                 "why": "Owner, jarr. A dual in jarr takes yāʾ."},
                {"s": "خَرَجَتِ النِّسَاءُ غَيْرَ [المُدَرِّسَاتِ]", "gloss": "other than the female teachers", "ans": {"sign": "kas"},
                 "why": "Owner, jarr. A sound feminine plural in jarr takes kasra."},
            ],
        },
    ],
}
