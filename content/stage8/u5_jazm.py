# Stage 8, Unit 5: The present verb in jazm

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

VERB = {"k": "verb",  "label": "Verb · فِعْلٌ",                       "color": "navy"}
DOER = {"k": "doer",  "label": "Doer · فَاعِلٌ",                      "color": "orange"}
PREP = {"k": "prep",  "label": "After a preposition · اِسْمٌ مَجْرُورٌ",    "color": "green"}
PART = {"k": "part",  "label": "Particle · حَرْفٌ",                     "color": "grey"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s8-jazm",
    "order": 5,
    "title": "The present verb in jazm",
    "ar": "جَزْمُ الفِعْلِ المُضَارِعِ",
    "blurb": "After لَمْ، لَمَّا، the لِـ of order and the لَا that forbids, the present verb goes into jazm: sukūn, or the nūn drops.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 8 · UNIT 5", "title": "The third case: jazm",
         "text": "Jazm belongs only to the present verb. Four small words put it in jazm. Its sign is a sukūn, or the nūn drops.",
         "wm": "الجَزْمُ"},

        {"t": "h2", "text": "Four particles of jazm"},
        {"t": "p", "text": "A noun can never be in jazm. A present verb goes into jazm when one of these particles comes before it."},
        {"t": "table", "head": ["Particle", "Name", "Meaning", "Example", "In English"], "rows": [
            ["لَمْ", "حَرْفُ نَفْيٍ", "did not", "لَمْ يَكْتُبْ", "he did not write"],
            ["لَمَّا", "حَرْفُ نَفْيٍ", "not yet", "لَمَّا يَكْتُبْ", "he has not written yet"],
            ["لِـ", "لَامُ الأَمْرِ", "let him...", "لِيَكْتُبْ", "let him write"],
            ["لَا", "لَا النَّاهِيَةُ", "don't!", "لَا تَكْتُبْ", "don't write"],
        ]},
        {"t": "rule", "color": "navy", "title": "Particle → jazm",
         "text": "{لَمْ}، {لَمَّا}، the {لِـ} of order and the {لَا} that forbids all put the present verb in jazm. They are fixed particles."},
        {"t": "tip", "text": "The {لِـ} of order has kasra and joins the verb: {لِيَكْتُبْ}. It is a different {لِـ} from the {لِـ} of purpose in Unit 4 ({لِيَكْتُبَ} \"so that he writes\"). The meaning tells you which one it is."},

        {"t": "h2", "text": "The signs of jazm"},
        {"t": "p", "text": "Look at the end of the verb. A normal verb takes sukūn. One of the five verbs loses its nūn."},
        {"t": "table", "head": ["Rafʿ", "Jazm", "Sign of jazm"], "rows": [
            ["يَكْتُبُ", "لَمْ يَكْتُبْ", "sukūn · السُّكُونُ"],
            ["تَكْتُبُ", "لَا تَكْتُبْ", "sukūn · السُّكُونُ"],
            ["أَكْتُبُ", "لَمْ أَكْتُبْ", "sukūn · السُّكُونُ"],
            ["يَكْتُبَانِ", "لَمْ يَكْتُبَا", "nūn drops · حَذْفُ النُّونِ"],
            ["يَكْتُبُونَ", "لَمْ يَكْتُبُوا", "nūn drops · حَذْفُ النُّونِ"],
            ["تَكْتُبِينَ", "لَا تَكْتُبِي", "nūn drops · حَذْفُ النُّونِ"],
        ]},
        {"t": "p", "text": "When the nūn of {يَكْتُبُونَ} drops, an alif is written after the wāw: {لَمْ يَكْتُبُوا}. The alif is only spelling."},
        {"t": "tip", "text": "With the nūn of women nothing changes: {الطَّالِبَاتُ لَمْ يَكْتُبْنَ}. The verb {يَكْتُبْنَ} is fixed. Its place is jazm."},
        {"t": "tip", "text": "If the next word starts with {ال}, the sukūn becomes a kasra so you can say it: {لَمْ يَذْهَبِ الوَلَدُ}. The sign is still sukūn. In this unit's cards the next word never starts with {ال}."},
        {"t": "tip", "text": "Verbs with a weak last letter ({يَدْعُو}، {يَرْمِي}، {يَسْعَى}) lose that letter in jazm. That comes in Unit 7."},

        {"t": "h2", "text": "لَمْ + present = مَا + past"},
        {"t": "p", "text": "{لَمْ} takes a present verb, but the meaning is past. {لَمْ يَكْتُبْ} means the same as {مَا كَتَبَ} from Stage 3."},
        {"t": "table", "head": ["مَا + past", "لَمْ + present", "Meaning"], "rows": [
            ["مَا كَتَبَ", "لَمْ يَكْتُبْ", "he did not write"],
            ["مَا ذَهَبْتُ", "لَمْ أَذْهَبْ", "I did not go"],
            ["مَا خَرَجْنَا", "لَمْ نَخْرُجْ", "we did not go out"],
            ["مَا شَرِبُوا", "لَمْ يَشْرَبُوا", "they did not drink"],
        ]},
        {"t": "p", "text": "{لَمَّا} is the same, with one more idea: up to now. {لَمَّا يَحْضُرْ خَالِدٌ} \"Khālid has not come yet\" (we still wait for him)."},

        {"t": "h2", "text": "Two kinds of لَا"},
        {"t": "cols", "items": [
            {"color": "navy", "title": "لَا that forbids · jazm", "ar": "لَا النَّاهِيَةُ",
             "text": "It tells someone not to act: {لَا تَكْتُبْ} \"Don't write!\" The verb is in jazm."},
            {"color": "red", "title": "لَا that negates · no effect", "ar": "لَا النَّافِيَةُ",
             "text": "It only says \"no\": {لَا تَكْتُبُ} \"You do not write.\" The verb stays in rafʿ."},
        ]},
        {"t": "rule", "color": "navy", "title": "The test",
         "text": "Is it an order not to do something? Then {لَا} forbids and the verb is in jazm. Is it only a fact? Then the verb stays in rafʿ."},
        {"t": "examples", "items": [
            {"ar": "لَا تَلْعَبْ فِي الفَصْلِ.", "en": "Don't play in the classroom.", "note": "{لَا} forbids: {تَلْعَبْ} with sukūn."},
            {"ar": "خَالِدٌ لَا يَلْعَبُ فِي الفَصْلِ.", "en": "Khālid does not play in the classroom.", "note": "Only a fact: {يَلْعَبُ} stays with damma."},
            {"ar": "لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا", "en": "Do not be sad. Allah is with us. (at-Tawba 9:40)", "note": "{تَحْزَنْ}: jazm after {لَا} that forbids."},
        ]},

        {"t": "h2", "text": "Worked examples"},
        {"t": "p", "text": "Use the same steps as always. Find the job. The job gives the case. The kind of word gives the sign."},
        {"t": "examples", "items": [
            {"ar": "لَمْ يَذْهَبْ خَالِدٌ.", "en": "Khālid did not go.",
             "note": "{لَمْ}: {حَرْفُ نَفْيٍ وَجَزْمٍ مَبْنِيٌّ عَلَى السُّكُونِ}. {يَذْهَبْ}: {فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ}. {خَالِدٌ}: {فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}."},
            {"ar": "لَا تَلْعَبُوا فِي الفَصْلِ.", "en": "Don't play in the classroom (you all).",
             "note": "{تَلْعَبُوا}: {فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الأَفْعَالِ الخَمْسَةِ}. The wāw: {ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ}."},
            {"ar": "لِيَقْرَأْ حَامِدٌ الدَّرْسَ.", "en": "Let Ḥāmid read the lesson.",
             "note": "{لِـ}: {لَامُ الأَمْرِ، حَرْفُ جَزْمٍ مَبْنِيٌّ عَلَى الكَسْرِ}. {يَقْرَأْ}: {فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَامِ الأَمْرِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ}."},
            {"ar": "لَمْ يَلِدْ وَلَمْ يُولَدْ", "en": "He did not beget, and He was not begotten. (al-Ikhlāṣ 112:3)",
             "note": "Two verbs after {لَمْ}. Both are in jazm with sukūn."},
        ]},

        {"t": "summary", "title": "In short", "items": [
            "Jazm is only for the present verb. Nouns are never in jazm.",
            "{لَمْ} \"did not\", {لَمَّا} \"not yet\", {لِـ} \"let him\", {لَا} \"don't\" put the verb in jazm.",
            "Sign: sukūn ({لَمْ يَكْتُبْ}). The five verbs lose the nūn ({لَمْ يَكْتُبُوا}، {لَا تَكْتُبِي}).",
            "{لَمْ يَكْتُبْ} = {مَا كَتَبَ}: the meaning is past.",
            "{لَا} that forbids gives jazm ({لَا تَكْتُبْ}). {لَا} that negates changes nothing ({لَا تَكْتُبُ}).",
            "The formula: {فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Which case comes after it?",
            "fields": [{"key": "case", "label": "Case of the verb", "options": [RAF, NASB, JAZM]}],
            "rows": [
                {"s": "لَمْ", "gloss": "did not", "ans": {"case": "jazm"},
                 "why": "{لَمْ} is a particle of jazm: {لَمْ يَكْتُبْ}."},
                {"s": "لَنْ", "gloss": "will not", "ans": {"case": "nasb"},
                 "why": "{لَنْ} is a particle of naṣb (Unit 4): {لَنْ يَكْتُبَ}."},
                {"s": "لَمَّا", "gloss": "not yet", "ans": {"case": "jazm"},
                 "why": "{لَمَّا} is a particle of jazm: {لَمَّا يَكْتُبْ}."},
                {"s": "لَا النَّاهِيَةُ", "gloss": "don't!", "ans": {"case": "jazm"},
                 "why": "The {لَا} that forbids gives jazm: {لَا تَكْتُبْ}."},
                {"s": "لَا النَّافِيَةُ", "gloss": "does not", "ans": {"case": "raf"},
                 "why": "The {لَا} that only negates has no effect. The verb stays in rafʿ: {لَا يَكْتُبُ}."},
                {"s": "لَامُ الأَمْرِ", "gloss": "let him...", "ans": {"case": "jazm"},
                 "why": "The {لِـ} of order gives jazm: {لِيَكْتُبْ}."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "لَمْ ___ خَالِدٌ إِلَى السُّوقِ.", "gloss": "Khālid did not go to the market.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَذْهَبُ", "يَذْهَبَ", "يَذْهَبْ")},
                 "why": "After {لَمْ} the verb is in jazm. Its sign is sukūn: {يَذْهَبْ}."},
                {"s": "لَا ___ فِي الفَصْلِ.", "gloss": "Don't play in the classroom.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَلْعَبْ", "تَلْعَبُ", "تَلْعَبَ")},
                 "why": "\"Don't\": {لَا} forbids, so jazm with sukūn. {تَلْعَبُ} would mean \"you do not play\"."},
                {"s": "لَمَّا ___ حَامِدٌ الدَّرْسَ.", "gloss": "Ḥāmid has not understood the lesson yet.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَفْهَمُ", "يَفْهَمْ", "يَفْهَمَ")},
                 "why": "{لَمَّا} gives jazm. Sign: sukūn."},
                {"s": "الطُّلَّابُ لَمْ ___ الوَاجِبَ.", "gloss": "The students did not write the homework.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَكْتُبُوا", "يَكْتُبُونَ", "يَكْتُبْ")},
                 "why": "{يَكْتُبُونَ} is one of the five verbs. In jazm its nūn drops: {يَكْتُبُوا}."},
                {"s": "___ كُلُّ طَالِبٍ اسْمَهُ.", "gloss": "Let every student write his name.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لِيَكْتُبُ", "لِيَكْتُبْ", "لِيَكْتُبَ")},
                 "why": "\"Let him write\": the {لِـ} of order gives jazm. {لِيَكْتُبَ} would be the {لِـ} of purpose."},
                {"s": "لَا ___ فِي المَسْجِدِ.", "gloss": "Don't talk in the mosque (you all).", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَتَكَلَّمُونَ", "تَتَكَلَّمْ", "تَتَكَلَّمُوا")},
                 "why": "\"You all\" is {تَتَكَلَّمُونَ}. After {لَا} that forbids, the nūn drops: {تَتَكَلَّمُوا}."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "لَمْ يَذْهَبْ خَالِدٌ إِلَى المَدْرَسَةِ.",
            "en": "Khālid did not go to school.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PART, VERB, DOER, PREP]},
                {"key": "sign", "label": "Sign", "options": [SUK, DAM, KAS, FIXED]},
            ],
            "rows": [
                {"s": "لَمْ", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A particle of jazm. It is fixed on sukūn."},
                {"s": "يَذْهَبْ", "ans": {"job": "verb", "sign": "suk"},
                 "why": "Present verb in jazm after {لَمْ}. Sign: sukūn."},
                {"s": "خَالِدٌ", "ans": {"job": "doer", "sign": "dam"},
                 "why": "{فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}."},
                {"s": "المَدْرَسَةِ", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {إِلَى}: jarr with kasra."},
            ],
        },
        {
            "title": "Iʿrāb: case and sign",
            "prompt": "الأَوْلَادُ لَمْ يَشْرَبُوا الحَلِيبَ فِي البَيْتِ.",
            "en": "The boys did not drink the milk at home.",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR, JAZM]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, DROP]},
            ],
            "rows": [
                {"s": "الأَوْلَادُ", "ans": {"case": "raf", "sign": "dam"},
                 "why": "Topic, rafʿ. A broken plural takes damma."},
                {"s": "يَشْرَبُوا", "ans": {"case": "jazm", "sign": "drop"},
                 "why": "Jazm after {لَمْ}. One of the five verbs, so the nūn drops."},
                {"s": "الحَلِيبَ", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "Object, naṣb with fatha."},
                {"s": "البَيْتِ", "ans": {"case": "jarr", "sign": "kas"},
                 "why": "After {فِي}: jarr with kasra."},
            ],
        },
        {
            "title": "Say it with لَمْ",
            "fields": [{"key": "pick", "label": "Same meaning", "options": []}],
            "rows": [
                {"s": "مَا كَتَبَ", "gloss": "he did not write", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لَمْ يَكْتُبْ", "لَمْ كَتَبَ", "لَمْ يَكْتُبُ")},
                 "why": "{لَمْ} takes a present verb in jazm: {لَمْ يَكْتُبْ}."},
                {"s": "مَا ذَهَبُوا", "gloss": "they did not go", "ans": {"pick": "c"},
                 "opts": {"pick": pick("لَمْ يَذْهَبُونَ", "لَمْ ذَهَبُوا", "لَمْ يَذْهَبُوا")},
                 "why": "{يَذْهَبُونَ} loses its nūn in jazm: {لَمْ يَذْهَبُوا}."},
                {"s": "مَا شَرِبْتُ", "gloss": "I did not drink", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَمْ يَشْرَبْ", "لَمْ أَشْرَبْ", "لَمْ أَشْرَبُ")},
                 "why": "\"I\" is {أَشْرَبُ}. In jazm: {لَمْ أَشْرَبْ}."},
                {"s": "مَا خَرَجْنَا", "gloss": "we did not go out", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لَمْ نَخْرُجْ", "لَمْ نَخْرُجُ", "لَمْ تَخْرُجْ")},
                 "why": "\"We\" is {نَخْرُجُ}. In jazm: {لَمْ نَخْرُجْ}."},
                {"s": "مَا فَهِمْتِ", "gloss": "you (f.) did not understand", "ans": {"pick": "c"},
                 "opts": {"pick": pick("لَمْ تَفْهَمِينَ", "لَمْ تَفْهَمْ", "لَمْ تَفْهَمِي")},
                 "why": "\"You (f.)\" is {تَفْهَمِينَ}, one of the five verbs. In jazm the nūn drops: {لَمْ تَفْهَمِي}."},
            ],
        },
        {
            "title": "Which particle fits the meaning?",
            "fields": [{"key": "pick", "label": "Particle", "options": []}],
            "rows": [
                {"s": "___ يَحْضُرْ زَيْدٌ أَمْسِ.", "gloss": "Zayd did not come yesterday.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لَمْ", "لَنْ", "لَا")},
                 "why": "\"Did not\" with a verb in jazm: {لَمْ}."},
                {"s": "___ تَشْرَبْ هَذَا المَاءَ.", "gloss": "Don't drink this water.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("لَمْ", "لَنْ", "لَا")},
                 "why": "\"Don't\" is the {لَا} that forbids. It gives jazm."},
                {"s": "___ يَخْرُجُ خَالِدٌ مِنَ البَيْتِ.", "gloss": "Khālid does not go out of the house.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَمْ", "لَا", "لَنْ")},
                 "why": "The verb has damma, so no particle of jazm or naṣb is before it. Only {لَا} that negates fits."},
                {"s": "___ يَرْجِعْ أَبِي مِنَ السَّفَرِ.", "gloss": "My father has not come back from the trip yet.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَنْ", "لَمَّا", "لَا")},
                 "why": "\"Not yet\" is {لَمَّا}. It gives jazm."},
                {"s": "___ يَذْهَبَ خَالِدٌ غَدًا.", "gloss": "Khālid will not go tomorrow.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لَنْ", "لَمْ", "لَمَّا")},
                 "why": "\"Will not\" is {لَنْ}. The verb has fatha: naṣb."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "يَا فَاطِمَةُ، لَا ___ البَابَ.", "gloss": "Fāṭima, don't open the door.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَفْتَحِينَ", "تَفْتَحِي", "تَفْتَحْ")},
                 "why": "To a woman: {تَفْتَحِينَ}. After {لَا} that forbids, the nūn drops: {تَفْتَحِي}."},
                {"s": "الطَّالِبَانِ لَمْ ___.", "gloss": "The two students did not come.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَحْضُرَا", "يَحْضُرَانِ", "يَحْضُرْ")},
                 "why": "For two: {يَحْضُرَانِ}. In jazm the nūn drops: {يَحْضُرَا}."},
                {"s": "نَحْنُ لَمْ ___ شَيْئًا.", "gloss": "We did not eat anything.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("نَأْكُلُ", "يَأْكُلْ", "نَأْكُلْ")},
                 "why": "\"We\" is {نَأْكُلُ}. After {لَمْ}: sukūn."},
                {"s": "___ خَالِدٌ إِلَى البَيْتِ.", "gloss": "Let Khālid go home.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لِيَذْهَبْ", "لِيَذْهَبُ", "لِيَذْهَبَ")},
                 "why": "\"Let him go\": the {لِـ} of order gives jazm with sukūn."},
                {"s": "أَنَا لَا ___ القَهْوَةَ.", "gloss": "I don't drink coffee.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَشْرَبْ", "أَشْرَبُ", "أَشْرَبَ")},
                 "why": "A fact, not an order. This {لَا} only negates, so the verb stays in rafʿ."},
                {"s": "لَا ___ فِي الشَّارِعِ.", "gloss": "Don't play in the street (you two).", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَلْعَبَانِ", "تَلْعَبْ", "تَلْعَبَا")},
                 "why": "For two: {تَلْعَبَانِ}. After {لَا} that forbids, the nūn drops: {تَلْعَبَا}."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "لَا تَكْتُبُوا عَلَى الجِدَارِ.",
            "en": "Don't write on the wall (you all).",
            "fields": [
                {"key": "job", "label": "Job", "options": [PART, VERB, DOER, PREP]},
                {"key": "sign", "label": "Sign", "options": [DROP, KAS, SUK, FIXED]},
            ],
            "rows": [
                {"s": "لَا", "ans": {"job": "part", "sign": "fixed"},
                 "why": "The {لَا} that forbids: a particle of jazm, fixed on sukūn."},
                {"s": "تَكْتُبُوا", "ans": {"job": "verb", "sign": "drop"},
                 "why": "Present verb in jazm after {لَا} that forbids. One of the five verbs: the nūn drops."},
                {"s": "الوَاوُ", "gloss": "the wāw at the end of the verb", "ans": {"job": "doer", "sign": "fixed"},
                 "why": "An attached pronoun, fixed on sukūn, in the place of rafʿ. It is the doer."},
                {"s": "الجِدَارِ", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {عَلَى}: jarr with kasra."},
            ],
        },
        {
            "title": "Iʿrāb: case and sign",
            "prompt": "لَمَّا يَرْجِعْ أَبُوكَ مِنَ السُّوقِ.",
            "en": "Your father has not come back from the market yet.",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR, JAZM]},
                {"key": "sign", "label": "Sign", "options": [DAM, KAS, SUK, {"k": "waw", "label": "Wāw · الوَاوُ", "color": "blue"}]},
            ],
            "rows": [
                {"s": "يَرْجِعْ", "ans": {"case": "jazm", "sign": "suk"},
                 "why": "{فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمَّا وَعَلَامَةُ جَزْمِهِ السُّكُونُ}."},
                {"s": "أَبُوكَ", "ans": {"case": "raf", "sign": "waw"},
                 "why": "Doer, rafʿ. One of the five nouns, so the sign is wāw."},
                {"s": "السُّوقِ", "ans": {"case": "jarr", "sign": "kas"},
                 "why": "After {مِنْ}: jarr with kasra."},
            ],
        },
        {
            "title": "Which case and sign does the verb take here?",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JAZM]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, SUK, NUN, DROP]},
            ],
            "rows": [
                {"s": "لَمْ [يَسْمَعُوا] الأَذَانَ", "gloss": "they did not hear the call to prayer", "ans": {"case": "jazm", "sign": "drop"},
                 "why": "Jazm after {لَمْ}. A five verb: the nūn drops."},
                {"s": "هُوَ لَا [يَسْمَعُ] الصَّوْتَ", "gloss": "he does not hear the sound", "ans": {"case": "raf", "sign": "dam"},
                 "why": "This {لَا} only negates. No effect: rafʿ with damma."},
                {"s": "[لِيَسْمَعْ] كُلُّ طَالِبٍ", "gloss": "let every student listen", "ans": {"case": "jazm", "sign": "suk"},
                 "why": "The {لِـ} of order gives jazm. Sign: sukūn."},
                {"s": "لَمَّا [تَسْمَعِي] الخَبَرَ", "gloss": "you (f.) have not heard the news yet", "ans": {"case": "jazm", "sign": "drop"},
                 "why": "Jazm after {لَمَّا}. {تَسْمَعِينَ} is a five verb: the nūn drops."},
                {"s": "أَنْتُمَا [تَسْمَعَانِ] الدَّرْسَ", "gloss": "you two hear the lesson", "ans": {"case": "raf", "sign": "nun"},
                 "why": "No particle before it: rafʿ. A five verb in rafʿ keeps its nūn."},
                {"s": "لَنْ [يَسْمَعَ] أَحَدٌ", "gloss": "no one will hear", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "After {لَنْ}: naṣb with fatha (Unit 4)."},
            ],
        },
        {
            "title": "Which particle fits the meaning?",
            "fields": [{"key": "pick", "label": "Particle", "options": []}],
            "rows": [
                {"s": "___ أَذْهَبْ إِلَى السُّوقِ أَمْسِ.", "gloss": "I did not go to the market yesterday.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَنْ", "لَمْ", "لَا")},
                 "why": "\"Did not\" with a verb in jazm: {لَمْ}."},
                {"s": "___ تَكْذِبْ.", "gloss": "Don't lie.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لَا", "لَمْ", "لَنْ")},
                 "why": "\"Don't\": the {لَا} that forbids, with jazm."},
                {"s": "___ يَنْجَحُ الطَّالِبُ الكَسُولُ.", "gloss": "The lazy student does not succeed.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("لَمْ", "لَنْ", "لَا")},
                 "why": "The verb has damma. Only {لَا} that negates leaves it in rafʿ."},
                {"s": "___ يَفْتَحْ حَامِدٌ البَابَ.", "gloss": "Ḥāmid has not opened the door yet.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَنْ", "لَمَّا", "لَا")},
                 "why": "\"Not yet\" is {لَمَّا}, with jazm."},
                {"s": "___يَدْخُلْ خَالِدٌ.", "gloss": "Let Khālid come in.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لِـ", "لَنْ", "لَمْ")},
                 "why": "\"Let him\" is the {لِـ} of order: {لِيَدْخُلْ}."},
            ],
        },
        {
            "title": "Turn the order into \"don't\"",
            "fields": [{"key": "pick", "label": "Don't...", "options": []}],
            "rows": [
                {"s": "اُكْتُبْ", "gloss": "write! → don't write!", "ans": {"pick": "c"},
                 "opts": {"pick": pick("لَا تَكْتُبُ", "لَا اُكْتُبْ", "لَا تَكْتُبْ")},
                 "why": "Use {لَا} + the present verb {تَكْتُبُ} in jazm: {لَا تَكْتُبْ}."},
                {"s": "اِجْلِسُوا", "gloss": "sit (you all)! → don't sit!", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لَا تَجْلِسُوا", "لَا تَجْلِسُونَ", "لَا اِجْلِسُوا")},
                 "why": "{تَجْلِسُونَ} in jazm loses its nūn: {لَا تَجْلِسُوا}."},
                {"s": "اِذْهَبِي", "gloss": "go (f.)! → don't go!", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَا تَذْهَبِينَ", "لَا تَذْهَبِي", "لَا تَذْهَبْ")},
                 "why": "To a woman: {تَذْهَبِينَ}. In jazm: {لَا تَذْهَبِي}."},
                {"s": "اِلْعَبَا", "gloss": "play (you two)! → don't play!", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَا تَلْعَبَانِ", "لَا تَلْعَبَا", "لَا تَلْعَبْ")},
                 "why": "For two: {تَلْعَبَانِ}. In jazm: {لَا تَلْعَبَا}."},
                {"s": "اِفْتَحْ", "gloss": "open! → don't open!", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لَا تَفْتَحْ", "لَا تَفْتَحُ", "لَا يَفْتَحْ")},
                 "why": "Speaking to \"you\": {تَفْتَحُ}. In jazm: {لَا تَفْتَحْ}."},
            ],
        },
    ],
}
