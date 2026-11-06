# Stage 8, Unit 7: Verbs with a weak ending

# Canonical options (copied from STAGES_5_8_SPEC.md)
DAM = {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
FAT = {"k": "fat",   "label": "Fatha · فَتْحَةٌ",                "color": "pink"}
KAS = {"k": "kas",   "label": "Kasra · كَسْرَةٌ",                "color": "green"}
SUK = {"k": "suk",   "label": "Sukūn · سُكُونٌ",                 "color": "navy"}
HID = {"k": "hid",   "label": "Hidden vowel · مُقَدَّرَةٌ",         "color": "brown"}
NUN = {"k": "nun",   "label": "Nūn stays · ثُبُوتُ النُّونِ",        "color": "olive"}
WEAK = {"k": "weak",  "label": "Weak letter drops · حَذْفُ حَرْفِ العِلَّةِ", "color": "gold"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ",                  "color": "grey"}

RAF = {"k": "raf",  "label": "Rafʿ · رَفْعٌ",   "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ",  "color": "pink"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ",   "color": "green"}
JAZM = {"k": "jazm", "label": "Jazm · جَزْمٌ",  "color": "navy"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s8-weak",
    "order": 7,
    "title": "Verbs with a weak ending",
    "ar": "الفِعْلُ المُضَارِعُ المُعْتَلُّ الآخِرِ",
    "blurb": "يَدْعُو، يَرْمِي، يَسْعَى: a hidden damma in rafʿ, fatha or a hidden fatha in naṣb, and the weak letter drops in jazm.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 8 · UNIT 7", "title": "When the last letter is weak",
         "text": "Some present verbs end in {و}، {ي} or {ا}. These letters are weak. They change how the signs look.",
         "wm": "المُعْتَلُّ الآخِرِ"},

        {"t": "h2", "text": "Three weak endings"},
        {"t": "p", "text": "The weak letters are {و}، {ي} and {ا} (written {ى}). A verb that ends in one of them is {مُعْتَلُّ الآخِرِ}."},
        {"t": "table", "head": ["Ends in", "Verb", "Meaning", "Verb", "Meaning"], "rows": [
            ["و", "يَدْعُو", "he calls, he prays", "يَرْجُو", "he hopes"],
            ["ي", "يَرْمِي", "he throws", "يَمْشِي", "he walks"],
            ["ا (ى)", "يَسْعَى", "he strives", "يَنْسَى", "he forgets"],
        ]},
        {"t": "tip", "text": "You met the same letters in nouns in Stage 4: {القَاضِي} and {مُوسَى} hide their vowel. Verbs work in a similar way."},

        {"t": "h2", "text": "Rafʿ: a hidden damma"},
        {"t": "p", "text": "With no particle the verb is in rafʿ. You cannot see the damma. It is hidden on the last letter."},
        {"t": "cols", "items": [
            {"color": "brown", "title": "On و and ي: too heavy", "ar": "لِلثِّقَلِ",
             "text": "{يَدْعُو}، {يَرْمِي}: a damma on these letters is heavy to say, so it is hidden."},
            {"color": "brown", "title": "On ا: impossible", "ar": "لِلتَّعَذُّرِ",
             "text": "{يَسْعَى}: an alif can never carry a vowel."},
        ]},
        {"t": "examples", "items": [
            {"ar": "المُسْلِمُ يَدْعُو رَبَّهُ.", "en": "The Muslim calls on his Lord.", "note": "{يَدْعُو}: hidden damma on the {و}."},
            {"ar": "الوَلَدُ يَمْشِي إِلَى المَدْرَسَةِ.", "en": "The boy walks to school.", "note": "{يَمْشِي}: hidden damma on the {ي}."},
            {"ar": "الطَّالِبُ يَسْعَى إِلَى النَّجَاحِ.", "en": "The student strives for success.", "note": "{يَسْعَى}: hidden damma on the alif."},
        ]},

        {"t": "h2", "text": "Naṣb: fatha shows on و and ي, hidden on ا"},
        {"t": "p", "text": "A fatha is light. It shows on {و} and {ي}. Only the alif still hides it."},
        {"t": "examples", "items": [
            {"ar": "لَنْ يَدْعُوَ", "en": "he will not call", "note": "Fatha shows on the {و}."},
            {"ar": "لَنْ يَرْمِيَ", "en": "he will not throw", "note": "Fatha shows on the {ي}."},
            {"ar": "لَنْ يَسْعَى", "en": "he will not strive", "note": "Hidden fatha on the alif. It looks the same as rafʿ."},
        ]},
        {"t": "tip", "text": "{لَنْ يَنْسَى} and {يَنْسَى} look the same. The particle {لَنْ} tells you the case is naṣb."},

        {"t": "h2", "text": "Jazm: the weak letter drops"},
        {"t": "p", "text": "In jazm the weak letter falls off. The short vowel before it stays."},
        {"t": "rule", "color": "gold", "title": "Weak letter drops",
         "text": "{يَدْعُو} → {لَمْ يَدْعُ}. {يَرْمِي} → {لَمْ يَرْمِ}. {يَسْعَى} → {لَمْ يَسْعَ}. The sign of jazm is {حَذْفُ حَرْفِ العِلَّةِ}."},
        {"t": "examples", "items": [
            {"ar": "لَا تَنْسَ وَاجِبَكَ.", "en": "Don't forget your homework.", "note": "{لَا} forbids. The alif drops: {تَنْسَ}."},
            {"ar": "وَلَا تَمْشِ فِي الأَرْضِ مَرَحًا", "en": "And do not walk on the earth arrogantly. (al-Isrāʾ 17:37)", "note": "{تَمْشِ}: jazm after {لَا} that forbids. The {ي} drops."},
        ]},

        {"t": "h2", "text": "The whole table"},
        {"t": "table", "head": ["Rafʿ", "Naṣb", "Jazm"], "rows": [
            ["يَدْعُو", "لَنْ يَدْعُوَ", "لَمْ يَدْعُ"],
            ["يَرْجُو", "لَنْ يَرْجُوَ", "لَمْ يَرْجُ"],
            ["يَرْمِي", "لَنْ يَرْمِيَ", "لَمْ يَرْمِ"],
            ["يَمْشِي", "لَنْ يَمْشِيَ", "لَمْ يَمْشِ"],
            ["يَسْعَى", "لَنْ يَسْعَى", "لَمْ يَسْعَ"],
            ["يَنْسَى", "لَنْ يَنْسَى", "لَمْ يَنْسَ"],
            ["hidden damma", "fatha (hidden on ا)", "weak letter drops"],
        ]},
        {"t": "tip", "text": "This unit drills the forms without an ending. Their five-verb forms ({يَدْعُونَ}، {يَمْشُونَ}) still follow the nūn rule of Unit 3."},

        {"t": "h2", "text": "Worked examples"},
        {"t": "examples", "items": [
            {"ar": "خَالِدٌ يَدْعُو أَخَاهُ.", "en": "Khālid calls his brother.",
             "note": "{يَدْعُو}: {فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ عَلَى الوَاوِ لِلثِّقَلِ}."},
            {"ar": "لَنْ يَسْعَى الكَسُولُ.", "en": "The lazy one will not strive.",
             "note": "{يَسْعَى}: {فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ عَلَى الأَلِفِ لِلتَّعَذُّرِ}."},
            {"ar": "لَمْ يَرْمِ الوَلَدُ الحَجَرَ.", "en": "The boy did not throw the stone.",
             "note": "{يَرْمِ}: {فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ العِلَّةِ}. {الوَلَدُ}: {فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ}."},
        ]},

        {"t": "h2", "text": "Review: the fixed present verb"},
        {"t": "p", "text": "The present verb is muʿrab only when nothing is attached to its end. Two nūns make it fixed."},
        {"t": "table", "head": ["Attached", "Example", "Meaning", "Fixed on"], "rows": [
            ["nūn of women · نُونُ النِّسْوَةِ", "الطَّالِبَاتُ يَكْتُبْنَ.", "The female students write.", "sukūn"],
            ["nūn of emphasis · نُونُ التَّوْكِيدِ", "وَاللَّهِ لَأَكْتُبَنَّ.", "By Allah, I will surely write.", "fatha"],
        ]},
        {"t": "p", "text": "A particle cannot change a fixed verb. {لَمْ يَكْتُبْنَ} and {لَنْ يَكْتُبْنَ} stay the same. Only the place changes. After {لَنْ} the place is naṣb. After {لَمْ}: {فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ فِي مَحَلِّ جَزْمٍ}."},

        {"t": "summary", "title": "In short", "items": [
            "Weak endings: {و} ({يَدْعُو}), {ي} ({يَرْمِي}), {ا} ({يَسْعَى}).",
            "Rafʿ: hidden damma on all three.",
            "Naṣb: fatha shows on {و} and {ي} ({لَنْ يَدْعُوَ}، {لَنْ يَرْمِيَ}); hidden on the alif ({لَنْ يَسْعَى}).",
            "Jazm: the weak letter drops ({لَمْ يَدْعُ}، {لَمْ يَرْمِ}، {لَمْ يَسْعَ}).",
            "With the nūn of women or the nūn of emphasis the present verb is fixed.",
        ]},
    ],

    "practice": [
        {
            "title": "Which case and sign does the verb take here?",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JAZM]},
                {"key": "sign", "label": "Sign", "options": [FAT, HID, WEAK]},
            ],
            "rows": [
                {"s": "خَالِدٌ [يَدْعُو] رَبَّهُ", "gloss": "Khālid calls on his Lord", "ans": {"case": "raf", "sign": "hid"},
                 "why": "No particle: rafʿ. Hidden damma on the {و} (too heavy)."},
                {"s": "لَنْ [يَدْعُوَ]", "gloss": "he will not call", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "After {لَنْ}: naṣb. The fatha shows on the {و}."},
                {"s": "لَمْ [يَدْعُ]", "gloss": "he did not call", "ans": {"case": "jazm", "sign": "weak"},
                 "why": "After {لَمْ}: jazm. The {و} drops."},
                {"s": "الوَلَدُ [يَسْعَى]", "gloss": "the boy strives", "ans": {"case": "raf", "sign": "hid"},
                 "why": "No particle: rafʿ. Hidden damma on the alif."},
                {"s": "لَنْ [يَسْعَى]", "gloss": "he will not strive", "ans": {"case": "nasb", "sign": "hid"},
                 "why": "After {لَنْ}: naṣb. The fatha is hidden on the alif."},
                {"s": "لَمْ [يَسْعَ]", "gloss": "he did not strive", "ans": {"case": "jazm", "sign": "weak"},
                 "why": "After {لَمْ}: jazm. The alif drops."},
            ],
        },
        {
            "title": "Which form is right? (jazm)",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "لَمْ ___ خَالِدٌ دَرْسَهُ.", "gloss": "Khālid did not forget his lesson.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَنْسَى", "يَنْسَ")},
                 "why": "After {لَمْ} the alif drops: {يَنْسَ}."},
                {"s": "لَمْ ___ زَيْدٌ الكُرَةَ.", "gloss": "Zayd did not throw the ball.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَرْمِ", "يَرْمِي", "يَرْمِيَ")},
                 "why": "After {لَمْ} the {ي} drops: {يَرْمِ}."},
                {"s": "لَمْ ___ خَالِدٌ إِلَى المَسْجِدِ.", "gloss": "Khālid did not walk to the mosque.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَمْشِي", "يَمْشِيَ", "يَمْشِ")},
                 "why": "Jazm: the {ي} drops and the kasra stays: {يَمْشِ}."},
                {"s": "___ الإِمَامُ.", "gloss": "Let the imām make duʿāʾ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لِيَدْعُ", "لِيَدْعُو", "لِيَدْعُوَ")},
                 "why": "\"Let him\": the {لِـ} of order gives jazm. The {و} drops."},
                {"s": "لَا ___ يَا خَالِدُ.", "gloss": "Don't forget, Khālid.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَنْسَى", "تَنْسَ")},
                 "why": "\"Don't\": {لَا} forbids, so jazm. The alif drops: {تَنْسَ}."},
            ],
        },
        {
            "title": "Iʿrāb: case and sign",
            "prompt": "لَمْ يَنْسَ الطَّالِبُ كِتَابَهُ فِي البَيْتِ.",
            "en": "The student did not forget his book at home.",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR, JAZM]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, WEAK]},
            ],
            "rows": [
                {"s": "يَنْسَ", "ans": {"case": "jazm", "sign": "weak"},
                 "why": "{فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ العِلَّةِ}."},
                {"s": "الطَّالِبُ", "ans": {"case": "raf", "sign": "dam"},
                 "why": "Doer: rafʿ with damma."},
                {"s": "كِتَابَهُ", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "Object: naṣb with fatha."},
                {"s": "البَيْتِ", "ans": {"case": "jarr", "sign": "kas"},
                 "why": "After {فِي}: jarr with kasra."},
            ],
        },
        {
            "title": "Iʿrāb: case and sign",
            "prompt": "القَاضِي يَمْشِي إِلَى المَسْجِدِ.",
            "en": "The judge walks to the mosque.",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR]},
                {"key": "sign", "label": "Sign", "options": [DAM, KAS, HID]},
            ],
            "rows": [
                {"s": "القَاضِي", "ans": {"case": "raf", "sign": "hid"},
                 "why": "Topic, rafʿ. A manqūṣ noun: hidden damma on the {ي}."},
                {"s": "يَمْشِي", "ans": {"case": "raf", "sign": "hid"},
                 "why": "Present verb with no particle: rafʿ. Hidden damma on the {ي}."},
                {"s": "المَسْجِدِ", "ans": {"case": "jarr", "sign": "kas"},
                 "why": "After {إِلَى}: jarr with kasra."},
            ],
        },
        {
            "title": "Which form is right? (naṣb)",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "لَنْ ___.", "gloss": "He will not forget.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَنْسَى", "يَنْسَ")},
                 "why": "Naṣb on an alif: the fatha is hidden, the alif stays."},
                {"s": "أُرِيدُ أَنْ ___ الكُرَةَ.", "gloss": "I want to throw the ball.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَرْمِيَ", "أَرْمِي", "أَرْمِ")},
                 "why": "After {أَنْ}: naṣb. The fatha shows on the {ي}."},
                {"s": "جِئْتُ ___.", "gloss": "I came to call you.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("لِأَدْعُكَ", "لِأَدْعُوكَ", "لِأَدْعُوَكَ")},
                 "why": "The {لِـ} of purpose gives naṣb. The fatha shows on the {و}."},
                {"s": "يُحِبُّ خَالِدٌ أَنْ ___ فِي الحَدِيقَةِ.", "gloss": "Khālid likes to walk in the garden.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَمْشِي", "يَمْشِيَ", "يَمْشِ")},
                 "why": "After {أَنْ}: naṣb. The fatha shows on the {ي}."},
            ],
        },
        {
            "title": "Muʿrab or fixed? Choose the sign",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, SUK, HID, FIXED]}],
            "rows": [
                {"s": "الطَّالِبَاتُ [يَكْتُبْنَ] الدَّرْسَ", "gloss": "the female students write the lesson", "ans": {"sign": "fixed"},
                 "why": "The nūn of women makes it fixed on sukūn."},
                {"s": "وَاللَّهِ [لَأَكْتُبَنَّ]", "gloss": "by Allah, I will surely write", "ans": {"sign": "fixed"},
                 "why": "The nūn of emphasis makes it fixed on fatha."},
                {"s": "البِنْتُ لَمْ [تَحْضُرْ]", "gloss": "the girl did not come", "ans": {"sign": "suk"},
                 "why": "Nothing attached: muʿrab. Jazm after {لَمْ} with sukūn."},
                {"s": "الوَلَدُ لَنْ [يَبْكِيَ]", "gloss": "the boy will not cry", "ans": {"sign": "fat"},
                 "why": "Naṣb after {لَنْ}. The fatha shows on the {ي}."},
                {"s": "الطِّفْلُ [يَبْكِي]", "gloss": "the child is crying", "ans": {"sign": "hid"},
                 "why": "Rafʿ with a hidden damma on the {ي}."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Which case and sign does the verb take here?",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JAZM]},
                {"key": "sign", "label": "Sign", "options": [FAT, HID, WEAK]},
            ],
            "rows": [
                {"s": "أَنَا [أَرْجُو] رَحْمَةَ اللَّهِ", "gloss": "I hope for Allah's mercy", "ans": {"case": "raf", "sign": "hid"},
                 "why": "No particle: rafʿ. Hidden damma on the {و}."},
                {"s": "لَمْ [يَرْجُ] خَالِدٌ شَيْئًا", "gloss": "Khālid did not hope for anything", "ans": {"case": "jazm", "sign": "weak"},
                 "why": "After {لَمْ}: jazm. The {و} drops."},
                {"s": "لَنْ [يَرْمِيَ] الوَلَدُ الحَجَرَ", "gloss": "the boy will not throw the stone", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "After {لَنْ}: naṣb. The fatha shows on the {ي}."},
                {"s": "الرَّجُلُ [يَخْشَى] اللَّهَ", "gloss": "the man fears Allah", "ans": {"case": "raf", "sign": "hid"},
                 "why": "No particle: rafʿ. Hidden damma on the alif."},
                {"s": "لَنْ [تَخْشَى] شَيْئًا", "gloss": "you will not fear anything", "ans": {"case": "nasb", "sign": "hid"},
                 "why": "After {لَنْ}: naṣb. Hidden fatha on the alif."},
                {"s": "لَا [تَخْشَ] أَحَدًا", "gloss": "don't fear anyone", "ans": {"case": "jazm", "sign": "weak"},
                 "why": "{لَا} forbids: jazm. The alif drops."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "لَمْ ___ رَبَّهُ.", "gloss": "He did not call on his Lord.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَدْعُ", "يَدْعُو", "يَدْعُوَ")},
                 "why": "After {لَمْ} the {و} drops: {يَدْعُ}."},
                {"s": "الوَلَدُ لَا ___ مَعَ أَبِيهِ.", "gloss": "The boy does not walk with his father.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَمْشِ", "يَمْشِيَ", "يَمْشِي")},
                 "why": "A fact. This {لَا} only negates, so rafʿ with a hidden damma."},
                {"s": "لَنْ ___ فَضْلَكَ.", "gloss": "I will never forget your kindness.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَنْسَى", "أَنْسَ")},
                 "why": "Naṣb after {لَنْ}: hidden fatha, the alif stays."},
                {"s": "___ كُلُّ طَالِبٍ إِلَى الخَيْرِ.", "gloss": "Let every student strive for good.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لِيَسْعَى", "لِيَسْعَ")},
                 "why": "\"Let him\": the {لِـ} of order gives jazm. The alif drops."},
                {"s": "هِيَ لَمْ ___.", "gloss": "She did not cry.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَبْكِ", "تَبْكِي", "تَبْكِيَ")},
                 "why": "\"She\" is {تَبْكِي}. After {لَمْ} the {ي} drops: {تَبْكِ}."},
                {"s": "يَعْمَلُ كَيْ ___ بَيْتًا.", "gloss": "He works so that he can build a house.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَبْنِي", "يَبْنِيَ", "يَبْنِ")},
                 "why": "After {كَيْ}: naṣb. The fatha shows on the {ي}."},
            ],
        },
        {
            "title": "Iʿrāb: case and sign",
            "prompt": "لَمْ يَرْمِ اللَّاعِبُ الكُرَةَ إِلَى زَمِيلِهِ.",
            "en": "The player did not throw the ball to his teammate.",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR, JAZM]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, WEAK]},
            ],
            "rows": [
                {"s": "يَرْمِ", "ans": {"case": "jazm", "sign": "weak"},
                 "why": "Jazm after {لَمْ}. The {ي} drops."},
                {"s": "اللَّاعِبُ", "ans": {"case": "raf", "sign": "dam"},
                 "why": "Doer: rafʿ with damma."},
                {"s": "الكُرَةَ", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "Object: naṣb with fatha."},
                {"s": "زَمِيلِهِ", "ans": {"case": "jarr", "sign": "kas"},
                 "why": "After {إِلَى}: jarr with kasra."},
            ],
        },
        {
            "title": "Iʿrāb: case and sign",
            "prompt": "لَنْ يَنْسَى مُصْطَفَى دَرْسَهُ.",
            "en": "Muṣṭafā will not forget his lesson.",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JAZM]},
                {"key": "sign", "label": "Sign", "options": [FAT, HID, WEAK]},
            ],
            "rows": [
                {"s": "يَنْسَى", "ans": {"case": "nasb", "sign": "hid"},
                 "why": "{مَنْصُوبٌ بِلَنْ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ عَلَى الأَلِفِ}: hidden fatha."},
                {"s": "مُصْطَفَى", "ans": {"case": "raf", "sign": "hid"},
                 "why": "Doer, rafʿ. A maqṣūr noun: hidden damma on the alif."},
                {"s": "دَرْسَهُ", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "Object: naṣb with fatha."},
            ],
        },
        {
            "title": "Muʿrab or fixed? Choose the sign",
            "fields": [{"key": "sign", "label": "Sign", "options": [DAM, SUK, NUN, FIXED]}],
            "rows": [
                {"s": "البَنَاتُ [يَلْعَبْنَ] فِي الحَدِيقَةِ", "gloss": "the girls play in the garden", "ans": {"sign": "fixed"},
                 "why": "The nūn of women: fixed on sukūn, in the place of rafʿ."},
                {"s": "البِنْتُ [تَلْعَبُ] فِي الحَدِيقَةِ", "gloss": "the girl plays in the garden", "ans": {"sign": "dam"},
                 "why": "Nothing attached: muʿrab. Rafʿ with damma."},
                {"s": "البِنْتَانِ [تَلْعَبَانِ]", "gloss": "the two girls play", "ans": {"sign": "nun"},
                 "why": "A five verb in rafʿ: the nūn stays. This nūn is the sign of rafʿ."},
                {"s": "وَاللَّهِ [لَأَجْتَهِدَنَّ]", "gloss": "by Allah, I will surely work hard", "ans": {"sign": "fixed"},
                 "why": "The nūn of emphasis: fixed on fatha."},
                {"s": "المُدَرِّسَاتُ لَمْ [يَحْضُرْنَ]", "gloss": "the female teachers did not come", "ans": {"sign": "fixed"},
                 "why": "The nūn of women: fixed on sukūn, in the place of jazm. {لَمْ} cannot change it."},
                {"s": "الوَلَدُ لَمْ [يَحْضُرْ]", "gloss": "the boy did not come", "ans": {"sign": "suk"},
                 "why": "Nothing attached: jazm after {لَمْ} with sukūn."},
            ],
        },
        {
            "title": "Fill the table",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "يَشْكُو → لَمْ ___", "gloss": "he complains → he did not complain", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَشْكُ", "يَشْكُو", "يَشْكُوَ")},
                 "why": "Jazm: the {و} drops."},
                {"s": "يَجْرِي → لَنْ ___", "gloss": "he runs → he will not run", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَجْرِي", "يَجْرِيَ", "يَجْرِ")},
                 "why": "Naṣb: the fatha shows on the {ي}."},
                {"s": "يَبْقَى → لَمْ ___", "gloss": "he stays → he did not stay", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَبْقَى", "يَبْقِ", "يَبْقَ")},
                 "why": "Jazm: the alif drops. The fatha before it stays."},
                {"s": "يَبْقَى → لَنْ ___", "gloss": "he stays → he will not stay", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَبْقَى", "يَبْقَ")},
                 "why": "Naṣb on an alif: hidden fatha, the alif stays."},
                {"s": "يَقْضِي → لَمْ ___", "gloss": "he judges → he did not judge", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَقْضِي", "يَقْضِ", "يَقْضِيَ")},
                 "why": "Jazm: the {ي} drops. The kasra before it stays."},
                {"s": "يَعْلُو → لَنْ ___", "gloss": "it rises → it will not rise", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَعْلُوَ", "يَعْلُو", "يَعْلُ")},
                 "why": "Naṣb: the fatha shows on the {و}."},
            ],
        },
    ],
}
