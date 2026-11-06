# Stage 6, Unit 5: Followers in jarr (التَّوَابِعُ المَجْرُورَةُ)

KAS = {"k": "kas", "label": "Kasra · كَسْرَةٌ", "color": "green"}
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
YA = {"k": "ya", "label": "Yāʾ · اليَاءُ", "color": "purple"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}

PREP = {"k": "prep", "label": "After a preposition · اِسْمٌ مَجْرُورٌ", "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
AND = {"k": "and", "label": "After وَ (and) · مَعْطُوفٌ", "color": "blue"}
TAWK = {"k": "tawk", "label": "Emphasis · تَوْكِيدٌ", "color": "grey"}
BADAL = {"k": "badal", "label": "Substitute · بَدَلٌ", "color": "grey"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s6-followers",
    "order": 5,
    "title": "Followers in jarr",
    "ar": "التَّوَابِعُ المَجْرُورَةُ",
    "blurb": "Adjective, after وَ, emphasis and substitute: they copy the jarr, and their own kind gives the sign.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 6 · UNIT 5", "title": "Followers copy the jarr",
         "text": "Some words have no case of their own. They follow a noun and copy its case. When the noun is in jarr, they are in jarr too.",
         "wm": "التَّوَابِعُ"},

        {"t": "h2", "text": "The four followers"},
        {"t": "p", "text": "You met them in Stage 5 in rafʿ. Here they follow a noun in jarr."},
        {"t": "cols", "items": [
            {"color": "grey", "title": "Adjective", "ar": "نَعْتٌ", "text": "{بِالطُّلَّابِ المُجْتَهِدِينَ}"},
            {"color": "blue", "title": "After وَ", "ar": "مَعْطُوفٌ", "text": "{عَلَى أَبِيكَ وَأَخِيكَ}"},
            {"color": "grey", "title": "Emphasis", "ar": "تَوْكِيدٌ", "text": "{بِالقَوْمِ كُلِّهِمْ}"},
            {"color": "grey", "title": "Substitute", "ar": "بَدَلٌ", "text": "{عَنِ الخَلِيفَةِ عُمَرَ}"},
        ]},

        {"t": "h2", "text": "Same case, own sign"},
        {"t": "rule", "color": "green", "title": "Copy the case only",
         "text": "The follower takes the case of the noun it follows: jarr. Its own kind of noun gives its sign. So the two signs can be different."},
        {"t": "table", "head": ["Phrase", "The noun", "The follower"], "rows": [
            ["مَرَرْتُ بِالطُّلَّابِ المُجْتَهِدِينَ", "{الطُّلَّابِ}: broken plural, kasra", "{المُجْتَهِدِينَ}: sound m. plural, yāʾ"],
            ["صَلَّيْتُ فِي مَسَاجِدَ كَثِيرَةٍ", "{مَسَاجِدَ}: diptote, fatha", "{كَثِيرَةٍ}: singular, kasra"],
            ["سَلَّمْتُ عَلَى خَالِدٍ وَأَحْمَدَ", "{خَالِدٍ}: singular, kasra", "{أَحْمَدَ}: diptote, fatha"],
            ["جَلَسْتُ فِي البَيْتَيْنِ الكَبِيرَيْنِ", "{البَيْتَيْنِ}: dual, yāʾ", "{الكَبِيرَيْنِ}: dual, yāʾ"],
            ["نَظَرْتُ إِلَى الطَّالِبَاتِ المُجْتَهِدَاتِ", "{الطَّالِبَاتِ}: sound f. plural, kasra", "{المُجْتَهِدَاتِ}: sound f. plural, kasra"],
            ["سَلَّمْتُ عَلَى القَاضِي العَادِلِ", "{القَاضِي}: hidden kasra", "{العَادِلِ}: singular, kasra"],
        ]},

        {"t": "h2", "text": "The adjective (نَعْتٌ)"},
        {"t": "p", "text": "The adjective comes after its noun. It copies the case, {ال} or tanween, gender and number. A plural of things takes a feminine singular adjective: {مَسَاجِدَ كَثِيرَةٍ}."},
        {"t": "examples", "items": [
            {"ar": "مَرَرْتُ بِالطُّلَّابِ المُجْتَهِدِينَ.", "en": "I passed by the hardworking students.",
             "note": "{المُجْتَهِدِينَ}: {نَعْتٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}"},
            {"ar": "جَلَسْتُ فِي السَّيَّارَةِ الحَمْرَاءِ.", "en": "I sat in the red car.",
             "note": "{الحَمْرَاءِ} is a diptote, but it has {ال}: kasra."},
            {"ar": "بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيمِ", "en": "In the name of Allah, the Most Merciful, the Very Merciful (al-Fātiḥa 1:1)",
             "note": "{الرَّحْمٰنِ} and {الرَّحِيمِ} are adjectives. {اللّٰهِ} is the owner, in jarr, so they are in jarr with kasra."},
        ]},

        {"t": "h2", "text": "After وَ، ثُمَّ، أَوْ (مَعْطُوفٌ)"},
        {"t": "p", "text": "A noun after {وَ} \"and\", {ثُمَّ} \"then\" or {أَوْ} \"or\" copies the case of the noun before it."},
        {"t": "examples", "items": [
            {"ar": "سَلَّمْتُ عَلَى أَبِيكَ وَأَخِيكَ.", "en": "I greeted your father and your brother.",
             "note": "{أَخِيكَ}: {اسْمٌ مَعْطُوفٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ}"},
            {"ar": "ذَهَبْتُ إِلَى المَسْجِدِ ثُمَّ السُّوقِ.", "en": "I went to the mosque, then the market.",
             "note": "{السُّوقِ} follows {المَسْجِدِ}: jarr with kasra."},
            {"ar": "اِجْلِسْ عَلَى الكُرْسِيِّ أَوِ السَّرِيرِ.", "en": "Sit on the chair or the bed.",
             "note": "{السَّرِيرِ} follows {الكُرْسِيِّ}: jarr with kasra."},
        ]},
        {"t": "tip", "text": "If the preposition comes again, the noun is not a follower: {ذَهَبْتُ إِلَى المَسْجِدِ ثُمَّ إِلَى السُّوقِ}. Here {السُّوقِ} is after a preposition."},

        {"t": "h2", "text": "Emphasis (تَوْكِيدٌ)"},
        {"t": "p", "text": "{نَفْسُ} and {عَيْنُ} mean \"himself, itself\". {كُلُّ} means \"all of\". They take a pronoun that matches the noun. The pronoun is the owner, in the place of jarr."},
        {"t": "table", "head": ["Phrase", "Meaning"], "rows": [
            ["مَرَرْتُ بِالمُدِيرِ نَفْسِهِ", "I passed by the headmaster himself."],
            ["سَلَّمْتُ عَلَى المُدِيرَةِ نَفْسِهَا", "I greeted the headmistress herself."],
            ["سَأَلْتُ عَنِ الرَّجُلِ عَيْنِهِ", "I asked about the man himself."],
            ["سَلَّمْتُ عَلَى الطُّلَّابِ كُلِّهِمْ", "I greeted all the students."],
            ["مَرَرْتُ بِالبُيُوتِ كُلِّهَا", "I passed by all the houses."],
            ["سَلَّمْتُ عَلَى المُعَلِّمِينَ أَنْفُسِهِمْ", "I greeted the teachers themselves."],
        ]},
        {"t": "examples", "items": [
            {"ar": "سَلَّمْتُ عَلَى الطُّلَّابِ كُلِّهِمْ.", "en": "I greeted all the students.",
             "note": "{كُلِّهِمْ}: {تَوْكِيدٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}, and {هُمْ} is {ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ}."},
        ]},
        {"t": "tip", "text": "For three or more people use {أَنْفُسِ}: {أَنْفُسِهِمْ}. For things in the plural use {ـهَا}: {البُيُوتِ كُلِّهَا}."},

        {"t": "h2", "text": "The substitute (بَدَلٌ)"},
        {"t": "p", "text": "A substitute names the same person again, more clearly. It copies the case."},
        {"t": "examples", "items": [
            {"ar": "سَلَّمْتُ عَلَى أَخِيكَ زَيْدٍ.", "en": "I greeted your brother Zayd.",
             "note": "{زَيْدٍ}: {بَدَلٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الكَسْرَةُ}"},
            {"ar": "قَرَأْتُ عَنِ الخَلِيفَةِ عُمَرَ.", "en": "I read about the caliph Umar.",
             "note": "{عُمَرَ}: {بَدَلٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الفَتْحَةُ نِيَابَةً عَنِ الكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ}"},
        ]},

        {"t": "h2", "text": "Which word does it follow?"},
        {"t": "p", "text": "After an iḍāfa, an adjective can describe the first word or the owner. Look at its last vowel. It copies the case of the word it describes."},
        {"t": "table", "head": ["Sentence", "The adjective follows"], "rows": [
            ["هَذَا كِتَابُ الطَّالِبِ المُجْتَهِدِ.", "{الطَّالِبِ} (jarr): the hardworking student's book"],
            ["بَيْتُ الرَّجُلِ الكَبِيرُ جَمِيلٌ.", "{بَيْتُ} (rafʿ): the man's big house is beautiful"],
            ["قَرَأْتُ كِتَابَ المُدَرِّسِ الجَدِيدَ.", "{كِتَابَ} (naṣb): I read the teacher's new book"],
        ]},

        {"t": "summary", "title": "In short", "items": [
            "Four followers: adjective, after {وَ}/{ثُمَّ}/{أَوْ}, emphasis, substitute.",
            "A follower of a noun in jarr is in jarr too.",
            "Its own kind gives the sign: {بِالطُّلَّابِ المُجْتَهِدِينَ}، {فِي مَسَاجِدَ كَثِيرَةٍ}، {عَلَى خَالِدٍ وَأَحْمَدَ}.",
            "Emphasis {نَفْسِ}، {عَيْنِ}، {كُلِّ} takes a matching pronoun: {بِالقَوْمِ كُلِّهِمْ}.",
            "If the preposition comes again, the noun is after a preposition, not a follower.",
            "After an iḍāfa, the last vowel shows which word the adjective follows.",
        ]},
    ],

    "practice": [
        {
            "title": "Find the job",
            "prompt": "سَلَّمْتُ عَلَى المُدِيرِ نَفْسِهِ وَالمُعَلِّمِينَ الجُدُدِ.",
            "en": "I greeted the headmaster himself and the new teachers.",
            "fields": [{"key": "job", "label": "Job", "options": [PREP, ADJ, AND, TAWK]}],
            "rows": [
                {"s": "المُدِيرِ", "gloss": "the headmaster", "ans": {"job": "prep"},
                 "why": "It comes after {عَلَى}: jarr with kasra."},
                {"s": "نَفْسِهِ", "gloss": "himself", "ans": {"job": "tawk"},
                 "why": "{نَفْسُ} + a matching pronoun: emphasis. It copies the jarr of {المُدِيرِ}."},
                {"s": "المُعَلِّمِينَ", "gloss": "the teachers", "ans": {"job": "and"},
                 "why": "After {وَ}, it copies the jarr of {المُدِيرِ}. A sound masculine plural: yāʾ."},
                {"s": "الجُدُدِ", "gloss": "new", "ans": {"job": "adj"},
                 "why": "It describes {المُعَلِّمِينَ}. A broken plural: kasra."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "مَرَرْتُ بِالطُّلَّابِ ___", "gloss": "I passed by the hardworking students.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُجْتَهِدُونَ", "المُجْتَهِدِينَ", "المُجْتَهِدِ")},
                 "why": "The adjective is in jarr. A sound masculine plural: yāʾ."},
                {"s": "سَلَّمْتُ عَلَى أَبِيكَ وَ___", "gloss": "I greeted your father and your brother.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَخُوكَ", "أَخَاكَ", "أَخِيكَ")},
                 "why": "After {وَ}, jarr like {أَبِيكَ}. One of the five nouns: yāʾ."},
                {"s": "جَلَسْتُ فِي البَيْتَيْنِ ___", "gloss": "I sat in the two big houses.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الكَبِيرَيْنِ", "الكَبِيرَانِ", "الكَبِيرِينَ")},
                 "why": "A dual adjective in jarr: {ـَيْنِ}. {الكَبِيرِينَ} would be a plural."},
                {"s": "نَظَرْتُ إِلَى الطَّالِبَاتِ ___", "gloss": "I looked at the hardworking female students.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُجْتَهِدَاتُ", "المُجْتَهِدَاتِ", "المُجْتَهِدِينَ")},
                 "why": "A sound feminine plural in jarr: kasra."},
                {"s": "سَلَّمْتُ عَلَى الضُّيُوفِ ___", "gloss": "I greeted all the guests.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("كُلُّهُمْ", "كُلَّهُمْ", "كُلِّهِمْ")},
                 "why": "Emphasis copies the jarr of {الضُّيُوفِ}: kasra."},
                {"s": "سَلَّمْتُ عَلَى خَالِدٍ وَ___", "gloss": "I greeted Khalid and Ahmad.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَحْمَدَ", "أَحْمَدٍ", "أَحْمَدِ")},
                 "why": "After {وَ}, jarr. A diptote name: fatha in place of kasra."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "سَلَّمْتُ عَلَى المُسْلِمِينَ وَالمُسْلِمَاتِ فِي المَسْجِدِ الكَبِيرِ.",
            "en": "I greeted the Muslim men and women in the big mosque.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PREP, ADJ, AND]},
                {"key": "sign", "label": "Sign", "options": [KAS, FAT, YA]},
            ],
            "rows": [
                {"s": "المُسْلِمِينَ", "gloss": "the Muslim men", "ans": {"job": "prep", "sign": "ya"},
                 "why": "After {عَلَى}. A sound masculine plural: yāʾ."},
                {"s": "المُسْلِمَاتِ", "gloss": "the Muslim women", "ans": {"job": "and", "sign": "kas"},
                 "why": "After {وَ}, jarr. A sound feminine plural: kasra."},
                {"s": "المَسْجِدِ", "gloss": "the mosque", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {فِي}. A singular: kasra."},
                {"s": "الكَبِيرِ", "gloss": "big", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {المَسْجِدِ}: jarr with kasra."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "قَرَأْتُ عَنِ الخَلِيفَةِ عُمَرَ فِي كِتَابٍ جَدِيدٍ.",
            "en": "I read about the caliph Umar in a new book.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PREP, ADJ, BADAL]},
                {"key": "sign", "label": "Sign", "options": [KAS, FAT]},
            ],
            "rows": [
                {"s": "الخَلِيفَةِ", "gloss": "the caliph", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {عَنْ}. A singular with {ال}: kasra."},
                {"s": "عُمَرَ", "gloss": "Umar", "ans": {"job": "badal", "sign": "fat"},
                 "why": "It names the caliph again: a substitute in jarr. A diptote name: fatha in place of kasra."},
                {"s": "كِتَابٍ", "gloss": "a book", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {فِي}. A singular: kasra with tanween."},
                {"s": "جَدِيدٍ", "gloss": "new", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {كِتَابٍ}: jarr, kasra with tanween."},
            ],
        },
        {
            "title": "Which sign does the follower in [brackets] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [KAS, FAT, YA]}],
            "rows": [
                {"s": "جَلَسْتُ فِي البَيْتِ [الجَدِيدِ]", "gloss": "I sat in the new house.", "ans": {"sign": "kas"},
                 "why": "An adjective in jarr. A singular: kasra."},
                {"s": "سَمِعْتُ مِنَ الطَّالِبَيْنِ [المُجْتَهِدَيْنِ]", "gloss": "I heard from the two hardworking students.", "ans": {"sign": "ya"},
                 "why": "A dual adjective in jarr: yāʾ."},
                {"s": "سَلَّمْتُ عَلَى زَيْنَبَ وَ[مَرْيَمَ]", "gloss": "I greeted Zaynab and Maryam.", "ans": {"sign": "fat"},
                 "why": "After {وَ}, jarr. A feminine name: fatha in place of kasra."},
                {"s": "مَرَرْتُ بِالأَوْلَادِ [كُلِّهِمْ]", "gloss": "I passed by all the boys.", "ans": {"sign": "kas"},
                 "why": "Emphasis in jarr: kasra."},
                {"s": "كَتَبْتُ إِلَى المُسْلِمِينَ [الصَّادِقِينَ]", "gloss": "I wrote to the truthful Muslims.", "ans": {"sign": "ya"},
                 "why": "A sound masculine plural adjective in jarr: yāʾ."},
                {"s": "سَأَلْتُ عَنْ أَبِيكَ وَ[أَخِيكَ]", "gloss": "I asked about your father and your brother.", "ans": {"sign": "ya"},
                 "why": "After {وَ}, jarr. One of the five nouns: yāʾ."},
            ],
        },
        {
            "title": "Which word does the adjective in [brackets] follow?",
            "fields": [{"key": "pick", "label": "It follows", "options": []}],
            "rows": [
                {"s": "هَذَا بَيْتُ الرَّجُلِ [الكَرِيمِ]", "gloss": "This is the generous man's house.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("بَيْتُ", "الرَّجُلِ")},
                 "why": "Kasra, like {الرَّجُلِ}, the owner in jarr."},
                {"s": "بَيْتُ الرَّجُلِ [الكَبِيرُ] جَمِيلٌ", "gloss": "The man's big house is beautiful.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بَيْتُ", "الرَّجُلِ")},
                 "why": "Damma, like {بَيْتُ}, the topic in rafʿ."},
                {"s": "قَرَأْتُ كِتَابَ المُدَرِّسِ [الجَدِيدَ]", "gloss": "I read the teacher's new book.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("كِتَابَ", "المُدَرِّسِ")},
                 "why": "Fatha, like {كِتَابَ}, the object in naṣb."},
                {"s": "هَذَا كِتَابُ الطَّالِبِ [المُجْتَهِدِ]", "gloss": "This is the hardworking student's book.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("كِتَابُ", "الطَّالِبِ")},
                 "why": "Kasra, like {الطَّالِبِ}, the owner in jarr."},
                {"s": "ذَهَبْتُ إِلَى مَدْرَسَةِ الوَلَدِ [الجَدِيدَةِ]", "gloss": "I went to the boy's new school.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَدْرَسَةِ", "الوَلَدِ")},
                 "why": "Both are in jarr. {الجَدِيدَةِ} is feminine, like {مَدْرَسَةِ}. For the boy it would be {الجَدِيدِ}."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Find the job",
            "prompt": "سَلَّمْتُ عَلَى الضُّيُوفِ كُلِّهِمْ ثُمَّ عَلَى صَدِيقِي خَالِدٍ.",
            "en": "I greeted all the guests, then my friend Khalid.",
            "fields": [{"key": "job", "label": "Job", "options": [PREP, AND, TAWK, BADAL]}],
            "rows": [
                {"s": "الضُّيُوفِ", "gloss": "the guests", "ans": {"job": "prep"},
                 "why": "After {عَلَى}: jarr with kasra."},
                {"s": "كُلِّهِمْ", "gloss": "all of them", "ans": {"job": "tawk"},
                 "why": "{كُلُّ} + a matching pronoun: emphasis in jarr."},
                {"s": "صَدِيقِي", "gloss": "my friend", "ans": {"job": "prep"},
                 "why": "{عَلَى} comes again after {ثُمَّ}, so this noun is after a preposition. Hidden kasra."},
                {"s": "خَالِدٍ", "gloss": "Khalid", "ans": {"job": "badal"},
                 "why": "It names my friend again: a substitute in jarr, kasra."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "نَظَرْتُ إِلَى المُهَنْدِسِينَ ___", "gloss": "I looked at the engineers themselves.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَنْفُسِهِمْ", "أَنْفُسُهُمْ", "أَنْفُسَهُمْ")},
                 "why": "Emphasis copies the jarr of {المُهَنْدِسِينَ}. {أَنْفُسٌ} is a broken plural: kasra."},
                {"s": "صَلَّيْنَا فِي مَسَاجِدَ ___", "gloss": "We prayed in many mosques.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("كَثِيرَةَ", "كَثِيرَةٍ", "كَثِيرَةٌ")},
                 "why": "The adjective is jarr. It is not a diptote, so kasra with tanween. Do not copy the fatha of {مَسَاجِدَ}."},
                {"s": "سَلَّمْتُ عَلَى الضَّيْفَيْنِ وَ___", "gloss": "I greeted the two guests and their father.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَبُوهُمَا", "أَبَاهُمَا", "أَبِيهِمَا")},
                 "why": "After {وَ}, jarr. One of the five nouns: yāʾ."},
                {"s": "سَأَلْتُ عَنِ المُدِيرِ ___", "gloss": "I asked about the headmaster himself.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("عَيْنِهِ", "عَيْنُهُ", "عَيْنَهُ")},
                 "why": "Emphasis with {عَيْنُ}, in jarr: kasra."},
                {"s": "كَتَبْتُ إِلَى المُدَرِّسَاتِ ___", "gloss": "I wrote to the new female teachers.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الجَدِيدَاتَ", "الجَدِيدَاتِ", "الجَدِيدِينَ")},
                 "why": "A sound feminine plural adjective in jarr: kasra. {الجَدِيدِينَ} is masculine."},
                {"s": "هَذَا بَيْتُ أَحْمَدَ وَ___", "gloss": "This is the house of Ahmad and Fatima.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فَاطِمَةَ", "فَاطِمَةٍ", "فَاطِمَةِ")},
                 "why": "After {وَ}, it copies the jarr of the owner {أَحْمَدَ}. A feminine name: fatha in place of kasra."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "سَافَرْتُ إِلَى المَدِينَةِ ثُمَّ مَكَّةَ فِي رَمَضَانَ.",
            "en": "I travelled to Madinah, then Makkah, in Ramadan.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PREP, OWNER, AND]},
                {"key": "sign", "label": "Sign", "options": [KAS, FAT]},
            ],
            "rows": [
                {"s": "المَدِينَةِ", "gloss": "Madinah", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {إِلَى}. It has {ال}: kasra."},
                {"s": "مَكَّةَ", "gloss": "Makkah", "ans": {"job": "and", "sign": "fat"},
                 "why": "After {ثُمَّ}, it copies the jarr of {المَدِينَةِ}. A diptote name: fatha in place of kasra."},
                {"s": "رَمَضَانَ", "gloss": "Ramadan", "ans": {"job": "prep", "sign": "fat"},
                 "why": "After {فِي}. A name ending in {ـَانُ}: fatha in place of kasra."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "سَلَّمْتُ عَلَى القَاضِي العَادِلِ وَأَبِيكَ الكَرِيمِ.",
            "en": "I greeted the just judge and your generous father.",
            "fields": [
                {"key": "job", "label": "Job", "options": [PREP, ADJ, AND]},
                {"key": "sign", "label": "Sign", "options": [KAS, YA, HID]},
            ],
            "rows": [
                {"s": "القَاضِي", "gloss": "the judge", "ans": {"job": "prep", "sign": "hid"},
                 "why": "After {عَلَى}. It ends in {ي}: hidden kasra."},
                {"s": "العَادِلِ", "gloss": "just", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {القَاضِي}: jarr. A singular: kasra you can see."},
                {"s": "أَبِيكَ", "gloss": "your father", "ans": {"job": "and", "sign": "ya"},
                 "why": "After {وَ}, jarr. One of the five nouns: yāʾ."},
                {"s": "الكَرِيمِ", "gloss": "generous", "ans": {"job": "adj", "sign": "kas"},
                 "why": "It describes {أَبِيكَ}: jarr with kasra."},
            ],
        },
        {
            "title": "Which sign does the follower in [brackets] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [KAS, FAT, YA]}],
            "rows": [
                {"s": "سَمِعْتُ الخَبَرَ مِنْ أَصْدِقَاءَ [كَثِيرِينَ]", "gloss": "I heard the news from many friends.", "ans": {"sign": "ya"},
                 "why": "A sound masculine plural adjective in jarr: yāʾ."},
                {"s": "نَظَرْتُ إِلَى الكُتُبِ [كُلِّهَا]", "gloss": "I looked at all the books.", "ans": {"sign": "kas"},
                 "why": "Emphasis in jarr: kasra."},
                {"s": "قَرَأْتُ عَنِ الخَلِيفَةِ [عُثْمَانَ]", "gloss": "I read about the caliph Uthman.", "ans": {"sign": "fat"},
                 "why": "A substitute in jarr. A name ending in {ـَانُ}: fatha in place of kasra."},
                {"s": "سَلَّمْتُ عَلَى الأَطِبَّاءِ [أَنْفُسِهِمْ]", "gloss": "I greeted the doctors themselves.", "ans": {"sign": "kas"},
                 "why": "Emphasis in jarr. {أَنْفُسٌ} is a broken plural: kasra."},
                {"s": "مَرَرْتُ بِالطَّالِبَاتِ [المُسْلِمَاتِ]", "gloss": "I passed by the Muslim female students.", "ans": {"sign": "kas"},
                 "why": "A sound feminine plural adjective in jarr: kasra."},
                {"s": "سَأَلْتُ عَنِ الرَّجُلَيْنِ [الصَّالِحَيْنِ]", "gloss": "I asked about the two righteous men.", "ans": {"sign": "ya"},
                 "why": "A dual adjective in jarr: yāʾ."},
            ],
        },
        {
            "title": "Which word does the adjective in [brackets] follow?",
            "fields": [{"key": "pick", "label": "It follows", "options": []}],
            "rows": [
                {"s": "دَخَلْتُ بَيْتَ المُدِيرِ [الجَدِيدِ]", "gloss": "I entered the new headmaster's house.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("بَيْتَ", "المُدِيرِ")},
                 "why": "Kasra, like {المُدِيرِ}, the owner in jarr."},
                {"s": "دَخَلْتُ بَيْتَ المُدِيرِ [الجَدِيدَ]", "gloss": "I entered the headmaster's new house.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بَيْتَ", "المُدِيرِ")},
                 "why": "Fatha, like {بَيْتَ}, the object in naṣb."},
                {"s": "هَذِهِ سَيَّارَةُ المُدَرِّسَةِ [الجَدِيدَةُ]", "gloss": "This is the teacher's new car.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("سَيَّارَةُ", "المُدَرِّسَةِ")},
                 "why": "Damma, like {سَيَّارَةُ}, the information in rafʿ."},
                {"s": "هَذِهِ سَيَّارَةُ المُدَرِّسَةِ [الجَدِيدَةِ]", "gloss": "This is the new teacher's car.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("سَيَّارَةُ", "المُدَرِّسَةِ")},
                 "why": "Kasra, like {المُدَرِّسَةِ}, the owner in jarr."},
                {"s": "سَأَلْتُ عَنْ مُعَلِّمِ البِنْتِ [الصَّغِيرَةِ]", "gloss": "I asked about the little girl's teacher.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُعَلِّمِ", "البِنْتِ")},
                 "why": "Both are in jarr. {الصَّغِيرَةِ} is feminine, like {البِنْتِ}. For the teacher it would be {الصَّغِيرِ}."},
            ],
        },
    ],
}
