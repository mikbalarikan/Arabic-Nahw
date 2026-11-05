# Stage 0, Unit 8: Stage 0 check-up (mixed quiz over units 1-7)


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abc", labels)]


MARKS = [
    {"k": "fatha", "label": "Fatha ـَ", "color": "pink"},
    {"k": "damma", "label": "Single damma ـُ", "color": "red"},
    {"k": "kasra", "label": "Kasra ـِ", "color": "green"},
    {"k": "sukun", "label": "Sukūn ـْ", "color": "navy"},
    {"k": "tanween", "label": "Tanween (doubled) ـٌ ـً ـٍ", "color": "olive"},
]

KINDS = [
    {"k": "ism", "label": "Ism · اِسْمٌ", "color": "blue"},
    {"k": "fil", "label": "Fiʿl · فِعْلٌ", "color": "navy"},
    {"k": "harf", "label": "Ḥarf · حَرْفٌ", "color": "grey"},
]

GENDER = [
    {"k": "m", "label": "Masculine · مُذَكَّرٌ", "color": "blue"},
    {"k": "f", "label": "Feminine · مُؤَنَّثٌ", "color": "pink"},
]

DEF = [
    {"k": "marifa", "label": "Maʿrifa · مَعْرِفَةٌ", "color": "teal"},
    {"k": "nakira", "label": "Nakira · نَكِرَةٌ", "color": "brown"},
]

SUNMOON = [
    {"k": "sun", "label": "Sun letter", "color": "gold"},
    {"k": "moon", "label": "Moon letter", "color": "navy"},
]

