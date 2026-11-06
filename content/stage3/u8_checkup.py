# Stage 3, Unit 8: Stage 3 check-up (mixed quiz over units 1-7)


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abc", labels)]


JOBS = [
    {"k": "topic", "label": "Topic · مُبْتَدَأٌ", "color": "gold"},
    {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"},
    {"k": "obj", "label": "Object · مَفْعُولٌ بِهِ", "color": "pink"},
    {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"},
    {"k": "prep", "label": "After a preposition", "color": "green"},
    {"k": "harf", "label": "Ḥarf (no iʿrāb job)", "color": "grey"},
]

PLACES = [
    {"k": "raf", "label": "Place of rafʿ · فِي مَحَلِّ رَفْعٍ", "color": "red"},
    {"k": "nasb", "label": "Place of naṣb · فِي مَحَلِّ نَصْبٍ", "color": "pink"},
    {"k": "jarr", "label": "Place of jarr · فِي مَحَلِّ جَرٍّ", "color": "green"},
    {"k": "none", "label": "No place · لَا مَحَلَّ لَهُ", "color": "grey"},
]

BUILT = [
    {"k": "fatha", "label": "On fatha", "color": "pink"},
    {"k": "damma", "label": "On damma", "color": "red"},
    {"k": "sukun", "label": "On sukūn", "color": "navy"},
    {"k": "noon", "label": "On dropping the ن", "color": "brown"},
]


UNIT = {
    "id": "s3-checkup",
    "order": 9,
    "kind": "quiz",
    "title": "Stage 3 quiz",
    "ar": "مُرَاجَعَةُ المَبْنِيَّاتِ",
    "blurb": "A mixed quiz on all the fixed words of Stage 3: pronouns, pointing words, relatives, questions, verbs and ḥarfs.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 3 · QUIZ", "title": "Do you know your fixed words?",
         "text": "Eight cards, at least one for every Stage 3 unit. Do them without your notes.",
         "wm": "المَبْنِيَّاتُ"},

        {"t": "h2", "text": "How it works"},
        {"t": "p", "text": "Do the practice cards in class, one card at a time. Some cards ask for the job and the place of a fixed word. Remember: a fixed word does not change, but its job gives it a place. A ḥarf has no place at all."},
        {"t": "tip", "text": "If you miss a card, go back to its unit and learn the table again. Then do the homework cards."},

        {"t": "summary", "title": "The seven topics", "items": [
            "1. Separate pronouns {أَنَا} to {هُنَّ}, and the idea of a place: {فِي مَحَلِّ رَفْعٍ}.",
            "2. Attached pronouns {ـي} {ـكَ} {ـهُ} on nouns, ḥarfs and verbs.",
            "3. Pointing words {هَذَا} {هَذِهِ} {ذَلِكَ} {تِلْكَ} {هَؤُلَاءِ} {أُولَئِكَ} {هُنَا} {هُنَاكَ}. {هَذَانِ} is not fixed.",
            "4. Relative words {الَّذِي} {الَّتِي} {الَّذِينَ} {اللَّاتِي} {مَنْ} {مَا}. {اللَّذَانِ} is not fixed.",
            "5. Question words {مَنْ} {مَا} {مَاذَا} {مَتَى} {أَيْنَ} {كَيْفَ} {كَمْ} {لِمَاذَا}, and {هَلْ} {أَ}. {أَيٌّ} is not fixed.",
            "6. Past and order verbs: {كَتَبْتُ}، {كَتَبُوا}، {اُكْتُبِي}، {اِذْهَبْ}.",
            "7. Ḥarfs: jarr, joining, answer, question and {يَا}.",
        ]},
    ],

    "practice": [
        {
            "title": "Choose the separate pronoun",
            "fields": [{"key": "pick", "label": "Pronoun", "options": []}],
            "rows": [
                {"s": "I", "ans": {"pick": "a"}, "opts": {"pick": pick("أَنَا", "أَنْتَ", "نَحْنُ")}, "why": "\"I\" is {أَنَا}."},
                {"s": "you (women)", "ans": {"pick": "b"}, "opts": {"pick": pick("أَنْتُمْ", "أَنْتُنَّ", "هُنَّ")}, "why": "\"You\" to a group of women is {أَنْتُنَّ}."},
                {"s": "they two", "ans": {"pick": "a"}, "opts": {"pick": pick("هُمَا", "أَنْتُمَا", "هُمْ")}, "why": "\"They two\" is {هُمَا}. \"You two\" is {أَنْتُمَا}."},
                {"s": "she", "ans": {"pick": "c"}, "opts": {"pick": pick("هُوَ", "أَنْتِ", "هِيَ")}, "why": "\"She\" is {هِيَ}."},
                {"s": "we", "ans": {"pick": "b"}, "opts": {"pick": pick("هُمْ", "نَحْنُ", "أَنَا")}, "why": "\"We\" is {نَحْنُ}."},
            ],
        },
        {
            "title": "Job and place of the fixed word in ( )",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "place", "label": "Place", "options": PLACES},
            ],
            "rows": [
                {"s": "هُوَ طَالِبٌ. (هُوَ)", "gloss": "He is a student.", "ans": {"job": "topic", "place": "raf"},
                 "why": "{هُوَ} is the Topic. Fixed, in the place of rafʿ."},
                {"s": "كِتَابُهُ جَدِيدٌ. (ـهُ)", "gloss": "His book is new.", "ans": {"job": "owner", "place": "jarr"},
                 "why": "\"His\": {ـهُ} owns the book. Owner, in the place of jarr."},
                {"s": "فَتَحَهُ مُحَمَّدٌ. (ـهُ)", "gloss": "Muhammad opened it.", "ans": {"job": "obj", "place": "nasb"},
                 "why": "Opened what? {ـهُ}. Object, in the place of naṣb."},
                {"s": "ذَهَبْتُ إِلَى المَسْجِدِ. (ـتُ)", "gloss": "I went to the mosque.", "ans": {"job": "doer", "place": "raf"},
                 "why": "{ـتُ} \"I\" did the action. Doer, in the place of rafʿ."},
                {"s": "ذَهَبَ إِلَيْهِ. (ـهِ)", "gloss": "He went to him.", "ans": {"job": "prep", "place": "jarr"},
                 "why": "{ـهِ} comes after {إِلَى}. In the place of jarr."},
                {"s": "مَنْ فِي الفَصْلِ؟ (مَنْ)", "gloss": "Who is in the classroom?", "ans": {"job": "topic", "place": "raf"},
                 "why": "{مَنْ} is the Topic and {فِي الفَصْلِ} is the Information. In the place of rafʿ."},
            ],
        },
        {
            "title": "Choose the attached pronoun",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "my book", "ans": {"pick": "a"}, "opts": {"pick": pick("كِتَابِي", "كِتَابُكَ", "كِتَابُهُ")}, "why": "\"My\" is {ـي}: {كِتَابِي}."},
                {"s": "your bag (to a woman)", "ans": {"pick": "b"}, "opts": {"pick": pick("حَقِيبَتُكَ", "حَقِيبَتُكِ", "حَقِيبَتُهَا")}, "why": "\"Your\" to a woman is {ـكِ} with kasra: {حَقِيبَتُكِ}."},
                {"s": "on it (m)", "ans": {"pick": "a"}, "opts": {"pick": pick("عَلَيْهِ", "عَلَيْكَ", "عَلَيْهَا")}, "why": "\"It\" (m) is {ـهِ}: {عَلَيْهِ}. {عَلَيْهَا} is \"on it (f)\"."},
                {"s": "their house (men)", "ans": {"pick": "c"}, "opts": {"pick": pick("بَيْتُنَا", "بَيْتُهُمَا", "بَيْتُهُمْ")}, "why": "\"Their\" for a group of men is {ـهُمْ}: {بَيْتُهُمْ}."},
            ],
        },
        {
            "title": "Choose the pointing word",
            "fields": [{"key": "pick", "label": "Right word", "options": []}],
            "rows": [
                {"s": "… بِنْتٌ.", "gloss": "This is a girl.", "ans": {"pick": "b"}, "opts": {"pick": pick("هَذَا", "هَذِهِ", "تِلْكَ")}, "why": "Near and feminine: {هَذِهِ}."},
                {"s": "… طُلَّابٌ.", "gloss": "These are students.", "ans": {"pick": "c"}, "opts": {"pick": pick("هَذَا", "أُولَئِكَ", "هَؤُلَاءِ")}, "why": "Near and plural: {هَؤُلَاءِ}. {أُولَئِكَ} is \"those\"."},
                {"s": "… سَيَّارَةٌ.", "gloss": "That is a car.", "ans": {"pick": "a"}, "opts": {"pick": pick("تِلْكَ", "ذَلِكَ", "هَذِهِ")}, "why": "Far and feminine: {تِلْكَ}."},
                {"s": "الكِتَابُ …", "gloss": "The book is here.", "ans": {"pick": "a"}, "opts": {"pick": pick("هُنَا", "هُنَاكَ", "هَذَا")}, "why": "\"Here\" is {هُنَا}. {هُنَاكَ} is \"there\"."},
                {"s": "Which one is NOT fixed?", "ans": {"pick": "b"}, "opts": {"pick": pick("هَذَا", "هَذَانِ", "هَؤُلَاءِ")}, "why": "{هَذَانِ} changes for case. We study it in Stage 4."},
            ],
        },
        {
            "title": "Choose the relative word",
            "fields": [{"key": "pick", "label": "Right word", "options": []}],
            "rows": [
                {"s": "خَرَجَ الوَلَدُ … كَتَبَ الدَّرْسَ.", "gloss": "The boy who wrote the lesson went out.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الَّذِي", "الَّتِي", "الَّذِينَ")}, "why": "One boy: {الَّذِي}."},
                {"s": "دَخَلَتِ البِنْتُ … جَلَسَتْ هُنَا.", "gloss": "The girl who sat here came in.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الَّذِي", "الَّتِي", "اللَّاتِي")}, "why": "One girl: {الَّتِي}."},
                {"s": "ذَهَبَ الرِّجَالُ … خَرَجُوا مِنَ المَسْجِدِ.", "gloss": "The men who came out of the mosque left.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الَّذِي", "اللَّاتِي", "الَّذِينَ")}, "why": "A group of men: {الَّذِينَ}."},
                {"s": "Which one is NOT fixed?", "ans": {"pick": "b"}, "opts": {"pick": pick("الَّذِي", "اللَّذَانِ", "الَّذِينَ")}, "why": "{اللَّذَانِ} changes for case. We study it in Stage 4."},
            ],
        },
        {
            "title": "Choose the question word",
            "fields": [{"key": "pick", "label": "Right word", "options": []}],
            "rows": [
                {"s": "… ذَهَبْتَ؟ إِلَى السُّوقِ.", "gloss": "Where did you go? To the market.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَيْنَ", "مَتَى", "مَنْ")}, "why": "The answer is a place: {أَيْنَ}."},
                {"s": "… هَذَا؟ هَذَا طَبِيبٌ.", "gloss": "Who is this? This is a doctor.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَا", "مَنْ", "كَمْ")}, "why": "A person: {مَنْ}."},
                {"s": "… هَذَا؟ هَذَا قَلَمٌ.", "gloss": "What is this? This is a pen.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَا", "مَنْ", "أَيْنَ")}, "why": "A thing: {مَا}."},
                {"s": "… ذَهَبَ مُحَمَّدٌ إِلَى السُّوقِ؟ نَعَمْ.", "gloss": "Did Muhammad go to the market? Yes.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مَاذَا", "أَيْنَ", "هَلْ")}, "why": "A yes/no question: the ḥarf {هَلْ}."},
                {"s": "… كَتَبْتَ؟ كَتَبْتُ الدَّرْسَ.", "gloss": "What did you write? I wrote the lesson.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَتَى", "مَاذَا", "كَيْفَ")}, "why": "What before a verb: {مَاذَا}."},
            ],
        },
        {
            "title": "Past and order verbs",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "أَنْتُمْ + جَلَسَ", "gloss": "you (m pl) sat", "ans": {"pick": "c"},
                 "opts": {"pick": pick("جَلَسُوا", "جَلَسْتُمَا", "جَلَسْتُمْ")}, "why": "{أَنْتُمْ} takes {ـتُمْ}: {جَلَسْتُمْ}."},
                {"s": "Go out! (to a woman)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("اُخْرُجِي", "اِخْرُجِي", "اُخْرُجْ")}, "why": "Middle damma, so {اُ}. To a woman: {اُخْرُجِي}."},
                {"s": "هِيَ + فَتَحَ", "gloss": "she opened", "ans": {"pick": "b"},
                 "opts": {"pick": pick("فَتَحْتِ", "فَتَحَتْ", "فَتَحْتُ")}, "why": "{هِيَ} takes the ḥarf {ـتْ}: {فَتَحَتْ}."},
                {"s": "Enter! (to men)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("اِدْخُلُوا", "اُدْخُلُوا", "دَخَلُوا")}, "why": "Middle damma, so {اُ}: {اُدْخُلُوا}. {دَخَلُوا} is the past."},
            ],
        },
        {
            "title": "Job and place of each fixed word",
            "prompt": "كَتَبْتُهُ فِي بَيْتِهِ.",
            "en": "I wrote it in his house.",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "place", "label": "Place", "options": PLACES},
            ],
            "rows": [
                {"s": "ـتُ (in كَتَبْتُهُ)", "ans": {"job": "doer", "place": "raf"},
                 "why": "{ـتُ} \"I\" wrote. Doer, in the place of rafʿ."},
                {"s": "ـهُ (in كَتَبْتُهُ)", "ans": {"job": "obj", "place": "nasb"},
                 "why": "Wrote what? {ـهُ} \"it\". Object, in the place of naṣb."},
                {"s": "فِي", "ans": {"job": "harf", "place": "none"},
                 "why": "{فِي} is a jarr ḥarf. A ḥarf has no place: {لَا مَحَلَّ لَهُ}."},
                {"s": "ـهِ (in بَيْتِهِ)", "ans": {"job": "owner", "place": "jarr"},
                 "why": "\"His\" house: {ـهِ} is the owner, in the place of jarr."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Job and place of the fixed word in ( )",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "place", "label": "Place", "options": PLACES},
            ],
            "rows": [
                {"s": "نَحْنُ طُلَّابٌ. (نَحْنُ)", "gloss": "We are students.", "ans": {"job": "topic", "place": "raf"},
                 "why": "{نَحْنُ} is the Topic. In the place of rafʿ."},
                {"s": "أَيْنَ قَلَمُكَ؟ (ـكَ)", "gloss": "Where is your pen?", "ans": {"job": "owner", "place": "jarr"},
                 "why": "\"Your\" pen: {ـكَ} is the owner, in the place of jarr."},
                {"s": "دَخَلْنَا الفَصْلَ. (ـنَا)", "gloss": "We entered the classroom.", "ans": {"job": "doer", "place": "raf"},
                 "why": "{ـنَا} \"we\" did the action. Doer, in the place of rafʿ."},
                {"s": "فَتَحْنَاهُ. (ـهُ)", "gloss": "We opened it.", "ans": {"job": "obj", "place": "nasb"},
                 "why": "Opened what? {ـهُ}. Object, in the place of naṣb."},
                {"s": "هَذَا كِتَابٌ. (هَذَا)", "gloss": "This is a book.", "ans": {"job": "topic", "place": "raf"},
                 "why": "{هَذَا} is the Topic. Fixed, in the place of rafʿ."},
                {"s": "الكِتَابُ عَلَيْهِ. (ـهِ)", "gloss": "The book is on it.", "ans": {"job": "prep", "place": "jarr"},
                 "why": "{ـهِ} comes after {عَلَى}. In the place of jarr."},
            ],
        },
        {
            "title": "Pointing and relative words",
            "fields": [{"key": "pick", "label": "Right word", "options": []}],
            "rows": [
                {"s": "… رِجَالٌ.", "gloss": "Those are men.", "ans": {"pick": "a"}, "opts": {"pick": pick("أُولَئِكَ", "ذَلِكَ", "هَؤُلَاءِ")}, "why": "Far and plural: {أُولَئِكَ}. {هَؤُلَاءِ} is \"these\"."},
                {"s": "… مَدْرَسَةٌ.", "gloss": "That is a school.", "ans": {"pick": "b"}, "opts": {"pick": pick("ذَلِكَ", "تِلْكَ", "هَذِهِ")}, "why": "Far and feminine: {تِلْكَ}."},
                {"s": "البِنْتُ … فِي الغُرْفَةِ طَالِبَةٌ.", "gloss": "The girl who is in the room is a student.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الَّتِي", "الَّذِي", "اللَّاتِي")}, "why": "One girl: {الَّتِي}."},
                {"s": "جَلَسَ الأَوْلَادُ … دَخَلُوا الفَصْلَ.", "gloss": "The boys who entered the classroom sat down.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الَّذِي", "اللَّاتِي", "الَّذِينَ")}, "why": "A group of boys: {الَّذِينَ}."},
                {"s": "Which one is NOT fixed?", "ans": {"pick": "a"}, "opts": {"pick": pick("هَاتَانِ", "هَذِهِ", "تِلْكَ")}, "why": "{هَاتَانِ} changes for case. We study it in Stage 4."},
            ],
        },
        {
            "title": "Choose the question word",
            "fields": [{"key": "pick", "label": "Right word", "options": []}],
            "rows": [
                {"s": "… كِتَابًا عَلَى المَكْتَبِ؟", "gloss": "How many books are on the desk?", "ans": {"pick": "a"},
                 "opts": {"pick": pick("كَمْ", "مَنْ", "مَتَى")}, "why": "\"How many\": {كَمْ}, then a noun with fatha."},
                {"s": "… أَنْتَ؟ أَنَا بِخَيْرٍ.", "gloss": "How are you? I am well.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَنْ", "كَيْفَ", "أَيْنَ")}, "why": "The answer is how you are: {كَيْفَ}."},
                {"s": "… ذَهَبَ خَالِدٌ؟ ذَهَبَ أَمْسِ.", "gloss": "When did Khalid go? He went yesterday.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَيْنَ", "كَمْ", "مَتَى")}, "why": "The answer is a time: {مَتَى}."},
                {"s": "Which one is NOT fixed?", "ans": {"pick": "a"}, "opts": {"pick": pick("أَيٌّ", "أَيْنَ", "مَتَى")}, "why": "{أَيٌّ} changes its ending. It is flexible."},
            ],
        },
        {
            "title": "What is the verb built on?",
            "fields": [{"key": "built", "label": "Built on", "options": BUILT}],
            "rows": [
                {"s": "دَرَسْنَ", "gloss": "they (f) studied", "ans": {"built": "sukun"}, "why": "Before {ـنَ} the past verb is built on sukūn."},
                {"s": "اِذْهَبَا", "gloss": "go! (you two)", "ans": {"built": "noon"}, "why": "With {ـا} the order verb is built on dropping the {ن}."},
                {"s": "شَرِبُوا", "gloss": "they drank", "ans": {"built": "damma"}, "why": "Before {ـُوا} the past verb is built on damma."},
                {"s": "اُكْتُبْنَ", "gloss": "write! (women)", "ans": {"built": "sukun"}, "why": "With {ـنَ} the order verb is built on sukūn."},
                {"s": "خَرَجَتَا", "gloss": "they two (f) went out", "ans": {"built": "fatha"}, "why": "Fatha on {ج}. {ـتَ} is a ḥarf and {ـا} is the doer."},
            ],
        },
        {
            "title": "Choose the right ḥarf",
            "fields": [{"key": "pick", "label": "Ḥarf", "options": []}],
            "rows": [
                {"s": "ذَهَبْتُ … السُّوقِ.", "gloss": "I went to the market.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("إِلَى", "ثُمَّ", "بَلْ")}, "why": "\"To\": {إِلَى}, and {السُّوقِ} is jarr."},
                {"s": "كَتَبْتُ الدَّرْسَ … القَلَمِ.", "gloss": "I wrote the lesson with the pen.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("ثُمَّ", "يَا", "بِـ")}, "why": "\"With\": {بِالقَلَمِ}."},
                {"s": "أَمَا دَخَلْتَ الفَصْلَ؟ …، دَخَلْتُ.", "gloss": "Didn't you enter the classroom? Yes, I did.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("نَعَمْ", "بَلَى", "بَلْ")}, "why": "Yes to a \"not\" question: {بَلَى}."},
                {"s": "… وَلَدُ، اِجْلِسْ.", "gloss": "Boy, sit down.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَا", "هَلْ", "فِي")}, "why": "Calling: {يَا وَلَدُ}, with one damma."},
            ],
        },
        {
            "title": "Job and place of each fixed word",
            "prompt": "يَا خَالِدُ، أَيْنَ كِتَابُكَ؟ هُوَ عَلَى مَكْتَبِي.",
            "en": "Khalid, where is your book? It is on my desk.",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "place", "label": "Place", "options": PLACES},
            ],
            "rows": [
                {"s": "يَا", "ans": {"job": "harf", "place": "none"}, "why": "{يَا} is the calling ḥarf. It has no place."},
                {"s": "ـكَ (in كِتَابُكَ)", "ans": {"job": "owner", "place": "jarr"}, "why": "\"Your\" book: owner, in the place of jarr."},
                {"s": "هُوَ", "ans": {"job": "topic", "place": "raf"}, "why": "{هُوَ} starts the answer. Topic, in the place of rafʿ."},
                {"s": "عَلَى", "ans": {"job": "harf", "place": "none"}, "why": "{عَلَى} is a jarr ḥarf. It has no place."},
                {"s": "ـي (in مَكْتَبِي)", "ans": {"job": "owner", "place": "jarr"}, "why": "\"My\" desk: owner, in the place of jarr."},
            ],
        },
    ],
}
