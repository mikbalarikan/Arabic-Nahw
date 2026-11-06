# Stage 5: class exercise (review of units 1-7, done together in class before the Stage 5 quiz)

# Canonical options (STAGES_5_8_SPEC.md)
DAM = {"k": "dam", "label": "Damma · ضَمَّةٌ", "color": "red"}
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
ALIF = {"k": "alif", "label": "Alif · الأَلِفُ", "color": "teal"}
WAW = {"k": "waw", "label": "Wāw · الوَاوُ", "color": "blue"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}

RAF = {"k": "raf", "label": "Rafʿ · رَفْعٌ", "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ", "color": "pink"}

DUAL = {"k": "dual", "label": "Dual · مُثَنًّى", "color": "teal"}
SMP = {"k": "smp", "label": "Sound m. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ", "color": "blue"}
SFP = {"k": "sfp", "label": "Sound f. plural · جَمْعُ مُؤَنَّثٍ سَالِمٌ", "color": "pink"}
BRK = {"k": "brk", "label": "Broken plural · جَمْعُ تَكْسِيرٍ", "color": "purple"}
FIVE = {"k": "five", "label": "Five nouns · الأَسْمَاءُ الخَمْسَةُ", "color": "gold"}
HIDV = {"k": "hidv", "label": "Hidden vowel", "color": "brown"}

