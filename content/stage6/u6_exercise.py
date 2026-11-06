# Stage 6: class exercise (review of units 1-5, done together in class before the Stage 6 quiz)

KAS = {"k": "kas", "label": "Kasra · كَسْرَةٌ", "color": "green"}
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
DAM = {"k": "dam", "label": "Damma · ضَمَّةٌ", "color": "red"}
ALIF = {"k": "alif", "label": "Alif · الأَلِفُ", "color": "teal"}
WAW = {"k": "waw", "label": "Wāw · الوَاوُ", "color": "blue"}
YA = {"k": "ya", "label": "Yāʾ · اليَاءُ", "color": "purple"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}
JSIGNS = [KAS, YA, FAT, HID]
PSIGNS = [KAS, YA, HID, FIXED]

RAF = {"k": "raf", "label": "Rafʿ · رَفْعٌ", "color": "red"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ", "color": "green"}

PREP = {"k": "prep", "label": "After a preposition · اِسْمٌ مَجْرُورٌ", "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
AND = {"k": "and", "label": "After وَ (and) · مَعْطُوفٌ", "color": "blue"}
TAWK = {"k": "tawk", "label": "Emphasis · تَوْكِيدٌ", "color": "grey"}
BADAL = {"k": "badal", "label": "Substitute · بَدَلٌ", "color": "grey"}
JOBS = [PREP, OWNER, ADJ, AND]

R_ALONE = {"k": "alone", "label": "Diptote, no ال, no owner: fatha", "color": "orange"}
R_AL = {"k": "al", "label": "Diptote with ال: kasra", "color": "green"}
R_OWN = {"k": "own", "label": "Diptote with an owner: kasra", "color": "purple"}
R_NOT = {"k": "not", "label": "Not a diptote: kasra", "color": "grey"}
REASONS = [R_ALONE, R_AL, R_OWN, R_NOT]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s6-exercise",
    "order": 6,
    "kind": "exercise",
    "title": "Stage 6 class exercise",
    "ar": "تَمْرِينُ المَجْرُورَاتِ",
    "blurb": "Ten mixed cards on the whole of Stage 6, done together in class before the Stage 6 quiz.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 6 · CLASS EXERCISE", "title": "All of jarr together",
         "text": "Ten cards that mix every Stage 6 unit. We do them together in class, before the Stage 6 quiz.",
         "wm": "المَجْرُورَاتُ"},

        {"t": "h2", "text": "How we do it in class"},
        {"t": "p", "text": "Work in pairs, or come to the board. One student reads the sentence aloud. Then for each word, say three things: the job, the case, the sign. The partner checks it or corrects it. Then swap."},
        {"t": "rule", "color": "teal", "title": "Job → case → sign",
         "text": "Find the job. The job gives the case. The kind of noun gives the sign."},
        {"t": "tip", "text": "Say the full formula aloud for one word in every card: {اِسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
        {"t": "tip", "text": "If a card is hard, open its unit and read the table again before the quiz."},

        {"t": "h2", "text": "The five topics"},
        {"t": "cols", "items": [
            {"color": "green", "title": "1. The signs of jarr", "ar": "عَلَامَاتُ الجَرِّ",
             "text": "Three jobs: after a preposition, owner, follower. Four signs: kasra, yāʾ, fatha, hidden kasra."},
            {"color": "green", "title": "2. After a preposition", "ar": "حُرُوفُ الجَرِّ",
             "text": "{مِنْ}، {إِلَى}، {عَنْ}، {عَلَى}، {فِي}، {بِـ}، {لِـ}، {كَـ}، {رُبَّ}، {حَتَّى}، {مُنْذُ}. A pronoun after them is fixed: {عَلَيْهِ}."},
            {"color": "purple", "title": "3. The owner", "ar": "المُضَافُ إِلَيْهِ",
             "text": "Always jarr. The first noun drops {ال}, tanween and the {ن}: {كِتَابَا الطَّالِبِ}، {مُعَلِّمِي المَدْرَسَةِ}."},
            {"color": "orange", "title": "4. The diptote", "ar": "المَمْنُوعُ مِنَ الصَّرْفِ",
             "text": "Fatha in place of kasra: {بِأَحْمَدَ}. Kasra again with {ال} or an owner: {فِي المَسَاجِدِ}."},
            {"color": "grey", "title": "5. Followers", "ar": "التَّوَابِعُ",
             "text": "Adjective, after {وَ}, emphasis, substitute. They copy the jarr. Their own kind gives the sign."},
        ]},

        {"t": "h2", "text": "The signs at a glance"},
        {"t": "table", "head": ["Kind of noun", "Example", "Sign"], "rows": [
            ["Singular, broken plural, sound f. plural", "فِي البَيْتِ، مِنَ الكُتُبِ، إِلَى المُدَرِّسَاتِ", "Kasra"],
            ["Dual, sound m. plural, five nouns", "بِالقَلَمَيْنِ، عَلَى المُسْلِمِينَ، إِلَى أَبِيكَ", "Yāʾ"],
            ["Diptote, no {ال}, no owner", "عَلَى أَحْمَدَ، فِي مَسَاجِدَ", "Fatha"],
            ["Maqṣūr, manqūṣ, noun + {ـي} \"my\"", "إِلَى المُسْتَشْفَى، عَلَى قَاضٍ، فِي بَيْتِي", "Hidden kasra"],
            ["Attached pronoun", "عَلَيْهِ، كِتَابُهُ", "Fixed, in the place of jarr"],
        ]},

        {"t": "summary", "title": "Remember", "items": [
            "Three jobs give jarr: after a preposition, owner, follower.",
            "Yāʾ in jarr: look at the vowel before it. Fatha {ـَيْنِ} is a dual. Kasra {ـِينَ} is a sound m. plural.",
            "A diptote takes fatha in jarr only with no {ال} and no owner.",
            "The first noun of an iḍāfa takes the case of its own job. The owner is always jarr.",
            "A follower copies the case, not the sign: {فِي مَسَاجِدَ كَثِيرَةٍ}.",
            "If the preposition comes again, the noun is after a preposition, not a follower.",
        ]},
    ],

    "practice": [
        # 1 · unit 1: the four signs
        {
            "title": "Which sign of jarr does the word in [brackets] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "سَلَّمْتُ عَلَى [المُوَظَّفِينَ]", "gloss": "I greeted the employees.", "ans": {"sign": "ya"},
                 "why": "Kasra before {ي}: {ـِينَ}. A sound m. plural: {اِسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ}."},
                {"s": "نَظَرْتُ إِلَى [السَّمَاءِ]", "gloss": "I looked at the sky.", "ans": {"sign": "kas"},
                 "why": "{السَّمَاءُ} ends in {ـَاءُ}. The hamza carries the vowel, so the kasra shows."},
                {"s": "رَجَعْتُ مِنَ [المَقْهَى]", "gloss": "I came back from the café.", "ans": {"sign": "hid"},
                 "why": "Maqṣūr: it ends in alif. The alif cannot carry a vowel, so the kasra is hidden."},
                {"s": "مَشَيْتُ فِي [شَوَارِعَ] ضَيِّقَةٍ", "gloss": "I walked in narrow streets.", "ans": {"sign": "fat"},
                 "why": "{شَوَارِعُ} is a long plural, a diptote. No {ال}, no owner: fatha in place of kasra."},
                {"s": "سَأَلْتُ عَنِ [الوَلَدَيْنِ]", "gloss": "I asked about the two boys.", "ans": {"sign": "ya"},
                 "why": "Fatha before {ي}: {ـَيْنِ}. A dual: {مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
                {"s": "كَتَبْتُ بِ[الأَقْلَامِ]", "gloss": "I wrote with the pens.", "ans": {"sign": "kas"},
                 "why": "{أَقْلَامٌ} is a broken plural with tanween. It is not a diptote: kasra."},
            ],
        },
        # 2 · unit 1: from rafʿ to jarr (review card)
        {
            "title": "Review: rafʿ or jarr? Which sign?",
            "fields": [{"key": "case", "label": "Case", "options": [RAF, JARR]},
                       {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, KAS, YA, FAT]}],
            "rows": [
                {"s": "[الطَّبَّاخُونَ] فِي المَطْبَخِ.", "gloss": "The cooks are in the kitchen.",
                 "ans": {"case": "raf", "sign": "waw"},
                 "why": "Topic: rafʿ. A sound m. plural shows rafʿ with {و}."},
                {"s": "سَأَلْتُ عَنِ [الطَّبَّاخِينَ].", "gloss": "I asked about the cooks.",
                 "ans": {"case": "jarr", "sign": "ya"},
                 "why": "After {عَنْ}: jarr. A sound m. plural shows jarr with {ي}."},
                {"s": "جَاءَ [أَخُوكَ].", "gloss": "Your brother came.",
                 "ans": {"case": "raf", "sign": "waw"},
                 "why": "Doer: rafʿ. A five noun with an owner shows rafʿ with {و}."},
                {"s": "هَذَا قَلَمُ [أَخِيكَ].", "gloss": "This is your brother's pen.",
                 "ans": {"case": "jarr", "sign": "ya"},
                 "why": "Owner: jarr. A five noun shows jarr with {ي}."},
                {"s": "[المُمَرِّضَتَانِ] فِي المُسْتَشْفَى.", "gloss": "The two nurses are in the hospital.",
                 "ans": {"case": "raf", "sign": "alif"},
                 "why": "Topic: rafʿ. A dual shows rafʿ with alif."},
                {"s": "سَلَّمْتُ عَلَى [المُمَرِّضَتَيْنِ].", "gloss": "I greeted the two nurses.",
                 "ans": {"case": "jarr", "sign": "ya"},
                 "why": "After {عَلَى}: jarr. A dual shows jarr with {ي}, fatha before it."},
            ],
        },
        # 3 · unit 2: prepositions and pronouns
        {
            "title": "Find the jarr job and the sign",
            "prompt": "سَلَّمْتُ عَلَيْهِ فِي المَلْعَبِ وَسَأَلْتُهُ عَنْ أَخِيهِ وَأُخْتِهِ.",
            "en": "I greeted him in the stadium and asked him about his brother and his sister.",
            "fields": [{"key": "job", "label": "Job", "options": JOBS},
                       {"key": "sign", "label": "Sign", "options": PSIGNS}],
            "rows": [
                {"s": "عَلَيْهِ", "gloss": "on him (the pronoun هِ)", "ans": {"job": "prep", "sign": "fixed"},
                 "why": "{هِ} comes after {عَلَى}. It is an attached pronoun: fixed, in the place of jarr."},
                {"s": "المَلْعَبِ", "gloss": "the stadium", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {فِي}. A singular: {اِسْمٌ مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}."},
                {"s": "أَخِيهِ", "gloss": "his brother", "ans": {"job": "prep", "sign": "ya"},
                 "why": "After {عَنْ}. A five noun with the owner {هِ}: {وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ}."},
                {"s": "أُخْتِهِ", "gloss": "his sister", "ans": {"job": "and", "sign": "kas"},
                 "why": "After {وَ}, it copies {أَخِيهِ} in jarr. {أُخْتٌ} is a normal singular: kasra."},
            ],
        },
        # 4 · unit 2: oath, رُبَّ، حَتَّى، مُنْذُ، كَـ، لِـ
        {
            "title": "Oath, رُبَّ، حَتَّى، مُنْذُ، كَـ، لِـ: which sign?",
            "fields": [{"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "وَ[القَمَرِ]", "gloss": "by the moon", "ans": {"sign": "kas"},
                 "why": "{وَ} of an oath is a preposition. {القَمَرِ}: a singular, kasra."},
                {"s": "رُبَّ [طَالِبٍ] مُجْتَهِدٍ رَأَيْتُهُ", "gloss": "many a hardworking student I have seen", "ans": {"sign": "kas"},
                 "why": "{رُبَّ} pulls an indefinite noun to jarr: kasra with tanween."},
                {"s": "مَا رَأَيْتُهُ مُنْذُ [الصَّيْفِ]", "gloss": "I have not seen him since the summer.", "ans": {"sign": "kas"},
                 "why": "After {مُنْذُ}. A singular: kasra."},
                {"s": "جَلَسْنَا فِي المَسْجِدِ حَتَّى [الظُّهْرِ]", "gloss": "We sat in the mosque until noon.", "ans": {"sign": "kas"},
                 "why": "After {حَتَّى} \"until\". A singular: kasra."},
                {"s": "هَذَا الوَلَدُ كَـ[أَبِيهِ]", "gloss": "This boy is like his father.", "ans": {"sign": "ya"},
                 "why": "After {كَـ}. A five noun with an owner: yāʾ."},
                {"s": "هَذِهِ الهَدِيَّةُ لِـ[عَائِشَةَ]", "gloss": "This gift is for Aisha.", "ans": {"sign": "fat"},
                 "why": "After {لِـ}. A feminine name is a diptote: fatha in place of kasra."},
            ],
        },
        # 5 · unit 3: the first noun of an iḍāfa
        {
            "title": "Make the iḍāfa: which first noun?",
            "fields": [{"key": "pick", "label": "First noun", "options": []}],
            "rows": [
                {"s": "___ المُهَنْدِسِ جَدِيدَةٌ", "gloss": "The engineer's car is new.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("السَّيَّارَةُ", "سَيَّارَةُ", "سَيَّارَةٌ")},
                 "why": "The first noun has no {ال} and no tanween. Topic: rafʿ, damma."},
                {"s": "خَرَجَ ___ الطَّبِيبِ", "gloss": "The doctor's two sons went out.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("ابْنَا", "ابْنَانِ", "ابْنَيْ")},
                 "why": "Doer: rafʿ, so alif. A dual first noun drops its {ن}."},
                {"s": "سَأَلْتُ عَنْ ___ المَصْنَعِ", "gloss": "I asked about the factory's employees.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُوَظَّفُو", "مُوَظَّفِينَ", "مُوَظَّفِي")},
                 "why": "After {عَنْ}: jarr, so {ي}. A sound m. plural first noun drops its {ن}."},
                {"s": "حَضَرَتْ ___ المُسْتَشْفَى", "gloss": "The hospital's nurses came.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُمَرِّضَاتُ", "مُمَرِّضَاتٌ", "المُمَرِّضَاتُ")},
                 "why": "Doer: rafʿ, damma. A sound f. plural first noun only drops its tanween."},
                {"s": "نَظَرْتُ إِلَى ___ خَالِدٍ", "gloss": "I looked at Khalid's two notebooks.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("دَفْتَرَا", "دَفْتَرَيْ", "دَفْتَرَيْنِ")},
                 "why": "After {إِلَى}: jarr, so {ي} with fatha before it. The {ن} drops in iḍāfa."},
                {"s": "حَضَرَ ___ القَرْيَةِ", "gloss": "The village's farmers came.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("فَلَّاحُونَ", "فَلَّاحِي", "فَلَّاحُو")},
                 "why": "Doer: rafʿ, so {و}. The {ن} drops in iḍāfa."},
            ],
        },
        # 6 · unit 3: a chain of owners
        {
            "title": "A chain of owners: job and sign",
            "prompt": "جَلَسْنَا فِي غُرْفَةِ مُدِيرِ المُسْتَشْفَى مَعَ أَبِي بَكْرٍ.",
            "en": "We sat in the room of the hospital's director with Abu Bakr.",
            "fields": [{"key": "job", "label": "Job", "options": JOBS},
                       {"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "غُرْفَةِ", "gloss": "room", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {فِي}. A singular: kasra. It is owned, so no tanween."},
                {"s": "مُدِيرِ", "gloss": "director", "ans": {"job": "owner", "sign": "kas"},
                 "why": "It owns {غُرْفَةِ}: {مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}. It is also a first noun, so no tanween."},
                {"s": "المُسْتَشْفَى", "gloss": "the hospital", "ans": {"job": "owner", "sign": "hid"},
                 "why": "It owns {مُدِيرِ}. Maqṣūr: the kasra is hidden on the alif."},
                {"s": "أَبِي", "gloss": "father (of)", "ans": {"job": "owner", "sign": "ya"},
                 "why": "{مَعَ} is not a preposition, so this is its owner. {أَبِي} is owned by {بَكْرٍ}: a five noun, yāʾ. It does not mean \"my\" here."},
                {"s": "بَكْرٍ", "gloss": "Bakr", "ans": {"job": "owner", "sign": "kas"},
                 "why": "It owns {أَبِي}. {بَكْرٌ} is not a diptote: kasra with tanween."},
            ],
        },
        # 7 · unit 4: why fatha or kasra?
        {
            "title": "Why fatha or kasra? Look at the noun after the preposition",
            "fields": [{"key": "why", "label": "Reason", "options": REASONS}],
            "rows": [
                {"s": "فِي فَنَادِقَ كَثِيرَةٍ", "gloss": "in many hotels", "ans": {"why": "alone"},
                 "why": "{فَنَادِقُ} is a long plural with no {ال} and no owner."},
                {"s": "إِلَى الأَطِبَّاءِ", "gloss": "to the doctors", "ans": {"why": "al"},
                 "why": "{أَطِبَّاءُ} has the extra {ـَاءُ}, a diptote. Here it has {ال}."},
                {"s": "فِي بَيْتٍ قَدِيمٍ", "gloss": "in an old house", "ans": {"why": "not"},
                 "why": "{بَيْتٌ} takes tanween. It is not a diptote."},
                {"s": "عَنْ إِسْمَاعِيلَ", "gloss": "about Ismail", "ans": {"why": "alone"},
                 "why": "A foreign name. Names have no {ال} and no owner."},
                {"s": "مِنْ أَفْضَلِ طَالِبٍ", "gloss": "from the best student", "ans": {"why": "own"},
                 "why": "{أَفْضَلُ} is on {أَفْعَلُ}, a diptote. {طَالِبٍ} is its owner."},
                {"s": "فِي فَنَادِقِ المَدِينَةِ", "gloss": "in the hotels of the city", "ans": {"why": "own"},
                 "why": "{المَدِينَةِ} is the owner of {فَنَادِقِ}."},
            ],
        },
        # 8 · unit 4: diptotes in a sentence
        {
            "title": "Job and sign",
            "prompt": "صَلَّيْنَا فِي مَسْجِدِ عُثْمَانَ ثُمَّ ذَهَبْنَا إِلَى مَطَاعِمَ قَرِيبَةٍ.",
            "en": "We prayed in Uthman's mosque, then we went to nearby restaurants.",
            "fields": [{"key": "job", "label": "Job", "options": [PREP, OWNER, ADJ]},
                       {"key": "sign", "label": "Sign", "options": [KAS, FAT]}],
            "rows": [
                {"s": "مَسْجِدِ", "gloss": "mosque", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {فِي}. {مَسْجِدٌ} is a normal singular: kasra."},
                {"s": "عُثْمَانَ", "gloss": "Uthman", "ans": {"job": "owner", "sign": "fat"},
                 "why": "It owns {مَسْجِدِ}. A name ending in {ـَانُ}: {مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الفَتْحَةُ نِيَابَةً عَنِ الكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ}."},
                {"s": "مَطَاعِمَ", "gloss": "restaurants", "ans": {"job": "prep", "sign": "fat"},
                 "why": "After {إِلَى}. A long plural with no {ال} and no owner: fatha in place of kasra."},
                {"s": "قَرِيبَةٍ", "gloss": "nearby", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {مَطَاعِمَ}, so it is jarr too. It is not a diptote: kasra with tanween."},
            ],
        },
        # 9 · unit 5: find the follower's job
        {
            "title": "Find the job",
            "prompt": "سَلَّمْتُ عَلَى جَارِنَا سَعِيدٍ وَأَوْلَادِهِ كُلِّهِمْ.",
            "en": "I greeted our neighbour Saeed and all his children.",
            "fields": [{"key": "job", "label": "Job", "options": [PREP, AND, TAWK, BADAL]}],
            "rows": [
                {"s": "جَارِنَا", "gloss": "our neighbour", "ans": {"job": "prep"},
                 "why": "It comes after {عَلَى}: jarr with kasra."},
                {"s": "سَعِيدٍ", "gloss": "Saeed", "ans": {"job": "badal"},
                 "why": "It names our neighbour again: a substitute in jarr, kasra."},
                {"s": "أَوْلَادِهِ", "gloss": "his children", "ans": {"job": "and"},
                 "why": "After {وَ}, it copies the jarr of {جَارِنَا}. A broken plural: kasra."},
                {"s": "كُلِّهِمْ", "gloss": "all of them", "ans": {"job": "tawk"},
                 "why": "{كُلُّ} + a matching pronoun: emphasis. It copies the jarr of {أَوْلَادِهِ}."},
            ],
        },
        # 10 · unit 5 + all signs: a full sentence
        {
            "title": "Job and sign",
            "prompt": "نَظَرْتُ إِلَى الطَّبِيبَيْنِ المَاهِرَيْنِ وَالمُمَرِّضَاتِ الجَدِيدَاتِ فِي مُسْتَشْفًى كَبِيرٍ.",
            "en": "I looked at the two skilled doctors and the new nurses in a big hospital.",
            "fields": [{"key": "job", "label": "Job", "options": [PREP, ADJ, AND]},
                       {"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "الطَّبِيبَيْنِ", "gloss": "the two doctors", "ans": {"job": "prep", "sign": "ya"},
                 "why": "After {إِلَى}. Fatha before {ي}: a dual. {اِسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
                {"s": "المَاهِرَيْنِ", "gloss": "skilled", "ans": {"job": "adj", "sign": "ya"},
                 "why": "It describes {الطَّبِيبَيْنِ}. A dual adjective in jarr: yāʾ."},
                {"s": "المُمَرِّضَاتِ", "gloss": "the nurses", "ans": {"job": "and", "sign": "kas"},
                 "why": "After {وَ}, it copies the jarr of {الطَّبِيبَيْنِ}. A sound f. plural: kasra."},
                {"s": "الجَدِيدَاتِ", "gloss": "new", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {المُمَرِّضَاتِ}. A sound f. plural adjective in jarr: kasra."},
                {"s": "مُسْتَشْفًى", "gloss": "a hospital", "ans": {"job": "prep", "sign": "hid"},
                 "why": "After {فِي}. Maqṣūr with tanween: the kasra is hidden on the alif."},
                {"s": "كَبِيرٍ", "gloss": "big", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {مُسْتَشْفًى}. A singular adjective: kasra you can see."},
            ],
        },
    ],

    "homework": [],
}
