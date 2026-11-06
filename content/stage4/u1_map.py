# Stage 4, Unit 1: Nouns in families (أَقْسَامُ الْأَسْمَاءِ)

ONE = {"k": "one", "label": "One", "color": "grey"}
TWO = {"k": "two", "label": "Two", "color": "teal"}
MANY = {"k": "many", "label": "Three or more", "color": "purple"}
NUMBER = [ONE, TWO, MANY]

SING = {"k": "sing", "label": "Singular · مُفْرَدٌ", "color": "grey"}
DUAL = {"k": "dual", "label": "Dual · مُثَنًّى", "color": "teal"}
SMP = {"k": "smp", "label": "Sound m. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ", "color": "blue"}
SFP = {"k": "sfp", "label": "Sound f. plural · جَمْعُ مُؤَنَّثٍ سَالِمٌ", "color": "pink"}
BP = {"k": "bp", "label": "Broken plural · جَمْعُ تَكْسِيرٍ", "color": "purple"}
FAMILY = [SING, DUAL, SMP, SFP, BP]

ORIG = {"k": "orig", "label": "Original signs · أَصْلِيَّةٌ", "color": "green"}
BRANCH = {"k": "branch", "label": "Branch signs · فَرْعِيَّةٌ", "color": "red"}
SIGNS = [ORIG, BRANCH]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s4-map",
    "order": 1,
    "title": "Nouns in families",
    "ar": "أَقْسَامُ الْأَسْمَاءِ",
    "blurb": "Meet the families of nouns in this stage: one, two or more, and which ones change their signs.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 4 · UNIT 1", "title": "Nouns in families",
         "text": "So far every noun ended in damma, fatha or kasra. Some families of nouns show their iʿrāb in a different way. In this stage you learn to recognise each family.",
         "wm": "أَقْسَامُ الْأَسْمَاءِ"},

        {"t": "h2", "text": "Why this stage?"},
        {"t": "p", "text": "Every noun you have met so far took the same three signs: damma for rafʿ, fatha for naṣb, kasra for jarr."},
        {"t": "examples", "items": [
            {"ar": "الْمَسْجِدُ كَبِيرٌ.", "en": "The mosque is big.", "note": "Topic: rafʿ with damma."},
            {"ar": "دَخَلَ الطَّالِبُ الْمَسْجِدَ.", "en": "The student entered the mosque.", "note": "Object: naṣb with fatha."},
            {"ar": "خَرَجَ الطَّالِبُ مِنَ الْمَسْجِدِ.", "en": "The student went out of the mosque.", "note": "After a preposition: jarr with kasra."},
        ]},
        {"t": "p", "text": "Some groups of nouns show iʿrāb differently: with a letter, with another vowel, or with a vowel we cannot see. Stages 5, 6 and 7 teach each case in detail. First you must know which group a noun belongs to. That is Stage 4."},

        {"t": "h2", "text": "Original signs and branch signs"},
        {"t": "cols", "items": [
            {"color": "green", "title": "Original signs", "ar": "الْعَلَامَاتُ الْأَصْلِيَّةُ",
             "text": "Damma for rafʿ, fatha for naṣb, kasra for jarr. The signs you know: {الْكِتَابُ}، {الْكِتَابَ}، {الْكِتَابِ}."},
            {"color": "red", "title": "Branch signs", "ar": "الْعَلَامَاتُ الْفَرْعِيَّةُ",
             "text": "Another sign takes the place of the original one: a letter ({ا}، {و}، {ي}) or a different vowel."},
        ]},
        {"t": "examples", "items": [
            {"ar": "الطَّالِبُ فِي الْفَصْلِ.", "en": "The student is in the classroom.", "note": "One student: damma. An original sign."},
            {"ar": "الطَّالِبَانِ فِي الْفَصْلِ.", "en": "The two students are in the classroom.", "note": "Two students: the letter {ا} shows rafʿ. A branch sign."},
            {"ar": "الْمُدَرِّسُونَ فِي الْفَصْلِ.", "en": "The teachers are in the classroom.", "note": "Many teachers: the letter {و} shows rafʿ. A branch sign."},
        ]},
        {"t": "tip", "text": "A hidden vowel is a third case. The original vowel is there, but we cannot see it or say it: {مُوسَى}، {الْقَاضِي}. Unit 8 explains it."},

        {"t": "h2", "text": "One, two, three or more"},
        {"t": "p", "text": "English has one and more than one. Arabic has three numbers: one, two, and three or more."},
        {"t": "words", "items": [
            {"ar": "كِتَابٌ", "label": "kitābun", "sub": "one book", "color": "grey"},
            {"ar": "كِتَابَانِ", "label": "kitābāni", "sub": "two books", "color": "teal"},
            {"ar": "كُتُبٌ", "label": "kutubun", "sub": "three or more books", "color": "purple"},
        ]},
        {"t": "table", "head": ["Number", "Arabic name", "Example"], "rows": [
            ["One", "مُفْرَدٌ", "{كِتَابٌ} a book"],
            ["Two", "مُثَنًّى", "{كِتَابَانِ} two books"],
            ["Three or more", "جَمْعٌ", "{كُتُبٌ} books"],
        ]},
        {"t": "examples", "items": [
            {"ar": "هَذَا كِتَابٌ.", "en": "This is a book."},
            {"ar": "هَذَانِ كِتَابَانِ.", "en": "These are two books.", "note": "{هَذَانِ} is the pointing word for two. You met it in Stage 3."},
            {"ar": "هَذِهِ كُتُبٌ.", "en": "These are books.", "note": "Plural things take {هَذِهِ}."},
        ]},

        {"t": "h2", "text": "The singular (مُفْرَدٌ)"},
        {"t": "rule", "color": "grey", "title": "One person or one thing",
         "text": "A singular noun means one: {رَجُلٌ}، {سَاعَةٌ}، {بَيْتٌ}. It can be masculine or feminine, with {ال} or without. It takes the original signs."},
        {"t": "words", "items": [
            {"ar": "طَالِبٌ", "sub": "a student", "color": "grey"},
            {"ar": "مَدْرَسَةٌ", "sub": "a school", "color": "grey"},
            {"ar": "الْقَلَمُ", "sub": "the pen", "color": "grey"},
            {"ar": "الْبِنْتُ", "sub": "the girl", "color": "grey"},
        ]},
        {"t": "tip", "text": "A few singular nouns have their own signs. Names like {أَحْمَدُ} are diptotes (Unit 6). {أَبُوكَ} \"your father\" is one of the five nouns (Unit 7). {مُوسَى} and {الْقَاضِي} hide their vowel (Unit 8)."},

        {"t": "h2", "text": "Sound plural or broken plural?"},
        {"t": "p", "text": "There are three kinds of plural. Look at what happens to the singular."},
        {"t": "table", "head": ["Singular", "Plural", "What happens", "Family"], "rows": [
            ["مُسْلِمٌ", "مُسْلِمُونَ", "The word stays whole. {ـُونَ} is added.", "Sound masculine plural"],
            ["مُدَرِّسَةٌ", "مُدَرِّسَاتٌ", "The word stays whole. {ة} goes and {ـَاتٌ} is added.", "Sound feminine plural"],
            ["كِتَابٌ", "كُتُبٌ", "The inside of the word changes.", "Broken plural"],
            ["رَجُلٌ", "رِجَالٌ", "The inside of the word changes.", "Broken plural"],
        ]},
        {"t": "rule", "color": "purple", "title": "Sound means whole",
         "text": "In a sound plural ({سَالِمٌ} \"safe\") the singular is kept safe and an ending is added. In a broken plural ({تَكْسِيرٌ} \"breaking\") the singular is broken and rebuilt."},
        {"t": "tip", "text": "Units 3, 4 and 5 teach the three plurals one by one."},

        {"t": "h2", "text": "The map of Stage 4"},
        {"t": "p", "text": "Here is every family of this stage with one example. The last column is only a preview. Stages 5, 6 and 7 teach the signs in detail."},
        {"t": "table", "head": ["Family", "Arabic name", "Example", "Signs"], "rows": [
            ["Singular (this unit)", "مُفْرَدٌ", "كِتَابٌ", "Original"],
            ["Dual (Unit 2)", "مُثَنًّى", "كِتَابَانِ", "Branch: letters {ا} / {ي}"],
            ["Sound masculine plural (Unit 3)", "جَمْعُ مُذَكَّرٍ سَالِمٌ", "مُسْلِمُونَ", "Branch: letters {و} / {ي}"],
            ["Sound feminine plural (Unit 4)", "جَمْعُ مُؤَنَّثٍ سَالِمٌ", "سَيَّارَاتٌ", "Mostly original. One branch sign: kasra for naṣb."],
            ["Broken plural (Unit 5)", "جَمْعُ تَكْسِيرٍ", "كُتُبٌ", "Original"],
            ["Diptote (Unit 6)", "الْمَمْنُوعُ مِنَ الصَّرْفِ", "أَحْمَدُ", "No tanween. Branch: fatha for jarr (kasra again with {ال} or an owner)."],
            ["The five nouns (Unit 7)", "الْأَسْمَاءُ الْخَمْسَةُ", "أَبُوكَ", "Branch: letters {و} / {ا} / {ي}"],
            ["Hidden vowel (Unit 8)", "{الْمَقْصُورُ}، {الْمَنْقُوصُ}، and a noun with {ـِي} \"my\"", "{مُوسَى}، {الْقَاضِي}، {كِتَابِي}", "Original, but hidden: we cannot see it."],
        ]},
        {"t": "words", "items": [
            {"ar": "كِتَابٌ", "sub": "singular", "color": "grey"},
            {"ar": "كِتَابَانِ", "sub": "dual", "color": "teal"},
            {"ar": "مُسْلِمُونَ", "sub": "sound m. plural", "color": "blue"},
            {"ar": "سَيَّارَاتٌ", "sub": "sound f. plural", "color": "pink"},
            {"ar": "كُتُبٌ", "sub": "broken plural", "color": "purple"},
            {"ar": "أَحْمَدُ", "sub": "diptote", "color": "orange"},
            {"ar": "أَبُوكَ", "sub": "five nouns", "color": "gold"},
            {"ar": "مُوسَى", "sub": "hidden vowel", "color": "brown"},
        ]},
        {"t": "tip", "text": "A word can be in two families. {مَسَاجِدُ} \"mosques\" is a broken plural and also a diptote. Unit 6 shows how."},

        {"t": "summary", "title": "In short", "items": [
            "Original signs: damma for rafʿ, fatha for naṣb, kasra for jarr.",
            "Branch signs: a letter or another vowel takes the place of the original sign.",
            "Arabic has three numbers: one {كِتَابٌ}، two {كِتَابَانِ}، three or more {كُتُبٌ}.",
            "A singular means one. It takes the original signs, except diptotes and the five nouns. A hidden vowel is original, but hidden.",
            "Sound plural: the singular stays whole and gets {ـُونَ} or {ـَاتٌ}. Broken plural: the inside changes.",
        ]},
    ],

    "practice": [
        {
            "title": "One, two, or three or more?",
            "fields": [{"key": "num", "label": "How many", "options": NUMBER}],
            "rows": [
                {"s": "قَلَمٌ", "gloss": "pen(s)", "ans": {"num": "one"}, "why": "No ending is added: one pen."},
                {"s": "قَلَمَانِ", "gloss": "pen(s)", "ans": {"num": "two"}, "why": "{ـَانِ} is added to {قَلَمٌ}: two pens."},
                {"s": "أَقْلَامٌ", "gloss": "pen(s)", "ans": {"num": "many"}, "why": "The plural of {قَلَمٌ}: three or more pens."},
                {"s": "بَيْتَانِ", "gloss": "house(s)", "ans": {"num": "two"}, "why": "{بَيْتٌ} + {ـَانِ}: two houses."},
                {"s": "رِجَالٌ", "gloss": "man / men", "ans": {"num": "many"}, "why": "The plural of {رَجُلٌ}: three or more men."},
                {"s": "سَاعَةٌ", "gloss": "watch(es)", "ans": {"num": "one"}, "why": "One watch. The {ة} shows feminine. It does not show number."},
            ],
        },
        {
            "title": "Which family?",
            "fields": [{"key": "fam", "label": "Family", "options": FAMILY}],
            "rows": [
                {"s": "مُدَرِّسُونَ", "gloss": "teachers", "ans": {"fam": "smp"}, "why": "{مُدَرِّسٌ} stays whole and gets {ـُونَ}."},
                {"s": "سَيَّارَاتٌ", "gloss": "cars", "ans": {"fam": "sfp"}, "why": "{سَيَّارَةٌ}: the {ة} goes and {ـَاتٌ} is added."},
                {"s": "كُتُبٌ", "gloss": "books", "ans": {"fam": "bp"}, "why": "The inside of {كِتَابٌ} changes."},
                {"s": "طَالِبَانِ", "gloss": "student(s)", "ans": {"fam": "dual"}, "why": "{طَالِبٌ} + {ـَانِ}: exactly two."},
                {"s": "بَيْتٌ", "gloss": "house(s)", "ans": {"fam": "sing"}, "why": "One house: singular."},
                {"s": "مُهَنْدِسُونَ", "gloss": "engineers", "ans": {"fam": "smp"}, "why": "{مُهَنْدِسٌ} stays whole and gets {ـُونَ}."},
            ],
        },
        {
            "title": "Original or branch signs? (preview)",
            "fields": [{"key": "sign", "label": "Signs", "options": SIGNS}],
            "rows": [
                {"s": "الْكِتَابُ", "gloss": "the book", "ans": {"sign": "orig"}, "why": "A singular: damma, fatha, kasra."},
                {"s": "الْكِتَابَانِ", "gloss": "the two books", "ans": {"sign": "branch"}, "why": "A dual: a letter shows its iʿrāb."},
                {"s": "الْمُسْلِمُونَ", "gloss": "the Muslims", "ans": {"sign": "branch"}, "why": "A sound masculine plural: a letter shows its iʿrāb."},
                {"s": "الْكُتُبُ", "gloss": "the books", "ans": {"sign": "orig"}, "why": "A broken plural takes damma, fatha and kasra like a singular."},
                {"s": "الرَّجُلُ", "gloss": "the man", "ans": {"sign": "orig"}, "why": "A singular: damma, fatha, kasra."},
                {"s": "أَبُوكَ", "gloss": "your father", "ans": {"sign": "branch"}, "why": "One of the five nouns. The letter {و} shows rafʿ. Unit 7."},
            ],
        },
        {
            "title": "Find the singular",
            "fields": [{"key": "pick", "label": "Singular", "options": []}],
            "rows": [
                {"s": "بُيُوتٌ", "gloss": "houses", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بَيْتٌ", "بَيْتَانِ", "بِنْتٌ")}, "why": "{بُيُوتٌ} is the plural of {بَيْتٌ}. {بَيْتَانِ} is two houses."},
                {"s": "طُلَّابٌ", "gloss": "students", "ans": {"pick": "b"},
                 "opts": {"pick": pick("طَالِبَانِ", "طَالِبٌ", "طَلَبٌ")}, "why": "{طُلَّابٌ} is the plural of {طَالِبٌ}."},
                {"s": "أَوْلَادٌ", "gloss": "boys", "ans": {"pick": "a"},
                 "opts": {"pick": pick("وَلَدٌ", "وَالِدٌ", "وَلَدَانِ")}, "why": "{أَوْلَادٌ} is the plural of {وَلَدٌ}."},
                {"s": "مُدَرِّسُونَ", "gloss": "teachers", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُدَرِّسَةٌ", "دَرْسٌ", "مُدَرِّسٌ")}, "why": "Take away {ـُونَ}: {مُدَرِّسٌ}."},
                {"s": "مُسْلِمَاتٌ", "gloss": "Muslim women", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُسْلِمٌ", "مُسْلِمَةٌ", "مُسْلِمُونَ")}, "why": "Women: the feminine singular {مُسْلِمَةٌ}. Take away {ـَاتٌ} and put back {ة}."},
            ],
        },
        {
            "title": "Same family: which word matches?",
            "fields": [{"key": "pick", "label": "Same family", "options": []}],
            "rows": [
                {"s": "الْمُسْلِمُونَ", "gloss": "the Muslims", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الْمُهَنْدِسُونَ", "الْمُسْلِمَاتُ", "الْمُسْلِمُ")},
                 "why": "Both are sound masculine plurals: a whole singular + {ـُونَ}."},
                {"s": "كُتُبٌ", "gloss": "books", "ans": {"pick": "b"},
                 "opts": {"pick": pick("كِتَابَانِ", "رِجَالٌ", "كِتَابٌ")},
                 "why": "Both are broken plurals. The same root does not make the same family."},
                {"s": "سَاعَتَانِ", "gloss": "two watches", "ans": {"pick": "b"},
                 "opts": {"pick": pick("سَاعَاتٌ", "بَابَانِ", "سَاعَةٌ")},
                 "why": "Both are duals: {ـَانِ} at the end."},
                {"s": "سَيَّارَاتٌ", "gloss": "cars", "ans": {"pick": "b"},
                 "opts": {"pick": pick("سَيَّارَةٌ", "مُدَرِّسَاتٌ", "سَيَّارَتَانِ")},
                 "why": "Both are sound feminine plurals: {ـَاتٌ} at the end."},
                {"s": "قَلَمٌ", "gloss": "a pen", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَقْلَامٌ", "قَلَمَانِ", "بَابٌ")},
                 "why": "Both are singular: one pen, one door."},
            ],
        },
        {
            "title": "Which family is the word in [ ]?",
            "fields": [{"key": "fam", "label": "Family", "options": FAMILY}],
            "rows": [
                {"s": "[الطُّلَّابُ] فِي الْفَصْلِ.", "gloss": "The students are in the classroom.", "ans": {"fam": "bp"},
                 "why": "The plural of {طَالِبٌ}. The inside of the word changes."},
                {"s": "[الْمُدَرِّسُونَ] فِي الْمَسْجِدِ.", "gloss": "The teachers are in the mosque.", "ans": {"fam": "smp"},
                 "why": "{مُدَرِّسٌ} + {ـُونَ}."},
                {"s": "هَذَانِ [بَابَانِ].", "gloss": "These are two doors.", "ans": {"fam": "dual"},
                 "why": "{بَابٌ} + {ـَانِ}: two doors."},
                {"s": "[الْمُهَنْدِسَاتُ] فِي الْجَامِعَةِ.", "gloss": "The female engineers are in the university.", "ans": {"fam": "sfp"},
                 "why": "{مُهَنْدِسَةٌ}: the {ة} goes and {ـَاتُ} is added."},
                {"s": "[الْبَابُ] مَفْتُوحٌ.", "gloss": "The door is open.", "ans": {"fam": "sing"},
                 "why": "One door: singular."},
                {"s": "دَخَلَ [الرِّجَالُ] الْمَسْجِدَ.", "gloss": "The men entered the mosque.", "ans": {"fam": "bp"},
                 "why": "The plural of {رَجُلٌ}. The inside of the word changes."},
            ],
        },
    ],

    "homework": [
        {
            "title": "One, two, or three or more?",
            "fields": [{"key": "num", "label": "How many", "options": NUMBER}],
            "rows": [
                {"s": "أَصْدِقَاءُ", "gloss": "friend(s)", "ans": {"num": "many"}, "why": "The plural of {صَدِيقٌ}: three or more friends."},
                {"s": "مَدْرَسَتَانِ", "gloss": "school(s)", "ans": {"num": "two"}, "why": "{مَدْرَسَةٌ} + {ـَانِ}. The {ة} became {ت}: two schools."},
                {"s": "مِفْتَاحٌ", "gloss": "key(s)", "ans": {"num": "one"}, "why": "One key."},
                {"s": "مَفَاتِيحُ", "gloss": "key(s)", "ans": {"num": "many"}, "why": "The plural of {مِفْتَاحٌ}: three or more keys."},
                {"s": "بِنْتَانِ", "gloss": "girl(s)", "ans": {"num": "two"}, "why": "{بِنْتٌ} + {ـَانِ}: two girls."},
                {"s": "مُهَنْدِسَاتٌ", "gloss": "female engineer(s)", "ans": {"num": "many"}, "why": "{ـَاتٌ} makes a plural: three or more."},
            ],
        },
        {
            "title": "Which family?",
            "fields": [{"key": "fam", "label": "Family", "options": FAMILY}],
            "rows": [
                {"s": "حَقِيبَتَانِ", "gloss": "bag(s)", "ans": {"fam": "dual"}, "why": "{حَقِيبَةٌ} + {ـَانِ}, with {ة} becoming {ت}."},
                {"s": "الْمُسْلِمَاتُ", "gloss": "the Muslim women", "ans": {"fam": "sfp"}, "why": "{مُسْلِمَةٌ}: the {ة} goes and {ـَاتُ} is added."},
                {"s": "كِلَابٌ", "gloss": "dogs", "ans": {"fam": "bp"}, "why": "The inside of {كَلْبٌ} changes."},
                {"s": "مَدْرَسَةٌ", "gloss": "school(s)", "ans": {"fam": "sing"}, "why": "One school. The {ة} only shows feminine."},
                {"s": "الْمُهَنْدِسُونَ", "gloss": "the engineers", "ans": {"fam": "smp"}, "why": "{مُهَنْدِسٌ} stays whole and gets {ـُونَ}."},
                {"s": "أَبْوَابٌ", "gloss": "doors", "ans": {"fam": "bp"}, "why": "The plural of {بَابٌ}. The inside of the word changes."},
            ],
        },
        {
            "title": "Original or branch signs? (preview)",
            "fields": [{"key": "sign", "label": "Signs", "options": SIGNS}],
            "rows": [
                {"s": "رَجُلَانِ", "gloss": "two men", "ans": {"sign": "branch"}, "why": "A dual: a letter shows its iʿrāb."},
                {"s": "الْبُيُوتُ", "gloss": "the houses", "ans": {"sign": "orig"}, "why": "A broken plural: damma, fatha, kasra."},
                {"s": "مُسْلِمُونَ", "gloss": "Muslims", "ans": {"sign": "branch"}, "why": "A sound masculine plural: a letter shows its iʿrāb."},
                {"s": "الْوَلَدُ", "gloss": "the boy", "ans": {"sign": "orig"}, "why": "A singular: damma, fatha, kasra."},
                {"s": "مِفْتَاحَانِ", "gloss": "two keys", "ans": {"sign": "branch"}, "why": "A dual: a letter shows its iʿrāb."},
                {"s": "غُرْفَةٌ", "gloss": "a room", "ans": {"sign": "orig"}, "why": "A singular. The {ة} does not change the signs."},
            ],
        },
        {
            "title": "Find the singular",
            "fields": [{"key": "pick", "label": "Singular", "options": []}],
            "rows": [
                {"s": "أَصْدِقَاءُ", "gloss": "friends", "ans": {"pick": "c"},
                 "opts": {"pick": pick("صِدْقٌ", "صَدِيقَانِ", "صَدِيقٌ")}, "why": "{أَصْدِقَاءُ} is the plural of {صَدِيقٌ}. {صَدِيقَانِ} is two friends."},
                {"s": "مَسَاجِدُ", "gloss": "mosques", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَسْجِدٌ", "سَاجِدٌ", "مَسْجِدَانِ")}, "why": "{مَسَاجِدُ} is the plural of {مَسْجِدٌ}."},
                {"s": "مَفَاتِيحُ", "gloss": "keys", "ans": {"pick": "b"},
                 "opts": {"pick": pick("فَتْحٌ", "مِفْتَاحٌ", "مَفْتُوحٌ")}, "why": "{مَفَاتِيحُ} is the plural of {مِفْتَاحٌ}. {مَفْتُوحٌ} means \"open\"."},
                {"s": "مُدَرِّسَاتٌ", "gloss": "female teachers", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُدَرِّسَةٌ", "مُدَرِّسٌ", "مُدَرِّسُونَ")}, "why": "Take away {ـَاتٌ} and put back {ة}: {مُدَرِّسَةٌ}."},
                {"s": "سَيَّارَتَانِ", "gloss": "two cars", "ans": {"pick": "c"},
                 "opts": {"pick": pick("سَيَّارٌ", "سَيَّارَاتٌ", "سَيَّارَةٌ")}, "why": "Take away {ـَانِ} and put back {ة}: {سَيَّارَةٌ}."},
                {"s": "دَفَاتِرُ", "gloss": "notebooks", "ans": {"pick": "b"},
                 "opts": {"pick": pick("دَفْتَرَانِ", "دَفْتَرٌ", "فَتْرَةٌ")}, "why": "{دَفَاتِرُ} is the plural of {دَفْتَرٌ}. {دَفْتَرَانِ} is two notebooks."},
            ],
        },
        {
            "title": "Same family: which word matches?",
            "fields": [{"key": "pick", "label": "Same family", "options": []}],
            "rows": [
                {"s": "نُجُومٌ", "gloss": "stars", "ans": {"pick": "c"},
                 "opts": {"pick": pick("نَجْمَانِ", "مُدَرِّسُونَ", "بُيُوتٌ")},
                 "why": "Both are broken plurals. {مُدَرِّسُونَ} is a plural too, but a sound one."},
                {"s": "وَلَدَانِ", "gloss": "two boys", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَوْلَادٌ", "مَسْجِدَانِ", "وَلَدٌ")},
                 "why": "Both are duals: {ـَانِ} at the end."},
                {"s": "مُهَنْدِسَاتٌ", "gloss": "female engineers", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُسْلِمَاتٌ", "مُهَنْدِسُونَ", "مُهَنْدِسَةٌ")},
                 "why": "Both are sound feminine plurals: {ـَاتٌ} at the end."},
                {"s": "كِتَابٌ", "gloss": "a book", "ans": {"pick": "a"},
                 "opts": {"pick": pick("سَاعَةٌ", "كُتُبٌ", "كِتَابَانِ")},
                 "why": "Both are singular. Masculine or feminine does not change the family."},
                {"s": "الْمُدَرِّسُونَ", "gloss": "the teachers", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْمُدَرِّسَاتُ", "الْمُهَنْدِسُونَ", "الْمُدَرِّسَانِ")},
                 "why": "Both are sound masculine plurals: a whole singular + {ـُونَ}."},
            ],
        },
        {
            "title": "Which family is the word in [ ]?",
            "fields": [{"key": "fam", "label": "Family", "options": FAMILY}],
            "rows": [
                {"s": "[الْأَوْلَادُ] فِي الْبَيْتِ.", "gloss": "The boys are in the house.", "ans": {"fam": "bp"},
                 "why": "The plural of {وَلَدٌ}. The inside of the word changes."},
                {"s": "خَرَجَ [الْمُسْلِمُونَ] مِنَ الْمَسْجِدِ.", "gloss": "The Muslims went out of the mosque.", "ans": {"fam": "smp"},
                 "why": "{مُسْلِمٌ} + {ـُونَ}."},
                {"s": "هَؤُلَاءِ [مُدَرِّسَاتٌ].", "gloss": "These are female teachers.", "ans": {"fam": "sfp"},
                 "why": "{مُدَرِّسَةٌ}: the {ة} goes and {ـَاتٌ} is added."},
                {"s": "[الْبِنْتَانِ] فِي الْمَدْرَسَةِ.", "gloss": "The two girls are in the school.", "ans": {"fam": "dual"},
                 "why": "{الْبِنْتُ} + {ـَانِ}: two girls."},
                {"s": "ذَهَبَ [الْمُدِيرُ] إِلَى السُّوقِ.", "gloss": "The principal went to the market.", "ans": {"fam": "sing"},
                 "why": "One principal: singular."},
                {"s": "[الْأَقْلَامُ] عَلَى الْمَكْتَبِ.", "gloss": "The pens are on the desk.", "ans": {"fam": "bp"},
                 "why": "The plural of {قَلَمٌ}. The inside of the word changes."},
            ],
        },
    ],
}
