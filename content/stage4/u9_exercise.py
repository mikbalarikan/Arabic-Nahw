# Stage 4: class exercise (review of units 1-8, done together in class before the Stage 4 quiz)


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abc", labels)]


GROUPS = [
    {"k": "sing", "label": "Singular · مُفْرَدٌ", "color": "grey"},
    {"k": "dual", "label": "Dual · مُثَنًّى", "color": "teal"},
    {"k": "smp", "label": "Sound m. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ", "color": "blue"},
    {"k": "sfp", "label": "Sound f. plural · جَمْعُ مُؤَنَّثٍ سَالِمٌ", "color": "pink"},
    {"k": "brk", "label": "Broken plural · جَمْعُ تَكْسِيرٍ", "color": "purple"},
]

ALSO = [
    {"k": "none", "label": "None of these"},
    {"k": "dip", "label": "Diptote · مَمْنُوعٌ مِنَ الصَّرْفِ", "color": "orange"},
    {"k": "five", "label": "Five nouns · الأَسْمَاءُ الخَمْسَةُ", "color": "gold"},
    {"k": "hid", "label": "Hidden vowel", "color": "brown"},
]

NUMBER = [
    {"k": "one", "label": "One", "color": "grey"},
    {"k": "two", "label": "Two", "color": "teal"},
    {"k": "many", "label": "Three or more"},
]

SIGNS = [
    {"k": "orig", "label": "Original signs only · العَلَامَاتُ الأَصْلِيَّةُ", "color": "green"},
    {"k": "branch", "label": "Uses branch signs · عَلَامَاتٌ فَرْعِيَّةٌ", "color": "red"},
]

PATTERNS = [
    {"k": "fuul", "label": "فُعُولٌ", "color": "purple"},
    {"k": "afal", "label": "أَفْعَالٌ", "color": "purple"},
    {"k": "fial", "label": "فِعَالٌ", "color": "purple"},
    {"k": "fuul2", "label": "فُعُلٌ", "color": "purple"},
    {"k": "fuaal", "label": "فُعَّالٌ", "color": "purple"},
    {"k": "dip", "label": "مَفَاعِلُ / مَفَاعِيلُ / فُعَلَاءُ (diptote)", "color": "orange"},
]

FIVE = [
    {"k": "five", "label": "Special five-noun signs", "color": "gold"},
    {"k": "orig", "label": "Original signs", "color": "green"},
    {"k": "hid", "label": "Hidden vowel (with ـي)", "color": "brown"},
]

HIDDEN = [
    {"k": "maq", "label": "Maqṣūr · المَقْصُورُ", "color": "brown"},
    {"k": "manq", "label": "Manqūṣ · المَنْقُوصُ", "color": "brown"},
    {"k": "ya", "label": "Noun + ـي (\"my\")", "color": "brown"},
    {"k": "mamd", "label": "Mamdūd · المَمْدُودُ", "color": "olive"},
]


