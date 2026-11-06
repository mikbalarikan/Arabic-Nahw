# Stage 6, Unit 7: Stage 6 quiz (mixed quiz over units 1-5)

KAS = {"k": "kas", "label": "Kasra · كَسْرَةٌ", "color": "green"}
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
YA = {"k": "ya", "label": "Yāʾ · اليَاءُ", "color": "purple"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}
JSIGNS = [KAS, YA, FAT, HID]
OSIGNS = [KAS, YA, FAT, HID, FIXED]
PSIGNS = [KAS, YA, HID, FIXED]

PREP = {"k": "prep", "label": "After a preposition · اِسْمٌ مَجْرُورٌ", "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
AND = {"k": "and", "label": "After وَ (and) · مَعْطُوفٌ", "color": "blue"}
TAWK = {"k": "tawk", "label": "Emphasis · تَوْكِيدٌ", "color": "grey"}
BADAL = {"k": "badal", "label": "Substitute · بَدَلٌ", "color": "grey"}
JOBS = [PREP, OWNER, ADJ, AND]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s6-quiz",
    "order": 7,
    "kind": "quiz",
    "title": "Stage 6 quiz",
    "ar": "اخْتِبَارُ المَجْرُورَاتِ",
    "blurb": "A mixed quiz on all five Stage 6 topics: the signs of jarr, prepositions, the owner, diptotes and followers.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 6 · QUIZ", "title": "Do you know your jarr?",
         "text": "Eight cards that cover every Stage 6 unit. Do them without your notes.",
         "wm": "المَجْرُورَاتُ"},

        {"t": "h2", "text": "How it works"},
        {"t": "p", "text": "Do the practice cards in class, one card at a time. For each word, find the job first. The job gives the case. The kind of noun gives the sign."},
        {"t": "tip", "text": "If you miss a card, go back to its unit and read the table again. Then do the homework cards."},

        {"t": "summary", "title": "The five topics", "items": [
            "1. The signs of jarr: kasra, yāʾ, fatha for a diptote, hidden kasra.",
            "2. After a preposition: the noun is always jarr. A pronoun is fixed, in the place of jarr: {عَلَيْهِ}.",
            "3. The owner is always jarr. The first noun drops {ال}, tanween and the {ن}: {مُعَلِّمِي المَدْرَسَةِ}.",
            "4. A diptote takes fatha in jarr: {بِأَحْمَدَ}. With {ال} or an owner it takes kasra: {فِي المَسَاجِدِ}.",
            "5. Followers copy the jarr. Their own kind gives the sign: {فِي مَسَاجِدَ كَثِيرَةٍ}.",
        ]},
    ],

    "practice": [
        # 1 · unit 1: the four signs
        {
            "title": "Which sign of jarr does the word in [brackets] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "خَرَجْتُ مِنَ [المَطْبَخِ]", "gloss": "I went out of the kitchen.", "ans": {"sign": "kas"},
                 "why": "A singular: {اِسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}."},
                {"s": "سَلَّمْتُ عَلَى [اللَّاعِبِينَ]", "gloss": "I greeted the players.", "ans": {"sign": "ya"},
                 "why": "Kasra before {ي}: a sound m. plural. The sign is the {ي}."},
                {"s": "نَظَرْتُ إِلَى [البَابَيْنِ]", "gloss": "I looked at the two doors.", "ans": {"sign": "ya"},
                 "why": "Fatha before {ي}: a dual. The sign is the {ي}."},
                {"s": "جَلَسْنَا فِي [المَبْنَى]", "gloss": "We sat in the building.", "ans": {"sign": "hid"},
                 "why": "Maqṣūr: it ends in alif. The kasra is hidden."},
                {"s": "سَافَرْتُ إِلَى [مُدُنٍ] كَثِيرَةٍ", "gloss": "I travelled to many cities.", "ans": {"sign": "kas"},
                 "why": "{مُدُنٌ} is a broken plural on {فُعُلٌ}. It takes tanween, so it is not a diptote: kasra."},
                {"s": "عَمِلْتُ فِي [مَصَانِعَ] كَبِيرَةٍ", "gloss": "I worked in big factories.", "ans": {"sign": "fat"},
                 "why": "{مَصَانِعُ} is a long plural, a diptote. No {ال}, no owner: fatha in place of kasra."},
            ],
        },
        # 2 · unit 2: prepositions and pronouns
        {
            "title": "Find the jarr job and the sign",
            "prompt": "كَتَبْتُ لَهُمْ رِسَالَةً مِنَ القَرْيَةِ عَنْ أَخِي الصَّغِيرِ.",
            "en": "I wrote them a letter from the village about my little brother.",
            "fields": [{"key": "job", "label": "Job", "options": JOBS},
                       {"key": "sign", "label": "Sign", "options": PSIGNS}],
            "rows": [
                {"s": "لَهُمْ", "gloss": "for them (the pronoun هُمْ)", "ans": {"job": "prep", "sign": "fixed"},
                 "why": "{هُمْ} comes after {لِـ}. It is an attached pronoun: fixed, in the place of jarr."},
                {"s": "القَرْيَةِ", "gloss": "the village", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {مِنْ}. A singular: {اِسْمٌ مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}."},
                {"s": "أَخِي", "gloss": "my brother", "ans": {"job": "prep", "sign": "hid"},
                 "why": "After {عَنْ}. Here {ـي} means \"my\", so the kasra is hidden."},
                {"s": "الصَّغِيرِ", "gloss": "little", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {أَخِي}, so it is jarr too. A singular: kasra you can see."},
            ],
        },
        # 3 · unit 2: every kind of noun after a preposition
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "سَلَّمْتُ عَلَى ___", "gloss": "the travellers", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُسَافِرُونَ", "المُسَافِرِينَ", "المُسَافِرَيْنِ")},
                 "why": "A sound m. plural in jarr: {ـِينَ}. {ـُونَ} is rafʿ. {ـَيْنِ} is a dual."},
                {"s": "ذَهَبْتُ إِلَى ___", "gloss": "your father (said to a woman)", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَبُوكِ", "أَبَاكِ", "أَبِيكِ")},
                 "why": "A five noun in jarr: {ي}."},
                {"s": "سَأَلْتُ عَنْ ___", "gloss": "a lawyer", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُحَامٍ", "مُحَامِي", "مُحَامِيٍ")},
                 "why": "Manqūṣ with no {ال}: the {ي} drops and the kasra is hidden."},
                {"s": "جَاءَ طُلَّابٌ مِنْ ___ كَثِيرَةٍ", "gloss": "Students came from many countries.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بِلَادٍ", "بِلَادَ", "بِلَادِ")},
                 "why": "{بِلَادٌ} is a broken plural with tanween, not a diptote: kasra with tanween."},
                {"s": "تَعَلَّمْتُ مِنَ ___", "gloss": "the two female doctors", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الطَّبِيبَتَانِ", "الطَّبِيبَتَيْنِ", "الطَّبِيبَاتُ")},
                 "why": "A dual in jarr: {ـَيْنِ}."},
                {"s": "أَرْسَلْتُ الهَدِيَّةَ إِلَى ___", "gloss": "Sulayman", "ans": {"pick": "a"},
                 "opts": {"pick": pick("سُلَيْمَانَ", "سُلَيْمَانٍ", "سُلَيْمَانِ")},
                 "why": "A name ending in {ـَانُ} is a diptote: fatha in place of kasra, no tanween."},
            ],
        },
        # 4 · unit 3: iḍāfa in a sentence
        {
            "title": "Find the jarr job and the sign",
            "prompt": "قَرَأْتُ رِسَالَةَ أَبِي يُوسُفَ إِلَى مُعَلِّمِي ابْنِهِ.",
            "en": "I read Abu Yusuf's letter to his son's teachers.",
            "fields": [{"key": "job", "label": "Job", "options": JOBS},
                       {"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "أَبِي", "gloss": "father (of)", "ans": {"job": "owner", "sign": "ya"},
                 "why": "It owns {رِسَالَةَ}. It is owned by {يُوسُفَ}, so it is a five noun: yāʾ. It does not mean \"my\" here."},
                {"s": "يُوسُفَ", "gloss": "Yusuf", "ans": {"job": "owner", "sign": "fat"},
                 "why": "It owns {أَبِي}. A foreign name: fatha in place of kasra."},
                {"s": "مُعَلِّمِي", "gloss": "teachers (of)", "ans": {"job": "prep", "sign": "ya"},
                 "why": "After {إِلَى}. A sound m. plural that drops its {ن} in iḍāfa: {مُعَلِّمِينَ} → {مُعَلِّمِي}. The {ي} is the sign of jarr."},
                {"s": "ابْنِهِ", "gloss": "his son", "ans": {"job": "owner", "sign": "kas"},
                 "why": "It owns {مُعَلِّمِي}. A singular: kasra."},
            ],
        },
        # 5 · unit 3: the owner's sign
        {
            "title": "Which sign does the owner take?",
            "fields": [{"key": "sign", "label": "Sign", "options": OSIGNS}],
            "rows": [
                {"s": "صَوْتُ [المُؤَذِّنِ]", "gloss": "the voice of the muezzin", "ans": {"sign": "kas"},
                 "why": "A singular owner: {مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}."},
                {"s": "مَلَابِسُ [اللَّاعِبَيْنِ]", "gloss": "the two players' clothes", "ans": {"sign": "ya"},
                 "why": "Fatha before {ي}: a dual owner. The sign is {ي}."},
                {"s": "سَيَّارَتُهُمْ", "gloss": "their car (the owner is \"their\")", "ans": {"sign": "fixed"},
                 "why": "{هُمْ} is an attached pronoun: fixed, in the place of jarr."},
                {"s": "حَقِيبَةُ [خَدِيجَةَ]", "gloss": "Khadija's bag", "ans": {"sign": "fat"},
                 "why": "A feminine name is a diptote: fatha in place of kasra."},
                {"s": "مَكْتَبُ [أَخِيهَا]", "gloss": "her brother's office", "ans": {"sign": "ya"},
                 "why": "A five noun with the owner {هَا}: yāʾ."},
                {"s": "طَعَامُ [الفَتَى]", "gloss": "the young man's food", "ans": {"sign": "hid"},
                 "why": "Maqṣūr: the kasra is hidden on the alif."},
            ],
        },
        # 6 · unit 4: diptotes in a sentence
        {
            "title": "Job and sign",
            "prompt": "سَلَّمْتُ عَلَى عُمَرَ وَأَصْدِقَائِهِ فِي شَوَارِعِ مَكَّةَ.",
            "en": "I greeted Umar and his friends in the streets of Makkah.",
            "fields": [{"key": "job", "label": "Job", "options": [PREP, OWNER, AND]},
                       {"key": "sign", "label": "Sign", "options": [KAS, FAT]}],
            "rows": [
                {"s": "عُمَرَ", "gloss": "Umar", "ans": {"job": "prep", "sign": "fat"},
                 "why": "After {عَلَى}. A name on {فُعَلُ}: {اِسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الفَتْحَةُ نِيَابَةً عَنِ الكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ}."},
                {"s": "أَصْدِقَائِهِ", "gloss": "his friends", "ans": {"job": "and", "sign": "kas"},
                 "why": "After {وَ}, it copies the jarr of {عُمَرَ}. A diptote, but it has an owner, {هِ}: kasra."},
                {"s": "شَوَارِعِ", "gloss": "streets", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {فِي}. A long plural, but it has an owner: kasra."},
                {"s": "مَكَّةَ", "gloss": "Makkah", "ans": {"job": "owner", "sign": "fat"},
                 "why": "It owns {شَوَارِعِ}. A city name is feminine, a diptote: fatha in place of kasra."},
            ],
        },
        # 7 · unit 5: adjective and after وَ
        {
            "title": "Job and sign",
            "prompt": "تَكَلَّمْتُ مَعَ المُدِيرِ عَنِ الطُّلَّابِ النَّاجِحِينَ وَآبَائِهِمْ.",
            "en": "I talked with the headmaster about the successful students and their fathers.",
            "fields": [{"key": "job", "label": "Job", "options": JOBS},
                       {"key": "sign", "label": "Sign", "options": [KAS, YA, FAT]}],
            "rows": [
                {"s": "المُدِيرِ", "gloss": "the headmaster", "ans": {"job": "owner", "sign": "kas"},
                 "why": "{مَعَ} is not a preposition. The noun after it is its owner: kasra."},
                {"s": "الطُّلَّابِ", "gloss": "the students", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {عَنْ}. A broken plural: kasra."},
                {"s": "النَّاجِحِينَ", "gloss": "successful", "ans": {"job": "adj", "sign": "ya"},
                 "why": "It describes {الطُّلَّابِ}. A sound m. plural adjective: {نَعْتٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ}."},
                {"s": "آبَائِهِمْ", "gloss": "their fathers", "ans": {"job": "and", "sign": "kas"},
                 "why": "After {وَ}, it copies the jarr of {الطُّلَّابِ}. {آبَاءٌ} is a broken plural: kasra. Only the singular {أَبٌ} is a five noun."},
            ],
        },
        # 8 · unit 5: emphasis and substitute
        {
            "title": "Job and sign",
            "prompt": "سَأَلْتُ عَنْ صَدِيقِكَ أَحْمَدَ وَعَنِ الضُّيُوفِ أَنْفُسِهِمْ.",
            "en": "I asked about your friend Ahmad and about the guests themselves.",
            "fields": [{"key": "job", "label": "Job", "options": [PREP, AND, TAWK, BADAL]},
                       {"key": "sign", "label": "Sign", "options": [KAS, FAT, YA]}],
            "rows": [
                {"s": "صَدِيقِكَ", "gloss": "your friend", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {عَنْ}. A singular: kasra."},
                {"s": "أَحْمَدَ", "gloss": "Ahmad", "ans": {"job": "badal", "sign": "fat"},
                 "why": "It names your friend again: a substitute in jarr. A diptote name: fatha in place of kasra."},
                {"s": "الضُّيُوفِ", "gloss": "the guests", "ans": {"job": "prep", "sign": "kas"},
                 "why": "{عَنْ} comes again, so this noun is after a preposition, not a follower. A broken plural: kasra."},
                {"s": "أَنْفُسِهِمْ", "gloss": "themselves", "ans": {"job": "tawk", "sign": "kas"},
                 "why": "{أَنْفُسُ} + a matching pronoun: emphasis in jarr. {أَنْفُسٌ} is a broken plural: kasra."},
            ],
        },
    ],

    "homework": [
        # 1 · units 1 and 4: all the signs, a little harder
        {
            "title": "Which sign of jarr does the word in [brackets] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "سَلَّمْتُ عَلَى [رَاعٍ]", "gloss": "I greeted a shepherd.", "ans": {"sign": "hid"},
                 "why": "Manqūṣ with no {ال}: the {ي} drops. The kasra is hidden on it. The tanween is not the sign."},
                {"s": "سَلَّمْتُ عَلَى [أَخِي] سَعِيدٍ", "gloss": "I greeted Saeed's brother.", "ans": {"sign": "ya"},
                 "why": "{أَخِي} is owned by {سَعِيدٍ}. It is a five noun, and the {ي} is the sign of jarr. It does not mean \"my\" here."},
                {"s": "سَأَلْتُ عَنِ [ابْنِي]", "gloss": "I asked about my son.", "ans": {"sign": "hid"},
                 "why": "Here {ـي} means \"my\". The kasra is hidden. {ابْنٌ} is not a five noun."},
                {"s": "مَرَرْتُ بِ[صَحْرَاءَ] وَاسِعَةٍ", "gloss": "I passed by a wide desert.", "ans": {"sign": "fat"},
                 "why": "{صَحْرَاءُ} has the extra {ـَاءُ}, a diptote. No {ال}, no owner: fatha in place of kasra."},
                {"s": "كَتَبْتُ عَنِ [الوُزَرَاءِ]", "gloss": "I wrote about the ministers.", "ans": {"sign": "kas"},
                 "why": "{وُزَرَاءُ} is a diptote, but here it has {ال}: kasra."},
                {"s": "جَلَسْتُ مَعَ [المُعَلِّمَيْنِ]", "gloss": "I sat with the two teachers.", "ans": {"sign": "ya"},
                 "why": "The owner of {مَعَ}. Fatha before {ي}: a dual, yāʾ."},
            ],
        },
        # 2 · units 2 and 3: prepositions and owners
        {
            "title": "Find the jarr job and the sign",
            "prompt": "خَرَجَ أَبُو سَعِيدٍ مِنْ بَيْتِ جَارِهِ إِلَى المُصَلَّى فِي سَيَّارَةِ ابْنَيْهِ.",
            "en": "Abu Saeed went out of his neighbour's house to the prayer hall in his two sons' car.",
            "fields": [{"key": "job", "label": "Job", "options": JOBS},
                       {"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "سَعِيدٍ", "gloss": "Saeed", "ans": {"job": "owner", "sign": "kas"},
                 "why": "It owns {أَبُو}. {سَعِيدٌ} is not a diptote: kasra with tanween."},
                {"s": "بَيْتِ", "gloss": "house", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {مِنْ}. A singular: kasra. It is owned, so no tanween."},
                {"s": "جَارِهِ", "gloss": "his neighbour", "ans": {"job": "owner", "sign": "kas"},
                 "why": "It owns {بَيْتِ}. A singular: kasra."},
                {"s": "المُصَلَّى", "gloss": "the prayer hall", "ans": {"job": "prep", "sign": "hid"},
                 "why": "After {إِلَى}. Maqṣūr: the kasra is hidden on the alif."},
                {"s": "ابْنَيْهِ", "gloss": "his two sons", "ans": {"job": "owner", "sign": "ya"},
                 "why": "It owns {سَيَّارَةِ}. A dual that drops its {ن} before {هِ}: {ابْنَيْنِ} → {ابْنَيْهِ}. The {ي} is the sign."},
            ],
        },
        # 3 · unit 3: which phrase is right?
        {
            "title": "Which phrase is right?",
            "fields": [{"key": "pick", "label": "Phrase", "options": []}],
            "rows": [
                {"s": "the two engineers' office", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَكْتَبُ المُهَنْدِسَانِ", "مَكْتَبُ المُهَنْدِسَيْنِ", "المَكْتَبُ المُهَنْدِسَيْنِ")},
                 "why": "The owner is a dual in jarr: {ـَيْنِ}. The first noun has no {ال}."},
                {"s": "about the school's players", "ans": {"pick": "a"},
                 "opts": {"pick": pick("عَنْ لَاعِبِي المَدْرَسَةِ", "عَنْ لَاعِبِينَ المَدْرَسَةِ", "عَنْ لَاعِبُو المَدْرَسَةِ")},
                 "why": "After {عَنْ}, jarr: {ي}. The {ن} drops in iḍāfa."},
                {"s": "The doctor's two daughters came.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("جَاءَتْ بِنْتَانِ الطَّبِيبِ", "جَاءَتِ البِنْتَانِ الطَّبِيبِ", "جَاءَتْ بِنْتَا الطَّبِيبِ")},
                 "why": "Doer, rafʿ: alif. A dual first noun drops its {ن} and has no {ال}."},
                {"s": "Maryam's father's car", "ans": {"pick": "a"},
                 "opts": {"pick": pick("سَيَّارَةُ أَبِي مَرْيَمَ", "سَيَّارَةُ أَبُو مَرْيَمَ", "سَيَّارَةُ أَبِي مَرْيَمٍ")},
                 "why": "{أَبِي} is the owner, in jarr: yāʾ. {مَرْيَمَ} is a diptote owner: fatha, no tanween."},
                {"s": "the lawyer's office", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَكْتَبُ المُحَامٍ", "مَكْتَبُ المُحَامِي", "مَكْتَبُ المُحَامِ")},
                 "why": "Manqūṣ with {ال}: the {ي} stays and the kasra is hidden."},
                {"s": "the door of my father's house", "ans": {"pick": "c"},
                 "opts": {"pick": pick("بَابُ البَيْتِ أَبِي", "بَابُ بَيْتُ أَبِي", "بَابُ بَيْتِ أَبِي")},
                 "why": "{بَيْتِ} owns {بَابُ}, so it is jarr. It is also a first noun, so no {ال}."},
            ],
        },
        # 4 · unit 4: diptotes with and without an owner
        {
            "title": "Job and sign",
            "prompt": "صَلَّيْتُ فِي أَكْبَرِ مَسَاجِدِ المَدِينَةِ مَعَ زُمَلَاءَ كَثِيرِينَ.",
            "en": "I prayed in the biggest of the city's mosques with many colleagues.",
            "fields": [{"key": "job", "label": "Job", "options": [PREP, OWNER, ADJ]},
                       {"key": "sign", "label": "Sign", "options": [KAS, YA, FAT]}],
            "rows": [
                {"s": "أَكْبَرِ", "gloss": "the biggest", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {فِي}. {أَكْبَرُ} is a diptote, but it has an owner: kasra."},
                {"s": "مَسَاجِدِ", "gloss": "mosques", "ans": {"job": "owner", "sign": "kas"},
                 "why": "It owns {أَكْبَرِ}. A long plural, but it has its own owner, {المَدِينَةِ}: kasra."},
                {"s": "المَدِينَةِ", "gloss": "the city", "ans": {"job": "owner", "sign": "kas"},
                 "why": "It owns {مَسَاجِدِ}. A singular: kasra."},
                {"s": "زُمَلَاءَ", "gloss": "colleagues", "ans": {"job": "owner", "sign": "fat"},
                 "why": "The owner of {مَعَ}. The extra {ـَاءُ}, no {ال}, no owner: fatha in place of kasra."},
                {"s": "كَثِيرِينَ", "gloss": "many", "ans": {"job": "adj", "sign": "ya"},
                 "why": "It describes {زُمَلَاءَ}, so it is jarr. A sound m. plural: yāʾ. Do not copy the fatha."},
            ],
        },
        # 5 · unit 5: which word does the adjective follow?
        {
            "title": "Which word does the adjective in [brackets] follow?",
            "fields": [{"key": "pick", "label": "It follows", "options": []}],
            "rows": [
                {"s": "زُرْتُ صَدِيقَ الطَّبِيبِ [المَرِيضَ]", "gloss": "I visited the doctor's sick friend.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("صَدِيقَ", "الطَّبِيبِ")},
                 "why": "Fatha, like {صَدِيقَ}, the object in naṣb."},
                {"s": "زُرْتُ صَدِيقَ الطَّبِيبِ [المَرِيضِ]", "gloss": "I visited the sick doctor's friend.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("صَدِيقَ", "الطَّبِيبِ")},
                 "why": "Kasra, like {الطَّبِيبِ}, the owner in jarr."},
                {"s": "هَذَا قَلَمُ البِنْتِ [الجَمِيلُ]", "gloss": "This is the girl's beautiful pen.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("قَلَمُ", "البِنْتِ")},
                 "why": "Damma, like {قَلَمُ}, the information in rafʿ. It is also masculine, like {قَلَمُ}."},
                {"s": "سَكَنْتُ فِي شَقَّةِ الرَّجُلِ [الغَنِيِّ]", "gloss": "I lived in the rich man's flat.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("شَقَّةِ", "الرَّجُلِ")},
                 "why": "Both are in jarr. {الغَنِيِّ} is masculine, like {الرَّجُلِ}. For the flat it would be {الغَنِيَّةِ}."},
                {"s": "سَأَلْتُ عَنْ أُمِّ الطِّفْلِ [الصَّغِيرِ]", "gloss": "I asked about the little child's mother.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أُمِّ", "الطِّفْلِ")},
                 "why": "Both are in jarr. {الصَّغِيرِ} is masculine, like {الطِّفْلِ}. For the mother it would be {الصَّغِيرَةِ}."},
            ],
        },
        # 6 · mixed: the whole stage in one sentence
        {
            "title": "Job and sign",
            "prompt": "تَكَلَّمْتُ عَنْ أَبِيكَ وَصَدِيقِهِ يُوسُفَ فِي مَقْهًى قَرِيبٍ.",
            "en": "I talked about your father and his friend Yusuf in a nearby café.",
            "fields": [{"key": "job", "label": "Job", "options": [PREP, ADJ, AND, BADAL]},
                       {"key": "sign", "label": "Sign", "options": JSIGNS}],
            "rows": [
                {"s": "أَبِيكَ", "gloss": "your father", "ans": {"job": "prep", "sign": "ya"},
                 "why": "After {عَنْ}. A five noun with an owner: {اِسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ}."},
                {"s": "صَدِيقِهِ", "gloss": "his friend", "ans": {"job": "and", "sign": "kas"},
                 "why": "After {وَ}, it copies the jarr of {أَبِيكَ}. A singular: kasra."},
                {"s": "يُوسُفَ", "gloss": "Yusuf", "ans": {"job": "badal", "sign": "fat"},
                 "why": "It names his friend again: a substitute in jarr. A foreign name: fatha in place of kasra."},
                {"s": "مَقْهًى", "gloss": "a café", "ans": {"job": "prep", "sign": "hid"},
                 "why": "After {فِي}. Maqṣūr with tanween: the kasra is hidden on the alif."},
                {"s": "قَرِيبٍ", "gloss": "nearby", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {مَقْهًى}. A singular adjective: kasra you can see."},
            ],
        },
    ],
}
