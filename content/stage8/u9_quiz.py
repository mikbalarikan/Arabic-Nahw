# Stage 8, Unit 9: Stage 8 quiz (mixed quiz over units 1-7, with a short course review)

# Canonical options (copied from STAGES_5_8_SPEC.md)
DAM = {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
FAT = {"k": "fat",   "label": "Fatha · فَتْحَةٌ",                "color": "pink"}
KAS = {"k": "kas",   "label": "Kasra · كَسْرَةٌ",                "color": "green"}
SUK = {"k": "suk",   "label": "Sukūn · سُكُونٌ",                 "color": "navy"}
ALIF = {"k": "alif",  "label": "Alif · الأَلِفُ",                  "color": "teal"}
WAW = {"k": "waw",   "label": "Wāw · الوَاوُ",                   "color": "blue"}
YA = {"k": "ya",    "label": "Yāʾ · اليَاءُ",                   "color": "purple"}
HID = {"k": "hid",   "label": "Hidden vowel · مُقَدَّرَةٌ",         "color": "brown"}
DROP = {"k": "drop",  "label": "Nūn drops · حَذْفُ النُّونِ",         "color": "orange"}
WEAK = {"k": "weak",  "label": "Weak letter drops · حَذْفُ حَرْفِ العِلَّةِ", "color": "gold"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ",                  "color": "grey"}

RAF = {"k": "raf",  "label": "Rafʿ · رَفْعٌ",   "color": "red"}
NASB = {"k": "nasb", "label": "Naṣb · نَصْبٌ",  "color": "pink"}
JARR = {"k": "jarr", "label": "Jarr · جَرٌّ",   "color": "green"}
JAZM = {"k": "jazm", "label": "Jazm · جَزْمٌ",  "color": "navy"}

TOPIC = {"k": "topic", "label": "Topic · مُبْتَدَأٌ",                  "color": "gold"}
VERB = {"k": "verb",  "label": "Verb · فِعْلٌ",                       "color": "navy"}
DOER = {"k": "doer",  "label": "Doer · فَاعِلٌ",                      "color": "orange"}
KISM = {"k": "kism",  "label": "Kāna's noun · اِسْمُ كَانَ",             "color": "gold"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ",               "color": "purple"}
ADJ = {"k": "adj",   "label": "Adjective · نَعْتٌ",                   "color": "grey"}
OBJ = {"k": "obj",   "label": "Object · مَفْعُولٌ بِهِ",                "color": "pink"}
PART = {"k": "part",  "label": "Particle · حَرْفٌ",                     "color": "grey"}

# From Unit 3
FV = {"k": "fv", "label": "One of the five verbs", "color": "olive"}
NOTFV = {"k": "notfv", "label": "Not one of them", "color": "red"}
FIXN = {"k": "fixn", "label": "Fixed: nūn of women", "color": "grey"}

# From Unit 6
CW = {"k": "cw", "label": "Condition word · أَدَاةُ الشَّرْطِ", "color": "navy"}
CV = {"k": "cv", "label": "Condition verb · فِعْلُ الشَّرْطِ", "color": "teal"}
AV = {"k": "av", "label": "Answer verb · جَوَابُ الشَّرْطِ", "color": "purple"}
OK = {"k": "ok", "label": "Correct", "color": "green"}
BAD = {"k": "bad", "label": "Has a mistake", "color": "red"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s8-quiz",
    "order": 9,
    "kind": "quiz",
    "title": "Stage 8 quiz",
    "ar": "اخْتِبَارُ الفِعْلِ المُضَارِعِ",
    "blurb": "A mixed quiz on the present verb: its forms, rafʿ, the five verbs, naṣb, jazm, condition and weak endings.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 8 · QUIZ", "title": "Do you know the present verb?",
         "text": "Eight cards, one for every Stage 8 unit and one course review. Do them without your notes.",
         "wm": "الفِعْلُ المُضَارِعُ"},

        {"t": "h2", "text": "How it works"},
        {"t": "p", "text": "For each verb, look at the word before it. That gives the case. Then look at the end of the verb. That gives the sign. For each noun, find the job first."},
        {"t": "tip", "text": "If you miss a card, go back to its unit and read the table again. Then do the homework cards."},

        {"t": "summary", "title": "The seven topics", "items": [
            "1. The present verb starts with {أ ن ي ت}. It is fixed with the nūn of women and the nūn of emphasis.",
            "2. Rafʿ: no particle. Damma, hidden on {و}، {ي} and alif.",
            "3. The five verbs: the nūn stays in rafʿ and drops in naṣb and jazm.",
            "4. Naṣb after {أَنْ}، {لَنْ}، {كَيْ}، {لِـ}، {حَتَّى}، {إِذَنْ}: fatha, hidden on alif.",
            "5. Jazm after {لَمْ}، {لَمَّا}، {لِـ} of order, {لَا} that forbids: sukūn.",
            "6. {إِنْ}، {مَنْ}، {مَا} of condition: two verbs in jazm.",
            "7. Weak endings: in jazm the weak letter drops.",
        ]},
    ],

    "practice": [
        # 1 · unit 1
        {
            "title": "Choose the present form for the pronoun",
            "fields": [{"key": "pick", "label": "Present verb", "options": []}],
            "rows": [
                {"s": "نَحْنُ + سَمِعَ", "gloss": "we hear", "ans": {"pick": "a"},
                 "opts": {"pick": pick("نَسْمَعُ", "أَسْمَعُ", "سَمِعْنَا")}, "why": "{نَحْنُ} takes {ن}: {نَسْمَعُ}. {سَمِعْنَا} is past."},
                {"s": "هِيَ + رَكِبَ", "gloss": "she rides", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَرْكَبُ", "تَرْكَبُ", "تَرْكَبِينَ")}, "why": "{هِيَ} takes {ت}: {تَرْكَبُ}. {تَرْكَبِينَ} is \"you (f)\"."},
                {"s": "أَنْتُمَا + ذَهَبَ", "gloss": "you two go", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَذْهَبُونَ", "يَذْهَبَانِ", "تَذْهَبَانِ")}, "why": "\"You two\": {ت} + {ـَانِ}."},
                {"s": "أَنْتُنَّ + دَخَلَ", "gloss": "you (f pl) enter", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَدْخُلْنَ", "يَدْخُلْنَ", "تَدْخُلِينَ")}, "why": "{أَنْتُنَّ} takes {ت} + {ـْنَ}: {تَدْخُلْنَ}."},
                {"s": "هُمْ + عَرَفَ", "gloss": "they (m) know", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَعْرِفُونَ", "يَعْرِفُونَ", "عَرَفُوا")}, "why": "{هُمْ} takes {ي} + {ـُونَ}: {يَعْرِفُونَ}."},
                {"s": "أَنَا + حَمَلَ", "gloss": "I carry", "ans": {"pick": "c"},
                 "opts": {"pick": pick("نَحْمِلُ", "يَحْمِلُ", "أَحْمِلُ")}, "why": "{أَنَا} takes {أ}: {أَحْمِلُ}."},
            ],
        },
        # 2 · unit 2
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "يَبْنِي العُمَّالُ بَيْتًا كَبِيرًا.",
            "en": "The workers build a big house.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, ADJ]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, HID, SUK]},
            ],
            "rows": [
                {"s": "يَبْنِي", "ans": {"job": "verb", "sign": "hid"},
                 "why": "No particle: rafʿ. Hidden damma on the {ي}, too heavy."},
                {"s": "العُمَّالُ", "ans": {"job": "doer", "sign": "dam"},
                 "why": "The ones who build: doer, rafʿ. A broken plural takes damma."},
                {"s": "بَيْتًا", "ans": {"job": "obj", "sign": "fat"},
                 "why": "What they build: object, fatha."},
                {"s": "كَبِيرًا", "ans": {"job": "adj", "sign": "fat"},
                 "why": "It describes {بَيْتًا} and copies its naṣb: fatha."},
            ],
        },
        # 3 · unit 3
        {
            "title": "The five verbs: which form is right?",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "المُهَنْدِسُونَ ___ فِي المَصْنَعِ.", "gloss": "The engineers work in the factory.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَعْمَلُونَ", "يَعْمَلُوا", "يَعْمَلُ")}, "why": "No particle: rafʿ, the nūn stays. The {و} is the doer."},
                {"s": "أَنْتِ لَنْ ___ الحَقِيبَةَ.", "gloss": "You (f) will not carry the bag.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَحْمِلِينَ", "تَحْمِلِي", "تَحْمِلْنَ")}, "why": "After {لَنْ}: naṣb. The nūn drops, the {ي} stays."},
                {"s": "الأُخْتَانِ ___ الثِّيَابَ.", "gloss": "The two sisters wash the clothes.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَغْسِلُونَ", "تَغْسِلَا", "تَغْسِلَانِ")}, "why": "Two women: {تَغْسِلَانِ}. No particle: the nūn stays."},
                {"s": "البَنَاتُ لَمْ ___ الدَّرْسَ.", "gloss": "The girls did not understand the lesson.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَفْهَمْنَ", "يَفْهَمُوا", "يَفْهَمْ")}, "why": "A group of women: the nūn of women. It never drops."},
                {"s": "أَنْتُمْ لَمْ ___ البَابَ.", "gloss": "You (m pl) did not close the door.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تُغْلِقُونَ", "تُغْلِقْ", "تُغْلِقُوا")}, "why": "After {لَمْ}: jazm. {تُغْلِقُونَ} loses its nūn."},
            ],
        },
        # 4 · unit 4
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "اِنْتَظَرَ المُسَافِرُونَ حَتَّى يَصِلَ القِطَارُ.",
            "en": "The travellers waited until the train arrived.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, PART, OBJ]},
                {"key": "sign", "label": "Sign", "options": [FIXED, FAT, DAM, WAW, SUK]},
            ],
            "rows": [
                {"s": "اِنْتَظَرَ", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb: fixed on fatha."},
                {"s": "المُسَافِرُونَ", "ans": {"job": "doer", "sign": "waw"},
                 "why": "{فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "حَتَّى", "ans": {"job": "part", "sign": "fixed"},
                 "why": "Before a present verb it is a particle of naṣb, fixed."},
                {"s": "يَصِلَ", "ans": {"job": "verb", "sign": "fat"},
                 "why": "{فِعْلٌ مُضَارِعٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
                {"s": "القِطَارُ", "ans": {"job": "doer", "sign": "dam"},
                 "why": "The one that arrives: doer of {يَصِلَ}, rafʿ, damma."},
            ],
        },
        # 5 · unit 5
        {
            "title": "Which form is right? (jazm and لَا)",
            "fields": [{"key": "pick", "label": "Verb", "options": []}],
            "rows": [
                {"s": "لَمْ ___ زَيْنَبُ الرِّسَالَةَ.", "gloss": "Zaynab did not read the letter.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تَقْرَأُ", "تَقْرَأْ", "تَقْرَأَ")}, "why": "After {لَمْ}: jazm, sukūn on the hamza."},
                {"s": "لَا ___ عَلَى أَخِيكَ.", "gloss": "Don't get angry with your brother.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَغْضَبْ", "تَغْضَبُ", "تَغْضَبَ")}, "why": "\"Don't\": {لَا} forbids, so jazm with sukūn."},
                {"s": "الطُّلَّابُ لَمَّا ___ الكِتَابَ.", "gloss": "The students have not opened the book yet.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَفْتَحُونَ", "يَفْتَحُوا", "يَفْتَحَ")}, "why": "After {لَمَّا}: jazm. A five verb: the nūn drops."},
                {"s": "___ عَلِيٌّ مَعَنَا.", "gloss": "Let ʿAlī sit with us.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("لِيَجْلِسْ", "لِيَجْلِسُ", "لِيَجْلِسَ")}, "why": "\"Let him\": the {لِـ} of order gives jazm with sukūn."},
                {"s": "يَا بَنَاتُ، لَا ___ مِنَ الفَصْلِ.", "gloss": "Girls, don't go out of the classroom.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تَخْرُجْنَ", "تَخْرُجُوا", "تَخْرُجِي")}, "why": "To a group of women: {تَخْرُجْنَ}, fixed. It keeps its {ن}."},
                {"s": "أَنْتَ لَا ___ الحَقَّ.", "gloss": "You do not hide the truth.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("تَكْتُمْ", "تَكْتُمَ", "تَكْتُمُ")}, "why": "A fact. This {لَا} only negates: rafʿ with damma."},
            ],
        },
        # 6 · unit 6
        {
            "title": "Part and sign",
            "prompt": "مَنْ يَعْمَلْ خَيْرًا يَجِدْهُ.",
            "en": "Whoever does good finds it.",
            "fields": [
                {"key": "role", "label": "Part", "options": [CW, CV, AV, OBJ]},
                {"key": "sign", "label": "Sign", "options": [FIXED, SUK, FAT, DAM]},
            ],
            "rows": [
                {"s": "مَنْ", "ans": {"role": "cw", "sign": "fixed"},
                 "why": "{مَنْ} \"whoever\": a condition word, fixed on sukūn."},
                {"s": "يَعْمَلْ", "ans": {"role": "cv", "sign": "suk"},
                 "why": "The first verb: the condition verb, jazm with sukūn."},
                {"s": "خَيْرًا", "ans": {"role": "obj", "sign": "fat"},
                 "why": "What he does: object, fatha."},
                {"s": "يَجِدْهُ", "ans": {"role": "av", "sign": "suk"},
                 "why": "The second verb: the answer verb, jazm with sukūn. Then the pronoun {هُ}."},
            ],
        },
        # 7 · unit 7
        {
            "title": "Weak endings: fill the table",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "يَهْدِي → لَمْ ___", "gloss": "he guides → he did not guide", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَهْدِ", "يَهْدِي", "يَهْدِيَ")}, "why": "Jazm: the {ي} drops. The kasra stays."},
                {"s": "يَنْجُو → لَنْ ___", "gloss": "he is saved → he will not be saved", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَنْجُو", "يَنْجُوَ", "يَنْجُ")}, "why": "Naṣb: the fatha shows on the {و}."},
                {"s": "يَلْقَى → لَمْ ___", "gloss": "he meets → he did not meet", "ans": {"pick": "c"},
                 "opts": {"pick": pick("يَلْقَى", "يَلْقِ", "يَلْقَ")}, "why": "Jazm: the alif drops. The fatha before it stays."},
                {"s": "يَحْكِي → لَنْ ___", "gloss": "he tells → he will not tell", "ans": {"pick": "b"},
                 "opts": {"pick": pick("يَحْكِي", "يَحْكِيَ", "يَحْكِ")}, "why": "Naṣb: the fatha shows on the {ي}."},
                {"s": "يَتْلُو → لَمْ ___", "gloss": "he recites → he did not recite", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَتْلُ", "يَتْلُو", "يَتْلُوَ")}, "why": "Jazm: the {و} drops. The damma stays."},
                {"s": "يَنْهَى → لَنْ ___", "gloss": "he forbids → he will not forbid", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَنْهَى", "يَنْهَ")}, "why": "Naṣb on an alif: hidden fatha, the alif stays."},
            ],
        },
        # 8 · course review
        {
            "title": "Course review: iʿrāb of the whole sentence",
            "prompt": "كَانَ أَبُو خَالِدٍ يُسَاعِدُ الفُقَرَاءَ.",
            "en": "Abū Khālid used to help the poor.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, KISM, OWNER, VERB, OBJ]},
                {"key": "sign", "label": "Sign", "options": [WAW, ALIF, KAS, DAM, FAT]},
            ],
            "rows": [
                {"s": "أَبُو", "ans": {"job": "kism", "sign": "waw"},
                 "why": "Kāna's noun, rafʿ. One of the five nouns with an owner: sign wāw."},
                {"s": "خَالِدٍ", "ans": {"job": "owner", "sign": "kas"},
                 "why": "Owner of {أَبُو}: jarr, kasra."},
                {"s": "يُسَاعِدُ", "ans": {"job": "verb", "sign": "dam"},
                 "why": "{كَانَ} is not a particle of naṣb or jazm: rafʿ, damma. The verb sentence is kāna's information."},
                {"s": "الفُقَرَاءَ", "ans": {"job": "obj", "sign": "fat"},
                 "why": "Who he helps: object, naṣb, fatha."},
            ],
        },
    ],

    "homework": [
        # 1 · units 1 and 3
        {
            "title": "Is it one of the five verbs?",
            "fields": [{"key": "grp", "label": "Group", "options": [FV, NOTFV, FIXN]}],
            "rows": [
                {"s": "تَرْكَبَانِ", "gloss": "you two ride", "ans": {"grp": "fv"}, "why": "{ا} of two + {ن}: the pattern {تَفْعَلَانِ}."},
                {"s": "تَرْكَبْنَ", "gloss": "you (f pl) ride", "ans": {"grp": "fixn"}, "why": "Sukūn before the {ن}: the nūn of women. Fixed."},
                {"s": "يَرْكَبُ", "gloss": "he rides", "ans": {"grp": "notfv"}, "why": "No ending at all. The sign is a damma."},
                {"s": "يَشْكُرُونَ", "gloss": "they thank", "ans": {"grp": "fv"}, "why": "{و} of the group + {ن}: the pattern {يَفْعَلُونَ}."},
                {"s": "يَسْمَعْنَ", "gloss": "they (f) hear", "ans": {"grp": "fixn"}, "why": "Sukūn on {ع} before the {ن}: the nūn of women."},
                {"s": "يَزِنُ", "gloss": "he weighs", "ans": {"grp": "notfv"}, "why": "The {ن} is a root letter of {وَزَنَ}. It is not the nūn of the five verbs."},
            ],
        },
        # 2 · unit 2, with hidden vowels in nouns
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "الفَتَى يَرْعَى غَنَمَ أَبِيهِ.",
            "en": "The young man looks after his father's sheep.",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, VERB, DOER, OBJ, OWNER]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, HID, YA]},
            ],
            "rows": [
                {"s": "الفَتَى", "ans": {"job": "topic", "sign": "hid"},
                 "why": "It comes before the verb: Topic, rafʿ. A maqṣūr noun: hidden damma on the alif."},
                {"s": "يَرْعَى", "ans": {"job": "verb", "sign": "hid"},
                 "why": "No particle: rafʿ. Hidden damma on the alif. Its doer is hidden: {هُوَ}."},
                {"s": "غَنَمَ", "ans": {"job": "obj", "sign": "fat"},
                 "why": "What he looks after: object, fatha."},
                {"s": "أَبِيهِ", "ans": {"job": "owner", "sign": "ya"},
                 "why": "Owner of {غَنَمَ}: jarr. One of the five nouns with an owner: sign yāʾ."},
            ],
        },
        # 3 · unit 4
        {
            "title": "Which sign does the verb take here?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, HID, DROP, FIXED]}],
            "rows": [
                {"s": "لَنْ [نَشْكُوَ] أَحَدًا", "gloss": "we will not complain about anyone", "ans": {"sign": "fat"},
                 "why": "After {لَنْ}: naṣb. The fatha shows on the {و}."},
                {"s": "اُدْرُسِي كَيْ [تَنْجَحِي]", "gloss": "study (f) so that you succeed", "ans": {"sign": "drop"},
                 "why": "After {كَيْ}: naṣb. {تَنْجَحِينَ} loses its nūn."},
                {"s": "سَأَحْضُرُ مُبَكِّرًا. إِذَنْ [أَنْتَظِرَكَ]", "gloss": "\"I will come early.\" Answer: \"Then I will wait for you.\"", "ans": {"sign": "fat"},
                 "why": "{إِذَنْ} starts the answer: naṣb, fatha. Then the pronoun {كَ}."},
                {"s": "يَجِبُ أَنْ [نَسْعَى] إِلَى الخَيْرِ", "gloss": "we must strive for good", "ans": {"sign": "hid"},
                 "why": "After {أَنْ}: naṣb. The fatha is hidden on the alif."},
                {"s": "البَنَاتُ لَنْ [يَخْرُجْنَ]", "gloss": "the girls will not go out", "ans": {"sign": "fixed"},
                 "why": "The nūn of women: fixed on sukūn, in the place of naṣb."},
                {"s": "خَرَجْنَا لِ[نَمْشِيَ]", "gloss": "we went out in order to walk", "ans": {"sign": "fat"},
                 "why": "After {لِـ} of purpose: naṣb. The fatha shows on the {ي}."},
            ],
        },
        # 4 · units 4-7
        {
            "title": "Correct, or does it have a mistake?",
            "fields": [{"key": "chk", "label": "Sentence", "options": [OK, BAD]}],
            "rows": [
                {"s": "لَمْ يَكْتُبُونَ الدَّرْسَ.", "ans": {"chk": "bad"},
                 "why": "After {لَمْ} the nūn must drop: {لَمْ يَكْتُبُوا الدَّرْسَ}."},
                {"s": "لَا تَلْعَبِي هُنَا.", "ans": {"chk": "ok"},
                 "why": "{لَا} forbids. {تَلْعَبِينَ} lost its nūn: jazm."},
                {"s": "إِنْ تَقْرَأْ تَفْهَمْ.", "ans": {"chk": "ok"},
                 "why": "Both verbs are in jazm with sukūn."},
                {"s": "لَمْ يَدْعُو رَبَّهُ.", "ans": {"chk": "bad"},
                 "why": "In jazm the {و} drops: {لَمْ يَدْعُ رَبَّهُ}."},
                {"s": "مَنْ يَصْبِرُ يَنْجَحُ.", "ans": {"chk": "bad"},
                 "why": "A condition: both verbs must be in jazm. {مَنْ يَصْبِرْ يَنْجَحْ}."},
                {"s": "لَنْ يَمْشِيَ مَعَنَا.", "ans": {"chk": "ok"},
                 "why": "After {لَنْ}: naṣb. The fatha shows on the {ي}."},
            ],
        },
        # 5 · units 6 and 7
        {
            "title": "Iʿrāb: case and sign",
            "prompt": "إِنْ تَدْعُوا رَبَّكُمْ يَسْمَعْ دُعَاءَكُمْ.",
            "en": "If you (all) call on your Lord, He hears your prayer.",
            "fields": [
                {"key": "case", "label": "Case", "options": [RAF, NASB, JARR, JAZM]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, SUK, DROP, WEAK]},
            ],
            "rows": [
                {"s": "تَدْعُوا", "ans": {"case": "jazm", "sign": "drop"},
                 "why": "The condition verb, jazm. {تَدْعُونَ} is a five verb: the nūn drops. The {و} here is the doer, so it stays."},
                {"s": "رَبَّكُمْ", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "Who you call on: object, naṣb, fatha."},
                {"s": "يَسْمَعْ", "ans": {"case": "jazm", "sign": "suk"},
                 "why": "The answer verb, jazm with sukūn."},
                {"s": "دُعَاءَكُمْ", "ans": {"case": "nasb", "sign": "fat"},
                 "why": "What He hears: object, naṣb, fatha."},
            ],
        },
        # 6 · course review
        {
            "title": "Course review: which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "إِنَّ ___ يُحِبُّونَ العِلْمَ.", "gloss": "The Muslims love knowledge.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُسْلِمُونَ", "المُسْلِمِينَ", "المُسْلِمَيْنِ")},
                 "why": "Inna's noun is in naṣb. A sound masculine plural: yāʾ."},
                {"s": "لَنْ يَنْسَى الطُّلَّابُ ___.", "gloss": "The students will not forget your father.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَبُوكَ", "أَبَاكَ", "أَبِيكَ")},
                 "why": "Object, naṣb. One of the five nouns: alif."},
                {"s": "يَجْلِسُ الأَطْفَالُ فِي ___ كَبِيرَةٍ.", "gloss": "The children sit in big gardens.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("حَدَائِقَ", "حَدَائِقٍ", "حَدَائِقِ")},
                 "why": "After {فِي}: jarr. A diptote with no {ال}: fatha, no tanween."},
                {"s": "تَحْتَرِمُ البِنْتُ ___.", "gloss": "The girl respects her (female) teachers.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُعَلِّمَاتِهَا", "مُعَلِّمَاتَهَا", "مُعَلِّمَاتُهَا")},
                 "why": "Object, naṣb. A sound feminine plural takes kasra in naṣb."},
                {"s": "يَحْكُمُ ___ بِالعَدْلِ.", "gloss": "The judge rules with justice.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("القَاضِي", "القَاضِيَ", "القَاضِ")},
                 "why": "Doer, rafʿ. A manqūṣ noun: hidden damma, the {ي} stays."},
                {"s": "يَلْعَبُ الوَلَدُ مَعَ ___.", "gloss": "The boy plays with his two friends.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("صَدِيقَاهُ", "صَدِيقَيْهِ", "صَدِيقَيْنِهِ")},
                 "why": "Owner of {مَعَ}: jarr. A dual: yāʾ, and the nūn drops before {هِ}."},
            ],
        },
    ],
}
