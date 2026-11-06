# Stage 3, Unit 7: Particles (al-ḥurūf)


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abc", labels)]


GROUPS = [
    {"k": "jarr", "label": "Jarr · حَرْفُ جَرٍّ", "color": "green"},
    {"k": "atf", "label": "Joining · حَرْفُ عَطْفٍ", "color": "blue"},
    {"k": "ans", "label": "Answer · حَرْفُ جَوَابٍ", "color": "olive"},
    {"k": "q", "label": "Question · حَرْفُ اسْتِفْهَامٍ", "color": "gold"},
    {"k": "voc", "label": "Calling · حَرْفُ نِدَاءٍ", "color": "grey"},
]

KINDS = [
    {"k": "ism", "label": "Ism · اِسْمٌ", "color": "blue"},
    {"k": "fil", "label": "Fiʿl · فِعْلٌ", "color": "navy"},
    {"k": "harf", "label": "Ḥarf · حَرْفٌ", "color": "grey"},
]

ISMHARF = [
    {"k": "ism", "label": "Ism · اِسْمٌ", "color": "blue"},
    {"k": "harf", "label": "Ḥarf · حَرْفٌ", "color": "grey"},
]


UNIT = {
    "id": "s3-particles",
    "order": 7,
    "title": "Particles",
    "ar": "الحُرُوفُ",
    "blurb": "The small words that link, ask, answer and call. Every ḥarf is fixed and has no place of its own.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 3 · UNIT 7", "title": "Small words, big work",
         "text": "A ḥarf never changes, and it has no iʿrāb place. Its job is to work on the words around it.",
         "wm": "الحُرُوفُ"},

        {"t": "h2", "text": "Every ḥarf is fixed, with no place"},
        {"t": "p", "text": "Pronouns, pointing words and question isms are fixed, but they still have a place: rafʿ, naṣb or jarr. A ḥarf is different. It is fixed and it has no place at all."},
        {"t": "rule", "color": "grey", "title": "How we say it",
         "text": "For a ḥarf we say: {حَرْفٌ مَبْنِيٌّ لَا مَحَلَّ لَهُ مِنَ الإِعْرَابِ}. A fixed ḥarf with no place in iʿrāb."},
        {"t": "cols", "items": [
            {"color": "green", "title": "Jarr", "ar": "حُرُوفُ الجَرِّ", "text": "{مِنْ}، {إِلَى}، {فِي} …"},
            {"color": "blue", "title": "Joining", "ar": "حُرُوفُ العَطْفِ", "text": "{وَ}، {فَ}، {ثُمَّ} …"},
            {"color": "olive", "title": "Answer", "ar": "حُرُوفُ الجَوَابِ", "text": "{نَعَمْ}، {لَا}، {بَلَى}"},
            {"color": "gold", "title": "Question", "ar": "الِاسْتِفْهَامُ", "text": "{هَلْ}، {أَ}"},
            {"color": "grey", "title": "Calling", "ar": "حَرْفُ النِّدَاءِ", "text": "{يَا}"},
        ]},

        {"t": "h2", "text": "The jarr ḥarfs (حُرُوفُ الجَرِّ)"},
        {"t": "p", "text": "You know four of them from Stage 1. Here are nine. The noun after each one is jarr."},
        {"t": "table", "head": ["Ḥarf", "Meaning", "Example"], "rows": [
            ["مِنْ", "from", "خَرَجَ مِنَ البَيْتِ."],
            ["إِلَى", "to", "ذَهَبَ إِلَى المَسْجِدِ."],
            ["عَنْ", "about, away from", "الدَّرْسُ عَنِ القَمَرِ."],
            ["عَلَى", "on", "الكِتَابُ عَلَى المَكْتَبِ."],
            ["فِي", "in", "الطَّالِبُ فِي الفَصْلِ."],
            ["بِـ", "with, by", "كَتَبْتُ بِالقَلَمِ."],
            ["لِـ", "for, belongs to", "الكِتَابُ لِمُحَمَّدٍ."],
            ["كَـ", "like", "البِنْتُ كَالقَمَرِ."],
            ["حَتَّى", "until", "جَلَسْتُ فِي المَسْجِدِ حَتَّى الظُّهْرِ."],
        ]},
        {"t": "rule", "color": "green", "title": "Two small changes before ال",
         "text": "{مِنْ} becomes {مِنَ}: {مِنَ البَيْتِ}. {عَنْ} becomes {عَنِ}: {عَنِ القَمَرِ}."},
        {"t": "tip", "text": "{بِـ}، {لِـ}، {كَـ} are written joined to the next word. With {ال}, {لِـ} drops the alif: {لِلمُدَرِّسِ}."},

        {"t": "h2", "text": "The joining ḥarfs (حُرُوفُ العَطْفِ)"},
        {"t": "p", "text": "They join a word to the word before it. The rule from Stage 1 stays: the word after them copies the ending of the word before."},
        {"t": "table", "head": ["Ḥarf", "Meaning", "Example"], "rows": [
            ["وَ", "and", "الكِتَابُ وَالقَلَمُ عَلَى المَكْتَبِ."],
            ["فَ", "and right after", "دَخَلَ مُحَمَّدٌ فَخَالِدٌ."],
            ["ثُمَّ", "then, after a while", "خَرَجَ حَامِدٌ ثُمَّ يَاسِرٌ."],
            ["أَوْ", "or", "اِشْرَبِ المَاءَ أَوِ اللَّبَنَ."],
            ["بَلْ", "no, rather (a correction)", "هَذَا كِتَابٌ بَلْ دَفْتَرٌ."],
        ]},
        {"t": "examples", "items": [
            {"ar": "دَخَلَ مُحَمَّدٌ فَخَالِدٌ.", "en": "Muhammad came in, and Khalid right after him.",
             "note": "{خَالِدٌ} copies the damma of {مُحَمَّدٌ}."},
            {"ar": "اِشْرَبِ المَاءَ أَوِ اللَّبَنَ.", "en": "Drink the water or the milk.",
             "note": "{اللَّبَنَ} copies the fatha of {المَاءَ}. {أَوْ} takes a helping kasra before {ال}."},
        ]},

        {"t": "h2", "text": "The answer ḥarfs (حُرُوفُ الجَوَابِ)"},
        {"t": "table", "head": ["Ḥarf", "Meaning", "Example"], "rows": [
            ["نَعَمْ", "yes", "أَهَذَا بَيْتٌ؟ نَعَمْ، هَذَا بَيْتٌ."],
            ["لَا", "no", "أَهَذَا بَيْتٌ؟ لَا، هَذَا مَسْجِدٌ."],
            ["بَلَى", "yes (to a \"not\" question)", "أَمَا ذَهَبْتَ إِلَى المَسْجِدِ؟ بَلَى، ذَهَبْتُ."],
        ]},
        {"t": "rule", "color": "olive", "title": "When to use بَلَى",
         "text": "Use {بَلَى} when the question has \"not\" in it and your answer is yes. \"Didn't you go?\" {بَلَى}: \"Yes, I did.\""},
        {"t": "tip", "text": "In {أَمَا ذَهَبْتَ؟} the {مَا} is the \"did not\" ḥarf from unit 6: {مَا ذَهَبْتَ} \"you did not go\". Add the question ḥarf {أَ}: {أَ} + {مَا} + {ذَهَبْتَ} = \"Didn't you go?\""},

        {"t": "h2", "text": "The question ḥarfs (هَلْ and أَ)"},
        {"t": "p", "text": "You met them in unit 5. They make a yes/no question. They are ḥarfs, so they have no place. The question words {مَنْ}، {مَا}، {أَيْنَ} are isms and do have a place."},
        {"t": "table", "head": ["Ḥarf", "Meaning", "Example"], "rows": [
            ["هَلْ", "yes/no question", "هَلْ ذَهَبَ مُحَمَّدٌ إِلَى السُّوقِ؟"],
            ["أَ", "yes/no question (joined)", "أَهَذَا بَيْتٌ؟"],
        ]},

        {"t": "h2", "text": "The calling ḥarf يَا"},
        {"t": "p", "text": "Use {يَا} to call someone. After {يَا} a name, or a single noun for the person you call, takes one damma. It never takes tanween. This damma is fixed. The called word is in the place of naṣb ({فِي مَحَلِّ نَصْبٍ})."},
        {"t": "table", "head": ["Noun", "Calling", "Meaning"], "rows": [
            ["مُحَمَّدٌ", "يَا مُحَمَّدُ", "O Muhammad"],
            ["عَلِيٌّ", "يَا عَلِيُّ", "O Ali"],
            ["آمِنَةُ", "يَا آمِنَةُ", "O Aminah"],
            ["وَلَدٌ", "يَا وَلَدُ", "O boy"],
            ["أُسْتَاذٌ", "يَا أُسْتَاذُ", "O teacher"],
        ]},
        {"t": "tip", "text": "This is the same as Madinah lesson 5: {يَا بِلَالُ}، {يَا شَيْخُ}."},

        {"t": "h2", "text": "Ḥarf or ism? Look-alikes"},
        {"t": "p", "text": "Some ḥarfs look like isms, and some short question words are isms. Read the vowels carefully."},
        {"t": "table", "head": ["Ḥarf", "Ism"], "rows": [
            ["{مِنْ} from", "{مَنْ} who"],
            ["{عَلَى} on", "{عَلِيٌّ} Ali (a name)"],
            ["{هَلْ} yes/no question", "{أَيْنَ} where"],
            ["{كَـ} like", "{كَمْ} how many"],
        ]},

        {"t": "summary", "title": "In short", "items": [
            "Every ḥarf is fixed and has no place: {لَا مَحَلَّ لَهُ مِنَ الإِعْرَابِ}.",
            "Jarr: {مِنْ} {إِلَى} {عَنْ} {عَلَى} {فِي} {بِـ} {لِـ} {كَـ} {حَتَّى}. The next noun is jarr.",
            "Joining: {وَ} {فَ} {ثُمَّ} {أَوْ} {بَلْ}. The next word copies the one before.",
            "Answer: {نَعَمْ} {لَا} {بَلَى}. {بَلَى} answers a \"not\" question.",
            "Question: {هَلْ} {أَ}. Calling: {يَا}, then one damma: {يَا مُحَمَّدُ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Which group?",
            "fields": [{"key": "group", "label": "Group", "options": GROUPS}],
            "rows": [
                {"s": "إِلَى", "gloss": "to", "ans": {"group": "jarr"}, "why": "{إِلَى} makes the next noun jarr."},
                {"s": "ثُمَّ", "gloss": "then", "ans": {"group": "atf"}, "why": "{ثُمَّ} joins two words, one after a while."},
                {"s": "بَلَى", "gloss": "yes (to a \"not\" question)", "ans": {"group": "ans"}, "why": "{بَلَى} is an answer."},
                {"s": "هَلْ", "ans": {"group": "q"}, "why": "{هَلْ} starts a yes/no question."},
                {"s": "يَا", "ans": {"group": "voc"}, "why": "{يَا} calls someone."},
                {"s": "كَـ", "gloss": "like", "ans": {"group": "jarr"}, "why": "{كَـ} makes the next noun jarr: {كَالقَمَرِ}."},
            ],
        },
        {
            "title": "Choose the right ḥarf",
            "fields": [{"key": "pick", "label": "Ḥarf", "options": []}],
            "rows": [
                {"s": "ذَهَبَ الطَّالِبُ … المَدْرَسَةِ.", "gloss": "The student went to the school.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("إِلَى", "عَلَى", "أَوْ")}, "why": "\"Went to\": {إِلَى المَدْرَسَةِ}."},
                {"s": "الكِتَابُ … المَكْتَبِ.", "gloss": "The book is on the desk.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("إِلَى", "عَلَى", "ثُمَّ")}, "why": "\"On\": {عَلَى المَكْتَبِ}."},
                {"s": "كَتَبْتُ … القَلَمِ.", "gloss": "I wrote with the pen.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("إِلَى", "ثُمَّ", "بِـ")}, "why": "\"With\": {بِالقَلَمِ}."},
                {"s": "… ذَهَبَ مُحَمَّدٌ إِلَى السُّوقِ؟", "gloss": "Did Muhammad go to the market?", "ans": {"pick": "a"},
                 "opts": {"pick": pick("هَلْ", "نَعَمْ", "بَلْ")}, "why": "A yes/no question starts with {هَلْ}."},
                {"s": "… خَالِدُ، اُدْخُلْ.", "gloss": "Khalid, come in.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("هَلْ", "فِي", "يَا")}, "why": "Calling Khalid: {يَا خَالِدُ}. Note the one damma."},
                {"s": "أَهَذَا قَلَمٌ؟ …، هَذَا قَلَمٌ.", "gloss": "Is this a pen? Yes, this is a pen.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَا", "نَعَمْ", "بَلَى")}, "why": "A normal question with yes: {نَعَمْ}. {بَلَى} is only for a \"not\" question."},
            ],
        },
        {
            "title": "The noun after the jarr ḥarf",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "مِنْ + البَيْتُ", "gloss": "from the house", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مِنَ البَيْتِ", "مِنَ البَيْتُ", "مِنْ البَيْتِ")}, "why": "Jarr: {البَيْتِ}. And {مِنْ} becomes {مِنَ} before {ال}."},
                {"s": "إِلَى + مَسْجِدٌ", "gloss": "to a mosque", "ans": {"pick": "c"},
                 "opts": {"pick": pick("إِلَى مَسْجِدٌ", "إِلَى مَسْجِدِ", "إِلَى مَسْجِدٍ")}, "why": "Indefinite and jarr: {مَسْجِدٍ}."},
                {"s": "بِـ + القَلَمُ", "gloss": "with the pen", "ans": {"pick": "b"},
                 "opts": {"pick": pick("بِالقَلَمُ", "بِالقَلَمِ", "بِالقَلَمَ")}, "why": "After {بِـ}: kasra, {بِالقَلَمِ}."},
                {"s": "عَنْ + الدَّرْسُ", "gloss": "about the lesson", "ans": {"pick": "a"},
                 "opts": {"pick": pick("عَنِ الدَّرْسِ", "عَنِ الدَّرْسُ", "عَنْ الدَّرْسِ")}, "why": "Jarr: {الدَّرْسِ}. And {عَنْ} becomes {عَنِ} before {ال}."},
                {"s": "كَـ + القَمَرُ", "gloss": "like the moon", "ans": {"pick": "c"},
                 "opts": {"pick": pick("كَالقَمَرُ", "كَالقَمَرٍ", "كَالقَمَرِ")}, "why": "After {كَـ}: kasra, no tanween with {ال}: {كَالقَمَرِ}."},
                {"s": "حَتَّى + الظُّهْرُ", "gloss": "until noon", "ans": {"pick": "b"},
                 "opts": {"pick": pick("حَتَّى الظُّهْرُ", "حَتَّى الظُّهْرِ", "حَتَّى الظُّهْرَ")}, "why": "After {حَتَّى}: jarr, {الظُّهْرِ}."},
            ],
        },
        {
            "title": "Ḥarf or ism?",
            "fields": [{"key": "kind", "label": "Kind", "options": ISMHARF}],
            "rows": [
                {"s": "مِنْ", "gloss": "from", "ans": {"kind": "harf"}, "why": "{مِنْ} with kasra is the jarr ḥarf \"from\"."},
                {"s": "مَنْ", "gloss": "who", "ans": {"kind": "ism"}, "why": "{مَنْ} with fatha is a question ism \"who\". It has a place."},
                {"s": "عَلَى", "gloss": "on", "ans": {"kind": "harf"}, "why": "{عَلَى} is a jarr ḥarf."},
                {"s": "عَلِيٌّ", "gloss": "Ali", "ans": {"kind": "ism"}, "why": "{عَلِيٌّ} is a name. It even has tanween."},
                {"s": "هَلْ", "ans": {"kind": "harf"}, "why": "{هَلْ} is a question ḥarf, with no place."},
                {"s": "أَيْنَ", "gloss": "where", "ans": {"kind": "ism"}, "why": "{أَيْنَ} is a question ism. It is fixed but has a place."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "عَنْ", "ans": {"pick": "b"}, "opts": {"pick": pick("to", "about", "on")}, "why": "{عَنْ}: about, away from."},
                {"s": "حَتَّى", "ans": {"pick": "a"}, "opts": {"pick": pick("until", "from", "then")}, "why": "{حَتَّى}: until."},
                {"s": "أَوْ", "ans": {"pick": "c"}, "opts": {"pick": pick("and", "no", "or")}, "why": "{أَوْ}: or."},
                {"s": "ثُمَّ", "ans": {"pick": "a"}, "opts": {"pick": pick("then, after a while", "here", "like")}, "why": "{ثُمَّ}: then, after some time."},
                {"s": "كَـ", "ans": {"pick": "b"}, "opts": {"pick": pick("for", "like", "how many")}, "why": "{كَـ}: like. \"How many\" is the ism {كَمْ}."},
            ],
        },
        {
            "title": "Ism, fiʿl or ḥarf?",
            "prompt": "خَرَجَ مُحَمَّدٌ مِنَ البَيْتِ ثُمَّ ذَهَبَ إِلَى المَسْجِدِ.",
            "en": "Muhammad went out of the house, then he went to the mosque.",
            "fields": [{"key": "kind", "label": "Kind", "options": KINDS}],
            "rows": [
                {"s": "خَرَجَ", "ans": {"kind": "fil"}, "why": "A past verb: he went out."},
                {"s": "مِنَ", "ans": {"kind": "harf"}, "why": "A jarr ḥarf. Its sukūn became fatha before {ال}."},
                {"s": "البَيْتِ", "ans": {"kind": "ism"}, "why": "A noun, jarr after {مِنَ}."},
                {"s": "ثُمَّ", "ans": {"kind": "harf"}, "why": "A joining ḥarf: then."},
                {"s": "إِلَى", "ans": {"kind": "harf"}, "why": "A jarr ḥarf: to."},
                {"s": "المَسْجِدِ", "ans": {"kind": "ism"}, "why": "A noun, jarr after {إِلَى}."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Which group?",
            "fields": [{"key": "group", "label": "Group", "options": GROUPS}],
            "rows": [
                {"s": "عَنْ", "gloss": "about", "ans": {"group": "jarr"}, "why": "{عَنْ} makes the next noun jarr."},
                {"s": "فَ", "gloss": "and right after", "ans": {"group": "atf"}, "why": "{فَ} joins two words with no gap in time."},
                {"s": "لَا", "gloss": "no", "ans": {"group": "ans"}, "why": "{لَا} is an answer."},
                {"s": "أَ", "ans": {"group": "q"}, "why": "{أَ} at the start makes a yes/no question: {أَهَذَا بَيْتٌ؟}."},
                {"s": "أَوْ", "gloss": "or", "ans": {"group": "atf"}, "why": "{أَوْ} joins two words: this or that."},
                {"s": "لِـ", "gloss": "for", "ans": {"group": "jarr"}, "why": "{لِـ} makes the next noun jarr: {لِمُحَمَّدٍ}."},
            ],
        },
        {
            "title": "Choose the right ḥarf",
            "fields": [{"key": "pick", "label": "Ḥarf", "options": []}],
            "rows": [
                {"s": "أَمَا جَلَسْتَ هُنَا؟ …، جَلَسْتُ.", "gloss": "Didn't you sit here? Yes, I did.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بَلَى", "نَعَمْ", "لَا")}, "why": "The question has \"not\" and the answer is yes: {بَلَى}."},
                {"s": "جَلَسْنَا فِي الفَصْلِ … الظُّهْرِ.", "gloss": "We sat in the classroom until noon.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("ثُمَّ", "يَا", "حَتَّى")}, "why": "\"Until\": {حَتَّى}. It makes {الظُّهْرِ} jarr."},
                {"s": "اِفْتَحِ البَابَ … النَّافِذَةَ.", "gloss": "Open the door or the window.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("عَلَى", "أَوِ", "إِلَى")}, "why": "{النَّافِذَةَ} has fatha, copying {البَابَ}. So a joining ḥarf: {أَوِ}."},
                {"s": "هَذَا قَلَمٌ … مِفْتَاحٌ.", "gloss": "This is a pen, no, rather a key.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بَلْ", "مِنْ", "فِي")}, "why": "A correction: {بَلْ}. {مِفْتَاحٌ} copies the damma of {قَلَمٌ}."},
                {"s": "دَخَلَ المُدَرِّسُ … الطَّالِبُ.", "gloss": "The teacher came in, and the student right after.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("عَلَى", "بِـ", "فَـ")}, "why": "{الطَّالِبُ} has damma, copying {المُدَرِّسُ}. So {فَ}: {فَالطَّالِبُ}."},
                {"s": "… أُسْتَاذُ، أَيْنَ الكِتَابُ؟", "gloss": "Teacher, where is the book?", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هَلْ", "يَا", "فِي")}, "why": "Calling the teacher: {يَا أُسْتَاذُ}, with one damma."},
            ],
        },
        {
            "title": "The noun after the jarr ḥarf",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "فِي + غُرْفَةُ المُدِيرِ", "gloss": "in the principal's room", "ans": {"pick": "c"},
                 "opts": {"pick": pick("فِي غُرْفَةُ المُدِيرِ", "فِي غُرْفَةٍ المُدِيرِ", "فِي غُرْفَةِ المُدِيرِ")}, "why": "{غُرْفَةِ} is jarr after {فِي}, with no tanween because it is owned."},
                {"s": "لِـ + مُحَمَّدٌ", "gloss": "for Muhammad", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لِمُحَمَّدٍ", "لِمُحَمَّدٌ", "لِمُحَمَّدَ")}, "why": "Jarr with tanween: {لِمُحَمَّدٍ}."},
                {"s": "عَلَى + الكُرْسِيُّ", "gloss": "on the chair", "ans": {"pick": "b"},
                 "opts": {"pick": pick("عَلَى الكُرْسِيُّ", "عَلَى الكُرْسِيِّ", "عَلَى الكُرْسِيٍّ")}, "why": "Kasra under the doubled {ي}, no tanween with {ال}."},
                {"s": "مِنْ + المَدْرَسَةُ", "gloss": "from the school", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مِنْ المَدْرَسَةِ", "مِنَ المَدْرَسَةَ", "مِنَ المَدْرَسَةِ")}, "why": "{مِنَ} before {ال}, and jarr: {المَدْرَسَةِ}."},
                {"s": "بِـ + مِفْتَاحٌ", "gloss": "with a key", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بِمِفْتَاحٍ", "بِمِفْتَاحِ", "بِمِفْتَاحٌ")}, "why": "Indefinite and jarr: {بِمِفْتَاحٍ}."},
                {"s": "عَنْ + الرَّجُلُ", "gloss": "about the man", "ans": {"pick": "b"},
                 "opts": {"pick": pick("عَنْ الرَّجُلِ", "عَنِ الرَّجُلِ", "عَنِ الرَّجُلُ")}, "why": "{عَنِ} before {ال}, and jarr: {الرَّجُلِ}."},
            ],
        },
        {
            "title": "Ḥarf or ism? Look at the word in [ ]",
            "fields": [{"key": "kind", "label": "Kind", "options": ISMHARF}],
            "rows": [
                {"s": "[مَا] هَذَا؟", "gloss": "What is this?", "ans": {"kind": "ism"}, "why": "{مَا} \"what\" is a question ism. It has a place."},
                {"s": "[لَا]، هَذَا مَسْجِدٌ.", "gloss": "No, this is a mosque.", "ans": {"kind": "harf"}, "why": "{لَا} is an answer ḥarf."},
                {"s": "[كَمْ] طَالِبًا فِي الفَصْلِ؟", "gloss": "How many students are in the classroom?", "ans": {"kind": "ism"}, "why": "{كَمْ} \"how many\" is a question ism."},
                {"s": "البِنْتُ [كَـ]القَمَرِ.", "gloss": "The girl is like the moon.", "ans": {"kind": "harf"}, "why": "{كَـ} \"like\" is a jarr ḥarf."},
                {"s": "[أَ]هَذَا بَيْتٌ؟", "gloss": "Is this a house?", "ans": {"kind": "harf"}, "why": "{أَ} is a question ḥarf, with no place."},
                {"s": "[أَنَا] طَالِبٌ.", "gloss": "I am a student.", "ans": {"kind": "ism"}, "why": "{أَنَا} is a pronoun, an ism, in the place of rafʿ."},
            ],
        },
        {
            "title": "What does the sentence mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "خَرَجَ حَامِدٌ ثُمَّ خَالِدٌ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("Hamid or Khalid went out.", "Hamid went out, then later Khalid.", "Hamid went out, no, Khalid did.")},
                 "why": "{ثُمَّ}: then, after a while."},
                {"s": "خَرَجَ حَامِدٌ بَلْ خَالِدٌ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("Hamid went out, then later Khalid.", "Hamid and Khalid went out.", "Hamid went out, no, Khalid did.")},
                 "why": "{بَلْ} corrects the first name."},
                {"s": "خَرَجَ حَامِدٌ فَخَالِدٌ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("Hamid went out, and Khalid right after.", "Hamid went out with Khalid.", "Hamid went out to Khalid.")},
                 "why": "{فَ}: right after, with no gap."},
                {"s": "الكِتَابُ لِلمُدَرِّسِ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("The book is about the teacher.", "The book belongs to the teacher.", "The book is like the teacher.")},
                 "why": "{لِـ}: for, belongs to. \"About\" would be {عَنِ}."},
                {"s": "أَمَا خَرَجَ حَامِدٌ؟ بَلَى.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("Didn't Hamid go out? Yes, he did.", "Didn't Hamid go out? No, he didn't.", "Did Hamid go out? No.")},
                 "why": "{بَلَى} says yes to a \"not\" question."},
            ],
        },
        {
            "title": "Which group? (or not a ḥarf)",
            "prompt": "يَا خَالِدُ، هَلْ ذَهَبْتَ إِلَى السُّوقِ أَوْ إِلَى المَسْجِدِ؟",
            "en": "Khalid, did you go to the market or to the mosque?",
            "fields": [{"key": "group", "label": "Group", "options": GROUPS + [{"k": "no", "label": "Not a ḥarf", "color": "blue"}]}],
            "rows": [
                {"s": "يَا", "ans": {"group": "voc"}, "why": "{يَا} calls Khalid."},
                {"s": "خَالِدُ", "ans": {"group": "no"}, "why": "A name, an ism. After {يَا} it takes one damma."},
                {"s": "هَلْ", "ans": {"group": "q"}, "why": "{هَلْ} makes the yes/no question."},
                {"s": "ذَهَبْتَ", "ans": {"group": "no"}, "why": "A past verb: you went."},
                {"s": "إِلَى", "ans": {"group": "jarr"}, "why": "{إِلَى} makes {السُّوقِ} jarr."},
                {"s": "أَوْ", "ans": {"group": "atf"}, "why": "{أَوْ} joins the two places: or."},
            ],
        },
    ],
}