JOBS = [
    {"k": "topic", "label": "Topic · مُبْتَدَأٌ", "color": "gold"},
    {"k": "info", "label": "Information · خَبَرٌ", "color": "red"},
    {"k": "prep", "label": "After a preposition", "color": "green"},
    {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"},
]

FORMS = [
    {"k": "raf", "label": "Rafʿ · رَفْعٌ", "color": "red"},
    {"k": "jarr", "label": "Jarr · جَرٌّ", "color": "green"},
]


UNIT = {
    "id": "s0-checkup",
    "order": 8,
    "title": "Stage 0 check-up",
    "ar": "مُرَاجَعَةٌ",
    "blurb": "A short mixed quiz on all of Stage 0. Pass it and you are ready for Stage 1.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 0 · UNIT 8", "title": "Are you ready for Stage 1?",
         "text": "Eight cards, one or more for every Stage 0 unit. Do them without your notes.",
         "wm": "مُرَاجَعَةٌ"},

        {"t": "h2", "text": "How the check-up works"},
        {"t": "p", "text": "The practice cards are the check-up. Do them in class, alone, in one go. Your teacher sees which cards you got right."},
        {"t": "p", "text": "If a card goes badly, go back to its unit and read the notes again. The homework cards are for review at home."},
        {"t": "tip", "text": "The last card matters most. It asks for the ending a word needs, which is the main skill of Stage 1."},

        {"t": "summary", "title": "What the check-up covers", "items": [
            "1. Reading the marks: fatha, damma, kasra, sukūn, shadda, tanween, long vowels.",
            "2. Ism, fiʿl and ḥarf.",
            "3. Masculine and feminine: {ة}, {هُوَ} and {هِيَ}.",
            "4. Maʿrifa and nakira: {ال} or tanween.",
            "5. Sun and moon letters, hamzat al-waṣl.",
            "6. Adjective and iḍāfa, phrase or sentence.",
            "7. Iʿrāb: role → form → sign.",
        ]},
    ],

    "practice": [
        {
            "title": "Which mark is on the last letter?",
            "fields": [{"key": "mark", "label": "Mark", "options": MARKS}],
            "rows": [
                {"s": "مِنْ", "gloss": "from", "ans": {"mark": "sukun"}, "why": "The small circle {ـْ} on the {ن}: sukūn."},
                {"s": "الْبَيْتِ", "ans": {"mark": "kasra"}, "why": "A small stroke under the {ت}: kasra."},
                {"s": "ذَهَبَ", "gloss": "he went", "ans": {"mark": "fatha"}, "why": "A small stroke over the {ب}: fatha."},
                {"s": "كِتَابٌ", "gloss": "a book", "ans": {"mark": "tanween"}, "why": "A doubled damma {ـٌ}: tanween, read kitābun."},
                {"s": "الْقَلَمُ", "gloss": "the pen", "ans": {"mark": "damma"}, "why": "A single small {و} shape over the {م}: damma."},
            ],
        },
        {
            "title": "Ism, fiʿl or ḥarf?",
            "prompt": "خَرَجَ الْمُدِيرُ مِنَ الْمَدْرَسَةِ",
            "en": "The principal went out of the school.",
            "fields": [{"key": "kind", "label": "Kind", "options": KINDS}],
            "rows": [
                {"s": "خَرَجَ", "gloss": "went out", "ans": {"kind": "fil"}, "why": "A past action: {خَرَجَ} 'he went out'."},
                {"s": "الْمُدِيرُ", "gloss": "the principal", "ans": {"kind": "ism"}, "why": "A person, and it has {ال}: ism."},
                {"s": "مِنَ", "gloss": "from", "ans": {"kind": "harf"}, "why": "A preposition. It means nothing alone: ḥarf."},
                {"s": "الْمَدْرَسَةِ", "gloss": "the school", "ans": {"kind": "ism"}, "why": "A place, with {ال} and kasra after {مِنَ}: ism."},
            ],
        },
        {
            "title": "Masculine or feminine?",
            "fields": [{"key": "g", "label": "Gender", "options": GENDER}],
            "rows": [
                {"s": "السَّيَّارَةُ", "gloss": "the car", "ans": {"g": "f"}, "why": "Ends in {ة}. We say {هِيَ}."},
                {"s": "الْمَطْبَخُ", "gloss": "the kitchen", "ans": {"g": "m"}, "why": "No {ة}. We say {هُوَ}."},
                {"s": "الْحَقِيبَةُ", "gloss": "the bag", "ans": {"g": "f"}, "why": "Ends in {ة}: feminine."},
                {"s": "الْبِنْتُ", "gloss": "the girl", "ans": {"g": "f"}, "why": "No {ة}, but a girl is female. We say {هِيَ}."},
                {"s": "الشَّارِعُ", "gloss": "the street", "ans": {"g": "m"}, "why": "No {ة}: masculine, {هُوَ}."},
                {"s": "زَيْنَبُ", "gloss": "Zaynab", "ans": {"g": "f"}, "why": "A woman's name. Feminine, even without {ة}."},
            ],
        },
        {
            "title": "Maʿrifa or nakira?",
            "fields": [{"key": "d", "label": "Definite?", "options": DEF}],
            "rows": [
                {"s": "قَلَمٌ", "gloss": "a pen", "ans": {"d": "nakira"}, "why": "Tanween, no {ال}: 'a pen'."},
                {"s": "الدُّكَّانُ", "gloss": "the shop", "ans": {"d": "marifa"}, "why": "It has {ال}: 'the shop'."},
                {"s": "غُرْفَةٌ", "gloss": "a room", "ans": {"d": "nakira"}, "why": "Tanween on the {ة}: 'a room'."},
                {"s": "الْغُرْفَةُ", "gloss": "the room", "ans": {"d": "marifa"}, "why": "{ال} and a single damma: 'the room'."},
                {"s": "بَيْتٌ", "gloss": "a house", "ans": {"d": "nakira"}, "why": "Tanween means 'a': 'a house'."},
            ],
        },
        {
            "title": "Sun letter or moon letter after {ال}?",
            "fields": [{"key": "sm", "label": "Letter", "options": SUNMOON}],
            "rows": [
                {"s": "الشَّمْسُ", "ans": {"sm": "sun"}, "why": "Shadda on {ش}, the {ل} is silent: ash-shamsu."},
                {"s": "الْقَمَرُ", "ans": {"sm": "moon"}, "why": "Sukūn on the {ل}, you hear it: al-qamaru."},
                {"s": "الطَّالِبُ", "ans": {"sm": "sun"}, "why": "Shadda on {ط}: aṭ-ṭālibu."},
                {"s": "الْمَسْجِدُ", "ans": {"sm": "moon"}, "why": "{م} is a moon letter: al-masjidu."},
                {"s": "الدَّفْتَرُ", "ans": {"sm": "sun"}, "why": "Shadda on {د}: ad-daftaru."},
                {"s": "الْكِتَابُ", "ans": {"sm": "moon"}, "why": "{ك} is a moon letter: al-kitābu."},
            ],
        },
        {
            "title": "Adjective or iḍāfa?",
            "fields": [{"key": "type", "label": "Type", "options": [
                {"k": "adj", "label": "Noun + adjective · صِفَةٌ", "color": "grey"},
                {"k": "idafa", "label": "Iḍāfa · إِضَافَةٌ", "color": "purple"},
            ]}],
            "rows": [
                {"s": "الْبَيْتُ الْجَدِيدُ", "gloss": "the new house", "ans": {"type": "adj"}, "why": "{الْجَدِيدُ} describes the house and copies its {ال} and damma."},
                {"s": "بَيْتُ الْإِمَامِ", "gloss": "the imam's house", "ans": {"type": "idafa"}, "why": "The first word has no {ال}, the owner is jarr."},
                {"s": "كِتَابٌ جَدِيدٌ", "gloss": "a new book", "ans": {"type": "adj"}, "why": "Both words have tanween damma. The second describes the first."},
                {"s": "كِتَابُ مُحَمَّدٍ", "gloss": "Muhammad's book", "ans": {"type": "idafa"}, "why": "{كِتَابُ} has no tanween, {مُحَمَّدٍ} is the owner in jarr."},
                {"s": "بَابُ الْمَسْجِدِ", "gloss": "the mosque door", "ans": {"type": "idafa"}, "why": "The door belongs to the mosque. {الْمَسْجِدِ} ends in kasra."},
                {"s": "الْقَلَمُ الْمَكْسُورُ", "gloss": "the broken pen", "ans": {"type": "adj"}, "why": "{الْمَكْسُورُ} describes the pen and copies {ال} and damma."},
            ],
        },
        {
            "title": "Phrase or sentence?",
            "fields": [{"key": "ps", "label": "Type", "options": [
                {"k": "phrase", "label": "Phrase (not complete)"},
                {"k": "sentence", "label": "Sentence (complete)"},
            ]}],
            "rows": [
                {"s": "الْبَيْتُ جَدِيدٌ", "ans": {"ps": "sentence"}, "why": "{ال} on the first word, tanween on the second: 'The house is new.'"},
                {"s": "الْبَيْتُ الْجَدِيدُ", "ans": {"ps": "phrase"}, "why": "Both words have {ال}: 'the new house'. Nothing is said about it yet."},
                {"s": "بَابُ الْمَدْرَسَةِ", "ans": {"ps": "phrase"}, "why": "An iḍāfa: 'the school door'. It needs Information."},
                {"s": "بَابُ الْمَدْرَسَةِ مُغْلَقٌ", "ans": {"ps": "sentence"}, "why": "Topic {بَابُ الْمَدْرَسَةِ} plus Information {مُغْلَقٌ}."},
                {"s": "الْوَلَدُ الصَّغِيرُ", "ans": {"ps": "phrase"}, "why": "Noun + adjective, both with {ال}: 'the small boy'."},
                {"s": "الْوَلَدُ جَالِسٌ", "ans": {"ps": "sentence"}, "why": "'The boy is sitting.' {جَالِسٌ} has tanween, so it is the Information."},
            ],
        },
        {
            "title": "Choose the right ending",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "الطَّالِبُ فِي ___ (الْفَصْلُ)", "gloss": "The student is in the classroom.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الْفَصْلُ", "الْفَصْلَ", "الْفَصْلِ")}, "why": "After {فِي}: jarr, kasra."},
                {"s": "___ مَفْتُوحٌ (الْبَابُ)", "gloss": "The door is open.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الْبَابُ", "الْبَابِ", "الْبَابٌ")}, "why": "The Topic is rafʿ, and {ال} takes no tanween."},
                {"s": "بَيْتُ ___ قَرِيبٌ (التَّاجِرُ)", "gloss": "The merchant's house is near.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("التَّاجِرُ", "التَّاجِرِ", "التَّاجِرٍ")}, "why": "The owner in iḍāfa is jarr: {التَّاجِرِ}."},
                {"s": "الْمَاءُ ___ (بَارِدٌ)", "gloss": "The water is cold.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بَارِدٌ", "بَارِدٍ", "الْبَارِدُ")}, "why": "The Information is rafʿ and indefinite: {بَارِدٌ}. {الْبَارِدُ} would make a phrase."},
                {"s": "هِيَ عَلَى ___ (سَرِيرٌ)", "gloss": "It is on a bed.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("سَرِيرٌ", "سَرِيرٍ", "سَرِيرِ")}, "why": "After {عَلَى}, indefinite: tanween kasra {سَرِيرٍ}."},
                {"s": "مُحَمَّدٌ ___ (مُهَنْدِسٌ)", "gloss": "Muhammad is an engineer.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُهَنْدِسٍ", "مُهَنْدِسُ", "مُهَنْدِسٌ")}, "why": "The Information is rafʿ: {مُهَنْدِسٌ}."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Which mark is on the last letter?",
            "fields": [{"key": "mark", "label": "Mark", "options": MARKS}],
            "rows": [
                {"s": "نَعَمْ", "gloss": "yes", "ans": {"mark": "sukun"}, "why": "The small circle on the {م}: sukūn."},
                {"s": "أَيْنَ", "gloss": "where", "ans": {"mark": "fatha"}, "why": "A stroke over the {ن}: fatha, read ayna."},
                {"s": "الْمِفْتَاحِ", "ans": {"mark": "kasra"}, "why": "A stroke under the {ح}: kasra."},
                {"s": "سُكَّرٌ", "gloss": "sugar", "ans": {"mark": "tanween"}, "why": "A doubled damma {ـٌ}: sukkarun."},
                {"s": "الْخُبْزُ", "gloss": "the bread", "ans": {"mark": "damma"}, "why": "A single damma on the {ز}."},
            ],
        },
        {
            "title": "Ism, fiʿl or ḥarf?",
            "prompt": "جَلَسَ الرَّجُلُ عَلَى السَّرِيرِ",
            "en": "The man sat on the bed.",
            "fields": [{"key": "kind", "label": "Kind", "options": KINDS}],
            "rows": [
                {"s": "جَلَسَ", "gloss": "sat", "ans": {"kind": "fil"}, "why": "A past action: {جَلَسَ} 'he sat'."},
                {"s": "الرَّجُلُ", "gloss": "the man", "ans": {"kind": "ism"}, "why": "A person with {ال}: ism."},
                {"s": "عَلَى", "gloss": "on", "ans": {"kind": "harf"}, "why": "A preposition: ḥarf."},
                {"s": "السَّرِيرِ", "gloss": "the bed", "ans": {"kind": "ism"}, "why": "A thing with {ال}, jarr after {عَلَى}: ism."},
            ],
        },
        {
            "title": "Gender and definiteness",
            "fields": [
                {"key": "g", "label": "Gender", "options": GENDER},
                {"key": "d", "label": "Definite?", "options": DEF},
            ],
            "rows": [
                {"s": "السَّاعَةُ", "gloss": "the watch", "ans": {"g": "f", "d": "marifa"}, "why": "{ة} makes it feminine. {ال} makes it definite."},
                {"s": "مِفْتَاحٌ", "gloss": "a key", "ans": {"g": "m", "d": "nakira"}, "why": "No {ة}: masculine. Tanween: indefinite."},
                {"s": "زَهْرَةٌ", "gloss": "a flower", "ans": {"g": "f", "d": "nakira"}, "why": "{ة}: feminine. Tanween: indefinite."},
                {"s": "الْحَمَّامُ", "gloss": "the bathroom", "ans": {"g": "m", "d": "marifa"}, "why": "No {ة}: masculine. {ال}: definite."},
                {"s": "الْجَامِعَةُ", "gloss": "the university", "ans": {"g": "f", "d": "marifa"}, "why": "{ة}: feminine. {ال}: definite."},
                {"s": "قَمِيصٌ", "gloss": "a shirt", "ans": {"g": "m", "d": "nakira"}, "why": "No {ة}: masculine. Tanween: indefinite."},
            ],
        },
        {
            "title": "How do you read it?",
            "fields": [{"key": "pick", "label": "Reading", "options": []}],
            "rows": [
                {"s": "وَالشَّمْسُ", "gloss": "and the sun", "ans": {"pick": "b"},
                 "opts": {"pick": pick("wal-shamsu", "wash-shamsu", "wa-ash-shamsu")},
                 "why": "The alif of {ال} is not read after {وَ}, and {ش} is a sun letter."},
                {"s": "فِي الْبَيْتِ", "gloss": "in the house", "ans": {"pick": "a"},
                 "opts": {"pick": pick("fil-bayti", "fī al-bayti", "fil-baytu")},
                 "why": "The alif drops and {فِي} is read short before {ال}: fil-bayti."},
                {"s": "وَاسْمُ الْبِنْتِ", "gloss": "and the girl's name", "ans": {"pick": "c"},
                 "opts": {"pick": pick("wa-ismu l-binti", "wasmu al-binti", "wasmul-binti")},
                 "why": "Both alifs are hamzat al-waṣl. Neither is read in the middle of speech."},
                {"s": "مِنَ السُّوقِ", "gloss": "from the market", "ans": {"pick": "a"},
                 "opts": {"pick": pick("minas-sūqi", "minal-sūqi", "min as-sūqi")},
                 "why": "{س} is a sun letter, and the alif of {ال} is not read after {مِنَ}."},
                {"s": "اِبْنُ الْمُدَرِّسِ", "gloss": "the teacher's son (at the start)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("bnul-mudarrisi", "ibnul-mudarrisi", "ibnu al-mudarrisi")},
                 "why": "At the start of speech the first alif is read: ibnu. The alif of {ال} drops."},
            ],
        },
        {
            "title": "Which is right?",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "the teacher's car", "ans": {"pick": "c"},
                 "opts": {"pick": pick("السَّيَّارَةُ الْمُدَرِّسِ", "سَيَّارَةٌ الْمُدَرِّسِ", "سَيَّارَةُ الْمُدَرِّسِ")},
                 "why": "The first word of an iḍāfa takes no {ال} and no tanween."},
                {"s": "a new key", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مِفْتَاحٌ جَدِيدٌ", "مِفْتَاحُ جَدِيدٍ", "مِفْتَاحٌ جَدِيدٍ")},
                 "why": "The adjective copies the noun: tanween damma on both."},
                {"s": "The house is far.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْبَيْتُ الْبَعِيدُ", "الْبَيْتُ بَعِيدٌ", "بَيْتُ بَعِيدٍ")},
                 "why": "A sentence: definite Topic, indefinite Information. {الْبَيْتُ الْبَعِيدُ} is only a phrase."},
                {"s": "Hamid's son", "ans": {"pick": "a"},
                 "opts": {"pick": pick("اِبْنُ حَامِدٍ", "الاِبْنُ حَامِدٍ", "اِبْنٌ حَامِدٍ")},
                 "why": "Iḍāfa: {اِبْنُ} has no {ال} and no tanween, {حَامِدٍ} is the owner in jarr."},
                {"s": "the big house", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الْبَيْتُ كَبِيرٌ", "بَيْتُ الْكَبِيرِ", "الْبَيْتُ الْكَبِيرُ")},
                 "why": "A phrase with an adjective: both words have {ال} and damma."},
            ],
        },
        {
            "title": "Job and form of each word",
            "prompt": "اِبْنُ الْمُدَرِّسِ طَبِيبٌ وَابْنُ الْإِمَامِ تَاجِرٌ",
            "en": "The teacher's son is a doctor and the imam's son is a merchant.",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "form", "label": "Form", "options": FORMS},
            ],
            "rows": [
                {"s": "اِبْنُ", "gloss": "son (first one)", "ans": {"job": "topic", "form": "raf"},
                 "why": "We talk about the son. Topic, damma."},
                {"s": "الْمُدَرِّسِ", "ans": {"job": "owner", "form": "jarr"}, "why": "The son belongs to the teacher. Owner, kasra."},
                {"s": "طَبِيبٌ", "ans": {"job": "info", "form": "raf"}, "why": "What we say about the son. Information, rafʿ."},
                {"s": "الْإِمَامِ", "ans": {"job": "owner", "form": "jarr"}, "why": "The second son belongs to the imam. Owner, kasra."},
                {"s": "تَاجِرٌ", "ans": {"job": "info", "form": "raf"}, "why": "What we say about the imam's son. Information, rafʿ."},
            ],
        },
    ],
}
