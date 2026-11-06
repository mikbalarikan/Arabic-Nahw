# Stage 7, Unit 11: Stage 7 quiz (mixed quiz over units 1-9)

# Canonical options (STAGES_5_8_SPEC.md), copied exactly.
DAM = {"k": "dam", "label": "Damma · ضَمَّةٌ", "color": "red"}
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
KAS = {"k": "kas", "label": "Kasra · كَسْرَةٌ", "color": "green"}
ALIF = {"k": "alif", "label": "Alif · الأَلِفُ", "color": "teal"}
WAW = {"k": "waw", "label": "Wāw · الوَاوُ", "color": "blue"}
YA = {"k": "ya", "label": "Yāʾ · اليَاءُ", "color": "purple"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}

VERB = {"k": "verb", "label": "Verb · فِعْلٌ", "color": "navy"}
DOER = {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"}
KISM = {"k": "kism", "label": "Kāna's noun · اِسْمُ كَانَ", "color": "gold"}
KKHAB = {"k": "kkhab", "label": "Kāna's information · خَبَرُ كَانَ", "color": "red"}
IISM = {"k": "iism", "label": "Inna's noun · اِسْمُ إِنَّ", "color": "gold"}
IKHAB = {"k": "ikhab", "label": "Inna's information · خَبَرُ إِنَّ", "color": "red"}
PREP = {"k": "prep", "label": "After a preposition · اِسْمٌ مَجْرُورٌ", "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
OBJ = {"k": "obj", "label": "Object · مَفْعُولٌ بِهِ", "color": "pink"}
MUTL = {"k": "mutl", "label": "Verb's own noun · مَفْعُولٌ مُطْلَقٌ", "color": "purple"}
PURP = {"k": "purp", "label": "Purpose · مَفْعُولٌ لِأَجْلِهِ", "color": "teal"}
WHEN = {"k": "when", "label": "Time/place · مَفْعُولٌ فِيهِ", "color": "brown"}
STATE = {"k": "state", "label": "State · حَالٌ", "color": "olive"}
TAMY = {"k": "tamy", "label": "Specifier · تَمْيِيزٌ", "color": "gold"}
EXC = {"k": "exc", "label": "Exception · مُسْتَثْنًى", "color": "red"}
VOC = {"k": "voc", "label": "Called · مُنَادًى", "color": "green"}
PART = {"k": "part", "label": "Particle · حَرْفٌ", "color": "grey"}

# The types of munādā, as in Unit 8.
NAME = {"k": "name", "label": "A name · عَلَمٌ", "color": "gold"}
FACE = {"k": "face", "label": "The one I face · نَكِرَةٌ مَقْصُودَةٌ", "color": "teal"}
OWN = {"k": "own", "label": "Owned · مُضَافٌ", "color": "purple"}
ANY = {"k": "any", "label": "Anyone at all · نَكِرَةٌ غَيْرُ مَقْصُودَةٍ", "color": "brown"}

NASB_SIGNS = [FAT, ALIF, YA, KAS, HID]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s7-quiz",
    "order": 11,
    "kind": "quiz",
    "title": "Stage 7 quiz",
    "ar": "اخْتِبَارُ المَنْصُوبَاتِ",
    "blurb": "A mixed quiz on all nine Stage 7 topics: the signs of naṣb and every job that puts a noun in naṣb.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 7 · QUIZ", "title": "Do you know your naṣb jobs?",
         "text": "Eight cards in class and six for homework. They cover every Stage 7 unit. Do them without your notes.",
         "wm": "المَنْصُوبَاتُ"},

        {"t": "h2", "text": "How it works"},
        {"t": "p", "text": "For each word, find the job first. The job gives the case. The kind of noun gives the sign. Then choose."},
        {"t": "tip", "text": "If you miss a card, go back to its unit and read the table again. Then do the homework cards."},

        {"t": "summary", "title": "The nine topics", "items": [
            "1. Signs of naṣb: fatha, alif (five nouns), yāʾ (dual, sound m. plural), kasra (sound f. plural), hidden fatha (maqṣūr, noun + ـي). The manqūṣ shows its fatha.",
            "2. The object: \"what?\" or \"whom?\". {أَعْطَى} takes two objects. A pronoun object is fixed, in the place of naṣb.",
            "3. The verb's own noun: the maṣdar of the same verb, for emphasis, kind or number.",
            "4. Purpose answers \"why?\". Time and place answer \"when?\", \"how long?\" or \"where?\".",
            "5. Together with: a {وَ} that cannot mean \"and\". The state answers \"how?\" and is indefinite.",
            "6. The specifier answers \"of what?\" or \"in what respect?\". After 11 to 99 it is singular.",
            "7. The exception after {إِلَّا} is naṣb. {غَيْرَ} takes the naṣb, and the word after it is jarr.",
            "8. The one called: a name or the one you face is fixed. Owned or anyone at all: naṣb.",
            "9. Inna's noun and kāna's information are naṣb.",
        ]},
    ],

    "practice": [
        # 1 · unit 1: the signs
        {
            "title": "Which sign of naṣb?",
            "fields": [{"key": "sign", "label": "Sign", "options": NASB_SIGNS}],
            "rows": [
                {"s": "اِحْتَرَمْتُ [العُلَمَاءَ]", "gloss": "I respected the scholars.", "ans": {"sign": "fat"},
                 "why": "Object, naṣb. A broken plural, also a diptote: fatha."},
                {"s": "نَصَحْتُ [الصَّدِيقَيْنِ]", "gloss": "I advised the two friends.", "ans": {"sign": "ya"},
                 "why": "Fatha before the {ي}: a dual. Sign yāʾ."},
                {"s": "دَعَوْتُ [المُهَنْدِسَاتِ]", "gloss": "I invited the female engineers.", "ans": {"sign": "kas"},
                 "why": "A sound f. plural: kasra in place of fatha."},
                {"s": "أَكْرَمْتُ [أَخَا] زَيْنَبَ", "gloss": "I honoured Zaynab's brother.", "ans": {"sign": "alif"},
                 "why": "{أَخٌ} with an owner: a five noun. Sign alif."},
                {"s": "زُرْتُ [القُرَى]", "gloss": "I visited the villages.", "ans": {"sign": "hid"},
                 "why": "{القُرَى} ends in {ـَى}: a maqṣūr. The fatha is hidden on the alif."},
                {"s": "سَمِعْتُ [المُنَادِيَ]", "gloss": "I heard the caller.", "ans": {"sign": "fat"},
                 "why": "A manqūṣ. In naṣb the fatha shows on the {ي}."},
            ],
        },
        # 2 · unit 2: pronoun object
        {
            "title": "Job and sign: a pronoun object",
            "prompt": "أَكْرَمَنَا جِيرَانُكَ.",
            "en": "Your neighbours honoured us.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, OWNER]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, FIXED]},
            ],
            "rows": [
                {"s": "أَكْرَمَ", "gloss": "honoured", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "نَا", "gloss": "us", "ans": {"job": "obj", "sign": "fixed"},
                 "why": "Fatha before {نَا}, and {جِيرَانُ} is the doer. So {نَا} is the object: fixed, in the place of naṣb."},
                {"s": "جِيرَانُ", "gloss": "neighbours", "ans": {"job": "doer", "sign": "dam"},
                 "why": "They did the honouring. Doer, rafʿ. A broken plural of {جَارٌ}: damma."},
                {"s": "ـكَ", "gloss": "your", "ans": {"job": "owner", "sign": "fixed"},
                 "why": "On a noun: the owner. A fixed pronoun, in the place of jarr."},
            ],
        },
        # 3 · unit 3: the verb's own noun
        {
            "title": "Job and sign: the verb's own noun",
            "prompt": "صَفَّقَ الحَاضِرُونَ تَصْفِيقًا حَارًّا.",
            "en": "The audience clapped warmly.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, MUTL, ADJ]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, WAW, FIXED]},
            ],
            "rows": [
                {"s": "صَفَّقَ", "gloss": "clapped", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "الحَاضِرُونَ", "gloss": "those present", "ans": {"job": "doer", "sign": "waw"},
                 "why": "{فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "تَصْفِيقًا", "gloss": "clapping", "ans": {"job": "mutl", "sign": "fat"},
                 "why": "{تَصْفِيقٌ} is the maṣdar of {صَفَّقَ}, the same verb: {مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
                {"s": "حَارًّا", "gloss": "warm", "ans": {"job": "adj", "sign": "fat"},
                 "why": "It describes {تَصْفِيقًا} and copies its naṣb. It tells the kind of clapping."},
            ],
        },
        # 4 · unit 4: purpose and time
        {
            "title": "Why or when? Job and sign",
            "fields": [
                {"key": "job", "label": "Job of the word in [ ]", "options": [OBJ, PURP, WHEN, STATE]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, YA]},
            ],
            "rows": [
                {"s": "عَمِلَ الفَلَّاحُ فِي الحَقْلِ [يَوْمَيْنِ].", "gloss": "The farmer worked in the field for two days.", "ans": {"job": "when", "sign": "ya"},
                 "why": "How long? Two days. Time, naṣb. A dual: yāʾ."},
                {"s": "تَبَرَّعَ الرَّجُلُ [حُبًّا] لِلْخَيْرِ.", "gloss": "The man gave out of love for good.", "ans": {"job": "purp", "sign": "fat"},
                 "why": "Why did he give? Out of love. A maṣdar giving the reason: purpose, fatha."},
                {"s": "نَامَ الوَلَدُ [قَبْلَ] العَشَاءِ.", "gloss": "The boy slept before dinner.", "ans": {"job": "when", "sign": "fat"},
                 "why": "When did he sleep? Before dinner. A time word, owned, fatha with no tanween."},
                {"s": "سَكَتَ الطَّالِبُ [خَجَلًا].", "gloss": "The student kept quiet out of shyness.", "ans": {"job": "purp", "sign": "fat"},
                 "why": "Why was he quiet? Out of shyness. A maṣdar giving the reason: purpose."},
                {"s": "اِنْتَظَرْتُكَ [دَقَائِقَ].", "gloss": "I waited for you for minutes.", "ans": {"job": "when", "sign": "fat"},
                 "why": "How long? Minutes. Time, naṣb. {دَقَائِقُ} is a diptote: fatha, no tanween. The object is {ـكَ}."},
                {"s": "عَمِلَتِ المُمَرِّضَةُ [سَاعَاتٍ].", "gloss": "The nurse worked for hours.", "ans": {"job": "when", "sign": "kas"},
                 "why": "How long? Hours. Time, naṣb. A sound f. plural: kasra in place of fatha."},
            ],
        },
        # 5 · unit 5: the state
        {
            "title": "Job and sign: the state",
            "prompt": "رَجَعَ الصَّيَّادُونَ مِنَ البَحْرِ فَرِحِينَ.",
            "en": "The fishermen came back from the sea happy.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, PREP, STATE, ADJ]},
                {"key": "sign", "label": "Sign", "options": [KAS, WAW, YA, FIXED]},
            ],
            "rows": [
                {"s": "رَجَعَ", "gloss": "came back", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "الصَّيَّادُونَ", "gloss": "the fishermen", "ans": {"job": "doer", "sign": "waw"},
                 "why": "They came back. Doer, rafʿ. Sound m. plural: wāw."},
                {"s": "البَحْرِ", "gloss": "the sea", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {مِنْ}: jarr with kasra."},
                {"s": "فَرِحِينَ", "gloss": "happy", "ans": {"job": "state", "sign": "ya"},
                 "why": "How did they come back? Happy. Indefinite, and its owner {الصَّيَّادُونَ} is definite: {حَالٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
            ],
        },
        # 6 · unit 6: the specifier
        {
            "title": "Specifier or another job?",
            "fields": [
                {"key": "job", "label": "Job of the word in [ ]", "options": [OBJ, OWNER, STATE, TAMY]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, YA]},
            ],
            "rows": [
                {"s": "عِنْدِي خَمْسَةَ عَشَرَ [دِينَارًا].", "gloss": "I have fifteen dinars.", "ans": {"job": "tamy", "sign": "fat"},
                 "why": "Fifteen of what? Dinars. After 11 to 99: a singular specifier in naṣb."},
                {"s": "شَرِبْتُ فِنْجَانًا [قَهْوَةً].", "gloss": "I drank a cup of coffee.", "ans": {"job": "tamy", "sign": "fat"},
                 "why": "A cup of what? Coffee. Specifier after a measure."},
                {"s": "بِعْتُ [صَاعَيْنِ] شَعِيرًا.", "gloss": "I sold two ṣāʿ of barley.", "ans": {"job": "obj", "sign": "ya"},
                 "why": "What did I sell? Two ṣāʿ. The measure is the object. A dual: yāʾ."},
                {"s": "حَسُنَ الطَّالِبُ [أَدَبًا].", "gloss": "The student was good in manners.", "ans": {"job": "tamy", "sign": "fat"},
                 "why": "Good in what respect? In manners. Specifier of the sentence."},
                {"s": "جَلَسَ الشَّيْخُ [مُبْتَسِمًا].", "gloss": "The old man sat smiling.", "ans": {"job": "state", "sign": "fat"},
                 "why": "How did he sit? Smiling. A describing word: state."},
                {"s": "أَكَلْتُ رَغِيفَ [خُبْزٍ].", "gloss": "I ate a loaf of bread.", "ans": {"job": "owner", "sign": "kas"},
                 "why": "{رَغِيفَ} has no tanween: it owns {خُبْزٍ}. Owner, jarr with kasra."},
            ],
        },
        # 7 · unit 7: the exception with غَيْرَ
        {
            "title": "Job and sign with غَيْرَ",
            "prompt": "حَضَرَ الأَعْضَاءُ غَيْرَ عُضْوَيْنِ.",
            "en": "The members attended, other than two members.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, EXC, OWNER]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, YA, FIXED]},
            ],
            "rows": [
                {"s": "حَضَرَ", "gloss": "attended", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "الأَعْضَاءُ", "gloss": "the members", "ans": {"job": "doer", "sign": "dam"},
                 "why": "The group is the doer. A broken plural in rafʿ: damma."},
                {"s": "غَيْرَ", "gloss": "other than", "ans": {"job": "exc", "sign": "fat"},
                 "why": "{غَيْرَ} takes the job of the exception: {مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
                {"s": "عُضْوَيْنِ", "gloss": "two members", "ans": {"job": "owner", "sign": "ya"},
                 "why": "The owner of {غَيْرَ}, in jarr. A dual in jarr: yāʾ."},
            ],
        },
        # 8 · units 8 and 9: the one called, inna's noun
        {
            "title": "Job and sign: يَا and إِنَّ",
            "prompt": "يَا مُدَرِّسِي الفَصْلِ، إِنَّ الطُّلَّابَ مُسْتَعِدُّونَ.",
            "en": "Teachers of the class, the students are ready.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VOC, OWNER, PART, IISM, IKHAB]},
                {"key": "sign", "label": "Sign", "options": [FAT, KAS, WAW, YA, FIXED]},
            ],
            "rows": [
                {"s": "مُدَرِّسِي", "gloss": "teachers (of)", "ans": {"job": "voc", "sign": "ya"},
                 "why": "Called and owned: naṣb. A sound m. plural: yāʾ. The {ن} drops before the owner. It is not \"my\"."},
                {"s": "الفَصْلِ", "gloss": "the class", "ans": {"job": "owner", "sign": "kas"},
                 "why": "The owner of {مُدَرِّسِي}: jarr with kasra."},
                {"s": "إِنَّ", "gloss": "indeed", "ans": {"job": "part", "sign": "fixed"},
                 "why": "A particle, fixed on fatha."},
                {"s": "الطُّلَّابَ", "gloss": "the students", "ans": {"job": "iism", "sign": "fat"},
                 "why": "{اِسْمُ إِنَّ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}. A broken plural."},
                {"s": "مُسْتَعِدُّونَ", "gloss": "ready", "ans": {"job": "ikhab", "sign": "waw"},
                 "why": "Inna's information stays rafʿ. A sound m. plural: wāw."},
            ],
        },
    ],

    "homework": [
        # 1 · units 1-2: the right shape
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "كَافَأَ المُدِيرُ ___", "gloss": "the two workers", "ans": {"pick": "b"},
                 "opts": {"pick": pick("العَامِلَانِ", "العَامِلَيْنِ", "العَامِلِينَ")},
                 "why": "Object, naṣb. Two workers: {ـَيْنِ}. {العَامِلِينَ} means three or more."},
                {"s": "اِسْتَقْبَلْنَا ___", "gloss": "the female pilgrims", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الحَاجَّاتُ", "الحَاجَّاتَ", "الحَاجَّاتِ")},
                 "why": "Object, naṣb. A sound f. plural takes kasra, never fatha."},
                {"s": "رَأَيْتُ ___", "gloss": "a shepherd", "ans": {"pick": "a"},
                 "opts": {"pick": pick("رَاعِيًا", "رَاعٍ", "رَاعِيٍ")},
                 "why": "A manqūṣ in naṣb shows its fatha: {رَاعِيًا}. {رَاعٍ} is rafʿ or jarr."},
                {"s": "أَكْرَمْتُ ___ المُعَلِّمِ", "gloss": "the teacher's father", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَبُو", "أَبِي", "أَبَا")},
                 "why": "Object, naṣb. A five noun takes alif: {أَبَا المُعَلِّمِ}."},
                {"s": "قَابَلْتُ ___ الشَّرِكَةِ", "gloss": "the company's employees (m.)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُوَظَّفِينَ", "مُوَظَّفِي", "مُوَظَّفُو")},
                 "why": "Naṣb with yāʾ, and the {ن} drops before the owner: {مُوَظَّفِي}."},
                {"s": "زُرْتُ ___", "gloss": "Makka", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَكَّةَ", "مَكَّةً", "مَكَّةِ")},
                 "why": "A feminine name: a diptote. Fatha with no tanween."},
            ],
        },
        # 2 · unit 4: time and purpose in one sentence
        {
            "title": "Job and sign: when and why",
            "prompt": "ذَهَبَ الطُّلَّابُ إِلَى المَكْتَبَةِ صَبَاحَ السَّبْتِ رَغْبَةً فِي القِرَاءَةِ.",
            "en": "The students went to the library on Saturday morning out of a wish to read.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, PREP, OWNER, PURP, WHEN]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS]},
            ],
            "rows": [
                {"s": "الطُّلَّابُ", "gloss": "the students", "ans": {"job": "doer", "sign": "dam"},
                 "why": "They went. Doer, rafʿ. A broken plural: damma."},
                {"s": "المَكْتَبَةِ", "gloss": "the library", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {إِلَى}: jarr with kasra."},
                {"s": "صَبَاحَ", "gloss": "morning (of)", "ans": {"job": "when", "sign": "fat"},
                 "why": "When did they go? A time word in naṣb. It is owned, so one fatha and no tanween."},
                {"s": "السَّبْتِ", "gloss": "Saturday", "ans": {"job": "owner", "sign": "kas"},
                 "why": "Owned by {صَبَاحَ}: owner, jarr with kasra."},
                {"s": "رَغْبَةً", "gloss": "out of a wish", "ans": {"job": "purp", "sign": "fat"},
                 "why": "Why did they go? Out of a wish. A maṣdar giving the reason: {مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
            ],
        },
        # 3 · units 2, 3, 4, 5, 6: which naṣb job?
        {
            "title": "Which naṣb job?",
            "fields": [{"key": "job", "label": "Job of the word in [ ]", "options": [OBJ, MUTL, PURP, STATE, TAMY]}],
            "rows": [
                {"s": "طَبَخَتِ الأُمُّ [الطَّعَامَ].", "gloss": "The mother cooked the food.", "ans": {"job": "obj"},
                 "why": "What did she cook? The food. It is not the maṣdar of {طَبَخَ}: object."},
                {"s": "طَبَخَتِ الأُمُّ الطَّعَامَ [طَبْخًا] جَيِّدًا.", "gloss": "The mother cooked the food well.", "ans": {"job": "mutl"},
                 "why": "{طَبْخٌ} is the maṣdar of {طَبَخَ}, the same verb: the verb's own noun."},
                {"s": "أَسْرَعْتُ [خَوْفًا] مِنَ المَطَرِ.", "gloss": "I hurried for fear of the rain.", "ans": {"job": "purp"},
                 "why": "Why did I hurry? Out of fear. A maṣdar of another verb giving the reason: purpose."},
                {"s": "وَقَفَ الحَارِسُ [يَقِظًا].", "gloss": "The guard stood alert.", "ans": {"job": "state"},
                 "why": "How did he stand? Alert. A describing word after a definite doer: state."},
                {"s": "كَثُرَ الطُّلَّابُ [عَدَدًا].", "gloss": "The students grew many in number.", "ans": {"job": "tamy"},
                 "why": "Many in what respect? In number. A thing word: specifier."},
                {"s": "جَرَى العَدَّاءُ [جَرْيًا] سَرِيعًا.", "gloss": "The runner ran a fast run.", "ans": {"job": "mutl"},
                 "why": "{جَرْيٌ} is the maṣdar of {جَرَى}. With the adjective it tells the kind of running."},
            ],
        },
        # 4 · units 5 and 7: after وَ, إِلَّا and غَيْرَ
        {
            "title": "Which form is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "سَافَرَ الحُجَّاجُ إِلَّا ___", "gloss": "an old man", "ans": {"pick": "b"},
                 "opts": {"pick": pick("شَيْخٌ", "شَيْخًا", "شَيْخٍ")},
                 "why": "Group named, no negative: the exception is naṣb with fatha and tanween."},
                {"s": "حَضَرَ المَدْعُوُّونَ غَيْرَ ___", "gloss": "the doctors", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الأَطِبَّاءَ", "الأَطِبَّاءُ", "الأَطِبَّاءِ")},
                 "why": "The owner of {غَيْرَ}, in jarr. {أَطِبَّاءُ} is a diptote, but with {ال} it takes kasra."},
                {"s": "نَامَتِ النِّسَاءُ إِلَّا ___", "gloss": "the female nurses", "ans": {"pick": "a"},
                 "opts": {"pick": pick("المُمَرِّضَاتِ", "المُمَرِّضَاتَ", "المُمَرِّضَاتُ")},
                 "why": "Exception, naṣb. A sound f. plural takes kasra in place of fatha."},
                {"s": "سِرْتُ وَ___ النَّهْرِ", "gloss": "I walked along the river bank.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("شَاطِئِ", "شَاطِئَ", "شَاطِئُ")},
                 "why": "A river bank does not walk. {وَ} means \"together with\": naṣb. It is owned, so no tanween."},
                {"s": "عَادَ التُّجَّارُ وَ___", "gloss": "and the sailors", "ans": {"pick": "a"},
                 "opts": {"pick": pick("البَحَّارَةُ", "البَحَّارَةَ", "البَحَّارَةِ")},
                 "why": "The sailors came back too. {وَ} means \"and\": it copies the doer in rafʿ."},
                {"s": "جَاءَتِ الأَخَوَاتُ ___", "gloss": "smiling", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُبْتَسِمَاتِ", "مُبْتَسِمَاتٍ", "مُبْتَسِمَاتًا")},
                 "why": "A state: indefinite, naṣb. A sound f. plural takes kasra with tanween."},
            ],
        },
        # 5 · unit 8: the one called
        {
            "title": "Which type, which sign?",
            "fields": [
                {"key": "type", "label": "Type", "options": [NAME, FACE, OWN, ANY]},
                {"key": "sign", "label": "Sign", "options": [FAT, ALIF, YA, FIXED]},
            ],
            "rows": [
                {"s": "يَا [مَرْيَمُ]", "gloss": "Maryam!", "ans": {"type": "name", "sign": "fixed"},
                 "why": "A name: fixed on damma, in the place of naṣb."},
                {"s": "يَا [سَائِقَ] الحَافِلَةِ", "gloss": "O driver of the bus!", "ans": {"type": "own", "sign": "fat"},
                 "why": "Owned by {الحَافِلَةِ}: naṣb with fatha."},
                {"s": "يَا [لَاعِبُونَ]", "gloss": "Players! (in front of you)", "ans": {"type": "face", "sign": "fixed"},
                 "why": "The players you face: fixed on the wāw, in the place of naṣb. It does not change to {ـِينَ}."},
                {"s": "يَا [مُسْرِفًا]", "gloss": "O wasteful one, whoever you are!", "ans": {"type": "any", "sign": "fat"},
                 "why": "No one person is meant: naṣb with fatha and tanween."},
                {"s": "يَا [أَبَا] الطِّفْلِ", "gloss": "O father of the child!", "ans": {"type": "own", "sign": "alif"},
                 "why": "Owned by {الطِّفْلِ}: naṣb. A five noun takes alif."},
                {"s": "يَا [مُدَرِّسَتَانِ]", "gloss": "O two (female) teachers! (in front of you)", "ans": {"type": "face", "sign": "fixed"},
                 "why": "Two people you face: fixed on the alif, in the place of naṣb."},
            ],
        },
        # 6 · unit 9: kāna's information
        {
            "title": "Job and sign: kāna",
            "prompt": "كَانَ أَخُوكَ مُحَامِيًا نَاجِحًا.",
            "en": "Your brother was a successful lawyer.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, KISM, KKHAB, OWNER, ADJ]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, WAW, FIXED]},
            ],
            "rows": [
                {"s": "كَانَ", "gloss": "was", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "أَخُو", "gloss": "brother, in أَخُوكَ", "ans": {"job": "kism", "sign": "waw"},
                 "why": "{اِسْمُ كَانَ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ}."},
                {"s": "ـكَ", "gloss": "your", "ans": {"job": "owner", "sign": "fixed"},
                 "why": "The owner: a fixed pronoun, in the place of jarr."},
                {"s": "مُحَامِيًا", "gloss": "a lawyer", "ans": {"job": "kkhab", "sign": "fat"},
                 "why": "Kāna's information, naṣb. A manqūṣ shows its fatha on the {ي}: {مُحَامِيًا}."},
                {"s": "نَاجِحًا", "gloss": "successful", "ans": {"job": "adj", "sign": "fat"},
                 "why": "It describes {مُحَامِيًا} and copies it: indefinite, naṣb, fatha."},
            ],
        },
    ],
}
