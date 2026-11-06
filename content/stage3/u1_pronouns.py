# Stage 3, Unit 1: Separate pronouns (الضَّمَائِرُ المُنْفَصِلَةُ)

RAF = {"k": "raf", "label": "Rafʿ · رَفْعٌ", "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ", "color": "pink"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ", "color": "green"}

FIXFLEX = [
    {"k": "fixed", "label": "Fixed · مَبْنِيٌّ"},
    {"k": "flex", "label": "Flexible · مُعْرَبٌ"},
]

JOBS = [
    {"k": "topic", "label": "Topic · مُبْتَدَأٌ", "color": "gold"},
    {"k": "info", "label": "Information · خَبَرٌ", "color": "red"},
    {"k": "prep", "label": "After a preposition", "color": "green"},
    {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"},
]

PERSON = [
    {"k": "p1", "label": "1st · speaker"},
    {"k": "p2", "label": "2nd · listener"},
    {"k": "p3", "label": "3rd · absent"},
]

NUMBER = [
    {"k": "one", "label": "One"},
    {"k": "two", "label": "Two"},
    {"k": "more", "label": "Three or more"},
]

GENDER = [
    {"k": "m", "label": "Masculine (or mixed)", "color": "blue"},
    {"k": "f", "label": "Feminine", "color": "pink"},
    {"k": "both", "label": "Either"},
]

SHOW = [
    {"k": "ending", "label": "On its ending (damma)", "color": "red"},
    {"k": "place", "label": "Only its place (fixed word)", "color": "blue"},
]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abc", labels)]


UNIT = {
    "id": "s3-pronouns",
    "order": 1,
    "title": "Separate pronouns",
    "ar": "الضَّمَائِرُ المُنْفَصِلَةُ",
    "blurb": "The twelve words for I, you, he, she, we and they. Their ending never changes, but they still have a job.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 3 · UNIT 1", "title": "Twelve words you will see every day",
         "text": "Stage 3 is about fixed words. We start with the pronouns: {أَنَا}، {هُوَ}، {هِيَ}، {نَحْنُ} and their friends.",
         "wm": "الضَّمَائِرُ"},

        {"t": "h2", "text": "Why we learn fixed words now"},
        {"t": "p", "text": "Fixed words are in almost every sentence. Pronouns, words like {هَذَا}, and question words come again and again."},
        {"t": "p", "text": "Their ending never changes. So you learn each one once, as a word in a table, and you know it for good."},
        {"t": "p", "text": "When you know them, every later example is easier. You see the fixed words at once and look only at the flexible ones."},
        {"t": "words", "items": [
            {"ar": "أَنَا", "sub": "I", "color": "blue"},
            {"ar": "هُوَ", "sub": "he, it", "color": "blue"},
            {"ar": "هِيَ", "sub": "she, it", "color": "blue"},
            {"ar": "نَحْنُ", "sub": "we", "color": "blue"},
        ]},

        {"t": "h2", "text": "Fixed and flexible: a quick recap"},
        {"t": "cols", "items": [
            {"color": "grey", "title": "Fixed", "ar": "مَبْنِيٌّ",
             "text": "The ending never changes: {هُوَ} is always {هُوَ}."},
            {"color": "blue", "title": "Flexible", "ar": "مُعْرَبٌ",
             "text": "The ending changes with the job: {البَيْتُ}، {البَيْتِ}."},
        ]},

        {"t": "h2", "text": "The twelve separate pronouns"},
        {"t": "p", "text": "Learn this table by heart. Read it aloud, top to bottom, every day this week."},
        {"t": "table", "head": ["Person", "Number", "Gender", "Arabic", "English"], "rows": [
            ["1st", "one", "m or f", "أَنَا", "I"],
            ["1st", "two or more", "m or f", "نَحْنُ", "we"],
            ["2nd", "one", "m", "أَنْتَ", "you (one man)"],
            ["2nd", "one", "f", "أَنْتِ", "you (one woman)"],
            ["2nd", "two", "m or f", "أَنْتُمَا", "you (two)"],
            ["2nd", "three or more", "m or mixed", "أَنْتُمْ", "you (men, or men and women)"],
            ["2nd", "three or more", "f", "أَنْتُنَّ", "you (women)"],
            ["3rd", "one", "m", "هُوَ", "he, it"],
            ["3rd", "one", "f", "هِيَ", "she, it"],
            ["3rd", "two", "m or f", "هُمَا", "they (two)"],
            ["3rd", "three or more", "m or mixed", "هُمْ", "they (men, or men and women)"],
            ["3rd", "three or more", "f", "هُنَّ", "they (women)"],
        ]},
        {"t": "tip", "text": "Watch the small vowels: {أَنْتَ} for a man, {أَنْتِ} for a woman. {هُمْ} for men, {هُنَّ} for women, with a shadda."},
        {"t": "tip", "text": "Side note: each pronoun is built on one fixed mark. {هُوَ} is built on fatha, {نَحْنُ} on damma, {هُمْ} on sukūn. You do not need to learn these. Just remember the word never changes."},

        {"t": "h2", "text": "Three groups"},
        {"t": "cols", "items": [
            {"color": "blue", "title": "1st person: the speaker", "ar": "المُتَكَلِّمُ",
             "text": "{أَنَا}، {نَحْنُ}"},
            {"color": "blue", "title": "2nd person: the listener", "ar": "المُخَاطَبُ",
             "text": "{أَنْتَ}، {أَنْتِ}، {أَنْتُمَا}، {أَنْتُمْ}، {أَنْتُنَّ}"},
            {"color": "blue", "title": "3rd person: the absent one", "ar": "الغَائِبُ",
             "text": "{هُوَ}، {هِيَ}، {هُمَا}، {هُمْ}، {هُنَّ}"},
        ]},
        {"t": "tip", "text": "{هُوَ} and {هِيَ} are also used for things. A masculine noun is {هُوَ}, a feminine noun is {هِيَ}: {أَيْنَ السَّاعَةُ؟ هِيَ عَلَى السَّرِيرِ}."},
        {"t": "tip", "text": "For two people, men or women, there is one word: {أَنْتُمَا} or {هُمَا}. For a group of men and women together, use {أَنْتُمْ} and {هُمْ}."},

        {"t": "h2", "text": "A fixed word still has a job"},
        {"t": "p", "text": "A pronoun never changes its last vowel to show rafʿ, naṣb or jarr. But it still does a job in the sentence, like any noun."},
        {"t": "rule", "color": "red", "title": "The place of rafʿ",
         "text": "In {هُوَ طَالِبٌ}, {هُوَ} is the Topic. A Topic is rafʿ. {هُوَ} cannot show a damma, so we say it is in the place of rafʿ: {فِي مَحَلِّ رَفْعٍ}."},
        {"t": "p", "text": "So we describe a fixed word in two steps: first its job, then its place."},
        {"t": "table", "head": ["Word", "Job", "Ending", "Rafʿ, naṣb or jarr"], "rows": [
            ["{هُوَ}", "Topic", "fixed, never changes", "in the place of rafʿ"],
            ["{طَالِبٌ}", "Information", "damma, you can see it", "rafʿ"],
        ]},
        {"t": "tip", "text": "There are three places: {فِي مَحَلِّ رَفْعٍ}، {فِي مَحَلِّ نَصْبٍ}، {فِي مَحَلِّ جَرٍّ}. In this stage, these twelve pronouns are always in the place of rafʿ."},

        {"t": "h2", "text": "Sentences with a pronoun"},
        {"t": "p", "text": "Here the pronoun is the Topic. The Information is a noun or a place phrase."},
        {"t": "examples", "items": [
            {"ar": "أَنَا طَالِبٌ.", "en": "I am a student.",
             "note": "{أَنَا} is the Topic, in the place of rafʿ. {طَالِبٌ} is the Information, rafʿ with damma."},
            {"ar": "هِيَ مُدَرِّسَةٌ.", "en": "She is a teacher.",
             "note": "{هِيَ} is the Topic, in the place of rafʿ."},
            {"ar": "نَحْنُ فِي الفَصْلِ.", "en": "We are in the classroom.",
             "note": "{نَحْنُ} is the Topic. {الفَصْلِ} is jarr after {فِي}."},
            {"ar": "هُمْ فِي المَسْجِدِ.", "en": "They are in the mosque.",
             "note": "{هُمْ} is the Topic, in the place of rafʿ."},
            {"ar": "أَنْتُمَا فِي البَيْتِ.", "en": "You two are in the house.",
             "note": "{أَنْتُمَا} is the Topic, in the place of rafʿ."},
            {"ar": "أَيْنَ الوَلَدُ؟ هُوَ فِي المَسْجِدِ.", "en": "Where is the boy? He is in the mosque.",
             "note": "Madinah lesson 4. {هُوَ} takes the place of {الوَلَدُ}."},
        ]},
        {"t": "tip", "text": "A pronoun can replace a noun: {الطَّالِبُ فِي الفَصْلِ} becomes {هُوَ فِي الفَصْلِ}. Pick the pronoun by number and gender."},

        {"t": "summary", "title": "In short", "items": [
            "Fixed words are in every sentence. Learn them once, as a table.",
            "There are twelve separate pronouns: {أَنَا}، {نَحْنُ}، {أَنْتَ}، {أَنْتِ}، {أَنْتُمَا}، {أَنْتُمْ}، {أَنْتُنَّ}، {هُوَ}، {هِيَ}، {هُمَا}، {هُمْ}، {هُنَّ}.",
            "Choose by person (speaker, listener, absent), number (one, two, more) and gender.",
            "A pronoun never changes its ending, but it still has a job.",
            "As the Topic it is in the place of rafʿ: {فِي مَحَلِّ رَفْعٍ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Which pronoun?",
            "fields": [{"key": "pick", "label": "Pronoun", "options": []}],
            "rows": [
                {"s": "I", "ans": {"pick": "a"}, "opts": {"pick": pick("أَنَا", "نَحْنُ", "أَنْتَ")},
                 "why": "The speaker alone is {أَنَا}."},
                {"s": "you (two people)", "ans": {"pick": "b"}, "opts": {"pick": pick("أَنْتُمْ", "أَنْتُمَا", "هُمَا")},
                 "why": "Two listeners: {أَنْتُمَا}. {هُمَا} is for two people who are absent."},
                {"s": "she", "ans": {"pick": "b"}, "opts": {"pick": pick("هُوَ", "هِيَ", "هُنَّ")},
                 "why": "One absent woman: {هِيَ}."},
                {"s": "you (one woman)", "ans": {"pick": "b"}, "opts": {"pick": pick("أَنْتَ", "أَنْتِ", "أَنْتُنَّ")},
                 "why": "One woman: {أَنْتِ}, with kasra on the {ت}."},
                {"s": "they (three men)", "ans": {"pick": "a"}, "opts": {"pick": pick("هُمْ", "هُنَّ", "هُمَا")},
                 "why": "Three or more men: {هُمْ}."},
                {"s": "we", "ans": {"pick": "b"}, "opts": {"pick": pick("أَنَا", "نَحْنُ", "هُمْ")},
                 "why": "The speaker with others: {نَحْنُ}."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "هُوَ", "ans": {"pick": "c"}, "opts": {"pick": pick("she", "they (two)", "he, it")},
                 "why": "{هُوَ} is one absent male, or a masculine thing."},
                {"s": "أَنْتُمْ", "ans": {"pick": "a"}, "opts": {"pick": pick("you (three or more men)", "you (two)", "they (men)")},
                 "why": "{أَنْتُمْ} talks to a group of men, or men and women."},
                {"s": "هُنَّ", "ans": {"pick": "b"}, "opts": {"pick": pick("they (men)", "they (women)", "you (women)")},
                 "why": "{هُنَّ} is for three or more absent women."},
                {"s": "أَنْتَ", "ans": {"pick": "a"}, "opts": {"pick": pick("you (one man)", "you (one woman)", "I")},
                 "why": "Fatha on the {ت}: one man."},
                {"s": "هُمَا", "ans": {"pick": "c"}, "opts": {"pick": pick("they (men)", "you (two)", "they (two)")},
                 "why": "{هُمَا} is for two absent people."},
                {"s": "نَحْنُ", "ans": {"pick": "b"}, "opts": {"pick": pick("I", "we", "they")},
                 "why": "{نَحْنُ} means we."},
            ],
        },
        {
            "title": "Fixed or flexible?",
            "fields": [{"key": "type", "label": "Type", "options": FIXFLEX}],
            "rows": [
                {"s": "أَنْتُمَا", "gloss": "you (two)", "ans": {"type": "fixed"}, "why": "A pronoun. It never changes."},
                {"s": "الطَّالِبُ", "gloss": "the student", "ans": {"type": "flex"}, "why": "A noun. After {فِي} it becomes {الطَّالِبِ}."},
                {"s": "هُنَّ", "gloss": "they (women)", "ans": {"type": "fixed"}, "why": "A pronoun. It is always {هُنَّ}."},
                {"s": "مُدَرِّسَةٌ", "gloss": "a teacher (f)", "ans": {"type": "flex"}, "why": "A noun. It can become {مُدَرِّسَةٍ}."},
                {"s": "نَحْنُ", "gloss": "we", "ans": {"type": "fixed"}, "why": "A pronoun. It always ends in damma."},
                {"s": "عَلَى", "gloss": "on", "ans": {"type": "fixed"}, "why": "A ḥarf. Ḥarfs never change."},
            ],
        },
        {
            "title": "Replace the word in [ ] with a pronoun",
            "fields": [{"key": "pick", "label": "Pronoun", "options": []}],
            "rows": [
                {"s": "[الطَّالِبُ] فِي الفَصْلِ", "gloss": "The student is in the classroom.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("هُوَ", "هِيَ", "هُمْ")}, "why": "One male student: {هُوَ فِي الفَصْلِ}."},
                {"s": "[السَّاعَةُ] عَلَى السَّرِيرِ", "gloss": "The watch is on the bed.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هُوَ", "هِيَ", "أَنْتِ")}, "why": "{السَّاعَةُ} is feminine: {هِيَ عَلَى السَّرِيرِ}."},
                {"s": "[الكِتَابُ] عَلَى المَكْتَبِ", "gloss": "The book is on the desk.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("هُوَ", "هِيَ", "أَنْتَ")}, "why": "{الكِتَابُ} is masculine: {هُوَ عَلَى المَكْتَبِ}."},
                {"s": "[الرِّجَالُ] فِي المَسْجِدِ", "gloss": "The men are in the mosque.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هُمَا", "هُمْ", "هُنَّ")}, "why": "Many men: {هُمْ فِي المَسْجِدِ}."},
                {"s": "[آمِنَةُ] فِي المَطْبَخِ", "gloss": "Aminah is in the kitchen.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("هُوَ", "أَنْتِ", "هِيَ")}, "why": "One absent woman: {هِيَ فِي المَطْبَخِ}."},
                {"s": "[مُحَمَّدٌ وَخَالِدٌ] فِي الغُرْفَةِ", "gloss": "Muhammad and Khalid are in the room.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هُمْ", "هُمَا", "نَحْنُ")}, "why": "Two people: {هُمَا فِي الغُرْفَةِ}."},
            ],
        },
        {
            "title": "Job, and rafʿ, naṣb or jarr, of the word in [ ]",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "case", "label": "Rafʿ, naṣb or jarr", "options": [RAF, NASB, JARR]},
            ],
            "rows": [
                {"s": "[هُوَ] طَالِبٌ", "gloss": "He is a student.", "ans": {"job": "topic", "case": "raf"},
                 "why": "{هُوَ} is the Topic. It is fixed, so it is in the place of rafʿ."},
                {"s": "هِيَ [مُدَرِّسَةٌ]", "gloss": "She is a teacher.", "ans": {"job": "info", "case": "raf"},
                 "why": "{مُدَرِّسَةٌ} tells us about her. Information, rafʿ, and you can see the damma."},
                {"s": "[نَحْنُ] فِي الفَصْلِ", "gloss": "We are in the classroom.", "ans": {"job": "topic", "case": "raf"},
                 "why": "{نَحْنُ} is the Topic, in the place of rafʿ."},
                {"s": "هُمْ فِي [المَسْجِدِ]", "gloss": "They are in the mosque.", "ans": {"job": "prep", "case": "jarr"},
                 "why": "{المَسْجِدِ} comes after {فِي}. Jarr with kasra."},
                {"s": "[أَنَا] مِنَ الهِنْدِ", "gloss": "I am from India.", "ans": {"job": "topic", "case": "raf"},
                 "why": "{أَنَا} is the Topic, in the place of rafʿ."},
            ],
        },
        {
            "title": "Person and number",
            "fields": [
                {"key": "person", "label": "Person", "options": PERSON},
                {"key": "number", "label": "Number", "options": NUMBER},
            ],
            "rows": [
                {"s": "أَنْتُمَا", "ans": {"person": "p2", "number": "two"}, "why": "{أَنْتُمَا}: you, two listeners."},
                {"s": "هُمْ", "ans": {"person": "p3", "number": "more"}, "why": "{هُمْ}: they, three or more."},
                {"s": "أَنَا", "ans": {"person": "p1", "number": "one"}, "why": "{أَنَا}: the speaker alone."},
                {"s": "هِيَ", "ans": {"person": "p3", "number": "one"}, "why": "{هِيَ}: one absent woman, or a feminine thing."},
                {"s": "أَنْتُنَّ", "ans": {"person": "p2", "number": "more"}, "why": "{أَنْتُنَّ}: you, three or more women."},
                {"s": "هُمَا", "ans": {"person": "p3", "number": "two"}, "why": "{هُمَا}: two absent people."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Which pronoun?",
            "fields": [{"key": "pick", "label": "Pronoun", "options": []}],
            "rows": [
                {"s": "you (three women)", "ans": {"pick": "b"}, "opts": {"pick": pick("أَنْتُمْ", "أَنْتُنَّ", "هُنَّ")},
                 "why": "Talking to women: {أَنْتُنَّ}. {هُنَّ} is for women who are absent."},
                {"s": "they (two women)", "ans": {"pick": "a"}, "opts": {"pick": pick("هُمَا", "هُنَّ", "أَنْتُمَا")},
                 "why": "Two absent people, men or women: {هُمَا}."},
                {"s": "you (one man)", "ans": {"pick": "a"}, "opts": {"pick": pick("أَنْتَ", "أَنْتِ", "أَنَا")},
                 "why": "One man: {أَنْتَ}, with fatha on the {ت}."},
                {"s": "they (three women)", "ans": {"pick": "b"}, "opts": {"pick": pick("هُمْ", "هُنَّ", "أَنْتُنَّ")},
                 "why": "Absent women: {هُنَّ}."},
                {"s": "you (a group of men and women)", "ans": {"pick": "a"}, "opts": {"pick": pick("أَنْتُمْ", "أَنْتُنَّ", "هُمْ")},
                 "why": "A mixed group takes the masculine form: {أَنْتُمْ}."},
                {"s": "it (the door)", "ans": {"pick": "a"}, "opts": {"pick": pick("هُوَ", "هِيَ", "هُمْ")},
                 "why": "{البَابُ} is masculine, so it is {هُوَ}."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "أَنْتِ", "ans": {"pick": "b"}, "opts": {"pick": pick("you (one man)", "you (one woman)", "she")},
                 "why": "Kasra on the {ت}: one woman."},
                {"s": "أَنْتُمَا", "ans": {"pick": "c"}, "opts": {"pick": pick("they (two)", "you (three or more men)", "you (two)")},
                 "why": "{أَنْتُمَا} talks to two people."},
                {"s": "هِيَ", "ans": {"pick": "a"}, "opts": {"pick": pick("she, it", "he, it", "they (women)")},
                 "why": "{هِيَ} is one absent woman, or a feminine thing."},
                {"s": "أَنْتُنَّ", "ans": {"pick": "b"}, "opts": {"pick": pick("they (women)", "you (women)", "you (men)")},
                 "why": "{أَنْتُنَّ} talks to three or more women."},
                {"s": "أَنَا", "ans": {"pick": "c"}, "opts": {"pick": pick("we", "you (one man)", "I")},
                 "why": "{أَنَا} means I."},
                {"s": "هُمْ", "ans": {"pick": "a"}, "opts": {"pick": pick("they (men, or men and women)", "they (two)", "you (men)")},
                 "why": "{هُمْ} is for three or more absent men, or a mixed group."},
            ],
        },
        {
            "title": "Replace the words in [ ] with a pronoun",
            "fields": [{"key": "pick", "label": "Pronoun", "options": []}],
            "rows": [
                {"s": "[المُدَرِّسَةُ] فِي الفَصْلِ", "gloss": "The teacher (f) is in the classroom.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("هُوَ", "أَنْتِ", "هِيَ")}, "why": "One woman, absent: {هِيَ فِي الفَصْلِ}."},
                {"s": "[الطُّلَّابُ] فِي الجَامِعَةِ", "gloss": "The students are in the university.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("هُمْ", "هُوَ", "هُمَا")}, "why": "Many male students: {هُمْ فِي الجَامِعَةِ}."},
                {"s": "[البَابُ] مَفْتُوحٌ", "gloss": "The door is open.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هِيَ", "هُوَ", "أَنْتَ")}, "why": "{البَابُ} is masculine: {هُوَ مَفْتُوحٌ}."},
                {"s": "[فَاطِمَةُ وَزَيْنَبُ] فِي البَيْتِ", "gloss": "Fatimah and Zaynab are in the house.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هُنَّ", "هُمَا", "أَنْتُمَا")}, "why": "Two women, absent: {هُمَا}. {هُنَّ} needs three or more."},
                {"s": "[السَّيَّارَةُ] فِي الشَّارِعِ", "gloss": "The car is in the street.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هُوَ", "هِيَ", "أَنْتِ")}, "why": "{السَّيَّارَةُ} is feminine: {هِيَ فِي الشَّارِعِ}."},
                {"s": "[أَنَا وَخَالِدٌ] فِي المَسْجِدِ", "gloss": "Khalid and I are in the mosque.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هُمَا", "نَحْنُ", "أَنْتُمَا")}, "why": "The speaker is in the group, so it is {نَحْنُ}."},
            ],
        },
        {
            "title": "Number and gender",
            "fields": [
                {"key": "number", "label": "Number", "options": NUMBER},
                {"key": "gender", "label": "Gender", "options": GENDER},
            ],
            "rows": [
                {"s": "أَنْتُنَّ", "ans": {"number": "more", "gender": "f"}, "why": "{أَنْتُنَّ}: three or more women."},
                {"s": "هُمَا", "ans": {"number": "two", "gender": "both"}, "why": "{هُمَا} is used for two men or two women."},
                {"s": "أَنْتِ", "ans": {"number": "one", "gender": "f"}, "why": "{أَنْتِ}: one woman."},
                {"s": "هُمْ", "ans": {"number": "more", "gender": "m"}, "why": "{هُمْ}: three or more men, or a mixed group."},
                {"s": "أَنْتَ", "ans": {"number": "one", "gender": "m"}, "why": "{أَنْتَ}: one man."},
                {"s": "أَنْتُمَا", "ans": {"number": "two", "gender": "both"}, "why": "{أَنْتُمَا} is used for two men or two women."},
            ],
        },
        {
            "title": "Job, and rafʿ, naṣb or jarr, of the word in [ ]",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "case", "label": "Rafʿ, naṣb or jarr", "options": [RAF, NASB, JARR]},
            ],
            "rows": [
                {"s": "[أَنْتُمْ] طُلَّابٌ", "gloss": "You are students.", "ans": {"job": "topic", "case": "raf"},
                 "why": "{أَنْتُمْ} is the Topic. It is fixed, so it is in the place of rafʿ."},
                {"s": "هُوَ [ابْنُ] المُدَرِّسِ", "gloss": "He is the teacher's son.", "ans": {"job": "info", "case": "raf"},
                 "why": "{ابْنُ} tells us about him. Information, rafʿ with damma."},
                {"s": "هُوَ ابْنُ [المُدَرِّسِ]", "gloss": "He is the teacher's son.", "ans": {"job": "owner", "case": "jarr"},
                 "why": "The son belongs to the teacher. Owner, jarr with kasra."},
                {"s": "[هُنَّ] فِي الغُرْفَةِ", "gloss": "They (women) are in the room.", "ans": {"job": "topic", "case": "raf"},
                 "why": "{هُنَّ} is the Topic, in the place of rafʿ."},
                {"s": "أَنْتِ مِنَ [الصِّينِ]", "gloss": "You (f) are from China.", "ans": {"job": "prep", "case": "jarr"},
                 "why": "{الصِّينِ} comes after {مِنْ}. Jarr with kasra."},
                {"s": "[أَنْتُمَا] فِي السُّوقِ", "gloss": "You two are in the market.", "ans": {"job": "topic", "case": "raf"},
                 "why": "{أَنْتُمَا} is the Topic, in the place of rafʿ."},
            ],
        },
        {
            "title": "Rafʿ: on the ending, or only its place?",
            "fields": [{"key": "show", "label": "How it is rafʿ", "options": SHOW}],
            "rows": [
                {"s": "[هُوَ] مَرِيضٌ", "gloss": "He is sick.", "ans": {"show": "place"},
                 "why": "{هُوَ} is fixed. It is in the place of rafʿ."},
                {"s": "هُوَ [مَرِيضٌ]", "gloss": "He is sick.", "ans": {"show": "ending"},
                 "why": "{مَرِيضٌ} is flexible. Its tanween damma shows rafʿ."},
                {"s": "نَحْنُ [رِجَالٌ]", "gloss": "We are men.", "ans": {"show": "ending"},
                 "why": "{رِجَالٌ} is a noun. You can see the damma."},
                {"s": "[هُمْ] فِي المَسْجِدِ", "gloss": "They are in the mosque.", "ans": {"show": "place"},
                 "why": "{هُمْ} ends in sukūn and never changes. It is in the place of rafʿ."},
                {"s": "[الوَلَدُ] فِي البَيْتِ", "gloss": "The boy is in the house.", "ans": {"show": "ending"},
                 "why": "{الوَلَدُ} is a noun. Its damma shows rafʿ."},
                {"s": "[أَنْتُنَّ] فِي الفَصْلِ", "gloss": "You (women) are in the classroom.", "ans": {"show": "place"},
                 "why": "{أَنْتُنَّ} is fixed. It is in the place of rafʿ."},
            ],
        },
    ],
}
