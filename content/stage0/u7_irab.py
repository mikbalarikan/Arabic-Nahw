# Stage 0, Unit 7: What is iʿrāb? (bridge into Stage 1)

RAF = {"k": "raf", "label": "Rafʿ · رَفْعٌ", "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ", "color": "pink"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ", "color": "green"}

FIXFLEX = [
    {"k": "fixed", "label": "Fixed · مَبْنِيٌّ"},
    {"k": "flex", "label": "Flexible · مُعْرَبٌ"},
]

WHYJARR = [
    {"k": "prep", "label": "After a preposition", "color": "grey"},
    {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"},
]

TOPIC = {"k": "topic", "label": "Topic · مُبْتَدَأٌ", "color": "gold"}
INFO = {"k": "info", "label": "Information · خَبَرٌ", "color": "red"}
HARF = {"k": "harf", "label": "Ḥarf · حَرْفٌ", "color": "grey"}

JOBS = [
    TOPIC,
    INFO,
    {"k": "prep", "label": "After a preposition", "color": "green"},
    {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"},
]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abc", labels)]


UNIT = {
    "id": "s0-irab",
    "order": 7,
    "title": "What is iʿrāb?",
    "ar": "مَا الْإِعْرَابُ؟",
    "blurb": "Why the last vowel of a word changes, and how the job of a word decides it.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 0 · UNIT 7", "title": "The ending follows the job",
         "text": "Every word has a job in the sentence. The job gives it a colour, and the colour tells you its last vowel.",
         "wm": "الْإِعْرَابُ"},

        {"t": "h2", "text": "Fixed and flexible words"},
        {"t": "p", "text": "Some words never change their last letter. Others change it when their job changes. The change is called {إِعْرَابٌ}."},
        {"t": "cols", "items": [
            {"color": "grey", "title": "Fixed", "ar": "مَبْنِيٌّ",
             "text": "The ending never changes: {أَنَا}، {هُوَ}، {هَذَا}، {فِي}، {عَلَى}، {مَنْ}."},
            {"color": "blue", "title": "Flexible", "ar": "مُعْرَبٌ",
             "text": "The ending changes with the job: {الْبَيْتُ}، {الْبَيْتِ}."},
        ]},
        {"t": "tip", "text": "Most nouns are flexible. Pronouns like {هُوَ}, words like {هَذَا} and {مَنْ}, and all ḥarfs are fixed."},

        {"t": "h2", "text": "Same word, different endings"},
        {"t": "p", "text": "Madinah lesson 4 showed this. The word is the same. Only the last vowel moves."},
        {"t": "examples", "items": [
            {"ar": "الْبَيْتُ جَدِيدٌ.", "en": "The house is new.", "note": "{الْبَيْتُ} ends in damma. It is rafʿ."},
            {"ar": "فِي الْبَيْتِ", "en": "in the house", "note": "{الْبَيْتِ} ends in kasra. It is jarr, because of {فِي}."},
            {"ar": "فِي بَيْتٍ", "en": "in a house", "note": "With tanween: {بَيْتٌ} becomes {بَيْتٍ}."},
        ]},

        {"t": "h2", "text": "The four forms"},
        {"t": "cols", "items": [
            {"color": "red", "title": "Rafʿ", "ar": "رَفْعٌ", "text": "damma {ـُ}"},
            {"color": "pink", "title": "Naṣb", "ar": "نَصْبٌ", "text": "fatha {ـَ}"},
            {"color": "green", "title": "Jarr", "ar": "جَرٌّ", "text": "kasra {ـِ}"},
            {"color": "navy", "title": "Jazm", "ar": "جَزْمٌ", "text": "sukūn {ـْ}, verbs only, later"},
        ]},
        {"t": "table", "head": ["Form", "With ال", "With tanween"], "rows": [
            ["Rafʿ", "الْكِتَابُ", "كِتَابٌ"],
            ["Naṣb", "الْكِتَابَ", "كِتَابًا"],
            ["Jarr", "الْكِتَابِ", "كِتَابٍ"],
        ]},
        {"t": "rule", "color": "navy", "title": "Nouns never take jazm",
         "text": "A noun can be rafʿ, naṣb or jarr. Jazm is only for verbs. We meet it much later."},

        {"t": "h2", "text": "Role → form → sign"},
        {"t": "p", "text": "This is the chain from the board. Read it from left to right."},
        {"t": "table", "head": ["Role (job)", "Form", "Sign (last vowel)"], "rows": [
            ["Topic or Information", "Rafʿ", "{ـُ} or {ـٌ}"],
            ["After a preposition", "Jarr", "{ـِ} or {ـٍ}"],
            ["Owner in iḍāfa", "Jarr", "{ـِ} or {ـٍ}"],
        ]},
        {"t": "rule", "color": "gold", "title": "Ask about the job first",
         "text": "Do not guess the vowel. Find the job, the job gives the form, and the form gives the sign."},

        {"t": "h2", "text": "First sentences: Topic + Information"},
        {"t": "p", "text": "A nominal sentence starts with a noun. It has two parts: the Topic and the Information about it."},
        {"t": "cols", "items": [
            {"color": "gold", "title": "Topic", "ar": "مُبْتَدَأٌ", "text": "What we talk about. Rafʿ."},
            {"color": "red", "title": "Information", "ar": "خَبَرٌ", "text": "What we say about it. Rafʿ."},
        ]},
        {"t": "examples", "items": [
            {"ar": "مُحَمَّدٌ مُهَنْدِسٌ.", "en": "Muhammad is an engineer.", "note": "Topic {مُحَمَّدٌ}, Information {مُهَنْدِسٌ}. Both damma."},
            {"ar": "الطَّالِبُ فِي الْفَصْلِ.", "en": "The student is in the classroom.", "note": "Topic {الطَّالِبُ}. Information {فِي الْفَصْلِ}."},
            {"ar": "الْكِتَابُ عَلَى الْمَكْتَبِ.", "en": "The book is on the desk.", "note": "Topic {الْكِتَابُ}. Information {عَلَى الْمَكْتَبِ}."},
        ]},
        {"t": "tip", "text": "Arabic has no word for \"is\". {مُحَمَّدٌ مُهَنْدِسٌ} is already a full sentence."},
        {"t": "tip", "text": "When the Information is a place phrase like {فِي الْفَصْلِ}, the noun after the preposition is jarr. The preposition rule wins inside the phrase."},

        {"t": "h2", "text": "Two jarr rules for Stage 1"},
        {"t": "rule", "color": "green", "title": "1. After a preposition",
         "text": "After {فِي}، {عَلَى}، {مِنْ}، {إِلَى} the next noun is jarr: {فِي الْمَسْجِدِ}، {إِلَى السُّوقِ}."},
        {"t": "rule", "color": "purple", "title": "2. The owner in iḍāfa",
         "text": "The second word of an iḍāfa (the owner) is jarr: {بَيْتُ الْإِمَامِ}، {كِتَابُ مُحَمَّدٍ}."},
        {"t": "examples", "items": [
            {"ar": "هُوَ عَلَى مَكْتَبِ الْمُدَرِّسِ.", "en": "It is on the teacher's desk.",
             "note": "{مَكْتَبِ} is jarr after {عَلَى}. {الْمُدَرِّسِ} is jarr as the owner."},
        ]},

        {"t": "h2", "text": "Coming in Stage 1: three questions"},
        {"t": "table", "head": ["Ask", "If yes", "Ending"], "rows": [
            ["What is its job? Topic or Information?", "Rafʿ", "damma {ـُ}"],
            ["Is there a preposition or an owner relationship?", "Jarr", "kasra {ـِ}"],
            ["Is it an adjective, or after {وَ}?", "Copy", "same ending as the word it follows"],
        ]},
        {"t": "examples", "items": [
            {"ar": "فِي الْبَيْتِ الْجَدِيدِ", "en": "in the new house", "note": "The adjective {الْجَدِيدِ} copies the kasra of {الْبَيْتِ}."},
            {"ar": "الشَّمْسُ وَالْقَمَرُ فِي السَّمَاءِ.", "en": "The sun and the moon are in the sky.", "note": "{الْقَمَرُ} comes after {وَ}, so it copies the damma of {الشَّمْسُ}."},
        ]},

        {"t": "summary", "title": "In short", "items": [
            "Fixed words ({مَبْنِيٌّ}) never change. Flexible words ({مُعْرَبٌ}) change with their job.",
            "Nouns are rafʿ {ـُ}, naṣb {ـَ} or jarr {ـِ}. Never jazm.",
            "Role → form → sign: the job decides the ending.",
            "Topic ({مُبْتَدَأٌ}) and Information ({خَبَرٌ}) are rafʿ.",
            "After {فِي}، {عَلَى}، {مِنْ}، {إِلَى}, and as the owner in iḍāfa: jarr.",
        ]},
    ],

    "practice": [
        {
            "title": "Fixed or flexible?",
            "fields": [{"key": "type", "label": "Type", "options": FIXFLEX}],
            "rows": [
                {"s": "أَنَا", "gloss": "I", "ans": {"type": "fixed"}, "why": "A pronoun. {أَنَا} always ends the same way."},
                {"s": "الْكِتَابُ", "gloss": "the book", "ans": {"type": "flex"}, "why": "A noun. It can be {الْكِتَابُ} or {الْكِتَابِ}."},
                {"s": "فِي", "gloss": "in", "ans": {"type": "fixed"}, "why": "A ḥarf. Ḥarfs never change."},
                {"s": "هَذَا", "gloss": "this", "ans": {"type": "fixed"}, "why": "{هَذَا} keeps the same ending in every sentence."},
                {"s": "بَيْتٌ", "gloss": "a house", "ans": {"type": "flex"}, "why": "A noun. After {فِي} it becomes {بَيْتٍ}."},
                {"s": "مَنْ", "gloss": "who", "ans": {"type": "fixed"}, "why": "{مَنْ} is fixed. Even in {كِتَابُ مَنْ؟} it keeps its sukūn."},
            ],
        },
        {
            "title": "Which form does the ending show?",
            "fields": [{"key": "form", "label": "Form", "options": [RAF, NASB, JARR]}],
            "rows": [
                {"s": "الْبَيْتُ", "ans": {"form": "raf"}, "why": "Damma on the last letter: rafʿ."},
                {"s": "الْبَيْتِ", "ans": {"form": "jarr"}, "why": "Kasra on the last letter: jarr."},
                {"s": "كِتَابًا", "ans": {"form": "nasb"}, "why": "Tanween fatha {ـً}: naṣb."},
                {"s": "قَلَمٍ", "ans": {"form": "jarr"}, "why": "Tanween kasra {ـٍ}: jarr."},
                {"s": "طَالِبٌ", "ans": {"form": "raf"}, "why": "Tanween damma {ـٌ}: rafʿ."},
                {"s": "الْبَابَ", "ans": {"form": "nasb"}, "why": "Fatha on the last letter: naṣb."},
            ],
        },
        {
            "title": "Why is the last word jarr?",
            "fields": [{"key": "why", "label": "Reason", "options": WHYJARR}],
            "rows": [
                {"s": "فِي الْمَسْجِدِ", "gloss": "in the mosque", "ans": {"why": "prep"}, "why": "{الْمَسْجِدِ} comes after the preposition {فِي}."},
                {"s": "بَيْتُ الْإِمَامِ", "gloss": "the imam's house", "ans": {"why": "owner"}, "why": "The imam owns the house. {الْإِمَامِ} is the owner."},
                {"s": "عَلَى السَّرِيرِ", "gloss": "on the bed", "ans": {"why": "prep"}, "why": "{السَّرِيرِ} comes after the preposition {عَلَى}."},
                {"s": "كِتَابُ مُحَمَّدٍ", "gloss": "Muhammad's book", "ans": {"why": "owner"}, "why": "Muhammad owns the book. {مُحَمَّدٍ} is the owner."},
                {"s": "مِنَ الْبَيْتِ", "gloss": "from the house", "ans": {"why": "prep"}, "why": "{الْبَيْتِ} comes after the preposition {مِنْ}."},
                {"s": "حَقِيبَةُ الْمُدَرِّسِ", "gloss": "the teacher's bag", "ans": {"why": "owner"}, "why": "The bag belongs to the teacher. {الْمُدَرِّسِ} is the owner."},
            ],
        },
        {
            "title": "Mark the Topic and the Information",
            "prompt": "الْبَيْتُ جَدِيدٌ وَالْمَسْجِدُ قَرِيبٌ",
            "en": "The house is new and the mosque is near.",
            "fields": [{"key": "job", "label": "Job", "options": [TOPIC, INFO, HARF]}],
            "rows": [
                {"s": "الْبَيْتُ", "ans": {"job": "topic"}, "why": "We talk about the house. Topic, so damma."},
                {"s": "جَدِيدٌ", "ans": {"job": "info"}, "why": "What we say about the house. Information, so damma."},
                {"s": "وَ", "gloss": "and", "ans": {"job": "harf"}, "why": "{وَ} joins the two sentences. It is a ḥarf."},
                {"s": "الْمَسْجِدُ", "ans": {"job": "topic"}, "why": "The second sentence talks about the mosque. Topic."},
                {"s": "قَرِيبٌ", "ans": {"job": "info"}, "why": "What we say about the mosque. Information."},
            ],
        },
        {
            "title": "Choose the right ending after {فِي}",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "فِي + الْبَيْتُ", "gloss": "in the house", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الْبَيْتُ", "الْبَيْتَ", "الْبَيْتِ")}, "why": "After {فِي}: jarr, so kasra: {فِي الْبَيْتِ}."},
                {"s": "فِي + الْفَصْلُ", "gloss": "in the classroom", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الْفَصْلِ", "الْفَصْلُ", "الْفَصْلٍ")}, "why": "Kasra after {فِي}. A word with {ال} never takes tanween."},
                {"s": "فِي + بَيْتٌ", "gloss": "in a house", "ans": {"pick": "b"},
                 "opts": {"pick": pick("بَيْتِ", "بَيْتٍ", "بَيْتٌ")}, "why": "Indefinite and jarr: tanween kasra {بَيْتٍ}."},
                {"s": "فِي + الْمَطْبَخُ", "gloss": "in the kitchen", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الْمَطْبَخَ", "الْمَطْبَخُ", "الْمَطْبَخِ")}, "why": "After {فِي}: {الْمَطْبَخِ}."},
                {"s": "فِي + الْغُرْفَةُ", "gloss": "in the room", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الْغُرْفَةِ", "الْغُرْفَةُ", "الْغُرْفَةٍ")}, "why": "The kasra sits on the {ة}: {الْغُرْفَةِ}."},
                {"s": "فِي + مَسْجِدٌ", "gloss": "in a mosque", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَسْجِدٌ", "مَسْجِدٍ", "مَسْجِدِ")}, "why": "Indefinite and jarr: {مَسْجِدٍ}."},
            ],
        },
        {
            "title": "Job and form of the word in [ ]",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "form", "label": "Form", "options": [RAF, JARR]},
            ],
            "rows": [
                {"s": "مُحَمَّدٌ [مُهَنْدِسٌ]", "gloss": "Muhammad is an engineer.", "ans": {"job": "info", "form": "raf"},
                 "why": "{مُهَنْدِسٌ} tells us about Muhammad. Information, rafʿ."},
                {"s": "[الْقَلَمُ] مَكْسُورٌ", "gloss": "The pen is broken.", "ans": {"job": "topic", "form": "raf"},
                 "why": "We talk about the pen. Topic, rafʿ."},
                {"s": "الْكِتَابُ عَلَى [الْمَكْتَبِ]", "gloss": "The book is on the desk.", "ans": {"job": "prep", "form": "jarr"},
                 "why": "{الْمَكْتَبِ} comes after {عَلَى}. Jarr."},
                {"s": "بَيْتُ [الْإِمَامِ] قَرِيبٌ", "gloss": "The imam's house is near.", "ans": {"job": "owner", "form": "jarr"},
                 "why": "The imam owns the house. Owner, jarr."},
                {"s": "[الطَّالِبُ] فِي الْفَصْلِ", "gloss": "The student is in the classroom.", "ans": {"job": "topic", "form": "raf"},
                 "why": "We talk about the student. Topic, rafʿ."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Fixed or flexible?",
            "fields": [{"key": "type", "label": "Type", "options": FIXFLEX}],
            "rows": [
                {"s": "هُوَ", "gloss": "he, it", "ans": {"type": "fixed"}, "why": "A pronoun. {هُوَ} always ends in fatha."},
                {"s": "عَلَى", "gloss": "on", "ans": {"type": "fixed"}, "why": "A ḥarf. Ḥarfs never change."},
                {"s": "رَجُلٌ", "gloss": "a man", "ans": {"type": "flex"}, "why": "A noun. It can become {رَجُلٍ}."},
                {"s": "إِلَى", "gloss": "to", "ans": {"type": "fixed"}, "why": "A ḥarf. It is fixed."},
                {"s": "هِيَ", "gloss": "she, it", "ans": {"type": "fixed"}, "why": "A pronoun. {هِيَ} always ends in fatha."},
                {"s": "السَّيَّارَةُ", "gloss": "the car", "ans": {"type": "flex"}, "why": "A noun. After {فِي} it becomes {السَّيَّارَةِ}."},
            ],
        },
        {
            "title": "Which form does the ending show?",
            "fields": [{"key": "form", "label": "Form", "options": [RAF, NASB, JARR]}],
            "rows": [
                {"s": "مَسْجِدٍ", "ans": {"form": "jarr"}, "why": "Tanween kasra {ـٍ}: jarr."},
                {"s": "الْقَلَمَ", "ans": {"form": "nasb"}, "why": "Fatha on the last letter: naṣb."},
                {"s": "سَرِيرٌ", "ans": {"form": "raf"}, "why": "Tanween damma {ـٌ}: rafʿ."},
                {"s": "الْغُرْفَةِ", "ans": {"form": "jarr"}, "why": "Kasra on the {ة}: jarr."},
                {"s": "بَابًا", "ans": {"form": "nasb"}, "why": "Tanween fatha {ـً}: naṣb."},
                {"s": "السَّاعَةُ", "ans": {"form": "raf"}, "why": "Damma on the {ة}: rafʿ."},
            ],
        },
        {
            "title": "Why is the word in [ ] jarr?",
            "fields": [{"key": "why", "label": "Reason", "options": WHYJARR}],
            "rows": [
                {"s": "عَلَى [مَكْتَبِ] الْمُدَرِّسِ", "gloss": "on the teacher's desk", "ans": {"why": "prep"},
                 "why": "{مَكْتَبِ} comes right after {عَلَى}."},
                {"s": "عَلَى مَكْتَبِ [الْمُدَرِّسِ]", "gloss": "on the teacher's desk", "ans": {"why": "owner"},
                 "why": "The teacher owns the desk. {الْمُدَرِّسِ} is the owner."},
                {"s": "إِلَى [السُّوقِ]", "gloss": "to the market", "ans": {"why": "prep"},
                 "why": "{السُّوقِ} comes after {إِلَى}."},
                {"s": "مِفْتَاحُ [السَّيَّارَةِ]", "gloss": "the car key", "ans": {"why": "owner"},
                 "why": "The key belongs to the car. {السَّيَّارَةِ} is the owner."},
                {"s": "مِنْ [غُرْفَةِ] الْمُدِيرِ", "gloss": "from the principal's room", "ans": {"why": "prep"},
                 "why": "{غُرْفَةِ} comes right after {مِنْ}."},
                {"s": "اِسْمُ [الطَّالِبِ]", "gloss": "the student's name", "ans": {"why": "owner"},
                 "why": "The name belongs to the student. {الطَّالِبِ} is the owner."},
            ],
        },
        {
            "title": "Find the Topic and the Information",
            "fields": [
                {"key": "topic", "label": "Topic · مُبْتَدَأٌ", "options": []},
                {"key": "info", "label": "Information · خَبَرٌ", "options": []},
            ],
            "rows": [
                {"s": "خَالِدٌ طَبِيبٌ", "gloss": "Khalid is a doctor.", "ans": {"topic": "a", "info": "b"},
                 "opts": {"topic": pick("خَالِدٌ", "طَبِيبٌ"), "info": pick("خَالِدٌ", "طَبِيبٌ")},
                 "why": "We talk about {خَالِدٌ}. We say he is {طَبِيبٌ}."},
                {"s": "السَّيَّارَةُ فِي الشَّارِعِ", "gloss": "The car is in the street.", "ans": {"topic": "a", "info": "c"},
                 "opts": {"topic": pick("السَّيَّارَةُ", "الشَّارِعِ", "فِي الشَّارِعِ"), "info": pick("السَّيَّارَةُ", "الشَّارِعِ", "فِي الشَّارِعِ")},
                 "why": "Topic {السَّيَّارَةُ}. The whole place phrase {فِي الشَّارِعِ} is the Information."},
                {"s": "بَيْتُ الْمُدَرِّسِ بَعِيدٌ", "gloss": "The teacher's house is far.", "ans": {"topic": "b", "info": "c"},
                 "opts": {"topic": pick("الْمُدَرِّسِ", "بَيْتُ الْمُدَرِّسِ", "بَعِيدٌ"), "info": pick("الْمُدَرِّسِ", "بَيْتُ الْمُدَرِّسِ", "بَعِيدٌ")},
                 "why": "We talk about the teacher's house, {بَيْتُ الْمُدَرِّسِ}. {بَعِيدٌ} is the Information."},
                {"s": "عَمُّ الطَّالِبِ غَنِيٌّ", "gloss": "The student's uncle is rich.", "ans": {"topic": "a", "info": "c"},
                 "opts": {"topic": pick("عَمُّ الطَّالِبِ", "الطَّالِبِ", "غَنِيٌّ"), "info": pick("عَمُّ الطَّالِبِ", "الطَّالِبِ", "غَنِيٌّ")},
                 "why": "We talk about the uncle, {عَمُّ الطَّالِبِ}. He is {غَنِيٌّ}."},
                {"s": "الْقَلَمُ عَلَى الْكِتَابِ", "gloss": "The pen is on the book.", "ans": {"topic": "a", "info": "b"},
                 "opts": {"topic": pick("الْقَلَمُ", "عَلَى الْكِتَابِ", "الْكِتَابِ"), "info": pick("الْقَلَمُ", "عَلَى الْكِتَابِ", "الْكِتَابِ")},
                 "why": "Topic {الْقَلَمُ}. Information {عَلَى الْكِتَابِ}."},
            ],
        },
        {
            "title": "Choose the right ending after the preposition",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "فِي + غُرْفَةٌ", "gloss": "in a room", "ans": {"pick": "b"},
                 "opts": {"pick": pick("غُرْفَةٌ", "غُرْفَةٍ", "غُرْفَةِ")}, "why": "Indefinite and jarr: {غُرْفَةٍ}."},
                {"s": "عَلَى + الْكُرْسِيُّ", "gloss": "on the chair", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الْكُرْسِيُّ", "الْكُرْسِيٍّ", "الْكُرْسِيِّ")}, "why": "After {عَلَى}: kasra under the doubled {ي}: {الْكُرْسِيِّ}."},
                {"s": "إِلَى + الْمَدْرَسَةُ", "gloss": "to the school", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الْمَدْرَسَةِ", "الْمَدْرَسَةَ", "الْمَدْرَسَةُ")}, "why": "After {إِلَى}: {الْمَدْرَسَةِ}."},
                {"s": "مِنْ + الْجَامِعَةُ", "gloss": "from the university", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مِنَ الْجَامِعَةُ", "مِنَ الْجَامِعَةِ", "مِنَ الْجَامِعَةٍ")}, "why": "After {مِنْ}: jarr, no tanween with {ال}. ({مِنْ} becomes {مِنَ} before {ال}.)"},
                {"s": "فِي + السَّمَاءُ", "gloss": "in the sky", "ans": {"pick": "c"},
                 "opts": {"pick": pick("السَّمَاءُ", "السَّمَاءَ", "السَّمَاءِ")}, "why": "After {فِي}: {السَّمَاءِ}."},
                {"s": "عَلَى + مَكْتَبٌ", "gloss": "on a desk", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَكْتَبٍ", "مَكْتَبِ", "مَكْتَبٌ")}, "why": "Indefinite and jarr: {مَكْتَبٍ}."},
            ],
        },
        {
            "title": "Job and form of each word",
            "prompt": "بَابُ الْمَسْجِدِ مَفْتُوحٌ وَبَابُ الْمَدْرَسَةِ مُغْلَقٌ",
            "en": "The mosque door is open and the school door is closed.",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "form", "label": "Form", "options": [RAF, JARR]},
            ],
            "rows": [
                {"s": "بَابُ", "gloss": "door (first one)", "ans": {"job": "topic", "form": "raf"},
                 "why": "We talk about the door. Topic, damma. It has no {ال} and no tanween because it is the first word of an iḍāfa."},
                {"s": "الْمَسْجِدِ", "ans": {"job": "owner", "form": "jarr"}, "why": "The door belongs to the mosque. Owner, kasra."},
                {"s": "مَفْتُوحٌ", "ans": {"job": "info", "form": "raf"}, "why": "What we say about the door. Information, rafʿ."},
                {"s": "الْمَدْرَسَةِ", "ans": {"job": "owner", "form": "jarr"}, "why": "The door belongs to the school. Owner, kasra."},
                {"s": "مُغْلَقٌ", "ans": {"job": "info", "form": "raf"}, "why": "What we say about the second door. Information, rafʿ."},
            ],
        },
    ],
}