TOPIC = {"k": "topic", "label": "Topic · مُبْتَدَأٌ", "color": "gold"}
INFO = {"k": "info", "label": "Information · خَبَرٌ", "color": "red"}
VERB = {"k": "verb", "label": "Verb · فِعْلٌ", "color": "navy"}
DOER = {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"}
NAIB = {"k": "naib", "label": "Doer stand-in · نَائِبُ الفَاعِلِ", "color": "orange"}
KISM = {"k": "kism", "label": "Kāna's noun · اِسْمُ كَانَ", "color": "gold"}
KKHAB = {"k": "kkhab", "label": "Kāna's information · خَبَرُ كَانَ", "color": "red"}
IISM = {"k": "iism", "label": "Inna's noun · اِسْمُ إِنَّ", "color": "gold"}
IKHAB = {"k": "ikhab", "label": "Inna's information · خَبَرُ إِنَّ", "color": "red"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
AND = {"k": "and", "label": "After وَ (and) · مَعْطُوفٌ", "color": "blue"}
BADAL = {"k": "badal", "label": "Substitute · بَدَلٌ", "color": "grey"}
PART = {"k": "part", "label": "Particle · حَرْفٌ", "color": "grey"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s5-exercise",
    "order": 8,
    "kind": "exercise",
    "title": "Stage 5 class exercise",
    "ar": "تَمْرِينُ المَرْفُوعَاتِ",
    "blurb": "Ten mixed cards on all seven rafʿ jobs and the four signs of rafʿ, done together in class before the Stage 5 quiz.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 5 · CLASS EXERCISE", "title": "All the rafʿ jobs together",
         "text": "Ten cards that mix every Stage 5 unit. We do them together in class, before the Stage 5 quiz.",
         "wm": "المَرْفُوعَاتُ"},

        {"t": "h2", "text": "How we do it in class"},
        {"t": "p", "text": "Work in pairs, or come to the board. One student reads the sentence aloud. For each word, say the job, the case and the sign. The partner says why, or corrects it. Then swap."},
        {"t": "rule", "color": "gold", "title": "Three steps",
         "text": "Find the job. The job gives the case. The kind of noun gives the sign."},
        {"t": "tip", "text": "Say the full sentence out loud for at least one word in every card: {فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
        {"t": "tip", "text": "If a card is hard, open its unit and read the table again before the quiz."},

        {"t": "h2", "text": "The seven topics"},
        {"t": "cols", "items": [
            {"color": "red", "title": "1. Signs of rafʿ", "ar": "عَلَامَاتُ الرَّفْعِ",
             "text": "Damma, alif ({ـَانِ}), wāw ({ـُونَ}، {أَبُوكَ}), hidden damma ({الفَتَى}، {القَاضِي}، {كِتَابِي})."},
            {"color": "gold", "title": "2. Topic and information", "ar": "المُبْتَدَأُ وَالخَبَرُ",
             "text": "Both rafʿ. The information agrees: {الكُتُبُ جَدِيدَةٌ}، {المُسْلِمُونَ صَادِقُونَ}."},
            {"color": "orange", "title": "3. The doer", "ar": "الفَاعِلُ",
             "text": "The verb stays singular: {جَاءَ المُسْلِمُونَ}. Feminine {ت}: {حَضَرَتِ الطَّالِبَاتُ}."},
            {"color": "orange", "title": "4. The doer stand-in", "ar": "نَائِبُ الفَاعِلِ",
             "text": "Passive {فُعِلَ}: {كُتِبَ الدَّرْسُ}. The object moves into rafʿ."},
            {"color": "gold", "title": "5. Kāna and her sisters", "ar": "كَانَ وَأَخَوَاتُهَا",
             "text": "Kāna's noun is rafʿ, its information naṣb: {كَانَ البَيْتُ كَبِيرًا}."},
            {"color": "red", "title": "6. Inna and her sisters", "ar": "إِنَّ وَأَخَوَاتُهَا",
             "text": "Inna's noun is naṣb, its information rafʿ: {إِنَّ الدَّرْسَ سَهْلٌ}."},
            {"color": "grey", "title": "7. Followers", "ar": "التَّوَابِعُ",
             "text": "Adjective, after {وَ}, emphasis, substitute. Copy the case, keep your own sign."},
        ]},

        {"t": "h2", "text": "One table for every sign"},
        {"t": "table", "head": ["Group", "Example in rafʿ", "Sign"], "rows": [
            ["Singular, broken plural, sound f. plural", "الرَّجُلُ، الرِّجَالُ، المُسْلِمَاتُ", "damma"],
            ["Diptote", "زَيْنَبُ، مَسَاجِدُ", "damma, no tanween"],
            ["Dual", "الرَّجُلَانِ", "alif"],
            ["Sound m. plural", "المُسْلِمُونَ", "wāw"],
            ["Five nouns", "أَبُوكَ، ذُو مَالٍ", "wāw"],
            ["Maqṣūr, manqūṣ, noun + ـي \"my\"", "الفَتَى، القَاضِي، كِتَابِي", "hidden damma"],
            ["Fixed word", "هُوَ، هَذَا، كَتَبُوا", "fixed, in the place of rafʿ"],
        ]},

        {"t": "summary", "title": "Remember", "items": [
            "Seven rafʿ jobs: Topic, Information, doer, doer stand-in, kāna's noun, inna's information, and a follower of a rafʿ word.",
            "The job gives the case. The kind of noun gives the sign.",
            "Before its doer or stand-in, the verb stays singular. It takes {ت} for a feminine noun.",
            "Kāna: noun rafʿ, information naṣb. Inna: noun naṣb, information rafʿ.",
            "A follower copies the case of the word before it. Its own group gives the sign: {جَاءَ الطُّلَّابُ المُجْتَهِدُونَ}.",
            "A fixed word in a rafʿ job shows no sign. It is in the place of rafʿ.",
        ]},
    ],

    "practice": [
        # 1 · unit 1: group and sign
        {
            "title": "Which group is it? Which sign does it take in rafʿ?",
            "fields": [
                {"key": "kind", "label": "Group", "options": [DUAL, SMP, SFP, BRK, FIVE, HIDV]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID]},
            ],
            "rows": [
                {"s": "المُوَظَّفُونَ", "gloss": "the employees", "ans": {"kind": "smp", "sign": "waw"},
                 "why": "{مُوَظَّفٌ} + {ـُونَ}: a sound m. plural. Wāw."},
                {"s": "الحَقِيبَتَانِ", "gloss": "the two bags", "ans": {"kind": "dual", "sign": "alif"},
                 "why": "{حَقِيبَةٌ}: the {ة} becomes {ت}, then {ـَانِ}. A dual: alif."},
                {"s": "الشَّجَرَاتُ", "gloss": "the trees", "ans": {"kind": "sfp", "sign": "dam"},
                 "why": "{شَجَرَةٌ} → {شَجَرَاتٌ}: a sound f. plural. Damma."},
                {"s": "الأَقْلَامُ", "gloss": "the pens", "ans": {"kind": "brk", "sign": "dam"},
                 "why": "{قَلَمٌ} → {أَقْلَامٌ}: the shape changed. A broken plural: damma."},
                {"s": "أَخُوهَا", "gloss": "her brother", "ans": {"kind": "five", "sign": "waw"},
                 "why": "{أَخٌ} with an owner ({ـهَا}): a five noun. Wāw."},
                {"s": "الرَّاعِي", "gloss": "the shepherd", "ans": {"kind": "hidv", "sign": "hid"},
                 "why": "Manqūṣ: it ends in {ي} after kasra. Hidden damma."},
            ],
        },
        # 2 · unit 2: topic and information
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "مُوَظَّفُو الشَّرِكَةِ وَالمُحَامِي مَشْغُولُونَ.",
            "en": "The company's employees and the lawyer are busy.",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, INFO, AND]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID]},
            ],
            "rows": [
                {"s": "مُوَظَّفُو", "gloss": "the employees of", "ans": {"job": "topic", "sign": "waw"},
                 "why": "{مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}. The {ن} dropped before the owner."},
                {"s": "المُحَامِي", "gloss": "the lawyer", "ans": {"job": "and", "sign": "hid"},
                 "why": "After {وَ} it copies the Topic's rafʿ. Manqūṣ: hidden damma on the {ي}."},
                {"s": "مَشْغُولُونَ", "gloss": "busy", "ans": {"job": "info", "sign": "waw"},
                 "why": "Men, three or more: a sound m. plural Information. {خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ}."},
            ],
        },
        # 3 · unit 2: agreement of the information
        {
            "title": "Choose the right Information",
            "fields": [{"key": "pick", "label": "Information", "options": []}],
            "rows": [
                {"s": "المُمَرِّضَاتُ ___.", "gloss": "The nurses (f.) are active.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("نَشِيطُونَ", "نَشِيطَتَانِ", "نَشِيطَاتٌ")},
                 "why": "Women, three or more: a sound f. plural with damma."},
                {"s": "الحَدَائِقُ ___.", "gloss": "The gardens are wide.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("وَاسِعُونَ", "وَاسِعَةٌ", "وَاسِعَانِ")},
                 "why": "A plural of things takes a feminine singular Information: {وَاسِعَةٌ}."},
                {"s": "الضُّيُوفُ ___.", "gloss": "The guests are happy.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَسْرُورُونَ", "مَسْرُورٌ", "مَسْرُورَانِ")},
                 "why": "A broken plural of men takes a plural Information: {مَسْرُورُونَ} with wāw."},
                {"s": "الطَّبِيبُ وَالمُمَرِّضُ ___.", "gloss": "The doctor and the nurse are busy.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَشْغُولٌ", "مَشْغُولَانِ", "مَشْغُولُونَ")},
                 "why": "Two men joined with {وَ}: a dual Information with alif."},
                {"s": "أَنْتُمَا ___.", "gloss": "You (two) are students.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("طَالِبَانِ", "طَالِبٌ", "طُلَّابٌ")},
                 "why": "{أَنْتُمَا} is two people: a dual Information, {طَالِبَانِ}."},
            ],
        },
        # 4 · unit 3: verb and doer
        {
            "title": "The doer: which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "___ المُسَافِرُونَ.", "gloss": "The travellers arrived.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("وَصَلَ", "وَصَلُوا", "وَصَلَتْ")},
                 "why": "Before its doer the verb stays singular: {وَصَلَ المُسَافِرُونَ}."},
                {"s": "___ المُمَرِّضَاتُ.", "gloss": "The nurses (f.) went out.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("خَرَجْنَ", "خَرَجَتِ", "خَرَجُوا")},
                 "why": "A singular verb with {ت} for women. Kasra before {ال}: {خَرَجَتِ المُمَرِّضَاتُ}."},
                {"s": "رَجَعَ ___.", "gloss": "The two farmers returned.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الفَلَّاحَيْنِ", "الفَلَّاحُونَ", "الفَلَّاحَانِ")},
                 "why": "Two men, doer in rafʿ: alif. {الفَلَّاحُونَ} is three or more."},
                {"s": "سَافَرَ ___.", "gloss": "Khalid's father travelled.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَبُو خَالِدٍ", "أَبَا خَالِدٍ", "أَبِي خَالِدٍ")},
                 "why": "Doer in rafʿ, a five noun with an owner: wāw."},
                {"s": "___ عَائِشَةُ.", "gloss": "Aisha came.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("جَاءَ", "جَاءَتْ", "جِئْنَ")},
                 "why": "A woman is the doer: add {ت}, {جَاءَتْ عَائِشَةُ}."},
            ],
        },
        # 5 · units 3, 4, 5: pronouns in the place of rafʿ
        {
            "title": "What is the job of this part of the verb?",
            "fields": [{"key": "job", "label": "Job", "options": [DOER, NAIB, KISM, PART]}],
            "rows": [
                {"s": "و in دَخَلُوا", "gloss": "they entered", "ans": {"job": "doer"},
                 "why": "{دَخَلُوا} is active. The {و} \"they\" is the doer, in the place of rafʿ."},
                {"s": "نَا in نُصِرْنَا", "gloss": "we were helped to victory", "ans": {"job": "naib"},
                 "why": "{نُصِرْنَا} has the passive shape. The {نَا} \"we\" is the doer stand-in, in the place of rafʿ."},
                {"s": "ـتُمْ in كُنْتُمْ", "gloss": "you (pl.) were", "ans": {"job": "kism"},
                 "why": "{كُنْتُمْ} = {كَانَ} + {ـتُمْ}. The pronoun is kāna's noun, in the place of rafʿ."},
                {"s": "ـتْ in سُرِقَتِ الحَقِيبَةُ", "gloss": "the bag was stolen", "ans": {"job": "part"},
                 "why": "This {ت} only shows a feminine stand-in. The stand-in is {الحَقِيبَةُ}."},
                {"s": "ي in اُدْخُلِي", "gloss": "enter! (to a woman)", "ans": {"job": "doer"},
                 "why": "An order verb. The {ي} \"you (f.)\" is the doer, in the place of rafʿ."},
                {"s": "ـتِ in سُئِلْتِ", "gloss": "you (f.) were asked", "ans": {"job": "naib"},
                 "why": "{سُئِلْتِ} is passive. The {ـتِ} is the doer stand-in, fixed on kasra."},
            ],
        },
        # 6 · units 3 and 4: doer or stand-in, and the sign
        {
            "title": "Doer or doer stand-in? Which sign?",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, NAIB]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID]},
            ],
            "rows": [
                {"s": "كُسِرَ [الكُرْسِيُّ].", "gloss": "The chair was broken.", "ans": {"job": "naib", "sign": "dam"},
                 "why": "{كُسِرَ} is passive: stand-in. The {ي} has shadda and carries the damma."},
                {"s": "فَهِمَ [الطُّلَّابُ] الدَّرْسَ.", "gloss": "The students understood the lesson.", "ans": {"job": "doer", "sign": "dam"},
                 "why": "{فَهِمَ} is active: doer. A broken plural: damma."},
                {"s": "سُرِقَتِ [السَّيَّارَتَانِ].", "gloss": "The two cars were stolen.", "ans": {"job": "naib", "sign": "alif"},
                 "why": "{سُرِقَتْ} is passive: stand-in. A dual: alif."},
                {"s": "سُئِلَ [اللَّاعِبُونَ].", "gloss": "The players were asked.", "ans": {"job": "naib", "sign": "waw"},
                 "why": "{سُئِلَ} is passive: stand-in. A sound m. plural: wāw."},
                {"s": "شَرِبَ [أَخُو] سَعِيدٍ الشَّايَ.", "gloss": "Saʿid's brother drank the tea.", "ans": {"job": "doer", "sign": "waw"},
                 "why": "{شَرِبَ} is active: doer. A five noun with an owner: wāw."},
                {"s": "نَسِيَ [الفَتَى] الكِتَابَ.", "gloss": "The young man forgot the book.", "ans": {"job": "doer", "sign": "hid"},
                 "why": "{نَسِيَ} is active: doer. Maqṣūr: hidden damma on the alif."},
            ],
        },
        # 7 · unit 5: kāna and her sisters
        {
            "title": "Iʿrāb of the sentence",
            "prompt": "صَارَ أَبُو سَعِيدٍ تَاجِرًا وَأَمْسَى المُسْتَشْفَى هَادِئًا.",
            "en": "Saʿid's father became a merchant, and the hospital became quiet in the evening.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, KISM, KKHAB]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, WAW, HID, FIXED]},
            ],
            "rows": [
                {"s": "صَارَ", "gloss": "became", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A sister of kāna. A past verb, fixed on fatha."},
                {"s": "أَبُو", "gloss": "the father of", "ans": {"job": "kism", "sign": "waw"},
                 "why": "{اِسْمُ صَارَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ}."},
                {"s": "تَاجِرًا", "gloss": "a merchant", "ans": {"job": "kkhab", "sign": "fat"},
                 "why": "What he became: kāna's information, naṣb. A singular: fatha."},
                {"s": "أَمْسَى", "gloss": "became (in the evening)", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A sister of kāna. A past verb, fixed."},
                {"s": "المُسْتَشْفَى", "gloss": "the hospital", "ans": {"job": "kism", "sign": "hid"},
                 "why": "The noun of {أَمْسَى}, rafʿ. Maqṣūr: hidden damma on the alif."},
                {"s": "هَادِئًا", "gloss": "quiet", "ans": {"job": "kkhab", "sign": "fat"},
                 "why": "The information of {أَمْسَى}, naṣb. A singular: fatha."},
            ],
        },
        # 8 · units 5 and 6: kāna or inna
        {
            "title": "Kāna's family or inna's family? Job and case",
            "fields": [
                {"key": "job", "label": "Job", "options": [KISM, KKHAB, IISM, IKHAB]},
                {"key": "case", "label": "Case", "options": [RAF, NASB]},
            ],
            "rows": [
                {"s": "لَيْسَ [المُسَافِرُونَ] مُتْعَبِينَ", "gloss": "The travellers are not tired.", "ans": {"job": "kism", "case": "raf"},
                 "why": "{لَيْسَ} is a sister of kāna. Its noun is rafʿ, with wāw."},
                {"s": "لَعَلَّ [المَطَرَ] قَرِيبٌ", "gloss": "Perhaps the rain is near.", "ans": {"job": "iism", "case": "nasb"},
                 "why": "{لَعَلَّ} is a sister of inna. Its noun is naṣb: {المَطَرَ}."},
                {"s": "ظَلَّ البَحْرُ [هَادِئًا]", "gloss": "The sea stayed calm.", "ans": {"job": "kkhab", "case": "nasb"},
                 "why": "{ظَلَّ} is a sister of kāna. Its information is naṣb: {هَادِئًا}."},
                {"s": "إِنَّ الطَّرِيقَ [قَصِيرٌ]", "gloss": "Indeed, the road is short.", "ans": {"job": "ikhab", "case": "raf"},
                 "why": "Inna's information stays in rafʿ: {قَصِيرٌ}."},
                {"s": "كَانَتِ [الغُرْفَتَانِ] نَظِيفَتَيْنِ", "gloss": "The two rooms were clean.", "ans": {"job": "kism", "case": "raf"},
                 "why": "Kāna's noun is rafʿ. A dual: alif."},
                {"s": "كَأَنَّ [الطِّفْلَ] مَلَكٌ", "gloss": "It is as if the child is an angel.", "ans": {"job": "iism", "case": "nasb"},
                 "why": "{كَأَنَّ} is a sister of inna. Its noun is naṣb: {الطِّفْلَ}."},
            ],
        },
        # 9 · units 6 and 7: inna with a pronoun noun
        {
            "title": "Iʿrāb of the sentence",
            "prompt": "إِنَّهُمْ مُهَنْدِسُونَ مَشْهُورُونَ.",
            "en": "Indeed, they are famous engineers.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PART, IISM, IKHAB, ADJ]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, FIXED]},
            ],
            "rows": [
                {"s": "إِنَّ", "gloss": "indeed", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A particle, fixed on fatha."},
                {"s": "ـهُمْ", "gloss": "they", "ans": {"job": "iism", "sign": "fixed"},
                 "why": "An attached pronoun, fixed on sukūn. It is inna's noun, in the place of naṣb."},
                {"s": "مُهَنْدِسُونَ", "gloss": "engineers", "ans": {"job": "ikhab", "sign": "waw"},
                 "why": "{خَبَرُ إِنَّ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "مَشْهُورُونَ", "gloss": "famous", "ans": {"job": "adj", "sign": "waw"},
                 "why": "It describes {مُهَنْدِسُونَ} and copies its rafʿ. A sound m. plural: wāw."},
            ],
        },
        # 10 · unit 7: followers
        {
            "title": "Iʿrāb of the sentence",
            "prompt": "جَاءَ جَارِي عَلِيٌّ وَالمُهَنْدِسُونَ الكِبَارُ.",
            "en": "My neighbour Ali and the senior engineers came.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, ADJ, AND, BADAL]},
                {"key": "sign", "label": "Sign", "options": [DAM, WAW, HID, FIXED]},
            ],
            "rows": [
                {"s": "جَاءَ", "gloss": "came", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "جَارِي", "gloss": "my neighbour", "ans": {"job": "doer", "sign": "hid"},
                 "why": "Doer, rafʿ. A noun with {ـي} \"my\": hidden damma."},
                {"s": "عَلِيٌّ", "gloss": "Ali", "ans": {"job": "badal", "sign": "dam"},
                 "why": "The same person named again: a substitute, rafʿ. The {ي} has shadda and carries the damma."},
                {"s": "المُهَنْدِسُونَ", "gloss": "the engineers", "ans": {"job": "and", "sign": "waw"},
                 "why": "After {وَ}, joined to the doer, rafʿ. A sound m. plural: wāw."},
                {"s": "الكِبَارُ", "gloss": "the senior", "ans": {"job": "adj", "sign": "dam"},
                 "why": "It describes {المُهَنْدِسُونَ} and copies rafʿ. {كِبَارٌ} is a broken plural: damma."},
            ],
        },
    ],

    "homework": [],
}
