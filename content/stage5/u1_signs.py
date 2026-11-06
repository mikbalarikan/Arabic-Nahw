# Stage 5, Unit 1: The signs of rafʿ (عَلَامَاتُ الرَّفْعِ)

# Canonical options (STAGES_5_8_SPEC.md)
DAM = {"k": "dam", "label": "Damma · ضَمَّةٌ", "color": "red"}
ALIF = {"k": "alif", "label": "Alif · الأَلِفُ", "color": "teal"}
WAW = {"k": "waw", "label": "Wāw · الوَاوُ", "color": "blue"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "grey"}

SING = {"k": "sing", "label": "Singular · مُفْرَدٌ", "color": "grey"}
DUAL = {"k": "dual", "label": "Dual · مُثَنًّى", "color": "teal"}
SMP = {"k": "smp", "label": "Sound m. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ", "color": "blue"}
SFP = {"k": "sfp", "label": "Sound f. plural · جَمْعُ مُؤَنَّثٍ سَالِمٌ", "color": "pink"}
BRK = {"k": "brk", "label": "Broken plural · جَمْعُ تَكْسِيرٍ", "color": "purple"}
FIVE = {"k": "five", "label": "Five nouns · الأَسْمَاءُ الخَمْسَةُ", "color": "gold"}
HIDV = {"k": "hidv", "label": "Hidden vowel", "color": "brown"}

