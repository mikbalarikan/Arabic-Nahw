# Stage 8, Unit 4: The present verb in naṣb (نَصْبُ الفِعْلِ المُضَارِعِ)

DAM = {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
FAT = {"k": "fat",   "label": "Fatha · فَتْحَةٌ",                "color": "pink"}
KAS = {"k": "kas",   "label": "Kasra · كَسْرَةٌ",                "color": "green"}
SUK = {"k": "suk",   "label": "Sukūn · سُكُونٌ",                 "color": "navy"}
ALIF = {"k": "alif",  "label": "Alif · الأَلِفُ",                  "color": "teal"}
HID = {"k": "hid",   "label": "Hidden vowel · مُقَدَّرَةٌ",         "color": "brown"}
NUN = {"k": "nun",   "label": "Nūn stays · ثُبُوتُ النُّونِ",        "color": "olive"}
DROP = {"k": "drop",  "label": "Nūn drops · حَذْفُ النُّونِ",         "color": "orange"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ",                  "color": "grey"}

RAF = {"k": "raf",  "label": "Rafʿ · رَفْعٌ",   "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ",  "color": "pink"}

VERB = {"k": "verb",  "label": "Verb · فِعْلٌ",                       "color": "navy"}
DOER = {"k": "doer",  "label": "Doer · فَاعِلٌ",                      "color": "orange"}
PREP = {"k": "prep",  "label": "After a preposition · اِسْمٌ مَجْرُورٌ",    "color": "green"}
OBJ = {"k": "obj",   "label": "Object · مَفْعُولٌ بِهِ",                "color": "pink"}
PART = {"k": "part",  "label": "Particle · حَرْفٌ",                     "color": "grey"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s8-nasb",
    "order": 4,
    "title": "The present verb in naṣb",
    "ar": "نَصْبُ الفِعْلِ المُضَارِعِ",
    "blurb": "Six particles put the present verb in naṣb: أَنْ، لَنْ، كَيْ، لِـ، حَتَّى، إِذَنْ. Learn their meanings and the four signs.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 8 · UNIT 4", "title": "Six particles of naṣb",
         "text": "When one of six particles comes before the present verb, the verb goes into naṣb. Its usual sign is fatha.",
         "wm": "لَنْ يَكْتُبَ"},

        {"t": "h2", "text": "The particles and their meanings"},
        {"t": "table", "head": ["Particle", "Meaning", "Example", "English"], "rows": [
            ["أَنْ", "to, that", "أُرِيدُ أَنْ أَكْتُبَ.", "I want to write."],
            ["لَنْ", "will not, will never", "لَنْ يَكْذِبَ المُسْلِمُ.", "The Muslim will not lie."],
            ["كَيْ", "so that", "دَرَسْتُ كَيْ أَنْجَحَ.", "I studied so that I succeed."],
            ["لِـ", "in order to", "جَلَسَ الطَّالِبُ لِيَكْتُبَ.", "The student sat down in order to write."],
            ["حَتَّى", "until, so that", "اِنْتَظِرْ حَتَّى يَرْجِعَ أَبُوكَ.", "Wait until your father returns."],
            ["إِذَنْ", "then, in that case", "إِذَنْ تَنْجَحَ.", "Then you will succeed."],
        ]},
        {"t": "rule", "color": "pink", "title": "Particle of naṣb → naṣb",
         "text": "These six are particles of naṣb ({حُرُوفُ النَّصْبِ}). The verb right after them is in naṣb. The particle itself is fixed, with no place."},
        {"t": "tip", "text": "{إِذَنْ} answers what someone said. It comes first in the answer, right before the verb. Someone says {سَأَجْتَهِدُ} \"I will work hard\". You answer {إِذَنْ تَنْجَحَ} \"Then you will succeed\"."},

        {"t": "h2", "text": "Do not mix them up"},
        {"t": "cols", "items": [
            {"color": "pink", "title": "أَنْ + verb", "ar": "أَنْ يَكْتُبَ",
             "text": "Sukūn on the {ن}. A particle of naṣb."},
            {"color": "gold", "title": "أَنَّ + noun", "ar": "أَنَّ الطَّالِبَ",
             "text": "Shadda on the {ن}. A sister of {إِنَّ} (Stage 5). It takes a noun."},
            {"color": "green", "title": "لِـ / حَتَّى + noun", "ar": "لِلطَّالِبِ",
             "text": "Before a noun they are prepositions: jarr. Before a present verb: naṣb."},
        ]},
        {"t": "examples", "items": [
            {"ar": "نِمْتُ حَتَّى الفَجْرِ.", "en": "I slept until dawn.", "note": "{حَتَّى} before a noun: a preposition, {الفَجْرِ} is in jarr."},
            {"ar": "اُدْرُسْ حَتَّى تَنْجَحَ.", "en": "Study so that you succeed.", "note": "{حَتَّى} before a present verb: naṣb."},
        ]},

        {"t": "h2", "text": "Sign 1: fatha"},
        {"t": "p", "text": "A verb with a strong last letter shows the fatha."},
        {"t": "examples", "items": [
            {"ar": "لَنْ يَتْرُكَ المُسْلِمُ الصَّلَاةَ.", "en": "The Muslim will not leave the prayer."},
        ]},
        {"t": "table", "head": ["Word", "Iʿrāb"], "rows": [
            ["لَنْ", "{حَرْفُ نَصْبٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ مِنَ الإِعْرَابِ}"],
            ["يَتْرُكَ", "{فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ}"],
            ["المُسْلِمُ", "{فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}"],
            ["الصَّلَاةَ", "{مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}"],
        ]},

        {"t": "h2", "text": "Sign 2: fatha on و and ي, hidden on alif"},
        {"t": "p", "text": "In rafʿ the damma was hidden on {و}، {ي} and alif. In naṣb the fatha is light, so it shows on {و} and {ي}. On alif it is still hidden."},
        {"t": "table", "head": ["Rafʿ", "Naṣb", "Fatha"], "rows": [
            ["يَدْعُو", "لَنْ يَدْعُوَ", "shows on {و}"],
            ["يَرْجُو", "لَنْ يَرْجُوَ", "shows on {و}"],
            ["يَرْمِي", "لَنْ يَرْمِيَ", "shows on {ي}"],
            ["يَمْشِي", "لَنْ يَمْشِيَ", "shows on {ي}"],
            ["يَسْعَى", "لَنْ يَسْعَى", "hidden on alif"],
            ["يَنْسَى", "لَنْ يَنْسَى", "hidden on alif"],
        ]},
        {"t": "examples", "items": [
            {"ar": "ذَهَبْتُ إِلَى المَسْجِدِ لِأُصَلِّيَ.", "en": "I went to the mosque in order to pray.",
             "note": "{أُصَلِّيَ}: {فِعْلٌ مُضَارِعٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ عَلَى اليَاءِ}"},
            {"ar": "لَنْ يَنْسَى الطَّالِبُ الدَّرْسَ.", "en": "The student will not forget the lesson.",
             "note": "{يَنْسَى}: {فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ عَلَى الأَلِفِ لِلتَّعَذُّرِ}"},
        ]},
        {"t": "tip", "text": "{لَنْ يَسْعَى} looks the same as {يَسْعَى}. Only the particle tells you it is naṣb."},

        {"t": "h2", "text": "Sign 3: the nūn drops"},
        {"t": "p", "text": "The five verbs lose their {ن} in naṣb, as you saw in Unit 3. This works after all six particles."},
        {"t": "examples", "items": [
            {"ar": "جَلَسَ الأَوْلَادُ لِيَكْتُبُوا الدَّرْسَ.", "en": "The boys sat down in order to write the lesson.",
             "note": "{يَكْتُبُوا}: {فِعْلٌ مُضَارِعٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الأَفْعَالِ الخَمْسَةِ}. The {و} is the doer."},
            {"ar": "أُرِيدُ أَنْ تَفْهَمِي الدَّرْسَ.", "en": "I want you (f) to understand the lesson.", "note": "{تَفْهَمِينَ} loses its {ن}."},
            {"ar": "لَنْ تَنَالُوا البِرَّ حَتَّى تُنْفِقُوا مِمَّا تُحِبُّونَ", "en": "You will never reach righteousness until you spend from what you love. (Āl ʿImrān 3:92)",
             "note": "Two five verbs in naṣb, after {لَنْ} and {حَتَّى}: the nūn drops. {تُحِبُّونَ} has no particle: the nūn stays."},
        ]},
        {"t": "tip", "text": "The nūn of women does not drop: {لَنْ يَكْتُبْنَ}. The verb is fixed on sukūn, in the place of naṣb."},

        {"t": "h2", "text": "All the signs of naṣb"},
        {"t": "table", "head": ["Kind of verb", "Rafʿ", "Naṣb", "Sign of naṣb"], "rows": [
            ["strong ending", "يَكْتُبُ", "لَنْ يَكْتُبَ", "fatha"],
            ["ends in و / ي", "يَدْعُو، يَرْمِي", "لَنْ يَدْعُوَ، لَنْ يَرْمِيَ", "fatha, it shows"],
            ["ends in alif", "يَسْعَى", "لَنْ يَسْعَى", "hidden fatha"],
            ["five verbs", "يَكْتُبُونَ", "لَنْ يَكْتُبُوا", "nūn drops"],
            ["nūn of women", "يَكْتُبْنَ", "لَنْ يَكْتُبْنَ", "fixed, place of naṣb"],
        ]},

        {"t": "summary", "title": "In short", "items": [
            "Six particles of naṣb: {أَنْ} to, {لَنْ} will not, {كَيْ} so that, {لِـ} in order to, {حَتَّى} until, {إِذَنْ} then.",
            "Strong ending: fatha. {لَنْ يَكْتُبَ}.",
            "On {و} and {ي} the fatha shows: {لَنْ يَدْعُوَ}، {لَنْ يَرْمِيَ}. On alif it is hidden: {لَنْ يَسْعَى}.",
            "Five verbs: the nūn drops. {لَنْ يَكْتُبُوا}.",
            "The formula: {فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}.",
        ]},
    ],

    "practice": [
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "لَنْ يَذْهَبَ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("He will not go.", "He did not go.", "He goes.")}, "why": "{لَنْ} means \"will not\"."},
                {"s": "أُرِيدُ أَنْ أَقْرَأَ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("I will not read.", "I want to read.", "I read.")}, "why": "{أَنْ} + verb: \"to read\"."},
                {"s": "جِئْتُ كَيْ أَتَعَلَّمَ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("I came and I learned.", "I came until I learned.", "I came so that I learn.")}, "why": "{كَيْ} means \"so that\"."},
                {"s": "اِنْتَظِرْ حَتَّى يَرْجِعَ أَبُوكَ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("Wait until your father returns.", "Wait, your father will not return.", "Wait, your father returned.")}, "why": "{حَتَّى} here means \"until\"."},
                {"s": "سَأَجْتَهِدُ. إِذَنْ تَنْجَحَ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("I will work hard. You did not succeed.", "I will work hard. Then you will succeed.", "I will work hard until you succeed.")}, "why": "{إِذَنْ} answers: \"then, in that case\"."},
                {"s": "جَلَسَ لِيَكْتُبَ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("He sat and wrote.", "He sat but did not write.", "He sat down in order to write.")}, "why": "{لِـ} before a present verb: \"in order to\"."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "لَنْ ___ الطَّالِبُ.", "gloss": "The student will not go.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَذْهَبُ", "يَذْهَبَ", "يَذْهَبْ")}, "why": "After {لَنْ}: naṣb, fatha."},
                {"s": "أُرِيدُ أَنْ ___ القُرْآنَ.", "gloss": "I want to read the Qur'an.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَقْرَأُ", "أَقْرَأْ", "أَقْرَأَ")}, "why": "After {أَنْ}: naṣb, fatha on the hamza."},
                {"s": "لَنْ ___ المُسْلِمُ رَبَّهُ.", "gloss": "The Muslim will not forget his Lord.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَنْسَى", "يَنْسَ", "يَنْسَيَ")}, "why": "After {لَنْ}: naṣb. The fatha is hidden on the alif, so the word does not change."},
                {"s": "ذَهَبْتُ إِلَى المَسْجِدِ ___.", "gloss": "I went to the mosque in order to pray.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لِأُصَلِّيَ", "لِأُصَلِّي", "لِأُصَلِّ")}, "why": "After {لِـ}: naṣb. The fatha shows on the {ي}."},
                {"s": "اُدْرُسُوا حَتَّى ___.", "gloss": "Study (men) so that you succeed.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَنْجَحُونَ", "تَنْجَحُوا", "تَنْجَحَ")}, "why": "After {حَتَّى}: naṣb. A five verb: the nūn drops."},
                {"s": "الوَلَدُ لَنْ ___ الكُرَةَ.", "gloss": "The boy will not throw the ball.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَرْمِي", "يَرْمِ", "يَرْمِيَ")}, "why": "After {لَنْ}: naṣb. The fatha shows on the {ي}."},
            ],
        },
        {
            "title": "Which sign does the verb take here?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, HID, DROP, DAM]}],
            "rows": [
                {"s": "لَنْ [يَكْتُبَ]", "gloss": "he will not write", "ans": {"sign": "fat"}, "why": "A strong ending: fatha."},
                {"s": "لَنْ [يَرْمِيَ]", "gloss": "he will not throw", "ans": {"sign": "fat"}, "why": "The fatha shows on the {ي}."},
                {"s": "لَنْ [يَسْعَى]", "gloss": "he will not strive", "ans": {"sign": "hid"}, "why": "Alif cannot carry a vowel: hidden fatha."},
                {"s": "لَنْ [يَكْتُبُوا]", "gloss": "they will not write", "ans": {"sign": "drop"}, "why": "A five verb: the nūn drops."},
                {"s": "أَنْ [يَدْعُوَ]", "gloss": "that he calls", "ans": {"sign": "fat"}, "why": "The fatha shows on the {و}."},
                {"s": "حَتَّى [تَخْرُجِي]", "gloss": "until you (f) go out", "ans": {"sign": "drop"}, "why": "{تَخْرُجِينَ} is a five verb: the nūn drops."},
            ],
        },
        {
            "title": "Rafʿ or naṣb? And the sign",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, HID, NUN, DROP]},
            ],
            "rows": [
                {"s": "[يَكْتُبُ] الطَّالِبُ", "gloss": "the student writes", "ans": {"case": "raf", "sign": "dam"}, "why": "No particle: rafʿ, damma."},
                {"s": "لَنْ [يَكْتُبَ]", "gloss": "he will not write", "ans": {"case": "nasb", "sign": "fat"}, "why": "After {لَنْ}: naṣb, fatha."},
                {"s": "سَـ[يَسْعَى]", "gloss": "he will strive", "ans": {"case": "raf", "sign": "hid"}, "why": "{سَـ} is not a particle of naṣb: rafʿ, hidden damma."},
                {"s": "لَنْ [يَسْعَى]", "gloss": "he will not strive", "ans": {"case": "nasb", "sign": "hid"}, "why": "After {لَنْ}: naṣb, hidden fatha on the alif."},
                {"s": "[يَدْعُو] الإِمَامُ", "gloss": "the imam prays", "ans": {"case": "raf", "sign": "hid"}, "why": "No particle: rafʿ. The damma is hidden on the {و}."},
                {"s": "أَنْ [يَدْعُوَ]", "gloss": "that he prays", "ans": {"case": "nasb", "sign": "fat"}, "why": "After {أَنْ}: naṣb. The fatha shows on the {و}."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "لَنْ يَتْرُكَ المُسْلِمُ الصَّلَاةَ.",
            "en": "The Muslim will not leave the prayer.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PART, VERB, DOER, OBJ]},
                {"key": "sign", "label": "Sign", "options": [FIXED, DAM, FAT, SUK]},
            ],
            "rows": [
                {"s": "لَنْ", "ans": {"job": "part", "sign": "fixed"}, "why": "A particle of naṣb, fixed on sukūn, with no place."},
                {"s": "يَتْرُكَ", "ans": {"job": "verb", "sign": "fat"}, "why": "In naṣb after {لَنْ}. The fatha shows."},
                {"s": "المُسْلِمُ", "ans": {"job": "doer", "sign": "dam"}, "why": "The one who does not leave: doer, rafʿ, damma."},
                {"s": "الصَّلَاةَ", "ans": {"job": "obj", "sign": "fat"}, "why": "What is left: object, naṣb, fatha."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "جَلَسَ الأَوْلَادُ فِي الفَصْلِ لِيَكْتُبُوا الدَّرْسَ.",
            "en": "The boys sat in the classroom in order to write the lesson.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, PREP, OBJ]},
                {"key": "sign", "label": "Sign", "options": [FIXED, DAM, KAS, FAT, DROP]},
            ],
            "rows": [
                {"s": "جَلَسَ", "ans": {"job": "verb", "sign": "fixed"}, "why": "A past verb: fixed on fatha."},
                {"s": "الأَوْلَادُ", "ans": {"job": "doer", "sign": "dam"}, "why": "A broken plural as doer: rafʿ, damma."},
                {"s": "الفَصْلِ", "ans": {"job": "prep", "sign": "kas"}, "why": "After {فِي}: jarr, kasra."},
                {"s": "لِيَكْتُبُوا", "ans": {"job": "verb", "sign": "drop"}, "why": "{يَكْتُبُوا} is in naṣb after {لِـ}. A five verb: the nūn drops."},
                {"s": "الدَّرْسَ", "ans": {"job": "obj", "sign": "fat"}, "why": "What they write: object, fatha."},
            ],
        },
    ],

    "homework": [
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "لَنْ نَتْرُكَ الصَّلَاةَ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("We did not leave the prayer.", "We will never leave the prayer.", "Leave the prayer.")}, "why": "{لَنْ} means \"will not, will never\"."},
                {"s": "يُرِيدُ الطَّالِبُ أَنْ يَفْهَمَ الدَّرْسَ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The student wants to understand the lesson.", "The student understood the lesson.", "The student will not understand the lesson.")}, "why": "{أَنْ} + verb: \"to understand\"."},
                {"s": "سَأَزُورُكَ غَدًا. إِذَنْ أُكْرِمَكَ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("I will visit you tomorrow. I did not honour you.", "I will visit you tomorrow until I honour you.", "I will visit you tomorrow. Then I will honour you.")}, "why": "{إِذَنْ} starts the answer: \"then\"."},
                {"s": "اِقْرَأْ حَتَّى تَفْهَمَ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("Read until you understand.", "Read, you will not understand.", "You read and understood.")}, "why": "{حَتَّى} + present verb: \"until\"."},
                {"s": "سَافَرَ كَيْ يَتَعَلَّمَ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("He travelled and did not learn.", "He travelled so that he could learn.", "He learns when he travels.")}, "why": "{كَيْ} means \"so that\"."},
                {"s": "تَعَلَّمْتُ العَرَبِيَّةَ لِأَفْهَمَ القُرْآنَ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("I learned Arabic and understood the Qur'an.", "I learned Arabic for the Qur'an's sake.", "I learned Arabic in order to understand the Qur'an.")}, "why": "{لِـ} + present verb: \"in order to\"."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "أُرِيدُ أَنْ ___ اللّٰهَ.", "gloss": "I want to pray to Allah.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَدْعُوَ", "أَدْعُو", "أَدْعُ")}, "why": "After {أَنْ}: naṣb. The fatha shows on the {و}."},
                {"s": "لَنْ ___ الدَّرْسَ أَبَدًا.", "gloss": "I will never forget the lesson.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَنْسَ", "أَنْسَيَ", "أَنْسَى")}, "why": "After {لَنْ}: naṣb with a hidden fatha. The alif stays."},
                {"s": "أَنْتِ لَنْ ___.", "gloss": "You (f) will not be late.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَتَأَخَّرِينَ", "تَتَأَخَّرِي", "تَتَأَخَّرْ")}, "why": "After {لَنْ}: naṣb. A five verb: the nūn drops, the {ي} stays."},
                {"s": "سَأَدْرُسُ النَّحْوَ. إِذَنْ ___.", "gloss": "I will study grammar. Then you will understand.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَفْهَمُ", "تَفْهَمَ", "تَفْهَمْ")}, "why": "{إِذَنْ} at the start of the answer, right before the verb: naṣb, fatha."},
                {"s": "جَاءَ الطُّلَّابُ ___ العِلْمَ.", "gloss": "The students came in order to seek knowledge.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لِيَطْلُبُونَ", "لِيَطْلُبُوا", "لِيَطْلُبَ")}, "why": "After {لِـ}: naṣb. The doer is \"they\", so a five verb: the nūn drops."},
                {"s": "البَنَاتُ لَنْ ___ الصَّلَاةَ.", "gloss": "The girls will not leave the prayer.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَتْرُكْنَ", "يَتْرُكْ", "يَتْرُكُوا")}, "why": "The nūn of women is the doer. The verb is fixed and keeps its {ن}."},
            ],
        },
        {
            "title": "Which sign does the verb take here?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, HID, DROP, FIXED]}],
            "rows": [
                {"s": "لَنْ [يَرْضَى]", "gloss": "he will not be pleased", "ans": {"sign": "hid"}, "why": "It ends in alif: the fatha is hidden."},
                {"s": "اِنْتَظِرْ حَتَّى [يَمْشِيَ] الطِّفْلُ", "gloss": "wait until the child walks", "ans": {"sign": "fat"}, "why": "After {حَتَّى}: naṣb. The fatha shows on the {ي}."},
                {"s": "كَيْ [تَفْهَمُوا]", "gloss": "so that you (m pl) understand", "ans": {"sign": "drop"}, "why": "A five verb after {كَيْ}: the nūn drops."},
                {"s": "أَنْ [يَرْجُوَ]", "gloss": "that he hopes", "ans": {"sign": "fat"}, "why": "The fatha shows on the {و}."},
                {"s": "لِ[يَبْنِيَ] بَيْتًا", "gloss": "in order to build a house", "ans": {"sign": "fat"}, "why": "After {لِـ}: naṣb. The fatha shows on the {ي}."},
                {"s": "لَنْ [يَكْتُبْنَ]", "gloss": "they (f) will not write", "ans": {"sign": "fixed"}, "why": "The nūn of women: fixed on sukūn, in the place of naṣb."},
            ],
        },
        {
            "title": "Rafʿ or naṣb? And the sign",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, HID, NUN, DROP]},
            ],
            "rows": [
                {"s": "سَوْفَ [يَرْمِي]", "gloss": "he will throw", "ans": {"case": "raf", "sign": "hid"}, "why": "{سَوْفَ} changes nothing: rafʿ, hidden damma on the {ي}."},
                {"s": "لَنْ [يَرْمِيَ]", "gloss": "he will not throw", "ans": {"case": "nasb", "sign": "fat"}, "why": "After {لَنْ}: naṣb. The fatha shows on the {ي}."},
                {"s": "هِيَ [تَخْشَى] اللّٰهَ", "gloss": "she fears Allah", "ans": {"case": "raf", "sign": "hid"}, "why": "No particle: rafʿ, hidden damma on the alif."},
                {"s": "لَنْ [تَخْشَى]", "gloss": "she will not fear", "ans": {"case": "nasb", "sign": "hid"}, "why": "After {لَنْ}: naṣb, hidden fatha on the alif."},
                {"s": "هُمْ [يَدْرُسُونَ]", "gloss": "they study", "ans": {"case": "raf", "sign": "nun"}, "why": "No particle: rafʿ, the nūn stays."},
                {"s": "كَيْ [يَدْرُسُوا]", "gloss": "so that they study", "ans": {"case": "nasb", "sign": "drop"}, "why": "After {كَيْ}: naṣb, the nūn drops."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "يُحِبُّ الطَّالِبُ أَنْ يَقْرَأَ القُرْآنَ.",
            "en": "The student loves to read the Qur'an.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, PART, OBJ]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, FIXED, SUK]},
            ],
            "rows": [
                {"s": "يُحِبُّ", "ans": {"job": "verb", "sign": "dam"}, "why": "No particle before it: rafʿ, damma."},
                {"s": "الطَّالِبُ", "ans": {"job": "doer", "sign": "dam"}, "why": "The one who loves: doer, rafʿ, damma."},
                {"s": "أَنْ", "ans": {"job": "part", "sign": "fixed"}, "why": "A particle of naṣb, fixed on sukūn."},
                {"s": "يَقْرَأَ", "ans": {"job": "verb", "sign": "fat"}, "why": "In naṣb after {أَنْ}: fatha on the hamza."},
                {"s": "القُرْآنَ", "ans": {"job": "obj", "sign": "fat"}, "why": "What he reads: object of {يَقْرَأَ}, fatha."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "لَنْ يَنْسَى الطَّالِبَانِ الدَّرْسَ.",
            "en": "The two students will not forget the lesson.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PART, VERB, DOER, OBJ]},
                {"key": "sign", "label": "Sign", "options": [FIXED, HID, FAT, ALIF, DAM]},
            ],
            "rows": [
                {"s": "لَنْ", "ans": {"job": "part", "sign": "fixed"}, "why": "A particle of naṣb, fixed."},
                {"s": "يَنْسَى", "ans": {"job": "verb", "sign": "hid"}, "why": "In naṣb after {لَنْ}. The fatha is hidden on the alif."},
                {"s": "الطَّالِبَانِ", "ans": {"job": "doer", "sign": "alif"}, "why": "{فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الأَلِفُ لِأَنَّهُ مُثَنًّى}"},
                {"s": "الدَّرْسَ", "ans": {"job": "obj", "sign": "fat"}, "why": "What they will not forget: object, fatha."},
            ],
        },
    ],
}
