# Stage 7, Unit 5: "Together with" and the state (المَفْعُولُ مَعَهُ وَالحَالُ)


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


# Canonical options (copied from STAGES_5_8_SPEC.md)
DAM = {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
FAT = {"k": "fat",   "label": "Fatha · فَتْحَةٌ",                "color": "pink"}
KAS = {"k": "kas",   "label": "Kasra · كَسْرَةٌ",                "color": "green"}
ALIF = {"k": "alif",  "label": "Alif · الأَلِفُ",                  "color": "teal"}
WAW = {"k": "waw",   "label": "Wāw · الوَاوُ",                   "color": "blue"}
YA = {"k": "ya",    "label": "Yāʾ · اليَاءُ",                   "color": "purple"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ",                  "color": "grey"}

RAF = {"k": "raf",  "label": "Rafʿ · رَفْعٌ",   "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ",  "color": "pink"}

VERB = {"k": "verb",  "label": "Verb · فِعْلٌ",                       "color": "navy"}
DOER = {"k": "doer",  "label": "Doer · فَاعِلٌ",                      "color": "orange"}
PREP = {"k": "prep",  "label": "After a preposition · اِسْمٌ مَجْرُورٌ",    "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ",               "color": "purple"}
ADJ = {"k": "adj",   "label": "Adjective · نَعْتٌ",                   "color": "grey"}
AND = {"k": "and",   "label": "After وَ (and) · مَعْطُوفٌ",              "color": "blue"}
MAAH = {"k": "maah",  "label": "Together with · مَفْعُولٌ مَعَهُ",         "color": "blue"}
STATE = {"k": "state", "label": "State · حَالٌ",                       "color": "olive"}
PART = {"k": "part",  "label": "Particle · حَرْفٌ",                     "color": "grey"}


UNIT = {
    "id": "s7-maah-state",
    "order": 5,
    "title": "\"Together with\" and the state",
    "ar": "المَفْعُولُ مَعَهُ وَالحَالُ",
    "blurb": "A وَ that means \"together with\" puts the next noun in naṣb. The state tells you how the doer or object was, with every kind of noun.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 7 · UNIT 5", "title": "With whom, and in what state",
         "text": "Two more naṣb jobs. The \"together with\" noun comes after a special {وَ}. The state describes someone at the time of the action.",
         "wm": "مَعَهُ وَالحَالُ"},

        {"t": "h2", "text": "\"Together with\": المَفْعُولُ مَعَهُ"},
        {"t": "p", "text": "Sometimes {وَ} does not mean \"and\". It means \"together with, along with\". It is called {وَاوُ المَعِيَّةِ}. The noun after it is {المَفْعُولُ مَعَهُ}, and it is in naṣb."},
        {"t": "examples", "items": [
            {"ar": "سِرْتُ وَالنِّيلَ.", "en": "I walked along the Nile.",
             "note": "The Nile did not walk. It was only there with me."},
            {"ar": "اِسْتَيْقَظْتُ وَطُلُوعَ الشَّمْسِ.", "en": "I woke up at sunrise.",
             "note": "The rising of the sun did not wake up. It happened together with my waking."},
            {"ar": "ذَاكَرَ الطَّالِبُ وَالمِصْبَاحَ.", "en": "The student studied by the lamp."},
        ]},
        {"t": "p", "text": "Full iʿrāb of {سِرْتُ وَالنِّيلَ}:"},
        {"t": "table", "head": ["Word", "Iʿrāb"], "rows": [
            ["وَ", "وَاوُ المَعِيَّةِ، حَرْفٌ مَبْنِيٌّ عَلَى الفَتْحِ"],
            ["النِّيلَ", "مَفْعُولٌ مَعَهُ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ"],
        ]},

        {"t": "h2", "text": "\"And\" or \"together with\"?"},
        {"t": "rule", "color": "blue", "title": "The test",
         "text": "Ask: can the noun after {وَ} also do the action? If yes, {وَ} means \"and\". The noun copies the case before it. If no, {وَ} means \"together with\". The noun is in naṣb."},
        {"t": "table", "head": ["Sentence", "Can it do the action?", "Job and case"], "rows": [
            ["جَاءَ المُدِيرُ وَالمُعَلِّمُ.", "Yes, the teacher came too.", "After وَ (and), rafʿ: {المُعَلِّمُ}"],
            ["سِرْتُ وَالنِّيلَ.", "No, a river does not walk.", "Together with, naṣb: {النِّيلَ}"],
            ["خَرَجَ الطُّلَّابُ وَالمُعَلِّمُونَ.", "Yes, the teachers went out too.", "After وَ (and), rafʿ: {المُعَلِّمُونَ}"],
            ["اِسْتَيْقَظَ الأَوْلَادُ وَطُلُوعَ الشَّمْسِ.", "No, sunrise does not wake up.", "Together with, naṣb: {طُلُوعَ}"],
        ]},
        {"t": "tip", "text": "In this unit we only use clear cases. If the second noun could also do the action, read {وَ} as \"and\"."},

        {"t": "h2", "text": "The state: الحَالُ"},
        {"t": "p", "text": "The state ({الحَالُ}) answers \"how?\" or \"in what state?\". It describes the doer or the object at the time of the action."},
        {"t": "rule", "color": "olive", "title": "Two rules of the state",
         "text": "1. The state is indefinite: {مُسْرِعًا}. It never takes {ال}. 2. Its owner ({صَاحِبُ الحَالِ}) is definite: {جَاءَ الوَلَدُ مُسْرِعًا}."},
        {"t": "examples", "items": [
            {"ar": "رَجَعَ الوَلَدُ فَرِحًا.", "en": "The boy came back happy.",
             "note": "The owner of the state is the doer {الوَلَدُ}."},
            {"ar": "شَرِبْتُ المَاءَ بَارِدًا.", "en": "I drank the water cold.",
             "note": "The owner of the state is the object {المَاءَ}."},
            {"ar": "جَاءَ أَبُوكَ مُبْتَسِمًا.", "en": "Your father came smiling."},
        ]},
        {"t": "tip", "text": "The state matches its owner in number and gender: {جَاءَ الطُّلَّابُ مُسْرِعِينَ}، {رَجَعَتِ البَنَاتُ فَرِحَاتٍ}."},

        {"t": "h2", "text": "The state with every kind of noun"},
        {"t": "p", "text": "Find the job. The job gives the case. The kind of noun gives the sign."},
        {"t": "table", "head": ["Kind of noun", "Example", "Sign of naṣb"], "rows": [
            ["Singular", "رَجَعَ الوَلَدُ فَرِحًا.", "Fatha"],
            ["Dual", "جَاءَ الطَّالِبَانِ ضَاحِكَيْنِ.", "Yāʾ: {ـَيْنِ}"],
            ["Sound m. plural", "جَاءَ الطُّلَّابُ مُسْرِعِينَ.", "Yāʾ: {ـِينَ}"],
            ["Sound f. plural", "رَجَعَتِ البَنَاتُ فَرِحَاتٍ.", "Kasra in place of fatha"],
            ["Manqūṣ", "مَشَى الرَّجُلُ حَافِيًا.", "Fatha, it shows on the {ي}"],
        ]},
        {"t": "examples", "items": [
            {"ar": "جَاءَ الطُّلَّابُ مُسْرِعِينَ.", "en": "The students came hurrying.",
             "note": "{مُسْرِعِينَ}: {حَالٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
            {"ar": "رَجَعَتِ البَنَاتُ فَرِحَاتٍ.", "en": "The girls came back happy.",
             "note": "{فَرِحَاتٍ}: {حَالٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الكَسْرَةُ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ}."},
            {"ar": "جَاءَ الطَّالِبَانِ ضَاحِكَيْنِ.", "en": "The two students came laughing.",
             "note": "{ضَاحِكَيْنِ}: {حَالٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
        ]},

        {"t": "h2", "text": "State or adjective?"},
        {"t": "p", "text": "An adjective copies its noun in case and in {ال}. A state is always indefinite and in naṣb, and its owner is definite."},
        {"t": "table", "head": ["Sentence", "The word", "Job"], "rows": [
            ["جَاءَ الرَّجُلُ ضَاحِكًا.", "ضَاحِكًا", "State: indefinite, its owner is definite"],
            ["جَاءَ الرَّجُلُ الضَّاحِكُ.", "الضَّاحِكُ", "Adjective: it copies {ال} and rafʿ"],
            ["رَأَيْتُ رَجُلًا ضَاحِكًا.", "ضَاحِكًا", "Adjective: {رَجُلًا} is indefinite, so the word copies it"],
        ]},
        {"t": "tip", "text": "Look at the noun before it. Definite noun + indefinite naṣb word: a state. Indefinite noun + indefinite word with the same ending: an adjective."},

        {"t": "summary", "title": "In short", "items": [
            "{وَاوُ المَعِيَّةِ} means \"together with\". The noun after it is {مَفْعُولٌ مَعَهُ}, in naṣb: {سِرْتُ وَالنِّيلَ}.",
            "Test: can the noun after {وَ} do the action too? Yes: \"and\". No: \"together with\".",
            "The state answers \"how?\". It is indefinite, in naṣb, and its owner is definite.",
            "Signs of the state: fatha (singular, manqūṣ {حَافِيًا}), yāʾ (dual {ضَاحِكَيْنِ}, sound m. plural {مُسْرِعِينَ}), kasra (sound f. plural {فَرِحَاتٍ}).",
            "After an indefinite noun, a matching indefinite word is an adjective: {رَأَيْتُ رَجُلًا ضَاحِكًا}.",
        ]},
    ],

    "practice": [
        {
            "title": "Full iʿrāb: together with (with review)",
            "prompt": "سَارَ المُسَافِرُونَ وَالنِّيلَ.",
            "en": "The travellers walked along the Nile.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, PART, MAAH]},
                {"key": "sign", "label": "Sign", "options": [FAT, WAW, YA, FIXED]},
            ],
            "rows": [
                {"s": "سَارَ", "ans": {"job": "verb", "sign": "fixed"}, "why": "A past verb, fixed on fatha."},
                {"s": "المُسَافِرُونَ", "ans": {"job": "doer", "sign": "waw"}, "why": "Who walked? The doer, rafʿ. A sound m. plural: the wāw."},
                {"s": "وَ", "ans": {"job": "part", "sign": "fixed"}, "why": "{وَاوُ المَعِيَّةِ}: a particle fixed on fatha. It means \"together with\"."},
                {"s": "النِّيلَ", "ans": {"job": "maah", "sign": "fat"}, "why": "The Nile does not walk. {مَفْعُولٌ مَعَهُ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
            ],
        },
        {
            "title": "Full iʿrāb: the state (with review)",
            "prompt": "جَاءَ الطَّالِبَانِ إِلَى الفَصْلِ ضَاحِكَيْنِ.",
            "en": "The two students came to the classroom laughing.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, PREP, STATE]},
                {"key": "sign", "label": "Sign", "options": [KAS, ALIF, YA, FIXED]},
            ],
            "rows": [
                {"s": "جَاءَ", "ans": {"job": "verb", "sign": "fixed"}, "why": "A past verb, fixed on fatha."},
                {"s": "الطَّالِبَانِ", "ans": {"job": "doer", "sign": "alif"}, "why": "The doer, rafʿ. A dual in rafʿ: the alif."},
                {"s": "الفَصْلِ", "ans": {"job": "prep", "sign": "kas"}, "why": "After {إِلَى}: jarr with kasra."},
                {"s": "ضَاحِكَيْنِ", "ans": {"job": "state", "sign": "ya"}, "why": "How did they come? Laughing. {حَالٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
            ],
        },
        {
            "title": "What is the word after وَ?",
            "fields": [
                {"key": "job", "label": "Job", "options": [AND, MAAH]},
                {"key": "case", "label": "Case", "options": [RAF, NASB]},
            ],
            "rows": [
                {"s": "سِرْنَا وَالنَّهْرَ.", "ans": {"job": "maah", "case": "nasb"}, "why": "A river cannot walk. {وَ} means \"together with\": naṣb."},
                {"s": "جَاءَ الطَّبِيبُ وَالمُمَرِّضُ.", "ans": {"job": "and", "case": "raf"}, "why": "The nurse came too. {وَ} means \"and\": {المُمَرِّضُ} copies the doer in rafʿ."},
                {"s": "اِسْتَيْقَظَ الفَلَّاحُ وَطُلُوعَ الفَجْرِ.", "ans": {"job": "maah", "case": "nasb"}, "why": "Dawn does not wake up. Together with: {طُلُوعَ} in naṣb."},
                {"s": "حَضَرَ المُهَنْدِسُونَ وَالعُمَّالُ.", "ans": {"job": "and", "case": "raf"}, "why": "The workers came too: \"and\". {العُمَّالُ} copies the doer in rafʿ."},
                {"s": "ذَاكَرَتِ البِنْتُ وَالمِصْبَاحَ.", "ans": {"job": "maah", "case": "nasb"}, "why": "A lamp does not study. Together with: {المِصْبَاحَ} in naṣb."},
            ],
        },
        {
            "title": "State or adjective?",
            "fields": [{"key": "job", "label": "Job of the word in [ ]", "options": [STATE, ADJ]}],
            "rows": [
                {"s": "جَاءَ الطَّالِبُ [مُبْتَسِمًا].", "ans": {"job": "state"}, "why": "Indefinite, naṣb, after a definite noun: how did he come? A state."},
                {"s": "جَاءَ الطَّالِبُ [المُبْتَسِمُ].", "ans": {"job": "adj"}, "why": "It has {ال} and rafʿ like {الطَّالِبُ}: an adjective."},
                {"s": "رَأَيْتُ طَالِبًا [مُبْتَسِمًا].", "ans": {"job": "adj"}, "why": "{طَالِبًا} is indefinite. The word copies it: an adjective."},
                {"s": "رَجَعَتِ الأُمَّهَاتُ [فَرِحَاتٍ].", "ans": {"job": "state"}, "why": "Indefinite, naṣb, after the definite {الأُمَّهَاتُ}: a state."},
                {"s": "قَرَأْتُ كِتَابًا [مُفِيدًا].", "ans": {"job": "adj"}, "why": "{كِتَابًا} is indefinite, and {مُفِيدًا} copies it: an adjective."},
                {"s": "شَرِبَ الوَلَدُ العَصِيرَ [بَارِدًا].", "ans": {"job": "state"}, "why": "{العَصِيرَ} is definite and {بَارِدًا} is not: the state of the juice when he drank it."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "خَرَجَ اللَّاعِبُونَ ___", "gloss": "The players went out hurrying.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُسْرِعُونَ", "مُسْرِعِينَ", "مُسْرِعَاتٍ")},
                 "why": "A state for men, in naṣb: the sound m. plural ends in {ـِينَ}."},
                {"s": "رَجَعَتِ النِّسَاءُ ___", "gloss": "The women came back happy.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فَرِحَاتٍ", "فَرِحَاتًا", "فَرِحَاتٌ")},
                 "why": "A sound f. plural in naṣb takes the kasra: {فَرِحَاتٍ}."},
                {"s": "دَخَلَ الوَلَدَانِ ___", "gloss": "The two boys came in laughing.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("ضَاحِكَانِ", "ضَاحِكِينَ", "ضَاحِكَيْنِ")},
                 "why": "A dual in naṣb: {ـَيْنِ}. {ـِينَ} is for a plural."},
                {"s": "خَرَجَتِ الأُمُّ ___", "gloss": "The mother went out hurrying.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُسْرِعَةً", "مُسْرِعَةٌ", "المُسْرِعَةَ")},
                 "why": "The state is indefinite and in naṣb: {مُسْرِعَةً}."},
                {"s": "طَافَ الرَّجُلُ ___", "gloss": "The man walked round barefoot.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("حَافٍ", "حَافِيًا", "الحَافِي")},
                 "why": "A manqūṣ word in naṣb: the fatha shows on the {ي}: {حَافِيًا}. {حَافٍ} is for rafʿ and jarr."},
                {"s": "مَشَى السَّائِحُ وَ___", "gloss": "The tourist walked along the Nile.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("النِّيلِ", "النِّيلُ", "النِّيلَ")},
                 "why": "{وَ} means \"together with\": {مَفْعُولٌ مَعَهُ} in naṣb."},
            ],
        },
        {
            "title": "Job and sign of the word in [ ]",
            "fields": [
                {"key": "job", "label": "Job", "options": [MAAH, STATE]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, YA]},
            ],
            "rows": [
                {"s": "رَجَعَتِ الطَّالِبَاتُ [مَسْرُورَاتٍ].", "ans": {"job": "state", "sign": "kas"}, "why": "How did they come back? A state. Sound f. plural: kasra."},
                {"s": "حَضَرَ المُسْلِمُونَ [مُبَكِّرِينَ].", "ans": {"job": "state", "sign": "ya"}, "why": "How did they come? Early. A state. Sound m. plural: yāʾ."},
                {"s": "مَشَيْتُ وَ[الشَّاطِئَ].", "ans": {"job": "maah", "sign": "fat"}, "why": "The shore does not walk. Together with, naṣb, fatha."},
                {"s": "خَرَجَتِ البِنْتَانِ [ضَاحِكَتَيْنِ].", "ans": {"job": "state", "sign": "ya"}, "why": "A state for two girls. Dual in naṣb: yāʾ."},
                {"s": "جَاءَ أَبُوكَ [رَاكِبًا].", "ans": {"job": "state", "sign": "fat"}, "why": "How did he come? Riding. A singular state: fatha."},
                {"s": "اِسْتَيْقَظَتِ البِنْتُ وَ[أَذَانَ] الفَجْرِ.", "ans": {"job": "maah", "sign": "fat"}, "why": "The call to prayer does not wake up. Together with, naṣb, fatha. It is owned, so no tanween."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Full iʿrāb: the state (with review)",
            "prompt": "رَجَعَتِ الطَّالِبَاتُ مِنَ الرِّحْلَةِ فَرِحَاتٍ.",
            "en": "The female students came back from the trip happy.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, PREP, STATE]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, FIXED]},
            ],
            "rows": [
                {"s": "رَجَعَتِ", "ans": {"job": "verb", "sign": "fixed"}, "why": "A past verb, fixed on fatha."},
                {"s": "الطَّالِبَاتُ", "ans": {"job": "doer", "sign": "dam"}, "why": "The doer, rafʿ. A sound f. plural takes the damma in rafʿ."},
                {"s": "الرِّحْلَةِ", "ans": {"job": "prep", "sign": "kas"}, "why": "After {مِنْ}: jarr with kasra."},
                {"s": "فَرِحَاتٍ", "ans": {"job": "state", "sign": "kas"}, "why": "{حَالٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الكَسْرَةُ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ}. Naṣb, but the sign is a kasra."},
            ],
        },
        {
            "title": "Full iʿrāb: together with (with review)",
            "prompt": "اِسْتَيْقَظَ أَبُوكَ وَطُلُوعَ الفَجْرِ.",
            "en": "Your father woke up at dawn.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, PART, MAAH, OWNER]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, WAW, FIXED]},
            ],
            "rows": [
                {"s": "أَبُوكَ", "ans": {"job": "doer", "sign": "waw"}, "why": "The doer, rafʿ. One of the five nouns: the wāw."},
                {"s": "وَ", "ans": {"job": "part", "sign": "fixed"}, "why": "{وَاوُ المَعِيَّةِ}, a particle fixed on fatha."},
                {"s": "طُلُوعَ", "ans": {"job": "maah", "sign": "fat"}, "why": "Dawn does not wake up. {مَفْعُولٌ مَعَهُ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}, owned, so no tanween."},
                {"s": "الفَجْرِ", "ans": {"job": "owner", "sign": "kas"}, "why": "Owned by {طُلُوعَ}: owner, jarr with kasra."},
            ],
        },
        {
            "title": "What is the word after وَ?",
            "fields": [
                {"key": "job", "label": "Job", "options": [AND, MAAH]},
                {"key": "case", "label": "Case", "options": [RAF, NASB]},
            ],
            "rows": [
                {"s": "سَافَرَ الطُّلَّابُ وَالمُعَلِّمَانِ.", "ans": {"job": "and", "case": "raf"}, "why": "The two teachers travelled too: \"and\". Rafʿ, the dual ends in {ـَانِ}."},
                {"s": "خَرَجْتُ وَطُلُوعَ الفَجْرِ.", "ans": {"job": "maah", "case": "nasb"}, "why": "Dawn does not go out. Together with: naṣb."},
                {"s": "مَشَى الأَوْلَادُ وَالنَّهْرَ.", "ans": {"job": "maah", "case": "nasb"}, "why": "A river does not walk. The boys walked along it: naṣb."},
                {"s": "حَضَرَ الآبَاءُ وَالأُمَّهَاتُ.", "ans": {"job": "and", "case": "raf"}, "why": "The mothers came too: \"and\". {الأُمَّهَاتُ} copies the doer in rafʿ."},
                {"s": "اِسْتَوَى المَاءُ وَالخَشَبَةَ.", "ans": {"job": "maah", "case": "nasb"}, "why": "The water rose level with the plank. The plank did not rise: together with, naṣb."},
                {"s": "خَرَجَ زَيْدٌ وَأَخُوهُ.", "ans": {"job": "and", "case": "raf"}, "why": "His brother went out too: \"and\". {أَخُوهُ} is rafʿ with wāw."},
            ],
        },
        {
            "title": "State or adjective?",
            "fields": [{"key": "job", "label": "Job of the word in [ ]", "options": [STATE, ADJ]}],
            "rows": [
                {"s": "شَاهَدْتُ اللَّاعِبِينَ [مُتْعَبِينَ].", "ans": {"job": "state"}, "why": "{اللَّاعِبِينَ} is definite and {مُتْعَبِينَ} is not: their state when I saw them."},
                {"s": "شَاهَدْتُ لَاعِبِينَ [مُتْعَبِينَ].", "ans": {"job": "adj"}, "why": "{لَاعِبِينَ} is indefinite. The word copies it: an adjective."},
                {"s": "أَكَلْتُ الخُبْزَ [سَاخِنًا].", "ans": {"job": "state"}, "why": "Definite noun, then an indefinite naṣb word: the state of the bread."},
                {"s": "اِشْتَرَيْتُ خُبْزًا [سَاخِنًا].", "ans": {"job": "adj"}, "why": "{خُبْزًا} is indefinite, so {سَاخِنًا} is its adjective."},
                {"s": "جَاءَتِ الطَّالِبَتَانِ [المُجْتَهِدَتَانِ].", "ans": {"job": "adj"}, "why": "It has {ال} and rafʿ like {الطَّالِبَتَانِ}: an adjective."},
                {"s": "رَجَعَ المُسَافِرُونَ [مُتْعَبِينَ].", "ans": {"job": "state"}, "why": "How did they come back? Tired. Indefinite, naṣb, after a definite doer: a state."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "حَضَرَتِ المُعَلِّمَاتُ ___", "gloss": "The female teachers came early.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُبَكِّرَاتٍ", "مُبَكِّرَاتٌ", "مُبَكِّرَاتًا")},
                 "why": "A state in naṣb. Sound f. plural: kasra, {مُبَكِّرَاتٍ}."},
                {"s": "جَاءَ المُهَنْدِسُونَ ___", "gloss": "The engineers came riding.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("رَاكِبُونَ", "رَاكِبِينَ", "رَاكِبَيْنِ")},
                 "why": "A state for many men, in naṣb: {رَاكِبِينَ}. {رَاكِبَيْنِ} is for two."},
                {"s": "رَجَعَتِ الأُخْتَانِ ___", "gloss": "The two sisters came back happy.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("فَرِحَتَانِ", "فَرِحَاتٍ", "فَرِحَتَيْنِ")},
                 "why": "Two women, in naṣb: {فَرِحَتَيْنِ}."},
                {"s": "شَرِبْتُ الشَّايَ ___", "gloss": "I drank the tea hot (state).", "ans": {"pick": "a"},
                 "opts": {"pick": pick("سَاخِنًا", "سَاخِنٍ", "سَاخِنٌ")},
                 "why": "The state is in naṣb: fatha with tanween."},
                {"s": "اِسْتَيْقَظْتُ وَ___ الشَّمْسِ", "gloss": "I woke up at sunrise.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("طُلُوعِ", "طُلُوعَ", "طُلُوعًا")},
                 "why": "Together with, naṣb. It is owned by {الشَّمْسِ}, so no tanween: {طُلُوعَ}."},
                {"s": "جَاءَ أَبُوكَ ___", "gloss": "Your father came walking.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَاشِيًا", "مَاشٍ", "مَاشِيَيْنِ")},
                 "why": "A manqūṣ word in naṣb shows the fatha on the {ي}: {مَاشِيًا}. One father, so not the dual."},
            ],
        },
        {
            "title": "Job and sign of the word in [ ]",
            "fields": [
                {"key": "job", "label": "Job", "options": [AND, MAAH, STATE]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, WAW, YA]},
            ],
            "rows": [
                {"s": "خَرَجَتِ المُمَرِّضَاتُ [مُسْرِعَاتٍ].", "ans": {"job": "state", "sign": "kas"}, "why": "How did they go out? A state. Sound f. plural in naṣb: kasra."},
                {"s": "سَافَرَ الأَخَوَانِ [مَسْرُورَيْنِ].", "ans": {"job": "state", "sign": "ya"}, "why": "A state for two brothers. Dual in naṣb: yāʾ."},
                {"s": "خَرَجْنَا وَ[غُرُوبَ] الشَّمْسِ.", "ans": {"job": "maah", "sign": "fat"}, "why": "Sunset does not go out. Together with, naṣb, fatha."},
                {"s": "جَاءَ الطُّلَّابُ وَ[المُدَرِّسُونَ].", "ans": {"job": "and", "sign": "waw"}, "why": "The teachers came too: \"and\". It copies the doer in rafʿ; sound m. plural: wāw."},
                {"s": "رَجَعَ الجُنُودُ [مُنْتَصِرِينَ].", "ans": {"job": "state", "sign": "ya"}, "why": "How did they come back? Victorious. Sound m. plural in naṣb: yāʾ."},
                {"s": "جَلَسَ الشَّيْخُ [مُتَّكِئًا].", "ans": {"job": "state", "sign": "fat"}, "why": "How did he sit? Leaning. A singular state: fatha."},
            ],
        },
    ],
}
