# Stage 8, Unit 1: Meet the present verb (الفِعْلُ المُضَارِعُ)

RAF = {"k": "raf",  "label": "Rafʿ · رَفْعٌ",   "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ",  "color": "pink"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ",   "color": "green"}
JAZM = {"k": "jazm", "label": "Jazm · جَزْمٌ",  "color": "navy"}

PAST = {"k": "past", "label": "Past · مَاضٍ", "color": "navy"}
PRES = {"k": "pres", "label": "Present · مُضَارِعٌ", "color": "orange"}
ORDR = {"k": "ordr", "label": "Order · أَمْرٌ", "color": "brown"}
VTYPE = [PAST, PRES, ORDR]

FLEX = {"k": "flex", "label": "Flexible · مُعْرَبٌ", "color": "green"}
FIXD = {"k": "fixd", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}

BUILT = [
    {"k": "fatha", "label": "On fatha · عَلَى الفَتْحِ", "color": "pink"},
    {"k": "damma", "label": "On damma · عَلَى الضَّمِّ", "color": "red"},
    {"k": "sukun", "label": "On sukūn · عَلَى السُّكُونِ", "color": "navy"},
]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s8-present",
    "order": 1,
    "title": "Meet the present verb",
    "ar": "الفِعْلُ المُضَارِعُ",
    "blurb": "The verb for \"is doing\" and \"will do\": its four first letters, all its persons, and why it is the one verb that changes.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 8 · UNIT 1", "title": "The verb that changes",
         "text": "Past and order verbs are fixed. The present verb ({الفِعْلُ المُضَارِعُ}) is different: its last letter changes with iʿrāb.",
         "wm": "يَكْتُبُ"},

        {"t": "h2", "text": "Three kinds of verb"},
        {"t": "cols", "items": [
            {"color": "navy", "title": "Past · fixed", "ar": "كَتَبَ", "text": "he wrote"},
            {"color": "orange", "title": "Present · flexible", "ar": "يَكْتُبُ", "text": "he writes, he is writing, he will write"},
            {"color": "brown", "title": "Order · fixed", "ar": "اُكْتُبْ", "text": "write!"},
        ]},
        {"t": "table", "head": ["Past", "Present", "Order", "Meaning"], "rows": [
            ["كَتَبَ", "يَكْتُبُ", "اُكْتُبْ", "write"],
            ["ذَهَبَ", "يَذْهَبُ", "اِذْهَبْ", "go"],
            ["جَلَسَ", "يَجْلِسُ", "اِجْلِسْ", "sit"],
            ["خَرَجَ", "يَخْرُجُ", "اُخْرُجْ", "go out"],
            ["فَتَحَ", "يَفْتَحُ", "اِفْتَحْ", "open"],
            ["شَرِبَ", "يَشْرَبُ", "اِشْرَبْ", "drink"],
        ]},
        {"t": "tip", "text": "The middle vowel of the present verb is not always the same: {يَكْتُبُ}، {يَجْلِسُ}، {يَذْهَبُ}. Learn each present verb as a word. The order verb takes the same middle vowel: {يَكْتُبُ} → {اُكْتُبْ}."},

        {"t": "h2", "text": "It starts with أ ن ي ت"},
        {"t": "rule", "color": "orange", "title": "The letters of أَنَيْتُ",
         "text": "Every present verb starts with one of four letters: {أ}، {ن}، {ي}، {ت}. Put them together and you get the word {أَنَيْتُ}."},
        {"t": "table", "head": ["Letter", "Who", "Example"], "rows": [
            ["{أ}", "I", "أَكْتُبُ"],
            ["{ن}", "we", "نَكْتُبُ"],
            ["{ي}", "he, they", "يَكْتُبُ، يَكْتُبُونَ"],
            ["{ت}", "you, she", "تَكْتُبُ، تَكْتُبِينَ"],
        ]},
        {"t": "tip", "text": "Some past verbs also start with one of these letters as part of the word: {أَكَلَ} \"he ate\", {نَزَلَ} \"he went down\", {تَعَلَّمَ} \"he learned\". Their present verbs are {يَأْكُلُ}، {يَنْزِلُ}، {يَتَعَلَّمُ}. Check the meaning, not only the first letter."},
        {"t": "tip", "text": "The first letter usually has fatha: {يَكْتُبُ}. If the past verb has four letters (a shadda counts as two), it has damma: {سَاعَدَ} → {يُسَاعِدُ}، {عَلَّمَ} → {يُعَلِّمُ}."},

        {"t": "h2", "text": "All the persons of يَكْتُبُ"},
        {"t": "p", "text": "Learn this table by heart, the same way you learned the past verb in Stage 3."},
        {"t": "table", "head": ["Person", "Pronoun", "Present verb", "Meaning"], "rows": [
            ["he", "هُوَ", "يَكْتُبُ", "he writes"],
            ["they two (m)", "هُمَا", "يَكْتُبَانِ", "they two write"],
            ["they (m)", "هُمْ", "يَكْتُبُونَ", "they write"],
            ["she", "هِيَ", "تَكْتُبُ", "she writes"],
            ["they two (f)", "هُمَا", "تَكْتُبَانِ", "they two write"],
            ["they (f)", "هُنَّ", "يَكْتُبْنَ", "they write"],
            ["you (m)", "أَنْتَ", "تَكْتُبُ", "you write"],
            ["you two", "أَنْتُمَا", "تَكْتُبَانِ", "you two write"],
            ["you (m pl)", "أَنْتُمْ", "تَكْتُبُونَ", "you all write"],
            ["you (f)", "أَنْتِ", "تَكْتُبِينَ", "you write"],
            ["you (f pl)", "أَنْتُنَّ", "تَكْتُبْنَ", "you all write"],
            ["I", "أَنَا", "أَكْتُبُ", "I write"],
            ["we", "نَحْنُ", "نَكْتُبُ", "we write"],
        ]},
        {"t": "tip", "text": "Some forms are shared. {تَكْتُبُ} is \"you (m)\" and \"she\". {تَكْتُبَانِ} is \"you two\" and \"they two (f)\". The sentence tells you which one is meant."},

        {"t": "h2", "text": "Who is the doer?"},
        {"t": "p", "text": "As with the past verb, the doer is either hidden or an attached pronoun at the end."},
        {"t": "cols", "items": [
            {"color": "blue", "title": "Hidden doer", "ar": "يَكْتُبُ", "text": "{أَكْتُبُ} (أَنَا)، {نَكْتُبُ} (نَحْنُ)، {يَكْتُبُ} (هُوَ)، {تَكْتُبُ} (أَنْتَ or هِيَ)"},
            {"color": "red", "title": "Attached doer", "ar": "يَكْتُبُونَ", "text": "{ا} of two, {و} of a group, {ي} of one woman, {ن} of women"},
        ]},
        {"t": "examples", "items": [
            {"ar": "يَكْتُبُ الطَّالِبُ الدَّرْسَ.", "en": "The student writes the lesson.", "note": "A noun is the doer: {الطَّالِبُ}. The verb has no doer ending."},
            {"ar": "الطُّلَّابُ يَكْتُبُونَ الدَّرْسَ.", "en": "The students write the lesson.", "note": "The {و} is the doer. Unit 3 explains the {ن}."},
        ]},

        {"t": "h2", "text": "Now and later"},
        {"t": "p", "text": "The present verb is for an action that is happening now or happens often. It can also be about the future."},
        {"t": "examples", "items": [
            {"ar": "أَقْرَأُ القُرْآنَ.", "en": "I read the Qur'an. / I am reading the Qur'an."},
            {"ar": "سَيَكْتُبُ المُدَرِّسُ الدَّرْسَ.", "en": "The teacher will write the lesson.", "note": "{سَـ} adds \"will\"."},
            {"ar": "سَوْفَ نَرْجِعُ إِلَى البَيْتِ.", "en": "We will return to the house.", "note": "{سَوْفَ} also adds \"will\"."},
            {"ar": "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ.", "en": "You alone we worship, and You alone we ask for help. (al-Fātiḥa 1:5)", "note": "Two present verbs, both with {ن} \"we\"."},
        ]},
        {"t": "tip", "text": "{سَـ} and {سَوْفَ} only add \"will\". They do not change the ending of the verb."},

        {"t": "h2", "text": "The only flexible verb: three cases"},
        {"t": "p", "text": "Nouns have rafʿ, naṣb and jarr. The present verb has rafʿ, naṣb and jazm. It never takes jarr, and a noun never takes jazm."},
        {"t": "table", "head": ["Case", "Example", "Meaning", "Unit"], "rows": [
            ["Rafʿ · رَفْعٌ", "يَكْتُبُ", "he writes", "Unit 2"],
            ["Naṣb · نَصْبٌ", "لَنْ يَكْتُبَ", "he will not write", "Unit 4"],
            ["Jazm · جَزْمٌ", "لَمْ يَكْتُبْ", "he did not write", "Unit 5"],
        ]},
        {"t": "rule", "color": "red", "title": "Job → case → sign, for verbs too",
         "text": "With no particle before it, the verb is in rafʿ. A particle of naṣb ({لَنْ}) puts it in naṣb. A particle of jazm ({لَمْ}) puts it in jazm. Then the kind of verb gives the sign."},
        {"t": "examples", "items": [
            {"ar": "يَكْتُبُ", "en": "he writes",
             "note": "{فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}: a present verb in rafʿ, and its sign is damma."},
            {"ar": "لَنْ يَكْتُبَ", "en": "he will not write",
             "note": "{فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}: in naṣb because of {لَنْ}, sign fatha."},
            {"ar": "لَمْ يَكْتُبْ", "en": "he did not write",
             "note": "{فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ}: in jazm because of {لَمْ}, sign sukūn."},
        ]},

        {"t": "h2", "text": "When the present verb is fixed"},
        {"t": "p", "text": "The present verb is flexible only when nothing is attached to its end that makes it fixed. Two nūns make it fixed."},
        {"t": "cols", "items": [
            {"color": "grey", "title": "Nūn of women · نُونُ النِّسْوَةِ", "ar": "يَكْتُبْنَ",
             "text": "Fixed on sukūn. The {ن} is the doer: \"they (f)\". Also {تَكْتُبْنَ} \"you (f pl)\"."},
            {"color": "grey", "title": "Nūn of emphasis · نُونُ التَّوْكِيدِ", "ar": "لَيَكْتُبَنَّ",
             "text": "Fixed on fatha. The {نَّ} adds \"surely\". It is a ḥarf."},
        ]},
        {"t": "examples", "items": [
            {"ar": "البَنَاتُ يَكْتُبْنَ الدَّرْسَ.", "en": "The girls write the lesson.",
             "note": "{يَكْتُبْنَ}: {فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ}. The {ن} is the doer, in the place of rafʿ."},
            {"ar": "وَاللّٰهِ لَأَكْتُبَنَّ الدَّرْسَ.", "en": "By Allah, I will surely write the lesson.",
             "note": "{أَكْتُبَنَّ}: {فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ}. The doer is hidden: {أَنَا}."},
        ]},
        {"t": "tip", "text": "A fixed present verb never changes its ending. {لَنْ يَكْتُبْنَ} and {لَمْ يَكْتُبْنَ} keep the same shape."},

        {"t": "summary", "title": "In short", "items": [
            "The present verb starts with {أ}، {ن}، {ي} or {ت}: {أَنَيْتُ}.",
            "It means \"is doing\" or \"does\". With {سَـ} or {سَوْفَ} it means \"will do\".",
            "Know all its persons: {أَكْتُبُ}، {نَكْتُبُ}، {تَكْتُبُ}، {تَكْتُبِينَ}، {يَكْتُبُ}، {تَكْتُبَانِ}، {يَكْتُبَانِ}، {تَكْتُبُونَ}، {يَكْتُبُونَ}، {تَكْتُبْنَ}، {يَكْتُبْنَ}.",
            "It is the only flexible verb. Its cases are rafʿ, naṣb and jazm, never jarr.",
            "It is fixed with the nūn of women ({يَكْتُبْنَ}, on sukūn) and with the nūn of emphasis ({لَيَكْتُبَنَّ}, on fatha).",
        ]},
    ],

    "practice": [
        {
            "title": "Past, present or order?",
            "fields": [{"key": "vt", "label": "Kind of verb", "options": VTYPE}],
            "rows": [
                {"s": "يَكْتُبُ", "gloss": "write", "ans": {"vt": "pres"}, "why": "It starts with {ي}: \"he writes\"."},
                {"s": "كَتَبَ", "gloss": "write", "ans": {"vt": "past"}, "why": "\"He wrote\". The action is done."},
                {"s": "اُكْتُبْ", "gloss": "write", "ans": {"vt": "ordr"}, "why": "\"Write!\" A helping alif and sukūn at the end."},
                {"s": "نَشْرَبُ", "gloss": "drink", "ans": {"vt": "pres"}, "why": "It starts with {ن}: \"we drink\"."},
                {"s": "أَكَلَ", "gloss": "eat", "ans": {"vt": "past"}, "why": "\"He ate\". The {أ} is part of the word. Its present is {يَأْكُلُ}."},
                {"s": "اِجْلِسْ", "gloss": "sit", "ans": {"vt": "ordr"}, "why": "\"Sit!\" An order to one man."},
            ],
        },
        {
            "title": "Who is doing it?",
            "fields": [{"key": "pick", "label": "Who", "options": []}],
            "rows": [
                {"s": "نَكْتُبُ", "ans": {"pick": "a"}, "opts": {"pick": pick("we", "I", "you (m)")},
                 "why": "The first letter {ن} means \"we\"."},
                {"s": "أَذْهَبُ", "ans": {"pick": "b"}, "opts": {"pick": pick("we", "I", "he")},
                 "why": "The first letter {أ} means \"I\"."},
                {"s": "تَجْلِسِينَ", "ans": {"pick": "c"}, "opts": {"pick": pick("she", "you (m pl)", "you (f)")},
                 "why": "{ت} at the start and {ـِينَ} at the end: one woman you speak to."},
                {"s": "يَخْرُجُونَ", "ans": {"pick": "a"}, "opts": {"pick": pick("they (m)", "you (m pl)", "they (f)")},
                 "why": "{ي} at the start and {ـُونَ} at the end: \"they (m)\". \"You (m pl)\" would be {تَخْرُجُونَ}."},
                {"s": "يَدْرُسْنَ", "ans": {"pick": "b"}, "opts": {"pick": pick("they (m)", "they (f)", "you (f pl)")},
                 "why": "{ي} at the start and {ـْنَ} at the end: \"they (f)\". \"You (f pl)\" would be {تَدْرُسْنَ}."},
                {"s": "يَشْرَبَانِ", "ans": {"pick": "c"}, "opts": {"pick": pick("he", "you two", "they two (m)")},
                 "why": "{ي} at the start and {ـَانِ} at the end: two absent men."},
            ],
        },
        {
            "title": "Choose the present form for the pronoun",
            "fields": [{"key": "pick", "label": "Present verb", "options": []}],
            "rows": [
                {"s": "هُوَ + ذَهَبَ", "gloss": "he goes", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَذْهَبُ", "تَذْهَبُ", "ذَهَبَ")}, "why": "{هُوَ} takes {ي}: {يَذْهَبُ}. {ذَهَبَ} is past."},
                {"s": "أَنَا + جَلَسَ", "gloss": "I sit", "ans": {"pick": "b"},
                 "opts": {"pick": pick("نَجْلِسُ", "أَجْلِسُ", "يَجْلِسُ")}, "why": "{أَنَا} takes {أ}: {أَجْلِسُ}."},
                {"s": "نَحْنُ + كَتَبَ", "gloss": "we write", "ans": {"pick": "a"},
                 "opts": {"pick": pick("نَكْتُبُ", "أَكْتُبُ", "كَتَبْنَا")}, "why": "{نَحْنُ} takes {ن}: {نَكْتُبُ}. {كَتَبْنَا} is \"we wrote\"."},
                {"s": "أَنْتِ + خَرَجَ", "gloss": "you (f) go out", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَخْرُجُ", "تَخْرُجْنَ", "تَخْرُجِينَ")}, "why": "One woman: {ت} + {ـِينَ}: {تَخْرُجِينَ}."},
                {"s": "هُمْ + دَرَسَ", "gloss": "they (m) study", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَدْرُسُونَ", "يَدْرُسُونَ", "دَرَسُوا")}, "why": "{هُمْ} takes {ي} + {ـُونَ}: {يَدْرُسُونَ}."},
                {"s": "هُنَّ + كَتَبَ", "gloss": "they (f) write", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَكْتُبْنَ", "يَكْتُبُونَ", "تَكْتُبْنَ")}, "why": "{هُنَّ} takes {ي} + {ـْنَ}: {يَكْتُبْنَ}."},
            ],
        },
        {
            "title": "Flexible or fixed?",
            "fields": [{"key": "st", "label": "Status", "options": [FLEX, FIXD]}],
            "rows": [
                {"s": "يَدْرُسُ", "gloss": "he studies", "ans": {"st": "flex"}, "why": "A present verb with nothing attached: flexible."},
                {"s": "دَرَسَ", "gloss": "he studied", "ans": {"st": "fixd"}, "why": "Every past verb is fixed."},
                {"s": "يَدْرُسْنَ", "gloss": "they (f) study", "ans": {"st": "fixd"}, "why": "The nūn of women makes it fixed on sukūn."},
                {"s": "تَدْرُسِينَ", "gloss": "you (f) study", "ans": {"st": "flex"}, "why": "The {ي} of one woman does not make it fixed. It stays flexible (Unit 3)."},
                {"s": "لَيَدْرُسَنَّ", "gloss": "he will surely study", "ans": {"st": "fixd"}, "why": "The nūn of emphasis makes it fixed on fatha."},
                {"s": "اُدْرُسْ", "gloss": "study!", "ans": {"st": "fixd"}, "why": "Every order verb is fixed."},
            ],
        },
        {
            "title": "Read the case from the ending",
            "fields": [{"key": "case", "label": "Case", "options": [RAF, NASB, JAZM, JARR]}],
            "rows": [
                {"s": "يَكْتُبُ", "gloss": "he writes", "ans": {"case": "raf"}, "why": "No particle, damma at the end: rafʿ."},
                {"s": "لَنْ يَكْتُبَ", "gloss": "he will not write", "ans": {"case": "nasb"}, "why": "{لَنْ} comes first. Fatha at the end: naṣb."},
                {"s": "لَمْ يَكْتُبْ", "gloss": "he did not write", "ans": {"case": "jazm"}, "why": "{لَمْ} comes first. Sukūn at the end: jazm."},
                {"s": "نَذْهَبُ", "gloss": "we go", "ans": {"case": "raf"}, "why": "No particle, damma at the end: rafʿ."},
                {"s": "لَنْ نَذْهَبَ", "gloss": "we will not go", "ans": {"case": "nasb"}, "why": "After {لَنْ}, fatha: naṣb. A verb is never in jarr."},
                {"s": "لَمْ أَجْلِسْ", "gloss": "I did not sit", "ans": {"case": "jazm"}, "why": "After {لَمْ}, sukūn: jazm."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "يَذْهَبُ الطَّالِبُ إِلَى المَسْجِدِ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The student goes to the mosque.", "The student went to the mosque.", "Go to the mosque, student.")},
                 "why": "{يَذْهَبُ} is a present verb: \"goes\"."},
                {"s": "سَيَكْتُبُ المُدَرِّسُ الدَّرْسَ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("The teacher wrote the lesson.", "Write the lesson, teacher.", "The teacher will write the lesson.")},
                 "why": "{سَـ} + present verb: \"will write\"."},
                {"s": "اِشْرَبِ اللَّبَنَ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("He drinks the milk.", "Drink the milk.", "I drink the milk.")},
                 "why": "{اِشْرَبْ} is an order verb. The kasra is only a bridge before {ال}."},
                {"s": "نَدْخُلُ الفَصْلَ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("We enter the classroom.", "I enter the classroom.", "We entered the classroom.")},
                 "why": "{ن} at the start: \"we\". Present: \"enter\"."},
                {"s": "خَرَجَتْ آمِنَةُ مِنَ البَيْتِ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("Aminah goes out of the house.", "Aminah will go out of the house.", "Aminah went out of the house.")},
                 "why": "{خَرَجَتْ} is a past verb: \"went out\"."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Past, present or order?",
            "fields": [{"key": "vt", "label": "Kind of verb", "options": VTYPE}],
            "rows": [
                {"s": "تَعَلَّمَ", "gloss": "learn", "ans": {"vt": "past"}, "why": "\"He learned\". The {ت} is part of the past verb. Its present is {يَتَعَلَّمُ}."},
                {"s": "يَتَعَلَّمُ", "gloss": "learn", "ans": {"vt": "pres"}, "why": "{ي} is added to {تَعَلَّمَ}: \"he learns\"."},
                {"s": "نَزَلَ", "gloss": "go down", "ans": {"vt": "past"}, "why": "\"He went down\". The {ن} is part of the word. Its present is {يَنْزِلُ}."},
                {"s": "أَفْهَمُ", "gloss": "understand", "ans": {"vt": "pres"}, "why": "{أ} is added to {فَهِمَ}: \"I understand\"."},
                {"s": "اُخْرُجْ", "gloss": "go out", "ans": {"vt": "ordr"}, "why": "\"Go out!\" A helping alif and sukūn at the end."},
                {"s": "تَخْرُجُ", "gloss": "go out", "ans": {"vt": "pres"}, "why": "{ت} is added to {خَرَجَ}: \"you go out\" or \"she goes out\"."},
            ],
        },
        {
            "title": "Who is doing it?",
            "fields": [{"key": "pick", "label": "Who", "options": []}],
            "rows": [
                {"s": "تَكْتُبُونَ", "ans": {"pick": "b"}, "opts": {"pick": pick("they (m)", "you (m pl)", "we")},
                 "why": "{ت} at the start and {ـُونَ} at the end: \"you (m pl)\". \"They (m)\" would be {يَكْتُبُونَ}."},
                {"s": "تَدْخُلِينَ", "ans": {"pick": "a"}, "opts": {"pick": pick("you (f)", "she", "they (f)")},
                 "why": "{ـِينَ} at the end: one woman you speak to. \"She\" would be {تَدْخُلُ}."},
                {"s": "نَسْمَعُ", "ans": {"pick": "c"}, "opts": {"pick": pick("I", "they (m)", "we")},
                 "why": "The first letter {ن} means \"we\"."},
                {"s": "أَقْرَأُ", "ans": {"pick": "a"}, "opts": {"pick": pick("I", "he", "we")},
                 "why": "The first letter {أ} means \"I\"."},
                {"s": "يَلْعَبَانِ", "ans": {"pick": "b"}, "opts": {"pick": pick("they (m)", "they two (m)", "you two")},
                 "why": "{ي} at the start and {ـَانِ} at the end: two absent men."},
                {"s": "تَجْلِسْنَ", "ans": {"pick": "c"}, "opts": {"pick": pick("she", "they (f)", "you (f pl)")},
                 "why": "{ت} at the start and {ـْنَ} at the end: \"you (f pl)\". \"They (f)\" would be {يَجْلِسْنَ}."},
            ],
        },
        {
            "title": "Choose the present form for the pronoun",
            "fields": [{"key": "pick", "label": "Present verb", "options": []}],
            "rows": [
                {"s": "أَنْتُمْ + شَرِبَ", "gloss": "you (m pl) drink", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَشْرَبُونَ", "شَرِبْتُمْ", "تَشْرَبُونَ")}, "why": "{أَنْتُمْ} takes {ت} + {ـُونَ}: {تَشْرَبُونَ}. {شَرِبْتُمْ} is past."},
                {"s": "هِيَ + جَلَسَ", "gloss": "she sits", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَجْلِسُ", "يَجْلِسُ", "تَجْلِسِينَ")}, "why": "{هِيَ} takes {ت}: {تَجْلِسُ}. {تَجْلِسِينَ} is \"you (f)\"."},
                {"s": "هُمَا + خَرَجَ", "gloss": "they two (m) go out", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَخْرُجُونَ", "يَخْرُجَانِ", "خَرَجَا")}, "why": "Two absent men: {ي} + {ـَانِ}: {يَخْرُجَانِ}."},
                {"s": "أَنْتُنَّ + كَتَبَ", "gloss": "you (f pl) write", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَكْتُبْنَ", "تَكْتُبْنَ", "تَكْتُبِينَ")}, "why": "{أَنْتُنَّ} takes {ت} + {ـْنَ}: {تَكْتُبْنَ}."},
                {"s": "أَنَا + فَتَحَ", "gloss": "I open", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَفْتَحُ", "فَتَحْتُ", "نَفْتَحُ")}, "why": "{أَنَا} takes {أ}: {أَفْتَحُ}. {فَتَحْتُ} is \"I opened\"."},
                {"s": "أَنْتِ + دَرَسَ", "gloss": "you (f) study", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَدْرُسُ", "دَرَسْتِ", "تَدْرُسِينَ")}, "why": "One woman: {ت} + {ـِينَ}: {تَدْرُسِينَ}."},
            ],
        },
        {
            "title": "Fixed verbs: built on what?",
            "fields": [{"key": "built", "label": "Built on", "options": BUILT}],
            "rows": [
                {"s": "يَكْتُبْنَ", "gloss": "they (f) write", "ans": {"built": "sukun"}, "why": "With the nūn of women the verb is built on sukūn."},
                {"s": "لَأَكْتُبَنَّ", "gloss": "I will surely write", "ans": {"built": "fatha"}, "why": "With the nūn of emphasis the verb is built on fatha."},
                {"s": "كَتَبُوا", "gloss": "they wrote", "ans": {"built": "damma"}, "why": "A past verb with {ـُوا} is built on damma (Stage 3)."},
                {"s": "اِذْهَبْ", "gloss": "go!", "ans": {"built": "sukun"}, "why": "An order to one man is built on sukūn."},
                {"s": "تَكْتُبْنَ", "gloss": "you (f pl) write", "ans": {"built": "sukun"}, "why": "The nūn of women again: built on sukūn."},
                {"s": "لَيَشْرَبَنَّ", "gloss": "he will surely drink", "ans": {"built": "fatha"}, "why": "The nūn of emphasis: built on fatha."},
            ],
        },
        {
            "title": "Read the case from the ending",
            "fields": [{"key": "case", "label": "Case", "options": [RAF, NASB, JAZM, JARR]}],
            "rows": [
                {"s": "تَخْرُجُ", "gloss": "you go out", "ans": {"case": "raf"}, "why": "No particle, damma at the end: rafʿ."},
                {"s": "لَنْ تَخْرُجَ", "gloss": "you will not go out", "ans": {"case": "nasb"}, "why": "After {لَنْ}, fatha: naṣb."},
                {"s": "لَمْ نَشْرَبْ", "gloss": "we did not drink", "ans": {"case": "jazm"}, "why": "After {لَمْ}, sukūn: jazm."},
                {"s": "سَأَفْهَمُ", "gloss": "I will understand", "ans": {"case": "raf"}, "why": "{سَـ} does not change the case. Damma: rafʿ."},
                {"s": "لَنْ أَفْهَمَ", "gloss": "I will not understand", "ans": {"case": "nasb"}, "why": "After {لَنْ}, fatha: naṣb. A verb is never in jarr."},
                {"s": "لَمْ يَفْتَحْ", "gloss": "he did not open", "ans": {"case": "jazm"}, "why": "After {لَمْ}, sukūn: jazm."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "سَوْفَ نَرْجِعُ إِلَى البَيْتِ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("We returned to the house.", "We will return to the house.", "Return to the house.")},
                 "why": "{سَوْفَ} + present verb with {ن}: \"we will return\"."},
                {"s": "تَشْرَبِينَ الحَلِيبَ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("You (f) drink the milk.", "She drinks the milk.", "Drink the milk (f).")},
                 "why": "{ت} + {ـِينَ}: one woman you speak to. \"She\" would be {تَشْرَبُ}."},
                {"s": "أَدْرُسُ النَّحْوَ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("We study grammar.", "I studied grammar.", "I study grammar.")},
                 "why": "{أ} at the start: \"I\". Present: \"study\"."},
                {"s": "اُدْرُسُوا النَّحْوَ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("Study grammar (men).", "They study grammar.", "They studied grammar.")},
                 "why": "{اُدْرُسُوا} is an order verb to a group of men. It has no {أَنَيْتُ} letter at the start."},
                {"s": "يَكْتُبْنَ الدُّرُوسَ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("They (m) write the lessons.", "They (f) write the lessons.", "You (f pl) write the lessons.")},
                 "why": "{ي} + {ـْنَ}: \"they (f)\"."},
            ],
        },
    ],
}
