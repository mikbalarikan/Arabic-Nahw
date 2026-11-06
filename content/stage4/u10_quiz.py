# Stage 4, Unit 10: Stage 4 quiz (mixed quiz over units 1-8)


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
    "id": "s4-quiz",
    "order": 10,
    "kind": "quiz",
    "title": "Stage 4 quiz",
    "ar": "اخْتِبَارُ أَقْسَامِ الأَسْمَاءِ",
    "blurb": "A mixed quiz on all eight Stage 4 topics: singular, dual, sound plurals, broken plurals, diptotes, five nouns and hidden vowels.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 4 · QUIZ", "title": "Do you know your kinds of nouns?",
         "text": "Eight cards, one for every Stage 4 unit. Do them without your notes.",
         "wm": "أَقْسَامُ الأَسْمَاءِ"},

        {"t": "h2", "text": "How it works"},
        {"t": "p", "text": "Do the practice cards in class, one card at a time. For each noun, find its singular first. Then ask: how many? Is it in a special group?"},
        {"t": "tip", "text": "If you miss a card, go back to its unit and learn the table again. Then do the homework cards."},

        {"t": "summary", "title": "The eight topics", "items": [
            "1. The map: one, two, or three or more. Original signs or branch signs.",
            "2. The dual: {ـَانِ} / {ـَيْنِ}, and {ة} becomes {ت}. {إِنْسَانٌ} is not a dual.",
            "3. The sound masculine plural: {ـُونَ} / {ـِينَ}, for male persons. {زَيْتُونٌ} is not a plural.",
            "4. The sound feminine plural: {ـَاتٌ}. {أَصْوَاتٌ} is a broken plural.",
            "5. The broken plural: {فُعُولٌ}، {أَفْعَالٌ}، {فِعَالٌ}، {فُعُلٌ}، {فُعَّالٌ}، and the patterns with no tanween: {مَفَاعِلُ}، {مَفَاعِيلُ}، {فُعَلَاءُ}.",
            "6. Diptotes: no tanween. In jarr they take fatha, unless they have {ال} or are owned. {فُعَلَاءُ} plurals are diptotes because of the extra {ـَاءُ}.",
            "7. The five nouns: special only when owned by something other than {ـي}: {أَبُوكَ}.",
            "8. Hidden vowels: {الفَتَى}، {القَاضِي}، {كِتَابِي}. {سَمَاءٌ} shows every vowel.",
        ]},
    ],

    "practice": [
        # 1 · unit 1: the map
        {
            "title": "How many, and which signs?",
            "fields": [
                {"key": "num", "label": "How many?", "options": NUMBER},
                {"key": "signs", "label": "Signs", "options": SIGNS},
            ],
            "rows": [
                {"s": "قَمَرٌ", "gloss": "a moon", "ans": {"num": "one", "signs": "orig"},
                 "why": "One moon. A singular takes damma, fatha, kasra."},
                {"s": "بِنْتَانِ", "gloss": "two girls", "ans": {"num": "two", "signs": "branch"},
                 "why": "A dual. It uses letters: {ـَانِ} / {ـَيْنِ}. Branch signs."},
                {"s": "مُعَلِّمُونَ", "gloss": "teachers (men)", "ans": {"num": "many", "signs": "branch"},
                 "why": "A sound masculine plural. It uses letters: {ـُونَ} / {ـِينَ}. Branch signs."},
                {"s": "دُرُوسٌ", "gloss": "lessons", "ans": {"num": "many", "signs": "orig"},
                 "why": "A broken plural of {دَرْسٌ} with tanween. Damma, fatha, kasra, like a singular."},
                {"s": "طَائِرَاتٌ", "gloss": "planes", "ans": {"num": "many", "signs": "branch"},
                 "why": "A sound feminine plural. In naṣb it takes kasra in place of fatha."},
                {"s": "شَوَارِعُ", "gloss": "streets", "ans": {"num": "many", "signs": "branch"},
                 "why": "A broken plural on {مَفَاعِلُ}, so also a diptote. In jarr it takes fatha in place of kasra (Stage 6)."},
            ],
        },
        # 2 · unit 2: dual
        {
            "title": "The dual",
            "fields": [{"key": "pick", "label": "Answer", "options": []}],
            "rows": [
                {"s": "صَدِيقٌ → two friends", "ans": {"pick": "a"},
                 "opts": {"pick": pick("صَدِيقَانِ", "أَصْدِقَاءُ", "صَدِيقُونَ")},
                 "why": "Add {ـَانِ}: {صَدِيقَانِ}. {أَصْدِقَاءُ} is the plural."},
                {"s": "مَدْرَسَةٌ → two schools", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَدْرَسَةَانِ", "مَدْرَسَتَانِ", "مَدَارِسُ")},
                 "why": "The {ة} becomes {ت}, then {ـَانِ}: {مَدْرَسَتَانِ}."},
                {"s": "Which one is NOT a dual?", "ans": {"pick": "b"},
                 "opts": {"pick": pick("كِتَابَانِ", "لِسَانٌ", "شَجَرَتَيْنِ")},
                 "why": "{لِسَانٌ} \"a tongue\" is one thing with tanween. The {ـَانٌ} is part of the word."},
                {"s": "رَمَضَانُ", "gloss": "Ramadan", "ans": {"pick": "c"},
                 "opts": {"pick": pick("A dual", "A sound plural", "A singular name")},
                 "why": "The name of one month. The {ـَانُ} is part of the name."},
            ],
        },
        # 3 · unit 3: sound masculine plural
        {
            "title": "The sound masculine plural",
            "fields": [{"key": "pick", "label": "Answer", "options": []}],
            "rows": [
                {"s": "مُجْتَهِدٌ → hard-working (men)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُجْتَهِدُونَ", "مُجْتَهِدَاتٌ", "مُجْتَهِدَانِ")},
                 "why": "Male persons, three or more: add {ـُونَ}."},
                {"s": "Which word can take ـُونَ?", "ans": {"pick": "b"},
                 "opts": {"pick": pick("كِتَابٌ", "مُسَافِرٌ", "مَسْجِدٌ")},
                 "why": "{مُسَافِرٌ} \"a traveller\" is a male person: {مُسَافِرُونَ}. A book and a mosque are things."},
                {"s": "Which one is a real sound masculine plural?", "ans": {"pick": "b"},
                 "opts": {"pick": pick("قَانُونٌ", "خَبَّازُونَ", "سِكِّينٌ")},
                 "why": "{خَبَّازٌ} + {ـُونَ}: bakers. {قَانُونٌ} \"a law\" and {سِكِّينٌ} \"a knife\" are singular."},
                {"s": "مُؤْمِنِينَ", "gloss": "believers (men)", "ans": {"pick": "c"},
                 "opts": {"pick": pick("A dual", "A broken plural", "A sound masculine plural")},
                 "why": "{مُؤْمِنٌ} + {ـِينَ}: the other shape of {مُؤْمِنُونَ}."},
            ],
        },
        # 4 · unit 4: sound feminine plural
        {
            "title": "The sound feminine plural",
            "fields": [{"key": "pick", "label": "Answer", "options": []}],
            "rows": [
                {"s": "مُهَنْدِسَةٌ → engineers (women)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُهَنْدِسَاتٌ", "مُهَنْدِسَتَاتٌ", "مُهَنْدِسُونَ")},
                 "why": "Drop the {ة}, add {ـَاتٌ}: {مُهَنْدِسَاتٌ}."},
                {"s": "أَبْيَاتٌ", "gloss": "lines of poetry", "ans": {"pick": "b"},
                 "opts": {"pick": pick("A sound feminine plural", "A broken plural", "A dual")},
                 "why": "The singular is {بَيْتٌ}. The {ت} is a root letter. Pattern {أَفْعَالٌ}."},
                {"s": "مُسْلِمَاتٌ", "gloss": "Muslims (women)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("A sound feminine plural", "A broken plural", "A singular")},
                 "why": "{مُسْلِمَةٌ}: drop the {ة}, add {ـَاتٌ}."},
                {"s": "The singular of مُمَرِّضَاتٌ", "gloss": "nurses (women)", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُمَرِّضٌ", "مُمَرِّضُونَ", "مُمَرِّضَةٌ")},
                 "why": "Take off {ـَاتٌ} and put back the {ة}: {مُمَرِّضَةٌ}."},
            ],
        },
        # 5 · unit 5: broken plural
        {
            "title": "Which pattern is this broken plural?",
            "fields": [{"key": "pat", "label": "Pattern", "options": PATTERNS}],
            "rows": [
                {"s": "نُجُومٌ", "gloss": "stars", "ans": {"pat": "fuul"},
                 "why": "{نَجْمٌ} → {نُجُومٌ}: pattern {فُعُولٌ}."},
                {"s": "أَبْوَابٌ", "gloss": "doors", "ans": {"pat": "afal"},
                 "why": "{بَابٌ} → {أَبْوَابٌ}: pattern {أَفْعَالٌ}."},
                {"s": "كِلَابٌ", "gloss": "dogs", "ans": {"pat": "fial"},
                 "why": "{كَلْبٌ} → {كِلَابٌ}: pattern {فِعَالٌ}."},
                {"s": "مُدُنٌ", "gloss": "cities", "ans": {"pat": "fuul2"},
                 "why": "{مَدِينَةٌ} → {مُدُنٌ}: pattern {فُعُلٌ}."},
                {"s": "تُجَّارٌ", "gloss": "merchants", "ans": {"pat": "fuaal"},
                 "why": "{تَاجِرٌ} → {تُجَّارٌ}: pattern {فُعَّالٌ}."},
                {"s": "عُلَمَاءُ", "gloss": "scholars", "ans": {"pat": "dip"},
                 "why": "{عَالِمٌ} → {عُلَمَاءُ}: pattern {فُعَلَاءُ}. It ends in the extra {ـَاءُ}, so no tanween."},
            ],
        },
        # 6 · unit 6: diptotes
        {
            "title": "Why does it take no tanween?",
            "fields": [{"key": "pick", "label": "Reason", "options": []}],
            "rows": [
                {"s": "يَزِيدُ", "gloss": "Yazid", "ans": {"pick": "a"},
                 "opts": {"pick": pick("A name on a verb pattern", "A foreign name", "A feminine name")},
                 "why": "A man's name with the shape of a verb, like {أَحْمَدُ}."},
                {"s": "إِبْرَاهِيمُ", "gloss": "Ibrahim", "ans": {"pick": "b"},
                 "opts": {"pick": pick("A name on a verb pattern", "A foreign name", "Plural مَفَاعِلُ / مَفَاعِيلُ")},
                 "why": "A name from another language. Foreign names are diptotes."},
                {"s": "أَزْرَقُ", "gloss": "blue", "ans": {"pick": "c"},
                 "opts": {"pick": pick("A name on a verb pattern", "A foreign name", "A describing word on أَفْعَلُ")},
                 "why": "A colour word on {أَفْعَلُ}. It describes, so it is not a name."},
                {"s": "بَيْضَاءُ", "gloss": "white (f)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("Ends in the extra ـَاءُ", "Plural مَفَاعِلُ / مَفَاعِيلُ", "An ـانُ name")},
                 "why": "One white thing (f). It ends in the feminine {ـَاءُ}."},
                {"s": "مَطَاعِمُ", "gloss": "restaurants", "ans": {"pick": "b"},
                 "opts": {"pick": pick("A feminine name", "Plural مَفَاعِلُ / مَفَاعِيلُ", "A foreign name")},
                 "why": "{مَطْعَمٌ} → {مَطَاعِمُ}: pattern {مَفَاعِلُ}."},
                {"s": "عَدْنَانُ", "gloss": "Adnan", "ans": {"pick": "c"},
                 "opts": {"pick": pick("A dual", "A foreign name", "An ـانُ name")},
                 "why": "A man's name ending in {ـانُ}. One person, so it is not a dual."},
            ],
        },
        # 7 · unit 7: five nouns
        {
            "title": "Five-noun signs or not?",
            "fields": [{"key": "sig", "label": "Signs", "options": FIVE}],
            "rows": [
                {"s": "أَبُو خَالِدٍ", "gloss": "Khalid's father", "ans": {"sig": "five"},
                 "why": "Owned by the noun {خَالِدٍ}. It is special."},
                {"s": "فُوكَ", "gloss": "your mouth", "ans": {"sig": "five"},
                 "why": "{فُو} without {م}, owned by {ـكَ}. It is special."},
                {"s": "ذُو عِلْمٍ", "gloss": "a man of knowledge", "ans": {"sig": "five"},
                 "why": "{ذُو} is always owned, so it is always special."},
                {"s": "أَخِي", "gloss": "my brother", "ans": {"sig": "hid"},
                 "why": "Owned by {ـي} \"my\". The vowel is hidden before {ـي}."},
                {"s": "الأَبُ", "gloss": "the father", "ans": {"sig": "orig"},
                 "why": "It has {ال}. Original signs."},
                {"s": "أَخٌ", "gloss": "a brother", "ans": {"sig": "orig"},
                 "why": "Alone, not owned. Original signs: {أَخٌ}، {أَخًا}، {أَخٍ}."},
            ],
        },
        # 8 · unit 8: hidden vowel
        {
            "title": "Which kind of ending?",
            "fields": [{"key": "end", "label": "Ending", "options": HIDDEN}],
            "rows": [
                {"s": "الوَادِي", "gloss": "the valley", "ans": {"end": "manq"},
                 "why": "It ends in {ـِي}. Damma and kasra are hidden. Fatha shows: {الوَادِيَ}."},
                {"s": "مُوسَى", "gloss": "Musa", "ans": {"end": "maq"},
                 "why": "It ends in {ـَى}. All three vowels are hidden."},
                {"s": "كِتَابِي", "gloss": "my book", "ans": {"end": "ya"},
                 "why": "{كِتَابٌ} + {ـي} \"my\". The vowel is hidden before {ـي}."},
                {"s": "دُعَاءٌ", "gloss": "a prayer", "ans": {"end": "mamd"},
                 "why": "It ends in {ـَاءٌ}. The hamza carries every vowel, so nothing is hidden."},
                {"s": "المَقْهَى", "gloss": "the café", "ans": {"end": "maq"},
                 "why": "It ends in {ـَى}. All three vowels are hidden."},
            ],
        },
    ],

    "homework": [
        # 1 · groups
        {
            "title": "Which group is it in?",
            "fields": [{"key": "grp", "label": "Group", "options": GROUPS}],
            "rows": [
                {"s": "مُعَلِّمَتَانِ", "gloss": "two teachers (women)", "ans": {"grp": "dual"},
                 "why": "{مُعَلِّمَةٌ}: the {ة} becomes {ت}, then {ـَانِ}."},
                {"s": "لَاعِبُونَ", "gloss": "players (men)", "ans": {"grp": "smp"},
                 "why": "{لَاعِبٌ} + {ـُونَ}. Male persons."},
                {"s": "أَلْوَانٌ", "gloss": "colours", "ans": {"grp": "brk"},
                 "why": "{لَوْنٌ} → {أَلْوَانٌ}: pattern {أَفْعَالٌ}."},
                {"s": "ثَلَّاجَاتٌ", "gloss": "fridges", "ans": {"grp": "sfp"},
                 "why": "{ثَلَّاجَةٌ}: drop the {ة}, add {ـَاتٌ}."},
                {"s": "عُنْوَانٌ", "gloss": "an address", "ans": {"grp": "sing"},
                 "why": "One thing with tanween. The {ـَانٌ} is part of the word."},
                {"s": "أُمَرَاءُ", "gloss": "princes", "ans": {"grp": "brk"},
                 "why": "{أَمِيرٌ} → {أُمَرَاءُ}: pattern {فُعَلَاءُ}. A broken plural, and a diptote because of the extra {ـَاءُ}."},
            ],
        },
        # 2 · forming duals and sound plurals
        {
            "title": "Make the right form",
            "fields": [{"key": "pick", "label": "Answer", "options": []}],
            "rows": [
                {"s": "غُرْفَةٌ → two rooms", "ans": {"pick": "b"},
                 "opts": {"pick": pick("غُرْفَةَانِ", "غُرْفَتَانِ", "غُرَفٌ")},
                 "why": "The {ة} becomes {ت}, then {ـَانِ}: {غُرْفَتَانِ}."},
                {"s": "نَجَّارٌ → carpenters (men)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("نَجَّارُونَ", "نَجَّارَاتٌ", "نَجَّارَانِ")},
                 "why": "Male persons, three or more: {نَجَّارُونَ}."},
                {"s": "مُسَافِرَةٌ → travellers (women)", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُسَافِرُونَ", "مُسَافِرَتَانِ", "مُسَافِرَاتٌ")},
                 "why": "Drop the {ة}, add {ـَاتٌ}: {مُسَافِرَاتٌ}."},
                {"s": "بُسْتَانٌ → two gardens", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بُسْتَانَانِ", "بُسْتَانٌ", "بَسَاتِينُ")},
                 "why": "{بُسْتَانٌ} is singular. Its {ـَانٌ} is part of the word. Add {ـَانِ}: {بُسْتَانَانِ}."},
                {"s": "Which one is a real dual?", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مَكَانٌ", "فِنْجَانٌ", "بَيْتَانِ")},
                 "why": "{بَيْتٌ} + {ـَانِ}: two houses. {مَكَانٌ} and {فِنْجَانٌ} are singular."},
            ],
        },
        # 3 · broken plural patterns
        {
            "title": "Which pattern is this broken plural?",
            "fields": [{"key": "pat", "label": "Pattern", "options": PATTERNS}],
            "rows": [
                {"s": "قُلُوبٌ", "gloss": "hearts", "ans": {"pat": "fuul"},
                 "why": "{قَلْبٌ} → {قُلُوبٌ}: pattern {فُعُولٌ}."},
                {"s": "أَسْوَاقٌ", "gloss": "markets", "ans": {"pat": "afal"},
                 "why": "{سُوقٌ} → {أَسْوَاقٌ}: pattern {أَفْعَالٌ}."},
                {"s": "جِمَالٌ", "gloss": "camels", "ans": {"pat": "fial"},
                 "why": "{جَمَلٌ} → {جِمَالٌ}: pattern {فِعَالٌ}."},
                {"s": "سُفُنٌ", "gloss": "ships", "ans": {"pat": "fuul2"},
                 "why": "{سَفِينَةٌ} → {سُفُنٌ}: pattern {فُعُلٌ}."},
                {"s": "كُتَّابٌ", "gloss": "writers", "ans": {"pat": "fuaal"},
                 "why": "{كَاتِبٌ} → {كُتَّابٌ}: pattern {فُعَّالٌ}."},
                {"s": "مَفَاتِيحُ", "gloss": "keys", "ans": {"pat": "dip"},
                 "why": "{مِفْتَاحٌ} → {مَفَاتِيحُ}: pattern {مَفَاعِيلُ}. A diptote, so no tanween."},
            ],
        },
        # 4 · diptotes
        {
            "title": "Why does it take no tanween?",
            "fields": [{"key": "pick", "label": "Reason", "options": []}],
            "rows": [
                {"s": "عَائِشَةُ", "gloss": "Aishah", "ans": {"pick": "a"},
                 "opts": {"pick": pick("A feminine name", "A foreign name", "An ـانُ name")},
                 "why": "A name for a woman. Feminine names are diptotes."},
                {"s": "يَعْقُوبُ", "gloss": "Yaqub", "ans": {"pick": "b"},
                 "opts": {"pick": pick("An ـانُ name", "A foreign name", "A feminine name")},
                 "why": "A name from another language. Foreign names are diptotes."},
                {"s": "أَكْبَرُ", "gloss": "bigger", "ans": {"pick": "c"},
                 "opts": {"pick": pick("A feminine name", "Plural مَفَاعِلُ / مَفَاعِيلُ", "A describing word on أَفْعَلُ")},
                 "why": "A describing word on {أَفْعَلُ}."},
                {"s": "غَضْبَانُ", "gloss": "angry", "ans": {"pick": "a"},
                 "opts": {"pick": pick("A describing word on فَعْلَانُ", "An ـانُ name", "A dual")},
                 "why": "It describes a person: \"angry\". Pattern {فَعْلَانُ}."},
                {"s": "حَسْنَاءُ", "gloss": "beautiful (f)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("Plural مَفَاعِلُ / مَفَاعِيلُ", "Ends in the extra ـَاءُ", "A foreign name")},
                 "why": "It describes one woman. It ends in the feminine {ـَاءُ}."},
                {"s": "شُعَرَاءُ", "gloss": "poets", "ans": {"pick": "c"},
                 "opts": {"pick": pick("A feminine name", "Plural مَفَاعِلُ / مَفَاعِيلُ", "Ends in the extra ـَاءُ")},
                 "why": "{شَاعِرٌ} → {شُعَرَاءُ}. Like {عُلَمَاءُ}, it ends in the extra {ـَاءُ}. It is not on {مَفَاعِلُ}."},
            ],
        },
        # 5 · five nouns
        {
            "title": "Five-noun signs or not?",
            "fields": [{"key": "sig", "label": "Signs", "options": FIVE}],
            "rows": [
                {"s": "أَخُوهَا", "gloss": "her brother", "ans": {"sig": "five"},
                 "why": "Owned by {ـهَا}. It is special."},
                {"s": "حَمُوهَا", "gloss": "her father-in-law", "ans": {"sig": "five"},
                 "why": "{حَمٌ} owned by {ـهَا}. It is special."},
                {"s": "ذُو فَضْلٍ", "gloss": "a man of merit", "ans": {"sig": "five"},
                 "why": "{ذُو} is always owned, so it is always special."},
                {"s": "أَبُونَا", "gloss": "our father", "ans": {"sig": "five"},
                 "why": "Owned by {ـنَا}. Only {ـي} stops it being special."},
                {"s": "فَمُهُ", "gloss": "his mouth", "ans": {"sig": "orig"},
                 "why": "It keeps the {م}. Only {فُو} without {م} is a five noun."},
                {"s": "إِخْوَتُكَ", "gloss": "your brothers", "ans": {"sig": "orig"},
                 "why": "A plural. Only the singular {أَخٌ} is a five noun."},
            ],
        },
        # 6 · mixed sentence
        {
            "title": "Classify each noun",
            "prompt": "الطَّبِيبَاتُ وَأَبُو مَحْمُودٍ فِي النَّادِي.",
            "en": "The doctors (women) and Abu Mahmud are in the club.",
            "fields": [
                {"key": "grp", "label": "Group", "options": GROUPS},
                {"key": "also", "label": "Also in", "options": ALSO},
            ],
            "rows": [
                {"s": "الطَّبِيبَاتُ", "ans": {"grp": "sfp", "also": "none"},
                 "why": "{طَبِيبَةٌ}: drop the {ة}, add {ـَاتٌ}. It is the Topic, in rafʿ."},
                {"s": "أَبُو", "ans": {"grp": "sing", "also": "five"},
                 "why": "One father, owned by {مَحْمُودٍ}. A five noun."},
                {"s": "مَحْمُودٍ", "ans": {"grp": "sing", "also": "none"},
                 "why": "A normal name with tanween. It is the owner, with kasra."},
                {"s": "النَّادِي", "ans": {"grp": "sing", "also": "hid"},
                 "why": "It ends in {ـِي}: manqūṣ. Its kasra after {فِي} is hidden."},
            ],
        },
    ],
}
