# Stage 3, Unit 4: Relative pronouns (الْأَسْمَاءُ الْمَوْصُولَةُ)

FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "purple"}
FLEX = {"k": "flex", "label": "Flexible · مُعْرَبٌ", "color": "orange"}

P_RAF = {"k": "raf", "label": "Place of rafʿ", "color": "red"}
P_NASB = {"k": "nasb", "label": "Place of naṣb", "color": "pink"}
P_JARR = {"k": "jarr", "label": "Place of jarr", "color": "green"}
PLACES = [P_RAF, P_NASB, P_JARR]

QWORD = {"k": "q", "label": "Question word", "color": "gold"}
REL = {"k": "rel", "label": "Relative: the one who, what", "color": "purple"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s3-relatives",
    "order": 4,
    "title": "Relative pronouns",
    "ar": "الْأَسْمَاءُ الْمَوْصُولَةُ",
    "blurb": "Who, which and what: words that join a noun to a clause that tells you more about it.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 3 · UNIT 4", "title": "The one who, the thing which",
         "text": "A relative pronoun joins a noun to a short clause about it: \"the student who passed\". It is fixed, and it never stands alone.",
         "wm": "الَّذِي"},

        {"t": "h2", "text": "The table to learn"},
        {"t": "table", "head": ["Word", "Used for", "Example"], "rows": [
            ["{الَّذِي}", "one male or thing", "{الطَّالِبُ الَّذِي نَجَحَ} the student who passed"],
            ["{الَّتِي}", "one female or thing", "{الْبِنْتُ الَّتِي نَجَحَتْ} the girl who passed"],
            ["{الَّذِينَ}", "a group of males", "{الطُّلَّابُ الَّذِينَ نَجَحُوا} the students who passed"],
            ["{اللَّاتِي} / {اللَّوَاتِي}", "a group of females", "{النِّسَاءُ اللَّاتِي نَجَحْنَ} the women who passed"],
        ]},
        {"t": "cols", "items": [
            {"color": "purple", "title": "General: who", "ar": "مَنْ",
             "text": "for people: {جَاءَ مَنْ نَجَحَ} \"The one who passed came.\""},
            {"color": "purple", "title": "General: what", "ar": "مَا",
             "text": "for things: {قَرَأْتُ مَا كَتَبَ الْمُدَرِّسُ} \"I read what the teacher wrote.\""},
        ]},
        {"t": "tip", "text": "Spelling: {الَّذِي}، {الَّتِي}، {الَّذِينَ} are written with one {ل} and a shadda. {اللَّاتِي} and {اللَّوَاتِي} are written with two."},
        {"t": "rule", "color": "purple", "title": "All of these are fixed",
         "text": "{الَّذِينَ} ends like a plural, but it never changes: it is {الَّذِينَ} in rafʿ, naṣb and jarr. {الَّذِي} and {الَّتِي} always end in a long ī."},

        {"t": "h2", "text": "A relative needs a clause after it"},
        {"t": "p", "text": "{الَّذِي} alone means nothing. The clause after it completes its meaning. This clause is called the {صِلَةٌ}."},
        {"t": "examples", "items": [
            {"ar": "جَاءَ الطَّالِبُ الَّذِي نَجَحَ.", "en": "The student who passed came.", "note": "The ṣila is {نَجَحَ}."},
            {"ar": "هَذِهِ هِيَ الْبِنْتُ الَّتِي كَتَبَتِ الدَّرْسَ.", "en": "This is the girl who wrote the lesson.", "note": "The ṣila is {كَتَبَتِ الدَّرْسَ}."},
            {"ar": "الْكِتَابُ الَّذِي عَلَى الْمَكْتَبِ جَدِيدٌ.", "en": "The book which is on the desk is new.", "note": "The ṣila is a place phrase: {عَلَى الْمَكْتَبِ}."},
            {"ar": "خَرَجَ الرِّجَالُ الَّذِينَ جَلَسُوا فِي الْمَسْجِدِ.", "en": "The men who sat in the mosque went out.", "note": "The ṣila is {جَلَسُوا فِي الْمَسْجِدِ}."},
        ]},
        {"t": "tip", "text": "The ṣila has a small link back to the noun. Often it is hidden in the verb ({نَجَحَ} \"he passed\"). Sometimes it is an attached pronoun: {الطَّالِبُ الَّذِي بَيْتُهُ قَرِيبٌ} \"the student whose house is near\"."},

        {"t": "h2", "text": "Choose by the noun before it"},
        {"t": "p", "text": "Like an adjective, the relative follows a noun with {ال} and matches it: male or female, one or a group."},
        {"t": "examples", "items": [
            {"ar": "الْوَلَدُ الَّذِي فِي الْبَيْتِ", "en": "the boy who is in the house", "note": "One male: {الَّذِي}."},
            {"ar": "السَّاعَةُ الَّتِي عَلَى السَّرِيرِ", "en": "the watch which is on the bed", "note": "{السَّاعَةُ} is feminine: {الَّتِي}."},
            {"ar": "الْأَوْلَادُ الَّذِينَ خَرَجُوا", "en": "the boys who went out", "note": "A group of males: {الَّذِينَ}."},
            {"ar": "النِّسَاءُ اللَّاتِي خَرَجْنَ", "en": "the women who went out", "note": "A group of females: {اللَّاتِي}."},
        ]},
        {"t": "tip", "text": "Look at the verb in the ṣila too. It matches the relative: {الَّذِي خَرَجَ}، {الَّتِي خَرَجَتْ}، {الَّذِينَ خَرَجُوا}، {اللَّاتِي خَرَجْنَ}."},
        {"t": "tip", "text": "After a noun without {ال}, Arabic leaves the relative out: {جَاءَ طَالِبٌ نَجَحَ} \"A student who passed came.\""},

        {"t": "h2", "text": "مَنْ and مَا: question or relative?"},
        {"t": "p", "text": "{مَنْ} and {مَا} are also question words (unit 5). Look at the sentence. A question ends in {؟}. A relative sits inside a normal sentence and means \"the one who\" or \"what\"."},
        {"t": "examples", "items": [
            {"ar": "مَنْ نَجَحَ؟", "en": "Who passed?", "note": "A question."},
            {"ar": "جَاءَ مَنْ نَجَحَ.", "en": "The one who passed came.", "note": "A relative. {نَجَحَ} is its ṣila."},
            {"ar": "مَا عَلَى الْمَكْتَبِ؟", "en": "What is on the desk?", "note": "A question."},
            {"ar": "اِقْرَأْ مَا عَلَى الْمَكْتَبِ.", "en": "Read what is on the desk.", "note": "A relative."},
        ]},

        {"t": "h2", "text": "Its place in the sentence"},
        {"t": "p", "text": "A relative after a noun works like an adjective. It is fixed, so it cannot copy the ending. It copies the place of the noun before it."},
        {"t": "examples", "items": [
            {"ar": "جَاءَ الطَّالِبُ الَّذِي نَجَحَ.", "en": "The student who passed came.", "note": "{الطَّالِبُ} is rafʿ, so {الَّذِي} is in the place of rafʿ."},
            {"ar": "شَكَرَ الْمُدِيرُ الطَّالِبَ الَّذِي نَجَحَ.", "en": "The principal thanked the student who passed.", "note": "{الطَّالِبَ} is naṣb, so {الَّذِي} is in the place of naṣb."},
            {"ar": "ذَهَبْتُ إِلَى الطَّالِبِ الَّذِي نَجَحَ.", "en": "I went to the student who passed.", "note": "{الطَّالِبِ} is jarr, so {الَّذِي} is in the place of jarr."},
        ]},
        {"t": "tip", "text": "{مَنْ} and {مَا} stand alone, so they have their own job. In {جَاءَ مَنْ نَجَحَ}, {مَنْ} is the doer: place of rafʿ."},

        {"t": "h2", "text": "Not fixed: اللَّذَانِ and اللَّتَانِ"},
        {"t": "rule", "color": "orange", "title": "The words for \"the two who\" change",
         "text": "{اللَّذَانِ} (two males) and {اللَّتَانِ} (two females) are flexible. In naṣb and jarr they become {اللَّذَيْنِ} and {اللَّتَيْنِ}. You learn them with the dual in Stage 4."},
        {"t": "table", "head": ["Form", "Two males", "Two females"], "rows": [
            ["Rafʿ", "اللَّذَانِ", "اللَّتَانِ"],
            ["Naṣb and jarr", "اللَّذَيْنِ", "اللَّتَيْنِ"],
        ]},

        {"t": "summary", "title": "In short", "items": [
            "{الَّذِي} one male or thing, {الَّتِي} one female or thing, {الَّذِينَ} males, {اللَّاتِي} / {اللَّوَاتِي} females.",
            "{مَنْ} \"the one who\" for people, {مَا} \"what\" for things.",
            "A relative needs a ṣila ({صِلَةٌ}) after it: {الَّذِي نَجَحَ}.",
            "Match the noun before it. The relative takes the place of that noun: rafʿ, naṣb or jarr.",
            "{اللَّذَانِ} and {اللَّتَانِ} are not fixed. They wait for Stage 4.",
        ]},
    ],

    "practice": [
        {
            "title": "Choose the relative pronoun",
            "fields": [{"key": "pick", "label": "Relative", "options": []}],
            "rows": [
                {"s": "خَرَجَ الْوَلَدُ ... جَلَسَ فِي الْفَصْلِ.", "gloss": "The boy who sat in the classroom went out.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الَّذِي", "الَّتِي", "الَّذِينَ")}, "why": "{الْوَلَدُ} is one male: {الَّذِي}."},
                {"s": "الْبِنْتُ ... ذَهَبَتْ إِلَى السُّوقِ بِنْتُ الْمُدِيرِ.", "gloss": "The girl who went to the market is the principal's daughter.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الَّذِي", "الَّتِي", "اللَّاتِي")}, "why": "{الْبِنْتُ} is one female: {الَّتِي}. The verb {ذَهَبَتْ} is feminine too."},
                {"s": "خَرَجَ الطُّلَّابُ ... دَرَسُوا فِي الْمَسْجِدِ.", "gloss": "The students who studied in the mosque went out.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الَّذِي", "اللَّاتِي", "الَّذِينَ")}, "why": "{الطُّلَّابُ} is a group of males: {الَّذِينَ دَرَسُوا}."},
                {"s": "أَيْنَ النِّسَاءُ ... جَلَسْنَ هُنَا؟", "gloss": "Where are the women who sat here?", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الَّتِي", "اللَّاتِي", "الَّذِينَ")}, "why": "A group of females, and the verb {جَلَسْنَ} is plural: {اللَّاتِي}."},
                {"s": "الْمِفْتَاحُ ... عَلَى السَّرِيرِ مِفْتَاحُ السَّيَّارَةِ.", "gloss": "The key which is on the bed is the car key.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الَّذِي", "الَّتِي", "مَنْ")}, "why": "{الْمِفْتَاحُ} is one masculine thing: {الَّذِي}."},
                {"s": "السَّاعَةُ ... فِي الْحَقِيبَةِ جَدِيدَةٌ.", "gloss": "The watch which is in the bag is new.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الَّذِي", "الَّذِينَ", "الَّتِي")}, "why": "{السَّاعَةُ} is feminine: {الَّتِي}."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "جَاءَ الطَّالِبُ الَّذِي نَجَحَ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("The student came and passed.", "The student who passed came.", "Who passed? The student.")},
                 "why": "{الَّذِي نَجَحَ} tells us which student: the one who passed."},
                {"s": "الرَّجُلُ الَّذِي فِي الْمَسْجِدِ إِمَامٌ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The man who is in the mosque is an imam.", "The man is in the imam's mosque.", "This man in the mosque is an imam.")},
                 "why": "The ṣila is {فِي الْمَسْجِدِ}. The Information is {إِمَامٌ}."},
                {"s": "خَرَجَ الرِّجَالُ الَّذِينَ جَلَسُوا فِي الدُّكَّانِ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("The men went out and sat in the shop.", "The man who sat in the shop went out.", "The men who sat in the shop went out.")},
                 "why": "{الَّذِينَ} and {جَلَسُوا} are plural: the men who sat."},
                {"s": "اُكْتُبْ مَا قَرَأْتَ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("Write what you read.", "What did you read? Write.", "Write the one who read.")},
                 "why": "{مَا} here is \"what\", and {قَرَأْتَ} is its ṣila."},
                {"s": "هَذِهِ هِيَ الْمُدَرِّسَةُ الَّتِي فَتَحَتِ الْبَابَ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("This teacher opened the door.", "This is the teacher who opened the door.", "This is the door the teacher opened.")},
                 "why": "{هِيَ} makes \"this is the teacher\", and {الَّتِي فَتَحَتِ الْبَابَ} says which one."},
            ],
        },
        {
            "title": "مَنْ and مَا: question or relative?",
            "fields": [{"key": "kind", "label": "The word in [ ]", "options": [QWORD, REL]}],
            "rows": [
                {"s": "[مَنْ] فِي الْغُرْفَةِ؟", "gloss": "Who is in the room?", "ans": {"kind": "q"}, "why": "It asks, and the sentence ends in {؟}."},
                {"s": "جَاءَ [مَنْ] نَجَحَ.", "gloss": "The one who passed came.", "ans": {"kind": "rel"}, "why": "No question. {مَنْ} means \"the one who\", and {نَجَحَ} is its ṣila."},
                {"s": "[مَا] هَذَا؟", "gloss": "What is this?", "ans": {"kind": "q"}, "why": "It asks about a thing. Madinah lesson 1."},
                {"s": "قَرَأْتُ [مَا] كَتَبَ الْمُدَرِّسُ.", "gloss": "I read what the teacher wrote.", "ans": {"kind": "rel"}, "why": "No question. {مَا} means \"what\", the thing which."},
                {"s": "[مَنْ] كَتَبَ الدَّرْسَ؟", "gloss": "Who wrote the lesson?", "ans": {"kind": "q"}, "why": "It asks, and the sentence ends in {؟}."},
                {"s": "خَرَجَ [مَنْ] جَلَسَ فِي الْفَصْلِ.", "gloss": "The one who sat in the classroom went out.", "ans": {"kind": "rel"}, "why": "No question. The ṣila is {جَلَسَ فِي الْفَصْلِ}."},
            ],
        },
        {
            "title": "Find the ṣila",
            "fields": [{"key": "pick", "label": "Ṣila · صِلَةٌ", "options": []}],
            "rows": [
                {"s": "الْكِتَابُ الَّذِي عَلَى الْمَكْتَبِ جَدِيدٌ.", "gloss": "The book which is on the desk is new.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْكِتَابُ", "عَلَى الْمَكْتَبِ", "جَدِيدٌ")}, "why": "The ṣila comes right after {الَّذِي}: {عَلَى الْمَكْتَبِ}. {جَدِيدٌ} is the Information."},
                {"s": "هَذَا هُوَ الطَّبِيبُ الَّذِي ذَهَبَ إِلَى الْمُدِيرِ.", "gloss": "This is the doctor who went to the principal.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("هَذَا هُوَ", "الطَّبِيبُ", "ذَهَبَ إِلَى الْمُدِيرِ")}, "why": "After {الَّذِي}: {ذَهَبَ إِلَى الْمُدِيرِ}."},
                {"s": "الْحَقِيبَةُ الَّتِي فِي السَّيَّارَةِ ثَقِيلَةٌ.", "gloss": "The bag which is in the car is heavy.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْحَقِيبَةُ", "فِي السَّيَّارَةِ", "ثَقِيلَةٌ")}, "why": "After {الَّتِي}: {فِي السَّيَّارَةِ}. {ثَقِيلَةٌ} is the Information."},
                {"s": "أَيْنَ الرِّجَالُ الَّذِينَ خَرَجُوا مِنَ الْمَسْجِدِ؟", "gloss": "Where are the men who went out of the mosque?", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَيْنَ", "الرِّجَالُ", "خَرَجُوا مِنَ الْمَسْجِدِ")}, "why": "After {الَّذِينَ}: {خَرَجُوا مِنَ الْمَسْجِدِ}."},
                {"s": "قَرَأْتُ مَا كَتَبْتَ.", "gloss": "I read what you wrote.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("قَرَأْتُ", "كَتَبْتَ", "قَرَأْتُ مَا")}, "why": "After {مَا}: {كَتَبْتَ}. {قَرَأْتُ} is the main verb."},
            ],
        },
        {
            "title": "Place of the relative in [ ]",
            "fields": [{"key": "place", "label": "Place", "options": PLACES}],
            "rows": [
                {"s": "نَجَحَ الطَّالِبُ [الَّذِي] دَرَسَ.", "gloss": "The student who studied passed.", "ans": {"place": "raf"},
                 "why": "It follows {الطَّالِبُ}, the doer, which is rafʿ."},
                {"s": "شَكَرَ الْمُدِيرُ الطَّالِبَ [الَّذِي] نَجَحَ.", "gloss": "The principal thanked the student who passed.", "ans": {"place": "nasb"},
                 "why": "It follows {الطَّالِبَ}, the object, which is naṣb."},
                {"s": "ذَهَبْتُ إِلَى الرَّجُلِ [الَّذِي] فِي الدُّكَّانِ.", "gloss": "I went to the man who is in the shop.", "ans": {"place": "jarr"},
                 "why": "It follows {الرَّجُلِ}, which is jarr after {إِلَى}."},
                {"s": "فَتَحَ الْوَلَدُ الْحَقِيبَةَ [الَّتِي] عَلَى الْمَكْتَبِ.", "gloss": "The boy opened the bag which is on the desk.", "ans": {"place": "nasb"},
                 "why": "It follows {الْحَقِيبَةَ}, the object, which is naṣb."},
                {"s": "كِتَابُ الْبِنْتِ [الَّتِي] نَجَحَتْ جَدِيدٌ.", "gloss": "The book of the girl who passed is new.", "ans": {"place": "jarr"},
                 "why": "{الَّتِي} is feminine, so it describes {الْبِنْتِ}, the owner, which is jarr."},
                {"s": "الْوَلَدُ [الَّذِي] فِي الْحَمَّامِ ابْنُ الْمُدَرِّسِ.", "gloss": "The boy who is in the bathroom is the teacher's son.", "ans": {"place": "raf"},
                 "why": "It follows {الْوَلَدُ}, the Topic, which is rafʿ."},
            ],
        },
        {
            "title": "Fixed or flexible?",
            "fields": [{"key": "type", "label": "Type", "options": [FIXED, FLEX]}],
            "rows": [
                {"s": "الَّذِي", "gloss": "who, which (m.)", "ans": {"type": "fixed"}, "why": "A relative pronoun. It never changes."},
                {"s": "الَّتِي", "gloss": "who, which (f.)", "ans": {"type": "fixed"}, "why": "A relative pronoun. It never changes."},
                {"s": "اللَّذَانِ", "gloss": "the two who (m.)", "ans": {"type": "flex"},
                 "why": "The exception. {اللَّذَانِ} becomes {اللَّذَيْنِ} in naṣb and jarr. Stage 4."},
                {"s": "الَّذِينَ", "gloss": "who (m. pl.)", "ans": {"type": "fixed"}, "why": "It looks like a plural, but it is {الَّذِينَ} in every place."},
                {"s": "الطَّالِبُ", "gloss": "the student", "ans": {"type": "flex"}, "why": "A normal noun. It can be {الطَّالِبَ} or {الطَّالِبِ}."},
                {"s": "مَنْ", "gloss": "the one who", "ans": {"type": "fixed"}, "why": "It always ends in sukūn."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Choose the relative pronoun",
            "fields": [{"key": "pick", "label": "Relative", "options": []}],
            "rows": [
                {"s": "هَذِهِ هِيَ الْبِنْتُ ... ذَهَبَتْ إِلَى الْجَامِعَةِ.", "gloss": "This is the girl who went to the university.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الَّذِي", "الَّتِي", "اللَّاتِي")}, "why": "One female: {الَّتِي ذَهَبَتْ}."},
                {"s": "أَيْنَ الْأَوْلَادُ ... خَرَجُوا مِنَ الْبَيْتِ؟", "gloss": "Where are the boys who went out of the house?", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الَّذِي", "الَّذِينَ", "اللَّاتِي")}, "why": "A group of males: {الَّذِينَ خَرَجُوا}."},
                {"s": "الطَّالِبُ ... بَيْتُهُ قَرِيبٌ فِي الْفَصْلِ.", "gloss": "The student whose house is near is in the classroom.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الَّذِي", "الَّتِي", "مَا")}, "why": "One male. The {ـهُ} in {بَيْتُهُ} links back to him."},
                {"s": "شَكَرَ الْمُدَرِّسُ الرِّجَالَ ... فَتَحُوا الْمَدْرَسَةَ.", "gloss": "The teacher thanked the men who opened the school.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الَّذِي", "الَّتِي", "الَّذِينَ")}, "why": "A group of males. In naṣb it is still {الَّذِينَ}: it is fixed."},
                {"s": "النِّسَاءُ ... خَرَجْنَ مِنَ الْمَسْجِدِ فِي السُّوقِ.", "gloss": "The women who went out of the mosque are in the market.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الَّتِي", "اللَّاتِي", "الَّذِينَ")}, "why": "A group of females with a plural verb {خَرَجْنَ}: {اللَّاتِي}."},
                {"s": "ذَهَبْتُ إِلَى الْغُرْفَةِ ... فِيهَا الْمُدِيرُ.", "gloss": "I went to the room which the principal is in.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الَّذِي", "الَّتِي", "اللَّاتِي")}, "why": "{الْغُرْفَةِ} is one feminine thing: {الَّتِي}. The {هَا} in {فِيهَا} links back."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "الْكِتَابُ الَّذِي كَتَبَهُ الْمُدَرِّسُ جَدِيدٌ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("The teacher wrote a new book.", "The teacher's book is new.", "The book which the teacher wrote is new.")},
                 "why": "The ṣila is {كَتَبَهُ الْمُدَرِّسُ}. The Information is {جَدِيدٌ}."},
                {"s": "خَرَجَ مَنْ فِي الْبَيْتِ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The one who was in the house went out.", "Who went out of the house?", "He went out of the house.")},
                 "why": "No {؟}, so {مَنْ} is a relative: \"the one who\"."},
                {"s": "هَؤُلَاءِ هُمُ الطُّلَّابُ الَّذِينَ نَجَحُوا.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("These students passed.", "These are the students who passed.", "Who are the students who passed?")},
                 "why": "{هُمُ} makes \"these are the students\", and {الَّذِينَ نَجَحُوا} says which ones."},
                {"s": "فَتَحَتِ الْبِنْتُ الْبَابَ الَّذِي فِي الْمَطْبَخِ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The girl opened the door which is in the kitchen.", "The girl who is in the kitchen opened the door.", "The girl opened the kitchen door and went in.")},
                 "why": "{الَّذِي} is masculine and comes after {الْبَابَ}. It describes the door."},
                {"s": "اِقْرَأْ مَا فِي الْكِتَابِ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("What is in the book?", "Read the book.", "Read what is in the book.")},
                 "why": "{مَا} is \"what\", and {فِي الْكِتَابِ} is its ṣila."},
            ],
        },
        {
            "title": "مَنْ and مَا: question or relative?",
            "fields": [{"key": "kind", "label": "The word in [ ]", "options": [QWORD, REL]}],
            "rows": [
                {"s": "[مَنْ] أَنْتَ؟", "gloss": "Who are you?", "ans": {"kind": "q"}, "why": "It asks, and the sentence ends in {؟}."},
                {"s": "شَكَرَ الْمُدِيرُ [مَنْ] نَجَحَ.", "gloss": "The principal thanked the one who passed.", "ans": {"kind": "rel"}, "why": "No question. {مَنْ نَجَحَ} is \"the one who passed\"."},
                {"s": "[مَا] اسْمُكَ؟", "gloss": "What is your name?", "ans": {"kind": "q"}, "why": "It asks, and the sentence ends in {؟}."},
                {"s": "اِقْرَأْ [مَا] كَتَبْتُ.", "gloss": "Read what I wrote.", "ans": {"kind": "rel"}, "why": "No question. {مَا} is \"what\", and {كَتَبْتُ} is its ṣila."},
                {"s": "[مَنْ] مِنَ الصِّينِ؟", "gloss": "Who is from China?", "ans": {"kind": "q"}, "why": "A question from Madinah lesson 4."},
                {"s": "ذَهَبَ [مَنْ] فِي الْفَصْلِ إِلَى الْمَسْجِدِ.", "gloss": "The one who was in the classroom went to the mosque.", "ans": {"kind": "rel"},
                 "why": "No question. The ṣila is {فِي الْفَصْلِ}."},
            ],
        },
        {
            "title": "Find the ṣila",
            "fields": [{"key": "pick", "label": "Ṣila · صِلَةٌ", "options": []}],
            "rows": [
                {"s": "الرَّجُلُ الَّذِي بَيْتُهُ بَعِيدٌ تَاجِرٌ.", "gloss": "The man whose house is far is a merchant.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الرَّجُلُ", "بَيْتُهُ بَعِيدٌ", "تَاجِرٌ")}, "why": "The ṣila is a small nominal sentence: {بَيْتُهُ بَعِيدٌ}. {تَاجِرٌ} is the Information."},
                {"s": "أَيْنَ الْقَلَمُ الَّذِي كَتَبْتَ بِهِ الدَّرْسَ؟", "gloss": "Where is the pen you wrote the lesson with?", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَيْنَ الْقَلَمُ", "كَتَبْتَ بِهِ الدَّرْسَ", "الدَّرْسَ")}, "why": "Everything after {الَّذِي}: {كَتَبْتَ بِهِ الدَّرْسَ}. The {ـهِ} in {بِهِ} links back to the pen."},
                {"s": "جَلَسَ مَنْ دَخَلَ الْفَصْلَ.", "gloss": "The one who entered the classroom sat down.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("جَلَسَ", "دَخَلَ الْفَصْلَ", "الْفَصْلَ")}, "why": "After {مَنْ}: {دَخَلَ الْفَصْلَ}. {جَلَسَ} is the main verb."},
                {"s": "هَؤُلَاءِ هُنَّ النِّسَاءُ اللَّاتِي ذَهَبْنَ إِلَى الْمَدِينَةِ.", "gloss": "These are the women who went to the city.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("هَؤُلَاءِ هُنَّ", "النِّسَاءُ", "ذَهَبْنَ إِلَى الْمَدِينَةِ")}, "why": "After {اللَّاتِي}: {ذَهَبْنَ إِلَى الْمَدِينَةِ}."},
                {"s": "فَتَحَ الْمُدِيرُ الْمَدْرَسَةَ الَّتِي فِي الشَّارِعِ.", "gloss": "The principal opened the school which is in the street.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فِي الشَّارِعِ", "الْمَدْرَسَةَ", "فَتَحَ الْمُدِيرُ")}, "why": "After {الَّتِي}: the place phrase {فِي الشَّارِعِ}."},
            ],
        },
        {
            "title": "Place of the word in [ ]",
            "fields": [{"key": "place", "label": "Place", "options": PLACES}],
            "rows": [
                {"s": "خَرَجَ [مَنْ] كَتَبَ الدَّرْسَ.", "gloss": "The one who wrote the lesson went out.", "ans": {"place": "raf"},
                 "why": "{مَنْ} stands alone here. It is the doer of {خَرَجَ}: place of rafʿ."},
                {"s": "نَجَحَ الطُّلَّابُ [الَّذِينَ] دَرَسُوا.", "gloss": "The students who studied passed.", "ans": {"place": "raf"},
                 "why": "It follows {الطُّلَّابُ}, the doer, which is rafʿ."},
                {"s": "شَكَرَ الْمُدَرِّسُ الْأَوْلَادَ [الَّذِينَ] فَتَحُوا الْبَابَ.", "gloss": "The teacher thanked the boys who opened the door.", "ans": {"place": "nasb"},
                 "why": "It follows {الْأَوْلَادَ}, the object, which is naṣb. The form stays {الَّذِينَ}."},
                {"s": "ذَهَبَ الْمُدَرِّسُ إِلَى الطُّلَّابِ [الَّذِينَ] فِي الْفَصْلِ.", "gloss": "The teacher went to the students who are in the classroom.", "ans": {"place": "jarr"},
                 "why": "It follows {الطُّلَّابِ}, which is jarr after {إِلَى}."},
                {"s": "كَتَبْتُ [مَا] قَرَأَ الْمُدَرِّسُ.", "gloss": "I wrote what the teacher read.", "ans": {"place": "nasb"},
                 "why": "{مَا} stands alone. It is the object of {كَتَبْتُ}: place of naṣb."},
                {"s": "سَيَّارَةُ الرَّجُلِ [الَّذِي] فِي الْمَسْجِدِ جَدِيدَةٌ.", "gloss": "The car of the man who is in the mosque is new.", "ans": {"place": "jarr"},
                 "why": "{الَّذِي} is masculine, so it describes {الرَّجُلِ}, the owner, which is jarr."},
            ],
        },
        {
            "title": "Fixed or flexible?",
            "fields": [{"key": "type", "label": "Type", "options": [FIXED, FLEX]}],
            "rows": [
                {"s": "اللَّاتِي", "gloss": "who (f. pl.)", "ans": {"type": "fixed"}, "why": "A relative pronoun. It never changes."},
                {"s": "اللَّتَانِ", "gloss": "the two who (f.)", "ans": {"type": "flex"},
                 "why": "The exception. {اللَّتَانِ} becomes {اللَّتَيْنِ} in naṣb and jarr. Stage 4."},
                {"s": "مَا", "gloss": "what", "ans": {"type": "fixed"}, "why": "It always ends in alif."},
                {"s": "اللَّوَاتِي", "gloss": "who (f. pl.)", "ans": {"type": "fixed"}, "why": "Another form of {اللَّاتِي}. It never changes."},
                {"s": "الرَّجُلُ", "gloss": "the man", "ans": {"type": "flex"}, "why": "A normal noun. After {إِلَى} it becomes {الرَّجُلِ}."},
                {"s": "هَؤُلَاءِ", "gloss": "these (unit 3)", "ans": {"type": "fixed"}, "why": "A pointing word. It always ends in kasra."},
            ],
        },
    ],
}
