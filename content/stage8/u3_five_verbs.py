# Stage 8, Unit 3: The five verbs (الأَفْعَالُ الخَمْسَةُ)

DAM = {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
FAT = {"k": "fat",   "label": "Fatha · فَتْحَةٌ",                "color": "pink"}
KAS = {"k": "kas",   "label": "Kasra · كَسْرَةٌ",                "color": "green"}
SUK = {"k": "suk",   "label": "Sukūn · سُكُونٌ",                 "color": "navy"}
WAW = {"k": "waw",   "label": "Wāw · الوَاوُ",                   "color": "blue"}
NUN = {"k": "nun",   "label": "Nūn stays · ثُبُوتُ النُّونِ",        "color": "olive"}
DROP = {"k": "drop",  "label": "Nūn drops · حَذْفُ النُّونِ",         "color": "orange"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ",                  "color": "grey"}

RAF = {"k": "raf",  "label": "Rafʿ · رَفْعٌ",   "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ",  "color": "pink"}
JAZM = {"k": "jazm", "label": "Jazm · جَزْمٌ",  "color": "navy"}

TOPIC = {"k": "topic", "label": "Topic · مُبْتَدَأٌ",                  "color": "gold"}
VERB = {"k": "verb",  "label": "Verb · فِعْلٌ",                       "color": "navy"}
DOER = {"k": "doer",  "label": "Doer · فَاعِلٌ",                      "color": "orange"}
PREP = {"k": "prep",  "label": "After a preposition · اِسْمٌ مَجْرُورٌ",    "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ",               "color": "purple"}
OBJ = {"k": "obj",   "label": "Object · مَفْعُولٌ بِهِ",                "color": "pink"}
PART = {"k": "part",  "label": "Particle · حَرْفٌ",                     "color": "grey"}

FV = {"k": "fv", "label": "One of the five verbs", "color": "olive"}
NOTFV = {"k": "notfv", "label": "Not one of them", "color": "red"}
FIXN = {"k": "fixn", "label": "Fixed: nūn of women", "color": "grey"}
GROUP = [FV, NOTFV, FIXN]

E_DOER = {"k": "edoer", "label": "Doer pronoun · place of rafʿ", "color": "orange"}
E_SIGN = {"k": "esign", "label": "Sign of rafʿ · ثُبُوتُ النُّونِ", "color": "olive"}
E_ROOT = {"k": "eroot", "label": "Letter of the verb itself", "color": "grey"}
ENDING = [E_DOER, E_SIGN, E_ROOT]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s8-five-verbs",
    "order": 3,
    "title": "The five verbs",
    "ar": "الأَفْعَالُ الخَمْسَةُ",
    "blurb": "Present verbs that end in a doer pronoun and a nūn. The nūn stays in rafʿ and drops in naṣb and jazm.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 8 · UNIT 3", "title": "Five verbs with a nūn",
         "text": "Five forms of the present verb end in {ا}، {و} or {ي} and then a {ن}. Their sign is not a vowel. It is the {ن}: it stays, or it drops.",
         "wm": "يَكْتُبُونَ"},

        {"t": "h2", "text": "Which are the five verbs?"},
        {"t": "p", "text": "Grammar books write them with the model verb {فَعَلَ}: {يَفْعَلَانِ}، {تَفْعَلَانِ}، {يَفْعَلُونَ}، {تَفْعَلُونَ}، {تَفْعَلِينَ}."},
        {"t": "table", "head": ["Pattern", "With كَتَبَ", "Who", "Doer pronoun"], "rows": [
            ["يَفْعَلَانِ", "يَكْتُبَانِ", "they two (m)", "{ا} alif of two"],
            ["تَفْعَلَانِ", "تَكْتُبَانِ", "you two / they two (f)", "{ا} alif of two"],
            ["يَفْعَلُونَ", "يَكْتُبُونَ", "they (m)", "{و} wāw of the group"],
            ["تَفْعَلُونَ", "تَكْتُبُونَ", "you (m pl)", "{و} wāw of the group"],
            ["تَفْعَلِينَ", "تَكْتُبِينَ", "you (f)", "{ي} yāʾ of the woman spoken to"],
        ]},
        {"t": "tip", "text": "The nūn has kasra after alif ({يَكْتُبَانِ}) and fatha after wāw and yāʾ ({يَكْتُبُونَ}، {تَكْتُبِينَ})."},

        {"t": "h2", "text": "Two parts at the end"},
        {"t": "p", "text": "Look at {يَكْتُبُونَ}. After the verb come two things: the doer, then the sign."},
        {"t": "cols", "items": [
            {"color": "orange", "title": "The doer", "ar": "و",
             "text": "An attached pronoun. Fixed on sukūn, in the place of rafʿ."},
            {"color": "olive", "title": "The sign", "ar": "ن",
             "text": "Shows rafʿ. It is in the place of the damma."},
        ]},
        {"t": "examples", "items": [
            {"ar": "الطُّلَّابُ يَكْتُبُونَ الدَّرْسَ.", "en": "The students write the lesson.",
             "note": "{يَكْتُبُونَ}: {فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ ثُبُوتُ النُّونِ لِأَنَّهُ مِنَ الأَفْعَالِ الخَمْسَةِ}. The {و}: {ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ}."},
        ]},
        {"t": "tip", "text": "In {الطُّلَّابُ يَكْتُبُونَ}، {الطُّلَّابُ} is the Topic and the {و} is the doer. When the noun comes after the verb, the verb has no {و}: {يَكْتُبُ الطُّلَّابُ}."},

        {"t": "h2", "text": "Rafʿ: the nūn stays"},
        {"t": "rule", "color": "olive", "title": "ثُبُوتُ النُّونِ",
         "text": "With no particle of naṣb or jazm before it, a five verb is in rafʿ. Its sign is that the {ن} stays."},
        {"t": "examples", "items": [
            {"ar": "الوَلَدَانِ يَلْعَبَانِ فِي الحَدِيقَةِ.", "en": "The two boys play in the garden.", "note": "Rafʿ, the nūn stays. The {ا} is the doer."},
            {"ar": "أَنْتِ تَكْتُبِينَ الدَّرْسَ.", "en": "You (f) write the lesson.", "note": "Rafʿ, the nūn stays. The {ي} is the doer."},
            {"ar": "هَلْ تَفْهَمُونَ الدَّرْسَ؟", "en": "Do you (m pl) understand the lesson?", "note": "{هَلْ} changes nothing. Rafʿ, the nūn stays."},
        ]},

        {"t": "h2", "text": "Naṣb and jazm: the nūn drops"},
        {"t": "p", "text": "Here are two particles you will study soon: {لَنْ} \"will not\" puts the verb in naṣb (Unit 4). {لَمْ} \"did not\" puts it in jazm (Unit 5). After both, the {ن} of a five verb drops."},
        {"t": "table", "head": ["Rafʿ: nūn stays", "Naṣb: nūn drops", "Jazm: nūn drops"], "rows": [
            ["يَكْتُبَانِ", "لَنْ يَكْتُبَا", "لَمْ يَكْتُبَا"],
            ["تَكْتُبَانِ", "لَنْ تَكْتُبَا", "لَمْ تَكْتُبَا"],
            ["يَكْتُبُونَ", "لَنْ يَكْتُبُوا", "لَمْ يَكْتُبُوا"],
            ["تَكْتُبُونَ", "لَنْ تَكْتُبُوا", "لَمْ تَكْتُبُوا"],
            ["تَكْتُبِينَ", "لَنْ تَكْتُبِي", "لَمْ تَكْتُبِي"],
        ]},
        {"t": "examples", "items": [
            {"ar": "الطُّلَّابُ لَنْ يَخْرُجُوا.", "en": "The students will not go out.",
             "note": "{فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الأَفْعَالِ الخَمْسَةِ}"},
            {"ar": "الطُّلَّابُ لَمْ يَخْرُجُوا.", "en": "The students did not go out.",
             "note": "{فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الأَفْعَالِ الخَمْسَةِ}"},
        ]},
        {"t": "rule", "color": "orange", "title": "The doer stays",
         "text": "Only the {ن} drops. The {ا}، {و} or {ي} stays, because it is the doer. After the {و} we write a silent alif: {يَكْتُبُوا}. It is only spelling."},

        {"t": "h2", "text": "In the Qur'an"},
        {"t": "examples", "items": [
            {"ar": "لَنْ تَنَالُوا البِرَّ حَتَّى تُنْفِقُوا مِمَّا تُحِبُّونَ", "en": "You will never reach righteousness until you spend from what you love. (Āl ʿImrān 3:92)",
             "note": "{تَنَالُوا} after {لَنْ} and {تُنْفِقُوا} after {حَتَّى}: naṣb, the nūn drops. {تُحِبُّونَ} has no particle: rafʿ, the nūn stays."},
        ]},

        {"t": "h2", "text": "Look-alikes that are not five verbs"},
        {"t": "cols", "items": [
            {"color": "grey", "title": "Nūn of women", "ar": "يَكْتُبْنَ",
             "text": "This {ن} is the doer itself. The verb is fixed on sukūn. The {ن} never drops: {لَنْ يَكْتُبْنَ}، {لَمْ يَكْتُبْنَ}."},
            {"color": "red", "title": "A nūn of the verb", "ar": "يَسْكُنُ",
             "text": "The {ن} is a letter of {سَكَنَ}. There is no doer pronoun before it. A normal damma."},
        ]},
        {"t": "examples", "items": [
            {"ar": "البَنَاتُ لَنْ يَخْرُجْنَ.", "en": "The girls will not go out.",
             "note": "{يَخْرُجْنَ}: {فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ فِي مَحَلِّ نَصْبٍ}. The {ن}: doer, in the place of rafʿ."},
        ]},
        {"t": "tip", "text": "Quick test: is there {ا}، {و} or {ي} right before the {ن}? Then it is a five verb and the {ن} can drop. A sukūn before the {ن} means the nūn of women."},

        {"t": "summary", "title": "In short", "items": [
            "The five verbs: {يَفْعَلَانِ}، {تَفْعَلَانِ}، {يَفْعَلُونَ}، {تَفْعَلُونَ}، {تَفْعَلِينَ}.",
            "The {ا}، {و}، {ي} is the doer, fixed, in the place of rafʿ.",
            "Rafʿ: the nūn stays ({ثُبُوتُ النُّونِ}): {يَكْتُبُونَ}.",
            "Naṣb and jazm: the nūn drops ({حَذْفُ النُّونِ}): {لَنْ يَكْتُبُوا}، {لَمْ يَكْتُبُوا}.",
            "{يَكْتُبْنَ} is not a five verb. It is fixed on sukūn and keeps its {ن}.",
        ]},
    ],

    "practice": [
        {
            "title": "Is it one of the five verbs?",
            "fields": [{"key": "grp", "label": "Group", "options": GROUP}],
            "rows": [
                {"s": "يَكْتُبُونَ", "gloss": "they (m) write", "ans": {"grp": "fv"}, "why": "{و} of the group + {ن}: the pattern {يَفْعَلُونَ}."},
                {"s": "تَجْلِسِينَ", "gloss": "you (f) sit", "ans": {"grp": "fv"}, "why": "{ي} of the woman + {ن}: the pattern {تَفْعَلِينَ}."},
                {"s": "يَكْتُبْنَ", "gloss": "they (f) write", "ans": {"grp": "fixn"}, "why": "Sukūn before the {ن}: the nūn of women. The verb is fixed."},
                {"s": "يَسْكُنُ", "gloss": "he lives", "ans": {"grp": "notfv"}, "why": "The {ن} belongs to {سَكَنَ}. No doer pronoun before it."},
                {"s": "يَذْهَبَانِ", "gloss": "they two go", "ans": {"grp": "fv"}, "why": "{ا} of two + {ن}: the pattern {يَفْعَلَانِ}."},
                {"s": "نَكْتُبُ", "gloss": "we write", "ans": {"grp": "notfv"}, "why": "No ending at all. The sign is a damma."},
            ],
        },
        {
            "title": "What is this letter?",
            "fields": [{"key": "end", "label": "The letter", "options": ENDING}],
            "rows": [
                {"s": "يَكْتُبُونَ → و", "ans": {"end": "edoer"}, "why": "The {و} of the group is the doer, in the place of rafʿ."},
                {"s": "يَكْتُبُونَ → ن", "ans": {"end": "esign"}, "why": "The {ن} after the doer shows rafʿ."},
                {"s": "تَكْتُبِينَ → ي", "ans": {"end": "edoer"}, "why": "The {ي} of the woman spoken to is the doer."},
                {"s": "يَكْتُبْنَ → ن", "ans": {"end": "edoer"}, "why": "The nūn of women is the doer itself, not a sign."},
                {"s": "يَسْكُنُ → ن", "ans": {"end": "eroot"}, "why": "The {ن} is a letter of {سَكَنَ}."},
                {"s": "يَكْتُبَانِ → ا", "ans": {"end": "edoer"}, "why": "The alif of two is the doer."},
            ],
        },
        {
            "title": "Case and sign of the verb",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JAZM]},
                {"key": "sign", "label": "Sign", "options": [DAM, NUN, DROP, FAT, SUK]},
            ],
            "rows": [
                {"s": "هُمْ [يَكْتُبُونَ]", "gloss": "they write", "ans": {"case": "raf", "sign": "nun"}, "why": "No particle: rafʿ. A five verb: the nūn stays."},
                {"s": "لَنْ [يَكْتُبُوا]", "gloss": "they will not write", "ans": {"case": "nasb", "sign": "drop"}, "why": "After {لَنْ}: naṣb. The nūn drops."},
                {"s": "لَمْ [يَكْتُبُوا]", "gloss": "they did not write", "ans": {"case": "jazm", "sign": "drop"}, "why": "After {لَمْ}: jazm. The nūn drops."},
                {"s": "أَنْتِ [تَجْلِسِينَ]", "gloss": "you (f) sit", "ans": {"case": "raf", "sign": "nun"}, "why": "No particle: rafʿ, the nūn stays."},
                {"s": "لَنْ [تَذْهَبَا]", "gloss": "you two will not go", "ans": {"case": "nasb", "sign": "drop"}, "why": "After {لَنْ}: naṣb. {تَذْهَبَانِ} loses its nūn."},
                {"s": "لَمْ [تَخْرُجِي]", "gloss": "you (f) did not go out", "ans": {"case": "jazm", "sign": "drop"}, "why": "After {لَمْ}: jazm. {تَخْرُجِينَ} loses its nūn."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "الطُّلَّابُ ___ إِلَى المَدْرَسَةِ.", "gloss": "The students go to the school.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَذْهَبُونَ", "يَذْهَبُوا", "يَذْهَبُونِ")}, "why": "No particle: rafʿ, the nūn stays, with fatha."},
                {"s": "الطُّلَّابُ لَنْ ___ اليَوْمَ.", "gloss": "The students will not go out today.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَخْرُجُونَ", "يَخْرُجُوا", "يَخْرُجَ")}, "why": "After {لَنْ}: naṣb, the nūn drops. The {و} stays."},
                {"s": "أَنْتِ ___ الدَّرْسَ.", "gloss": "You (f) write the lesson.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَكْتُبِي", "تَكْتُبِينَ", "تَكْتُبْنَ")}, "why": "No particle: rafʿ, the nūn stays."},
                {"s": "هُمَا لَمْ ___ اللَّبَنَ.", "gloss": "They two did not drink the milk.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَشْرَبَانِ", "يَشْرَبُ", "يَشْرَبَا")}, "why": "After {لَمْ}: jazm, the nūn drops."},
                {"s": "البَنَاتُ لَنْ ___.", "gloss": "The girls will not go out.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَخْرُجْنَ", "يَخْرُجْ", "يَخْرُجَا")}, "why": "The nūn of women is the doer. It never drops: {لَنْ يَخْرُجْنَ}."},
                {"s": "أَنْتُمْ ___ النَّحْوَ.", "gloss": "You (m pl) study grammar.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَدْرُسُوا", "يَدْرُسُونَ", "تَدْرُسُونَ")}, "why": "{أَنْتُمْ} takes {ت} + {ـُونَ}. No particle: the nūn stays."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "الطُّلَّابُ يَدْرُسُونَ النَّحْوَ فِي الفَصْلِ.",
            "en": "The students study grammar in the classroom.",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, VERB, OBJ, PREP]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, NUN, DROP]},
            ],
            "rows": [
                {"s": "الطُّلَّابُ", "ans": {"job": "topic", "sign": "dam"}, "why": "It comes first: Topic, rafʿ, damma. A broken plural."},
                {"s": "يَدْرُسُونَ", "ans": {"job": "verb", "sign": "nun"}, "why": "A five verb with no particle: rafʿ, the nūn stays. Its {و} is the doer."},
                {"s": "النَّحْوَ", "ans": {"job": "obj", "sign": "fat"}, "why": "What they study: object, fatha."},
                {"s": "الفَصْلِ", "ans": {"job": "prep", "sign": "kas"}, "why": "After {فِي}: jarr, kasra."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "أَنْتُمَا لَنْ تَخْرُجَا مِنَ البَيْتِ.",
            "en": "You two will not go out of the house.",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, PART, VERB, PREP]},
                {"key": "sign", "label": "Sign", "options": [FIXED, NUN, DROP, KAS, FAT]},
            ],
            "rows": [
                {"s": "أَنْتُمَا", "ans": {"job": "topic", "sign": "fixed"}, "why": "A fixed pronoun as Topic, in the place of rafʿ."},
                {"s": "لَنْ", "ans": {"job": "part", "sign": "fixed"}, "why": "A particle of naṣb. Every ḥarf is fixed."},
                {"s": "تَخْرُجَا", "ans": {"job": "verb", "sign": "drop"}, "why": "In naṣb after {لَنْ}. A five verb: the nūn drops. The {ا} is the doer."},
                {"s": "البَيْتِ", "ans": {"job": "prep", "sign": "kas"}, "why": "After {مِنَ}: jarr, kasra."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Is it one of the five verbs?",
            "fields": [{"key": "grp", "label": "Group", "options": GROUP}],
            "rows": [
                {"s": "تَشْرَبُونَ", "gloss": "you (m pl) drink", "ans": {"grp": "fv"}, "why": "{و} + {ن}: the pattern {تَفْعَلُونَ}."},
                {"s": "تَشْرَبْنَ", "gloss": "you (f pl) drink", "ans": {"grp": "fixn"}, "why": "Sukūn before the {ن}: the nūn of women. Fixed."},
                {"s": "تَلْعَبِينَ", "gloss": "you (f) play", "ans": {"grp": "fv"}, "why": "{ي} + {ن}: the pattern {تَفْعَلِينَ}."},
                {"s": "يَحْزَنُ", "gloss": "he is sad", "ans": {"grp": "notfv"}, "why": "The {ن} is a letter of {حَزِنَ}. It has a damma."},
                {"s": "يَسْجُدْنَ", "gloss": "they (f) prostrate", "ans": {"grp": "fixn"}, "why": "Sukūn on {د} before the {ن}: the nūn of women."},
                {"s": "يَلْعَبَانِ", "gloss": "they two play", "ans": {"grp": "fv"}, "why": "{ا} + {ن}: the pattern {يَفْعَلَانِ}."},
            ],
        },
        {
            "title": "What is this letter?",
            "fields": [{"key": "end", "label": "The letter", "options": ENDING}],
            "rows": [
                {"s": "تَجْلِسِينَ → ن", "ans": {"end": "esign"}, "why": "After the doer {ي}, the {ن} shows rafʿ."},
                {"s": "يَحْزَنُ → ن", "ans": {"end": "eroot"}, "why": "The {ن} is a letter of {حَزِنَ}."},
                {"s": "تَدْرُسْنَ → ن", "ans": {"end": "edoer"}, "why": "Sukūn before it: the nūn of women, the doer."},
                {"s": "يَخْرُجَانِ → ن", "ans": {"end": "esign"}, "why": "After the doer {ا}, the {ن} shows rafʿ."},
                {"s": "تَذْهَبُونَ → و", "ans": {"end": "edoer"}, "why": "The {و} of the group is the doer."},
                {"s": "تَشْرَبَانِ → ا", "ans": {"end": "edoer"}, "why": "The alif of two is the doer."},
            ],
        },
        {
            "title": "Case and sign of the verb",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JAZM]},
                {"key": "sign", "label": "Sign", "options": [NUN, DROP, FIXED, DAM]},
            ],
            "rows": [
                {"s": "لَنْ [تَكْتُبِي]", "gloss": "you (f) will not write", "ans": {"case": "nasb", "sign": "drop"}, "why": "After {لَنْ}: naṣb, the nūn drops."},
                {"s": "هُمَا [تَلْعَبَانِ]", "gloss": "they two (f) play", "ans": {"case": "raf", "sign": "nun"}, "why": "No particle: rafʿ, the nūn stays."},
                {"s": "لَمْ [يَحْضُرُوا]", "gloss": "they did not come", "ans": {"case": "jazm", "sign": "drop"}, "why": "After {لَمْ}: jazm, the nūn drops."},
                {"s": "لَنْ [يَكْتُبْنَ]", "gloss": "they (f) will not write", "ans": {"case": "nasb", "sign": "fixed"}, "why": "Fixed on sukūn because of the nūn of women. It is in the place of naṣb."},
                {"s": "لَمْ [تَجْلِسْنَ]", "gloss": "you (f pl) did not sit", "ans": {"case": "jazm", "sign": "fixed"}, "why": "Fixed with the nūn of women, in the place of jazm."},
                {"s": "أَنْتُمْ [تَفْهَمُونَ]", "gloss": "you (m pl) understand", "ans": {"case": "raf", "sign": "nun"}, "why": "No particle: rafʿ, the nūn stays."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "المُسْلِمُونَ لَنْ ___ الصَّلَاةَ.", "gloss": "The Muslims will not leave the prayer.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَتْرُكُوا", "يَتْرُكُونَ", "يَتْرُكَ")}, "why": "After {لَنْ}: naṣb, the nūn drops."},
                {"s": "أَنْتِ لَمْ ___ البَابَ.", "gloss": "You (f) did not open the door.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَفْتَحِينَ", "تَفْتَحِي", "تَفْتَحْ")}, "why": "After {لَمْ}: jazm, the nūn drops. The {ي} stays: it is the doer."},
                {"s": "الوَلَدَانِ ___ فِي الحَدِيقَةِ.", "gloss": "The two boys play in the garden.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَلْعَبَا", "يَلْعَبَانِ", "يَلْعَبُونَ")}, "why": "No particle: rafʿ, the nūn stays. Two boys: {ا}."},
                {"s": "المُدَرِّسَاتُ ___ الدَّرْسَ.", "gloss": "The female teachers explain the lesson.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَشْرَحُونَ", "يَشْرَحَا", "يَشْرَحْنَ")}, "why": "A group of women: the nūn of women, {يَشْرَحْنَ}."},
                {"s": "أَنْتُمَا لَنْ ___ الصَّلَاةَ.", "gloss": "You two will not leave the prayer.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَتْرُكَانِ", "تَتْرُكَا", "تَتْرُكُوا")}, "why": "After {لَنْ}: naṣb, the nūn drops. Two people: {ا}."},
                {"s": "هُمْ ___ الحَقَّ.", "gloss": "They know the truth.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَعْرِفُونَ", "يَعْرِفُوا", "يَعْرِفَانِ")}, "why": "No particle: rafʿ, the nūn stays."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "المُسْلِمُونَ لَمْ يَتْرُكُوا الصَّلَاةَ.",
            "en": "The Muslims did not leave the prayer.",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, PART, VERB, OBJ]},
                {"key": "sign", "label": "Sign", "options": [WAW, FIXED, NUN, DROP, FAT]},
            ],
            "rows": [
                {"s": "المُسْلِمُونَ", "ans": {"job": "topic", "sign": "waw"}, "why": "{مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}"},
                {"s": "لَمْ", "ans": {"job": "part", "sign": "fixed"}, "why": "A particle of jazm, fixed."},
                {"s": "يَتْرُكُوا", "ans": {"job": "verb", "sign": "drop"}, "why": "In jazm after {لَمْ}. A five verb: the nūn drops. The {و} is the doer."},
                {"s": "الصَّلَاةَ", "ans": {"job": "obj", "sign": "fat"}, "why": "What they did not leave: object, fatha."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "أَنْتِ تَحْفَظِينَ سُوَرَ القُرْآنِ.",
            "en": "You (f) memorise the sūras of the Qur'an.",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, VERB, OBJ, OWNER]},
                {"key": "sign", "label": "Sign", "options": [FIXED, NUN, DROP, FAT, KAS]},
            ],
            "rows": [
                {"s": "أَنْتِ", "ans": {"job": "topic", "sign": "fixed"}, "why": "A fixed pronoun as Topic, in the place of rafʿ."},
                {"s": "تَحْفَظِينَ", "ans": {"job": "verb", "sign": "nun"}, "why": "No particle: rafʿ. A five verb: the nūn stays. The {ي} is the doer."},
                {"s": "سُوَرَ", "ans": {"job": "obj", "sign": "fat"}, "why": "What you (f) memorise: object, fatha. A broken plural of {سُورَةٌ}."},
                {"s": "القُرْآنِ", "ans": {"job": "owner", "sign": "kas"}, "why": "Owner of {سُوَرَ}: jarr, kasra."},
            ],
        },
    ],
}