UNIT = {
    "id": "s4-exercise",
    "order": 9,
    "kind": "exercise",
    "title": "Stage 4 class exercise",
    "ar": "تَمْرِينُ أَقْسَامِ الأَسْمَاءِ",
    "blurb": "Ten mixed cards on all eight kinds of nouns, done together in class before the Stage 4 quiz.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 4 · CLASS EXERCISE", "title": "All the kinds of nouns together",
         "text": "Ten cards that mix every Stage 4 unit. We do them together in class, before the Stage 4 quiz.",
         "wm": "أَقْسَامُ الأَسْمَاءِ"},

        {"t": "h2", "text": "How we do it in class"},
        {"t": "p", "text": "Work in pairs, or come to the board. One student reads the word aloud and names its group. The partner says why, or corrects it. Then swap for the next row."},
        {"t": "tip", "text": "Ask two questions for every noun. How many? One, two, or three or more. Then: is it in a special group? Diptote, five nouns, or hidden vowel."},
        {"t": "tip", "text": "If a card is hard, open its unit and read the table again before the quiz."},

        {"t": "h2", "text": "The eight topics"},
        {"t": "cols", "items": [
            {"color": "grey", "title": "1. The map", "ar": "المُفْرَدُ",
             "text": "One, two, or three or more. Some groups use original signs, some use branch signs."},
            {"color": "teal", "title": "2. Dual", "ar": "المُثَنَّى",
             "text": "{ـَانِ} / {ـَيْنِ}. {ة} becomes {ت}: {مُدَرِّسَتَانِ}. {إِنْسَانٌ} only looks like one."},
            {"color": "blue", "title": "3. Sound m. plural", "ar": "جَمْعُ المُذَكَّرِ السَّالِمُ",
             "text": "{ـُونَ} / {ـِينَ}, for male persons: {مُسْلِمُونَ}. {زَيْتُونٌ} only looks like one."},
            {"color": "pink", "title": "4. Sound f. plural", "ar": "جَمْعُ المُؤَنَّثِ السَّالِمُ",
             "text": "Drop {ة}, add {ـَاتٌ}: {مُدَرِّسَاتٌ}. {أَصْوَاتٌ} is broken."},
            {"color": "purple", "title": "5. Broken plural", "ar": "جَمْعُ التَّكْسِيرِ",
             "text": "The singular's shape changes: {فُعُولٌ}، {أَفْعَالٌ}، {فِعَالٌ}، {فُعُلٌ}، {فُعَّالٌ}، {مَفَاعِلُ}."},
            {"color": "orange", "title": "6. Diptote", "ar": "المَمْنُوعُ مِنَ الصَّرْفِ",
             "text": "No tanween. In jarr it takes fatha, unless it has {ال} or is owned."},
            {"color": "gold", "title": "7. Five nouns", "ar": "الأَسْمَاءُ الخَمْسَةُ",
             "text": "{أَبٌ}، {أَخٌ}، {حَمٌ}، {فُو}، {ذُو}. Special only when owned, and not by {ـي}."},
            {"color": "brown", "title": "8. Hidden vowel", "ar": "المَقْصُورُ وَالمَنْقُوصُ",
             "text": "{الفَتَى} hides every vowel. {القَاضِي} shows only fatha. {سَمَاءٌ} shows them all."},
        ]},

        {"t": "summary", "title": "Remember", "items": [
            "Most singulars and broken plurals use the original signs: damma, fatha, kasra. Diptotes and the five nouns are the exceptions.",
            "Duals and sound plurals use branch signs: letters, or kasra in place of fatha.",
            "An ending can trick you. Find the singular first: {إِنْسَانٌ}، {زَيْتُونٌ}، {أَوْقَاتٌ}.",
            "A diptote never takes tanween: {أَحْمَدُ}، {مَسَاجِدُ}، {صَحْرَاءُ}.",
            "A five noun is special only when it is owned by something other than {ـي}: {أَبُوكَ}.",
        ]},
    ],

    "practice": [
        # 1 · unit 1: the map, singular, original vs branch signs
        {
            "title": "How many, and which signs?",
            "fields": [
                {"key": "num", "label": "How many?", "options": NUMBER},
                {"key": "signs", "label": "Signs", "options": SIGNS},
            ],
            "rows": [
                {"s": "بَيْتٌ", "gloss": "a house", "ans": {"num": "one", "signs": "orig"},
                 "why": "One house. A singular takes the original signs: damma, fatha, kasra."},
                {"s": "قَلَمَانِ", "gloss": "two pens", "ans": {"num": "two", "signs": "branch"},
                 "why": "A dual. It shows iʿrāb with letters: {ـَانِ} / {ـَيْنِ}. These are branch signs."},
                {"s": "مُوَظَّفُونَ", "gloss": "employees (men)", "ans": {"num": "many", "signs": "branch"},
                 "why": "A sound masculine plural. It uses letters: {ـُونَ} / {ـِينَ}. Branch signs."},
                {"s": "أَوْلَادٌ", "gloss": "boys", "ans": {"num": "many", "signs": "orig"},
                 "why": "A broken plural of {وَلَدٌ}. It takes damma, fatha, kasra like a singular."},
                {"s": "طَالِبَاتٌ", "gloss": "students (women)", "ans": {"num": "many", "signs": "branch"},
                 "why": "A sound feminine plural. In naṣb it takes kasra in place of fatha. That is a branch sign."},
            ],
        },
        # 2 · unit 2: dual
        {
            "title": "Real dual, or does it only look like one?",
            "fields": [{"key": "grp", "label": "Group", "options": [
                {"k": "dual", "label": "Real dual · مُثَنًّى", "color": "teal"},
                {"k": "sing", "label": "Singular · مُفْرَدٌ", "color": "grey"},
            ]}],
            "rows": [
                {"s": "رَجُلَانِ", "gloss": "two men", "ans": {"grp": "dual"},
                 "why": "{رَجُلٌ} + {ـَانِ}. Two men."},
                {"s": "إِنْسَانٌ", "gloss": "a human being", "ans": {"grp": "sing"},
                 "why": "One person. The {ـَانٌ} is part of the word, and it has tanween. A dual ends in {ـَانِ} with kasra."},
                {"s": "بَابَيْنِ", "gloss": "two doors", "ans": {"grp": "dual"},
                 "why": "{بَابٌ} + {ـَيْنِ}. This is the dual's other shape. We use it in Stages 6 and 7."},
                {"s": "عُثْمَانُ", "gloss": "Uthman (a name)", "ans": {"grp": "sing"},
                 "why": "The name of one man. The {ـَانُ} is part of the name."},
                {"s": "حَقِيبَتَانِ", "gloss": "two bags", "ans": {"grp": "dual"},
                 "why": "{حَقِيبَةٌ}: the {ة} becomes {ت}, then add {ـَانِ}."},
            ],
        },
        # 3 · unit 3: sound masculine plural
        {
            "title": "Sound masculine plural, singular or broken plural?",
            "fields": [{"key": "grp", "label": "Group", "options": [
                {"k": "smp", "label": "Sound m. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ", "color": "blue"},
                {"k": "sing", "label": "Singular · مُفْرَدٌ", "color": "grey"},
                {"k": "brk", "label": "Broken plural · جَمْعُ تَكْسِيرٍ", "color": "purple"},
            ]}],
            "rows": [
                {"s": "مُسْلِمُونَ", "gloss": "Muslims (men)", "ans": {"grp": "smp"},
                 "why": "{مُسْلِمٌ} + {ـُونَ}. The singular stays whole."},
                {"s": "زَيْتُونٌ", "gloss": "olives", "ans": {"grp": "sing"},
                 "why": "A fruit, not people. The {ـُونٌ} is part of the word, and it has tanween."},
                {"s": "فَلَّاحُونَ", "gloss": "farmers (men)", "ans": {"grp": "smp"},
                 "why": "{فَلَّاحٌ} + {ـُونَ}. Male persons."},
                {"s": "مِسْكِينٌ", "gloss": "a poor man", "ans": {"grp": "sing"},
                 "why": "One person. The {ـِينٌ} is part of the word, and it has tanween."},
                {"s": "مُدَرِّسِينَ", "gloss": "teachers (men)", "ans": {"grp": "smp"},
                 "why": "{مُدَرِّسٌ} + {ـِينَ}. This is the other shape of {مُدَرِّسُونَ}."},
                {"s": "مَسَاكِينُ", "gloss": "poor people", "ans": {"grp": "brk"},
                 "why": "The plural of {مِسْكِينٌ}. The shape of the singular is broken. Pattern {مَفَاعِيلُ}."},
            ],
        },
        # 4 · unit 4: sound feminine plural
        {
            "title": "Sound feminine plural or broken plural?",
            "fields": [{"key": "grp", "label": "Group", "options": [
                {"k": "sfp", "label": "Sound f. plural · جَمْعُ مُؤَنَّثٍ سَالِمٌ", "color": "pink"},
                {"k": "brk", "label": "Broken plural · جَمْعُ تَكْسِيرٍ", "color": "purple"},
            ]}],
            "rows": [
                {"s": "مُدَرِّسَاتٌ", "gloss": "teachers (women)", "ans": {"grp": "sfp"},
                 "why": "{مُدَرِّسَةٌ}: drop the {ة}, add {ـَاتٌ}."},
                {"s": "أَصْوَاتٌ", "gloss": "voices", "ans": {"grp": "brk"},
                 "why": "The singular is {صَوْتٌ}. The {ت} is a root letter. Pattern {أَفْعَالٌ}."},
                {"s": "سَيَّارَاتٌ", "gloss": "cars", "ans": {"grp": "sfp"},
                 "why": "{سَيَّارَةٌ}: drop the {ة}, add {ـَاتٌ}."},
                {"s": "أَوْقَاتٌ", "gloss": "times", "ans": {"grp": "brk"},
                 "why": "The singular is {وَقْتٌ}. The {ت} is a root letter. Pattern {أَفْعَالٌ}."},
                {"s": "سَاعَاتٌ", "gloss": "hours", "ans": {"grp": "sfp"},
                 "why": "{سَاعَةٌ}: drop the {ة}, add {ـَاتٌ}."},
            ],
        },
        # 5 · unit 5: broken plural patterns
        {
            "title": "Which pattern is this broken plural?",
            "fields": [{"key": "pat", "label": "Pattern", "options": PATTERNS}],
            "rows": [
                {"s": "بُيُوتٌ", "gloss": "houses", "ans": {"pat": "fuul"},
                 "why": "{بَيْتٌ} → {بُيُوتٌ}: pattern {فُعُولٌ}."},
                {"s": "أَقْلَامٌ", "gloss": "pens", "ans": {"pat": "afal"},
                 "why": "{قَلَمٌ} → {أَقْلَامٌ}: pattern {أَفْعَالٌ}."},
                {"s": "جِبَالٌ", "gloss": "mountains", "ans": {"pat": "fial"},
                 "why": "{جَبَلٌ} → {جِبَالٌ}: pattern {فِعَالٌ}."},
                {"s": "كُتُبٌ", "gloss": "books", "ans": {"pat": "fuul2"},
                 "why": "{كِتَابٌ} → {كُتُبٌ}: pattern {فُعُلٌ}."},
                {"s": "طُلَّابٌ", "gloss": "students", "ans": {"pat": "fuaal"},
                 "why": "{طَالِبٌ} → {طُلَّابٌ}: pattern {فُعَّالٌ}, with a shadda."},
                {"s": "مَكَاتِبُ", "gloss": "desks, offices", "ans": {"pat": "dip"},
                 "why": "{مَكْتَبٌ} → {مَكَاتِبُ}: pattern {مَفَاعِلُ}. It is a diptote, so no tanween."},
            ],
        },
        # 6 · unit 6: diptotes
        {
            "title": "Why does it take no tanween?",
            "fields": [{"key": "pick", "label": "Reason", "options": []}],
            "rows": [
                {"s": "فَاطِمَةُ", "gloss": "Fatimah", "ans": {"pick": "b"},
                 "opts": {"pick": pick("A foreign name", "A feminine name", "Plural مَفَاعِلُ / مَفَاعِيلُ")},
                 "why": "A name for a woman. Feminine names are diptotes."},
                {"s": "يُوسُفُ", "gloss": "Yusuf", "ans": {"pick": "a"},
                 "opts": {"pick": pick("A foreign name", "An ـانُ name", "A feminine name")},
                 "why": "{يُوسُفُ} is a name from another language. Foreign names are diptotes."},
                {"s": "عَطْشَانُ", "gloss": "thirsty", "ans": {"pick": "c"},
                 "opts": {"pick": pick("An ـانُ name", "A dual", "A describing word on فَعْلَانُ")},
                 "why": "It describes a person: \"thirsty\". Pattern {فَعْلَانُ}. It is not a name."},
                {"s": "صَحْرَاءُ", "gloss": "a desert", "ans": {"pick": "a"},
                 "opts": {"pick": pick("Ends in the extra ـَاءُ", "Plural مَفَاعِلُ / مَفَاعِيلُ", "A foreign name")},
                 "why": "One desert. It ends in the feminine {ـَاءُ}."},
                {"s": "مَصَابِيحُ", "gloss": "lamps", "ans": {"pick": "b"},
                 "opts": {"pick": pick("A feminine name", "Plural مَفَاعِلُ / مَفَاعِيلُ", "A foreign name")},
                 "why": "{مِصْبَاحٌ} → {مَصَابِيحُ}: pattern {مَفَاعِيلُ}."},
                {"s": "سَلْمَانُ", "gloss": "Salman", "ans": {"pick": "c"},
                 "opts": {"pick": pick("A describing word on فَعْلَانُ", "A foreign name", "An ـانُ name")},
                 "why": "A man's name ending in {ـانُ}. It is a name, so it is not a describing word."},
            ],
        },
        # 7 · unit 7: the five nouns
        {
            "title": "Five-noun signs or not?",
            "fields": [{"key": "sig", "label": "Signs", "options": FIVE}],
            "rows": [
                {"s": "أَبُوكَ", "gloss": "your father", "ans": {"sig": "five"},
                 "why": "Owned by {ـكَ}. It is special: {أَبُوكَ}، {أَبَاكَ}، {أَبِيكَ}."},
                {"s": "أَخُو زَيْدٍ", "gloss": "Zayd's brother", "ans": {"sig": "five"},
                 "why": "Owned by the noun {زَيْدٍ}. It is special."},
                {"s": "ذُو مَالٍ", "gloss": "a man of wealth", "ans": {"sig": "five"},
                 "why": "{ذُو} means \"owner of\". It is always owned, so it is always special."},
                {"s": "أَبٌ", "gloss": "a father", "ans": {"sig": "orig"},
                 "why": "Alone, not owned. Original signs: {أَبٌ}، {أَبًا}، {أَبٍ}."},
                {"s": "الأَخُ", "gloss": "the brother", "ans": {"sig": "orig"},
                 "why": "It has {ال}. Original signs."},
                {"s": "أَبِي", "gloss": "my father", "ans": {"sig": "hid"},
                 "why": "Owned by {ـي} \"my\". The vowel is hidden before {ـي}."},
            ],
        },
        # 8 · unit 8: hidden vowel
        {
            "title": "Which kind of ending?",
            "fields": [{"key": "end", "label": "Ending", "options": HIDDEN}],
            "rows": [
                {"s": "الفَتَى", "gloss": "the young man", "ans": {"end": "maq"},
                 "why": "It ends in {ـَى}. All three vowels are hidden."},
                {"s": "القَاضِي", "gloss": "the judge", "ans": {"end": "manq"},
                 "why": "It ends in {ـِي}. Damma and kasra are hidden. Fatha shows: {القَاضِيَ}."},
                {"s": "دَفْتَرِي", "gloss": "my notebook", "ans": {"end": "ya"},
                 "why": "{دَفْتَرٌ} + {ـي} \"my\". The vowel is hidden before {ـي}."},
                {"s": "سَمَاءٌ", "gloss": "a sky", "ans": {"end": "mamd"},
                 "why": "It ends in {ـَاءٌ}. The hamza carries every vowel, so nothing is hidden."},
                {"s": "العَصَا", "gloss": "the stick", "ans": {"end": "maq"},
                 "why": "It ends in a long {ـَا}. All three vowels are hidden."},
            ],
        },
        # 9 · mixed sentence
        {
            "title": "Classify each noun",
            "prompt": "المُهَنْدِسُونَ وَالمُمَرِّضَتَانِ وَأَخُوكَ فِي المُسْتَشْفَى.",
            "en": "The engineers, the two nurses and your brother are in the hospital.",
            "fields": [
                {"key": "grp", "label": "Group", "options": GROUPS},
                {"key": "also", "label": "Also in", "options": ALSO},
            ],
            "rows": [
                {"s": "المُهَنْدِسُونَ", "ans": {"grp": "smp", "also": "none"},
                 "why": "{مُهَنْدِسٌ} + {ـُونَ}: engineers (men). It is the Topic, in rafʿ."},
                {"s": "المُمَرِّضَتَانِ", "ans": {"grp": "dual", "also": "none"},
                 "why": "{مُمَرِّضَةٌ}: the {ة} becomes {ت}, then {ـَانِ}. Two nurses."},
                {"s": "أَخُوكَ", "ans": {"grp": "sing", "also": "five"},
                 "why": "One brother, owned by {ـكَ}. A five noun."},
                {"s": "المُسْتَشْفَى", "ans": {"grp": "sing", "also": "hid"},
                 "why": "One hospital. It ends in {ـَى}: maqṣūr. Its kasra after {فِي} is hidden."},
            ],
        },
        # 10 · mixed sentence
        {
            "title": "Classify each noun",
            "prompt": "خَرَجَ المُحَامِي وَأَحْمَدُ وَالعُمَّالُ مِنَ المَصَانِعِ.",
            "en": "The lawyer, Ahmad and the workers came out of the factories.",
            "fields": [
                {"key": "grp", "label": "Group", "options": GROUPS},
                {"key": "also", "label": "Also in", "options": ALSO},
            ],
            "rows": [
                {"s": "المُحَامِي", "ans": {"grp": "sing", "also": "hid"},
                 "why": "One lawyer. It ends in {ـِي}: manqūṣ. It is the doer, and its damma is hidden."},
                {"s": "أَحْمَدُ", "ans": {"grp": "sing", "also": "dip"},
                 "why": "A name on the verb pattern {أَفْعَلُ}. A diptote: no tanween."},
                {"s": "العُمَّالُ", "ans": {"grp": "brk", "also": "none"},
                 "why": "{عَامِلٌ} → {عُمَّالٌ}: pattern {فُعَّالٌ}. Without {ال} it takes tanween, {عُمَّالٌ}, so it is not a diptote."},
                {"s": "المَصَانِعِ", "ans": {"grp": "brk", "also": "dip"},
                 "why": "{مَصْنَعٌ} → {مَصَانِعُ}: pattern {مَفَاعِلُ}, a diptote. Here it has {ال}, so it takes kasra after {مِنْ}."},
            ],
        },
    ],

    "homework": [],
}
