# Stage 7, Unit 9: Inna's noun and kāna's information (اِسْمُ إِنَّ وَخَبَرُ كَانَ)

# Canonical options (copied from STAGES_5_8_SPEC.md)
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

VERB = {"k": "verb", "label": "Verb · فِعْلٌ", "color": "navy"}
KISM = {"k": "kism", "label": "Kāna's noun · اِسْمُ كَانَ", "color": "gold"}
KKHAB = {"k": "kkhab", "label": "Kāna's information · خَبَرُ كَانَ", "color": "red"}
IISM = {"k": "iism", "label": "Inna's noun · اِسْمُ إِنَّ", "color": "gold"}
IKHAB = {"k": "ikhab", "label": "Inna's information · خَبَرُ إِنَّ", "color": "red"}
PART = {"k": "part", "label": "Particle · حَرْفٌ", "color": "grey"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s7-inna-kana",
    "order": 9,
    "title": "Inna's noun and kāna's information",
    "ar": "اِسْمُ إِنَّ وَخَبَرُ كَانَ",
    "blurb": "The two naṣb partners from Stage 5: inna's noun and kāna's information, with the sign of every noun group.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 7 · UNIT 9", "title": "Two naṣb partners",
         "text": "In Stage 5 you met {كَانَ} and {إِنَّ}. Each one puts one partner of the sentence in naṣb. Now you give that partner the right sign for every group.",
         "wm": "إِنَّ وَكَانَ"},

        {"t": "h2", "text": "Mirror images"},
        {"t": "p", "text": "Both enter a nominal sentence. They do opposite things."},
        {"t": "table", "head": ["", "First partner", "Second partner"], "rows": [
            ["Plain sentence", "Topic: rafʿ", "Information: rafʿ"],
            ["{كَانَ} and her sisters", "Kāna's noun: rafʿ", "Kāna's information: naṣb"],
            ["{إِنَّ} and her sisters", "Inna's noun: naṣb", "Inna's information: rafʿ"],
        ]},
        {"t": "examples", "items": [
            {"ar": "اللّٰهُ غَفُورٌ رَحِيمٌ", "en": "Allah is Forgiving, Merciful.", "note": "Topic and information, both rafʿ."},
            {"ar": "وَكَانَ اللّٰهُ غَفُورًا رَحِيمًا", "en": "And Allah is ever Forgiving, Merciful. (an-Nisāʾ 4:96)", "note": "After {كَانَ}: the information {غَفُورًا} is naṣb."},
            {"ar": "إِنَّ اللّٰهَ غَفُورٌ رَحِيمٌ", "en": "Indeed Allah is Forgiving, Merciful. (al-Baqara 2:173)", "note": "After {إِنَّ}: the noun {اللّٰهَ} is naṣb."},
        ]},
        {"t": "cols", "items": [
            {"color": "navy", "title": "Kāna and her sisters", "ar": "كَانَ، أَصْبَحَ، أَمْسَى، أَضْحَى، ظَلَّ، بَاتَ، صَارَ، لَيْسَ", "text": "Past verbs. They are fixed."},
            {"color": "grey", "title": "Inna and her sisters", "ar": "إِنَّ، أَنَّ، كَأَنَّ، لَكِنَّ، لَيْتَ، لَعَلَّ", "text": "Particles. They are fixed."},
        ]},

        {"t": "h2", "text": "Inna's noun with every group"},
        {"t": "p", "text": "The job is inna's noun, so the case is naṣb. The group gives the sign."},
        {"t": "table", "head": ["Group", "Example", "Sign of naṣb"], "rows": [
            ["Singular", "إِنَّ الجَوَّ جَمِيلٌ", "fatha"],
            ["Broken plural", "إِنَّ الطُّلَّابَ مُجْتَهِدُونَ", "fatha"],
            ["Diptote", "كَأَنَّ زَيْنَبَ قَمَرٌ", "fatha, no tanween"],
            ["Manqūṣ", "إِنَّ القَاضِيَ عَادِلٌ", "fatha, it shows on the {ي}"],
            ["Dual", "إِنَّ الطَّالِبَيْنِ مُجْتَهِدَانِ", "yāʾ"],
            ["Sound m. plural", "إِنَّ المُسْلِمِينَ صَادِقُونَ", "yāʾ"],
            ["Sound f. plural", "إِنَّ الطَّالِبَاتِ مُجْتَهِدَاتٌ", "kasra in place of fatha"],
            ["Five nouns", "لَيْتَ أَبَاكَ حَاضِرٌ", "alif"],
            ["Maqṣūr", "لَعَلَّ الفَتَى مَرِيضٌ", "hidden fatha"],
            ["Noun + ـي \"my\"", "إِنَّ أُمِّي مَرِيضَةٌ", "hidden fatha"],
        ]},
        {"t": "tip", "text": "Inna's information stays in rafʿ with its own sign: {مُجْتَهِدُونَ} (wāw), {مُجْتَهِدَانِ} (alif), {مُجْتَهِدَاتٌ} (damma)."},

        {"t": "h2", "text": "Kāna's information with every group"},
        {"t": "p", "text": "The job is kāna's information, so the case is naṣb. The group gives the sign."},
        {"t": "table", "head": ["Group", "Example", "Sign of naṣb"], "rows": [
            ["Singular", "كَانَ الجَوُّ بَارِدًا", "fatha"],
            ["Broken plural", "صَارَ الطُّلَّابُ إِخْوَةً", "fatha"],
            ["Diptote", "أَصْبَحَ الطُّلَّابُ أَصْدِقَاءَ", "fatha, no tanween"],
            ["Manqūṣ", "كَانَ الرَّجُلُ قَاضِيًا", "fatha, it shows on the {ي}"],
            ["Dual", "صَارَ الوَلَدَانِ صَدِيقَيْنِ", "yāʾ"],
            ["Sound m. plural", "أَصْبَحَ الطُّلَّابُ مُجْتَهِدِينَ", "yāʾ"],
            ["Sound f. plural", "كَانَتِ الطَّالِبَاتُ مُجْتَهِدَاتٍ", "kasra in place of fatha"],
            ["Five nouns", "كَانَ الضَّيْفُ أَخَاكَ", "alif"],
            ["Maqṣūr", "كَانَ عَلِيٌّ فَتًى شُجَاعًا", "hidden fatha"],
            ["Noun + ـي \"my\"", "كَانَ زَيْدٌ صَدِيقِي", "hidden fatha"],
        ]},
        {"t": "tip", "text": "A sound feminine plural never takes fatha. Write {مُجْتَهِدَاتٍ}, not {مُجْتَهِدَاتًا}."},

        {"t": "h2", "text": "Fixed words in these jobs"},
        {"t": "p", "text": "An attached pronoun after {إِنَّ} is inna's noun. It is fixed, in the place of naṣb."},
        {"t": "examples", "items": [
            {"ar": "إِنَّهُ صَادِقٌ.", "en": "Indeed he is truthful.", "note": "{ـهُ}: inna's noun, fixed, in the place of naṣb."},
            {"ar": "لَعَلَّكَ مُتْعَبٌ.", "en": "Perhaps you are tired.", "note": "{ـكَ}: inna's noun, fixed, in the place of naṣb."},
            {"ar": "كُنْتُ مَرِيضًا.", "en": "I was ill.", "note": "{ـتُ}: kāna's noun, fixed, in the place of rafʿ. {مَرِيضًا}: kāna's information, naṣb."},
        ]},

        {"t": "h2", "text": "Full iʿrāb"},
        {"t": "examples", "items": [
            {"ar": "إِنَّ المُسْلِمِينَ صَادِقُونَ.", "en": "Indeed the Muslims are truthful.",
             "note": "{المُسْلِمِينَ}: {اِسْمُ إِنَّ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}. {صَادِقُونَ}: {خَبَرُ إِنَّ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ}."},
            {"ar": "لَيْتَ أَبَاكَ حَاضِرٌ.", "en": "If only your father were here.",
             "note": "{أَبَا}: {اِسْمُ لَيْتَ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الأَلِفُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ}."},
            {"ar": "أَصْبَحَ الطُّلَّابُ مُجْتَهِدِينَ.", "en": "The students became hard-working.",
             "note": "{الطُّلَّابُ}: {اِسْمُ أَصْبَحَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}. {مُجْتَهِدِينَ}: {خَبَرُ أَصْبَحَ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
            {"ar": "كَانَتِ الطَّالِبَاتُ مُجْتَهِدَاتٍ.", "en": "The female students were hard-working.",
             "note": "{مُجْتَهِدَاتٍ}: {خَبَرُ كَانَ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الكَسْرَةُ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ}."},
            {"ar": "لَعَلَّ الفَتَى مَرِيضٌ.", "en": "Perhaps the young man is ill.",
             "note": "{الفَتَى}: {اِسْمُ لَعَلَّ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ عَلَى الأَلِفِ}."},
        ]},
        {"t": "rule", "color": "red", "title": "Find the word first",
         "text": "Ask: is it {كَانَ} or {إِنَّ}? After {كَانَ}, the second partner is naṣb. After {إِنَّ}, the first partner is naṣb. Then ask the group for the sign."},

        {"t": "summary", "title": "In short", "items": [
            "Kāna: noun rafʿ, information naṣb. Inna: noun naṣb, information rafʿ.",
            "Signs of naṣb: fatha; yāʾ (dual, sound m. plural); kasra (sound f. plural); alif (five nouns); hidden fatha (maqṣūr, noun + ـي).",
            "A manqūṣ shows its fatha: {إِنَّ القَاضِيَ}، {كَانَ قَاضِيًا}.",
            "An attached pronoun after {إِنَّ} is fixed, in the place of naṣb: {إِنَّهُ}.",
            "Formula: {اِسْمُ إِنَّ مَنْصُوبٌ ...} and {خَبَرُ كَانَ مَنْصُوبٌ ...}",
        ]},
    ],

    "practice": [
        {
            "title": "Job and sign: inna",
            "prompt": "إِنَّ المُعَلِّمِينَ صَادِقُونَ.",
            "en": "Indeed the teachers are truthful.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PART, IISM, IKHAB]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, WAW, YA, FIXED]},
            ],
            "rows": [
                {"s": "إِنَّ", "gloss": "indeed", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A particle, fixed on fatha."},
                {"s": "المُعَلِّمِينَ", "gloss": "the teachers", "ans": {"job": "iism", "sign": "ya"},
                 "why": "{اِسْمُ إِنَّ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "صَادِقُونَ", "gloss": "truthful", "ans": {"job": "ikhab", "sign": "waw"},
                 "why": "{خَبَرُ إِنَّ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ}. A sound masculine plural."},
            ],
        },
        {
            "title": "Job and sign: kāna's sister",
            "prompt": "أَصْبَحَ الطُّلَّابُ مُجْتَهِدِينَ.",
            "en": "The students became hard-working.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, KISM, KKHAB]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, WAW, YA, FIXED]},
            ],
            "rows": [
                {"s": "أَصْبَحَ", "gloss": "became", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A sister of {كَانَ}: a past verb, fixed on fatha."},
                {"s": "الطُّلَّابُ", "gloss": "the students", "ans": {"job": "kism", "sign": "dam"},
                 "why": "{اِسْمُ أَصْبَحَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}. A broken plural."},
                {"s": "مُجْتَهِدِينَ", "gloss": "hard-working", "ans": {"job": "kkhab", "sign": "ya"},
                 "why": "{خَبَرُ أَصْبَحَ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "إِنَّ ___ مُجْتَهِدُونَ", "gloss": "the engineers", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُهَنْدِسُونَ", "المُهَنْدِسِينَ", "المُهَنْدِسَيْنِ")},
                 "why": "Inna's noun, naṣb. A sound masculine plural takes yāʾ: {المُهَنْدِسِينَ}."},
                {"s": "كَانَ الجَوُّ ___", "gloss": "cold", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بَارِدًا", "بَارِدٌ", "بَارِدٍ")},
                 "why": "Kāna's information, naṣb with fatha."},
                {"s": "لَيْتَ ___ حَاضِرٌ", "gloss": "your father", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَبُوكَ", "أَبِيكَ", "أَبَاكَ")},
                 "why": "Inna's noun, naṣb. A five noun takes alif."},
                {"s": "كَانَتِ الطَّالِبَاتُ ___", "gloss": "hard-working", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُجْتَهِدَاتٌ", "مُجْتَهِدَاتٍ", "مُجْتَهِدَاتًا")},
                 "why": "Kāna's information, naṣb. A sound feminine plural takes kasra."},
                {"s": "صَارَ الوَلَدَانِ ___", "gloss": "two friends", "ans": {"pick": "a"},
                 "opts": {"pick": pick("صَدِيقَيْنِ", "صَدِيقَانِ", "صَدِيقِينَ")},
                 "why": "Kāna's information, naṣb. A dual takes yāʾ with fatha before it: {ـَيْنِ}."},
            ],
        },
        {
            "title": "Which sign of naṣb?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, KAS, ALIF, YA, HID]}],
            "rows": [
                {"s": "إِنَّ [الطَّالِبَاتِ] مُجْتَهِدَاتٌ", "gloss": "the female students", "ans": {"sign": "kas"},
                 "why": "Inna's noun. A sound feminine plural: kasra in place of fatha."},
                {"s": "لَعَلَّ [الفَتَى] مَرِيضٌ", "gloss": "the young man", "ans": {"sign": "hid"},
                 "why": "Inna's noun. A maqṣūr noun: the fatha is hidden on the alif."},
                {"s": "إِنَّ [القَاضِيَ] عَادِلٌ", "gloss": "the judge", "ans": {"sign": "fat"},
                 "why": "Inna's noun. A manqūṣ noun shows its fatha on the {ي}."},
                {"s": "كَانَ الضَّيْفُ [أَخَاكَ]", "gloss": "your brother", "ans": {"sign": "alif"},
                 "why": "Kāna's information. A five noun takes alif."},
                {"s": "كَأَنَّ [زَيْنَبَ] قَمَرٌ", "gloss": "Zaynab", "ans": {"sign": "fat"},
                 "why": "Inna's noun. A diptote: fatha, no tanween."},
                {"s": "أَصْبَحَ الطُّلَّابُ [أَصْدِقَاءَ]", "gloss": "friends", "ans": {"sign": "fat"},
                 "why": "Kāna's information. {أَصْدِقَاءُ} is a diptote: fatha, no tanween."},
            ],
        },
        {
            "title": "Which partner is it?",
            "fields": [{"key": "job", "label": "Job", "options": [KISM, KKHAB, IISM, IKHAB]}],
            "rows": [
                {"s": "إِنَّ [الطَّالِبَيْنِ] مُجْتَهِدَانِ", "gloss": "the two students", "ans": {"job": "iism"},
                 "why": "The first partner after {إِنَّ}: inna's noun, naṣb with yāʾ."},
                {"s": "كَانَ [المُعَلِّمُونَ] حَاضِرِينَ", "gloss": "the teachers", "ans": {"job": "kism"},
                 "why": "The first partner after {كَانَ}: kāna's noun, rafʿ with wāw."},
                {"s": "كَانَ المُعَلِّمُونَ [حَاضِرِينَ]", "gloss": "present", "ans": {"job": "kkhab"},
                 "why": "The second partner after {كَانَ}: kāna's information, naṣb with yāʾ."},
                {"s": "لَيْتَ الجَوَّ [بَارِدٌ]", "gloss": "cold", "ans": {"job": "ikhab"},
                 "why": "The second partner after {لَيْتَ}: inna's information, rafʿ."},
                {"s": "بَاتَ [الأَطْفَالُ] نَائِمِينَ", "gloss": "the children", "ans": {"job": "kism"},
                 "why": "{بَاتَ} is a sister of {كَانَ}. Its first partner is its noun, rafʿ."},
            ],
        },
        {
            "title": "Case and sign",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, ALIF, WAW, YA, FIXED]},
            ],
            "rows": [
                {"s": "إِنَّ [أَبَاكَ] كَرِيمٌ", "gloss": "your father", "ans": {"case": "nasb", "sign": "alif"},
                 "why": "Inna's noun: naṣb. A five noun: alif."},
                {"s": "كَانَ [أَبُوكَ] كَرِيمًا", "gloss": "your father", "ans": {"case": "raf", "sign": "waw"},
                 "why": "Kāna's noun: rafʿ. A five noun: wāw."},
                {"s": "إِنَّ الطُّلَّابَ [مُجْتَهِدُونَ]", "gloss": "hard-working", "ans": {"case": "raf", "sign": "waw"},
                 "why": "Inna's information stays rafʿ. A sound masculine plural: wāw."},
                {"s": "أَمْسَى الطِّفْلَانِ [مَرِيضَيْنِ]", "gloss": "ill", "ans": {"case": "nasb", "sign": "ya"},
                 "why": "Kāna's information: naṣb. A dual: yāʾ."},
                {"s": "إِنَّـ[كَ] صَادِقٌ", "gloss": "you (the attached ـكَ)", "ans": {"case": "nasb", "sign": "fixed"},
                 "why": "An attached pronoun as inna's noun: fixed, in the place of naṣb."},
                {"s": "لَيْسَ [الطَّالِبُ] غَائِبًا", "gloss": "the student", "ans": {"case": "raf", "sign": "dam"},
                 "why": "{لَيْسَ} is a sister of {كَانَ}. Its noun is rafʿ with damma."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Job and sign: a sister of inna",
            "prompt": "لَعَلَّ المُهَنْدِسَيْنِ حَاضِرَانِ.",
            "en": "Perhaps the two engineers are present.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PART, IISM, IKHAB, KISM]},
                {"key": "sign", "label": "Sign", "options": [ALIF, YA, WAW, FIXED]},
            ],
            "rows": [
                {"s": "لَعَلَّ", "gloss": "perhaps", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A sister of {إِنَّ}: a particle, fixed on fatha."},
                {"s": "المُهَنْدِسَيْنِ", "gloss": "the two engineers", "ans": {"job": "iism", "sign": "ya"},
                 "why": "{اِسْمُ لَعَلَّ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}. Fatha before the {ي}: a dual."},
                {"s": "حَاضِرَانِ", "gloss": "present", "ans": {"job": "ikhab", "sign": "alif"},
                 "why": "{خَبَرُ لَعَلَّ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الأَلِفُ لِأَنَّهُ مُثَنًّى}."},
            ],
        },
        {
            "title": "Job and sign: kāna",
            "prompt": "كَانَتِ المُعَلِّمَاتُ مَسْرُورَاتٍ.",
            "en": "The female teachers were happy.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, KISM, KKHAB, IISM]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, FIXED]},
            ],
            "rows": [
                {"s": "كَانَتِ", "gloss": "were", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha. The {ت} shows the feminine noun. Its kasra is only for joining."},
                {"s": "المُعَلِّمَاتُ", "gloss": "the female teachers", "ans": {"job": "kism", "sign": "dam"},
                 "why": "{اِسْمُ كَانَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}. A sound feminine plural."},
                {"s": "مَسْرُورَاتٍ", "gloss": "happy", "ans": {"job": "kkhab", "sign": "kas"},
                 "why": "{خَبَرُ كَانَ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الكَسْرَةُ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ}."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "إِنَّ ___ عَادِلٌ", "gloss": "the judge", "ans": {"pick": "b"},
                 "opts": {"pick": pick("القَاضِي", "القَاضِيَ", "القَاضِيُ")},
                 "why": "Inna's noun, naṣb. A manqūṣ noun shows its fatha: {القَاضِيَ}."},
                {"s": "كَانَ الرَّجُلُ ___", "gloss": "a judge", "ans": {"pick": "c"},
                 "opts": {"pick": pick("قَاضٍ", "قَاضِيٌ", "قَاضِيًا")},
                 "why": "Kāna's information, naṣb. The fatha shows on the {ي}, with tanween: {قَاضِيًا}."},
                {"s": "كَانَ عُثْمَانُ ___ كَرِيمًا", "gloss": "a young man", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فَتًى", "فَتًا", "فَتَى")},
                 "why": "Kāna's information, naṣb. A maqṣūr noun: {فَتًى}, the fatha is hidden. It is indefinite, so it has tanween."},
                {"s": "إِنَّ ___ مُجْتَهِدَاتٌ", "gloss": "the girls", "ans": {"pick": "c"},
                 "opts": {"pick": pick("البَنَاتُ", "البَنَاتَ", "البَنَاتِ")},
                 "why": "Inna's noun, naṣb. A sound feminine plural takes kasra."},
                {"s": "ظَلَّ العُمَّالُ ___", "gloss": "standing", "ans": {"pick": "b"},
                 "opts": {"pick": pick("قَائِمُونَ", "قَائِمِينَ", "قَائِمَيْنِ")},
                 "why": "Kāna's information, naṣb. A sound masculine plural takes yāʾ with kasra before it."},
                {"s": "لَيْتَ ___ هُنَا", "gloss": "your brother", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَخُوكَ", "أَخَاكَ", "أَخِيكَ")},
                 "why": "Inna's noun, naṣb. A five noun takes alif."},
            ],
        },
        {
            "title": "Which sign of naṣb?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, KAS, ALIF, YA, HID]}],
            "rows": [
                {"s": "إِنَّ [أُمِّي] مَرِيضَةٌ", "gloss": "my mother", "ans": {"sign": "hid"},
                 "why": "Inna's noun. Noun + ـي \"my\": the fatha is hidden before the {ي}."},
                {"s": "أَصْبَحَ المُسْلِمُونَ [إِخْوَةً]", "gloss": "brothers", "ans": {"sign": "fat"},
                 "why": "Kāna's information. {إِخْوَةٌ} is a broken plural: fatha."},
                {"s": "جَاءَ زَيْدٌ لَكِنَّ [أَخَاهُ] غَائِبٌ", "gloss": "his brother", "ans": {"sign": "alif"},
                 "why": "Inna's noun after {لَكِنَّ}. A five noun: alif."},
                {"s": "إِنَّ [المُدَرِّسَاتِ] حَاضِرَاتٌ", "gloss": "the female teachers", "ans": {"sign": "kas"},
                 "why": "Inna's noun. A sound feminine plural: kasra in place of fatha."},
                {"s": "بَاتَ الطِّفْلَانِ [نَائِمَيْنِ]", "gloss": "asleep", "ans": {"sign": "ya"},
                 "why": "Kāna's information. A dual: yāʾ."},
                {"s": "إِنَّ [مُوسَى] نَبِيٌّ", "gloss": "Mūsā", "ans": {"sign": "hid"},
                 "why": "Inna's noun. A maqṣūr name: the fatha is hidden on the alif."},
            ],
        },
        {
            "title": "Which partner is it?",
            "fields": [{"key": "job", "label": "Job", "options": [KISM, KKHAB, IISM, IKHAB]}],
            "rows": [
                {"s": "لَيْسَ [المُهْمِلُونَ] نَاجِحِينَ", "gloss": "the careless ones", "ans": {"job": "kism"},
                 "why": "{لَيْسَ} is a sister of {كَانَ}. Its first partner is its noun, rafʿ with wāw."},
                {"s": "لَيْسَ المُهْمِلُونَ [نَاجِحِينَ]", "gloss": "successful", "ans": {"job": "kkhab"},
                 "why": "The second partner after {لَيْسَ}: kāna's information, naṣb with yāʾ."},
                {"s": "لَعَلَّ [الجَوَّ] جَمِيلٌ", "gloss": "the weather", "ans": {"job": "iism"},
                 "why": "{لَعَلَّ} is a sister of {إِنَّ}. Its first partner is its noun, naṣb."},
                {"s": "إِنَّكَ [مُجْتَهِدٌ]", "gloss": "hard-working", "ans": {"job": "ikhab"},
                 "why": "The {ـكَ} is inna's noun. {مُجْتَهِدٌ} is inna's information, rafʿ."},
                {"s": "ظَلَّ [العُمَّالُ] صَائِمِينَ", "gloss": "the workers", "ans": {"job": "kism"},
                 "why": "{ظَلَّ} is a sister of {كَانَ}. Its first partner is its noun, rafʿ."},
            ],
        },
        {
            "title": "Case and sign",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, ALIF, WAW, YA]},
            ],
            "rows": [
                {"s": "إِنَّ [المُعَلِّمَيْنِ] حَاضِرَانِ", "gloss": "the two teachers", "ans": {"case": "nasb", "sign": "ya"},
                 "why": "Inna's noun: naṣb. A dual: yāʾ."},
                {"s": "كَانَ [المُعَلِّمَانِ] حَاضِرَيْنِ", "gloss": "the two teachers", "ans": {"case": "raf", "sign": "alif"},
                 "why": "Kāna's noun: rafʿ. A dual: alif."},
                {"s": "لَيْتَ الأَوْلَادَ [صَادِقُونَ]", "gloss": "truthful", "ans": {"case": "raf", "sign": "waw"},
                 "why": "Inna's information: rafʿ. A sound masculine plural: wāw."},
                {"s": "صَارَ الرِّجَالُ [أَغْنِيَاءَ]", "gloss": "rich", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "Kāna's information: naṣb. {أَغْنِيَاءُ} is a diptote: fatha, no tanween."},
                {"s": "إِنَّ [أَبَاهُ] مُسَافِرٌ", "gloss": "his father", "ans": {"case": "nasb", "sign": "alif"},
                 "why": "Inna's noun: naṣb. A five noun: alif."},
                {"s": "كَانَ [أَبُوهُ] مُسَافِرًا", "gloss": "his father", "ans": {"case": "raf", "sign": "waw"},
                 "why": "Kāna's noun: rafʿ. A five noun: wāw."},
            ],
        },
    ],
}
