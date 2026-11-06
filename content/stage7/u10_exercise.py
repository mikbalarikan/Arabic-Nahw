# Stage 7: class exercise (review of units 1-9, done together in class before the Stage 7 quiz)

# Canonical options (STAGES_5_8_SPEC.md), copied exactly.
DAM = {"k": "dam", "label": "Damma · ضَمَّةٌ", "color": "red"}
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
KAS = {"k": "kas", "label": "Kasra · كَسْرَةٌ", "color": "green"}
ALIF = {"k": "alif", "label": "Alif · الأَلِفُ", "color": "teal"}
WAW = {"k": "waw", "label": "Wāw · الوَاوُ", "color": "blue"}
YA = {"k": "ya", "label": "Yāʾ · اليَاءُ", "color": "purple"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}

DUAL = {"k": "dual", "label": "Dual · مُثَنًّى", "color": "teal"}
SMP = {"k": "smp", "label": "Sound m. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ", "color": "blue"}
SFP = {"k": "sfp", "label": "Sound f. plural · جَمْعُ مُؤَنَّثٍ سَالِمٌ", "color": "pink"}
BRK = {"k": "brk", "label": "Broken plural · جَمْعُ تَكْسِيرٍ", "color": "purple"}
FIVE = {"k": "five", "label": "Five nouns · الأَسْمَاءُ الخَمْسَةُ", "color": "gold"}
HIDV = {"k": "hidv", "label": "Hidden vowel", "color": "brown"}

