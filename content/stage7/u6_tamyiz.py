# Stage 7, Unit 6: The specifier (التَّمْيِيزُ)


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


# Canonical options (copied from STAGES_5_8_SPEC.md)
DAM = {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
FAT = {"k": "fat",   "label": "Fatha · فَتْحَةٌ",                "color": "pink"}
KAS = {"k": "kas",   "label": "Kasra · كَسْرَةٌ",                "color": "green"}
WAW = {"k": "waw",   "label": "Wāw · الوَاوُ",                   "color": "blue"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ",                  "color": "grey"}

NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ",  "color": "pink"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ",   "color": "green"}

TOPIC = {"k": "topic", "label": "Topic · مُبْتَدَأٌ",                  "color": "gold"}
INFO = {"k": "info",  "label": "Information · خَبَرٌ",                "color": "red"}
VERB = {"k": "verb",  "label": "Verb · فِعْلٌ",                       "color": "navy"}
DOER = {"k": "doer",  "label": "Doer · فَاعِلٌ",                      "color": "orange"}
PREP = {"k": "prep",  "label": "After a preposition · اِسْمٌ مَجْرُورٌ",    "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ",               "color": "purple"}
OBJ = {"k": "obj",   "label": "Object · مَفْعُولٌ بِهِ",                "color": "pink"}
WHEN = {"k": "when",  "label": "Time/place · مَفْعُولٌ فِيهِ",            "color": "brown"}
STATE = {"k": "state", "label": "State · حَالٌ",                       "color": "olive"}
TAMY = {"k": "tamy",  "label": "Specifier · تَمْيِيزٌ",                 "color": "gold"}


UNIT = {
    "id": "s7-tamyiz",
    "order": 6,
    "title": "The specifier",
    "ar": "التَّمْيِيزُ",
    "blurb": "\"A pound of what?\" The specifier makes a vague word clear: after measures, after the numbers 11 to 99, and after a whole sentence.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 7 · UNIT 6", "title": "Of what? In what respect?",
         "text": "Some words leave the listener asking \"of what?\". The specifier ({التَّمْيِيزُ}) answers that question. It is in naṣb.",
         "wm": "التَّمْيِيزُ"},

        {"t": "h2", "text": "What is the specifier?"},
        {"t": "p", "text": "If I say {اِشْتَرَيْتُ رِطْلًا} \"I bought a pound\", you ask: a pound of what? The word that answers is the specifier: {اِشْتَرَيْتُ رِطْلًا زَيْتًا} \"I bought a pound of oil\"."},
        {"t": "rule", "color": "gold", "title": "Three marks of the specifier",
         "text": "1. It is indefinite, usually with tanween. 2. It is in naṣb. 3. It answers \"of what?\" or \"in what respect?\"."},
        {"t": "p", "text": "Full iʿrāb: {زَيْتًا}: {تَمْيِيزٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}. The specifier is almost always a singular noun, so its sign is the fatha."},

        {"t": "h2", "text": "After measures and amounts"},
        {"t": "p", "text": "Weights, volumes, lengths and amounts are vague. The specifier tells you what is measured."},
        {"t": "table", "head": ["Measure", "Specifier", "Sentence", "Meaning"], "rows": [
            ["رِطْلًا", "زَيْتًا", "اِشْتَرَيْتُ رِطْلًا زَيْتًا.", "I bought a pound of oil."],
            ["صَاعًا", "قَمْحًا", "بَاعَ الفَلَّاحُ صَاعًا قَمْحًا.", "The farmer sold a ṣāʿ of wheat."],
            ["ذِرَاعًا", "قُمَاشًا", "اِشْتَرَتِ الأُمُّ ذِرَاعًا قُمَاشًا.", "The mother bought an arm's length of cloth."],
            ["كُوبًا", "لَبَنًا", "شَرِبَ الطِّفْلُ كُوبًا لَبَنًا.", "The child drank a cup of milk."],
        ]},
        {"t": "p", "text": "In {اِشْتَرَيْتُ رِطْلًا زَيْتًا} the measure {رِطْلًا} is the object. The specifier {زَيْتًا} comes after it."},
        {"t": "tip", "text": "You may also make the measure own the next word: {اِشْتَرَيْتُ رِطْلَ زَيْتٍ}. Then {زَيْتٍ} is the owner in jarr, and {رِطْلَ} loses its tanween."},

        {"t": "h2", "text": "After the numbers 11 to 99"},
        {"t": "p", "text": "After the numbers 11 to 99 the counted noun is a specifier: singular, indefinite, in naṣb."},
        {"t": "table", "head": ["Number", "Sentence", "Meaning"], "rows": [
            ["11", "رَأَى يُوسُفُ أَحَدَ عَشَرَ كَوْكَبًا.", "Yūsuf saw eleven stars."],
            ["12", "فِي السَّنَةِ اثْنَا عَشَرَ شَهْرًا.", "In the year there are twelve months."],
            ["15", "سَافَرْتُ خَمْسَةَ عَشَرَ يَوْمًا.", "I travelled for fifteen days."],
            ["20", "فِي الفَصْلِ عِشْرُونَ طَالِبًا.", "In the classroom there are twenty students."],
            ["30", "قَرَأْتُ ثَلَاثِينَ صَفْحَةً.", "I read thirty pages."],
        ]},
        {"t": "examples", "items": [
            {"ar": "إِنِّي رَأَيْتُ أَحَدَ عَشَرَ كَوْكَبًا", "en": "I saw eleven stars (Yūsuf 12:4)",
             "note": "{كَوْكَبًا}: {تَمْيِيزٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
            {"ar": "لَهُ تِسْعٌ وَتِسْعُونَ نَعْجَةً", "en": "He has ninety-nine ewes (Ṣād 38:23)",
             "note": "{نَعْجَةً}: specifier of the number, naṣb with fatha."},
        ]},
        {"t": "tip", "text": "The number word itself can change ({عِشْرُونَ} / {عِشْرِينَ}). The specifier after it stays the same: singular and in naṣb. The numbers 3 to 10 work differently: they own a plural in jarr, {ثَلَاثَةُ كُتُبٍ}."},

        {"t": "h2", "text": "The specifier of a sentence"},
        {"t": "p", "text": "Sometimes a whole sentence is vague. {طَابَ زَيْدٌ} \"Zayd was good\": good in what respect? The specifier tells you."},
        {"t": "table", "head": ["Sentence", "Meaning", "In what respect?"], "rows": [
            ["طَابَ زَيْدٌ نَفْسًا.", "Zayd was content.", "نَفْسًا: in himself"],
            ["اِمْتَلَأَ الإِنَاءُ مَاءً.", "The vessel was filled with water.", "مَاءً: with what?"],
            ["حَسُنَ الوَلَدُ خُلُقًا.", "The boy was good in character.", "خُلُقًا: in character"],
            ["زَيْدٌ أَكْثَرُ مِنْكَ مَالًا.", "Zayd has more money than you.", "مَالًا: more in what?"],
        ]},
        {"t": "examples", "items": [
            {"ar": "وَاشْتَعَلَ الرَّأْسُ شَيْبًا", "en": "And the head has filled with grey hair (Maryam 19:4)",
             "note": "{شَيْبًا}: lit with what? A specifier in naṣb."},
            {"ar": "أَنَا أَكْثَرُ مِنْكَ مَالًا", "en": "I have more wealth than you (al-Kahf 18:34)",
             "note": "{أَكْثَرُ}: Information, rafʿ. {مَالًا}: {تَمْيِيزٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
        ]},
        {"t": "tip", "text": "After {أَكْثَرُ}، {أَحْسَنُ}، {أَكْبَرُ} \"more, better, bigger\" look for a specifier: {أَنَا أَكْبَرُ مِنْكَ سِنًّا} \"I am older than you\"."},

        {"t": "h2", "text": "Specifier or state?"},
        {"t": "p", "text": "Both are indefinite and in naṣb. Ask two questions."},
        {"t": "cols", "items": [
            {"color": "gold", "title": "Specifier", "ar": "تَمْيِيزٌ",
             "text": "A thing word: {مَاءً}، {زَيْتًا}، {نَفْسًا}. It answers \"of what?\" or \"in what respect?\": {اِمْتَلَأَ الكُوبُ مَاءً}."},
            {"color": "olive", "title": "State", "ar": "حَالٌ",
             "text": "A describing word: {مُسْرِعًا}، {فَرِحًا}. It answers \"how?\": {رَجَعَ الوَلَدُ مَسْرُورًا}."},
        ]},
        {"t": "tip", "text": "Try \"in what respect?\". {طَابَ الطَّالِبُ نَفْسًا}: in himself, so a specifier. {جَاءَ الضَّيْفُ رَاكِبًا}: how did he come? Riding, so a state."},

        {"t": "summary", "title": "In short", "items": [
            "The specifier answers \"of what?\" or \"in what respect?\". It is indefinite and in naṣb.",
            "After measures: {اِشْتَرَيْتُ رِطْلًا زَيْتًا}. With the owned form, {رِطْلَ زَيْتٍ}, the next word is the owner in jarr.",
            "After 11 to 99: a singular in naṣb: {أَحَدَ عَشَرَ كَوْكَبًا}، {عِشْرُونَ طَالِبًا}.",
            "Of a sentence: {طَابَ زَيْدٌ نَفْسًا}، {اِمْتَلَأَ الإِنَاءُ مَاءً}، {زَيْدٌ أَكْثَرُ مِنْكَ مَالًا}.",
            "Full iʿrāb: {تَمْيِيزٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}.",
            "A thing word answering \"of what?\" is a specifier. A describing word answering \"how?\" is a state.",
        ]},
    ],

    "practice": [
        {
            "title": "Full iʿrāb: after a measure (with review)",
            "prompt": "اِشْتَرَى التَّاجِرُ رِطْلًا زَيْتًا.",
            "en": "The merchant bought a pound of oil.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, TAMY]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, FIXED]},
            ],
            "rows": [
                {"s": "اِشْتَرَى", "ans": {"job": "verb", "sign": "fixed"}, "why": "A past verb. It is fixed."},
                {"s": "التَّاجِرُ", "ans": {"job": "doer", "sign": "dam"}, "why": "Who bought? The doer, rafʿ with damma."},
                {"s": "رِطْلًا", "ans": {"job": "obj", "sign": "fat"}, "why": "What did he buy? A pound. The object, naṣb with fatha."},
                {"s": "زَيْتًا", "ans": {"job": "tamy", "sign": "fat"}, "why": "A pound of what? Of oil. {تَمْيِيزٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
            ],
        },
        {
            "title": "Full iʿrāb: specifier of a sentence (with review)",
            "prompt": "اِمْتَلَأَ كُوبُ الطِّفْلِ حَلِيبًا.",
            "en": "The child's cup was filled with milk.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OWNER, TAMY]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, FIXED]},
            ],
            "rows": [
                {"s": "اِمْتَلَأَ", "ans": {"job": "verb", "sign": "fixed"}, "why": "A past verb, fixed on fatha."},
                {"s": "كُوبُ", "ans": {"job": "doer", "sign": "dam"}, "why": "What was filled? The cup. The doer, rafʿ. It is owned, so no tanween."},
                {"s": "الطِّفْلِ", "ans": {"job": "owner", "sign": "kas"}, "why": "Owned by {كُوبُ}: owner, jarr with kasra."},
                {"s": "حَلِيبًا", "ans": {"job": "tamy", "sign": "fat"}, "why": "Filled with what? Milk. A specifier in naṣb."},
            ],
        },
        {
            "title": "Specifier or state?",
            "fields": [{"key": "job", "label": "Job of the word in [ ]", "options": [TAMY, STATE]}],
            "rows": [
                {"s": "اِمْتَلَأَتِ البِئْرُ [مَاءً].", "ans": {"job": "tamy"}, "why": "Filled with what? Water. A thing word: specifier."},
                {"s": "رَجَعَ الحُجَّاجُ [مَسْرُورِينَ].", "ans": {"job": "state"}, "why": "How did they come back? Happy. A describing word: state. Its sign is the yāʾ."},
                {"s": "طَابَ العَامِلُ [نَفْسًا].", "ans": {"job": "tamy"}, "why": "Good in what respect? In himself. Specifier."},
                {"s": "جَاءَ الضَّيْفُ [مَاشِيًا].", "ans": {"job": "state"}, "why": "How did he come? Walking. State."},
                {"s": "اِشْتَرَيْتُ رِطْلًا [عَسَلًا].", "ans": {"job": "tamy"}, "why": "A pound of what? Honey. Specifier after a measure."},
                {"s": "حَسُنَ الجَارُ [خُلُقًا].", "ans": {"job": "tamy"}, "why": "Good in what respect? In character. Specifier."},
            ],
        },
        {
            "title": "Which form is right after the number?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "فِي البَيْتِ أَحَدَ عَشَرَ ___", "gloss": "In the house there are eleven chairs.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("كُرْسِيًّا", "كَرَاسِيَّ", "كُرْسِيٍّ")},
                 "why": "After 11 to 99: a singular in naṣb, {كُرْسِيًّا}."},
                {"s": "فِي المَدْرَسَةِ عِشْرُونَ ___", "gloss": "In the school there are twenty teachers.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُعَلِّمِينَ", "مُعَلِّمًا", "مُعَلِّمٍ")},
                 "why": "The specifier of {عِشْرُونَ} is singular and in naṣb: {مُعَلِّمًا}."},
                {"s": "كَتَبْتُ اثْنَيْ عَشَرَ ___", "gloss": "I wrote twelve lines.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("سُطُورًا", "سَطْرٌ", "سَطْرًا")},
                 "why": "Singular, indefinite, naṣb: {سَطْرًا}."},
                {"s": "قَرَأْتُ خَمْسِينَ ___", "gloss": "I read fifty pages.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("صَفْحَةً", "صَفَحَاتٍ", "صَفْحَةٍ")},
                 "why": "After {خَمْسِينَ}: a singular in naṣb, {صَفْحَةً}."},
                {"s": "أَقَمْتُ فِي المَدِينَةِ خَمْسَةَ عَشَرَ ___", "gloss": "I stayed in the city for fifteen days.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَيَّامًا", "يَوْمًا", "يَوْمٍ")},
                 "why": "After 11 to 99 the specifier is singular: {يَوْمًا}."},
                {"s": "اِشْتَرَيْتُ ثَلَاثَةَ ___", "gloss": "I bought three books.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("كِتَابًا", "كُتُبًا", "كُتُبٍ")},
                 "why": "3 to 10 are different: they own a plural in jarr, {ثَلَاثَةَ كُتُبٍ}."},
            ],
        },
        {
            "title": "After a measure: specifier, object or owner?",
            "fields": [
                {"key": "job", "label": "Job of the word in [ ]", "options": [OBJ, TAMY, OWNER]},
                {"key": "case", "label": "Case", "options": [NASB, JARR]},
            ],
            "rows": [
                {"s": "اِشْتَرَيْتُ رِطْلًا [لَحْمًا].", "ans": {"job": "tamy", "case": "nasb"}, "why": "A pound of what? Meat. Specifier, naṣb."},
                {"s": "اِشْتَرَيْتُ رِطْلَ [لَحْمٍ].", "ans": {"job": "owner", "case": "jarr"}, "why": "{رِطْلَ} has no tanween: it owns {لَحْمٍ}. Owner, jarr."},
                {"s": "بِعْتُ صَاعًا [قَمْحًا].", "ans": {"job": "tamy", "case": "nasb"}, "why": "A ṣāʿ of what? Wheat. Specifier, naṣb."},
                {"s": "بِعْتُ [صَاعًا] قَمْحًا.", "ans": {"job": "obj", "case": "nasb"}, "why": "What did I sell? A ṣāʿ. The measure is the object."},
                {"s": "شَرِبْتُ كُوبًا [لَبَنًا].", "ans": {"job": "tamy", "case": "nasb"}, "why": "A cup of what? Milk. Specifier, naṣb."},
                {"s": "اِشْتَرَتِ الأُمُّ ذِرَاعَ [قُمَاشٍ].", "ans": {"job": "owner", "case": "jarr"}, "why": "{ذِرَاعَ} owns the next word. Owner, jarr with kasra."},
            ],
        },
        {
            "title": "Full iʿrāb: more in what? (with review)",
            "prompt": "الطَّالِبَةُ أَحْسَنُ مِنْ أُخْتِهَا خَطًّا.",
            "en": "The student has better handwriting than her sister.",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, INFO, PREP, TAMY]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS]},
            ],
            "rows": [
                {"s": "الطَّالِبَةُ", "ans": {"job": "topic", "sign": "dam"}, "why": "The sentence is about her: Topic, rafʿ with damma."},
                {"s": "أَحْسَنُ", "ans": {"job": "info", "sign": "dam"}, "why": "What is said about her: Information, rafʿ with damma. A diptote, so no tanween."},
                {"s": "أُخْتِهَا", "ans": {"job": "prep", "sign": "kas"}, "why": "After {مِنْ}: jarr with kasra."},
                {"s": "خَطًّا", "ans": {"job": "tamy", "sign": "fat"}, "why": "Better in what respect? In handwriting. {تَمْيِيزٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Full iʿrāb: specifier of a sentence (with review)",
            "prompt": "طَابَ المُسَافِرُونَ نَفْسًا بَعْدَ الرِّحْلَةِ.",
            "en": "The travellers were content after the trip.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, TAMY, WHEN, OWNER]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, WAW]},
            ],
            "rows": [
                {"s": "المُسَافِرُونَ", "ans": {"job": "doer", "sign": "waw"}, "why": "The doer, rafʿ. Sound m. plural: wāw."},
                {"s": "نَفْسًا", "ans": {"job": "tamy", "sign": "fat"}, "why": "Good in what respect? In themselves. Specifier, naṣb with fatha. It stays singular."},
                {"s": "بَعْدَ", "ans": {"job": "when", "sign": "fat"}, "why": "When? After the trip. A time word, naṣb with fatha, owned."},
                {"s": "الرِّحْلَةِ", "ans": {"job": "owner", "sign": "kas"}, "why": "Owned by {بَعْدَ}: owner, jarr with kasra."},
            ],
        },
        {
            "title": "Full iʿrāb: after a number (with review)",
            "prompt": "أَعْطَى الأَبُ ابْنَهُ عِشْرِينَ دِرْهَمًا.",
            "en": "The father gave his son twenty dirhams.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, TAMY]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, FIXED]},
            ],
            "rows": [
                {"s": "أَعْطَى", "ans": {"job": "verb", "sign": "fixed"}, "why": "A past verb. It is fixed."},
                {"s": "الأَبُ", "ans": {"job": "doer", "sign": "dam"}, "why": "The doer, rafʿ. Not owned, so it is a normal noun with damma."},
                {"s": "ابْنَهُ", "ans": {"job": "obj", "sign": "fat"}, "why": "The first object of {أَعْطَى}, naṣb with fatha."},
                {"s": "دِرْهَمًا", "ans": {"job": "tamy", "sign": "fat"}, "why": "Twenty of what? Dirhams. The specifier of the number: singular, naṣb, fatha."},
            ],
        },
        {
            "title": "Specifier or state?",
            "fields": [{"key": "job", "label": "Job of the word in [ ]", "options": [TAMY, STATE]}],
            "rows": [
                {"s": "اِمْتَلَأَ القَلْبُ [فَرَحًا].", "ans": {"job": "tamy"}, "why": "Filled with what? Joy. A specifier. Compare {فَرِحًا} \"happy\", a describing word."},
                {"s": "خَرَجَ الرَّجُلُ [غَاضِبًا].", "ans": {"job": "state"}, "why": "How did he go out? Angry. State."},
                {"s": "أَبِي أَكْبَرُ مِنْ عَمِّي [سِنًّا].", "ans": {"job": "tamy"}, "why": "Bigger in what respect? In age. Specifier."},
                {"s": "جَلَسَ الطَّالِبُ [صَامِتًا].", "ans": {"job": "state"}, "why": "How did he sit? Silent. State."},
                {"s": "عِنْدِي عِشْرُونَ [قَلَمًا].", "ans": {"job": "tamy"}, "why": "Twenty of what? Pens. The specifier of a number."},
                {"s": "وَقَفَتِ البِنْتُ [خَائِفَةً].", "ans": {"job": "state"}, "why": "How did she stand? Afraid. A describing word: state."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "اِشْتَرَيْتُ صَاعًا ___", "gloss": "I bought a ṣāʿ of dates.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَمْرًا", "تَمْرٍ", "التَّمْرَ")},
                 "why": "After {صَاعًا} with tanween: a specifier, indefinite, naṣb."},
                {"s": "اِشْتَرَيْتُ صَاعَ ___", "gloss": "I bought a ṣāʿ of dates.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَمْرًا", "تَمْرٍ", "تَمْرٌ")},
                 "why": "{صَاعَ} has no tanween: it owns the next word. Owner, jarr: {تَمْرٍ}."},
                {"s": "فِي الشَّهْرِ ثَلَاثُونَ ___", "gloss": "In the month there are thirty days.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَيَّامًا", "يَوْمٍ", "يَوْمًا")},
                 "why": "After 11 to 99: singular, naṣb, {يَوْمًا}."},
                {"s": "زَيْدٌ أَحْسَنُ مِنْ عَمْرٍو ___", "gloss": "Zayd is better than ʿAmr in character.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("خُلُقًا", "الخُلُقَ", "خُلُقٌ")},
                 "why": "The specifier is indefinite and in naṣb: {خُلُقًا}."},
                {"s": "قَرَأْتُ أَرْبَعِينَ ___", "gloss": "I read forty ḥadīths.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَحَادِيثَ", "حَدِيثًا", "حَدِيثٍ")},
                 "why": "After {أَرْبَعِينَ}: a singular in naṣb, {حَدِيثًا}."},
                {"s": "اِشْتَرَيْتُ عَشَرَةَ ___", "gloss": "I bought ten pens.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("قَلَمًا", "أَقْلَامًا", "أَقْلَامٍ")},
                 "why": "10 owns a plural in jarr: {عَشَرَةَ أَقْلَامٍ}. The naṣb specifier starts at 11."},
            ],
        },
        {
            "title": "Specifier, object or owner?",
            "fields": [
                {"key": "job", "label": "Job of the word in [ ]", "options": [OBJ, TAMY, OWNER]},
                {"key": "case", "label": "Case", "options": [NASB, JARR]},
            ],
            "rows": [
                {"s": "عِنْدِي رِطْلٌ [عَسَلًا].", "ans": {"job": "tamy", "case": "nasb"}, "why": "A pound of what? Honey. The specifier is in naṣb even when the measure is in rafʿ."},
                {"s": "اِشْتَرَيْتُ [ذِرَاعًا] حَرِيرًا.", "ans": {"job": "obj", "case": "nasb"}, "why": "What did I buy? An arm's length. The object."},
                {"s": "اِشْتَرَيْتُ ذِرَاعًا [حَرِيرًا].", "ans": {"job": "tamy", "case": "nasb"}, "why": "An arm's length of what? Silk. Specifier."},
                {"s": "شَرِبْتُ كُوبَ [حَلِيبٍ].", "ans": {"job": "owner", "case": "jarr"}, "why": "{كُوبَ} has no tanween: it owns {حَلِيبٍ}. Owner, jarr."},
                {"s": "اِمْتَلَأَ الحَوْضُ [مَاءً].", "ans": {"job": "tamy", "case": "nasb"}, "why": "Filled with what? Water. Specifier of the sentence."},
                {"s": "اِشْتَرَيْتُ ثَلَاثِينَ [كِتَابًا].", "ans": {"job": "tamy", "case": "nasb"}, "why": "Thirty of what? Books. After 11 to 99: specifier, singular, naṣb."},
            ],
        },
        {
            "title": "Find the specifier",
            "fields": [{"key": "pick", "label": "Specifier", "options": []}],
            "rows": [
                {"s": "اِشْتَرَى الرَّجُلُ صَاعًا قَمْحًا.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الرَّجُلُ", "صَاعًا", "قَمْحًا")},
                 "why": "{صَاعًا} is the object. A ṣāʿ of what? {قَمْحًا}."},
                {"s": "رَجَعَ الطُّلَّابُ مُسْرِعِينَ بَعْدَ أَحَدَ عَشَرَ يَوْمًا.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَوْمًا", "مُسْرِعِينَ", "أَحَدَ")},
                 "why": "Eleven of what? Days: {يَوْمًا}. {مُسْرِعِينَ} says how the students came back: a state."},
                {"s": "زَيْدٌ أَكْرَمُ مِنْكَ أَبًا.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("زَيْدٌ", "أَبًا", "أَكْرَمُ")},
                 "why": "More noble in what respect? In his father: {أَبًا}. It is not owned, so it has fatha with tanween."},
                {"s": "اِمْتَلَأَ الفَصْلُ طُلَّابًا.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الفَصْلُ", "طُلَّابًا", "اِمْتَلَأَ")},
                 "why": "Filled with what? Students. A broken plural specifier, naṣb with fatha."},
                {"s": "حَسُنَتِ البِنْتُ خُلُقًا وَجَلَسَتْ صَامِتَةً.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("خُلُقًا", "صَامِتَةً", "البِنْتُ")},
                 "why": "Good in what respect? In character: {خُلُقًا}. {صَامِتَةً} answers \"how?\": a state."},
                {"s": "سَافَرْتُ خَمْسَةَ عَشَرَ يَوْمًا فَرِحًا.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("فَرِحًا", "خَمْسَةَ", "يَوْمًا")},
                 "why": "Fifteen of what? Days: {يَوْمًا}. {فَرِحًا} answers \"how?\": a state."},
            ],
        },
    ],
}
