# Stage 6, Unit 4: The diptote in jarr (المَمْنُوعُ مِنَ الصَّرْفِ فِي الجَرِّ)

KAS = {"k": "kas", "label": "Kasra · كَسْرَةٌ", "color": "green"}
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
YA = {"k": "ya", "label": "Yāʾ · اليَاءُ", "color": "purple"}

RAF = {"k": "raf", "label": "Rafʿ · رَفْعٌ", "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ", "color": "pink"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ", "color": "green"}

PREP = {"k": "prep", "label": "After a preposition · اِسْمٌ مَجْرُورٌ", "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
AND = {"k": "and", "label": "After وَ (and) · مَعْطُوفٌ", "color": "blue"}

R_ALONE = {"k": "alone", "label": "Diptote, no ال, no owner: fatha", "color": "orange"}
R_AL = {"k": "al", "label": "Diptote with ال: kasra", "color": "green"}
R_OWN = {"k": "own", "label": "Diptote with an owner: kasra", "color": "purple"}
R_NOT = {"k": "not", "label": "Not a diptote: kasra", "color": "grey"}
REASONS = [R_ALONE, R_AL, R_OWN, R_NOT]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s6-diptote",
    "order": 4,
    "title": "The diptote in jarr",
    "ar": "المَمْنُوعُ مِنَ الصَّرْفِ فِي الجَرِّ",
    "blurb": "A diptote takes fatha in jarr. With ال or an owner it takes kasra again.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 6 · UNIT 4", "title": "Fatha in place of kasra",
         "text": "In Stage 4 you met nouns that never take tanween. Now see what they do in jarr: they take fatha.",
         "wm": "بِأَحْمَدَ"},

        {"t": "h2", "text": "A diptote in jarr takes fatha"},
        {"t": "p", "text": "A normal noun in jarr takes kasra: {سَلَّمْتُ عَلَى خَالِدٍ}. A diptote takes fatha: {سَلَّمْتُ عَلَى أَحْمَدَ}. Both are jarr. Only the sign is different."},
        {"t": "rule", "color": "orange", "title": "Fatha stands in for kasra",
         "text": "A diptote with no {ال} and no owner is in jarr with fatha. Arabic says {الفَتْحَةُ نِيَابَةً عَنِ الكَسْرَةِ} \"fatha in place of kasra\". This is a branch sign."},
        {"t": "examples", "items": [
            {"ar": "سَلَّمْتُ عَلَى أَحْمَدَ.", "en": "I greeted Ahmad.", "note": "A name with the shape of a verb."},
            {"ar": "صَلَّيْتُ فِي مَسَاجِدَ كَثِيرَةٍ.", "en": "I prayed in many mosques.", "note": "A long plural."},
            {"ar": "سَمِعْتُ الخَبَرَ مِنْ أَصْدِقَاءَ.", "en": "I heard the news from friends.", "note": "A plural with the extra {ـَاءُ}."},
            {"ar": "سَافَرْتُ إِلَى مَكَّةَ.", "en": "I travelled to Makkah.", "note": "The name of a city is feminine."},
        ]},
        {"t": "tip", "text": "No tanween, and no kasra. Never write {أَحْمَدٍ} or {مَسَاجِدِ} with no {ال} and no owner."},

        {"t": "h2", "text": "Back to kasra: ال or an owner"},
        {"t": "p", "text": "Give the diptote {ال}, or put an owner after it. Then it takes kasra like any other noun. It is still in jarr."},
        {"t": "rule", "color": "green", "title": "ال or an owner brings kasra back",
         "text": "{فِي المَسَاجِدِ} \"in the mosques\". {فِي مَسَاجِدِ المَدِينَةِ} \"in the mosques of the city\"."},
        {"t": "table", "head": ["Diptote", "Alone: fatha", "With ال: kasra", "With an owner: kasra"], "rows": [
            ["مَسَاجِدُ", "فِي مَسَاجِدَ", "فِي المَسَاجِدِ", "فِي مَسَاجِدِ المَدِينَةِ"],
            ["مَدَارِسُ", "إِلَى مَدَارِسَ", "إِلَى المَدَارِسِ", "إِلَى مَدَارِسِ القَرْيَةِ"],
            ["أَصْدِقَاءُ", "مِنْ أَصْدِقَاءَ", "مِنَ الأَصْدِقَاءِ", "مِنْ أَصْدِقَاءِ خَالِدٍ"],
            ["صَحْرَاءُ", "فِي صَحْرَاءَ", "فِي الصَّحْرَاءِ", "فِي صَحْرَاءِ العَرَبِ"],
        ]},
        {"t": "p", "text": "Adjectives work the same way: {فِي البَيْتِ الأَبْيَضِ} \"in the white house\" (with {ال}), {فِي أَكْبَرِ مَسْجِدٍ} \"in the biggest mosque\" (with an owner)."},
        {"t": "tip", "text": "Names never take {ال} or an owner. So a diptote name in jarr always has fatha: {عَلَى أَحْمَدَ}، {إِلَى فَاطِمَةَ}، {مِنْ يُوسُفَ}."},

        {"t": "h2", "text": "Which nouns are diptotes? (review)"},
        {"t": "table", "head": ["Group", "Examples", "In jarr"], "rows": [
            ["Feminine names, or names with {ة}", "فَاطِمَةُ، زَيْنَبُ، مَرْيَمُ، حَمْزَةُ، مَكَّةُ", "إِلَى زَيْنَبَ"],
            ["Foreign names", "إِبْرَاهِيمُ، يُوسُفُ، إِسْمَاعِيلُ", "مِنْ يُوسُفَ"],
            ["Names with the shape of a verb", "أَحْمَدُ، يَزِيدُ", "عَلَى أَحْمَدَ"],
            ["Names ending in {ـَانُ}", "عُثْمَانُ، سُلَيْمَانُ، رَمَضَانُ", "فِي رَمَضَانَ"],
            ["Names on {فُعَلُ}", "عُمَرُ", "عَنْ عُمَرَ"],
            ["Adjectives {أَفْعَلُ} and {فَعْلَانُ}", "أَكْبَرُ، أَحْمَرُ، عَطْشَانُ", "فِي البَيْتِ الأَبْيَضِ"],
            ["The extra {ـَاءُ}", "صَحْرَاءُ، أَصْدِقَاءُ، عُلَمَاءُ", "مِنْ عُلَمَاءَ"],
            ["Long plurals", "مَسَاجِدُ، مَدَارِسُ، مَكَاتِبُ، مَفَاتِيحُ، شَوَارِعُ، حَدَائِقُ", "فِي حَدَائِقَ"],
        ]},
        {"t": "tip", "text": "Not diptotes: {مُحَمَّدٌ}، {خَالِدٌ}، {عَلِيٌّ}، {كُتُبٌ}، {أَقْلَامٌ}، {مَسْجِدٌ}، {سَمَاءٌ}. They take kasra in jarr: {عَلَى مُحَمَّدٍ}، {فِي كُتُبٍ}."},

        {"t": "h2", "text": "Both jarr jobs"},
        {"t": "p", "text": "The rule works for both jarr jobs: after a preposition and as the owner."},
        {"t": "examples", "items": [
            {"ar": "ذَهَبْتُ إِلَى بَيْتِ فَاطِمَةَ.", "en": "I went to Fatima's house.", "note": "{بَيْتِ} is after a preposition. {فَاطِمَةَ} is the owner: jarr with fatha."},
            {"ar": "قَرَأْتُ كِتَابَ إِبْرَاهِيمَ.", "en": "I read Ibrahim's book.", "note": "{إِبْرَاهِيمَ} is the owner: jarr with fatha. {كِتَابَ} is the object."},
            {"ar": "صُحُفِ إِبْرَاهِيمَ وَمُوسَى", "en": "the scrolls of Ibrahim and Musa (al-Aʿlā 87:19)", "note": "{إِبْرَاهِيمَ} is the owner of {صُحُفِ}: jarr with fatha."},
        ]},
        {"t": "tip", "text": "One phrase can have two diptotes: {مَفَاتِيحِ بَيْتِ عُمَرَ}. {مَفَاتِيحِ} has an owner, so kasra. {عُمَرَ} is a name with no owner, so fatha."},

        {"t": "h2", "text": "The full iʿrāb"},
        {"t": "p", "text": "Find the job. The job gives the case. The kind of noun gives the sign. For a diptote, also say why."},
        {"t": "examples", "items": [
            {"ar": "سَلَّمْتُ عَلَى أَحْمَدَ.", "en": "I greeted Ahmad.",
             "note": "{أَحْمَدَ}: {اسْمٌ مَجْرُورٌ بِـ(عَلَى) وَعَلَامَةُ جَرِّهِ الفَتْحَةُ نِيَابَةً عَنِ الكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ}"},
            {"ar": "هَذَا قَلَمُ زَيْنَبَ.", "en": "This is Zaynab's pen.",
             "note": "{زَيْنَبَ}: {مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الفَتْحَةُ نِيَابَةً عَنِ الكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ}"},
            {"ar": "صَلَّيْتُ فِي المَسَاجِدِ.", "en": "I prayed in the mosques.",
             "note": "{المَسَاجِدِ}: {اسْمٌ مَجْرُورٌ بِـ(فِي) وَعَلَامَةُ جَرِّهِ الكَسْرَةُ لِأَنَّهُ مُعَرَّفٌ بِأَلْ}"},
            {"ar": "صَلَّيْتُ فِي مَسَاجِدِ المَدِينَةِ.", "en": "I prayed in the mosques of the city.",
             "note": "{مَسَاجِدِ}: {اسْمٌ مَجْرُورٌ بِـ(فِي) وَعَلَامَةُ جَرِّهِ الكَسْرَةُ لِأَنَّهُ مُضَافٌ}"},
        ]},

        {"t": "h2", "text": "Fatha does not always mean naṣb"},
        {"t": "p", "text": "The same word can have fatha in naṣb and in jarr. The job tells you the case."},
        {"t": "table", "head": ["Sentence", "Job", "Case and sign"], "rows": [
            ["رَأَيْتُ أَحْمَدَ.", "Object", "Naṣb, fatha"],
            ["سَلَّمْتُ عَلَى أَحْمَدَ.", "After a preposition", "Jarr, fatha in place of kasra"],
            ["هَذَا بَيْتُ أَحْمَدَ.", "Owner", "Jarr, fatha in place of kasra"],
            ["جَاءَ أَحْمَدُ.", "Doer", "Rafʿ, damma"],
        ]},
        {"t": "tip", "text": "An adjective after a diptote keeps its own sign: {فِي مَسَاجِدَ كَثِيرَةٍ}. {كَثِيرَةٍ} is not a diptote, so it takes kasra."},

        {"t": "summary", "title": "In short", "items": [
            "A diptote in jarr with no {ال} and no owner takes fatha in place of kasra: {عَلَى أَحْمَدَ}، {فِي مَسَاجِدَ}.",
            "With {ال} or an owner it takes kasra: {فِي المَسَاجِدِ}، {فِي مَسَاجِدِ المَدِينَةِ}.",
            "Names never take {ال} or an owner, so a diptote name in jarr always has fatha.",
            "The rule is the same after a preposition and as the owner: {بَيْتُ فَاطِمَةَ}.",
            "Fatha on a diptote can be jarr or naṣb. The job decides.",
            "Formula: {اسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الفَتْحَةُ نِيَابَةً عَنِ الكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Which sign of jarr does the word in [brackets] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [KAS, FAT]}],
            "rows": [
                {"s": "سَلَّمْتُ عَلَى [أَحْمَدَ]", "gloss": "I greeted Ahmad.", "ans": {"sign": "fat"},
                 "why": "A diptote name with no {ال}: fatha in place of kasra."},
                {"s": "صَلَّيْتُ فِي [المَسَاجِدِ]", "gloss": "I prayed in the mosques.", "ans": {"sign": "kas"},
                 "why": "A long plural, but it has {ال}: kasra."},
                {"s": "سَافَرْتُ إِلَى [مَكَّةَ]", "gloss": "I travelled to Makkah.", "ans": {"sign": "fat"},
                 "why": "A city name is feminine: a diptote. Fatha in place of kasra."},
                {"s": "هَذَا كِتَابُ [فَاطِمَةَ]", "gloss": "This is Fatima's book.", "ans": {"sign": "fat"},
                 "why": "The owner, a feminine name: jarr with fatha."},
                {"s": "جَلَسْتُ فِي [مَكَاتِبِ] الشَّرِكَةِ", "gloss": "I sat in the company's offices.", "ans": {"sign": "kas"},
                 "why": "{مَكَاتِبِ} has an owner, {الشَّرِكَةِ}: kasra."},
                {"s": "سَلَّمْتُ عَلَى [خَالِدٍ]", "gloss": "I greeted Khalid.", "ans": {"sign": "kas"},
                 "why": "{خَالِدٌ} is not a diptote. Normal kasra with tanween."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "ذَهَبْتُ إِلَى ___", "gloss": "I went to Makkah.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَكَّةَ", "مَكَّةٍ", "مَكَّةِ")},
                 "why": "A diptote name: no tanween, fatha in place of kasra."},
                {"s": "صَلَّيْتُ فِي ___ كَثِيرَةٍ", "gloss": "I prayed in many mosques.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَسَاجِدٍ", "مَسَاجِدَ", "مَسَاجِدِ")},
                 "why": "No {ال}, no owner: {مَسَاجِدَ} with fatha."},
                {"s": "صَلَّيْتُ فِي ___", "gloss": "I prayed in the mosques.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المَسَاجِدَ", "المَسَاجِدِ", "المَسَاجِدُ")},
                 "why": "With {ال} the diptote takes kasra: {المَسَاجِدِ}."},
                {"s": "هَذَا بَيْتُ ___", "gloss": "This is Umar's house.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("عُمَرَ", "عُمَرٍ", "عُمَرِ")},
                 "why": "The owner, a name on {فُعَلُ}: jarr with fatha."},
                {"s": "سَلَّمْتُ عَلَى ___ خَالِدٍ", "gloss": "I greeted Khalid's friends.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَصْدِقَاءَ", "أَصْدِقَاءٍ", "أَصْدِقَاءِ")},
                 "why": "{أَصْدِقَاءِ} has an owner, {خَالِدٍ}: kasra."},
                {"s": "أَخَذْتُ القَلَمَ مِنْ ___", "gloss": "I took the pen from Yusuf.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يُوسُفٍ", "يُوسُفَ", "يُوسُفِ")},
                 "why": "A foreign name: fatha in place of kasra."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "سَلَّمْتُ عَلَى أَصْدِقَاءِ أَحْمَدَ فِي المَسْجِدِ.",
            "en": "I greeted Ahmad's friends in the mosque.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PREP, OWNER]},
                {"key": "sign", "label": "Sign", "options": [KAS, FAT]},
            ],
            "rows": [
                {"s": "أَصْدِقَاءِ", "gloss": "friends", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {عَلَى}. A diptote, but it has an owner: kasra."},
                {"s": "أَحْمَدَ", "gloss": "Ahmad", "ans": {"job": "owner", "sign": "fat"},
                 "why": "The owner of {أَصْدِقَاءِ}. A diptote name: fatha in place of kasra."},
                {"s": "المَسْجِدِ", "gloss": "the mosque", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {فِي}. A singular with {ال}: kasra."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "قَرَأْتُ عَنْ عُلَمَاءَ كِبَارٍ فِي مَكْتَبَةِ إِبْرَاهِيمَ.",
            "en": "I read about great scholars in Ibrahim's library.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PREP, OWNER, ADJ]},
                {"key": "sign", "label": "Sign", "options": [KAS, FAT]},
            ],
            "rows": [
                {"s": "عُلَمَاءَ", "gloss": "scholars", "ans": {"job": "prep", "sign": "fat"},
                 "why": "After {عَنْ}. The extra {ـَاءُ}, no {ال}, no owner: fatha in place of kasra."},
                {"s": "كِبَارٍ", "gloss": "great", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {عُلَمَاءَ}, so it is jarr too. {كِبَارٌ} is not a diptote: kasra."},
                {"s": "مَكْتَبَةِ", "gloss": "library", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {فِي}. A normal singular: kasra."},
                {"s": "إِبْرَاهِيمَ", "gloss": "Ibrahim", "ans": {"job": "owner", "sign": "fat"},
                 "why": "The owner of {مَكْتَبَةِ}. A foreign name: fatha in place of kasra."},
            ],
        },
        {
            "title": "Why fatha or kasra? Look at the noun after the preposition",
            "fields": [{"key": "why", "label": "Reason", "options": REASONS}],
            "rows": [
                {"s": "فِي مَدَارِسَ كَثِيرَةٍ", "gloss": "in many schools", "ans": {"why": "alone"},
                 "why": "{مَدَارِسَ} is a long plural with no {ال} and no owner."},
                {"s": "فِي مَدَارِسِ المَدِينَةِ", "gloss": "in the schools of the city", "ans": {"why": "own"},
                 "why": "{المَدِينَةِ} is its owner."},
                {"s": "فِي المَدَارِسِ", "gloss": "in the schools", "ans": {"why": "al"},
                 "why": "{ال} brings back the kasra."},
                {"s": "فِي مَدْرَسَةٍ كَبِيرَةٍ", "gloss": "in a big school", "ans": {"why": "not"},
                 "why": "The singular {مَدْرَسَةٌ} takes tanween. It is not a diptote."},
                {"s": "إِلَى يُوسُفَ", "gloss": "to Yusuf", "ans": {"why": "alone"},
                 "why": "A foreign name. Names have no {ال} and no owner."},
                {"s": "فِي الصَّحْرَاءِ", "gloss": "in the desert", "ans": {"why": "al"},
                 "why": "{صَحْرَاءُ} is a diptote, but here it has {ال}."},
            ],
        },
        {
            "title": "Review: fatha in jarr or in naṣb? Find the case of the word in [brackets]",
            "fields": [{"key": "case", "label": "Case", "options": [RAF, NASB, JARR]}],
            "rows": [
                {"s": "رَأَيْتُ [أَحْمَدَ]", "gloss": "I saw Ahmad.", "ans": {"case": "nasb"},
                 "why": "The object: naṣb with fatha."},
                {"s": "سَلَّمْتُ عَلَى [أَحْمَدَ]", "gloss": "I greeted Ahmad.", "ans": {"case": "jarr"},
                 "why": "After {عَلَى}: jarr, fatha in place of kasra."},
                {"s": "جَاءَ [أَحْمَدُ]", "gloss": "Ahmad came.", "ans": {"case": "raf"},
                 "why": "The doer: rafʿ with one damma."},
                {"s": "هَذَا قَلَمُ [أَحْمَدَ]", "gloss": "This is Ahmad's pen.", "ans": {"case": "jarr"},
                 "why": "The owner: jarr, fatha in place of kasra."},
                {"s": "زُرْتُ [مَكَّةَ]", "gloss": "I visited Makkah.", "ans": {"case": "nasb"},
                 "why": "The object of {زُرْتُ}: naṣb with fatha."},
                {"s": "سَافَرْتُ إِلَى [مَكَّةَ]", "gloss": "I travelled to Makkah.", "ans": {"case": "jarr"},
                 "why": "After {إِلَى}: jarr, fatha in place of kasra."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "صَلَّيْتُ فِي ___ مَسْجِدٍ فِي المَدِينَةِ", "gloss": "I prayed in the biggest mosque in the city.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَكْبَرَ", "أَكْبَرِ", "أَكْبَرٍ")},
                 "why": "{أَكْبَرُ} is a diptote, but here it has an owner, {مَسْجِدٍ}: kasra."},
                {"s": "مَشَيْتُ فِي ___ المَدِينَةِ", "gloss": "I walked in the streets of the city.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("شَوَارِعَ", "شَوَارِعِ", "شَوَارِعٍ")},
                 "why": "A long plural with an owner: kasra."},
                {"s": "جَلَسْنَا فِي ___ جَمِيلَةٍ", "gloss": "We sat in beautiful gardens.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("حَدَائِقَ", "حَدَائِقٍ", "حَدَائِقِ")},
                 "why": "A long plural, no {ال}, no owner: fatha in place of kasra."},
                {"s": "كَتَبْتُ رِسَالَةً إِلَى ___", "gloss": "I wrote a letter to Uthman.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("عُثْمَانَ", "عُثْمَانٍ", "عُثْمَانِ")},
                 "why": "A name ending in {ـَانُ}: fatha in place of kasra."},
                {"s": "خَرَجْنَا مِنَ ___", "gloss": "We went out of the desert.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الصَّحْرَاءَ", "الصَّحْرَاءِ", "الصَّحْرَاءُ")},
                 "why": "With {ال} the diptote takes kasra."},
                {"s": "أَخَذْتُ الكِتَابَ مِنْ ___", "gloss": "I took the book from Hamza.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("حَمْزَةٍ", "حَمْزَةِ", "حَمْزَةَ")},
                 "why": "A man's name ending in {ة}: a diptote. Fatha in place of kasra."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "كَتَبْتُ رِسَالَةً مِنْ مَكَّةَ إِلَى يُوسُفَ وَزَيْنَبَ.",
            "en": "I wrote a letter from Makkah to Yusuf and Zaynab.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PREP, OWNER, AND]},
                {"key": "sign", "label": "Sign", "options": [KAS, FAT]},
            ],
            "rows": [
                {"s": "مَكَّةَ", "gloss": "Makkah", "ans": {"job": "prep", "sign": "fat"},
                 "why": "After {مِنْ}. A city name, feminine: fatha in place of kasra."},
                {"s": "يُوسُفَ", "gloss": "Yusuf", "ans": {"job": "prep", "sign": "fat"},
                 "why": "After {إِلَى}. A foreign name: fatha in place of kasra."},
                {"s": "زَيْنَبَ", "gloss": "Zaynab", "ans": {"job": "and", "sign": "fat"},
                 "why": "After {وَ}, it copies the jarr of {يُوسُفَ}. A feminine name: fatha in place of kasra."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "نَظَرْتُ إِلَى مَفَاتِيحِ بَيْتِ عُمَرَ.",
            "en": "I looked at the keys of Umar's house.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PREP, OWNER, ADJ]},
                {"key": "sign", "label": "Sign", "options": [KAS, FAT]},
            ],
            "rows": [
                {"s": "مَفَاتِيحِ", "gloss": "keys", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {إِلَى}. A long plural, but it has an owner: kasra."},
                {"s": "بَيْتِ", "gloss": "house", "ans": {"job": "owner", "sign": "kas"},
                 "why": "The owner of {مَفَاتِيحِ}. A normal singular: kasra."},
                {"s": "عُمَرَ", "gloss": "Umar", "ans": {"job": "owner", "sign": "fat"},
                 "why": "The owner of {بَيْتِ}. A name on {فُعَلُ}: fatha in place of kasra."},
            ],
        },
        {
            "title": "Why fatha or kasra? Look at the noun after the preposition",
            "fields": [{"key": "why", "label": "Reason", "options": REASONS}],
            "rows": [
                {"s": "فِي أَكْبَرِ مَسْجِدٍ", "gloss": "in the biggest mosque", "ans": {"why": "own"},
                 "why": "{أَكْبَرُ} is a diptote. {مَسْجِدٍ} is its owner."},
                {"s": "مِنْ عُلَمَاءَ كِبَارٍ", "gloss": "from great scholars", "ans": {"why": "alone"},
                 "why": "{عُلَمَاءَ} has the extra {ـَاءُ}, no {ال} and no owner."},
                {"s": "بِالأَصْدِقَاءِ", "gloss": "with the friends", "ans": {"why": "al"},
                 "why": "{أَصْدِقَاءُ} is a diptote, but here it has {ال}."},
                {"s": "عَلَى مُحَمَّدٍ", "gloss": "upon Muhammad", "ans": {"why": "not"},
                 "why": "{مُحَمَّدٌ} takes tanween. It is not a diptote."},
                {"s": "لِزَيْنَبَ", "gloss": "for Zaynab", "ans": {"why": "alone"},
                 "why": "A feminine name. Names have no {ال} and no owner."},
                {"s": "فِي مَطَابِخِ الفُنْدُقِ", "gloss": "in the kitchens of the hotel", "ans": {"why": "own"},
                 "why": "{مَطَابِخِ} is a long plural. {الفُنْدُقِ} is its owner."},
            ],
        },
        {
            "title": "Which phrase is right?",
            "fields": [{"key": "pick", "label": "Phrase", "options": []}],
            "rows": [
                {"s": "in the mosques of the city", "ans": {"pick": "b"},
                 "opts": {"pick": pick("فِي مَسَاجِدَ المَدِينَةِ", "فِي مَسَاجِدِ المَدِينَةِ", "فِي مَسَاجِدٍ المَدِينَةِ")},
                 "why": "The diptote has an owner, so kasra: {مَسَاجِدِ}."},
                {"s": "to Ahmad", "ans": {"pick": "c"},
                 "opts": {"pick": pick("إِلَى أَحْمَدٍ", "إِلَى أَحْمَدِ", "إِلَى أَحْمَدَ")},
                 "why": "A diptote name: fatha in place of kasra, no tanween."},
                {"s": "from many friends", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مِنْ أَصْدِقَاءَ كَثِيرِينَ", "مِنْ أَصْدِقَاءٍ كَثِيرِينَ", "مِنْ أَصْدِقَاءُ كَثِيرِينَ")},
                 "why": "No {ال}, no owner: {أَصْدِقَاءَ}. The adjective {كَثِيرِينَ} is a sound masculine plural: yāʾ."},
                {"s": "about the scholars", "ans": {"pick": "b"},
                 "opts": {"pick": pick("عَنِ العُلَمَاءَ", "عَنِ العُلَمَاءِ", "عَنِ العُلَمَاءٍ")},
                 "why": "With {ال} the diptote takes kasra."},
                {"s": "in Fatima's house", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فِي بَيْتِ فَاطِمَةَ", "فِي بَيْتِ فَاطِمَةٍ", "فِي بَيْتَ فَاطِمَةَ")},
                 "why": "{بَيْتِ} is after {فِي}: kasra. {فَاطِمَةَ} is the owner: fatha in place of kasra."},
            ],
        },
        {
            "title": "All the jarr signs: which sign does the word in [brackets] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [KAS, FAT, YA]}],
            "rows": [
                {"s": "سَمِعْتُ مِنَ [المُسْلِمِينَ]", "gloss": "I heard from the Muslims.", "ans": {"sign": "ya"},
                 "why": "A sound masculine plural: yāʾ."},
                {"s": "أَرْسَلْتُ الكِتَابَ إِلَى [عُثْمَانَ]", "gloss": "I sent the book to Uthman.", "ans": {"sign": "fat"},
                 "why": "A diptote name: fatha in place of kasra."},
                {"s": "سَلَّمْتُ عَلَى [الطَّالِبَاتِ]", "gloss": "I greeted the female students.", "ans": {"sign": "kas"},
                 "why": "A sound feminine plural: kasra."},
                {"s": "جَلَسْنَا فِي [حَدَائِقِ] البَيْتِ", "gloss": "We sat in the gardens of the house.", "ans": {"sign": "kas"},
                 "why": "A long plural with an owner: kasra."},
                {"s": "سَلَّمْتُ عَلَى [أَبِيكَ]", "gloss": "I greeted your father.", "ans": {"sign": "ya"},
                 "why": "One of the five nouns: yāʾ."},
                {"s": "هَذِهِ سَيَّارَةُ [عُمَرَ]", "gloss": "This is Umar's car.", "ans": {"sign": "fat"},
                 "why": "The owner, a diptote name: fatha in place of kasra."},
            ],
        },
    ],
}