VERB = {"k": "verb", "label": "Verb · فِعْلٌ", "color": "navy"}
DOER = {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"}
KISM = {"k": "kism", "label": "Kāna's noun · اِسْمُ كَانَ", "color": "gold"}
KKHAB = {"k": "kkhab", "label": "Kāna's information · خَبَرُ كَانَ", "color": "red"}
IISM = {"k": "iism", "label": "Inna's noun · اِسْمُ إِنَّ", "color": "gold"}
IKHAB = {"k": "ikhab", "label": "Inna's information · خَبَرُ إِنَّ", "color": "red"}
PREP = {"k": "prep", "label": "After a preposition · اِسْمٌ مَجْرُورٌ", "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
AND = {"k": "and", "label": "After وَ (and) · مَعْطُوفٌ", "color": "blue"}
OBJ = {"k": "obj", "label": "Object · مَفْعُولٌ بِهِ", "color": "pink"}
MUTL = {"k": "mutl", "label": "Verb's own noun · مَفْعُولٌ مُطْلَقٌ", "color": "purple"}
PURP = {"k": "purp", "label": "Purpose · مَفْعُولٌ لِأَجْلِهِ", "color": "teal"}
WHEN = {"k": "when", "label": "Time/place · مَفْعُولٌ فِيهِ", "color": "brown"}
MAAH = {"k": "maah", "label": "Together with · مَفْعُولٌ مَعَهُ", "color": "blue"}
STATE = {"k": "state", "label": "State · حَالٌ", "color": "olive"}
TAMY = {"k": "tamy", "label": "Specifier · تَمْيِيزٌ", "color": "gold"}
EXC = {"k": "exc", "label": "Exception · مُسْتَثْنًى", "color": "red"}
PART = {"k": "part", "label": "Particle · حَرْفٌ", "color": "grey"}

NASB_SIGNS = [FAT, ALIF, YA, KAS, HID]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s7-exercise",
    "order": 10,
    "kind": "exercise",
    "title": "Stage 7 class exercise",
    "ar": "تَمْرِينُ المَنْصُوبَاتِ",
    "blurb": "Ten mixed cards on every naṣb job of Stage 7, done together in class before the Stage 7 quiz.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 7 · CLASS EXERCISE", "title": "All the naṣb jobs together",
         "text": "Ten cards that mix every Stage 7 unit. We do them together in class, before the Stage 7 quiz.",
         "wm": "المَنْصُوبَاتُ"},

        {"t": "h2", "text": "How we do it in class"},
        {"t": "p", "text": "Work in pairs, or come to the board. One student reads the sentence aloud. For each word, say three things: the job, the case and the sign. The partner checks it, or corrects it. Then swap for the next row."},
        {"t": "tip", "text": "Use the method of the stage. Find the job. The job gives the case. The kind of noun gives the sign."},
        {"t": "tip", "text": "Say the full formula for at least one word in every card: {حَالٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},

        {"t": "h2", "text": "The topics in short"},
        {"t": "cols", "items": [
            {"color": "pink", "title": "1. The signs", "ar": "عَلَامَاتُ النَّصْبِ",
             "text": "Fatha, alif ({أَبَاكَ}), yāʾ ({ـَيْنِ} / {ـِينَ}), kasra ({ـَاتِ}), hidden fatha ({الفَتَى}). The manqūṣ shows it: {القَاضِيَ}."},
            {"color": "pink", "title": "2. The object", "ar": "المَفْعُولُ بِهِ",
             "text": "\"What?\" or \"whom?\". {أَعْطَى} takes two objects. A pronoun object: {رَأَيْتُهُ}."},
            {"color": "purple", "title": "3. Verb's own noun", "ar": "المَفْعُولُ المُطْلَقُ",
             "text": "The maṣdar of the same verb: {جَلَسْتُ جُلُوسًا}. Emphasis, kind, number."},
            {"color": "teal", "title": "4. Purpose, time, place", "ar": "لِأَجْلِهِ وَفِيهِ",
             "text": "\"Why?\": {احْتِرَامًا}. \"When?\" or \"where?\": {مَسَاءً}، {أَمَامَ}."},
            {"color": "olive", "title": "5. Together with, state", "ar": "مَعَهُ وَالحَالُ",
             "text": "{سِرْتُ وَالنِّيلَ}. The state answers \"how?\": {جَاءَ مُسْرِعًا}."},
            {"color": "gold", "title": "6. The specifier", "ar": "التَّمْيِيزُ",
             "text": "\"Of what?\": {رِطْلًا زَيْتًا}، {عِشْرُونَ طَالِبًا}، {اِمْتَلَأَ مَاءً}."},
            {"color": "red", "title": "7. The exception", "ar": "المُسْتَثْنَى",
             "text": "{إِلَّا زَيْدًا}: naṣb. {غَيْرَ زَيْدٍ}: {غَيْرَ} takes the naṣb, the next word is jarr."},
            {"color": "green", "title": "8. The one called", "ar": "المُنَادَى",
             "text": "{يَا زَيْدُ} fixed. {يَا عَبْدَ اللّٰهِ} naṣb. {يَا غَافِلًا} naṣb."},
            {"color": "gold", "title": "9. Inna and kāna", "ar": "إِنَّ وَكَانَ",
             "text": "Inna's noun is naṣb: {إِنَّ المُسْلِمِينَ}. Kāna's information is naṣb: {كَانَ بَارِدًا}."},
        ]},

        {"t": "h2", "text": "One question for each job"},
        {"t": "table", "head": ["Job", "Ask", "Example"], "rows": [
            ["Object", "What? Whom?", "{فَتَحْتُ البَابَ.}"],
            ["Verb's own noun", "Is it the maṣdar of the same verb?", "{ضَحِكْتُ ضَحِكًا.}"],
            ["Purpose", "Why?", "{سَكَتُّ خَوْفًا.}"],
            ["Time/place", "When? How long? Where?", "{نِمْتُ سَاعَةً.}"],
            ["Together with", "Can it do the action too? No.", "{سِرْتُ وَالنِّيلَ.}"],
            ["State", "How? In what state?", "{رَجَعَ فَرِحًا.}"],
            ["Specifier", "Of what? In what respect?", "{اِمْتَلَأَ الكُوبُ مَاءً.}"],
        ]},

        {"t": "summary", "title": "Remember", "items": [
            "The job gives naṣb. The kind of noun gives the sign.",
            "Yāʾ for the dual and the sound m. plural. Kasra for the sound f. plural, never fatha. Alif for the five nouns.",
            "Hidden fatha for the maqṣūr and noun + ـي. The manqūṣ shows its fatha: {الرَّاعِيَ}.",
            "The state and the specifier are indefinite. The state describes, the specifier names a thing.",
            "Kāna: its information is naṣb. Inna: its noun is naṣb. The other partner is rafʿ.",
        ]},
    ],

    "practice": [
        # 1 · unit 1: the signs of naṣb
        {
            "title": "Which group, which sign?",
            "fields": [
                {"key": "kind", "label": "Group", "options": [DUAL, SMP, SFP, BRK, FIVE, HIDV]},
                {"key": "sign", "label": "Sign", "options": NASB_SIGNS},
            ],
            "rows": [
                {"s": "شَكَرْتُ [المُوَظَّفِينَ]", "gloss": "I thanked the employees.", "ans": {"kind": "smp", "sign": "ya"},
                 "why": "{مُوَظَّفٌ} + {ـِينَ}: a sound m. plural. Object, naṣb, sign yāʾ."},
                {"s": "سَاعَدْتُ [المُسَافِرَاتِ]", "gloss": "I helped the female travellers.", "ans": {"kind": "sfp", "sign": "kas"},
                 "why": "{مُسَافِرَةٌ} → {مُسَافِرَاتٌ}: a sound f. plural. Kasra in place of fatha."},
                {"s": "قَابَلْتُ [أَبَا] خَالِدٍ", "gloss": "I met Khālid's father.", "ans": {"kind": "five", "sign": "alif"},
                 "why": "{أَبٌ} owned by {خَالِدٍ}: a five noun. Sign alif."},
                {"s": "فَتَحْتُ [الأَبْوَابَ]", "gloss": "I opened the doors.", "ans": {"kind": "brk", "sign": "fat"},
                 "why": "{أَبْوَابٌ} is the broken plural of {بَابٌ}. Broken plurals take fatha."},
                {"s": "زُرْتُ [المَقْهَى]", "gloss": "I visited the café.", "ans": {"kind": "hidv", "sign": "hid"},
                 "why": "It ends in {ـَى}: a maqṣūr. The fatha is hidden on the alif."},
                {"s": "سَأَلْتُ [الرَّاعِيَ]", "gloss": "I asked the shepherd.", "ans": {"kind": "hidv", "sign": "fat"},
                 "why": "A manqūṣ, in the hidden-vowel group. But in naṣb the fatha shows on the {ي}."},
            ],
        },
        # 2 · unit 2: the object, two objects
        {
            "title": "Job and sign: two objects",
            "prompt": "أَعْطَى المُعَلِّمُ الفَائِزِينَ كُتُبًا مُفِيدَةً.",
            "en": "The teacher gave the winners useful books.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, ADJ]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, YA, FIXED]},
            ],
            "rows": [
                {"s": "أَعْطَى", "gloss": "gave", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb. It is fixed."},
                {"s": "المُعَلِّمُ", "gloss": "the teacher", "ans": {"job": "doer", "sign": "dam"},
                 "why": "He did the giving. Doer, rafʿ, damma."},
                {"s": "الفَائِزِينَ", "gloss": "the winners", "ans": {"job": "obj", "sign": "ya"},
                 "why": "The first object, the ones who received: {مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "كُتُبًا", "gloss": "books", "ans": {"job": "obj", "sign": "fat"},
                 "why": "The second object, the thing given. A broken plural: fatha."},
                {"s": "مُفِيدَةً", "gloss": "useful", "ans": {"job": "adj", "sign": "fat"},
                 "why": "It describes {كُتُبًا} and copies it: indefinite, naṣb, fatha."},
            ],
        },
        # 3 · unit 3: the verb's own noun (number), with place
        {
            "title": "Job and sign: the verb's own noun",
            "prompt": "دَارَ اللَّاعِبُ حَوْلَ المَلْعَبِ دَوْرَتَيْنِ.",
            "en": "The player went round the field twice.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, OBJ, MUTL, WHEN, OWNER]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, YA]},
            ],
            "rows": [
                {"s": "اللَّاعِبُ", "gloss": "the player", "ans": {"job": "doer", "sign": "dam"},
                 "why": "He went round. Doer, rafʿ, damma."},
                {"s": "حَوْلَ", "gloss": "around", "ans": {"job": "when", "sign": "fat"},
                 "why": "Where did he go? Around the field. A place word, naṣb with fatha. It is owned, so no tanween."},
                {"s": "المَلْعَبِ", "gloss": "the field", "ans": {"job": "owner", "sign": "kas"},
                 "why": "Owned by {حَوْلَ}: owner, jarr with kasra."},
                {"s": "دَوْرَتَيْنِ", "gloss": "two rounds", "ans": {"job": "mutl", "sign": "ya"},
                 "why": "{دَوْرَةٌ} \"one turn\" comes from {دَارَ}. It counts the action: {مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
            ],
        },
        # 4 · unit 4: purpose and time
        {
            "title": "Job and sign: why and when",
            "prompt": "خَرَجَ الطَّبِيبُ إِلَى القَرْيَةِ لَيْلًا رَحْمَةً بِالمَرْضَى.",
            "en": "The doctor went out to the village at night, out of mercy for the sick.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, PREP, PURP, WHEN, STATE]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, HID]},
            ],
            "rows": [
                {"s": "الطَّبِيبُ", "gloss": "the doctor", "ans": {"job": "doer", "sign": "dam"},
                 "why": "He went out. Doer, rafʿ, damma."},
                {"s": "القَرْيَةِ", "gloss": "the village", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {إِلَى}: jarr with kasra."},
                {"s": "لَيْلًا", "gloss": "at night", "ans": {"job": "when", "sign": "fat"},
                 "why": "When did he go out? At night. {ظَرْفُ زَمَانٍ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
                {"s": "رَحْمَةً", "gloss": "out of mercy", "ans": {"job": "purp", "sign": "fat"},
                 "why": "Why did he go out? Out of mercy. A maṣdar giving the reason: {مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
                {"s": "المَرْضَى", "gloss": "the sick, in بِالمَرْضَى", "ans": {"job": "prep", "sign": "hid"},
                 "why": "Review: after {بِـ}, jarr. {المَرْضَى} ends in {ـَى}, so the kasra is hidden."},
            ],
        },
        # 5 · unit 5: together with, and the state
        {
            "title": "Job and sign of the word in [ ]",
            "fields": [
                {"key": "job", "label": "Job", "options": [AND, MAAH, STATE, ADJ]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, YA]},
            ],
            "rows": [
                {"s": "اِسْتَيْقَظْتُ وَ[صِيَاحَ] الدِّيكِ", "gloss": "I woke up at the cock's crow.", "ans": {"job": "maah", "sign": "fat"},
                 "why": "The crowing does not wake up. {وَ} means \"together with\": naṣb, fatha. It is owned, so no tanween."},
                {"s": "نَجَحَ الطُّلَّابُ وَ[الطَّالِبَاتُ]", "gloss": "The male and female students passed.", "ans": {"job": "and", "sign": "dam"},
                 "why": "The female students passed too. {وَ} means \"and\": it copies the doer in rafʿ, damma."},
                {"s": "خَرَجَ اللَّاعِبَانِ [غَاضِبَيْنِ]", "gloss": "The two players went out angry.", "ans": {"job": "state", "sign": "ya"},
                 "why": "How did they go out? Angry. Indefinite, after a definite doer: a state. Dual: yāʾ."},
                {"s": "رَأَيْتُ طِفْلًا [نَائِمًا]", "gloss": "I saw a sleeping child.", "ans": {"job": "adj", "sign": "fat"},
                 "why": "{طِفْلًا} is indefinite, and {نَائِمًا} copies it: an adjective."},
                {"s": "رَجَعَتِ المُمَرِّضَاتُ [مُتْعَبَاتٍ]", "gloss": "The nurses came back tired.", "ans": {"job": "state", "sign": "kas"},
                 "why": "How did they come back? Tired. A state. Sound f. plural: kasra in place of fatha."},
                {"s": "ذَاكَرْتُ وَ[ضَوْءَ] القَمَرِ", "gloss": "I studied by the light of the moon.", "ans": {"job": "maah", "sign": "fat"},
                 "why": "Moonlight does not study. Together with, naṣb, fatha."},
            ],
        },
        # 6 · unit 6: the specifier after a measure
        {
            "title": "Job and sign: the specifier",
            "prompt": "اِشْتَرَى الطَّبَّاخُ رِطْلَيْنِ لَحْمًا.",
            "en": "The cook bought two pounds of meat.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, OBJ, TAMY]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, YA, FIXED]},
            ],
            "rows": [
                {"s": "اِشْتَرَى", "gloss": "bought", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb. It is fixed."},
                {"s": "الطَّبَّاخُ", "gloss": "the cook", "ans": {"job": "doer", "sign": "dam"},
                 "why": "He did the buying. Doer, rafʿ, damma."},
                {"s": "رِطْلَيْنِ", "gloss": "two pounds", "ans": {"job": "obj", "sign": "ya"},
                 "why": "What did he buy? Two pounds. The measure is the object. A dual: yāʾ."},
                {"s": "لَحْمًا", "gloss": "meat", "ans": {"job": "tamy", "sign": "fat"},
                 "why": "Two pounds of what? Meat. {تَمْيِيزٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}. It stays singular."},
            ],
        },
        # 7 · unit 7: the exception
        {
            "title": "Job and sign: the exception",
            "prompt": "زَارَ السُّيَّاحُ المُدُنَ إِلَّا مَدِينَتَيْنِ.",
            "en": "The tourists visited the cities, except two cities.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, OBJ, EXC, PART]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, YA, FIXED]},
            ],
            "rows": [
                {"s": "السُّيَّاحُ", "gloss": "the tourists", "ans": {"job": "doer", "sign": "dam"},
                 "why": "They did the visiting. Doer, rafʿ. A broken plural takes damma."},
                {"s": "المُدُنَ", "gloss": "the cities", "ans": {"job": "obj", "sign": "fat"},
                 "why": "What did they visit? The cities. This is the group. Object, naṣb, fatha."},
                {"s": "إِلَّا", "gloss": "except", "ans": {"job": "part", "sign": "fixed"},
                 "why": "The tool of exception. A particle, fixed on sukūn."},
                {"s": "مَدِينَتَيْنِ", "gloss": "two cities", "ans": {"job": "exc", "sign": "ya"},
                 "why": "Group named, no negative: {مُسْتَثْنًى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}."},
            ],
        },
        # 8 · unit 8: the one called
        {
            "title": "Which form is right after يَا?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "يَا ___، اِفْتَحِ البَابَ.", "gloss": "Ḥasan, open the door.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("حَسَنُ", "حَسَنًا", "حَسَنٌ")},
                 "why": "A name: one damma, no tanween. Fixed on damma, in the place of naṣb."},
                {"s": "يَا ___ المَسْجِدِ", "gloss": "O imam of the mosque!", "ans": {"pick": "b"},
                 "opts": {"pick": pick("إِمَامُ", "إِمَامَ", "إِمَامِ")},
                 "why": "Owned by {المَسْجِدِ}: naṣb with fatha."},
                {"s": "يَا ___", "gloss": "O two girls! (in front of you)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("بِنْتَانِ", "بِنْتَيْنِ")},
                 "why": "Two girls you face: fixed on the alif, in the place of naṣb."},
                {"s": "يَا ___", "gloss": "O careless one, whoever you are!", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُهْمِلُ", "مُهْمِلٌ", "مُهْمِلًا")},
                 "why": "No one person is meant: naṣb with fatha and tanween. {مُهْمِلُ} would be the one you face."},
                {"s": "يَا ___ الفَرِيقِ", "gloss": "O players (m.) of the team!", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَاعِبُو", "لَاعِبِي", "لَاعِبِينَ")},
                 "why": "Owned: naṣb. A sound m. plural takes yāʾ, and the {ن} drops before the owner: {لَاعِبِي}."},
                {"s": "يَا ___ عَلِيٍّ", "gloss": "O brother of ʿAlī!", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَخُو", "أَخِي", "أَخَا")},
                 "why": "Owned by {عَلِيٍّ}: naṣb. A five noun takes alif: {أَخَا}."},
            ],
        },
        # 9 · unit 9: inna's noun and kāna's information
        {
            "title": "Which partner, which sign?",
            "fields": [
                {"key": "job", "label": "Job", "options": [KISM, KKHAB, IISM, IKHAB]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, ALIF, WAW, YA, HID]},
            ],
            "rows": [
                {"s": "إِنَّ [الفَلَّاحِينَ] نَشِيطُونَ", "gloss": "Indeed the farmers are active.", "ans": {"job": "iism", "sign": "ya"},
                 "why": "The first partner after {إِنَّ}: {اِسْمُ إِنَّ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "كَانَ [الفَلَّاحُونَ] نَشِيطِينَ", "gloss": "The farmers were active.", "ans": {"job": "kism", "sign": "waw"},
                 "why": "The first partner after {كَانَ}: kāna's noun, rafʿ. Sound m. plural: wāw."},
                {"s": "كَانَ الفَلَّاحُونَ [نَشِيطِينَ]", "gloss": "The farmers were active.", "ans": {"job": "kkhab", "sign": "ya"},
                 "why": "The second partner after {كَانَ}: kāna's information, naṣb. Sound m. plural: yāʾ."},
                {"s": "لَعَلَّ [المُسْتَشْفَى] قَرِيبٌ", "gloss": "Perhaps the hospital is near.", "ans": {"job": "iism", "sign": "hid"},
                 "why": "{لَعَلَّ} is a sister of {إِنَّ}. Its noun is naṣb. A maqṣūr: hidden fatha."},
                {"s": "أَصْبَحَتِ السَّمَاءُ [صَافِيَةً]", "gloss": "The sky became clear.", "ans": {"job": "kkhab", "sign": "fat"},
                 "why": "{أَصْبَحَ} is a sister of {كَانَ}. Its information is naṣb. A singular: fatha."},
                {"s": "كَأَنَّ [أَخَاكَ] أَسَدٌ", "gloss": "It is as if your brother is a lion.", "ans": {"job": "iism", "sign": "alif"},
                 "why": "{كَأَنَّ} is a sister of {إِنَّ}. Its noun is naṣb. A five noun: alif."},
            ],
        },
        # 10 · mixed: which naṣb job?
        {
            "title": "Which naṣb job?",
            "fields": [{"key": "job", "label": "Job of the word in [ ]", "options": [OBJ, MUTL, PURP, WHEN, STATE, TAMY]}],
            "rows": [
                {"s": "قُمْتُ [إِجْلَالًا] لِلشَّيْخِ.", "gloss": "I stood up out of reverence for the old man.", "ans": {"job": "purp"},
                 "why": "Why did I stand? Out of reverence. A maṣdar of another verb, giving the reason: purpose."},
                {"s": "اِمْتَلَأَ الكِيسُ [دَقِيقًا].", "gloss": "The bag was filled with flour.", "ans": {"job": "tamy"},
                 "why": "Filled with what? Flour. A thing word: specifier."},
                {"s": "صَلَّيْنَا [أَمَامَ] الكَعْبَةِ.", "gloss": "We prayed in front of the Kaʿba.", "ans": {"job": "when"},
                 "why": "Where did we pray? A place word in naṣb."},
                {"s": "فَتَحْتُ [النَّافِذَةَ].", "gloss": "I opened the window.", "ans": {"job": "obj"},
                 "why": "What did I open? The window. The action falls on it: object."},
                {"s": "رَجَعَ الحَارِسُ [حَزِينًا].", "gloss": "The guard came back sad.", "ans": {"job": "state"},
                 "why": "How did he come back? Sad. A describing word after a definite doer: state."},
                {"s": "اِبْتَسَمَتِ البِنْتُ [ابْتِسَامَةً] جَمِيلَةً.", "gloss": "The girl smiled a beautiful smile.", "ans": {"job": "mutl"},
                 "why": "{ابْتِسَامَةً} comes from {اِبْتَسَمَ}, the same verb, and {جَمِيلَةً} gives its kind: the verb's own noun."},
            ],
        },
    ],

    "homework": [],
}