TOPIC = {"k": "topic", "label": "Topic · مُبْتَدَأٌ", "color": "gold"}
INFO = {"k": "info", "label": "Information · خَبَرٌ", "color": "red"}
VERB = {"k": "verb", "label": "Verb · فِعْلٌ", "color": "navy"}
DOER = {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
AND = {"k": "and", "label": "After وَ (and) · مَعْطُوفٌ", "color": "blue"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s5-signs",
    "order": 1,
    "title": "The signs of rafʿ",
    "ar": "عَلَامَاتُ الرَّفْعِ",
    "blurb": "Seven jobs put a noun in rafʿ. Four signs show it: damma, alif, wāw and the hidden damma.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 5 · UNIT 1", "title": "One case, four signs",
         "text": "Stage 5 is about rafʿ. You will meet seven jobs that take rafʿ, and learn which sign every kind of noun uses.",
         "wm": "المَرْفُوعَاتُ"},

        {"t": "h2", "text": "Seven jobs take rafʿ"},
        {"t": "p", "text": "A noun is in rafʿ when it does one of these seven jobs. You know some of them already. This list is a preview. Units 2 to 7 take them one by one."},
        {"t": "table", "head": ["Job", "Arabic", "Example", "Unit"], "rows": [
            ["Topic", "المُبْتَدَأُ", "{الطَّالِبُ} مُجْتَهِدٌ.", "2"],
            ["Information", "الخَبَرُ", "الطَّالِبُ {مُجْتَهِدٌ}.", "2"],
            ["Doer", "الفَاعِلُ", "جَاءَ {المُعَلِّمُ}.", "3"],
            ["Doer stand-in", "نَائِبُ الفَاعِلِ", "كُتِبَ {الدَّرْسُ}.", "4"],
            ["Kāna's noun", "اِسْمُ كَانَ وَأَخَوَاتِهَا", "كَانَ {البَيْتُ} نَظِيفًا.", "5"],
            ["Inna's information", "خَبَرُ إِنَّ وَأَخَوَاتِهَا", "إِنَّ البَابَ {مَفْتُوحٌ}.", "6"],
            ["Follower", "التَّابِعُ لِلْمَرْفُوعِ", "جَاءَ الطَّالِبُ {المُجْتَهِدُ}.", "7"],
        ]},
        {"t": "tip", "text": "A follower is an adjective, a word after {وَ}, an emphasis word or a substitute. It copies the case of the word before it."},

        {"t": "h2", "text": "The four signs of rafʿ"},
        {"t": "cols", "items": [
            {"color": "red", "title": "Damma", "ar": "الضَّمَّةُ", "text": "The original sign: {الطَّالِبُ}."},
            {"color": "teal", "title": "Alif", "ar": "الأَلِفُ", "text": "The dual: {الطَّالِبَانِ}."},
            {"color": "blue", "title": "Wāw", "ar": "الوَاوُ", "text": "Sound m. plural and five nouns: {المُسْلِمُونَ}، {أَبُوكَ}."},
            {"color": "brown", "title": "Hidden damma", "ar": "الضَّمَّةُ المُقَدَّرَةُ", "text": "Ends in alif or {ي}, or has {ـي} \"my\": {الفَتَى}، {القَاضِي}، {كِتَابِي}."},
        ]},
        {"t": "rule", "color": "red", "title": "Original and branch signs",
         "text": "The damma is the original sign of rafʿ. Alif and wāw are branch signs: a letter does the work of the damma. The hidden damma is still the original sign. We just cannot see it."},

        {"t": "h2", "text": "Which group takes which sign"},
        {"t": "table", "head": ["Group", "In rafʿ", "Sign"], "rows": [
            ["Singular", "الطَّالِبُ، طَالِبٌ", "damma"],
            ["Broken plural", "الطُّلَّابُ، طُلَّابٌ", "damma"],
            ["Sound f. plural", "الطَّالِبَاتُ، طَالِبَاتٌ", "damma"],
            ["Diptote", "أَحْمَدُ، مَسَاجِدُ", "damma (no tanween)"],
            ["Dual", "الطَّالِبَانِ، طَالِبَانِ", "alif"],
            ["Sound m. plural", "المُسْلِمُونَ، مُسْلِمُونَ", "wāw"],
            ["Five nouns", "أَبُوكَ، أَخُو زَيْدٍ، ذُو مَالٍ", "wāw"],
            ["Maqṣūr", "الفَتَى، مُوسَى", "hidden damma"],
            ["Manqūṣ", "القَاضِي، النَّادِي", "hidden damma"],
            ["Noun + ـي \"my\"", "كِتَابِي، أَبِي", "hidden damma"],
        ]},
        {"t": "tip", "text": "In the dual and the sound m. plural the {ن} is not the sign. The sign is the letter before it: {ا} in {ـَانِ}, {و} in {ـُونَ}."},
        {"t": "tip", "text": "{أَبِي} \"my father\" is a five noun with {ـي} \"my\". It does not take the wāw. Its damma is hidden."},

        {"t": "h2", "text": "The method: job, case, sign"},
        {"t": "rule", "color": "gold", "title": "Three steps",
         "text": "Find the job. The job gives the case. The kind of noun gives the sign."},
        {"t": "p", "text": "Every answer in this stage has three parts. Here is the classic sentence for a doer in the sound m. plural: {فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
        {"t": "examples", "items": [
            {"ar": "المُسْلِمَانِ حَاضِرَانِ.", "en": "The two Muslims are present.",
             "note": "{المُسْلِمَانِ}: Topic, rafʿ, alif. {مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الأَلِفُ لِأَنَّهُ مُثَنًّى}."},
            {"ar": "جَاءَ المُعَلِّمُونَ.", "en": "The teachers came.",
             "note": "{المُعَلِّمُونَ}: doer, rafʿ, wāw. {فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
            {"ar": "أَبُوكَ كَرِيمٌ.", "en": "Your father is generous.",
             "note": "{أَبُوكَ}: Topic, rafʿ, wāw. {مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ}."},
            {"ar": "القَاضِي عَادِلٌ.", "en": "The judge is just.",
             "note": "{القَاضِي}: Topic, rafʿ, hidden damma. {مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ عَلَى اليَاءِ}."},
            {"ar": "الطَّالِبَاتُ مُجْتَهِدَاتٌ.", "en": "The female students are hard-working.",
             "note": "{مُجْتَهِدَاتٌ}: Information, rafʿ, damma. {خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ}."},
        ]},

        {"t": "h2", "text": "Fixed words in a rafʿ job"},
        {"t": "p", "text": "A fixed word can do a rafʿ job too. It shows no sign. We say it is in the place of rafʿ: {فِي مَحَلِّ رَفْعٍ}. You met this in Stage 3."},
        {"t": "examples", "items": [
            {"ar": "هُوَ طَبِيبٌ.", "en": "He is a doctor.",
             "note": "{هُوَ}: {ضَمِيرٌ مَبْنِيٌّ عَلَى الفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ}."},
            {"ar": "هَذَا كِتَابٌ.", "en": "This is a book.",
             "note": "{هَذَا}: {اِسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ}."},
            {"ar": "كَتَبُوا.", "en": "They wrote.",
             "note": "The {و} is the doer. It is fixed, in the place of rafʿ."},
        ]},
        {"t": "tip", "text": "{هَذَانِ} \"these two\" is not fixed. It changes like a dual, so in rafʿ its sign is the alif."},

        {"t": "summary", "title": "In short", "items": [
            "Seven jobs take rafʿ: Topic, Information, doer, doer stand-in, kāna's noun, inna's information, and a follower of a rafʿ word.",
            "Damma: singular, broken plural, sound f. plural, diptote (no tanween).",
            "Alif: the dual. Wāw: the sound m. plural and the five nouns.",
            "Hidden damma: maqṣūr ({الفَتَى}), manqūṣ ({القَاضِي}), and a noun with {ـي} \"my\".",
            "Find the job. The job gives the case. The kind of noun gives the sign.",
            "A fixed word in a rafʿ job is in the place of rafʿ: {فِي مَحَلِّ رَفْعٍ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Which sign of rafʿ does the word in [brackets] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID]}],
            "rows": [
                {"s": "[الطَّالِبَانِ] فِي الفَصْلِ.", "gloss": "the two students", "ans": {"sign": "alif"},
                 "why": "A dual in rafʿ: the sign is the alif of {ـَانِ}."},
                {"s": "[المُهَنْدِسُونَ] حَاضِرُونَ.", "gloss": "the engineers", "ans": {"sign": "waw"},
                 "why": "A sound m. plural in rafʿ: the sign is the wāw of {ـُونَ}."},
                {"s": "[البِنْتُ] صَغِيرَةٌ.", "gloss": "the girl", "ans": {"sign": "dam"},
                 "why": "A singular: the damma shows on the {ت}."},
                {"s": "[الفَتَى] طَالِبٌ.", "gloss": "the young man", "ans": {"sign": "hid"},
                 "why": "Maqṣūr: an alif cannot carry a vowel. Hidden damma."},
                {"s": "[أَخُوكَ] طَبِيبٌ.", "gloss": "your brother", "ans": {"sign": "waw"},
                 "why": "A five noun with an owner ({ـكَ}): the sign is the wāw."},
                {"s": "[المُدَرِّسَاتُ] فِي المَدْرَسَةِ.", "gloss": "the female teachers", "ans": {"sign": "dam"},
                 "why": "A sound f. plural takes damma in rafʿ: {المُدَرِّسَاتُ}."},
            ],
        },
        {
            "title": "Which group is it? Which sign does it take in rafʿ?",
            "fields": [
                {"key": "kind", "label": "Group", "options": [SING, DUAL, SMP, SFP, BRK]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW]},
            ],
            "rows": [
                {"s": "المُسْلِمُونَ", "gloss": "the Muslims", "ans": {"kind": "smp", "sign": "waw"},
                 "why": "{مُسْلِمٌ} + {ـُونَ}: a sound m. plural. The sign is the wāw."},
                {"s": "الكُتُبُ", "gloss": "the books", "ans": {"kind": "brk", "sign": "dam"},
                 "why": "The shape of {كِتَابٌ} changed: a broken plural. Damma."},
                {"s": "السَّيَّارَتَانِ", "gloss": "the two cars", "ans": {"kind": "dual", "sign": "alif"},
                 "why": "{سَيَّارَةٌ} + {ـَانِ}: a dual. The sign is the alif."},
                {"s": "المُسْلِمَاتُ", "gloss": "the Muslim women", "ans": {"kind": "sfp", "sign": "dam"},
                 "why": "{مُسْلِمَةٌ} → {مُسْلِمَاتٌ}: a sound f. plural. Damma."},
                {"s": "الرَّجُلُ", "gloss": "the man", "ans": {"kind": "sing", "sign": "dam"},
                 "why": "One man: a singular. Damma."},
                {"s": "الأَصْوَاتُ", "gloss": "the voices", "ans": {"kind": "brk", "sign": "dam"},
                 "why": "It ends in {ات}, but the singular is {صَوْتٌ}: a broken plural. Damma."},
            ],
        },
        {
            "title": "Which form is right in rafʿ?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "___ مُجْتَهِدُونَ.", "gloss": "The teachers are hard-working.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("المُعَلِّمُونَ", "المُعَلِّمِينَ", "المُعَلِّمَيْنِ")},
                 "why": "Topic in rafʿ, sound m. plural: wāw. {المُعَلِّمِينَ} is the shape for naṣb and jarr."},
                {"s": "___ فِي البَيْتِ.", "gloss": "The two boys are in the house.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الوَلَدَيْنِ", "الوَلَدَانِ", "الوَلَدُونَ")},
                 "why": "Topic in rafʿ, dual: alif. {الوَلَدَانِ}."},
                {"s": "___ كَرِيمٌ.", "gloss": "Your father is generous.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَبَاكَ", "أَبِيكَ", "أَبُوكَ")},
                 "why": "Topic in rafʿ, a five noun: wāw. {أَبُوكَ}."},
                {"s": "جَاءَ ___.", "gloss": "Ahmad came.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَحْمَدٌ", "أَحْمَدُ", "أَحْمَدَ")},
                 "why": "Doer in rafʿ. {أَحْمَدُ} is a diptote: one damma and no tanween."},
                {"s": "___ مُجْتَهِدَاتٌ.", "gloss": "The female students are hard-working.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الطَّالِبَاتُ", "الطَّالِبَاتِ", "الطَّالِبَاتَ")},
                 "why": "Topic in rafʿ, sound f. plural: damma."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "حَضَرَ المُهَنْدِسُونَ المُجْتَهِدُونَ وَالعُمَّالُ.",
            "en": "The hard-working engineers and the workers were present.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, ADJ, AND]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, FIXED]},
            ],
            "rows": [
                {"s": "حَضَرَ", "gloss": "was present", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb. It is fixed on fatha."},
                {"s": "المُهَنْدِسُونَ", "gloss": "the engineers", "ans": {"job": "doer", "sign": "waw"},
                 "why": "{فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ}."},
                {"s": "المُجْتَهِدُونَ", "gloss": "the hard-working", "ans": {"job": "adj", "sign": "waw"},
                 "why": "It describes {المُهَنْدِسُونَ} and copies its rafʿ. It is a sound m. plural too: wāw."},
                {"s": "العُمَّالُ", "gloss": "the workers", "ans": {"job": "and", "sign": "dam"},
                 "why": "After {وَ} it copies the doer's rafʿ. {عُمَّالٌ} is a broken plural: damma."},
            ],
        },
        {
            "title": "Topic or Information? Which sign?",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, INFO]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID, FIXED]},
            ],
            "rows": [
                {"s": "[المُسْلِمَانِ] صَادِقَانِ.", "gloss": "the two Muslims", "ans": {"job": "topic", "sign": "alif"},
                 "why": "The sentence starts with it: Topic. A dual: alif."},
                {"s": "المُسْلِمَانِ [صَادِقَانِ].", "gloss": "truthful (two)", "ans": {"job": "info", "sign": "alif"},
                 "why": "It tells us about the Topic: Information. A dual: alif."},
                {"s": "[هُوَ] مُهَنْدِسٌ.", "gloss": "he", "ans": {"job": "topic", "sign": "fixed"},
                 "why": "A fixed pronoun as Topic: in the place of rafʿ."},
                {"s": "الرَّجُلُ [ذُو] مَالٍ.", "gloss": "the owner of", "ans": {"job": "info", "sign": "waw"},
                 "why": "{ذُو مَالٍ} is the Information. {ذُو} is a five noun: wāw."},
                {"s": "[صَدِيقِي] طَبِيبٌ.", "gloss": "my friend", "ans": {"job": "topic", "sign": "hid"},
                 "why": "Topic. The {ـي} \"my\" needs a kasra before it, so the damma is hidden."},
                {"s": "صَدِيقِي [طَبِيبٌ].", "gloss": "a doctor", "ans": {"job": "info", "sign": "dam"},
                 "why": "Information, a singular: damma with tanween."},
            ],
        },
        {
            "title": "Damma that shows, or hidden damma?",
            "fields": [{"key": "sign", "label": "Sign", "options": [DAM, HID]}],
            "rows": [
                {"s": "[النَّادِي] كَبِيرٌ.", "gloss": "the club", "ans": {"sign": "hid"},
                 "why": "Manqūṣ: ends in {ي} after kasra. Hidden damma."},
                {"s": "[المُسْتَشْفَى] قَرِيبٌ.", "gloss": "the hospital", "ans": {"sign": "hid"},
                 "why": "Maqṣūr: ends in alif. Hidden damma."},
                {"s": "[الكُرْسِيُّ] جَدِيدٌ.", "gloss": "the chair", "ans": {"sign": "dam"},
                 "why": "The {ي} has shadda and carries the damma: {الكُرْسِيُّ}."},
                {"s": "[كِتَابِي] جَدِيدٌ.", "gloss": "my book", "ans": {"sign": "hid"},
                 "why": "A noun with {ـي} \"my\". Hidden damma."},
                {"s": "[السَّمَاءُ] صَافِيَةٌ.", "gloss": "the sky", "ans": {"sign": "dam"},
                 "why": "Mamdūd: the hamza carries the damma. Nothing is hidden."},
                {"s": "[مُوسَى] نَبِيٌّ.", "gloss": "Musa", "ans": {"sign": "hid"},
                 "why": "Ends in alif: hidden damma."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Which sign of rafʿ does the word in [brackets] take?",
            "fields": [{"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID]}],
            "rows": [
                {"s": "[المُدَرِّسَتَانِ] مَشْغُولَتَانِ.", "gloss": "the two female teachers", "ans": {"sign": "alif"},
                 "why": "A dual: alif. The {ة} became {ت} before {ـَانِ}."},
                {"s": "[المُؤْمِنُونَ] صَادِقُونَ.", "gloss": "the believers", "ans": {"sign": "waw"},
                 "why": "A sound m. plural: wāw."},
                {"s": "[زَيْنَبُ] مُدَرِّسَةٌ.", "gloss": "Zaynab", "ans": {"sign": "dam"},
                 "why": "A diptote in rafʿ: one damma, no tanween."},
                {"s": "[المُحَامِي] مَشْغُولٌ.", "gloss": "the lawyer", "ans": {"sign": "hid"},
                 "why": "Manqūṣ: hidden damma on the {ي}."},
                {"s": "[أَخُو] حَامِدٍ تَاجِرٌ.", "gloss": "Hamid's brother", "ans": {"sign": "waw"},
                 "why": "A five noun with an owner ({حَامِدٍ}): wāw."},
                {"s": "[الأَصْدِقَاءُ] حَاضِرُونَ.", "gloss": "the friends", "ans": {"sign": "dam"},
                 "why": "A broken plural and a diptote. In rafʿ both take damma."},
            ],
        },
        {
            "title": "Which group is it? Which sign does it take in rafʿ?",
            "fields": [
                {"key": "kind", "label": "Group", "options": [DUAL, SMP, SFP, FIVE, HIDV]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID]},
            ],
            "rows": [
                {"s": "المُهَنْدِسَتَانِ", "gloss": "the two female engineers", "ans": {"kind": "dual", "sign": "alif"},
                 "why": "{مُهَنْدِسَةٌ} + {ـَانِ}: a dual. Alif."},
                {"s": "أَبُوهُ", "gloss": "his father", "ans": {"kind": "five", "sign": "waw"},
                 "why": "{أَبٌ} with an owner ({ـهُ}): a five noun. Wāw."},
                {"s": "المُعَلِّمُونَ", "gloss": "the teachers", "ans": {"kind": "smp", "sign": "waw"},
                 "why": "{مُعَلِّمٌ} + {ـُونَ}: a sound m. plural. Wāw."},
                {"s": "النَّادِي", "gloss": "the club", "ans": {"kind": "hidv", "sign": "hid"},
                 "why": "Manqūṣ: hidden damma."},
                {"s": "السَّاعَاتُ", "gloss": "the watches", "ans": {"kind": "sfp", "sign": "dam"},
                 "why": "{سَاعَةٌ} → {سَاعَاتٌ}: a sound f. plural. Damma."},
                {"s": "الفَتَى", "gloss": "the young man", "ans": {"kind": "hidv", "sign": "hid"},
                 "why": "Maqṣūr: hidden damma."},
            ],
        },
        {
            "title": "Which form is right in rafʿ?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "___ صَادِقُونَ.", "gloss": "The Muslims are truthful.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("المُسْلِمِينَ", "المُسْلِمُونَ", "المُسْلِمُونِ")},
                 "why": "Topic, sound m. plural: wāw. The {ن} has fatha: {ـُونَ}."},
                {"s": "___ نَظِيفَتَانِ.", "gloss": "The two rooms are clean.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الغُرْفَتَيْنِ", "الغُرْفَتَانُ", "الغُرْفَتَانِ")},
                 "why": "Topic, dual: alif. The {ن} has kasra: {ـَانِ}."},
                {"s": "___ تَاجِرٌ.", "gloss": "Zayd's brother is a merchant.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَخُو زَيْدٍ", "أَخَا زَيْدٍ", "أَخِي زَيْدٍ")},
                 "why": "Topic, a five noun: wāw. {أَخُو زَيْدٍ}."},
                {"s": "___ فِي البَيْتِ.", "gloss": "Fatima is in the house.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("فَاطِمَةٌ", "فَاطِمَةُ", "فَاطِمَةَ")},
                 "why": "Topic, a diptote: one damma, no tanween."},
                {"s": "___ حَاضِرُونَ.", "gloss": "The school's teachers are present.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُعَلِّمُونَ المَدْرَسَةِ", "مُعَلِّمُو المَدْرَسَةِ", "مُعَلِّمِي المَدْرَسَةِ")},
                 "why": "Sound m. plural in rafʿ: wāw. With an owner the {ن} drops: {مُعَلِّمُو}."},
                {"s": "___ جَدِيدَانِ.", "gloss": "The student's two books are new.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("كِتَابَانِ الطَّالِبِ", "كِتَابَيِ الطَّالِبِ", "كِتَابَا الطَّالِبِ")},
                 "why": "Dual in rafʿ: alif. With an owner the {ن} drops: {كِتَابَا}."},
            ],
        },
        {
            "title": "Iʿrāb: job and sign",
            "prompt": "خَرَجَ الطَّالِبَانِ وَأَبُوهُمَا مِنَ البَيْتِ.",
            "en": "The two students and their father went out of the house.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, AND]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, FIXED]},
            ],
            "rows": [
                {"s": "خَرَجَ", "gloss": "went out", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha. It stays singular before a dual doer."},
                {"s": "الطَّالِبَانِ", "gloss": "the two students", "ans": {"job": "doer", "sign": "alif"},
                 "why": "{فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الأَلِفُ لِأَنَّهُ مُثَنًّى}."},
                {"s": "أَبُوهُمَا", "gloss": "their father", "ans": {"job": "and", "sign": "waw"},
                 "why": "After {وَ} it copies the doer's rafʿ. A five noun: wāw."},
            ],
        },
        {
            "title": "Topic or Information? Which sign?",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, INFO]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW, HID, FIXED]},
            ],
            "rows": [
                {"s": "[البَيْتَانِ] كَبِيرَانِ.", "gloss": "the two houses", "ans": {"job": "topic", "sign": "alif"},
                 "why": "A dual Topic: rafʿ with alif."},
                {"s": "هَذَانِ [كِتَابَانِ].", "gloss": "two books", "ans": {"job": "info", "sign": "alif"},
                 "why": "Information, a dual: alif."},
                {"s": "[هِيَ] طَبِيبَةٌ.", "gloss": "she", "ans": {"job": "topic", "sign": "fixed"},
                 "why": "A fixed pronoun as Topic: in the place of rafʿ."},
                {"s": "هَذَا [مُوسَى].", "gloss": "Musa", "ans": {"job": "info", "sign": "hid"},
                 "why": "Information. It ends in alif: hidden damma."},
                {"s": "[الَّذِي] فِي البَيْتِ أَخِي.", "gloss": "the one who", "ans": {"job": "topic", "sign": "fixed"},
                 "why": "{الَّذِي} is a fixed relative word. Here it is the Topic, in the place of rafʿ."},
                {"s": "الَّذِي فِي البَيْتِ [أَخِي].", "gloss": "my brother", "ans": {"job": "info", "sign": "hid"},
                 "why": "Information. With {ـي} \"my\" the five noun takes no wāw: hidden damma."},
            ],
        },
        {
            "title": "Damma that shows, or hidden damma?",
            "fields": [{"key": "sign", "label": "Sign", "options": [DAM, HID]}],
            "rows": [
                {"s": "[الوَادِي] وَاسِعٌ.", "gloss": "the valley", "ans": {"sign": "hid"},
                 "why": "Manqūṣ: hidden damma on the {ي}."},
                {"s": "[المَاءُ] بَارِدٌ.", "gloss": "the water", "ans": {"sign": "dam"},
                 "why": "The hamza carries the damma: {المَاءُ}."},
                {"s": "[العَصَا] طَوِيلَةٌ.", "gloss": "the stick", "ans": {"sign": "hid"},
                 "why": "Maqṣūr: ends in alif. Hidden damma."},
                {"s": "[أَبِي] طَبِيبٌ.", "gloss": "my father", "ans": {"sign": "hid"},
                 "why": "With {ـي} \"my\" the damma is hidden. It is not {أَبُو}."},
                {"s": "[عَلِيٌّ] مُهَنْدِسٌ.", "gloss": "Ali", "ans": {"sign": "dam"},
                 "why": "The {ي} has shadda and carries the damma: {عَلِيٌّ}."},
                {"s": "[الدُّنْيَا] جَمِيلَةٌ.", "gloss": "the world", "ans": {"sign": "hid"},
                 "why": "Maqṣūr: ends in alif. Hidden damma."},
            ],
        },
    ],
}
