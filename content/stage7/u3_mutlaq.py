# Stage 7, Unit 3: The verb's own noun (الْمَفْعُولُ الْمُطْلَقُ)

# Canonical options (STAGES_5_8_SPEC.md), copied exactly.
DAM = {"k": "dam", "label": "Damma · ضَمَّةٌ", "color": "red"}
FAT = {"k": "fat", "label": "Fatha · فَتْحَةٌ", "color": "pink"}
KAS = {"k": "kas", "label": "Kasra · كَسْرَةٌ", "color": "green"}
WAW = {"k": "waw", "label": "Wāw · الوَاوُ", "color": "blue"}
YA = {"k": "ya", "label": "Yāʾ · اليَاءُ", "color": "purple"}
HID = {"k": "hid", "label": "Hidden vowel · مُقَدَّرَةٌ", "color": "brown"}

DOER = {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"}
OBJ = {"k": "obj", "label": "Object · مَفْعُولٌ بِهِ", "color": "pink"}
MUTL = {"k": "mutl", "label": "Verb's own noun · مَفْعُولٌ مُطْلَقٌ", "color": "purple"}
PURP = {"k": "purp", "label": "Purpose · مَفْعُولٌ لِأَجْلِهِ", "color": "teal"}
STATE = {"k": "state", "label": "State · حَالٌ", "color": "olive"}
PREP = {"k": "prep", "label": "After a preposition · اِسْمٌ مَجْرُورٌ", "color": "green"}
ADJ = {"k": "adj", "label": "Adjective · نَعْتٌ", "color": "grey"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}

# Unit-specific: the three uses of the mafʿūl muṭlaq.
EMPH = {"k": "emph", "label": "Emphasis · لِلتَّأْكِيدِ", "color": "grey"}
TYPE = {"k": "type", "label": "Kind · لِبَيَانِ النَّوْعِ", "color": "navy"}
NUM = {"k": "num", "label": "Number · لِبَيَانِ العَدَدِ", "color": "teal"}
USES = [EMPH, TYPE, NUM]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s7-mutlaq",
    "order": 3,
    "title": "The verb's own noun",
    "ar": "الْمَفْعُولُ الْمُطْلَقُ",
    "blurb": "A verb followed by its own maṣdar: جَلَسْتُ جُلُوسًا. It stresses the action, says what kind it was, or counts it.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 7 · UNIT 3", "title": "The verb repeats itself",
         "text": "Sometimes a verb is followed by a noun made from the same verb: {جَلَسْتُ جُلُوسًا}. This noun is the verb's own noun, {المَفْعُولُ المُطْلَقُ}. It is in naṣb.",
         "wm": "المَفْعُولُ المُطْلَقُ"},

        {"t": "h2", "text": "The maṣdar of the same verb"},
        {"t": "p", "text": "Every verb has a noun that names the action. It is called the maṣdar ({المَصْدَرُ}). The maṣdar of {جَلَسَ} \"he sat\" is {جُلُوسٌ} \"sitting\"."},
        {"t": "table", "head": ["Verb", "Maṣdar", "Meaning"], "rows": [
            ["جَلَسَ", "جُلُوسٌ", "sitting"],
            ["فَرِحَ", "فَرَحٌ", "joy"],
            ["نَامَ", "نَوْمٌ", "sleep"],
            ["فَهِمَ", "فَهْمٌ", "understanding"],
            ["قَرَأَ", "قِرَاءَةٌ", "reading"],
            ["خَرَجَ", "خُرُوجٌ", "going out"],
            ["صَبَرَ", "صَبْرٌ", "patience"],
            ["اِحْتَرَمَ", "اِحْتِرَامٌ", "respect"],
            ["اِجْتَهَدَ", "اِجْتِهَادٌ", "hard work"],
        ]},
        {"t": "rule", "color": "purple", "title": "The verb's own noun",
         "text": "A maṣdar of the same verb, after that verb, is {مَفْعُولٌ مُطْلَقٌ}. It is always in naṣb."},
        {"t": "examples", "items": [
            {"ar": "جَلَسْتُ جُلُوسًا.", "en": "I really sat down.", "note": "{جُلُوسًا} comes from {جَلَسَ}."},
            {"ar": "فَهِمْتُ الدَّرْسَ فَهْمًا جَيِّدًا.", "en": "I understood the lesson well.", "note": "{الدَّرْسَ} is the object. {فَهْمًا} is the verb's own noun."},
        ]},

        {"t": "h2", "text": "Three uses"},
        {"t": "cols", "items": [
            {"color": "grey", "title": "Emphasis", "ar": "لِلتَّأْكِيدِ", "text": "The maṣdar alone: {نَامَ نَوْمًا}"},
            {"color": "navy", "title": "Kind", "ar": "لِبَيَانِ النَّوْعِ", "text": "With an adjective or an owner: {نَامَ نَوْمًا هَادِئًا}"},
            {"color": "teal", "title": "Number", "ar": "لِبَيَانِ العَدَدِ", "text": "How many times: {سَجَدَ سَجْدَتَيْنِ}"},
        ]},
        {"t": "p", "text": "1. Emphasis. The maṣdar stands alone. It makes the action strong and sure."},
        {"t": "examples", "items": [
            {"ar": "وَكَلَّمَ اللّٰهُ مُوسَى تَكْلِيمًا.", "en": "And Allah spoke to Musa directly. (an-Nisāʾ 4:164)",
             "note": "{تَكْلِيمًا} is the maṣdar of {كَلَّمَ}. {مُوسَى} is the object with a hidden fatha."},
        ]},
        {"t": "p", "text": "2. Kind. An adjective or an owner after the maṣdar tells us what kind of action it was."},
        {"t": "examples", "items": [
            {"ar": "فَرِحَ الطَّالِبُ فَرَحًا كَبِيرًا.", "en": "The student was very happy.", "note": "With an adjective: {كَبِيرًا}."},
            {"ar": "فَاصْبِرْ صَبْرًا جَمِيلًا.", "en": "So be patient with a beautiful patience. (al-Maʿārij 70:5)", "note": "An order verb. With an adjective: {جَمِيلًا}."},
            {"ar": "مَشَى الوَلَدُ مَشْيَ الأَسَدِ.", "en": "The boy walked like a lion.", "note": "With an owner: {الأَسَدِ}. An owned maṣdar has no tanween."},
        ]},
        {"t": "p", "text": "3. Number. The maṣdar counts the action. Arabic has a \"one time\" shape on the pattern {فَعْلَةٌ}: {سَجْدَةٌ} \"one prostration\", {دَقَّةٌ} \"one knock\", {نَظْرَةٌ} \"one look\". It can be dual or plural."},
        {"t": "examples", "items": [
            {"ar": "سَجَدْتُ سَجْدَةً.", "en": "I prostrated once."},
            {"ar": "سَجَدَ المُصَلِّي سَجْدَتَيْنِ.", "en": "The one praying prostrated twice."},
            {"ar": "دَقَّ الضَّيْفُ البَابَ دَقَّاتٍ.", "en": "The guest knocked on the door several times."},
        ]},
        {"t": "tip", "text": "{سَجْدَةً} alone still counts: it means one time. The plain maṣdar of {سَجَدَ} is {سُجُودٌ}."},

        {"t": "h2", "text": "Its signs"},
        {"t": "p", "text": "The verb's own noun follows the signs of naṣb from Unit 1. Most of the time it is singular, with fatha. When it counts, it can be a dual or a sound f. plural."},
        {"t": "table", "head": ["Example", "Use", "Group", "Sign"], "rows": [
            ["جَلَسْتُ جُلُوسًا.", "Emphasis", "Singular", "Fatha"],
            ["مَشَى مَشْيَ الأَسَدِ.", "Kind", "Singular, owned", "Fatha, no tanween"],
            ["سَجَدَ سَجْدَتَيْنِ.", "Number", "Dual", "Yāʾ"],
            ["دَقَّ البَابَ دَقَّاتٍ.", "Number", "Sound f. plural", "Kasra in place of fatha"],
        ]},

        {"t": "h2", "text": "The full iʿrāb"},
        {"t": "examples", "items": [
            {"ar": "جَلَسْتُ جُلُوسًا.", "en": "I really sat down.",
             "note": "{جُلُوسًا}: {مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}."},
            {"ar": "سَجَدَ المُصَلِّي سَجْدَتَيْنِ.", "en": "The one praying prostrated twice.",
             "note": "{سَجْدَتَيْنِ}: {مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ اليَاءُ لِأَنَّهُ مُثَنًّى}. {المُصَلِّي} is the doer with a hidden damma."},
            {"ar": "دَقَّ الضَّيْفُ البَابَ دَقَّاتٍ.", "en": "The guest knocked on the door several times.",
             "note": "{دَقَّاتٍ}: {مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الكَسْرَةُ نِيَابَةً عَنِ الفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ}."},
        ]},

        {"t": "h2", "text": "Object or verb's own noun?"},
        {"t": "p", "text": "Both are in naṣb, so ask one question: is this noun the maṣdar of the same verb?"},
        {"t": "table", "head": ["Sentence", "The naṣb noun", "Why"], "rows": [
            ["فَهِمْتُ الدَّرْسَ.", "Object", "{الدَّرْسُ} is the thing understood."],
            ["فَهِمْتُ فَهْمًا.", "Verb's own noun", "{فَهْمٌ} is the maṣdar of {فَهِمَ}."],
            ["أَحْبَبْتُ القِرَاءَةَ.", "Object", "{القِرَاءَةُ} is the maṣdar of another verb. It is the thing I loved."],
            ["قَرَأْتُ قِرَاءَةً جَيِّدَةً.", "Verb's own noun", "{قِرَاءَةٌ} is the maṣdar of {قَرَأَ}."],
        ]},
        {"t": "tip", "text": "A maṣdar of another verb can be the purpose. {قُمْتُ احْتِرَامًا لِلْمُعَلِّمِ}: {احْتِرَامًا} answers \"why did you stand?\" (Unit 4). Compare {قُمْتُ قِيَامًا}: same verb, so it is the verb's own noun."},
        {"t": "tip", "text": "A maṣdar after a preposition is jarr:{فَرِحْتُ بِالنَّجَاحِ} \"I was happy with the success\"."},

        {"t": "summary", "title": "In short", "items": [
            "The verb's own noun is the maṣdar of the same verb: {جَلَسْتُ جُلُوسًا}. It is in naṣb.",
            "Emphasis: the maṣdar alone. Kind: with an adjective or an owner. Number: how many times, often {فَعْلَةٌ}.",
            "Signs: usually fatha. Dual: yāʾ ({سَجْدَتَيْنِ}). Sound f. plural: kasra ({دَقَّاتٍ}).",
            "Object or verb's own noun? Check if it is the maṣdar of the same verb.",
            "Full iʿrāb: {مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Find the verb's own noun",
            "fields": [{"key": "pick", "label": "Word", "options": []}],
            "rows": [
                {"s": "جَلَسَ الضَّيْفُ جُلُوسًا.", "gloss": "The guest sat down.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الضَّيْفُ", "جُلُوسًا", "جَلَسَ")},
                 "why": "{جُلُوسًا} is the maṣdar of {جَلَسَ}."},
                {"s": "فَرِحَ الطَّالِبُ فَرَحًا كَبِيرًا.", "gloss": "The student was very happy.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فَرَحًا", "كَبِيرًا", "الطَّالِبُ")},
                 "why": "{فَرَحًا} comes from {فَرِحَ}. {كَبِيرًا} is its adjective."},
                {"s": "سَجَدَ المُصَلِّي سَجْدَتَيْنِ.", "gloss": "The one praying prostrated twice.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("سَجَدَ", "المُصَلِّي", "سَجْدَتَيْنِ")},
                 "why": "{سَجْدَتَيْنِ} comes from {سَجَدَ} and counts the action."},
                {"s": "نَامَ الطِّفْلُ نَوْمًا هَادِئًا.", "gloss": "The child slept a calm sleep.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الطِّفْلُ", "نَوْمًا", "هَادِئًا")},
                 "why": "{نَوْمًا} is the maṣdar of {نَامَ}."},
                {"s": "فَهِمْتُ الدَّرْسَ فَهْمًا جَيِّدًا.", "gloss": "I understood the lesson well.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الدَّرْسَ", "جَيِّدًا", "فَهْمًا")},
                 "why": "{فَهْمًا} comes from {فَهِمَ}. {الدَّرْسَ} is the object."},
                {"s": "اِحْتَرَمَ الطُّلَّابُ المُعَلِّمَ احْتِرَامًا.", "gloss": "The students truly respected the teacher.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("احْتِرَامًا", "المُعَلِّمَ", "الطُّلَّابُ")},
                 "why": "{احْتِرَامًا} is the maṣdar of {اِحْتَرَمَ}."},
            ],
        },
        {
            "title": "Which use?",
            "fields": [{"key": "use", "label": "Use", "options": USES}],
            "rows": [
                {"s": "جَلَسْتُ [جُلُوسًا]", "gloss": "I really sat down.", "ans": {"use": "emph"},
                 "why": "The maṣdar alone, with no adjective, owner or count: emphasis."},
                {"s": "فَرِحَ الوَلَدُ [فَرَحًا كَبِيرًا]", "gloss": "The boy was very happy.", "ans": {"use": "type"},
                 "why": "The adjective {كَبِيرًا} tells what kind of joy."},
                {"s": "دَقَّ الضَّيْفُ البَابَ [دَقَّتَيْنِ]", "gloss": "The guest knocked on the door twice.", "ans": {"use": "num"},
                 "why": "A dual of {دَقَّةٌ} \"one knock\": it counts."},
                {"s": "مَشَى الجُنْدِيُّ [مَشْيَ الأَسَدِ]", "gloss": "The soldier walked like a lion.", "ans": {"use": "type"},
                 "why": "The owner {الأَسَدِ} tells what kind of walking."},
                {"s": "قُمْتُ [قِيَامًا]", "gloss": "I really stood up.", "ans": {"use": "emph"},
                 "why": "{قِيَامًا} alone: emphasis."},
                {"s": "سَجَدْتُ [سَجْدَةً]", "gloss": "I prostrated once.", "ans": {"use": "num"},
                 "why": "{سَجْدَةٌ} is the \"one time\" shape: it counts one."},
            ],
        },
        {
            "title": "Which sign?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, YA, KAS, HID]}],
            "rows": [
                {"s": "سَجَدَ المُصَلِّي [سَجْدَتَيْنِ]", "gloss": "The one praying prostrated twice.", "ans": {"sign": "ya"},
                 "why": "A dual in naṣb: yāʾ."},
                {"s": "دَقَّ الرَّجُلُ البَابَ [دَقَّاتٍ]", "gloss": "The man knocked on the door several times.", "ans": {"sign": "kas"},
                 "why": "{دَقَّاتٌ} is a sound f. plural: kasra in place of fatha."},
                {"s": "فَرِحْتُ [فَرَحًا] كَبِيرًا", "gloss": "I was very happy.", "ans": {"sign": "fat"},
                 "why": "A singular: fatha with tanween."},
                {"s": "قَرَأْتُ الدَّرْسَ [قِرَاءَتَيْنِ]", "gloss": "I read the lesson twice.", "ans": {"sign": "ya"},
                 "why": "A dual: yāʾ."},
                {"s": "نَظَرْتُ إِلَيْهِ [نَظْرَةً]", "gloss": "I looked at him once.", "ans": {"sign": "fat"},
                 "why": "A singular: fatha."},
                {"s": "جَلَسْتُ [جُلُوسَ] المُعَلِّمِ", "gloss": "I sat the way the teacher sits.", "ans": {"sign": "fat"},
                 "why": "Owned, so no tanween. Still a singular: fatha."},
            ],
        },
        {
            "title": "Object or verb's own noun?",
            "fields": [{"key": "job", "label": "Job", "options": [OBJ, MUTL]}],
            "rows": [
                {"s": "فَهِمْتُ [الدَّرْسَ]", "gloss": "I understood the lesson.", "ans": {"job": "obj"},
                 "why": "{الدَّرْسُ} is the thing understood. It is not the maṣdar of {فَهِمَ}."},
                {"s": "فَهِمْتُ الدَّرْسَ [فَهْمًا]", "gloss": "I truly understood the lesson.", "ans": {"job": "mutl"},
                 "why": "{فَهْمٌ} is the maṣdar of {فَهِمَ}."},
                {"s": "أَحْبَبْتُ [القِرَاءَةَ]", "gloss": "I loved reading.", "ans": {"job": "obj"},
                 "why": "A maṣdar, but of another verb ({قَرَأَ}). It is the thing loved."},
                {"s": "قَرَأْتُ [قِرَاءَةً] جَيِّدَةً", "gloss": "I read well.", "ans": {"job": "mutl"},
                 "why": "{قِرَاءَةٌ} is the maṣdar of {قَرَأَ}, the same verb."},
                {"s": "حَفِظْتُ [القُرْآنَ]", "gloss": "I memorised the Qurʾan.", "ans": {"job": "obj"},
                 "why": "What did I memorise? The Qurʾan. Object."},
                {"s": "حَفِظْتُ القُرْآنَ [حِفْظًا] جَيِّدًا", "gloss": "I memorised the Qurʾan well.", "ans": {"job": "mutl"},
                 "why": "{حِفْظٌ} is the maṣdar of {حَفِظَ}."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "فَرِحَ المُسْلِمُونَ بِالعِيدِ فَرَحًا كَبِيرًا.",
            "en": "The Muslims were very happy with the Eid.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, PREP, MUTL, ADJ, OBJ]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, WAW, YA]},
            ],
            "rows": [
                {"s": "المُسْلِمُونَ", "gloss": "the Muslims", "ans": {"job": "doer", "sign": "waw"},
                 "why": "Doer, rafʿ. Sound m. plural: wāw."},
                {"s": "العِيدِ", "gloss": "the Eid", "ans": {"job": "prep", "sign": "kas"},
                 "why": "After {بِـ}, jarr. Kasra."},
                {"s": "فَرَحًا", "gloss": "joy", "ans": {"job": "mutl", "sign": "fat"},
                 "why": "The maṣdar of {فَرِحَ}: verb's own noun, naṣb, fatha."},
                {"s": "كَبِيرًا", "gloss": "big", "ans": {"job": "adj", "sign": "fat"},
                 "why": "Adjective of {فَرَحًا}. It copies its naṣb: fatha."},
            ],
        },
        {
            "title": "Choose the right form",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "سَجَدَ المُصَلِّي ___", "gloss": "two prostrations", "ans": {"pick": "b"},
                 "opts": {"pick": pick("سَجْدَتَانِ", "سَجْدَتَيْنِ", "سَجَدَاتٍ")},
                 "why": "Naṣb dual: {سَجْدَتَيْنِ}. {سَجْدَتَانِ} is rafʿ. {سَجَدَاتٍ} is three or more."},
                {"s": "دَقَّ الضَّيْفُ البَابَ ___", "gloss": "several knocks", "ans": {"pick": "c"},
                 "opts": {"pick": pick("دَقَّاتٌ", "دَقَّاتًا", "دَقَّاتٍ")},
                 "why": "Sound f. plural in naṣb: kasra with tanween."},
                {"s": "فَرِحَ الوَلَدُ ___ كَبِيرًا", "gloss": "joy", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فَرَحًا", "فَرَحٌ", "فَرَحٍ")},
                 "why": "Verb's own noun, naṣb: fatha with tanween."},
                {"s": "سَارَ الجُنْدِيُّ ___ الأَبْطَالِ", "gloss": "the way heroes march", "ans": {"pick": "b"},
                 "opts": {"pick": pick("سَيْرُ", "سَيْرَ", "سَيْرًا")},
                 "why": "Naṣb, and owned by {الأَبْطَالِ}: fatha, no tanween."},
                {"s": "اِجْتَهَدَ الطُّلَّابُ ___", "gloss": "hard work (emphasis)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("اجْتِهَادًا", "اجْتِهَادٌ", "اجْتِهَادٍ")},
                 "why": "Naṣb: fatha with tanween."},
                {"s": "قَفَزَ الوَلَدُ ___", "gloss": "one jump", "ans": {"pick": "c"},
                 "opts": {"pick": pick("قَفْزَةٌ", "قَفْزَةٍ", "قَفْزَةً")},
                 "why": "The \"one time\" shape of {قَفَزَ}, in naṣb: {قَفْزَةً}."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Find the verb's own noun",
            "fields": [{"key": "pick", "label": "Word", "options": []}],
            "rows": [
                {"s": "اِحْتَرَمْتُ أَبَاكَ احْتِرَامًا عَظِيمًا.", "gloss": "I respected your father greatly.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَبَاكَ", "احْتِرَامًا", "عَظِيمًا")},
                 "why": "{احْتِرَامًا} is the maṣdar of {اِحْتَرَمَ}. {أَبَاكَ} is the object."},
                {"s": "فَرِحَتِ البَنَاتُ فَرَحَ الأَطْفَالِ.", "gloss": "The girls were happy like children.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("البَنَاتُ", "فَرَحَ", "الأَطْفَالِ")},
                 "why": "{فَرَحَ} is the maṣdar of {فَرِحَ}, owned by {الأَطْفَالِ}."},
                {"s": "صَبَرَ المُؤْمِنُونَ صَبْرًا جَمِيلًا.", "gloss": "The believers were beautifully patient.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("صَبْرًا", "جَمِيلًا", "المُؤْمِنُونَ")},
                 "why": "{صَبْرًا} is the maṣdar of {صَبَرَ}."},
                {"s": "قَرَأَ القَارِئُ السُّورَةَ قِرَاءَتَيْنِ.", "gloss": "The reciter read the sūra twice.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("القَارِئُ", "السُّورَةَ", "قِرَاءَتَيْنِ")},
                 "why": "{قِرَاءَتَيْنِ} comes from {قَرَأَ}. {القَارِئُ} is the doer and {السُّورَةَ} the object."},
                {"s": "زَارَ الطَّبِيبُ المَرِيضَ زِيَارَتَيْنِ.", "gloss": "The doctor visited the patient twice.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("زِيَارَتَيْنِ", "المَرِيضَ", "الطَّبِيبُ")},
                 "why": "{زِيَارَتَيْنِ} comes from {زَارَ}. {المَرِيضَ} is the object."},
                {"s": "خَرَجَ الطُّلَّابُ مِنَ الفَصْلِ خُرُوجًا سَرِيعًا.", "gloss": "The students left the classroom quickly.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الطُّلَّابُ", "الفَصْلِ", "خُرُوجًا")},
                 "why": "{خُرُوجًا} is the maṣdar of {خَرَجَ}."},
            ],
        },
        {
            "title": "Which use?",
            "fields": [{"key": "use", "label": "Use", "options": USES}],
            "rows": [
                {"s": "صَبَرْتُ [صَبْرًا جَمِيلًا]", "gloss": "I was beautifully patient.", "ans": {"use": "type"},
                 "why": "The adjective {جَمِيلًا} gives the kind of patience."},
                {"s": "زُرْتُ المَرِيضَ [زِيَارَتَيْنِ]", "gloss": "I visited the patient twice.", "ans": {"use": "num"},
                 "why": "A dual: it counts two visits."},
                {"s": "اِجْتَهَدَ الطَّالِبُ [اجْتِهَادًا]", "gloss": "The student truly worked hard.", "ans": {"use": "emph"},
                 "why": "The maṣdar alone: emphasis."},
                {"s": "عَمِلَ المُهَنْدِسُ [عَمَلَ المَاهِرِينَ]", "gloss": "The engineer worked like skilled people.", "ans": {"use": "type"},
                 "why": "The owner {المَاهِرِينَ} gives the kind of work."},
                {"s": "نَظَرَ المُعَلِّمُ إِلَى الطَّالِبِ [نَظْرَتَيْنِ]", "gloss": "The teacher looked at the student twice.", "ans": {"use": "num"},
                 "why": "The dual of {نَظْرَةٌ} \"one look\": it counts."},
                {"s": "خَرَجَ الضَّيْفُ [خُرُوجًا]", "gloss": "The guest really left.", "ans": {"use": "emph"},
                 "why": "{خُرُوجًا} alone: emphasis."},
            ],
        },
        {
            "title": "Which sign?",
            "fields": [{"key": "sign", "label": "Sign", "options": [FAT, YA, KAS, HID]}],
            "rows": [
                {"s": "زَارَ الطَّبِيبُ المَرِيضَ [زِيَارَاتٍ] كَثِيرَةً", "gloss": "The doctor visited the patient many times.", "ans": {"sign": "kas"},
                 "why": "{زِيَارَاتٌ} is a sound f. plural: kasra in place of fatha."},
                {"s": "ضَرَبَ الحَارِسُ الجَرَسَ [ضَرْبَتَيْنِ]", "gloss": "The guard struck the bell twice.", "ans": {"sign": "ya"},
                 "why": "A dual in naṣb: yāʾ."},
                {"s": "مَشَى الشَّيْخُ [مَشْيًا] بَطِيئًا", "gloss": "The old man walked slowly.", "ans": {"sign": "fat"},
                 "why": "A singular: fatha."},
                {"s": "دَعَوْتُ اللّٰهَ [دُعَاءً] طَوِيلًا", "gloss": "I made a long prayer to Allah.", "ans": {"sign": "fat"},
                 "why": "{دُعَاءٌ} ends in {ـَاءٌ}. Nothing is hidden: fatha."},
                {"s": "جَلَسْنَا مَعَ المُعَلِّمِ [جَلَسَاتٍ]", "gloss": "We sat with the teacher several times.", "ans": {"sign": "kas"},
                 "why": "{جَلَسَاتٌ}, plural of {جَلْسَةٌ}: a sound f. plural. Kasra."},
                {"s": "اِحْتَرَمْتُ أَبَاكَ [احْتِرَامَ] الأَبْنَاءِ", "gloss": "I respected your father as sons do.", "ans": {"sign": "fat"},
                 "why": "Owned by {الأَبْنَاءِ}: no tanween, fatha."},
            ],
        },
        {
            "title": "Which naṣb job?",
            "fields": [{"key": "job", "label": "Job", "options": [OBJ, MUTL, PURP, STATE]}],
            "rows": [
                {"s": "دَعَوْتُ [اللّٰهَ]", "gloss": "I called on Allah.", "ans": {"job": "obj"},
                 "why": "Whom did I call on? Object."},
                {"s": "قُمْتُ [احْتِرَامًا] لِلْمُعَلِّمِ", "gloss": "I stood up out of respect for the teacher.", "ans": {"job": "purp"},
                 "why": "A maṣdar of another verb. It answers \"why?\": purpose."},
                {"s": "قُمْتُ [قِيَامًا] طَوِيلًا", "gloss": "I stood for a long time.", "ans": {"job": "mutl"},
                 "why": "{قِيَامٌ} is the maṣdar of {قَامَ}, the same verb."},
                {"s": "جَاءَ الطَّالِبُ [مُسْرِعًا]", "gloss": "The student came hurrying.", "ans": {"job": "state"},
                 "why": "Not a maṣdar. It tells how he came: state."},
                {"s": "كَتَبْتُ [رِسَالَةً]", "gloss": "I wrote a letter.", "ans": {"job": "obj"},
                 "why": "{رِسَالَةٌ} is the thing written. It is not the maṣdar of {كَتَبَ}."},
                {"s": "أَسْرَعَ الطَّالِبُ [إِسْرَاعًا]", "gloss": "The student really hurried.", "ans": {"job": "mutl"},
                 "why": "{إِسْرَاعٌ} is the maṣdar of {أَسْرَعَ}."},
            ],
        },
        {
            "title": "Job and sign",
            "prompt": "شَكَرَ المُدِيرُ المُهَنْدِسَاتِ شُكْرًا كَثِيرًا.",
            "en": "The manager thanked the female engineers very much.",
            "fields": [
                {"key": "job", "label": "Job", "options": [DOER, OBJ, MUTL, ADJ]},
                {"key": "sign", "label": "Sign", "options": [DAM, FAT, KAS, YA]},
            ],
            "rows": [
                {"s": "المُدِيرُ", "gloss": "the manager", "ans": {"job": "doer", "sign": "dam"},
                 "why": "Doer, rafʿ. Singular: damma."},
                {"s": "المُهَنْدِسَاتِ", "gloss": "the female engineers", "ans": {"job": "obj", "sign": "kas"},
                 "why": "Object, naṣb. Sound f. plural: kasra in place of fatha."},
                {"s": "شُكْرًا", "gloss": "thanks", "ans": {"job": "mutl", "sign": "fat"},
                 "why": "The maṣdar of {شَكَرَ}: verb's own noun, fatha."},
                {"s": "كَثِيرًا", "gloss": "much", "ans": {"job": "adj", "sign": "fat"},
                 "why": "Adjective of {شُكْرًا}: naṣb, fatha."},
            ],
        },
        {
            "title": "Choose the right form",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "طَرَقَ الضَّيْفُ البَابَ ___", "gloss": "two knocks", "ans": {"pick": "b"},
                 "opts": {"pick": pick("طَرْقَتَانِ", "طَرْقَتَيْنِ", "طَرَقَاتٍ")},
                 "why": "Dual in naṣb: {طَرْقَتَيْنِ}. {طَرَقَاتٍ} is three or more."},
                {"s": "ضَحِكَ الأَطْفَالُ ___", "gloss": "several laughs", "ans": {"pick": "a"},
                 "opts": {"pick": pick("ضَحَكَاتٍ", "ضَحَكَاتًا", "ضَحَكَاتُ")},
                 "why": "Sound f. plural in naṣb: kasra with tanween."},
                {"s": "صَبَرَ المُسْلِمُونَ ___ جَمِيلًا", "gloss": "patience", "ans": {"pick": "c"},
                 "opts": {"pick": pick("صَبْرٌ", "صَبْرٍ", "صَبْرًا")},
                 "why": "Verb's own noun, naṣb: fatha with tanween."},
                {"s": "مَشَى الطِّفْلُ ___ الشُّيُوخِ", "gloss": "the way old men walk", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَشْيًا", "مَشْيَ", "مَشْيُ")},
                 "why": "Naṣb, and owned by {الشُّيُوخِ}: fatha, no tanween."},
                {"s": "اِجْتَهَدَتِ الطَّالِبَاتُ ___ كَبِيرًا", "gloss": "hard work", "ans": {"pick": "a"},
                 "opts": {"pick": pick("اجْتِهَادًا", "اجْتِهَادٍ", "اجْتِهَادَاتٍ")},
                 "why": "One maṣdar with its adjective {كَبِيرًا}: {اجْتِهَادًا}."},
            ],
        },
    ],
}
