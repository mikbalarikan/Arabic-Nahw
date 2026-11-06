# Stage 4, Unit 7: The five nouns (الْأَسْمَاءُ الْخَمْسَةُ)

FIVE = {"k": "five", "label": "Five noun: letter signs", "color": "gold"}
NORM = {"k": "norm", "label": "Normal vowel signs", "color": "green"}
HID = {"k": "hid", "label": "Hidden vowel (ـي \"my\")", "color": "brown"}
USE = [FIVE, NORM, HID]

L_WAW = {"k": "waw", "label": "و", "color": "red"}
L_ALIF = {"k": "alif", "label": "ا", "color": "red"}
L_YA = {"k": "ya", "label": "ي", "color": "red"}
L_NONE = {"k": "none", "label": "No letter sign", "color": "green"}
LETTERS = [L_WAW, L_ALIF, L_YA, L_NONE]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s4-five-nouns",
    "order": 7,
    "title": "The five nouns",
    "ar": "الْأَسْمَاءُ الْخَمْسَةُ",
    "blurb": "Father, brother, father-in-law, mouth and owner: nouns that show iʿrāb with a letter.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 4 · UNIT 7", "title": "Five nouns that use letters",
         "text": "Five short nouns can show their iʿrāb with a long letter, {و}، {ا} or {ي}, in place of a vowel.",
         "wm": "أَبُوكَ"},

        {"t": "h2", "text": "The five nouns"},
        {"t": "table", "head": ["Noun", "Meaning", "With an owner"], "rows": [
            ["أَبٌ", "father", "{أَبُوكَ} your father"],
            ["أَخٌ", "brother", "{أَخُوكَ} your brother"],
            ["حَمٌ", "father-in-law (husband's father)", "{حَمُوهَا} her father-in-law"],
            ["فُو", "mouth", "{فُوكَ} your mouth"],
            ["ذُو", "owner of, having", "{ذُو مَالٍ} having money"],
        ]},
        {"t": "words", "items": [
            {"ar": "أَبُوكَ", "sub": "your father", "color": "gold"},
            {"ar": "أَخُو زَيْدٍ", "sub": "Zayd's brother", "color": "gold"},
            {"ar": "ذُو عِلْمٍ", "sub": "having knowledge", "color": "gold"},
        ]},
        {"t": "tip", "text": "Some books count six and add {هَنٌ} \"a thing\". It is rare. We leave it out."},

        {"t": "h2", "text": "When they use letters"},
        {"t": "rule", "color": "gold", "title": "They need an owner",
         "text": "A five noun uses letter signs when it has an owner: a noun ({أَخُو زَيْدٍ}) or a pronoun other than {ـي} ({أَبُوكَ}، {أَخُوهُ})."},
        {"t": "examples", "items": [
            {"ar": "أَبُوكَ طَبِيبٌ.", "en": "Your father is a doctor.", "note": "Topic in rafʿ. The sign is {و}."},
            {"ar": "أَخُو زَيْدٍ طَالِبٌ.", "en": "Zayd's brother is a student.", "note": "The owner {زَيْدٍ} is in jarr, as normal."},
            {"ar": "الطَّبِيبُ ذُو عِلْمٍ.", "en": "The doctor has knowledge.", "note": "{ذُو عِلْمٍ} is the Information."},
        ]},
        {"t": "p", "text": "Here is the preview table. Each case has its own letter. You will practise them in Stages 5 to 7."},
        {"t": "table", "head": ["Case", "Sign", "أَبٌ", "أَخٌ", "ذُو"], "rows": [
            ["Rafʿ", "{و}", "أَبُوكَ", "أَخُوكَ", "ذُو مَالٍ"],
            ["Naṣb", "{ا}", "أَبَاكَ", "أَخَاكَ", "ذَا مَالٍ"],
            ["Jarr", "{ي}", "أَبِيكَ", "أَخِيكَ", "ذِي مَالٍ"],
        ]},
        {"t": "tip", "text": "These letters are branch signs. They do the job of damma, fatha and kasra."},

        {"t": "h2", "text": "When they are normal"},
        {"t": "p", "text": "Without an owner, a five noun is a normal noun. With {ـي} \"my\", its vowel is hidden."},
        {"t": "cols", "items": [
            {"color": "green", "title": "Alone", "ar": "أَبٌ", "text": "Normal signs with tanween."},
            {"color": "green", "title": "With ال", "ar": "الْأَبُ", "text": "Normal signs: {الْأَبُ}، {الْأَبَ}، {الْأَبِ}."},
            {"color": "brown", "title": "With ـي", "ar": "أَبِي", "text": "Always {أَبِي}. The vowel is hidden (unit 8)."},
        ]},
        {"t": "examples", "items": [
            {"ar": "الْأَبُ فِي الْبَيْتِ.", "en": "The father is in the house.", "note": "{ال}, so a normal damma."},
            {"ar": "أَبِي مُدَرِّسٌ.", "en": "My father is a teacher.", "note": "The {ي} here means \"my\". It is not a sign of jarr."},
            {"ar": "حَامِدٌ أَخٌ كَرِيمٌ.", "en": "Hamid is a generous brother.", "note": "No owner, so normal tanween."},
        ]},

        {"t": "h2", "text": "فُو and فَمٌ"},
        {"t": "p", "text": "\"Mouth\" has two forms. Only {فُو} (with no {م}) is a five noun, and only with an owner: {فُوكَ}."},
        {"t": "p", "text": "The common form {فَمٌ} has {م}. It always takes normal signs: {فَمٌ}، {الْفَمُ}، {فَمُكَ}."},
        {"t": "examples", "items": [
            {"ar": "فَمُ الْوَلَدِ صَغِيرٌ.", "en": "The boy's mouth is small.", "note": "With {م}: a normal damma."},
        ]},

        {"t": "h2", "text": "ذُو: owner of"},
        {"t": "rule", "color": "gold", "title": "ذُو always has an owner after it",
         "text": "{ذُو} means \"having\" or \"owner of\". It never stands alone. The noun after it is in jarr: {ذُو مَالٍ}، {ذُو عِلْمٍ}."},
        {"t": "examples", "items": [
            {"ar": "هُوَ رَجُلٌ ذُو مَالٍ.", "en": "He is a man with money.", "note": "{ذُو مَالٍ} describes {رَجُلٌ}."},
            {"ar": "الْمُدِيرُ ذُو عِلْمٍ.", "en": "The principal has knowledge.", "note": "Information in rafʿ: {ذُو}."},
        ]},
        {"t": "tip", "text": "Do not mix up {ذُو} with the pointing word {ذَلِكَ}. {ذُو} is a flexible noun."},

        {"t": "summary", "title": "In short", "items": [
            "The five nouns: {أَبٌ}، {أَخٌ}، {حَمٌ}، {فُو}، {ذُو}.",
            "With an owner (not {ـي}) they use letters: {و} rafʿ, {ا} naṣb, {ي} jarr: {أَبُوكَ}، {أَبَاكَ}، {أَبِيكَ}.",
            "Alone or with {ال} they are normal: {أَبٌ}، {الْأَبُ}. With {ـي} the vowel is hidden: {أَبِي}.",
            "{فَمٌ} with {م} is always normal.",
            "{ذُو} means \"having\" and always has a noun after it: {ذُو مَالٍ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Is it used as a five noun here?",
            "fields": [{"key": "use", "label": "Signs", "options": USE}],
            "rows": [
                {"s": "أَبُوكَ", "gloss": "your father", "ans": {"use": "five"}, "why": "It has an owner, {كَ}. The sign is {و}."},
                {"s": "الْأَبُ", "gloss": "the father", "ans": {"use": "norm"}, "why": "With {ال} it takes a normal damma."},
                {"s": "أَبِي", "gloss": "my father", "ans": {"use": "hid"}, "why": "With {ـي} \"my\" the vowel is hidden."},
                {"s": "أَخُو زَيْدٍ", "gloss": "Zayd's brother", "ans": {"use": "five"}, "why": "Its owner is the noun {زَيْدٍ}."},
                {"s": "أَخٌ", "gloss": "a brother", "ans": {"use": "norm"}, "why": "No owner: normal signs with tanween."},
                {"s": "ذُو عِلْمٍ", "gloss": "having knowledge", "ans": {"use": "five"}, "why": "{ذُو} always has an owner. The sign is {و}."},
            ],
        },
        {
            "title": "Which word is one of the five nouns?",
            "fields": [{"key": "pick", "label": "Five noun", "options": []}],
            "rows": [
                {"s": "father / door / son", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَبٌ", "بَابٌ", "ابْنٌ")}, "why": "{أَبٌ}. {ابْنٌ} \"son\" is a normal noun."},
                {"s": "sister / brother / mother", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أُخْتٌ", "أَخٌ", "أُمٌّ")}, "why": "{أَخٌ}. {أُخْتٌ} and {أُمٌّ} take normal signs."},
                {"s": "owner of / that / gold", "ans": {"pick": "a"},
                 "opts": {"pick": pick("ذُو", "ذَلِكَ", "ذَهَبٌ")}, "why": "{ذُو}. {ذَلِكَ} is a fixed pointing word."},
                {"s": "his hand / his mouth / his eye", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَدُهُ", "فُوهُ", "عَيْنُهُ")}, "why": "{فُوهُ} \"his mouth\", with no {م}."},
                {"s": "uncle / father-in-law / maternal uncle", "ans": {"pick": "b"},
                 "opts": {"pick": pick("عَمٌّ", "حَمٌ", "خَالٌ")}, "why": "{حَمٌ}. {عَمٌّ} looks close but is a normal noun."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "أَبُوكَ طَبِيبٌ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("My father is a doctor.", "Your father is a doctor.", "Your brother is a doctor.")},
                 "why": "{أَبُو} + {كَ} \"your\"."},
                {"s": "أَخُو حَامِدٍ فِي الْمَسْجِدِ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("Hamid's brother is in the mosque.", "Hamid's father is in the mosque.", "Hamid is in his brother's mosque.")},
                 "why": "{أَخُو حَامِدٍ} is \"Hamid's brother\"."},
                {"s": "هُوَ رَجُلٌ ذُو مَالٍ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("This is the man's money.", "He is a man without money.", "He is a man with money.")},
                 "why": "{ذُو مَالٍ} means \"having money\"."},
                {"s": "أَبِي مُدَرِّسٌ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("My father is a teacher.", "Your father is a teacher.", "The father is a teacher.")},
                 "why": "{ـي} means \"my\"."},
                {"s": "فَمُ الْوَلَدِ صَغِيرٌ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("The boy's hand is small.", "The boy's mouth is small.", "The boy's father is small.")},
                 "why": "{فَمٌ} is \"mouth\"."},
                {"s": "حَمُوهَا تَاجِرٌ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("Her brother is a merchant.", "His father is a merchant.", "Her father-in-law is a merchant.")},
                 "why": "{حَمُو} + {هَا} \"her\"."},
            ],
        },
        {
            "title": "Which letter sign does it show?",
            "fields": [{"key": "letter", "label": "Letter sign", "options": LETTERS}],
            "rows": [
                {"s": "أَخُوكَ", "ans": {"letter": "waw"}, "why": "{أَخُو} + {كَ}: the sign is {و}."},
                {"s": "أَبَاهُ", "ans": {"letter": "alif"}, "why": "{أَبَا} + {هُ}: the sign is {ا}."},
                {"s": "أَخِيكَ", "ans": {"letter": "ya"}, "why": "{أَخِي} + {كَ}: the sign is {ي}."},
                {"s": "ذُو مَالٍ", "ans": {"letter": "waw"}, "why": "{ذُو}: the sign is {و}."},
                {"s": "ذَا عِلْمٍ", "ans": {"letter": "alif"}, "why": "{ذَا}: the sign is {ا}."},
                {"s": "الْأَبُ", "ans": {"letter": "none"}, "why": "With {ال} it has a normal damma."},
            ],
        },
        {
            "title": "Choose the right form (rafʿ)",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "... طَبِيبٌ", "gloss": "Your father is a doctor.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَبُوكَ", "أَبَاكَ", "أَبِيكَ")}, "why": "The Topic is in rafʿ. A five noun with an owner shows {و}."},
                {"s": "... فِي الْبَيْتِ", "gloss": "Your brother is in the house.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَخُكَ", "أَخُوكَ", "أَخَاكَ")}, "why": "With the owner {كَ}, rafʿ is {أَخُوكَ}."},
                {"s": "... كَبِيرٌ", "gloss": "His father is old.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَبُهُ", "أَبُوهُ", "أَبِيهِ")}, "why": "With the owner {هُ}, rafʿ is {أَبُوهُ}."},
                {"s": "... مُدَرِّسٌ", "gloss": "My father is a teacher.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَبُوكَ", "أَبِي", "أَبُو")}, "why": "With {ـي} it is always {أَبِي}."},
                {"s": "... فِي الْبَيْتِ", "gloss": "The father is in the house.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْأَبُو", "الْأَبُ", "الْأَبَا")}, "why": "With {ال} it is a normal noun: {الْأَبُ}."},
                {"s": "... طَوِيلٌ", "gloss": "Zayd's brother is tall.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَخُو زَيْدٍ", "أَخُ زَيْدٍ", "أَخَا زَيْدٍ")}, "why": "With an owner, rafʿ is {أَخُو}."},
            ],
        },
        {
            "title": "How does each word show its iʿrāb?",
            "prompt": "أَبُو خَالِدٍ ذُو مَالٍ وَأَخِي ذُو عِلْمٍ.",
            "en": "Khalid's father has money, and my brother has knowledge.",
            "fields": [{"key": "use", "label": "Signs", "options": USE}],
            "rows": [
                {"s": "أَبُو", "ans": {"use": "five"}, "why": "It has the owner {خَالِدٍ}. The sign is {و}."},
                {"s": "خَالِدٍ", "ans": {"use": "norm"}, "why": "The owner, with a normal kasra."},
                {"s": "ذُو", "ans": {"use": "five"}, "why": "{ذُو مَالٍ}: the sign is {و}."},
                {"s": "أَخِي", "ans": {"use": "hid"}, "why": "With {ـي} \"my\" the vowel is hidden."},
                {"s": "عِلْمٍ", "ans": {"use": "norm"}, "why": "The owner after {ذُو}, with a normal kasra."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Is it used as a five noun here?",
            "fields": [{"key": "use", "label": "Signs", "options": USE}],
            "rows": [
                {"s": "أَخُوهُ", "gloss": "his brother", "ans": {"use": "five"}, "why": "It has the owner {هُ}. The sign is {و}."},
                {"s": "حَمُوهَا", "gloss": "her father-in-law", "ans": {"use": "five"}, "why": "It has the owner {هَا}. The sign is {و}."},
                {"s": "الْأَخُ", "gloss": "the brother", "ans": {"use": "norm"}, "why": "With {ال}: a normal damma."},
                {"s": "فَمُكَ", "gloss": "your mouth", "ans": {"use": "norm"}, "why": "{فَمٌ} with {م} always takes normal signs."},
                {"s": "فُوكَ", "gloss": "your mouth", "ans": {"use": "five"}, "why": "{فُو} with no {م} and an owner: the sign is {و}."},
                {"s": "أَخِي الْكَبِيرُ", "gloss": "my big brother", "ans": {"use": "hid"}, "why": "With {ـي} \"my\" the vowel is hidden."},
            ],
        },
        {
            "title": "Which word is one of the five nouns?",
            "fields": [{"key": "pick", "label": "Five noun", "options": []}],
            "rows": [
                {"s": "his door / his son / his father", "ans": {"pick": "c"},
                 "opts": {"pick": pick("بَابُهُ", "ابْنُهُ", "أَبُوهُ")}, "why": "{أَبُوهُ} shows the letter {و}."},
                {"s": "your sister / your brother / your mother", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أُخْتُكَ", "أَخُوكَ", "أُمُّكَ")}, "why": "{أَخُوكَ}. The others take normal signs."},
                {"s": "having knowledge / that knowledge / this is knowledge", "ans": {"pick": "a"},
                 "opts": {"pick": pick("ذُو عِلْمٍ", "ذَلِكَ الْعِلْمُ", "هَذَا عِلْمٌ")}, "why": "{ذُو} means \"having\"."},
                {"s": "her uncle / her father-in-law / her maternal uncle", "ans": {"pick": "b"},
                 "opts": {"pick": pick("عَمُّهَا", "حَمُوهَا", "خَالُهَا")}, "why": "{حَمُوهَا} shows {و}. {عَمُّهَا} has a normal damma."},
                {"s": "your mouth / your hand / your face", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فُوكَ", "يَدُكَ", "وَجْهُكَ")}, "why": "{فُوكَ}, with no {م}."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "أَبُو يَاسِرٍ مُهَنْدِسٌ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("Yasir's father is an engineer.", "Yasir is an engineer's father.", "My father Yasir is an engineer.")},
                 "why": "{أَبُو يَاسِرٍ} is \"Yasir's father\". {مُهَنْدِسٌ} is the Information."},
                {"s": "الطَّالِبُ ذُو عِلْمٍ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("This is the student's knowledge.", "The student wants knowledge.", "The student has knowledge.")},
                 "why": "{ذُو عِلْمٍ} means \"having knowledge\"."},
                {"s": "أَخُوهَا فِي الْبَيْتِ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("His brother is in the house.", "Her brother is in the house.", "Her father is in the house.")},
                 "why": "{أَخُو} + {هَا} \"her\"."},
                {"s": "أَبُوكُمْ فِي الْمَسْجِدِ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("Your (pl.) father is in the mosque.", "Our father is in the mosque.", "Your (pl.) brother is in the mosque.")},
                 "why": "{أَبُو} + {كُمْ} \"your (plural)\"."},
                {"s": "أَخِي ذُو مَالٍ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("Your brother has money.", "This is my brother's money.", "My brother has money.")},
                 "why": "{أَخِي} \"my brother\", {ذُو مَالٍ} \"having money\"."},
                {"s": "أَبُونَا مُدَرِّسٌ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("My father is a teacher.", "Our father is a teacher.", "Your father is a teacher.")},
                 "why": "{أَبُو} + {نَا} \"our\"."},
            ],
        },
        {
            "title": "Which letter sign does it show?",
            "fields": [{"key": "letter", "label": "Letter sign", "options": LETTERS}],
            "rows": [
                {"s": "أَبُوهَا", "ans": {"letter": "waw"}, "why": "{أَبُو} + {هَا}: the sign is {و}."},
                {"s": "أَخَاكَ", "ans": {"letter": "alif"}, "why": "{أَخَا} + {كَ}: the sign is {ا}."},
                {"s": "أَبِيهِ", "ans": {"letter": "ya"}, "why": "{أَبِي} + {هِ}: the sign is {ي}."},
                {"s": "ذِي عِلْمٍ", "ans": {"letter": "ya"}, "why": "{ذِي}: the sign is {ي}."},
                {"s": "أَبِي", "gloss": "my father", "ans": {"letter": "none"}, "why": "This {ي} is the pronoun \"my\". The vowel is hidden. No letter sign."},
                {"s": "فَمُهُ", "ans": {"letter": "none"}, "why": "{فَمٌ} with {م}: a normal damma."},
            ],
        },
        {
            "title": "Choose the right form (rafʿ)",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "... طَبِيبٌ", "gloss": "Her brother is a doctor.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَخُوهَا", "أَخُهَا", "أَخِيهَا")}, "why": "The Topic is in rafʿ: {أَخُوهَا}."},
                {"s": "... فِي السُّوقِ", "gloss": "Your (pl.) father is in the market.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَبَاكُمْ", "أَبُوكُمْ", "أَبُكُمْ")}, "why": "With an owner, rafʿ is {أَبُو}."},
                {"s": "... نَظِيفٌ", "gloss": "Your mouth is clean.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فَمُكَ", "فَمُوكَ", "فَمَاكَ")}, "why": "{فَمٌ} with {م} takes a normal damma."},
                {"s": "... طَوِيلٌ", "gloss": "The brother is tall.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْأَخُو", "الْأَخُ", "أَخُو")}, "why": "With {ال} it is a normal noun."},
                {"s": "... تَاجِرٌ", "gloss": "Muhammad's father is a merchant.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَبُ مُحَمَّدٍ", "أَبَا مُحَمَّدٍ", "أَبُو مُحَمَّدٍ")}, "why": "With an owner, rafʿ is {أَبُو}."},
                {"s": "رَجُلٌ ... عِلْمٍ فِي الْمَسْجِدِ", "gloss": "A man with knowledge is in the mosque.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("ذُو", "ذَا", "ذِي")}, "why": "It describes {رَجُلٌ}, which is in rafʿ: {ذُو}."},
            ],
        },
        {
            "title": "How does each word show its iʿrāb?",
            "prompt": "أَبِي طَبِيبٌ، وَأَخُوهُ ذُو مَالٍ.",
            "en": "My father is a doctor, and his brother has money.",
            "fields": [{"key": "use", "label": "Signs", "options": USE}],
            "rows": [
                {"s": "أَبِي", "ans": {"use": "hid"}, "why": "With {ـي} \"my\" the vowel is hidden."},
                {"s": "طَبِيبٌ", "ans": {"use": "norm"}, "why": "The Information, with a normal damma."},
                {"s": "أَخُوهُ", "ans": {"use": "five"}, "why": "It has the owner {هُ}. The sign is {و}."},
                {"s": "ذُو", "ans": {"use": "five"}, "why": "{ذُو مَالٍ}: the sign is {و}."},
                {"s": "مَالٍ", "ans": {"use": "norm"}, "why": "The owner after {ذُو}, with a normal kasra."},
            ],
        },
    ],
}
