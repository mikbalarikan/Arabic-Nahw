# Stage 8: class exercise (review of units 1-7, done together in class before the Stage 8 quiz)

# Canonical options (copied from STAGES_5_8_SPEC.md)
DAM = {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
FAT = {"k": "fat",   "label": "Fatha · فَتْحَةٌ",                "color": "pink"}
KAS = {"k": "kas",   "label": "Kasra · كَسْرَةٌ",                "color": "green"}
SUK = {"k": "suk",   "label": "Sukūn · سُكُونٌ",                 "color": "navy"}
ALIF = {"k": "alif",  "label": "Alif · الأَلِفُ",                  "color": "teal"}
WAW = {"k": "waw",   "label": "Wāw · الوَاوُ",                   "color": "blue"}
YA = {"k": "ya",    "label": "Yāʾ · اليَاءُ",                   "color": "purple"}
HID = {"k": "hid",   "label": "Hidden vowel · مُقَدَّرَةٌ",         "color": "brown"}
NUN = {"k": "nun",   "label": "Nūn stays · ثُبُوتُ النُّونِ",        "color": "olive"}
DROP = {"k": "drop",  "label": "Nūn drops · حَذْفُ النُّونِ",         "color": "orange"}
WEAK = {"k": "weak",  "label": "Weak letter drops · حَذْفُ حَرْفِ العِلَّةِ", "color": "gold"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ",                  "color": "grey"}

RAF = {"k": "raf",  "label": "Rafʿ · رَفْعٌ",   "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ",  "color": "pink"}
JAZM = {"k": "jazm", "label": "Jazm · جَزْمٌ",  "color": "navy"}

VERB = {"k": "verb",  "label": "Verb · فِعْلٌ",                       "color": "navy"}
DOER = {"k": "doer",  "label": "Doer · فَاعِلٌ",                      "color": "orange"}
KISM = {"k": "kism",  "label": "Kāna's noun · اِسْمُ كَانَ",             "color": "gold"}
IISM = {"k": "iism",  "label": "Inna's noun · اِسْمُ إِنَّ",              "color": "gold"}
PREP = {"k": "prep",  "label": "After a preposition · اِسْمٌ مَجْرُورٌ",    "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ",               "color": "purple"}
OBJ = {"k": "obj",   "label": "Object · مَفْعُولٌ بِهِ",                "color": "pink"}
PART = {"k": "part",  "label": "Particle · حَرْفٌ",                     "color": "grey"}

# From Unit 1
PAST = {"k": "past", "label": "Past · مَاضٍ", "color": "navy"}
PRES = {"k": "pres", "label": "Present · مُضَارِعٌ", "color": "orange"}
ORDR = {"k": "ordr", "label": "Order · أَمْرٌ", "color": "brown"}
FLEX = {"k": "flex", "label": "Flexible · مُعْرَبٌ", "color": "green"}
FIXD = {"k": "fixd", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}

# From Unit 6
CW = {"k": "cw", "label": "Condition word · أَدَاةُ الشَّرْطِ", "color": "navy"}
CV = {"k": "cv", "label": "Condition verb · فِعْلُ الشَّرْطِ", "color": "teal"}
AV = {"k": "av", "label": "Answer verb · جَوَابُ الشَّرْطِ", "color": "purple"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s8-exercise",
    "order": 8,
    "kind": "exercise",
    "title": "Stage 8 class exercise",
    "ar": "تَمْرِينُ الفِعْلِ المُضَارِعِ",
    "blurb": "Ten mixed cards on the present verb in rafʿ, naṣb and jazm, done together in class before the Stage 8 quiz.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 8 · CLASS EXERCISE", "title": "The present verb, all together",
         "text": "Ten cards that mix every Stage 8 unit. The last two cards review the nouns of Stages 5 to 7. We do them together in class, before the Stage 8 quiz.",
         "wm": "الفِعْلُ المُضَارِعُ"},

        {"t": "h2", "text": "How we do it in class"},
        {"t": "p", "text": "Work in pairs, or come to the board. One student reads the sentence aloud and gives the iʿrāb of one word. The partner says why, or corrects it. Then swap for the next row."},
        {"t": "tip", "text": "For a verb, ask two questions. What comes before it? That gives the case. What kind of verb is it? That gives the sign."},
        {"t": "tip", "text": "For a noun, use the old steps. Find the job. The job gives the case. The kind of noun gives the sign."},

        {"t": "h2", "text": "The seven topics"},
        {"t": "cols", "items": [
            {"color": "orange", "title": "1. The present verb", "ar": "المُضَارِعُ",
             "text": "Starts with {أ ن ي ت}. Flexible, with rafʿ, naṣb and jazm. Fixed with {ـْنَ} and {ـَنَّ}."},
            {"color": "red", "title": "2. Rafʿ", "ar": "الرَّفْعُ",
             "text": "No particle: damma. Hidden on {و}، {ي} and alif: {يَدْعُو}، {يَرْمِي}، {يَسْعَى}."},
            {"color": "olive", "title": "3. The five verbs", "ar": "الأَفْعَالُ الخَمْسَةُ",
             "text": "{يَفْعَلَانِ}، {تَفْعَلَانِ}، {يَفْعَلُونَ}، {تَفْعَلُونَ}، {تَفْعَلِينَ}. The nūn stays in rafʿ and drops in naṣb and jazm."},
            {"color": "pink", "title": "4. Naṣb", "ar": "النَّصْبُ",
             "text": "After {أَنْ}، {لَنْ}، {كَيْ}، {لِـ}، {حَتَّى}، {إِذَنْ}: fatha."},
            {"color": "navy", "title": "5. Jazm", "ar": "الجَزْمُ",
             "text": "After {لَمْ}، {لَمَّا}، {لِـ} of order, {لَا} that forbids: sukūn."},
            {"color": "teal", "title": "6. Two verbs in jazm", "ar": "الشَّرْطُ",
             "text": "{إِنْ}، {مَنْ}، {مَا}: {إِنْ تَدْرُسْ تَنْجَحْ}."},
            {"color": "gold", "title": "7. Weak endings", "ar": "المُعْتَلُّ الآخِرِ",
             "text": "In jazm the weak letter drops: {لَمْ يَدْعُ}، {لَمْ يَرْمِ}، {لَمْ يَسْعَ}."},
        ]},

        {"t": "h2", "text": "All the signs in one table"},
        {"t": "table", "head": ["Kind of verb", "Rafʿ", "Naṣb", "Jazm"], "rows": [
            ["strong ending", "يَكْتُبُ", "لَنْ يَكْتُبَ", "لَمْ يَكْتُبْ"],
            ["ends in و", "يَدْعُو", "لَنْ يَدْعُوَ", "لَمْ يَدْعُ"],
            ["ends in ي", "يَرْمِي", "لَنْ يَرْمِيَ", "لَمْ يَرْمِ"],
            ["ends in alif", "يَسْعَى", "لَنْ يَسْعَى", "لَمْ يَسْعَ"],
            ["five verbs", "يَكْتُبُونَ", "لَنْ يَكْتُبُوا", "لَمْ يَكْتُبُوا"],
            ["nūn of women (fixed)", "يَكْتُبْنَ", "لَنْ يَكْتُبْنَ", "لَمْ يَكْتُبْنَ"],
        ]},

        {"t": "summary", "title": "Remember", "items": [
            "No particle of naṣb or jazm: rafʿ. {سَـ}، {سَوْفَ} and {لَا} \"not\" change nothing.",
            "Naṣb: fatha, also on {و} and {ي}. Hidden on alif. The five verbs lose the nūn.",
            "Jazm: sukūn. The weak letter drops. The five verbs lose the nūn.",
            "{إِنْ}، {مَنْ} and {مَا} of condition put two verbs in jazm.",
            "With the nūn of women or the nūn of emphasis the verb is fixed. A particle cannot change it.",
            "The formula: {فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ}.",
        ]},
    ],

    "practice": [
        # 1 · unit 1: kind of verb, flexible or fixed
        {
            "title": "Which kind of verb? Flexible or fixed?",
            "fields": [
                {"key": "vt", "label": "Kind of verb", "options": [PAST, PRES, ORDR]},
                {"key": "st", "label": "Status", "options": [FLEX, FIXD]},
            ],
            "rows": [
                {"s": "يَغْسِلُ", "gloss": "he washes", "ans": {"vt": "pres", "st": "flex"},
                 "why": "It starts with {ي}. Nothing is attached: flexible."},
                {"s": "غَسَلْنَا", "gloss": "we washed", "ans": {"vt": "past", "st": "fixd"},
                 "why": "A past verb. Every past verb is fixed."},
                {"s": "اِغْسِلُوا", "gloss": "wash (you all)!", "ans": {"vt": "ordr", "st": "fixd"},
                 "why": "An order verb. Every order verb is fixed."},
                {"s": "يَغْسِلْنَ", "gloss": "they (f) wash", "ans": {"vt": "pres", "st": "fixd"},
                 "why": "A present verb with the nūn of women: fixed on sukūn."},
                {"s": "لَأَغْسِلَنَّ", "gloss": "I will surely wash", "ans": {"vt": "pres", "st": "fixd"},
                 "why": "A present verb with the nūn of emphasis: fixed on fatha."},
                {"s": "تَغْسِلِينَ", "gloss": "you (f) wash", "ans": {"vt": "pres", "st": "flex"},
                 "why": "The {ي} of one woman does not make it fixed. It is one of the five verbs."},
            ],
        },
        # 2 · unit 2: rafʿ, hidden damma
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "يَرْجُو المُؤْمِنُ رَحْمَةَ رَبِّهِ.",
            "en": "The believer hopes for the mercy of his Lord.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, OWNER]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, HID]},
            ],
            "rows": [
                {"s": "يَرْجُو", "ans": {"job": "verb", "sign": "hid"},
                 "why": "No particle: rafʿ. The damma is hidden on the {و}, too heavy."},
                {"s": "المُؤْمِنُ", "ans": {"job": "doer", "sign": "dam"},
                 "why": "The one who hopes: {فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}."},
                {"s": "رَحْمَةَ", "ans": {"job": "obj", "sign": "fat"},
                 "why": "What he hopes for: object, naṣb, fatha."},
                {"s": "رَبِّهِ", "ans": {"job": "owner", "sign": "kas"},
                 "why": "Owner of {رَحْمَةَ}: jarr, kasra."},
            ],
        },
        # 3 · unit 3: the five verbs
        {
            "title": "The five verbs: case and sign",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JAZM]},
                {"key": "sign", "label": "Sign", "options": [DAM, NUN, DROP, SUK]},
            ],
            "rows": [
                {"s": "أَنْتُمَا [تَشْرَحَانِ] الدَّرْسَ", "gloss": "you two explain the lesson", "ans": {"case": "raf", "sign": "nun"},
                 "why": "No particle: rafʿ. A five verb: the nūn stays."},
                {"s": "لَنْ [تَجْلِسُوا] هُنَا", "gloss": "you (m pl) will not sit here", "ans": {"case": "nasb", "sign": "drop"},
                 "why": "After {لَنْ}: naṣb. {تَجْلِسُونَ} loses its nūn."},
                {"s": "لَمْ [تَحْفَظِي] السُّورَةَ", "gloss": "you (f) did not memorise the sūra", "ans": {"case": "jazm", "sign": "drop"},
                 "why": "After {لَمْ}: jazm. {تَحْفَظِينَ} loses its nūn. The {ي} is the doer."},
                {"s": "هُمْ [يَلْبَسُونَ] الثِّيَابَ", "gloss": "they wear the clothes", "ans": {"case": "raf", "sign": "nun"},
                 "why": "No particle: rafʿ, the nūn stays."},
                {"s": "اُدْرُسَا حَتَّى [تَفْهَمَا]", "gloss": "study (you two) so that you understand", "ans": {"case": "nasb", "sign": "drop"},
                 "why": "After {حَتَّى}: naṣb. {تَفْهَمَانِ} loses its nūn."},
            ],
        },
        # 4 · unit 4: the six particles of naṣb
        {
            "title": "Which form is right? (naṣb)",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "أُحِبُّ أَنْ ___ إِلَى مَكَّةَ.", "gloss": "I would like to travel to Makkah.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أُسَافِرَ", "أُسَافِرُ", "أُسَافِرْ")},
                 "why": "After {أَنْ}: naṣb, fatha."},
                {"s": "لَنْ ___ إِلَى هَذَا المَكَانِ.", "gloss": "We will not return to this place.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("نَرْجِعُ", "نَرْجِعَ", "نَرْجِعْ")},
                 "why": "After {لَنْ}: naṣb, fatha."},
                {"s": "يَدْرُسُ الطُّلَّابُ كَيْ ___.", "gloss": "The students study so that they succeed.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَنْجَحُونَ", "يَنْجَحَ", "يَنْجَحُوا")},
                 "why": "After {كَيْ}: naṣb. \"They\" is a five verb, so the nūn drops."},
                {"s": "ذَهَبَتِ البِنْتُ إِلَى السُّوقِ ___ خُبْزًا.", "gloss": "The girl went to the market in order to buy bread.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لِتَشْتَرِيَ", "لِتَشْتَرِي", "لِتَشْتَرِ")},
                 "why": "After {لِـ} of purpose: naṣb. The fatha shows on the {ي}."},
                {"s": "اِجْلِسْ حَتَّى ___ الدَّرْسُ.", "gloss": "Sit until the lesson ends.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَنْتَهِي", "يَنْتَهِيَ", "يَنْتَهِ")},
                 "why": "After {حَتَّى}: naṣb. The fatha shows on the {ي}."},
                {"s": "سَأَدْرُسُ اللَّيْلَةَ. إِذَنْ ___.", "gloss": "I will study tonight. Then you will understand.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَفْهَمُ", "تَفْهَمْ", "تَفْهَمَ")},
                 "why": "{إِذَنْ} starts the answer, right before the verb: naṣb, fatha."},
            ],
        },
        # 5 · unit 5: jazm with لَمْ
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "لَمْ يَكْتُبْ أَخُوكَ رِسَالَةً إِلَى صَدِيقِهِ.",
            "en": "Your brother did not write a letter to his friend.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PART, VERB, DOER, OBJ, PREP]},
                {"key": "sign", "label": "Sign", "options": [FIXED, SUK, DAM, WAW, FAT, KAS]},
            ],
            "rows": [
                {"s": "لَمْ", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A particle of jazm, fixed on sukūn, with no place."},
                {"s": "يَكْتُبْ", "ans": {"job": "verb", "sign": "suk"},
                 "why": "{فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ}."},
                {"s": "أَخُوكَ", "ans": {"job": "doer", "sign": "waw"},
                 "why": "Doer, rafʿ. One of the five nouns with an owner: sign wāw."},
                {"s": "رِسَالَةً", "ans": {"job": "obj", "sign": "fat"},
                 "why": "What he did not write: object, fatha."},
                {"s": "صَدِيقِهِ", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {إِلَى}: jarr, kasra."},
            ],
        },
        # 6 · unit 6: condition
        {
            "title": "Part and sign",
            "prompt": "إِنْ تَحْفَظِي القُرْآنَ تَفْرَحْ أُمُّكِ.",
            "en": "If you (f) memorise the Qur'an, your mother will be happy.",
            "fields": [
                {"key": "role", "label": "Part", "options": [CW, CV, AV, OBJ, DOER]},
                {"key": "sign", "label": "Sign", "options": [FIXED, SUK, DROP, FAT, DAM]},
            ],
            "rows": [
                {"s": "إِنْ", "ans": {"role": "cw", "sign": "fixed"},
                 "why": "{حَرْفُ شَرْطٍ جَازِمٌ}, fixed on sukūn."},
                {"s": "تَحْفَظِي", "ans": {"role": "cv", "sign": "drop"},
                 "why": "The condition verb, in jazm. {تَحْفَظِينَ} is a five verb: the nūn drops."},
                {"s": "القُرْآنَ", "ans": {"role": "obj", "sign": "fat"},
                 "why": "What you memorise: object, fatha."},
                {"s": "تَفْرَحْ", "ans": {"role": "av", "sign": "suk"},
                 "why": "The answer verb, in jazm with sukūn. It does not need the same person as the first verb."},
                {"s": "أُمُّكِ", "ans": {"role": "doer", "sign": "dam"},
                 "why": "The one who is happy: doer of {تَفْرَحْ}, rafʿ, damma."},
            ],
        },
        # 7 · unit 7: weak endings in three cases
        {
            "title": "Weak endings: case and sign",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JAZM]},
                {"key": "sign", "label": "Sign", "options": [HID, FAT, WEAK, SUK]},
            ],
            "rows": [
                {"s": "الرَّاعِي [يَرْعَى] الغَنَمَ", "gloss": "the shepherd looks after the sheep", "ans": {"case": "raf", "sign": "hid"},
                 "why": "No particle: rafʿ. Hidden damma on the alif, impossible."},
                {"s": "لَمْ [يَشْتَرِ] أَبِي سَيَّارَةً", "gloss": "my father did not buy a car", "ans": {"case": "jazm", "sign": "weak"},
                 "why": "After {لَمْ}: jazm. {يَشْتَرِي} loses its {ي}."},
                {"s": "أُرِيدُ أَنْ [أَتْلُوَ] سُورَةً", "gloss": "I want to recite a sūra", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "After {أَنْ}: naṣb. The fatha shows on the {و}."},
                {"s": "لَا [تَرْمِ] الوَرَقَ", "gloss": "don't throw the paper", "ans": {"case": "jazm", "sign": "weak"},
                 "why": "{لَا} forbids: jazm. {تَرْمِي} loses its {ي}."},
                {"s": "اِجْتَهِدْ حَتَّى [يَرْضَى] المُدَرِّسُ", "gloss": "work hard until the teacher is pleased", "ans": {"case": "nasb", "sign": "hid"},
                 "why": "After {حَتَّى}: naṣb. The fatha is hidden on the alif."},
                {"s": "الطِّفْلُ [يَجْرِي] فِي الحَدِيقَةِ", "gloss": "the child runs in the garden", "ans": {"case": "raf", "sign": "hid"},
                 "why": "No particle: rafʿ. Hidden damma on the {ي}, too heavy."},
            ],
        },
        # 8 · units 1, 3, 5: the two لَا, fixed verbs, mixed signs
        {
            "title": "Rafʿ, naṣb or jazm? And the sign",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JAZM]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, SUK, HID, DROP, FIXED]},
            ],
            "rows": [
                {"s": "المُؤْمِنُ لَا [يَكْذِبُ]", "gloss": "the believer does not lie", "ans": {"case": "raf", "sign": "dam"},
                 "why": "A fact. This {لَا} only negates, so the verb stays in rafʿ with damma."},
                {"s": "لَا [تَكْذِبْ] أَبَدًا", "gloss": "never lie", "ans": {"case": "jazm", "sign": "suk"},
                 "why": "An order not to act: {لَا} forbids. Jazm with sukūn."},
                {"s": "الطَّالِبَاتُ لَمْ [يَتَأَخَّرْنَ]", "gloss": "the female students were not late", "ans": {"case": "jazm", "sign": "fixed"},
                 "why": "The nūn of women: fixed on sukūn, in the place of jazm. {لَمْ} cannot change it."},
                {"s": "لَمْ [يَفْهَمُوا] السُّؤَالَ", "gloss": "they did not understand the question", "ans": {"case": "jazm", "sign": "drop"},
                 "why": "After {لَمْ}: jazm. A five verb: the nūn drops."},
                {"s": "سَوْفَ [نَمْشِي] مَعًا", "gloss": "we will walk together", "ans": {"case": "raf", "sign": "hid"},
                 "why": "{سَوْفَ} changes nothing: rafʿ. Hidden damma on the {ي}."},
                {"s": "لَنْ [أَسْكُتَ]", "gloss": "I will not be silent", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "After {لَنْ}: naṣb, fatha."},
            ],
        },
        # 9 · course review: nouns of Stages 5-7 with a present verb
        {
            "title": "Course review: iʿrāb of the whole sentence",
            "prompt": "إِنَّ المُعَلِّمِينَ يَشْرَحُونَ الدُّرُوسَ لِلطَّالِبَاتِ.",
            "en": "The teachers explain the lessons to the female students.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PART, IISM, VERB, OBJ, PREP]},
                {"key": "sign", "label": "Sign", "options": [FIXED, YA, NUN, FAT, KAS]},
            ],
            "rows": [
                {"s": "إِنَّ", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A particle like a verb, fixed on fatha."},
                {"s": "المُعَلِّمِينَ", "ans": {"job": "iism", "sign": "ya"},
                 "why": "{اِسْمُ إِنَّ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "يَشْرَحُونَ", "ans": {"job": "verb", "sign": "nun"},
                 "why": "No particle of naṣb or jazm: rafʿ. A five verb: the nūn stays. The verb sentence is inna's information."},
                {"s": "الدُّرُوسَ", "ans": {"job": "obj", "sign": "fat"},
                 "why": "What they explain: object. A broken plural takes fatha."},
                {"s": "لِلطَّالِبَاتِ", "ans": {"job": "prep", "sign": "kas"},
                 "why": "{الطَّالِبَاتِ} after {لِـ}: jarr, kasra. A sound feminine plural."},
            ],
        },
        # 10 · course review: job and sign of nouns
        {
            "title": "Course review: job and sign of the noun",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, KISM, OBJ, PREP]},
                {"key": "sign", "label": "Sign", "options": [WAW, ALIF, YA, FAT, KAS, HID]},
            ],
            "rows": [
                {"s": "أَرَى [أَخَاكَ] فِي السُّوقِ", "gloss": "I see your brother in the market", "ans": {"job": "obj", "sign": "alif"},
                 "why": "Object, naṣb. One of the five nouns with an owner: sign alif."},
                {"s": "نُصَلِّي فِي [مَسَاجِدَ] كَثِيرَةٍ", "gloss": "we pray in many mosques", "ans": {"job": "prep", "sign": "fat"},
                 "why": "After {فِي}: jarr. A diptote with no {ال}: fatha in place of kasra."},
                {"s": "يَشْكُرُ المُدِيرُ [المُدَرِّسَاتِ]", "gloss": "the headmaster thanks the female teachers", "ans": {"job": "obj", "sign": "kas"},
                 "why": "Object, naṣb. A sound feminine plural: kasra in place of fatha."},
                {"s": "يَجْلِسُ [المُحَامِي] فِي المَكْتَبِ", "gloss": "the lawyer sits in the office", "ans": {"job": "doer", "sign": "hid"},
                 "why": "Doer, rafʿ. A manqūṣ noun: hidden damma on the {ي}."},
                {"s": "نُسَلِّمُ عَلَى [المُهَنْدِسَيْنِ]", "gloss": "we greet the two engineers", "ans": {"job": "prep", "sign": "ya"},
                 "why": "After {عَلَى}: jarr. A dual: sign yāʾ."},
                {"s": "كَانَ [المُسْلِمُونَ] يَصُومُونَ", "gloss": "the Muslims used to fast", "ans": {"job": "kism", "sign": "waw"},
                 "why": "{اِسْمُ كَانَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
            ],
        },
    ],

    "homework": [],
}
