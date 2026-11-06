# Stage 8, Unit 6: Two verbs in jazm (condition)

# Canonical options (copied from STAGES_5_8_SPEC.md)
DAM = {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
FAT = {"k": "fat",   "label": "Fatha · فَتْحَةٌ",                "color": "pink"}
KAS = {"k": "kas",   "label": "Kasra · كَسْرَةٌ",                "color": "green"}
SUK = {"k": "suk",   "label": "Sukūn · سُكُونٌ",                 "color": "navy"}
NUN = {"k": "nun",   "label": "Nūn stays · ثُبُوتُ النُّونِ",        "color": "olive"}
DROP = {"k": "drop",  "label": "Nūn drops · حَذْفُ النُّونِ",         "color": "orange"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ",                  "color": "grey"}

RAF = {"k": "raf",  "label": "Rafʿ · رَفْعٌ",   "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ",  "color": "pink"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ",   "color": "green"}
JAZM = {"k": "jazm", "label": "Jazm · جَزْمٌ",  "color": "navy"}

PREP = {"k": "prep",  "label": "After a preposition · اِسْمٌ مَجْرُورٌ",    "color": "green"}

# Roles in a condition sentence (new in this unit)
CW = {"k": "cw", "label": "Condition word · أَدَاةُ الشَّرْطِ", "color": "navy"}
CV = {"k": "cv", "label": "Condition verb · فِعْلُ الشَّرْطِ", "color": "teal"}
AV = {"k": "av", "label": "Answer verb · جَوَابُ الشَّرْطِ", "color": "purple"}

OK = {"k": "ok", "label": "Correct", "color": "green"}
BAD = {"k": "bad", "label": "Has a mistake", "color": "red"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s8-condition",
    "order": 6,
    "title": "Two verbs in jazm",
    "ar": "جَزْمُ فِعْلَيْنِ",
    "blurb": "إِنْ، مَنْ and مَا of condition put two present verbs in jazm: the condition verb and the answer verb.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 8 · UNIT 6", "title": "If you study, you succeed",
         "text": "A condition sentence has two verbs. One word at the start puts both of them in jazm.",
         "wm": "الشَّرْطُ"},

        {"t": "h2", "text": "Three parts of a condition sentence"},
        {"t": "examples", "items": [
            {"ar": "إِنْ تَدْرُسْ تَنْجَحْ.", "en": "If you study, you succeed."},
        ]},
        {"t": "cols", "items": [
            {"color": "navy", "title": "Condition word", "ar": "أَدَاةُ الشَّرْطِ",
             "text": "{إِنْ} \"if\". It is fixed."},
            {"color": "teal", "title": "Condition verb", "ar": "فِعْلُ الشَّرْطِ",
             "text": "The first verb: {تَدْرُسْ}. Jazm."},
            {"color": "purple", "title": "Answer verb", "ar": "جَوَابُ الشَّرْطِ",
             "text": "The second verb: {تَنْجَحْ}. Jazm."},
        ]},
        {"t": "rule", "color": "navy", "title": "One word, two verbs in jazm",
         "text": "{إِنْ} puts the condition verb and the answer verb in jazm. The signs are the ones you know: sukūn, or the nūn drops."},

        {"t": "h2", "text": "The signs: sukūn or nūn drops"},
        {"t": "table", "head": ["Sentence", "Condition verb", "Answer verb", "Sign"], "rows": [
            ["إِنْ تَدْرُسْ تَنْجَحْ.", "تَدْرُسْ", "تَنْجَحْ", "sukūn · sukūn"],
            ["إِنْ يَدْرُسْ خَالِدٌ يَنْجَحْ.", "يَدْرُسْ", "يَنْجَحْ", "sukūn · sukūn"],
            ["إِنْ تَجْتَهِدُوا تَنْجَحُوا.", "تَجْتَهِدُوا", "تَنْجَحُوا", "nūn drops · nūn drops"],
            ["إِنْ تَدْرُسِي تَنْجَحِي.", "تَدْرُسِي", "تَنْجَحِي", "nūn drops · nūn drops"],
            ["إِنْ تَدْرُسَا تَنْجَحَا.", "تَدْرُسَا", "تَنْجَحَا", "nūn drops · nūn drops"],
            ["إِنْ تَسْأَلْ أُخْبِرْكَ.", "تَسْأَلْ", "أُخْبِرْكَ", "sukūn · sukūn"],
        ]},
        {"t": "p", "text": "The two verbs do not need the same person: {إِنْ تَسْأَلْ أُخْبِرْكَ} \"If you ask, I will tell you.\""},
        {"t": "tip", "text": "With the nūn of women the verbs stay fixed: {إِنْ تَدْرُسْنَ تَنْجَحْنَ}. Their place is jazm."},

        {"t": "h2", "text": "مَنْ and مَا of condition"},
        {"t": "p", "text": "Two more words work like {إِنْ}. They are fixed nouns. Each one puts two verbs in jazm."},
        {"t": "table", "head": ["Word", "Meaning", "Example", "In English"], "rows": [
            ["إِنْ", "if", "إِنْ تَدْرُسْ تَنْجَحْ.", "If you study, you succeed."],
            ["مَنْ", "whoever (people)", "مَنْ يَجْتَهِدْ يَنْجَحْ.", "Whoever works hard succeeds."],
            ["مَا", "whatever (things)", "مَا تَأْكُلْ آكُلْ.", "Whatever you eat, I eat."],
        ]},
        {"t": "examples", "items": [
            {"ar": "وَمَا تَفْعَلُوا مِنْ خَيْرٍ يَعْلَمْهُ اللَّهُ", "en": "And whatever good you do, Allah knows it. (al-Baqara 2:197)",
             "note": "{مَا} of condition. {تَفْعَلُوا}: the nūn drops. {يَعْلَمْهُ}: sukūn, then the pronoun {هُ}."},
        ]},

        {"t": "h2", "text": "Condition word or question word?"},
        {"t": "p", "text": "{مَنْ} and {مَا} can also ask a question. Then there is one verb, and it stays in rafʿ."},
        {"t": "table", "head": ["Question · rafʿ", "Condition · jazm"], "rows": [
            ["{مَنْ يَكْتُبُ؟} Who is writing?", "{مَنْ يَكْتُبْ يَتَعَلَّمْ.} Whoever writes learns."],
            ["{مَا تَأْكُلُ؟} What are you eating?", "{مَا تَأْكُلْ آكُلْ.} Whatever you eat, I eat."],
        ]},
        {"t": "rule", "color": "teal", "title": "The test",
         "text": "Can you say \"whoever\" or \"whatever\", and is there a second verb that answers the first? Then it is a condition, and both verbs are in jazm."},
        {"t": "tip", "text": "Do not mix up {إِنْ} and {أَنْ}. {إِنْ} \"if\" gives jazm to two verbs. {أَنْ} \"to\" gives naṣb to one verb: {أُرِيدُ أَنْ أَذْهَبَ}."},

        {"t": "h2", "text": "Worked examples"},
        {"t": "examples", "items": [
            {"ar": "إِنْ تَدْرُسْ تَنْجَحْ.", "en": "If you study, you succeed.",
             "note": "{إِنْ}: {حَرْفُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ}. {تَدْرُسْ}: {فِعْلُ الشَّرْطِ مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ السُّكُونُ}. {تَنْجَحْ}: {جَوَابُ الشَّرْطِ مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ السُّكُونُ}."},
            {"ar": "إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ", "en": "If you help (the cause of) Allah, He will help you. (Muḥammad 47:7)",
             "note": "{تَنْصُرُوا}: {فِعْلُ الشَّرْطِ مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الأَفْعَالِ الخَمْسَةِ}. {يَنْصُرْكُمْ}: {جَوَابُ الشَّرْطِ مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ السُّكُونُ}."},
            {"ar": "مَنْ يَجْتَهِدْ يَنْجَحْ.", "en": "Whoever works hard succeeds.",
             "note": "{مَنْ}: {اِسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ}. {يَجْتَهِدْ} and {يَنْجَحْ}: both in jazm with sukūn."},
        ]},
        {"t": "tip", "text": "In this unit the answer is always a plain present verb. Other kinds of answer come later."},

        {"t": "summary", "title": "In short", "items": [
            "A condition sentence: condition word + condition verb + answer verb.",
            "{إِنْ} \"if\", {مَنْ} \"whoever\", {مَا} \"whatever\" put both verbs in jazm.",
            "Signs: sukūn ({إِنْ تَدْرُسْ تَنْجَحْ}) or nūn drops ({إِنْ تَجْتَهِدُوا تَنْجَحُوا}).",
            "The condition words are fixed. {إِنْ} is a particle; {مَنْ} and {مَا} are nouns.",
            "A question with {مَنْ} or {مَا} has one verb in rafʿ: {مَنْ يَكْتُبُ؟}",
        ]},
    ],

    "practice": [
        {
            "title": "What is the word in brackets?",
            "fields": [{"key": "role", "label": "Part", "options": [CW, CV, AV]}],
            "rows": [
                {"s": "[إِنْ] تَدْرُسْ تَنْجَحْ.", "gloss": "If you study, you succeed.", "ans": {"role": "cw"},
                 "why": "{إِنْ} \"if\" is the condition word."},
                {"s": "إِنْ [تَدْرُسْ] تَنْجَحْ.", "gloss": "If you study, you succeed.", "ans": {"role": "cv"},
                 "why": "The first verb after {إِنْ} is the condition verb."},
                {"s": "إِنْ تَدْرُسْ [تَنْجَحْ].", "gloss": "If you study, you succeed.", "ans": {"role": "av"},
                 "why": "The second verb is the answer verb."},
                {"s": "[مَنْ] يَجْتَهِدْ يَنْجَحْ.", "gloss": "Whoever works hard succeeds.", "ans": {"role": "cw"},
                 "why": "{مَنْ} \"whoever\" is the condition word."},
                {"s": "مَنْ يَجْتَهِدْ [يَنْجَحْ].", "gloss": "Whoever works hard succeeds.", "ans": {"role": "av"},
                 "why": "The second verb answers the first."},
                {"s": "مَا [تَأْكُلْ] آكُلْ.", "gloss": "Whatever you eat, I eat.", "ans": {"role": "cv"},
                 "why": "The first verb after {مَا} is the condition verb."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "إِنْ تَدْرُسْ ___.", "gloss": "If you study, you succeed.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَنْجَحْ", "تَنْجَحُ", "تَنْجَحَ")},
                 "why": "The answer verb is in jazm too: sukūn."},
                {"s": "إِنْ ___ تَنْجَحُوا.", "gloss": "If you (all) work hard, you succeed.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَجْتَهِدُونَ", "تَجْتَهِدُوا", "تَجْتَهِدْ")},
                 "why": "The condition verb is in jazm. {تَجْتَهِدُونَ} loses its nūn: {تَجْتَهِدُوا}."},
                {"s": "مَنْ يَصْبِرْ ___.", "gloss": "Whoever is patient wins.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَظْفَرُ", "يَظْفَرَ", "يَظْفَرْ")},
                 "why": "{مَنْ} of condition: the answer verb is in jazm with sukūn."},
                {"s": "إِنْ ___ أَجْلِسْ.", "gloss": "If you sit, I sit.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَجْلِسْ", "تَجْلِسُ", "تَجْلِسِينَ")},
                 "why": "The condition verb is in jazm: {تَجْلِسْ}. {تَجْلِسِينَ} still has its nūn."},
                {"s": "مَا تَشْرَبْ ___.", "gloss": "Whatever you drink, I drink.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَشْرَبُ", "أَشْرَبْ", "أَشْرَبَ")},
                 "why": "The answer verb is in jazm: {أَشْرَبْ}."},
                {"s": "إِنْ تَذْهَبِي إِلَى السُّوقِ ___.", "gloss": "If you (f.) go to the market, you will get tired.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَتْعَبِينَ", "تَتْعَبْ", "تَتْعَبِي")},
                 "why": "To a woman: {تَتْعَبِينَ}. In jazm the nūn drops: {تَتْعَبِي}."},
            ],
        },
        {
            "title": "Part and sign",
            "prompt": "إِنْ تَجْتَهِدُوا فِي الدَّرْسِ تَنْجَحُوا.",
            "en": "If you (all) work hard in the lesson, you succeed.",
            "fields": [
                {"key": "role", "label": "Part", "options": [CW, CV, AV, PREP]},
                {"key": "sign", "label": "Sign", "options": [SUK, KAS, DROP, FIXED]},
            ],
            "rows": [
                {"s": "إِنْ", "ans": {"role": "cw", "sign": "fixed"},
                 "why": "{حَرْفُ شَرْطٍ جَازِمٌ}, fixed on sukūn."},
                {"s": "تَجْتَهِدُوا", "ans": {"role": "cv", "sign": "drop"},
                 "why": "The condition verb, in jazm. A five verb: the nūn drops."},
                {"s": "الدَّرْسِ", "ans": {"role": "prep", "sign": "kas"},
                 "why": "After {فِي}: jarr with kasra."},
                {"s": "تَنْجَحُوا", "ans": {"role": "av", "sign": "drop"},
                 "why": "The answer verb, in jazm. A five verb: the nūn drops."},
            ],
        },
        {
            "title": "Iʿrāb: case and sign",
            "prompt": "إِنْ يَدْرُسْ خَالِدٌ دُرُوسَهُ يَنْجَحْ.",
            "en": "If Khālid studies his lessons, he succeeds.",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR, JAZM]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, SUK, DROP]},
            ],
            "rows": [
                {"s": "يَدْرُسْ", "ans": {"case": "jazm", "sign": "suk"},
                 "why": "The condition verb: jazm with sukūn."},
                {"s": "خَالِدٌ", "ans": {"case": "raf", "sign": "dam"},
                 "why": "The doer: {فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}."},
                {"s": "دُرُوسَهُ", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "The object: naṣb. A broken plural takes fatha."},
                {"s": "يَنْجَحْ", "ans": {"case": "jazm", "sign": "suk"},
                 "why": "The answer verb: jazm with sukūn."},
            ],
        },
        {
            "title": "Which case and sign does the verb take here?",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, JAZM]},
                {"key": "sign", "label": "Sign", "options": [DAM, SUK, NUN, DROP]},
            ],
            "rows": [
                {"s": "إِنْ [تَسْأَلُوا] تَتَعَلَّمُوا", "gloss": "if you (all) ask, you learn", "ans": {"case": "jazm", "sign": "drop"},
                 "why": "Condition verb, jazm. A five verb: the nūn drops."},
                {"s": "إِنْ تَسْأَلْ [تَتَعَلَّمْ]", "gloss": "if you ask, you learn", "ans": {"case": "jazm", "sign": "suk"},
                 "why": "Answer verb, jazm with sukūn."},
                {"s": "الطُّلَّابُ [يَسْأَلُونَ] المُدَرِّسَ", "gloss": "the students ask the teacher", "ans": {"case": "raf", "sign": "nun"},
                 "why": "No condition word and no particle: rafʿ. The nūn stays."},
                {"s": "مَنْ [يَكْذِبْ] يَخْسَرْ", "gloss": "whoever lies loses", "ans": {"case": "jazm", "sign": "suk"},
                 "why": "Condition verb after {مَنْ}: jazm with sukūn."},
                {"s": "إِنْ تَحْضُرَا [تَفْهَمَا]", "gloss": "if you two come, you understand", "ans": {"case": "jazm", "sign": "drop"},
                 "why": "Answer verb, jazm. {تَفْهَمَانِ} loses its nūn."},
                {"s": "هِيَ [تَفْهَمُ] الدَّرْسَ", "gloss": "she understands the lesson", "ans": {"case": "raf", "sign": "dam"},
                 "why": "No particle before it: rafʿ with damma."},
            ],
        },
        {
            "title": "Condition or not? Choose the form",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "مَنْ ___ الآنَ؟", "gloss": "Who is sitting now?", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَجْلِسُ", "يَجْلِسْ")},
                 "why": "A question with one verb. No condition, so rafʿ."},
                {"s": "مَنْ ___ يَتَعَلَّمْ.", "gloss": "Whoever asks learns.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَسْأَلُ", "يَسْأَلْ", "يَسْأَلَ")},
                 "why": "\"Whoever\" with a second verb: a condition. Both verbs in jazm."},
                {"s": "مَا ___؟", "gloss": "What are you eating?", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَأْكُلُ", "تَأْكُلْ")},
                 "why": "A question with one verb: rafʿ."},
                {"s": "إِنْ ___ أَقْرَأْ.", "gloss": "If you read, I read.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَقْرَأُ", "تَقْرَأَ", "تَقْرَأْ")},
                 "why": "{إِنْ} of condition: jazm with sukūn."},
                {"s": "أُحِبُّ أَنْ ___.", "gloss": "I like to read.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَقْرَأْ", "أَقْرَأَ", "أَقْرَأُ")},
                 "why": "{أَنْ} \"to\" gives naṣb with fatha (Unit 4). It is not {إِنْ}."},
            ],
        },
    ],

    "homework": [
        {
            "title": "What is the word in brackets?",
            "fields": [{"key": "role", "label": "Part", "options": [CW, CV, AV]}],
            "rows": [
                {"s": "إِنْ [تَسْأَلُوا] تَعْرِفُوا.", "gloss": "If you (all) ask, you will know.", "ans": {"role": "cv"},
                 "why": "The first verb after {إِنْ}: the condition verb."},
                {"s": "إِنْ تَسْأَلُوا [تَعْرِفُوا].", "gloss": "If you (all) ask, you will know.", "ans": {"role": "av"},
                 "why": "The second verb: the answer verb."},
                {"s": "[مَا] تَدْرُسْ تَعْرِفْ.", "gloss": "Whatever you study, you know.", "ans": {"role": "cw"},
                 "why": "{مَا} \"whatever\" is the condition word."},
                {"s": "مَنْ [يَتَعَلَّمْ] يَعْرِفْ.", "gloss": "Whoever learns knows.", "ans": {"role": "cv"},
                 "why": "The first verb after {مَنْ}: the condition verb."},
                {"s": "إِنْ يَحْضُرْ أَبُوكَ [أُكْرِمْهُ].", "gloss": "If your father comes, I will honour him.", "ans": {"role": "av"},
                 "why": "The second verb, with the pronoun {هُ}: the answer verb."},
                {"s": "[مَنْ] يَصْدُقْ يَنْجَحْ.", "gloss": "Whoever tells the truth succeeds.", "ans": {"role": "cw"},
                 "why": "{مَنْ} \"whoever\" is the condition word."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "إِنْ تَلْعَبَا فِي الشَّارِعِ ___.", "gloss": "If you two play in the street, you will get tired.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَتْعَبَا", "تَتْعَبَانِ", "تَتْعَبْ")},
                 "why": "For two: {تَتْعَبَانِ}. As the answer verb in jazm: {تَتْعَبَا}."},
                {"s": "مَنْ ___ دُرُوسَهُ يَنْجَحْ.", "gloss": "Whoever reviews his lessons succeeds.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يُذَاكِرُ", "يُذَاكِرْ", "يُذَاكِرَ")},
                 "why": "The condition verb after {مَنْ}: jazm with sukūn."},
                {"s": "إِنْ ___ تَفْهَمِي.", "gloss": "If you (f.) ask, you will understand.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَسْأَلِينَ", "تَسْأَلْ", "تَسْأَلِي")},
                 "why": "To a woman: {تَسْأَلِينَ}. In jazm the nūn drops: {تَسْأَلِي}."},
                {"s": "إِنْ يَجْتَهِدْ أَخُوكَ ___.", "gloss": "If your brother works hard, he succeeds.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَنْجَحْ", "يَنْجَحُ", "يَنْجَحَا")},
                 "why": "The answer verb for \"he\": jazm with sukūn."},
                {"s": "مَا ___ أَفْعَلْ.", "gloss": "Whatever you do, I do.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَفْعَلُ", "تَفْعَلْ", "تَفْعَلِينَ")},
                 "why": "The condition verb after {مَا}: jazm with sukūn."},
                {"s": "إِنْ ___ إِلَى المَسْجِدِ نَذْهَبْ مَعَكُمْ.", "gloss": "If you (all) go to the mosque, we go with you.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَذْهَبُوا", "تَذْهَبُونَ", "تَذْهَبْ")},
                 "why": "\"You all\" is {تَذْهَبُونَ}. In jazm: {تَذْهَبُوا}."},
            ],
        },
        {
            "title": "Iʿrāb: case and sign",
            "prompt": "إِنْ تَحْفَظُوا الدَّرْسَ فِي البَيْتِ تَفْهَمُوهُ فِي الفَصْلِ.",
            "en": "If you (all) learn the lesson at home, you will understand it in class.",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR, JAZM]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, SUK, DROP]},
            ],
            "rows": [
                {"s": "تَحْفَظُوا", "ans": {"case": "jazm", "sign": "drop"},
                 "why": "The condition verb, jazm. A five verb: the nūn drops."},
                {"s": "الدَّرْسَ", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "Object: naṣb with fatha."},
                {"s": "البَيْتِ", "ans": {"case": "jarr", "sign": "kas"},
                 "why": "After {فِي}: jarr with kasra."},
                {"s": "تَفْهَمُوهُ", "ans": {"case": "jazm", "sign": "drop"},
                 "why": "The answer verb, jazm. The nūn drops, then the pronoun {هُ} is added."},
                {"s": "الفَصْلِ", "ans": {"case": "jarr", "sign": "kas"},
                 "why": "After {فِي}: jarr with kasra."},
            ],
        },
        {
            "title": "Part and sign",
            "prompt": "إِنْ تُسَافِرَا أُسَافِرْ مَعَكُمَا.",
            "en": "If you two travel, I will travel with you.",
            "fields": [
                {"key": "role", "label": "Part", "options": [CW, CV, AV]},
                {"key": "sign", "label": "Sign", "options": [SUK, NUN, DROP, FIXED]},
            ],
            "rows": [
                {"s": "إِنْ", "ans": {"role": "cw", "sign": "fixed"},
                 "why": "The condition word, a particle fixed on sukūn."},
                {"s": "تُسَافِرَا", "ans": {"role": "cv", "sign": "drop"},
                 "why": "The condition verb. {تُسَافِرَانِ} loses its nūn in jazm."},
                {"s": "أُسَافِرْ", "ans": {"role": "av", "sign": "suk"},
                 "why": "The answer verb for \"I\": jazm with sukūn."},
            ],
        },
        {
            "title": "Read the meaning, choose the form",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "مَنْ ___ فِي هَذَا البَيْتِ؟", "gloss": "Who lives in this house?", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَسْكُنُ", "يَسْكُنْ")},
                 "why": "A question with one verb. No condition: rafʿ."},
                {"s": "مَنْ ___ يَخْسَرْ.", "gloss": "Whoever is lazy loses.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَكْسَلُ", "يَكْسَلَ", "يَكْسَلْ")},
                 "why": "\"Whoever\" with an answer verb: the condition verb is in jazm."},
                {"s": "مَا ___ الآنَ؟", "gloss": "What are you (all) writing now?", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَكْتُبُوا", "تَكْتُبُونَ")},
                 "why": "A question: rafʿ. A five verb in rafʿ keeps its nūn."},
                {"s": "مَا ___ أَكْتُبْ.", "gloss": "Whatever you (all) write, I write.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَكْتُبُوا", "تَكْتُبُونَ", "تَكْتُبُ")},
                 "why": "A condition: jazm. The nūn drops: {تَكْتُبُوا}."},
                {"s": "إِنْ ___ تَرْسُبُوا.", "gloss": "If you (all) are lazy, you fail.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَكْسَلُونَ", "تَكْسَلُوا", "تَكْسَلْ")},
                 "why": "The condition verb is in jazm. For \"you all\": {تَكْسَلُوا}."},
            ],
        },
        {
            "title": "Correct, or does it have a mistake?",
            "fields": [{"key": "chk", "label": "Sentence", "options": [OK, BAD]}],
            "rows": [
                {"s": "إِنْ تَدْرُسُ تَنْجَحُ.", "ans": {"chk": "bad"},
                 "why": "Both verbs must be in jazm: {إِنْ تَدْرُسْ تَنْجَحْ}."},
                {"s": "مَنْ يَسْأَلْ يَتَعَلَّمْ.", "ans": {"chk": "ok"},
                 "why": "Both verbs are in jazm with sukūn."},
                {"s": "إِنْ تَجْتَهِدُونَ تَنْجَحُونَ.", "ans": {"chk": "bad"},
                 "why": "The nūn must drop in jazm: {إِنْ تَجْتَهِدُوا تَنْجَحُوا}."},
                {"s": "مَنْ يَعْمَلْ يَأْكُلْ.", "ans": {"chk": "ok"},
                 "why": "Both verbs are in jazm with sukūn."},
                {"s": "إِنْ تَذْهَبِي أَذْهَبْ.", "ans": {"chk": "ok"},
                 "why": "{تَذْهَبِي} lost its nūn, {أَذْهَبْ} has sukūn. Both are in jazm."},
                {"s": "إِنْ تَحْضُرَانِ أَحْضُرْ.", "ans": {"chk": "bad"},
                 "why": "The condition verb must lose its nūn: {إِنْ تَحْضُرَا أَحْضُرْ}."},
            ],
        },
    ],
}
