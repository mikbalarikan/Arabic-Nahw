# Stage 8, Unit 2: The present verb in rafʿ (رَفْعُ الفِعْلِ المُضَارِعِ)

DAM = {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
FAT = {"k": "fat",   "label": "Fatha · فَتْحَةٌ",                "color": "pink"}
KAS = {"k": "kas",   "label": "Kasra · كَسْرَةٌ",                "color": "green"}
SUK = {"k": "suk",   "label": "Sukūn · سُكُونٌ",                 "color": "navy"}
ALIF = {"k": "alif",  "label": "Alif · الأَلِفُ",                  "color": "teal"}
WAW = {"k": "waw",   "label": "Wāw · الوَاوُ",                   "color": "blue"}
HID = {"k": "hid",   "label": "Hidden vowel · مُقَدَّرَةٌ",         "color": "brown"}

TOPIC = {"k": "topic", "label": "Topic · مُبْتَدَأٌ",                  "color": "gold"}
VERB = {"k": "verb",  "label": "Verb · فِعْلٌ",                       "color": "navy"}
DOER = {"k": "doer",  "label": "Doer · فَاعِلٌ",                      "color": "orange"}
PREP = {"k": "prep",  "label": "After a preposition · اِسْمٌ مَجْرُورٌ",    "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ",               "color": "purple"}
AND = {"k": "and",   "label": "After وَ (and) · مَعْطُوفٌ",              "color": "blue"}
OBJ = {"k": "obj",   "label": "Object · مَفْعُولٌ بِهِ",                "color": "pink"}
WHEN = {"k": "when",  "label": "Time/place · مَفْعُولٌ فِيهِ",            "color": "brown"}

SHOW = {"k": "show", "label": "It shows · ظَاهِرَةٌ", "color": "red"}
HEAVY = {"k": "heavy", "label": "Too heavy on و / ي · لِلثِّقَلِ", "color": "brown"}
IMPOS = {"k": "impos", "label": "Impossible on alif · لِلتَّعَذُّرِ", "color": "orange"}
WHYH = [SHOW, HEAVY, IMPOS]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s8-rafa",
    "order": 2,
    "title": "The present verb in rafʿ",
    "ar": "رَفْعُ الفِعْلِ المُضَارِعِ",
    "blurb": "With no particle before it, the present verb is in rafʿ: a damma, or a hidden damma on a weak ending.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 8 · UNIT 2", "title": "No particle, so rafʿ",
         "text": "When nothing of naṣb or jazm comes before it, the present verb is in rafʿ. This is its normal state.",
         "wm": "يَكْتُبُ"},

        {"t": "h2", "text": "The rule"},
        {"t": "rule", "color": "red", "title": "Free of naṣb and jazm → rafʿ",
         "text": "A present verb is in rafʿ when no particle of naṣb and no particle of jazm comes before it. Arabic says: {مَرْفُوعٌ لِتَجَرُّدِهِ مِنَ النَّاصِبِ وَالجَازِمِ} \"in rafʿ because it is free of a naṣb or jazm word\"."},
        {"t": "p", "text": "For nouns, the job gives the case. For the present verb, the word before it gives the case. No such word means rafʿ."},
        {"t": "table", "head": ["Before the verb", "Case", "Example"], "rows": [
            ["nothing", "rafʿ", "يَكْتُبُ"],
            ["{سَـ} or {سَوْفَ} \"will\"", "rafʿ", "سَيَكْتُبُ، سَوْفَ يَكْتُبُ"],
            ["{لَا} \"not\"", "rafʿ", "لَا يَكْتُبُ"],
            ["a particle of naṣb", "naṣb", "لَنْ يَكْتُبَ (Unit 4)"],
            ["a particle of jazm", "jazm", "لَمْ يَكْتُبْ (Unit 5)"],
        ]},
        {"t": "tip", "text": "{سَـ}، {سَوْفَ} and {لَا} \"not\" do not change the case. Unit 5 shows a different {لَا}, \"don't!\", that does."},

        {"t": "h2", "text": "The sign: damma"},
        {"t": "p", "text": "Most present verbs show the damma on the last letter."},
        {"t": "words", "items": [
            {"ar": "يَكْتُبُ", "sub": "he writes", "color": "red"},
            {"ar": "أَقْرَأُ", "sub": "I read", "color": "red"},
            {"ar": "نَجْلِسُ", "sub": "we sit", "color": "red"},
            {"ar": "تَفْتَحُ", "sub": "you open", "color": "red"},
            {"ar": "يُسَاعِدُ", "sub": "he helps", "color": "red"},
        ]},
        {"t": "examples", "items": [
            {"ar": "يَكْتُبُ", "en": "he writes",
             "note": "{فِعْلٌ مُضَارِعٌ مَرْفُوعٌ لِتَجَرُّدِهِ مِنَ النَّاصِبِ وَالجَازِمِ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ}"},
        ]},
        {"t": "tip", "text": "{أَقْرَأُ} ends in hamza. The hamza is a strong letter, so the damma shows on it."},

        {"t": "h2", "text": "Weak endings: the damma is hidden"},
        {"t": "p", "text": "Some present verbs end in a long letter: {و}، {ي} or {ا} (written {ى}). These letters do not carry the damma. The damma is there, but hidden ({مُقَدَّرَةٌ}). It is the original sign, only hidden."},
        {"t": "table", "head": ["Past", "Present (rafʿ)", "Meaning", "Last letter", "Why hidden"], "rows": [
            ["دَعَا", "يَدْعُو", "he calls, he prays", "{و}", "too heavy"],
            ["رَجَا", "يَرْجُو", "he hopes", "{و}", "too heavy"],
            ["رَمَى", "يَرْمِي", "he throws", "{ي}", "too heavy"],
            ["مَشَى", "يَمْشِي", "he walks", "{ي}", "too heavy"],
            ["سَعَى", "يَسْعَى", "he strives, he hurries", "{ى}", "impossible"],
            ["نَسِيَ", "يَنْسَى", "he forgets", "{ى}", "impossible"],
        ]},
        {"t": "rule", "color": "brown", "title": "Heavy or impossible",
         "text": "On {و} and {ي} a damma is possible but too heavy to say ({لِلثِّقَلِ}). On an alif no vowel can sit at all ({لِلتَّعَذُّرِ})."},
        {"t": "examples", "items": [
            {"ar": "يَدْعُو المُسْلِمُ رَبَّهُ.", "en": "The Muslim prays to his Lord.",
             "note": "{يَدْعُو}: {فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ عَلَى الوَاوِ لِلثِّقَلِ}"},
            {"ar": "يَرْمِي الوَلَدُ الكُرَةَ.", "en": "The boy throws the ball.",
             "note": "{يَرْمِي}: hidden damma on the {ي}, too heavy."},
            {"ar": "يَسْعَى الطَّالِبُ إِلَى العِلْمِ.", "en": "The student strives for knowledge.",
             "note": "{يَسْعَى}: {فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ عَلَى الأَلِفِ لِلتَّعَذُّرِ}"},
        ]},
        {"t": "tip", "text": "Never write a damma on these letters: {يَدْعُوُ} and {يَرْمِيُ} are mistakes. Write {يَدْعُو}، {يَرْمِي}."},

        {"t": "h2", "text": "A verb sentence with a present verb"},
        {"t": "p", "text": "The verb sentence works as in Stage 2. Only the verb is new. Here is the full iʿrāb of every word."},
        {"t": "examples", "items": [
            {"ar": "يَكْتُبُ الطَّالِبُ الدَّرْسَ.", "en": "The student writes the lesson."},
        ]},
        {"t": "table", "head": ["Word", "Job", "Iʿrāb"], "rows": [
            ["يَكْتُبُ", "verb", "{فِعْلٌ مُضَارِعٌ مَرْفُوعٌ لِتَجَرُّدِهِ مِنَ النَّاصِبِ وَالجَازِمِ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}"],
            ["الطَّالِبُ", "doer", "{فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}"],
            ["الدَّرْسَ", "object", "{مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}"],
        ]},
        {"t": "tip", "text": "When a noun is the doer, the verb stays in the \"he\" or \"she\" form, even for two or many: {يَذْهَبُ الطُّلَّابُ}، {تَذْهَبُ البَنَاتُ}."},

        {"t": "h2", "text": "Doers with branch signs"},
        {"t": "p", "text": "The doer can be any kind of noun. Use the signs from Stage 5."},
        {"t": "examples", "items": [
            {"ar": "يَذْهَبُ المُسْلِمُونَ إِلَى المَسْجِدِ.", "en": "The Muslims go to the mosque.",
             "note": "{المُسْلِمُونَ}: {فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}"},
            {"ar": "يَجْلِسُ الطَّالِبَانِ فِي الفَصْلِ.", "en": "The two students sit in the classroom.",
             "note": "{الطَّالِبَانِ}: doer in rafʿ, sign alif, because it is dual."},
            {"ar": "يَحْضُرُ أَبُوكَ.", "en": "Your father comes.",
             "note": "{أَبُوكَ}: doer in rafʿ, sign wāw, one of the five nouns."},
            {"ar": "يَمْشِي القَاضِي.", "en": "The judge walks.",
             "note": "Two hidden dammas: on the {ي} of the verb and on the {ي} of {القَاضِي}."},
        ]},

        {"t": "h2", "text": "The verb after its doer"},
        {"t": "p", "text": "When the noun comes first, it is the Topic. The verb follows with a hidden doer. The verb sentence is the Information."},
        {"t": "examples", "items": [
            {"ar": "المُعَلِّمُ يَشْرَحُ الدَّرْسَ.", "en": "The teacher explains the lesson.",
             "note": "{المُعَلِّمُ}: Topic. {يَشْرَحُ}: present verb in rafʿ, damma. Its doer is hidden: {هُوَ}."},
            {"ar": "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ.", "en": "You alone we worship, and You alone we ask for help. (al-Fātiḥa 1:5)",
             "note": "{نَعْبُدُ} and {نَسْتَعِينُ}: present verbs in rafʿ, damma. No particle comes before them."},
        ]},

        {"t": "summary", "title": "In short", "items": [
            "No particle of naṣb or jazm before it: the present verb is in rafʿ.",
            "{سَـ}، {سَوْفَ} and {لَا} \"not\" do not change that.",
            "The sign is damma: {يَكْتُبُ}، {أَقْرَأُ}.",
            "On {و} and {ي} the damma is hidden, too heavy: {يَدْعُو}، {يَرْمِي}.",
            "On alif it is hidden, impossible: {يَسْعَى}، {يَنْسَى}.",
            "The formula: {فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "يَكْتُبُ الطَّالِبُ الدَّرْسَ فِي الفَصْلِ.",
            "en": "The student writes the lesson in the classroom.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, PREP]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, SUK, HID]},
            ],
            "rows": [
                {"s": "يَكْتُبُ", "ans": {"job": "verb", "sign": "dam"}, "why": "A present verb with no particle before it: rafʿ, damma."},
                {"s": "الطَّالِبُ", "ans": {"job": "doer", "sign": "dam"}, "why": "The one who writes: doer, rafʿ, damma."},
                {"s": "الدَّرْسَ", "ans": {"job": "obj", "sign": "fat"}, "why": "What is written: object, naṣb, fatha."},
                {"s": "الفَصْلِ", "ans": {"job": "prep", "sign": "kas"}, "why": "After {فِي}: jarr, kasra."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "الوَلَدُ ___ اللَّبَنَ.", "gloss": "The boy drinks the milk.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَشْرَبُ", "يَشْرَبَ", "يَشْرَبْ")}, "why": "No particle before it: rafʿ, damma."},
                {"s": "___ المُسْلِمُ رَبَّهُ.", "gloss": "The Muslim prays to his Lord.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَدْعُ", "يَدْعُوُ", "يَدْعُو")}, "why": "Rafʿ with a hidden damma. The {و} stays and takes no mark."},
                {"s": "___ الطِّفْلُ إِلَى البَيْتِ.", "gloss": "The child walks to the house.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَمْشِ", "يَمْشِي", "يَمْشِيُ")}, "why": "Rafʿ with a hidden damma on the {ي}."},
                {"s": "___ الدَّرْسَ غَدًا.", "gloss": "I will read the lesson tomorrow.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("سَأَقْرَأُ", "سَأَقْرَأَ", "سَأَقْرَأْ")}, "why": "{سَـ} does not change the case: rafʿ, damma on the hamza."},
                {"s": "___ الطَّالِبُ الكِتَابَ.", "gloss": "The student forgets the book.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَنْسَ", "يَنْسَى", "يَنْسَا")}, "why": "Rafʿ with a hidden damma on the alif, written {ى}."},
                {"s": "نَحْنُ ___ إِلَى المَدْرَسَةِ.", "gloss": "We go to the school.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("نَذْهَبْ", "نَذْهَبَ", "نَذْهَبُ")}, "why": "No particle: rafʿ, damma."},
            ],
        },
        {
            "title": "Which sign does the verb take here?",
            "fields": [{"key": "sign", "label": "Sign", "options": [DAM, HID, FAT, SUK]}],
            "rows": [
                {"s": "[يَدْعُو] الإِمَامُ", "gloss": "the imam prays", "ans": {"sign": "hid"}, "why": "Hidden damma on the {و}, too heavy."},
                {"s": "[يَسْعَى] الرَّجُلُ", "gloss": "the man hurries", "ans": {"sign": "hid"}, "why": "Hidden damma on the alif, impossible."},
                {"s": "[يَشْرَبُ] الوَلَدُ", "gloss": "the boy drinks", "ans": {"sign": "dam"}, "why": "A strong last letter: the damma shows."},
                {"s": "[يَمْشِي] الطِّفْلُ", "gloss": "the child walks", "ans": {"sign": "hid"}, "why": "Hidden damma on the {ي}, too heavy."},
                {"s": "[يَقْرَأُ] الطَّالِبُ", "gloss": "the student reads", "ans": {"sign": "dam"}, "why": "Hamza is a strong letter: the damma shows."},
                {"s": "[تَجْلِسُ] البِنْتُ", "gloss": "the girl sits", "ans": {"sign": "dam"}, "why": "No particle, strong last letter: damma."},
            ],
        },
        {
            "title": "Does the damma show? If not, why?",
            "fields": [{"key": "hide", "label": "Damma", "options": WHYH}],
            "rows": [
                {"s": "يَدْعُو", "gloss": "he calls", "ans": {"hide": "heavy"}, "why": "It ends in {و}: hidden, too heavy."},
                {"s": "يَسْعَى", "gloss": "he strives", "ans": {"hide": "impos"}, "why": "It ends in alif: hidden, impossible."},
                {"s": "يَرْمِي", "gloss": "he throws", "ans": {"hide": "heavy"}, "why": "It ends in {ي}: hidden, too heavy."},
                {"s": "يَكْتُبُ", "gloss": "he writes", "ans": {"hide": "show"}, "why": "A strong last letter: the damma shows."},
                {"s": "يَنْسَى", "gloss": "he forgets", "ans": {"hide": "impos"}, "why": "It ends in alif, written {ى}: impossible."},
                {"s": "يَمْشِي", "gloss": "he walks", "ans": {"hide": "heavy"}, "why": "It ends in {ي}: too heavy."},
            ],
        },
        {
            "title": "Iʿrāb: the verb after its Topic",
            "prompt": "المُعَلِّمُ يَشْرَحُ الدَّرْسَ لِلطُّلَّابِ.",
            "en": "The teacher explains the lesson to the students.",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, VERB, DOER, OBJ, PREP]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, HID]},
            ],
            "rows": [
                {"s": "المُعَلِّمُ", "ans": {"job": "topic", "sign": "dam"}, "why": "It comes first, before the verb: Topic, rafʿ, damma. The doer of {يَشْرَحُ} is hidden."},
                {"s": "يَشْرَحُ", "ans": {"job": "verb", "sign": "dam"}, "why": "A present verb with no particle: rafʿ, damma. The verb sentence is the Information."},
                {"s": "الدَّرْسَ", "ans": {"job": "obj", "sign": "fat"}, "why": "What is explained: object, fatha."},
                {"s": "لِلطُّلَّابِ", "ans": {"job": "prep", "sign": "kas"}, "why": "{الطُّلَّابِ} after {لِـ}: jarr, kasra. A broken plural takes the normal signs."},
            ],
        },
        {
            "title": "Iʿrāb: a plural doer",
            "prompt": "يَذْهَبُ المُسْلِمُونَ إِلَى المَسْجِدِ يَوْمَ الجُمُعَةِ.",
            "en": "The Muslims go to the mosque on Friday.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, PREP, WHEN, OWNER]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, WAW, ALIF]},
            ],
            "rows": [
                {"s": "يَذْهَبُ", "ans": {"job": "verb", "sign": "dam"}, "why": "No particle: rafʿ, damma. The verb stays singular before a noun doer."},
                {"s": "المُسْلِمُونَ", "ans": {"job": "doer", "sign": "waw"}, "why": "{فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}"},
                {"s": "المَسْجِدِ", "ans": {"job": "prep", "sign": "kas"}, "why": "After {إِلَى}: jarr, kasra."},
                {"s": "يَوْمَ", "ans": {"job": "when", "sign": "fat"}, "why": "It tells when: time, naṣb, fatha."},
                {"s": "الجُمُعَةِ", "ans": {"job": "owner", "sign": "kas"}, "why": "Owner of {يَوْمَ}: jarr, kasra."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "يَمْشِي أَبُوكَ إِلَى السُّوقِ صَبَاحًا.",
            "en": "Your father walks to the market in the morning.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, PREP, WHEN]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, WAW, HID]},
            ],
            "rows": [
                {"s": "يَمْشِي", "ans": {"job": "verb", "sign": "hid"}, "why": "No particle: rafʿ. The damma is hidden on the {ي}, too heavy."},
                {"s": "أَبُوكَ", "ans": {"job": "doer", "sign": "waw"}, "why": "Doer, rafʿ. One of the five nouns with an owner: sign wāw."},
                {"s": "السُّوقِ", "ans": {"job": "prep", "sign": "kas"}, "why": "After {إِلَى}: jarr, kasra."},
                {"s": "صَبَاحًا", "ans": {"job": "when", "sign": "fat"}, "why": "It tells when: time, naṣb, fatha."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "يَسْعَى الحُجَّاجُ بَيْنَ الصَّفَا وَالمَرْوَةِ.",
            "en": "The pilgrims walk between Ṣafā and Marwa.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, WHEN, OWNER, AND]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, HID]},
            ],
            "rows": [
                {"s": "يَسْعَى", "ans": {"job": "verb", "sign": "hid"}, "why": "No particle: rafʿ. Hidden damma on the alif, impossible."},
                {"s": "الحُجَّاجُ", "ans": {"job": "doer", "sign": "dam"}, "why": "A broken plural as doer: rafʿ, damma."},
                {"s": "بَيْنَ", "ans": {"job": "when", "sign": "fat"}, "why": "It tells where: place, naṣb, fatha."},
                {"s": "الصَّفَا", "ans": {"job": "owner", "sign": "hid"}, "why": "Owner of {بَيْنَ}: jarr. It ends in alif, so the kasra is hidden."},
                {"s": "المَرْوَةِ", "ans": {"job": "and", "sign": "kas"}, "why": "After {وَ}: it copies {الصَّفَا}, jarr. Here the kasra shows."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "أَنَا ___ اللّٰهَ.", "gloss": "I pray to Allah.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَدْعُو", "أَدْعُ", "أَدْعُوُ")}, "why": "Rafʿ with a hidden damma. Keep the {و} with no mark."},
                {"s": "___ الوَلَدُ الحَجَرَ.", "gloss": "The boy throws the stone.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَرْمِ", "يَرْمِيُ", "يَرْمِي")}, "why": "Rafʿ with a hidden damma on the {ي}."},
                {"s": "المُؤْمِنُ ___ اللّٰهَ.", "gloss": "The believer fears Allah.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَخْشَ", "يَخْشَى", "يَخْشَا")}, "why": "Rafʿ with a hidden damma on the alif, written {ى}."},
                {"s": "سَوْفَ ___ بَيْتًا.", "gloss": "We will build a house.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("نَبْنِي", "نَبْنِ", "نَبْنِيُ")}, "why": "{سَوْفَ} does not change the case: rafʿ, hidden damma on the {ي}."},
                {"s": "البِنْتُ ___ القُرْآنَ.", "gloss": "The girl recites the Qur'an.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَتْلُ", "تَتْلُوُ", "تَتْلُو")}, "why": "Rafʿ with a hidden damma on the {و}."},
                {"s": "هُوَ ___ مَعَنَا.", "gloss": "He stays with us.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَبْقَ", "يَبْقَى", "يَبْقَا")}, "why": "Rafʿ with a hidden damma on the alif, written {ى}."},
            ],
        },
        {
            "title": "Which sign does the verb take here?",
            "fields": [{"key": "sign", "label": "Sign", "options": [DAM, HID, FAT, SUK]}],
            "rows": [
                {"s": "[يَبْكِي] الطِّفْلُ", "gloss": "the child cries", "ans": {"sign": "hid"}, "why": "Hidden damma on the {ي}, too heavy."},
                {"s": "[يَسْأَلُ] الطَّالِبُ", "gloss": "the student asks", "ans": {"sign": "dam"}, "why": "A strong last letter: the damma shows."},
                {"s": "سَوْفَ [يَرْضَى] أَبُوكَ", "gloss": "your father will be pleased", "ans": {"sign": "hid"}, "why": "{سَوْفَ} changes nothing. Hidden damma on the alif."},
                {"s": "لَا [يَكْذِبُ] المُسْلِمُ", "gloss": "the Muslim does not lie", "ans": {"sign": "dam"}, "why": "{لَا} \"not\" does not change the case: rafʿ, damma."},
                {"s": "[يُصَلِّي] الرَّجُلُ", "gloss": "the man prays", "ans": {"sign": "hid"}, "why": "It ends in {ي}: hidden damma, too heavy."},
                {"s": "[نَسْكُنُ] فِي المَدِينَةِ", "gloss": "we live in the city", "ans": {"sign": "dam"}, "why": "The {ن} is a strong letter of the word: the damma shows."},
            ],
        },
        {
            "title": "Does the damma show? If not, why?",
            "fields": [{"key": "hide", "label": "Damma", "options": WHYH}],
            "rows": [
                {"s": "يَبْكِي", "gloss": "he cries", "ans": {"hide": "heavy"}, "why": "It ends in {ي}: too heavy."},
                {"s": "يَخْشَى", "gloss": "he fears", "ans": {"hide": "impos"}, "why": "It ends in alif: impossible."},
                {"s": "يَرْجُو", "gloss": "he hopes", "ans": {"hide": "heavy"}, "why": "It ends in {و}: too heavy."},
                {"s": "يَبْقَى", "gloss": "he stays", "ans": {"hide": "impos"}, "why": "It ends in alif: impossible."},
                {"s": "يَقْرَأُ", "gloss": "he reads", "ans": {"hide": "show"}, "why": "Hamza is a strong letter: the damma shows."},
                {"s": "يَشْكُو", "gloss": "he complains", "ans": {"hide": "heavy"}, "why": "It ends in {و}: too heavy."},
            ],
        },
        {
            "title": "Iʿrāb: a dual doer",
            "prompt": "يَجْلِسُ الطَّالِبَانِ أَمَامَ المُدَرِّسِ.",
            "en": "The two students sit in front of the teacher.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, WHEN, OWNER]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, ALIF, WAW]},
            ],
            "rows": [
                {"s": "يَجْلِسُ", "ans": {"job": "verb", "sign": "dam"}, "why": "No particle: rafʿ, damma. Singular before a noun doer."},
                {"s": "الطَّالِبَانِ", "ans": {"job": "doer", "sign": "alif"}, "why": "{فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الأَلِفُ لِأَنَّهُ مُثَنًّى}"},
                {"s": "أَمَامَ", "ans": {"job": "when", "sign": "fat"}, "why": "It tells where: place, naṣb, fatha."},
                {"s": "المُدَرِّسِ", "ans": {"job": "owner", "sign": "kas"}, "why": "Owner of {أَمَامَ}: jarr, kasra."},
            ],
        },
    ],
}
