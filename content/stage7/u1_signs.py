# Stage 7, Unit 1: The signs of naṣb (عَلَامَاتُ النَّصْبِ)

# Canonical options (STAGES_5_8_SPEC.md), copied exactly.
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
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ", "color": "green"}

SING = {"k": "sing", "label": "Singular · مُفْرَدٌ", "color": "grey"}
DUAL = {"k": "dual", "label": "Dual · مُثَنًّى", "color": "teal"}
SMP = {"k": "smp", "label": "Sound m. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ", "color": "blue"}
SFP = {"k": "sfp", "label": "Sound f. plural · جَمْعُ مُؤَنَّثٍ سَالِمٌ", "color": "pink"}
BRK = {"k": "brk", "label": "Broken plural · جَمْعُ تَكْسِيرٍ", "color": "purple"}
DIP = {"k": "dip", "label": "Diptote · مَمْنُوعٌ مِنَ الصَّرْفِ", "color": "orange"}
FIVE = {"k": "five", "label": "Five nouns · الأَسْمَاءُ الخَمْسَةُ", "color": "gold"}
HIDV = {"k": "hidv", "label": "Hidden vowel", "color": "brown"}

NASB_SIGNS = [FAT, ALIF, YA, KAS, HID]
KINDS = [SING, DUAL, SMP, SFP, BRK, DIP, FIVE, HIDV]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s7-signs",
    "order": 1,
    "title": "The signs of naṣb",
    "ar": "عَلَامَاتُ النَّصْبِ",
    "blurb": "Many jobs put a noun in naṣb. Five signs show it: fatha, alif, yāʾ, kasra and the hidden fatha.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 7 · UNIT 1", "title": "Five signs of naṣb",
         "text": "In Stage 2 every noun in naṣb ended in fatha. Now we meet all the noun groups. The job gives naṣb. The kind of noun gives the sign.",
         "wm": "النَّصْبُ"},

        {"t": "h2", "text": "The jobs that take naṣb"},
        {"t": "p", "text": "Stage 5 had the jobs of rafʿ. Stage 6 had the jobs of jarr. Stage 7 has the jobs of naṣb. They are called {المَنْصُوبَاتُ}. This is the map for the whole stage."},
        {"t": "table", "head": ["Job", "Arabic", "Example", "Unit"], "rows": [
            ["Object", "{مَفْعُولٌ بِهِ}", "{قَرَأْتُ الكِتَابَ.}", "2"],
            ["Verb's own noun", "{مَفْعُولٌ مُطْلَقٌ}", "{جَلَسْتُ جُلُوسًا.}", "3"],
            ["Purpose", "{مَفْعُولٌ لِأَجْلِهِ}", "{قُمْتُ احْتِرَامًا لِلْمُعَلِّمِ.}", "4"],
            ["Time/place", "{مَفْعُولٌ فِيهِ}", "{جَلَسْتُ أَمَامَ البَيْتِ.}", "4"],
            ["Together with", "{مَفْعُولٌ مَعَهُ}", "{سِرْتُ وَالنِّيلَ.}", "5"],
            ["State", "{حَالٌ}", "{جَاءَ الطَّالِبُ مُسْرِعًا.}", "5"],
            ["Specifier", "{تَمْيِيزٌ}", "{اِشْتَرَيْتُ رِطْلًا زَيْتًا.}", "6"],
            ["Exception", "{مُسْتَثْنًى}", "{جَاءَ الطُّلَّابُ إِلَّا زَيْدًا.}", "7"],
            ["Called", "{مُنَادًى}", "{يَا عَبْدَ اللّٰهِ}", "8"],
            ["Inna's noun", "{اِسْمُ إِنَّ}", "{إِنَّ المُسْلِمِينَ صَادِقُونَ.}", "9"],
            ["Kāna's information", "{خَبَرُ كَانَ}", "{كَانَ الجَوُّ بَارِدًا.}", "9"],
        ]},
        {"t": "tip", "text": "You do not need to learn all eleven jobs today. This unit is about the signs. Each job gets its own unit."},

        {"t": "h2", "text": "One original sign, four others"},
        {"t": "p", "text": "The original sign of naṣb is fatha. Four groups use a branch sign instead: alif, yāʾ or kasra. Some nouns keep the fatha, but we cannot see it."},
        {"t": "cols", "items": [
            {"color": "pink", "title": "Fatha", "ar": "فَتْحَةٌ", "text": "The original sign: {الكِتَابَ}، {زَيْنَبَ}، {القَاضِيَ}"},
            {"color": "teal", "title": "Alif", "ar": "الأَلِفُ", "text": "The five nouns: {أَبَاكَ}"},
            {"color": "purple", "title": "Yāʾ", "ar": "اليَاءُ", "text": "Dual and sound m. plural: {الطَّالِبَيْنِ}، {المُعَلِّمِينَ}"},
            {"color": "green", "title": "Kasra", "ar": "كَسْرَةٌ", "text": "Sound f. plural: {المُعَلِّمَاتِ}"},
            {"color": "brown", "title": "Hidden fatha", "ar": "مُقَدَّرَةٌ", "text": "Maqṣūr and noun + ـي: {الفَتَى}، {كِتَابِي}"},
        ]},
        {"t": "rule", "color": "pink", "title": "Job, case, sign",
         "text": "Find the job. The job gives the case. The kind of noun gives the sign. An object is always naṣb, but {المُعَلِّمِينَ} shows it with yāʾ and {أَبَاكَ} with alif."},

        {"t": "h2", "text": "Every group in naṣb"},
        {"t": "p", "text": "Here is the object of {رَأَيْتُ} \"I saw\" with every group. The job is the same in every row. Only the sign changes."},
        {"t": "table", "head": ["Group", "In naṣb", "Sign"], "rows": [
            ["Singular", "رَأَيْتُ الطَّالِبَ، طَالِبًا", "Fatha"],
            ["Broken plural", "رَأَيْتُ الرِّجَالَ، رِجَالًا", "Fatha"],
            ["Diptote", "رَأَيْتُ زَيْنَبَ، مَسَاجِدَ", "Fatha, no tanween"],
            ["Manqūṣ", "رَأَيْتُ القَاضِيَ، قَاضِيًا", "Fatha, it shows on the ي"],
            ["Dual", "رَأَيْتُ الطَّالِبَيْنِ", "Yāʾ: ـَيْنِ"],
            ["Sound m. plural", "رَأَيْتُ المُعَلِّمِينَ", "Yāʾ: ـِينَ"],
            ["Sound f. plural", "رَأَيْتُ الطَّالِبَاتِ، طَالِبَاتٍ", "Kasra in place of fatha"],
            ["Five nouns", "رَأَيْتُ أَبَاكَ، أَخَا زَيْدٍ", "Alif"],
            ["Maqṣūr", "رَأَيْتُ الفَتَى، مُوسَى", "Hidden fatha"],
            ["Noun + ـي \"my\"", "رَأَيْتُ أَبِي، قَرَأْتُ كِتَابِي", "Hidden fatha"],
        ]},
        {"t": "tip", "text": "The manqūṣ is the odd one. In rafʿ and jarr its vowel is hidden. In naṣb the fatha is light, so you see it: {رَأَيْتُ القَاضِيَ}. Writing {رَأَيْتُ القَاضِي} with no fatha is a mistake."},
        {"t": "tip", "text": "{أَبِي} \"my father\" is not in the five-noun pattern. With ـي \"my\" the vowel is hidden in every case: {رَأَيْتُ أَبِي}."},

        {"t": "h2", "text": "Three shapes side by side"},
        {"t": "p", "text": "Put rafʿ, naṣb and jarr next to each other. For the dual, the two sound plurals and the diptote, naṣb has the same shape as jarr. So the shape alone does not tell you the case. The job tells you."},
        {"t": "table", "head": ["Group", "Rafʿ", "Naṣb", "Jarr"], "rows": [
            ["Singular", "الكِتَابُ", "الكِتَابَ", "الكِتَابِ"],
            ["Broken plural", "الكُتُبُ", "الكُتُبَ", "الكُتُبِ"],
            ["Diptote", "مَسَاجِدُ", "مَسَاجِدَ", "مَسَاجِدَ"],
            ["Dual", "الكِتَابَانِ", "الكِتَابَيْنِ", "الكِتَابَيْنِ"],
            ["Sound m. plural", "المُسْلِمُونَ", "المُسْلِمِينَ", "المُسْلِمِينَ"],
            ["Sound f. plural", "المُسْلِمَاتُ", "المُسْلِمَاتِ", "المُسْلِمَاتِ"],
            ["Five nouns", "أَبُوكَ", "أَبَاكَ", "أَبِيكَ"],
            ["Maqṣūr", "الفَتَى", "الفَتَى", "الفَتَى"],
            ["Manqūṣ", "القَاضِي", "القَاضِيَ", "القَاضِي"],
        ]},
        {"t": "examples", "items": [
            {"ar": "رَأَيْتُ المُسْلِمِينَ.", "en": "I saw the Muslims.", "note": "Object, so naṣb. The sign is yāʾ."},
            {"ar": "سَلَّمْتُ عَلَى المُسْلِمِينَ.", "en": "I greeted the Muslims.", "note": "After {عَلَى}, so jarr. Same shape, sign yāʾ."},
        ]},
        {"t": "tip", "text": "Do not mix up {ـَيْنِ} and {ـِينَ}. Fatha before the ي is the dual: {المُعَلِّمَيْنِ} \"the two teachers\". Kasra before the ي is the plural: {المُعَلِّمِينَ} \"the teachers\"."},

        {"t": "h2", "text": "Say the full iʿrāb"},
        {"t": "p", "text": "Every answer has three parts: the job, the case and the sign. Add the reason when the sign is not fatha."},
        {"t": "examples", "items": [
            {"ar": "رَأَيْتُ المُعَلِّمِينَ.", "en": "I saw the teachers.",
             "note": "{المُعَلِّمِينَ}: {مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}. Object, naṣb, sign yāʾ, because it is a sound m. plural."},
            {"ar": "شَكَرْتُ المُعَلِّمَاتِ.", "en": "I thanked the female teachers.",
             "note": "{المُعَلِّمَاتِ}: {مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الكَسْرَةُ نِيَابَةً عَنِ الفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ}. Kasra in place of fatha."},
            {"ar": "زُرْتُ أَبَاكَ.", "en": "I visited your father.",
             "note": "{أَبَا}: {مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الأَلِفُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ}. The {ـكَ} is the owner."},
            {"ar": "رَأَيْتُ الفَتَى.", "en": "I saw the young man.",
             "note": "{الفَتَى}: {مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ عَلَى الأَلِفِ}. The alif cannot carry a vowel."},
            {"ar": "رَأَيْتُ القَاضِيَ.", "en": "I saw the judge.",
             "note": "{القَاضِيَ}: {مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ}. The fatha shows."},
        ]},

        {"t": "h2", "text": "Two traps"},
        {"t": "p", "text": "Some broken plurals end in {ات}, but the {ت} is part of the word. They take fatha: {سَمِعْتُ أَصْوَاتًا} \"I heard voices\", {حَفِظْتُ أَبْيَاتًا} \"I learned lines of poetry\"."},
        {"t": "p", "text": "The sound f. plural never takes fatha. With no {ال} it takes kasra with tanween: {رَأَيْتُ طَالِبَاتٍ}. {طَالِبَاتًا} is a mistake."},

        {"t": "summary", "title": "In short", "items": [
            "Many jobs give naṣb: object, verb's own noun, purpose, time/place, together with, state, specifier, exception, called, inna's noun, kāna's information.",
            "Fatha: singular, broken plural, diptote, and the manqūṣ ({القَاضِيَ}).",
            "Yāʾ: dual ({ـَيْنِ}) and sound m. plural ({ـِينَ}).",
            "Kasra in place of fatha: sound f. plural ({المُعَلِّمَاتِ}، {طَالِبَاتٍ}).",
            "Alif: the five nouns ({أَبَاكَ}). Hidden fatha: maqṣūr ({الفَتَى}) and noun + ـي ({كِتَابِي}).",
            "Many groups look the same in naṣb and jarr. The job decides the case.",
        ]},
    ],

    "practice": [
        {
            "title": "Which sign of naṣb?",
            "fields": [{"key": "sign", "label": "Sign", "options": NASB_SIGNS}],
            "rows": [
                {"s": "رَأَيْتُ [المُهَنْدِسِينَ]", "gloss": "I saw the engineers.", "ans": {"sign": "ya"},
                 "why": "Object, naṣb. A sound m. plural: the sign is yāʾ, {ـِينَ}."},
                {"s": "شَكَرْتُ [المُدَرِّسَاتِ]", "gloss": "I thanked the female teachers.", "ans": {"sign": "kas"},
                 "why": "Object, naṣb. A sound f. plural: kasra in place of fatha."},
                {"s": "قَرَأْتُ [الكِتَابَ]", "gloss": "I read the book.", "ans": {"sign": "fat"},
                 "why": "Object, naṣb. A singular: the original sign, fatha."},
                {"s": "رَأَيْتُ [أَخَاكَ]", "gloss": "I saw your brother.", "ans": {"sign": "alif"},
                 "why": "Object, naṣb. {أَخٌ} is one of the five nouns: the sign is alif."},
                {"s": "رَأَيْتُ [مُوسَى]", "gloss": "I saw Musa.", "ans": {"sign": "hid"},
                 "why": "Object, naṣb. A maqṣūr: hidden fatha on the alif."},
                {"s": "فَتَحْتُ [البَابَيْنِ]", "gloss": "I opened the two doors.", "ans": {"sign": "ya"},
                 "why": "Object, naṣb. A dual: the sign is yāʾ, {ـَيْنِ}."},
            ],
        },
        {
            "title": "Which group, which sign?",
            "fields": [
                {"key": "kind", "label": "Group", "options": KINDS},
                {"key": "sign", "label": "Sign", "options": NASB_SIGNS},
            ],
            "rows": [
                {"s": "رَأَيْتُ [الرِّجَالَ]", "gloss": "I saw the men.", "ans": {"kind": "brk", "sign": "fat"},
                 "why": "{رِجَالٌ} is the broken plural of {رَجُلٌ}. Broken plurals take fatha."},
                {"s": "زُرْتُ [أَحْمَدَ]", "gloss": "I visited Ahmad.", "ans": {"kind": "dip", "sign": "fat"},
                 "why": "{أَحْمَدُ} is a diptote. Fatha, with no tanween."},
                {"s": "سَمِعْتُ [الطَّالِبَاتِ]", "gloss": "I heard the female students.", "ans": {"kind": "sfp", "sign": "kas"},
                 "why": "A sound f. plural. In naṣb it takes kasra in place of fatha."},
                {"s": "زُرْتُ [أَبَاكَ]", "gloss": "I visited your father.", "ans": {"kind": "five", "sign": "alif"},
                 "why": "{أَبٌ} with an owner is one of the five nouns. Sign alif."},
                {"s": "كَتَبْتُ [رِسَالَتَيْنِ]", "gloss": "I wrote two letters.", "ans": {"kind": "dual", "sign": "ya"},
                 "why": "{رِسَالَةٌ} + {ـَيْنِ}: a dual. Sign yāʾ."},
                {"s": "رَأَيْتُ [القَاضِيَ]", "gloss": "I saw the judge.", "ans": {"kind": "hidv", "sign": "fat"},
                 "why": "{القَاضِي} is a manqūṣ, in the hidden-vowel group. But in naṣb the fatha shows: {القَاضِيَ}."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "رَأَيْتُ ___", "gloss": "the Muslims (three or more men)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُسْلِمُونَ", "المُسْلِمِينَ", "المُسْلِمَيْنِ")},
                 "why": "Object, naṣb: {ـِينَ}. {المُسْلِمُونَ} is rafʿ. {المُسْلِمَيْنِ} means two."},
                {"s": "شَكَرْتُ ___", "gloss": "the female teachers", "ans": {"pick": "c"},
                 "opts": {"pick": pick("المُعَلِّمَاتُ", "المُعَلِّمَاتَ", "المُعَلِّمَاتِ")},
                 "why": "A sound f. plural in naṣb takes kasra: {المُعَلِّمَاتِ}. Never fatha."},
                {"s": "زُرْتُ ___", "gloss": "your brother", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَخُوكَ", "أَخَاكَ", "أَخِيكَ")},
                 "why": "Object, naṣb. Five nouns take alif in naṣb: {أَخَاكَ}."},
                {"s": "رَأَيْتُ ___", "gloss": "two boys", "ans": {"pick": "a"},
                 "opts": {"pick": pick("وَلَدَيْنِ", "وَلَدَانِ", "وَلَدِينَ")},
                 "why": "A dual in naṣb: fatha, then {يْنِ}. {وَلَدَانِ} is rafʿ."},
                {"s": "رَأَيْتُ ___", "gloss": "a judge", "ans": {"pick": "c"},
                 "opts": {"pick": pick("قَاضٍ", "قَاضِي", "قَاضِيًا")},
                 "why": "A manqūṣ in naṣb shows its fatha. With no {ال}: {قَاضِيًا}. {قَاضٍ} is rafʿ or jarr."},
                {"s": "سَمِعْتُ ___", "gloss": "female students (no the)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("طَالِبَاتًا", "طَالِبَاتٍ", "طَالِبَاتٌ")},
                 "why": "Sound f. plural, naṣb: kasra with tanween, {طَالِبَاتٍ}. {طَالِبَاتًا} is a common mistake."},
            ],
        },
        {
            "title": "Same shape: which case?",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, WAW, YA]},
            ],
            "rows": [
                {"s": "جَاءَ [المُسْلِمُونَ]", "gloss": "The Muslims came.", "ans": {"case": "raf", "sign": "waw"},
                 "why": "Doer, rafʿ. A sound m. plural: sign wāw."},
                {"s": "رَأَيْتُ [المُسْلِمِينَ]", "gloss": "I saw the Muslims.", "ans": {"case": "nasb", "sign": "ya"},
                 "why": "Object, naṣb. Sign yāʾ."},
                {"s": "سَلَّمْتُ عَلَى [المُسْلِمِينَ]", "gloss": "I greeted the Muslims.", "ans": {"case": "jarr", "sign": "ya"},
                 "why": "After {عَلَى}, jarr. Same shape as naṣb. Sign yāʾ."},
                {"s": "رَأَيْتُ [المُسْلِمَاتِ]", "gloss": "I saw the Muslim women.", "ans": {"case": "nasb", "sign": "kas"},
                 "why": "Object, naṣb. Sound f. plural: kasra in place of fatha."},
                {"s": "نَظَرْتُ إِلَى [المُسْلِمَاتِ]", "gloss": "I looked at the Muslim women.", "ans": {"case": "jarr", "sign": "kas"},
                 "why": "After {إِلَى}, jarr. The sign is kasra, the original sign of jarr."},
            ],
        },
        {
            "title": "Review: case and sign in a sentence",
            "prompt": "زَارَ أَخُوكَ المُعَلِّمِينَ فِي البَيْتِ.",
            "en": "Your brother visited the teachers at home.",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR]},
                {"key": "sign", "label": "Sign", "options": [DAM, KAS, WAW, YA, ALIF, FIXED]},
            ],
            "rows": [
                {"s": "أَخُو", "gloss": "brother, in أَخُوكَ", "ans": {"case": "raf", "sign": "waw"},
                 "why": "Doer, rafʿ. A five noun: sign wāw."},
                {"s": "ـكَ", "gloss": "your", "ans": {"case": "jarr", "sign": "fixed"},
                 "why": "Owner. A pronoun is fixed, so it is in the place of jarr."},
                {"s": "المُعَلِّمِينَ", "gloss": "the teachers", "ans": {"case": "nasb", "sign": "ya"},
                 "why": "Object, naṣb. Sound m. plural: sign yāʾ."},
                {"s": "البَيْتِ", "gloss": "the house", "ans": {"case": "jarr", "sign": "kas"},
                 "why": "After {فِي}, jarr. Sign kasra."},
            ],
        },
        {
            "title": "Every naṣb job uses the same signs",
            "fields": [{"key": "sign", "label": "Sign", "options": NASB_SIGNS}],
            "rows": [
                {"s": "جَاءَ الطُّلَّابُ [مُسْرِعِينَ]", "gloss": "The students came hurrying.", "ans": {"sign": "ya"},
                 "why": "State, naṣb. A sound m. plural: yāʾ."},
                {"s": "سَافَرْتُ [يَوْمَيْنِ]", "gloss": "I travelled for two days.", "ans": {"sign": "ya"},
                 "why": "Time, naṣb. A dual: yāʾ."},
                {"s": "رَجَعَتِ البَنَاتُ [فَرِحَاتٍ]", "gloss": "The girls came back happy.", "ans": {"sign": "kas"},
                 "why": "State, naṣb. A sound f. plural: kasra in place of fatha."},
                {"s": "جَلَسْتُ [أَمَامَ] البَيْتِ", "gloss": "I sat in front of the house.", "ans": {"sign": "fat"},
                 "why": "Place, naṣb. A singular: fatha."},
                {"s": "كَانَ الجَوُّ [بَارِدًا]", "gloss": "The weather was cold.", "ans": {"sign": "fat"},
                 "why": "Kāna's information, naṣb. A singular: fatha."},
                {"s": "إِنَّ [المُسْلِمِينَ] صَادِقُونَ", "gloss": "The Muslims are truthful.", "ans": {"sign": "ya"},
                 "why": "Inna's noun, naṣb. A sound m. plural: yāʾ."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Which sign of naṣb?",
            "fields": [{"key": "sign", "label": "Sign", "options": NASB_SIGNS}],
            "rows": [
                {"s": "قَابَلْتُ [المُهَنْدِسَيْنِ]", "gloss": "I met the two engineers.", "ans": {"sign": "ya"},
                 "why": "Fatha before the ي: a dual. Object, naṣb, sign yāʾ."},
                {"s": "رَأَيْتُ رَجُلًا [ذَا] عِلْمٍ", "gloss": "I saw a man of knowledge.", "ans": {"sign": "alif"},
                 "why": "{ذُو} \"owner of\" is a five noun. It follows {رَجُلًا} in naṣb, so it takes alif: {ذَا}."},
                {"s": "زُرْتُ [المُسْتَشْفَى]", "gloss": "I visited the hospital.", "ans": {"sign": "hid"},
                 "why": "Object, naṣb. A maqṣūr: hidden fatha on the alif."},
                {"s": "رَأَيْتُ [المُحَامِيَ]", "gloss": "I saw the lawyer.", "ans": {"sign": "fat"},
                 "why": "A manqūṣ. In naṣb the fatha shows on the ي."},
                {"s": "فَتَحْتُ [النَّوَافِذَ]", "gloss": "I opened the windows.", "ans": {"sign": "fat"},
                 "why": "Object, naṣb. A broken plural takes fatha."},
                {"s": "قَرَأْتُ [كِتَابِي]", "gloss": "I read my book.", "ans": {"sign": "hid"},
                 "why": "Noun + ـي \"my\": the fatha is hidden before the ي."},
            ],
        },
        {
            "title": "Which group, which sign?",
            "fields": [
                {"key": "kind", "label": "Group", "options": KINDS},
                {"key": "sign", "label": "Sign", "options": NASB_SIGNS},
            ],
            "rows": [
                {"s": "زُرْتُ [فَاطِمَةَ]", "gloss": "I visited Fatima.", "ans": {"kind": "dip", "sign": "fat"},
                 "why": "A feminine name: a diptote. Fatha, no tanween."},
                {"s": "سَمِعْتُ [أَصْوَاتًا]", "gloss": "I heard voices.", "ans": {"kind": "brk", "sign": "fat"},
                 "why": "{أَصْوَاتٌ} is the broken plural of {صَوْتٌ}. The {ت} is part of the root, so it takes fatha."},
                {"s": "شَكَرْتُ [المُمَرِّضَاتِ]", "gloss": "I thanked the nurses.", "ans": {"kind": "sfp", "sign": "kas"},
                 "why": "{مُمَرِّضَةٌ} → {مُمَرِّضَاتٌ}: a sound f. plural. Kasra in place of fatha."},
                {"s": "رَأَيْتُ [الفَتَى]", "gloss": "I saw the young man.", "ans": {"kind": "hidv", "sign": "hid"},
                 "why": "A maqṣūr. The fatha is hidden on the alif."},
                {"s": "سَأَلْتُ [أَخَا] زَيْدٍ", "gloss": "I asked Zayd's brother.", "ans": {"kind": "five", "sign": "alif"},
                 "why": "{أَخٌ} with an owner: a five noun. Sign alif."},
                {"s": "سَمِعْتُ [المُؤَذِّنَيْنِ]", "gloss": "I heard the two callers to prayer.", "ans": {"kind": "dual", "sign": "ya"},
                 "why": "Fatha before {يْنِ}: a dual. Sign yāʾ."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "رَأَيْتُ ___ المَدْرَسَةِ", "gloss": "the teachers (m.) of the school", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُعَلِّمُو", "مُعَلِّمِينَ", "مُعَلِّمِي")},
                 "why": "Naṣb with yāʾ. The {ن} drops before the owner: {مُعَلِّمِي المَدْرَسَةِ}."},
                {"s": "زُرْتُ ___", "gloss": "your father", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَبَاكَ", "أَبُوكَ", "أَبِيكَ")},
                 "why": "Object, naṣb. Five noun: alif, {أَبَاكَ}."},
                {"s": "رَأَيْتُ ___", "gloss": "two cars", "ans": {"pick": "b"},
                 "opts": {"pick": pick("سَيَّارَتَانِ", "سَيَّارَتَيْنِ", "سَيَّارَاتٍ")},
                 "why": "Two, in naṣb: {سَيَّارَتَيْنِ}. {سَيَّارَاتٍ} means three or more."},
                {"s": "رَأَيْتُ ___", "gloss": "a lawyer", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُحَامٍ", "مُحَامِيًا", "مُحَامِي")},
                 "why": "A manqūṣ shows its fatha in naṣb: {مُحَامِيًا}."},
                {"s": "زُرْتُ ___", "gloss": "Zaynab", "ans": {"pick": "c"},
                 "opts": {"pick": pick("زَيْنَبًا", "زَيْنَبِ", "زَيْنَبَ")},
                 "why": "A diptote takes fatha with no tanween: {زَيْنَبَ}."},
                {"s": "شَكَرْتُ ___", "gloss": "the female engineers", "ans": {"pick": "a"},
                 "opts": {"pick": pick("المُهَنْدِسَاتِ", "المُهَنْدِسَاتَ", "المُهَنْدِسَاتُ")},
                 "why": "Sound f. plural in naṣb: kasra, {المُهَنْدِسَاتِ}."},
            ],
        },
        {
            "title": "Same shape: which case?",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR]},
                {"key": "sign", "label": "Sign", "options": [ALIF, YA, HID, WAW, KAS]},
            ],
            "rows": [
                {"s": "رَأَيْتُ [الطَّالِبَيْنِ]", "gloss": "I saw the two students.", "ans": {"case": "nasb", "sign": "ya"},
                 "why": "Object, naṣb. Dual: yāʾ."},
                {"s": "جَلَسْتُ مَعَ [الطَّالِبَيْنِ]", "gloss": "I sat with the two students.", "ans": {"case": "jarr", "sign": "ya"},
                 "why": "Owner after {مَعَ}, jarr. Dual: yāʾ. Same shape as naṣb."},
                {"s": "نَجَحَ [الطَّالِبَانِ]", "gloss": "The two students passed.", "ans": {"case": "raf", "sign": "alif"},
                 "why": "Doer, rafʿ. Dual: alif."},
                {"s": "رَأَيْتُ [الفَتَى]", "gloss": "I saw the young man.", "ans": {"case": "nasb", "sign": "hid"},
                 "why": "Object, naṣb. Maqṣūr: hidden fatha."},
                {"s": "ذَهَبْتُ مَعَ [الفَتَى]", "gloss": "I went with the young man.", "ans": {"case": "jarr", "sign": "hid"},
                 "why": "Owner after {مَعَ}, jarr. Maqṣūr: hidden kasra. The case comes from the job."},
                {"s": "قَرَأْتُ كِتَابَ [أَبِيكَ]", "gloss": "I read your father's book.", "ans": {"case": "jarr", "sign": "ya"},
                 "why": "Owner, jarr. A five noun: yāʾ."},
            ],
        },
        {
            "title": "Review: case and sign in a sentence",
            "prompt": "سَأَلَ المُهَنْدِسُ القَاضِيَ عَنْ أَبِيكَ.",
            "en": "The engineer asked the judge about your father.",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, YA, HID, FIXED]},
            ],
            "rows": [
                {"s": "المُهَنْدِسُ", "gloss": "the engineer", "ans": {"case": "raf", "sign": "dam"},
                 "why": "Doer, rafʿ. Singular: damma."},
                {"s": "القَاضِيَ", "gloss": "the judge", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "Object, naṣb. A manqūṣ shows its fatha. It is not hidden."},
                {"s": "أَبِي", "gloss": "father, in أَبِيكَ", "ans": {"case": "jarr", "sign": "ya"},
                 "why": "After {عَنْ}, jarr. A five noun: yāʾ."},
                {"s": "ـكَ", "gloss": "your", "ans": {"case": "jarr", "sign": "fixed"},
                 "why": "Owner, a fixed pronoun in the place of jarr."},
            ],
        },
        {
            "title": "Every naṣb job uses the same signs",
            "fields": [{"key": "sign", "label": "Sign", "options": NASB_SIGNS}],
            "rows": [
                {"s": "جَاءَ الطَّالِبَانِ [ضَاحِكَيْنِ]", "gloss": "The two students came laughing.", "ans": {"sign": "ya"},
                 "why": "State, naṣb. A dual: yāʾ."},
                {"s": "أَصْبَحَ الطُّلَّابُ [مُجْتَهِدِينَ]", "gloss": "The students became hard-working.", "ans": {"sign": "ya"},
                 "why": "Kāna's information ({أَصْبَحَ} is a sister of {كَانَ}), naṣb. Sound m. plural: yāʾ."},
                {"s": "كَانَتِ الطَّالِبَاتُ [مُجْتَهِدَاتٍ]", "gloss": "The female students were hard-working.", "ans": {"sign": "kas"},
                 "why": "Kāna's information, naṣb. Sound f. plural: kasra in place of fatha."},
                {"s": "لَيْتَ [أَبَاكَ] حَاضِرٌ", "gloss": "If only your father were here.", "ans": {"sign": "alif"},
                 "why": "Noun of {لَيْتَ}, a sister of {إِنَّ}: naṣb. Five noun: alif."},
                {"s": "جَلَسْتُ [خَلْفَ] الإِمَامِ", "gloss": "I sat behind the imam.", "ans": {"sign": "fat"},
                 "why": "Place, naṣb. Fatha."},
                {"s": "قُمْتُ [احْتِرَامًا] لِلْمُعَلِّمِ", "gloss": "I stood up out of respect for the teacher.", "ans": {"sign": "fat"},
                 "why": "Purpose, naṣb. Singular: fatha."},
            ],
        },
    ],
}
