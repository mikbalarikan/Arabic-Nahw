# Stage 7, Unit 4: Purpose, time and place (المَفْعُولُ لِأَجْلِهِ وَالمَفْعُولُ فِيهِ)


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


# Canonical options (copied from STAGES_5_8_SPEC.md)
DAM = {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
FAT = {"k": "fat",   "label": "Fatha · فَتْحَةٌ",                "color": "pink"}
KAS = {"k": "kas",   "label": "Kasra · كَسْرَةٌ",                "color": "green"}
WAW = {"k": "waw",   "label": "Wāw · الوَاوُ",                   "color": "blue"}
YA = {"k": "ya",    "label": "Yāʾ · اليَاءُ",                   "color": "purple"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ",                  "color": "grey"}

RAF = {"k": "raf",  "label": "Rafʿ · رَفْعٌ",   "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ",  "color": "pink"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ",   "color": "green"}

TOPIC = {"k": "topic", "label": "Topic · مُبْتَدَأٌ",                  "color": "gold"}
VERB = {"k": "verb",  "label": "Verb · فِعْلٌ",                       "color": "navy"}
DOER = {"k": "doer",  "label": "Doer · فَاعِلٌ",                      "color": "orange"}
PREP = {"k": "prep",  "label": "After a preposition · اِسْمٌ مَجْرُورٌ",    "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ",               "color": "purple"}
OBJ = {"k": "obj",   "label": "Object · مَفْعُولٌ بِهِ",                "color": "pink"}
PURP = {"k": "purp",  "label": "Purpose · مَفْعُولٌ لِأَجْلِهِ",            "color": "teal"}
WHEN = {"k": "when",  "label": "Time/place · مَفْعُولٌ فِيهِ",            "color": "brown"}
STATE = {"k": "state", "label": "State · حَالٌ",                       "color": "olive"}


UNIT = {
    "id": "s7-purpose-time",
    "order": 4,
    "title": "Purpose, time and place",
    "ar": "المَفْعُولُ لِأَجْلِهِ وَالمَفْعُولُ فِيهِ",
    "blurb": "Why, when and where: the purpose and the time or place word are in naṣb. Meet their signs with the dual and the plurals.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 7 · UNIT 4", "title": "Why, when and where",
         "text": "In Stage 2 you met two naṣb jobs: the purpose and the time or place word. Now you see them with every kind of noun.",
         "wm": "لِأَجْلِهِ وَفِيهِ"},

        {"t": "h2", "text": "The purpose: it answers \"why?\""},
        {"t": "p", "text": "The purpose ({المَفْعُولُ لِأَجْلِهِ}) tells you why the doer did the action. It is a verbal noun (a maṣdar) like {احْتِرَامٌ} \"respect\" or {خَوْفٌ} \"fear\"."},
        {"t": "rule", "color": "teal", "title": "The purpose test",
         "text": "Ask \"why?\" after the verb. If the answer is a maṣdar and you can put {لِ} \"for\" before it, it is the purpose. {قُمْتُ احْتِرَامًا} means {قُمْتُ لِلِاحْتِرَامِ} \"I stood up out of respect\"."},
        {"t": "table", "head": ["Purpose word", "Meaning", "Example"], "rows": [
            ["احْتِرَامًا", "out of respect", "قُمْتُ احْتِرَامًا لِلمُعَلِّمِ."],
            ["طَلَبًا", "seeking", "سَافَرَ التَّاجِرُ طَلَبًا لِلرِّزْقِ."],
            ["خَوْفًا", "out of fear", "هَرَبَ اللِّصُّ خَوْفًا مِنَ الشُّرْطِيِّ."],
            ["رَغْبَةً", "out of desire", "تَصَدَّقَتِ المَرْأَةُ رَغْبَةً فِي الثَّوَابِ."],
            ["حُبًّا", "out of love", "سَاعَدْتُ أَخِي حُبًّا لَهُ."],
        ]},
        {"t": "p", "text": "The purpose is usually indefinite with tanween. It can also be owned: {ذَهَبْتُ إِلَى المَدِينَةِ طَلَبَ العِلْمِ} \"I went to the city to seek knowledge\". Then it has one fatha and no tanween."},
        {"t": "tip", "text": "A purpose word is a singular maṣdar, so its sign is almost always the fatha."},

        {"t": "h2", "text": "Time: it answers \"when?\" or \"how long?\""},
        {"t": "p", "text": "A time word ({ظَرْفُ زَمَانٍ}) tells you when the action happened or how long it went on."},
        {"t": "words", "items": [
            {"ar": "يَوْمَ", "sub": "on the day of", "color": "brown"},
            {"ar": "لَيْلَةً", "sub": "for a night", "color": "brown"},
            {"ar": "صَبَاحًا", "sub": "in the morning", "color": "brown"},
            {"ar": "مَسَاءً", "sub": "in the evening", "color": "brown"},
            {"ar": "سَاعَةً", "sub": "for an hour", "color": "brown"},
            {"ar": "شَهْرًا", "sub": "for a month", "color": "brown"},
        ]},
        {"t": "examples", "items": [
            {"ar": "رَجَعَ الأَبُ مَسَاءً.", "en": "The father came back in the evening."},
            {"ar": "سَافَرْتُ يَوْمَ الجُمُعَةِ.", "en": "I travelled on Friday.",
             "note": "{يَوْمَ} is owned by {الجُمُعَةِ}: one fatha, no tanween."},
            {"ar": "نَامَ الطِّفْلُ سَاعَةً.", "en": "The child slept for an hour."},
        ]},
        {"t": "rule", "color": "brown", "title": "The time and place test",
         "text": "You can put {فِي} \"in, at\" before it in your mind: {رَجَعَ الأَبُ مَسَاءً} is like {رَجَعَ الأَبُ فِي المَسَاءِ}. That is why it is called {المَفْعُولُ فِيهِ} \"the one in which\"."},

        {"t": "h2", "text": "Place: it answers \"where?\""},
        {"t": "p", "text": "A place word ({ظَرْفُ مَكَانٍ}) tells you where. These six are very common. They are almost always owned, so the noun after them is the owner in jarr."},
        {"t": "table", "head": ["Place word", "Meaning", "Example"], "rows": [
            ["أَمَامَ", "in front of", "وَقَفَ المُعَلِّمُ أَمَامَ الفَصْلِ."],
            ["خَلْفَ", "behind", "جَلَسَ الطِّفْلُ خَلْفَ أُمِّهِ."],
            ["فَوْقَ", "above, on top of", "طَارَ الطَّائِرُ فَوْقَ البَيْتِ."],
            ["تَحْتَ", "under", "نَامَ القِطُّ تَحْتَ السَّرِيرِ."],
            ["عِنْدَ", "at, near", "جَلَسْنَا عِنْدَ البَابِ."],
            ["بَيْنَ", "between", "جَلَسْتُ بَيْنَ الطَّالِبَيْنِ."],
        ]},
        {"t": "tip", "text": "In {جَلَسْتُ بَيْنَ الطَّالِبَيْنِ} the owner is a dual. It is in jarr, so it ends in {ـَيْنِ}."},

        {"t": "h2", "text": "The signs with every kind of noun"},
        {"t": "p", "text": "Find the job. The job gives the case. The kind of noun gives the sign. Time words come in many shapes, so you meet more signs here."},
        {"t": "table", "head": ["Kind of noun", "Example", "Sign of naṣb"], "rows": [
            ["Singular", "سَافَرْتُ شَهْرًا.", "Fatha"],
            ["Broken plural", "سَافَرْتُ أَيَّامًا.", "Fatha"],
            ["Diptote", "مَشَيْنَا دَقَائِقَ.", "Fatha (no tanween)"],
            ["Dual", "سَافَرْتُ يَوْمَيْنِ.", "Yāʾ: {ـَيْنِ}"],
            ["Sound f. plural", "نَامَ الطِّفْلُ سَاعَاتٍ.", "Kasra in place of fatha"],
        ]},
        {"t": "examples", "items": [
            {"ar": "قَامَ الطُّلَّابُ احْتِرَامًا لِلمُعَلِّمِ.", "en": "The students stood up out of respect for the teacher.",
             "note": "{احْتِرَامًا}: {مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}. Purpose, naṣb, the sign is the fatha."},
            {"ar": "سَافَرَ المُهَنْدِسُ يَوْمَيْنِ.", "en": "The engineer travelled for two days.",
             "note": "{يَوْمَيْنِ}: {ظَرْفُ زَمَانٍ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}. Time, naṣb, the sign is the yāʾ because it is a dual."},
            {"ar": "نَامَ الطِّفْلُ سَاعَاتٍ.", "en": "The child slept for hours.",
             "note": "{سَاعَاتٍ}: {ظَرْفُ زَمَانٍ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الكَسْرَةُ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ}."},
            {"ar": "وَقَفَ الوَلَدُ أَمَامَ البَيْتِ.", "en": "The boy stood in front of the house.",
             "note": "{أَمَامَ}: {ظَرْفُ مَكَانٍ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ، وَهُوَ مُضَافٌ}. {البَيْتِ}: {مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}."},
        ]},

        {"t": "h2", "text": "Same word, other jobs"},
        {"t": "p", "text": "A time or place word is only {مَفْعُولٌ فِيهِ} when it stands alone after the verb. With a preposition before it, it is in jarr. As the Topic, it is in rafʿ."},
        {"t": "table", "head": ["Sentence", "The word", "Job and case"], "rows": [
            ["سَافَرْتُ يَوْمَ الخَمِيسِ.", "يَوْمَ", "Time, naṣb"],
            ["سَافَرْتُ فِي يَوْمِ الخَمِيسِ.", "يَوْمِ", "After a preposition, jarr"],
            ["اليَوْمُ جَمِيلٌ.", "اليَوْمُ", "Topic, rafʿ"],
            ["خَرَجَ الوَلَدُ مِنْ خَلْفِ البَيْتِ.", "خَلْفِ", "After a preposition, jarr"],
        ]},
        {"t": "tip", "text": "Purpose or state? The purpose is a maṣdar and answers \"why?\": {جَاءَ احْتِرَامًا}. The state describes the doer and answers \"how?\": {جَاءَ مُسْرِعًا}."},

        {"t": "summary", "title": "In short", "items": [
            "The purpose answers \"why?\". It is a maṣdar in naṣb: {قُمْتُ احْتِرَامًا لِلمُعَلِّمِ}.",
            "The time or place word answers \"when?\", \"how long?\" or \"where?\": {رَجَعَ مَسَاءً}، {جَلَسَ أَمَامَ البَيْتِ}.",
            "Place words like {أَمَامَ}، {خَلْفَ}، {فَوْقَ}، {تَحْتَ}، {عِنْدَ}، {بَيْنَ} are owned. The next noun is the owner in jarr.",
            "Signs: fatha for singular, broken plural and diptote; yāʾ for the dual ({يَوْمَيْنِ}); kasra for the sound f. plural ({سَاعَاتٍ}).",
            "After a preposition the same word is in jarr: {فِي يَوْمِ الخَمِيسِ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Full iʿrāb: the purpose (with review)",
            "prompt": "سَافَرَ التُّجَّارُ طَلَبًا لِلرِّزْقِ.",
            "en": "The merchants travelled seeking provision.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, PURP, PREP]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, FIXED]},
            ],
            "rows": [
                {"s": "سَافَرَ", "ans": {"job": "verb", "sign": "fixed"}, "why": "A past verb. It is fixed on fatha."},
                {"s": "التُّجَّارُ", "ans": {"job": "doer", "sign": "dam"}, "why": "Who travelled? The doer, rafʿ. A broken plural takes the damma."},
                {"s": "طَلَبًا", "ans": {"job": "purp", "sign": "fat"}, "why": "Why did they travel? To seek. A maṣdar: {مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
                {"s": "لِلرِّزْقِ", "ans": {"job": "prep", "sign": "kas"}, "why": "After the preposition {لِ}: jarr with kasra."},
            ],
        },
        {
            "title": "Full iʿrāb: time and place (with review)",
            "prompt": "جَلَسَ المُعَلِّمُونَ أَمَامَ الطُّلَّابِ سَاعَتَيْنِ.",
            "en": "The teachers sat in front of the students for two hours.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, WHEN, OWNER, OBJ]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, WAW, YA]},
            ],
            "rows": [
                {"s": "المُعَلِّمُونَ", "ans": {"job": "doer", "sign": "waw"}, "why": "The doer, rafʿ. A sound m. plural: the sign is the wāw."},
                {"s": "أَمَامَ", "ans": {"job": "when", "sign": "fat"}, "why": "Where did they sit? A place word: {ظَرْفُ مَكَانٍ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}. It is owned, so no tanween."},
                {"s": "الطُّلَّابِ", "ans": {"job": "owner", "sign": "kas"}, "why": "It is owned by {أَمَامَ}: owner, jarr with kasra."},
                {"s": "سَاعَتَيْنِ", "ans": {"job": "when", "sign": "ya"}, "why": "How long? A time word in naṣb. It is a dual, so the sign is the yāʾ: {سَاعَتَيْنِ}."},
            ],
        },
        {
            "title": "Why, when, where or how?",
            "fields": [{"key": "job", "label": "Job of the word in [ ]", "options": [OBJ, PURP, WHEN, STATE]}],
            "rows": [
                {"s": "رَجَعَ الأَبُ [لَيْلًا].", "ans": {"job": "when"}, "why": "When did he come back? At night. A time word."},
                {"s": "قُمْتُ [احْتِرَامًا] لِلضَّيْفِ.", "ans": {"job": "purp"}, "why": "Why did I stand up? Out of respect. A maṣdar giving the reason."},
                {"s": "خَرَجَ الوَلَدُ [مُسْرِعًا].", "ans": {"job": "state"}, "why": "How did he go out? Hurrying. {مُسْرِعًا} describes the boy, so it is the state."},
                {"s": "وَقَفَ الطَّالِبُ [أَمَامَ] السَّبُّورَةِ.", "ans": {"job": "when"}, "why": "Where did he stand? In front of the board. A place word."},
                {"s": "كَتَبَ الطَّالِبُ [الدَّرْسَ].", "ans": {"job": "obj"}, "why": "What did he write? The lesson. The action falls on it: the object."},
                {"s": "هَرَبَ القِطُّ [خَوْفًا] مِنَ الكَلْبِ.", "ans": {"job": "purp"}, "why": "Why did the cat run away? Out of fear. A maṣdar giving the reason."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "غَابَ الطَّالِبُ ___", "gloss": "The student was absent for two days.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَوْمَانِ", "يَوْمَيْنِ", "يَوْمِينَ")},
                 "why": "A time word in naṣb. The dual in naṣb ends in {ـَيْنِ}: {يَوْمَيْنِ}."},
                {"s": "جَلَسْتُ ___ البَيْتِ", "gloss": "I sat in front of the house.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَمَامَ", "أَمَامِ", "أَمَامًا")},
                 "why": "A place word in naṣb. It is owned, so one fatha and no tanween: {أَمَامَ}."},
                {"s": "قُمْتُ ___ لِلمُعَلِّمِ", "gloss": "I stood up out of respect for the teacher.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("احْتِرَامٌ", "احْتِرَامٍ", "احْتِرَامًا")},
                 "why": "The purpose is in naṣb: fatha with tanween, {احْتِرَامًا}."},
                {"s": "أَقَامَ التَّاجِرُ فِي المَدِينَةِ ___", "gloss": "The merchant stayed in the city for two months.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("شَهْرَانِ", "شَهْرَيْنِ", "شَهْرِينَ")},
                 "why": "How long? A time word in naṣb. Dual: {شَهْرَيْنِ}. {ـِينَ} is the sound m. plural shape."},
                {"s": "سَافَرَ الرَّجُلُ ___", "gloss": "The man travelled for days.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَيَّامًا", "أَيَّامٍ", "أَيَّامٌ")},
                 "why": "{أَيَّامٌ} is a broken plural. In naṣb it takes the fatha: {أَيَّامًا}."},
                {"s": "جَلَسَ الشَّيْخُ فِي المَسْجِدِ ___", "gloss": "The old man sat in the mosque for hours.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("سَاعَاتًا", "سَاعَاتٌ", "سَاعَاتٍ")},
                 "why": "A sound f. plural takes the kasra in naṣb: {سَاعَاتٍ}. {سَاعَاتًا} is a common mistake."},
            ],
        },
        {
            "title": "Which sign does the word in [ ] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, YA]}],
            "rows": [
                {"s": "سَهِرْتُ [لَيْلَتَيْنِ].", "gloss": "I stayed up for two nights.", "ans": {"sign": "ya"}, "why": "Time, naṣb. A dual: the sign is the yāʾ."},
                {"s": "جَلَسَ القِطُّ [تَحْتَ] الكُرْسِيِّ.", "gloss": "The cat sat under the chair.", "ans": {"sign": "fat"}, "why": "Place, naṣb. A singular: the sign is the fatha."},
                {"s": "مَشَى الرِّجَالُ [سَاعَاتٍ].", "gloss": "The men walked for hours.", "ans": {"sign": "kas"}, "why": "Time, naṣb. A sound f. plural: the kasra stands in place of the fatha."},
                {"s": "وَقَفَ الطُّلَّابُ [احْتِرَامًا] لِلمُدِيرِ.", "gloss": "The students stood up out of respect for the principal.", "ans": {"sign": "fat"}, "why": "Purpose, naṣb. A singular maṣdar: fatha."},
                {"s": "جَلَسَ المُدِيرُ [بَيْنَ] المُعَلِّمَيْنِ.", "gloss": "The principal sat between the two teachers.", "ans": {"sign": "fat"}, "why": "{بَيْنَ} is the place word, naṣb with fatha. The dual after it is the owner."},
                {"s": "سَافَرَ أَخِي [صَبَاحًا].", "gloss": "My brother travelled in the morning.", "ans": {"sign": "fat"}, "why": "Time, naṣb. A singular: fatha with tanween."},
            ],
        },
        {
            "title": "Time/place, or another job?",
            "fields": [
                {"key": "job", "label": "Job of the word in [ ]", "options": [WHEN, PREP, TOPIC]},
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR]},
            ],
            "rows": [
                {"s": "سَافَرْتُ [يَوْمَ] الخَمِيسِ.", "ans": {"job": "when", "case": "nasb"}, "why": "It stands alone after the verb and answers \"when?\": time, naṣb."},
                {"s": "سَافَرْتُ فِي [يَوْمِ] الخَمِيسِ.", "ans": {"job": "prep", "case": "jarr"}, "why": "The preposition {فِي} comes before it: jarr."},
                {"s": "[اليَوْمُ] جَمِيلٌ.", "ans": {"job": "topic", "case": "raf"}, "why": "The sentence is about the day. It is the Topic, rafʿ."},
                {"s": "جَلَسْتُ [خَلْفَ] المَسْجِدِ.", "ans": {"job": "when", "case": "nasb"}, "why": "Where did I sit? A place word in naṣb."},
                {"s": "خَرَجَ الوَلَدُ مِنْ [خَلْفِ] البَيْتِ.", "ans": {"job": "prep", "case": "jarr"}, "why": "After the preposition {مِنْ}: jarr with kasra."},
                {"s": "[اللَّيْلُ] طَوِيلٌ.", "ans": {"job": "topic", "case": "raf"}, "why": "The night is what we talk about: Topic, rafʿ."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Full iʿrāb: the purpose (with review)",
            "prompt": "وَقَفَتِ الطَّالِبَاتُ احْتِرَامًا لِلمُعَلِّمَةِ.",
            "en": "The female students stood up out of respect for the teacher.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, PURP, PREP]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, FIXED]},
            ],
            "rows": [
                {"s": "وَقَفَتِ", "ans": {"job": "verb", "sign": "fixed"}, "why": "A past verb, fixed on fatha. The {تِ} shows a feminine doer."},
                {"s": "الطَّالِبَاتُ", "ans": {"job": "doer", "sign": "dam"}, "why": "The doer, rafʿ. A sound f. plural takes the damma in rafʿ."},
                {"s": "احْتِرَامًا", "ans": {"job": "purp", "sign": "fat"}, "why": "Why did they stand? Out of respect. Purpose, naṣb, fatha."},
                {"s": "لِلمُعَلِّمَةِ", "ans": {"job": "prep", "sign": "kas"}, "why": "After {لِ}: jarr with kasra."},
            ],
        },
        {
            "title": "Full iʿrāb: place and time (with review)",
            "prompt": "جَلَسَ أَبُوكَ بَيْنَ الرَّجُلَيْنِ سَاعَةً.",
            "en": "Your father sat between the two men for an hour.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, WHEN, OWNER, OBJ]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, WAW, YA]},
            ],
            "rows": [
                {"s": "أَبُوكَ", "ans": {"job": "doer", "sign": "waw"}, "why": "The doer, rafʿ. One of the five nouns: the sign is the wāw."},
                {"s": "بَيْنَ", "ans": {"job": "when", "sign": "fat"}, "why": "Where did he sit? A place word, naṣb with fatha. It is owned."},
                {"s": "الرَّجُلَيْنِ", "ans": {"job": "owner", "sign": "ya"}, "why": "Owned by {بَيْنَ}: owner, jarr. A dual: the sign is the yāʾ."},
                {"s": "سَاعَةً", "ans": {"job": "when", "sign": "fat"}, "why": "How long? A time word, naṣb with fatha and tanween."},
            ],
        },
        {
            "title": "Object, purpose, time/place or state?",
            "fields": [{"key": "job", "label": "Job of the word in [ ]", "options": [OBJ, PURP, WHEN, STATE]}],
            "rows": [
                {"s": "أَكْرَمْتُ الضَّيْفَ [حُبًّا] لَهُ.", "ans": {"job": "purp"}, "why": "Why did I honour him? Out of love. A maṣdar giving the reason."},
                {"s": "رَجَعَ الجُنْدِيُّ [مَسَاءً].", "ans": {"job": "when"}, "why": "When did he come back? In the evening. A time word."},
                {"s": "رَجَعَ الجُنْدِيُّ [مُتْعَبًا].", "ans": {"job": "state"}, "why": "How did he come back? Tired. It describes the soldier: the state."},
                {"s": "تَرَكْتُ الكَذِبَ [خَوْفًا] مِنَ اللّٰهِ.", "ans": {"job": "purp"}, "why": "Why did I leave lying? Out of fear of Allah. {الكَذِبَ} is the object, {خَوْفًا} is the purpose."},
                {"s": "وَضَعْتُ الكِتَابَ [فَوْقَ] المَكْتَبِ.", "ans": {"job": "when"}, "why": "Where did I put it? On top of the desk. A place word."},
                {"s": "أَعْطَيْتُ الفَقِيرَ [مَالًا].", "ans": {"job": "obj"}, "why": "What did I give? Money. {أَعْطَى} takes two objects: {الفَقِيرَ} and {مَالًا}."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "سَهِرَ الطَّالِبُ ___", "gloss": "The student stayed up for two nights.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَيْلَتَانِ", "لَيْلَتَيْنِ", "لَيْلَةَيْنِ")},
                 "why": "Time in naṣb, a dual: {ـَيْنِ}. The {ة} becomes {ت} inside the word."},
                {"s": "أَقَمْنَا فِي مَكَّةَ ___", "gloss": "We stayed in Makka for two weeks.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أُسْبُوعَيْنِ", "أُسْبُوعَانِ", "أُسْبُوعِينَ")},
                 "why": "How long? Time in naṣb. The dual ends in {ـَيْنِ}: {أُسْبُوعَيْنِ}."},
                {"s": "جَلَسْنَا فِي الحَدِيقَةِ ___", "gloss": "We sat in the garden for minutes.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("دَقَائِقًا", "دَقَائِقٍ", "دَقَائِقَ")},
                 "why": "{دَقَائِقُ} is a diptote. In naṣb it takes one fatha and never tanween: {دَقَائِقَ}."},
                {"s": "ذَهَبَ أَخِي إِلَى المَدِينَةِ ___ العِلْمِ", "gloss": "My brother went to the city to seek knowledge.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("طَلَبَ", "طَلَبًا", "طَلَبِ")},
                 "why": "The purpose is owned by {العِلْمِ}, so it has one fatha and no tanween: {طَلَبَ}."},
                {"s": "تَصَدَّقَ الرَّجُلُ ___ فِي الأَجْرِ", "gloss": "The man gave charity out of desire for the reward.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("رَغْبَةٌ", "رَغْبَةً", "رَغْبَةٍ")},
                 "why": "Why did he give? Purpose, naṣb: {رَغْبَةً}."},
                {"s": "صَلَّيْنَا ___ الإِمَامِ", "gloss": "We prayed behind the imam.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("خَلْفِ", "خَلْفًا", "خَلْفَ")},
                 "why": "A place word in naṣb, owned by {الإِمَامِ}: {خَلْفَ}."},
            ],
        },
        {
            "title": "Which sign does the word in [ ] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, YA]}],
            "rows": [
                {"s": "سَافَرَ الرَّجُلُ [شَهْرَيْنِ].", "gloss": "The man travelled for two months.", "ans": {"sign": "ya"}, "why": "Time, naṣb, a dual: {ظَرْفُ زَمَانٍ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
                {"s": "جَلَسْنَا [عِنْدَ] أَبِيكَ.", "gloss": "We sat with your father.", "ans": {"sign": "fat"}, "why": "A place word, naṣb with fatha. {أَبِيكَ} is the owner."},
                {"s": "عَمِلَ العُمَّالُ [سَاعَاتٍ] طَوِيلَةً.", "gloss": "The workers worked for long hours.", "ans": {"sign": "kas"}, "why": "Time, naṣb. A sound f. plural: kasra in place of fatha. The adjective {طَوِيلَةً} follows it in naṣb."},
                {"s": "رَجَعَ المُسَافِرُونَ [لَيْلًا].", "gloss": "The travellers came back at night.", "ans": {"sign": "fat"}, "why": "Time, naṣb, singular: fatha."},
                {"s": "جَلَسَ الأَوْلَادُ بَيْنَ [الشَّجَرَتَيْنِ].", "gloss": "The boys sat between the two trees.", "ans": {"sign": "ya"}, "why": "Review: it is the owner of {بَيْنَ}, in jarr. A dual in jarr takes the yāʾ."},
                {"s": "وَقَفَ الحَارِسُ [خَلْفَ] البَابِ.", "gloss": "The guard stood behind the door.", "ans": {"sign": "fat"}, "why": "A place word, naṣb with fatha."},
            ],
        },
        {
            "title": "Time/place, or another job?",
            "fields": [
                {"key": "job", "label": "Job of the word in [ ]", "options": [WHEN, PREP, TOPIC]},
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR]},
            ],
            "rows": [
                {"s": "[الصَّبَاحُ] جَمِيلٌ.", "ans": {"job": "topic", "case": "raf"}, "why": "The morning is what we talk about: Topic, rafʿ."},
                {"s": "خَرَجْتُ [صَبَاحًا].", "ans": {"job": "when", "case": "nasb"}, "why": "When did I go out? A time word in naṣb."},
                {"s": "نِمْتُ فِي [اللَّيْلِ].", "ans": {"job": "prep", "case": "jarr"}, "why": "After {فِي}: jarr."},
                {"s": "جَلَسْتُ [تَحْتَ] الشَّجَرَةِ.", "ans": {"job": "when", "case": "nasb"}, "why": "Where did I sit? A place word in naṣb."},
                {"s": "سَقَطَ الكِتَابُ مِنْ [فَوْقِ] المَكْتَبِ.", "ans": {"job": "prep", "case": "jarr"}, "why": "After the preposition {مِنْ}: jarr with kasra."},
                {"s": "رَأَيْتُ القَمَرَ [لَيْلًا].", "ans": {"job": "when", "case": "nasb"}, "why": "When did I see it? At night. {القَمَرَ} is the object; {لَيْلًا} is the time."},
            ],
        },
    ],
}
