# Stage 5, Unit 9: Stage 5 quiz (mixed quiz over units 1-7)

# Canonical options (STAGES_5_8_SPEC.md)
DAM = {"k": "dam", "label": "Damma · ضَمَّةٌ", "color": "red"}
ALIF = {"k": "alif", "label": "Alif · الأَلِفُ", "color": "teal"}
WAW = {"k": "waw", "label": "Wāw · الوَاوُ", "color": "blue"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}

SING = {"k": "sing", "label": "Singular · مُفْرَدٌ", "color": "grey"}
DUAL = {"k": "dual", "label": "Dual · مُثَنًّى", "color": "teal"}
SMP = {"k": "smp", "label": "Sound m. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ", "color": "blue"}
SFP = {"k": "sfp", "label": "Sound f. plural · جَمْعُ مُؤَنَّثٍ سَالِمٌ", "color": "pink"}
BRK = {"k": "brk", "label": "Broken plural · جَمْعُ تَكْسِيرٍ", "color": "purple"}
FIVE = {"k": "five", "label": "Five nouns · الأَسْمَاءُ الخَمْسَةُ", "color": "gold"}

TOPIC = {"k": "topic", "label": "Topic · مُبْتَدَأٌ", "color": "gold"}
INFO = {"k": "info", "label": "Information · خَبَرٌ", "color": "red"}
VERB = {"k": "verb", "label": "Verb · فِعْلٌ", "color": "navy"}
DOER = {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"}
NAIB = {"k": "naib", "label": "Doer stand-in · نَائِبُ الفَاعِلِ", "color": "orange"}
KISM = {"k": "kism", "label": "Kāna's noun · اِسْمُ كَانَ", "color": "gold"}
IISM = {"k": "iism", "label": "Inna's noun · اِسْمُ إِنَّ", "color": "gold"}
IKHAB = {"k": "ikhab", "label": "Inna's information · خَبَرُ إِنَّ", "color": "red"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
AND = {"k": "and", "label": "After وَ (and) · مَعْطُوفٌ", "color": "blue"}
TAWK = {"k": "tawk", "label": "Emphasis · تَوْكِيدٌ", "color": "grey"}
BADAL = {"k": "badal", "label": "Substitute · بَدَلٌ", "color": "grey"}
PART = {"k": "part", "label": "Particle · حَرْفٌ", "color": "grey"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s5-quiz",
    "order": 9,
    "kind": "quiz",
    "title": "Stage 5 quiz",
    "ar": "اخْتِبَارُ المَرْفُوعَاتِ",
    "blurb": "A mixed quiz on the seven rafʿ jobs and the four signs of rafʿ.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 5 · QUIZ", "title": "Do you know your rafʿ?",
         "text": "Eight cards that cover every Stage 5 unit. Do them without your notes.",
         "wm": "المَرْفُوعَاتُ"},

        {"t": "h2", "text": "How it works"},
        {"t": "p", "text": "Do the practice cards in class, one card at a time. For each word, find the job first. The job gives the case. The kind of noun gives the sign."},
        {"t": "tip", "text": "If you miss a card, go back to its unit and read the table again. Then do the homework cards."},

        {"t": "summary", "title": "The seven topics", "items": [
            "1. Signs of rafʿ: damma, alif (dual), wāw (sound m. plural, five nouns), hidden damma ({الفَتَى}، {القَاضِي}، {كِتَابِي}).",
            "2. Topic and Information: both rafʿ. Plurals of things take a feminine singular: {الكُتُبُ جَدِيدَةٌ}.",
            "3. The doer: the verb stays singular, and takes {ت} for a feminine doer.",
            "4. The doer stand-in: passive {فُعِلَ}, the object moves into rafʿ: {كُتِبَ الدَّرْسُ}.",
            "5. Kāna and her sisters: the noun is rafʿ, the information naṣb.",
            "6. Inna and her sisters: the noun is naṣb, the information rafʿ.",
            "7. Followers: copy the case of the word before, keep your own sign.",
        ]},
    ],

    "practice": [
        # 1 · unit 1: signs of rafʿ
        {
            "title": "Which sign of rafʿ does the word in [brackets] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID]}],
            "rows": [
                {"s": "[اللَّاعِبُونَ] فِي المَلْعَبِ.", "gloss": "the players", "ans": {"sign": "waw"},
                 "why": "A sound m. plural in rafʿ: the wāw of {ـُونَ}."},
                {"s": "[الكُرَتَانِ] صَغِيرَتَانِ.", "gloss": "the two balls", "ans": {"sign": "alif"},
                 "why": "{كُرَةٌ} + {ـَانِ}: a dual. Alif."},
                {"s": "[المَبْنَى] جَمِيلٌ.", "gloss": "the building", "ans": {"sign": "hid"},
                 "why": "Maqṣūr: it ends in alif. Hidden damma."},
                {"s": "[أَبُوهُمْ] طَبِيبٌ.", "gloss": "their father", "ans": {"sign": "waw"},
                 "why": "A five noun with an owner ({ـهُمْ}): wāw."},
                {"s": "[الطَّائِرَاتُ] كَبِيرَةٌ.", "gloss": "the planes", "ans": {"sign": "dam"},
                 "why": "A sound f. plural in rafʿ: damma."},
                {"s": "[يَعْقُوبُ] نَبِيٌّ.", "gloss": "Yaʿqub", "ans": {"sign": "dam"},
                 "why": "A diptote name: one damma, no tanween."},
            ],
        },
        # 2 · unit 2: topic and information
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "أَخُو المُعَلِّمِ وَابْنُهُ صَدِيقَانِ.",
            "en": "The teacher's brother and his son are friends.",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, INFO, AND]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID]},
            ],
            "rows": [
                {"s": "أَخُو", "gloss": "the brother of", "ans": {"job": "topic", "sign": "waw"},
                 "why": "{مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ}."},
                {"s": "ابْنُهُ", "gloss": "his son", "ans": {"job": "and", "sign": "dam"},
                 "why": "After {وَ} it copies the Topic's rafʿ. {اِبْنٌ} is not a five noun: damma."},
                {"s": "صَدِيقَانِ", "gloss": "friends (two)", "ans": {"job": "info", "sign": "alif"},
                 "why": "Two men, so the Information is dual: {خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الأَلِفُ لِأَنَّهُ مُثَنًّى}."},
            ],
        },
        # 3 · unit 3: the doer
        {
            "title": "The doer: which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "حَضَرَ ___.", "gloss": "The pilots were present.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الطَّيَّارِينَ", "الطَّيَّارُونَ", "الطَّيَّارَيْنِ")},
                 "why": "Doer in rafʿ, sound m. plural: wāw."},
                {"s": "خَرَجَتِ ___.", "gloss": "The two sisters went out.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الأُخْتَيْنِ", "الأَخَوَاتُ", "الأُخْتَانِ")},
                 "why": "Two women, doer in rafʿ: alif. {الأَخَوَاتُ} is three or more."},
                {"s": "سَافَرَ ___.", "gloss": "Your (f.) father travelled.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَبَاكِ", "أَبِيكِ", "أَبُوكِ")},
                 "why": "Doer in rafʿ, a five noun with an owner: wāw."},
                {"s": "نَجَحَتْ ___.", "gloss": "Khadija passed.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("خَدِيجَةُ", "خَدِيجَةٌ", "خَدِيجَةَ")},
                 "why": "A feminine name is a diptote: one damma, no tanween."},
                {"s": "___ اللَّاعِبُونَ.", "gloss": "The players played.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لَعِبَ", "لَعِبُوا", "لَعِبَتْ")},
                 "why": "Before its doer the verb stays singular: {لَعِبَ اللَّاعِبُونَ}."},
            ],
        },
        # 4 · unit 4: the doer stand-in
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "قُرِئَ الكِتَابَانِ وَالمَقَالَاتُ.",
            "en": "The two books and the articles were read.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, NAIB, AND]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, FIXED]},
            ],
            "rows": [
                {"s": "قُرِئَ", "gloss": "was read", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A passive past verb, fixed on fatha."},
                {"s": "الكِتَابَانِ", "gloss": "the two books", "ans": {"job": "naib", "sign": "alif"},
                 "why": "{نَائِبُ فَاعِلٍ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الأَلِفُ لِأَنَّهُ مُثَنًّى}. Nobody here did the reading."},
                {"s": "المَقَالَاتُ", "gloss": "the articles", "ans": {"job": "and", "sign": "dam"},
                 "why": "After {وَ} it copies the rafʿ. A sound f. plural: damma."},
            ],
        },
        # 5 · unit 5: kāna and her sisters
        {
            "title": "Kāna and her sisters: which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "أَصْبَحَ ___ نَشِيطِينَ", "gloss": "The farmers became active.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الفَلَّاحِينَ", "الفَلَّاحُونَ", "الفَلَّاحَيْنِ")},
                 "why": "Kāna's noun is rafʿ. A sound m. plural in rafʿ: {الفَلَّاحُونَ}."},
                {"s": "ظَلَّ ___ وَاقِفَيْنِ", "gloss": "The two guards stayed standing.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الحَارِسَانِ", "الحَارِسَيْنِ", "الحُرَّاسُ")},
                 "why": "Kāna's noun is rafʿ. A dual in rafʿ: alif. {الحُرَّاسُ} is three or more."},
                {"s": "___ الطَّبِيبَاتُ مَشْغُولَاتٍ", "gloss": "The female doctors were busy.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("كَانُوا", "كَانَتِ", "كُنَّ")},
                 "why": "Women after the verb: add {ت}, keep it singular: {كَانَتِ الطَّبِيبَاتُ}."},
                {"s": "___ غَائِبَةً", "gloss": "You (f.) were absent.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("كُنْتِ", "كُنْتَ", "كَانَتْ")},
                 "why": "\"You (f.) were\" is {كُنْتِ}. The {ـتِ} is kāna's noun, in the place of rafʿ."},
                {"s": "لَيْسَ ___ سَهْلًا", "gloss": "The work is not easy.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("العَمَلَ", "العَمَلُ", "العَمَلِ")},
                 "why": "The noun of {لَيْسَ} is rafʿ: {العَمَلُ}. The naṣb goes on the information {سَهْلًا}."},
            ],
        },
        # 6 · units 6 and 7: inna
        {
            "title": "Iʿrāb of the sentence",
            "prompt": "لَعَلَّهُمَا جَارَانِ كَرِيمَانِ.",
            "en": "Perhaps they (two) are generous neighbours.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PART, IISM, IKHAB, ADJ]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, FIXED]},
            ],
            "rows": [
                {"s": "لَعَلَّ", "gloss": "perhaps", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A sister of inna. A particle, fixed on fatha."},
                {"s": "ـهُمَا", "gloss": "they (two)", "ans": {"job": "iism", "sign": "fixed"},
                 "why": "An attached pronoun, fixed. It is the noun of {لَعَلَّ}, in the place of naṣb."},
                {"s": "جَارَانِ", "gloss": "two neighbours", "ans": {"job": "ikhab", "sign": "alif"},
                 "why": "{خَبَرُ لَعَلَّ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الأَلِفُ لِأَنَّهُ مُثَنًّى}."},
                {"s": "كَرِيمَانِ", "gloss": "generous (two)", "ans": {"job": "adj", "sign": "alif"},
                 "why": "It describes {جَارَانِ} and copies its rafʿ. A dual: alif."},
            ],
        },
        # 7 · unit 7: followers
        {
            "title": "Which follower is it? Which sign?",
            "fields": [
                {"key": "job", "label": "Follower", "options": [ADJ, AND, TAWK, BADAL]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID]},
            ],
            "rows": [
                {"s": "حَضَرَ الضُّيُوفُ [كُلُّهُمْ]", "gloss": "The guests all came.", "ans": {"job": "tawk", "sign": "dam"},
                 "why": "{كُلُّهُمْ} \"all of them\": emphasis, rafʿ. {كُلُّ} is singular: damma."},
                {"s": "سَافَرَ عَمِّي [أَبُو] سَعِيدٍ", "gloss": "My uncle Abu Saʿid travelled.", "ans": {"job": "badal", "sign": "waw"},
                 "why": "The same person named again: a substitute, rafʿ. A five noun with an owner: wāw."},
                {"s": "جَاءَتِ البِنْتُ وَ[أُمُّهَا]", "gloss": "The girl and her mother came.", "ans": {"job": "and", "sign": "dam"},
                 "why": "After {وَ}, rafʿ. {أُمٌّ} is not a five noun: damma."},
                {"s": "نَجَحَ اللَّاعِبُونَ [المَاهِرُونَ]", "gloss": "The skilled players succeeded.", "ans": {"job": "adj", "sign": "waw"},
                 "why": "It describes the doer, rafʿ. A sound m. plural: wāw."},
                {"s": "رَجَعَ المُسَافِرَانِ [المُتْعَبَانِ]", "gloss": "The two tired travellers returned.", "ans": {"job": "adj", "sign": "alif"},
                 "why": "The adjective of a dual is a dual, rafʿ: alif."},
            ],
        },
        # 8 · mixed: one noun, six rafʿ jobs
        {
            "title": "What is the job of the word in [brackets]?",
            "fields": [{"key": "job", "label": "Job", "options": [TOPIC, INFO, DOER, NAIB, KISM, IKHAB]}],
            "rows": [
                {"s": "[الشَّمْسُ] طَالِعَةٌ.", "gloss": "The sun is rising.", "ans": {"job": "topic"},
                 "why": "The sentence starts with it and it has no verb before it: Topic."},
                {"s": "الشَّمْسُ [جَمِيلَةٌ].", "gloss": "The sun is beautiful.", "ans": {"job": "info"},
                 "why": "It tells us about the Topic: Information."},
                {"s": "طَلَعَتِ [الشَّمْسُ].", "gloss": "The sun rose.", "ans": {"job": "doer"},
                 "why": "{طَلَعَتْ} is an active verb. The sun did the rising: doer."},
                {"s": "خُلِقَتِ [الشَّمْسُ].", "gloss": "The sun was created.", "ans": {"job": "naib"},
                 "why": "{خُلِقَتْ} has the passive shape {فُعِلَ}: doer stand-in."},
                {"s": "كَانَتِ [الشَّمْسُ] حَارَّةً.", "gloss": "The sun was hot.", "ans": {"job": "kism"},
                 "why": "After {كَانَ}, in rafʿ: kāna's noun."},
                {"s": "إِنَّ الشَّمْسَ [حَارَّةٌ].", "gloss": "Indeed, the sun is hot.", "ans": {"job": "ikhab"},
                 "why": "After {إِنَّ} the information stays in rafʿ: inna's information."},
            ],
        },
    ],

    "homework": [
        # 1 · units 1, 2, 7
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "زَمِيلِي وَأَبُوهُ طَبِيبَانِ مَشْهُورَانِ.",
            "en": "My colleague and his father are two famous doctors.",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, INFO, ADJ, AND]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID]},
            ],
            "rows": [
                {"s": "زَمِيلِي", "gloss": "my colleague", "ans": {"job": "topic", "sign": "hid"},
                 "why": "{مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ عَلَى مَا قَبْلَ يَاءِ المُتَكَلِّمِ}."},
                {"s": "أَبُوهُ", "gloss": "his father", "ans": {"job": "and", "sign": "waw"},
                 "why": "After {وَ} it copies the Topic's rafʿ. A five noun with an owner: wāw."},
                {"s": "طَبِيبَانِ", "gloss": "two doctors", "ans": {"job": "info", "sign": "alif"},
                 "why": "Two men joined with {وَ}: a dual Information. Alif."},
                {"s": "مَشْهُورَانِ", "gloss": "famous (two)", "ans": {"job": "adj", "sign": "alif"},
                 "why": "It describes {طَبِيبَانِ} and copies its rafʿ. A dual: alif."},
            ],
        },
        # 2 · unit 1: group and sign, harder items
        {
            "title": "Which group is it? Which sign does it take in rafʿ?",
            "fields": [
                {"key": "kind", "label": "Group", "options": [SING, DUAL, SMP, SFP, BRK, FIVE]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW]},
            ],
            "rows": [
                {"s": "المُحَامُونَ", "gloss": "the lawyers", "ans": {"kind": "smp", "sign": "waw"},
                 "why": "{مُحَامٍ} + {ـُونَ}: the {ي} drops, but it is still a sound m. plural. Wāw."},
                {"s": "الأَطِبَّاءُ", "gloss": "the doctors", "ans": {"kind": "brk", "sign": "dam"},
                 "why": "{طَبِيبٌ} → {أَطِبَّاءُ}: a broken plural, and a diptote. Damma."},
                {"s": "الأَبُ", "gloss": "the father", "ans": {"kind": "sing", "sign": "dam"},
                 "why": "It has {ال} and no owner, so it is not a five noun here. A singular: damma."},
                {"s": "أَخُو سَعِيدٍ", "gloss": "Saʿid's brother", "ans": {"kind": "five", "sign": "waw"},
                 "why": "{أَخٌ} with an owner ({سَعِيدٍ}): a five noun. Wāw."},
                {"s": "الحَمَّامَاتُ", "gloss": "the bathrooms", "ans": {"kind": "sfp", "sign": "dam"},
                 "why": "{حَمَّامٌ} + {ـَاتٌ}: the singular stays whole. A sound f. plural: damma."},
                {"s": "العَيْنَانِ", "gloss": "the two eyes", "ans": {"kind": "dual", "sign": "alif"},
                 "why": "{عَيْنٌ} + {ـَانِ}: a dual. Alif."},
            ],
        },
        # 3 · units 3 and 4: doer or stand-in, harder items
        {
            "title": "Doer or doer stand-in? Which sign?",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, NAIB]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID, FIXED]},
            ],
            "rows": [
                {"s": "ـتُمْ in نُصِرْتُمْ", "gloss": "you (pl.) were helped to victory", "ans": {"job": "naib", "sign": "fixed"},
                 "why": "{نُصِرْتُمْ} is passive. The pronoun is the doer stand-in, fixed, in the place of rafʿ."},
                {"s": "أُكِلَتِ [التُّفَّاحَتَانِ].", "gloss": "The two apples were eaten.", "ans": {"job": "naib", "sign": "alif"},
                 "why": "{أُكِلَتْ} is passive: stand-in. A dual: alif."},
                {"s": "دَرَسَ [المُهَنْدِسُونَ] الخَرِيطَةَ.", "gloss": "The engineers studied the map.", "ans": {"job": "doer", "sign": "waw"},
                 "why": "{دَرَسَ} is active: doer. A sound m. plural: wāw."},
                {"s": "سُمِعَ [صَوْتُ] المُؤَذِّنِ.", "gloss": "The voice of the muezzin was heard.", "ans": {"job": "naib", "sign": "dam"},
                 "why": "{سُمِعَ} is passive: stand-in. A singular: damma."},
                {"s": "سُئِلَ [أَبُو] عَلِيٍّ.", "gloss": "Ali's father was asked.", "ans": {"job": "naib", "sign": "waw"},
                 "why": "{سُئِلَ} is passive: stand-in. A five noun with an owner: wāw."},
                {"s": "سَافَرَ [عِيسَى].", "gloss": "ʿIsa travelled.", "ans": {"job": "doer", "sign": "hid"},
                 "why": "{سَافَرَ} is active: doer. It ends in alif: hidden damma."},
            ],
        },
        # 4 · units 5 and 7: kāna with followers
        {
            "title": "Iʿrāb of the sentence",
            "prompt": "كَانَ اللَّاعِبُونَ وَالمُدَرِّبُ نَفْسُهُ مَسْرُورِينَ.",
            "en": "The players and the coach himself were happy.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, KISM, AND, TAWK]},
                {"key": "sign", "label": "Sign", "options": [DAM, WAW, HID, FIXED]},
            ],
            "rows": [
                {"s": "كَانَ", "gloss": "was", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha. It stays singular before a plural noun."},
                {"s": "اللَّاعِبُونَ", "gloss": "the players", "ans": {"job": "kism", "sign": "waw"},
                 "why": "{اِسْمُ كَانَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "المُدَرِّبُ", "gloss": "the coach", "ans": {"job": "and", "sign": "dam"},
                 "why": "After {وَ}, joined to kāna's noun, rafʿ. A singular: damma."},
                {"s": "نَفْسُهُ", "gloss": "himself", "ans": {"job": "tawk", "sign": "dam"},
                 "why": "Emphasis of {المُدَرِّبُ}, rafʿ. {نَفْسُ} is singular: damma."},
            ],
        },
        # 5 · unit 6: inna, choose the sentence
        {
            "title": "Choose the correct sentence",
            "fields": [{"key": "pick", "label": "Sentence", "options": []}],
            "rows": [
                {"s": "Perhaps the guests are hungry.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَعَلَّ الضُّيُوفَ جَائِعِينَ.", "لَعَلَّ الضُّيُوفَ جَائِعُونَ.", "لَعَلَّ الضُّيُوفُ جَائِعُونَ.")},
                 "why": "The noun of {لَعَلَّ} is naṣb: {الضُّيُوفَ}. The information stays rafʿ: {جَائِعُونَ} with wāw."},
                {"s": "Indeed, he is the owner of a car.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("إِنَّهُ ذُو سَيَّارَةٍ.", "إِنَّهُ ذَا سَيَّارَةٍ.", "إِنَّهُ ذِي سَيَّارَةٍ.")},
                 "why": "Inna's information is rafʿ. {ذُو} is a five noun: wāw."},
                {"s": "I heard that the judge is ill.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("سَمِعْتُ أَنَّ القَاضِيَ مَرِيضًا.", "سَمِعْتُ أَنَّ القَاضِي مَرِيضًا.", "سَمِعْتُ أَنَّ القَاضِيَ مَرِيضٌ.")},
                 "why": "The information of {أَنَّ} stays rafʿ: {مَرِيضٌ}. Naṣb is for kāna's information."},
                {"s": "If only they (f.) were present.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لَيْتَهُنَّ حَاضِرَاتٌ.", "لَيْتَهُنَّ حَاضِرَاتٍ.", "لَيْتَهُنَّ حَاضِرُونَ.")},
                 "why": "The information of {لَيْتَ} is rafʿ. Women: a sound f. plural with damma."},
            ],
        },
        # 6 · units 4 and 7: stand-in with followers
        {
            "title": "Iʿrāb of the sentence",
            "prompt": "سُئِلَ الطُّلَّابُ الجُدُدُ كُلُّهُمْ وَمُعَلِّمُوهُمْ.",
            "en": "The new students were all asked, and their teachers.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, NAIB, ADJ, TAWK, AND]},
                {"key": "sign", "label": "Sign", "options": [DAM, WAW, HID, FIXED]},
            ],
            "rows": [
                {"s": "سُئِلَ", "gloss": "was asked", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A passive past verb, fixed on fatha. Singular before its stand-in."},
                {"s": "الطُّلَّابُ", "gloss": "the students", "ans": {"job": "naib", "sign": "dam"},
                 "why": "{نَائِبُ فَاعِلٍ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}. A broken plural."},
                {"s": "الجُدُدُ", "gloss": "the new", "ans": {"job": "adj", "sign": "dam"},
                 "why": "It describes the stand-in and copies rafʿ. {جُدُدٌ} is a broken plural: damma."},
                {"s": "كُلُّهُمْ", "gloss": "all of them", "ans": {"job": "tawk", "sign": "dam"},
                 "why": "Emphasis of the stand-in, rafʿ. {كُلُّ} is singular: damma."},
                {"s": "مُعَلِّمُوهُمْ", "gloss": "their teachers", "ans": {"job": "and", "sign": "waw"},
                 "why": "After {وَ}, rafʿ. A sound m. plural: wāw. The {ن} dropped before the owner {ـهُمْ}."},
            ],
        },
    ],
}
