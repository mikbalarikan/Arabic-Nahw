# Stage 7, Unit 8: The one called (المُنَادَى)

# Canonical options (copied from STAGES_5_8_SPEC.md)
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
KAS = {"k": "kas", "label": "Kasra · كَسْرَةٌ", "color": "green"}
ALIF = {"k": "alif", "label": "Alif · الأَلِفُ", "color": "teal"}
YA = {"k": "ya", "label": "Yāʾ · اليَاءُ", "color": "purple"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}

VERB = {"k": "verb", "label": "Verb · فِعْلٌ", "color": "navy"}
DOER = {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
OBJ = {"k": "obj", "label": "Object · مَفْعُولٌ بِهِ", "color": "pink"}
MUTL = {"k": "mutl", "label": "Verb's own noun · مَفْعُولٌ مُطْلَقٌ", "color": "purple"}
STATE = {"k": "state", "label": "State · حَالٌ", "color": "olive"}
VOC = {"k": "voc", "label": "Called · مُنَادًى", "color": "green"}
PART = {"k": "part", "label": "Particle · حَرْفٌ", "color": "grey"}

# The three kinds of munādā in this unit (the first one has two sub-kinds)
NAME = {"k": "name", "label": "A name · عَلَمٌ", "color": "gold"}
FACE = {"k": "face", "label": "The one I face · نَكِرَةٌ مَقْصُودَةٌ", "color": "teal"}
OWN = {"k": "own", "label": "Owned · مُضَافٌ", "color": "purple"}
ANY = {"k": "any", "label": "Anyone at all · نَكِرَةٌ غَيْرُ مَقْصُودَةٍ", "color": "brown"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s7-vocative",
    "order": 8,
    "title": "The one called",
    "ar": "المُنَادَى",
    "blurb": "After يَا: a name or the one you face is fixed in the place of naṣb. An owned word, or anyone at all, shows naṣb.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 7 · UNIT 8", "title": "Calling someone",
         "text": "When you call a person with {يَا}, the word you call is the one called ({المُنَادَى}). Its place is naṣb.",
         "wm": "المُنَادَى"},

        {"t": "h2", "text": "يَا and the one called"},
        {"t": "p", "text": "{يَا} is a particle of calling. It is fixed. It stands for \"I call\", so the one called is like an object: its place is naṣb."},
        {"t": "p", "text": "But the one called does not always show a fatha. It depends on its type. There are three types."},
        {"t": "cols", "items": [
            {"color": "gold", "title": "1. A name, or the one you face", "ar": "يَا زَيْدُ، يَا رَجُلُ", "text": "Fixed on damma, in the place of naṣb."},
            {"color": "purple", "title": "2. Owned", "ar": "يَا عَبْدَ اللّٰهِ", "text": "Naṣb. The sign shows."},
            {"color": "brown", "title": "3. Anyone at all", "ar": "يَا غَافِلًا", "text": "Naṣb with tanween."},
        ]},

        {"t": "h2", "text": "Type 1: a name or the one you face"},
        {"t": "rule", "color": "gold", "title": "Fixed on damma, in the place of naṣb",
         "text": "A single name, or a common noun for the one person you are talking to, takes one damma. No tanween. This damma is fixed. The word is in the place of naṣb."},
        {"t": "examples", "items": [
            {"ar": "يَا زَيْدُ، اِجْلِسْ.", "en": "Zayd, sit down.", "note": "A name: {زَيْدُ} with one damma."},
            {"ar": "يَا فَاطِمَةُ، اُدْخُلِي.", "en": "Fāṭima, come in.", "note": "A name: fixed on damma."},
            {"ar": "يَا رَجُلُ، اِسْمَعْ.", "en": "(You,) man, listen.", "note": "One man in front of you. He becomes definite by being called: fixed on damma."},
            {"ar": "يَا نُوحُ اهْبِطْ بِسَلَامٍ", "en": "O Nūḥ, go down in peace. (Hūd 11:48)", "note": "A name: {نُوحُ} is fixed on damma."},
        ]},
        {"t": "p", "text": "A dual or a sound masculine plural of this type is fixed on its rafʿ letter."},
        {"t": "table", "head": ["Group", "Example", "Fixed on"], "rows": [
            ["Singular", "يَا زَيْدُ / يَا رَجُلُ", "damma"],
            ["Broken plural", "يَا طُلَّابُ", "damma"],
            ["Sound f. plural", "يَا مُسْلِمَاتُ", "damma"],
            ["Dual", "يَا مُحَمَّدَانِ", "alif"],
            ["Sound m. plural", "يَا مُسْلِمُونَ", "wāw"],
        ]},
        {"t": "tip", "text": "Type 1 is fixed. So its last letter does not change with a sign of naṣb. Do not write {يَا زَيْدًا} or {يَا مُسْلِمِينَ} when you call Zayd or the Muslims in front of you."},

        {"t": "h2", "text": "Type 2: owned, so naṣb"},
        {"t": "rule", "color": "purple", "title": "Owned = naṣb",
         "text": "When the one called has an owner after it, it is in naṣb. Each group shows its own sign of naṣb. The owner is in jarr."},
        {"t": "table", "head": ["Group", "Example", "Sign of naṣb"], "rows": [
            ["Singular", "يَا عَبْدَ اللّٰهِ", "fatha"],
            ["Singular", "يَا طَالِبَ العِلْمِ", "fatha"],
            ["Broken plural", "يَا أَهْلَ القَرْيَةِ", "fatha"],
            ["Five nouns", "يَا أَبَانَا", "alif"],
            ["Sound m. plural", "يَا مُعَلِّمِي المَدْرَسَةِ", "yāʾ (the {ن} drops)"],
            ["Sound f. plural", "يَا طَالِبَاتِ المَدْرَسَةِ", "kasra in place of fatha"],
        ]},
        {"t": "tip", "text": "{يَا مُعَلِّمِي المَدْرَسَةِ} means \"O teachers of the school\". The {ي} is the sign of naṣb of the plural. It is not \"my\"."},

        {"t": "h2", "text": "Type 3: anyone at all, so naṣb"},
        {"t": "rule", "color": "brown", "title": "Not one person = naṣb with tanween",
         "text": "Sometimes you call out to anyone who hears, not to one person. Then the word stays indefinite. It is in naṣb with fatha and tanween."},
        {"t": "examples", "items": [
            {"ar": "يَا غَافِلًا، اِسْتَيْقِظْ.", "en": "O heedless one (whoever you are), wake up."},
            {"ar": "يَا رَجُلًا، خُذْ بِيَدِي.", "en": "O some man, take my hand.", "note": "A blind man calls out. He does not know who will hear."},
        ]},
        {"t": "tip", "text": "Compare {يَا رَجُلُ} and {يَا رَجُلًا}. With damma you call one man you face. With tanween you call any man at all."},

        {"t": "h2", "text": "Full iʿrāb"},
        {"t": "examples", "items": [
            {"ar": "يَا: حَرْفُ نِدَاءٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "en": "yā: a particle of calling, fixed on sukūn."},
            {"ar": "زَيْدُ: مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "en": "Zaydu: called, fixed on damma, in the place of naṣb."},
            {"ar": "مُسْلِمُونَ: مُنَادًى مَبْنِيٌّ عَلَى الوَاوِ فِي مَحَلِّ نَصْبٍ.", "en": "muslimūna: called, fixed on the wāw, in the place of naṣb."},
            {"ar": "مُحَمَّدَانِ: مُنَادًى مَبْنِيٌّ عَلَى الأَلِفِ فِي مَحَلِّ نَصْبٍ.", "en": "Muḥammadāni: called, fixed on the alif, in the place of naṣb."},
            {"ar": "عَبْدَ: مُنَادًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ، وَهُوَ مُضَافٌ.", "en": "ʿabda: called, in naṣb, its sign is the fatha. It is owned.",
             "note": "From {يَا عَبْدَ اللّٰهِ}. {اللّٰهِ} is the owner, in jarr."},
            {"ar": "أَبَا: مُنَادًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الأَلِفُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ.", "en": "abā: called, in naṣb, its sign is the alif because it is one of the five nouns.",
             "note": "From {يَا أَبَانَا}. {نَا} is a fixed pronoun, in the place of jarr as owner."},
            {"ar": "غَافِلًا: مُنَادًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ.", "en": "ghāfilan: called, in naṣb, its sign is the fatha."},
        ]},

        {"t": "summary", "title": "In short", "items": [
            "{يَا} is a fixed particle. The one called is in the place of naṣb.",
            "A name or the one you face: fixed on damma, in the place of naṣb: {يَا زَيْدُ}، {يَا رَجُلُ}.",
            "Its dual is fixed on alif ({يَا مُحَمَّدَانِ}). Its sound m. plural is fixed on wāw ({يَا مُسْلِمُونَ}).",
            "Owned: naṣb with its own sign: {يَا عَبْدَ اللّٰهِ}، {يَا أَبَانَا}، {يَا مُعَلِّمِي المَدْرَسَةِ}.",
            "Anyone at all: naṣb with tanween: {يَا غَافِلًا}.",
        ]},
    ],

    "practice": [
        {
            "title": "Which type, which sign?",
            "fields": [
                {"key": "type", "label": "Type", "options": [NAME, FACE, OWN, ANY]},
                {"key": "sign", "label": "Sign", "options": [FAT, ALIF, YA, FIXED]},
            ],
            "rows": [
                {"s": "يَا زَيْدُ", "gloss": "Zayd!", "ans": {"type": "name", "sign": "fixed"},
                 "why": "A name: fixed on damma, in the place of naṣb."},
                {"s": "يَا عَبْدَ اللّٰهِ", "gloss": "ʿAbdullāh!", "ans": {"type": "own", "sign": "fat"},
                 "why": "{عَبْدَ} has an owner, {اللّٰهِ}. Owned: naṣb with fatha."},
                {"s": "يَا غَافِلًا", "gloss": "O heedless one, whoever you are", "ans": {"type": "any", "sign": "fat"},
                 "why": "No one person is meant. Naṣb with fatha and tanween."},
                {"s": "يَا رَجُلُ", "gloss": "(You,) man!", "ans": {"type": "face", "sign": "fixed"},
                 "why": "The man you are talking to. Fixed on damma, in the place of naṣb."},
                {"s": "يَا أَبَانَا", "gloss": "O our father!", "ans": {"type": "own", "sign": "alif"},
                 "why": "Owned by {نَا}. A five noun in naṣb takes alif."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "يَا ___، اِجْلِسْ.", "gloss": "ʿAlī, sit down.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("عَلِيُّ", "عَلِيًّا", "عَلِيٌّ")},
                 "why": "A name: one damma, no tanween. Fixed on damma, in the place of naṣb."},
                {"s": "يَا ___ البَيْتِ", "gloss": "O owner of the house!", "ans": {"pick": "b"},
                 "opts": {"pick": pick("صَاحِبُ", "صَاحِبَ", "صَاحِبِ")},
                 "why": "It has an owner, {البَيْتِ}. Owned: naṣb with fatha."},
                {"s": "يَا ___", "gloss": "O Muslims! (the people in front of you)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُسْلِمُونَ", "مُسْلِمِينَ")},
                 "why": "Specific people you face: fixed on the wāw, in the place of naṣb."},
                {"s": "يَا ___ المَدِينَةِ", "gloss": "O people of the city!", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَهْلُ", "أَهْلَ", "أَهْلِ")},
                 "why": "Owned by {المَدِينَةِ}: naṣb with fatha."},
                {"s": "يَا ___", "gloss": "O traveller! (any traveller at all)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُسَافِرُ", "مُسَافِرًا", "مُسَافِرٌ")},
                 "why": "No one person is meant: naṣb with fatha and tanween."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "يَا طَالِبَ العِلْمِ، اُكْتُبِ الدَّرْسَ.",
            "en": "O student of knowledge, write the lesson.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VOC, OWNER, OBJ, PART]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, FIXED]},
            ],
            "rows": [
                {"s": "يَا", "gloss": "O", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A particle of calling, fixed on sukūn."},
                {"s": "طَالِبَ", "gloss": "student (of)", "ans": {"job": "voc", "sign": "fat"},
                 "why": "Called and owned: {مُنَادًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
                {"s": "العِلْمِ", "gloss": "knowledge", "ans": {"job": "owner", "sign": "kas"},
                 "why": "The owner of {طَالِبَ}: jarr with kasra."},
                {"s": "الدَّرْسَ", "gloss": "the lesson", "ans": {"job": "obj", "sign": "fat"},
                 "why": "The object of the order verb {اُكْتُبِ}: naṣb with fatha."},
            ],
        },
        {
            "title": "Which sign does the called word take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, KAS, ALIF, YA, FIXED]}],
            "rows": [
                {"s": "يَا [سَعِيدُ]", "gloss": "O Saʿīd!", "ans": {"sign": "fixed"},
                 "why": "A single name: fixed on damma, in the place of naṣb."},
                {"s": "يَا [أَبَا] بَكْرٍ", "gloss": "O Abū Bakr!", "ans": {"sign": "alif"},
                 "why": "Owned by {بَكْرٍ}. A five noun in naṣb takes alif."},
                {"s": "يَا [طَالِبَاتِ] المَدْرَسَةِ", "gloss": "O students (f.) of the school!", "ans": {"sign": "kas"},
                 "why": "Owned: naṣb. A sound feminine plural takes kasra in place of fatha."},
                {"s": "يَا [مُهَنْدِسُونَ]", "gloss": "O engineers! (in front of you)", "ans": {"sign": "fixed"},
                 "why": "The ones you face: fixed on wāw, in the place of naṣb."},
                {"s": "يَا [نَائِمًا]", "gloss": "O sleeper, whoever you are!", "ans": {"sign": "fat"},
                 "why": "Anyone at all: naṣb with fatha and tanween."},
                {"s": "يَا [رَسُولَ] اللّٰهِ", "gloss": "O Messenger of Allah!", "ans": {"sign": "fat"},
                 "why": "Owned by {اللّٰهِ}: naṣb with fatha."},
            ],
        },
        {
            "title": "Find the job",
            "prompt": "يَا مُعَلِّمُ، شَرَحْتَ الدَّرْسَ شَرْحًا جَمِيلًا.",
            "en": "Teacher, you explained the lesson beautifully.",
            "fields": [{"key": "job", "label": "Job", "options": [VOC, OBJ, MUTL, ADJ, STATE]}],
            "rows": [
                {"s": "مُعَلِّمُ", "gloss": "teacher", "ans": {"job": "voc"},
                 "why": "After {يَا}: the teacher you face. Fixed on damma, in the place of naṣb."},
                {"s": "الدَّرْسَ", "gloss": "the lesson", "ans": {"job": "obj"},
                 "why": "What was explained: object, naṣb."},
                {"s": "شَرْحًا", "gloss": "an explaining", "ans": {"job": "mutl"},
                 "why": "The maṣdar of {شَرَحَ}, the verb's own noun."},
                {"s": "جَمِيلًا", "gloss": "beautiful", "ans": {"job": "adj"},
                 "why": "It describes {شَرْحًا}: the explaining was beautiful. It copies it: indefinite, naṣb, tanween."},
            ],
        },
        {
            "title": "Which type?",
            "fields": [{"key": "type", "label": "Type", "options": [NAME, FACE, OWN, ANY]}],
            "rows": [
                {"s": "يَا خَالِدُ", "gloss": "Khālid!", "ans": {"type": "name"},
                 "why": "{خَالِدٌ} is a name. It is fixed on damma."},
                {"s": "يَا رَجُلًا، خُذْ بِيَدِي.", "gloss": "a blind man calls out", "ans": {"type": "any"},
                 "why": "Tanween: he calls any man who hears."},
                {"s": "يَا بِنْتُ", "gloss": "(You,) girl!", "ans": {"type": "face"},
                 "why": "Not a name. One damma, no tanween: the girl you are talking to."},
                {"s": "يَا صَاحِبَ القَلَمِ", "gloss": "O owner of the pen!", "ans": {"type": "own"},
                 "why": "{القَلَمِ} is its owner. So it is owned, in naṣb."},
                {"s": "يَا جَاهِلًا", "gloss": "O ignorant one, whoever you are!", "ans": {"type": "any"},
                 "why": "Tanween with fatha: no one person is meant."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Which type, which sign?",
            "fields": [
                {"key": "type", "label": "Type", "options": [NAME, FACE, OWN, ANY]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, YA, FIXED]},
            ],
            "rows": [
                {"s": "يَا فَاطِمَةُ", "gloss": "Fāṭima!", "ans": {"type": "name", "sign": "fixed"},
                 "why": "A name: fixed on damma, in the place of naṣb."},
                {"s": "يَا أَهْلَ القَرْيَةِ", "gloss": "O people of the village!", "ans": {"type": "own", "sign": "fat"},
                 "why": "Owned by {القَرْيَةِ}: naṣb with fatha."},
                {"s": "يَا طُلَّابُ", "gloss": "Students! (in front of you)", "ans": {"type": "face", "sign": "fixed"},
                 "why": "The students you face. A broken plural: fixed on damma, in the place of naṣb."},
                {"s": "يَا مُعَلِّمِي المَدْرَسَةِ", "gloss": "O teachers of the school!", "ans": {"type": "own", "sign": "ya"},
                 "why": "Owned: naṣb. A sound masculine plural takes yāʾ, and its {ن} drops before the owner."},
                {"s": "يَا ظَالِمًا", "gloss": "O wrongdoer, whoever you are!", "ans": {"type": "any", "sign": "fat"},
                 "why": "No one person is meant: naṣb with fatha and tanween."},
            ],
        },
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "يَا ___، اِسْمَعْ.", "gloss": "Aḥmad, listen.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَحْمَدُ", "أَحْمَدَ", "أَحْمَدًا")},
                 "why": "A name: fixed on damma, in the place of naṣb."},
                {"s": "يَا ___ المَدِينَةِ", "gloss": "O women of the city!", "ans": {"pick": "b"},
                 "opts": {"pick": pick("نِسَاءُ", "نِسَاءَ", "نِسَاءِ")},
                 "why": "Owned by {المَدِينَةِ}: naṣb. A broken plural takes fatha."},
                {"s": "يَا ___ المَدْرَسَةِ", "gloss": "O female teachers of the school!", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُعَلِّمَاتُ", "مُعَلِّمَاتَ", "مُعَلِّمَاتِ")},
                 "why": "Owned: naṣb. A sound feminine plural takes kasra, never fatha."},
                {"s": "يَا ___", "gloss": "O two engineers! (in front of you)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُهَنْدِسَانِ", "مُهَنْدِسَيْنِ")},
                 "why": "Two people you face: fixed on alif, in the place of naṣb. No change to {ـَيْنِ}."},
                {"s": "يَا ___", "gloss": "O our brother!", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَخُونَا", "أَخَانَا", "أَخِينَا")},
                 "why": "Owned by {نَا}: naṣb. A five noun takes alif."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "يَا مُؤْمِنُونَ، اُذْكُرُوا اللّٰهَ.",
            "en": "Believers, remember Allah.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VOC, VERB, OBJ, PART]},
                {"key": "sign", "label": "Sign", "options": [FAT, YA, FIXED]},
            ],
            "rows": [
                {"s": "يَا", "gloss": "O", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A particle of calling, fixed on sukūn."},
                {"s": "مُؤْمِنُونَ", "gloss": "believers", "ans": {"job": "voc", "sign": "fixed"},
                 "why": "The ones you face: {مُنَادًى مَبْنِيٌّ عَلَى الوَاوِ فِي مَحَلِّ نَصْبٍ}. It does not change to {ـِينَ}."},
                {"s": "اُذْكُرُوا", "gloss": "remember!", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "An order verb. Order verbs are fixed."},
                {"s": "اللّٰهَ", "gloss": "Allah", "ans": {"job": "obj", "sign": "fat"},
                 "why": "The object: naṣb with fatha."},
            ],
        },
        {
            "title": "Which sign does the called word take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, KAS, ALIF, YA, FIXED]}],
            "rows": [
                {"s": "يَا [عَبْدَ] الرَّحْمٰنِ", "gloss": "ʿAbd al-Raḥmān!", "ans": {"sign": "fat"},
                 "why": "Owned by {الرَّحْمٰنِ}: naṣb with fatha."},
                {"s": "يَا [أَخَا] العَرَبِ", "gloss": "O brother of the Arabs!", "ans": {"sign": "alif"},
                 "why": "Owned: naṣb. A five noun takes alif."},
                {"s": "يَا [مُحَمَّدُ]", "gloss": "Muḥammad!", "ans": {"sign": "fixed"},
                 "why": "A name: fixed on damma, in the place of naṣb."},
                {"s": "يَا [مُهَنْدِسِي] الشَّرِكَةِ", "gloss": "O engineers of the company!", "ans": {"sign": "ya"},
                 "why": "Owned: naṣb. A sound masculine plural takes yāʾ. The {ن} drops."},
                {"s": "يَا [زَيْنَبُ]", "gloss": "Zaynab!", "ans": {"sign": "fixed"},
                 "why": "A name: fixed on damma, in the place of naṣb."},
                {"s": "يَا [مُسْلِمَاتُ]", "gloss": "O Muslim women! (in front of you)", "ans": {"sign": "fixed"},
                 "why": "The ones you face: fixed on damma, in the place of naṣb. Kasra would be for an owned one."},
            ],
        },
        {
            "title": "Find the job: review",
            "prompt": "يَا أَبَا زَيْدٍ، رَجَعَ الأَوْلَادُ مَسْرُورِينَ.",
            "en": "Abū Zayd, the children came back happy.",
            "fields": [{"key": "job", "label": "Job", "options": [VOC, OWNER, DOER, ADJ, STATE]}],
            "rows": [
                {"s": "أَبَا", "gloss": "father (of)", "ans": {"job": "voc"},
                 "why": "Called and owned: naṣb with alif, a five noun."},
                {"s": "زَيْدٍ", "gloss": "Zayd", "ans": {"job": "owner"},
                 "why": "The owner of {أَبَا}: jarr with kasra."},
                {"s": "الأَوْلَادُ", "gloss": "the children", "ans": {"job": "doer"},
                 "why": "They came back: doer, rafʿ with damma."},
                {"s": "مَسْرُورِينَ", "gloss": "happy", "ans": {"job": "state"},
                 "why": "Indefinite, and its owner {الأَوْلَادُ} is definite: a state, naṣb with yāʾ. An adjective would copy {ال}."},
            ],
        },
        {
            "title": "Which type?",
            "fields": [{"key": "type", "label": "Type", "options": [NAME, FACE, OWN, ANY]}],
            "rows": [
                {"s": "يَا عُمَرُ", "gloss": "ʿUmar!", "ans": {"type": "name"},
                 "why": "{عُمَرُ} is a name: fixed on damma."},
                {"s": "يَا مُسَافِرُ", "gloss": "(You,) traveller!", "ans": {"type": "face"},
                 "why": "One damma, no tanween: the traveller you are talking to."},
                {"s": "يَا صَاحِبَ السَّيَّارَةِ", "gloss": "O owner of the car!", "ans": {"type": "own"},
                 "why": "{السَّيَّارَةِ} is its owner, so it is owned."},
                {"s": "يَا عَاقِلًا", "gloss": "O wise one, whoever you are!", "ans": {"type": "any"},
                 "why": "Fatha with tanween: anyone at all."},
                {"s": "يَا وَلَدُ", "gloss": "(You,) boy!", "ans": {"type": "face"},
                 "why": "Not a name. One damma: the boy you face."},
            ],
        },
    ],
}
