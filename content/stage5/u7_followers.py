# Stage 5, Unit 7: Followers in rafʿ (التَّوَابِعُ)

# Canonical options (copied from STAGES_5_8_SPEC.md)
DAM = {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
ALIF = {"k": "alif",  "label": "Alif · الأَلِفُ",                  "color": "teal"}
WAW = {"k": "waw",   "label": "Wāw · الوَاوُ",                   "color": "blue"}
HID = {"k": "hid",   "label": "Hidden vowel · مُقَدَّرَةٌ",         "color": "brown"}
FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ",                  "color": "grey"}

TOPIC = {"k": "topic", "label": "Topic · مُبْتَدَأٌ",                  "color": "gold"}
INFO = {"k": "info",  "label": "Information · خَبَرٌ",                "color": "red"}
VERB = {"k": "verb",  "label": "Verb · فِعْلٌ",                       "color": "navy"}
DOER = {"k": "doer",  "label": "Doer · فَاعِلٌ",                      "color": "orange"}
KISM = {"k": "kism",  "label": "Kāna's noun · اِسْمُ كَانَ",             "color": "gold"}
ADJ = {"k": "adj",   "label": "Adjective · نَعْتٌ",                   "color": "grey"}
AND = {"k": "and",   "label": "After وَ (and) · مَعْطُوفٌ",              "color": "blue"}
TAWK = {"k": "tawk",  "label": "Emphasis · تَوْكِيدٌ",                  "color": "grey"}
BADAL = {"k": "badal", "label": "Substitute · بَدَلٌ",                   "color": "grey"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s5-followers",
    "order": 7,
    "title": "Followers in rafʿ",
    "ar": "التَّوَابِعُ",
    "blurb": "Adjective, words after وَ, emphasis and substitute: they copy the case of the word before them. Their own group gives the sign.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 5 · UNIT 7", "title": "Words that follow",
         "text": "Some words have no job of their own. They follow the word before them and copy its case. They are called followers ({التَّوَابِعُ}).",
         "wm": "التَّوَابِعُ"},

        {"t": "h2", "text": "Four followers"},
        {"t": "p", "text": "You met two of them in Stage 1: the adjective and the word after {وَ}. Now add two more."},
        {"t": "cols", "items": [
            {"color": "grey", "title": "Adjective", "ar": "نَعْتٌ", "text": "Describes: {جَاءَ الرَّجُلُ الكَرِيمُ}."},
            {"color": "blue", "title": "After وَ", "ar": "مَعْطُوفٌ", "text": "Joined by {وَ}، {ثُمَّ}، {أَوْ}: {جَاءَ خَالِدٌ وَأَخُوهُ}."},
            {"color": "grey", "title": "Emphasis", "ar": "تَوْكِيدٌ", "text": "Makes it strong: {جَاءَ المُدِيرُ نَفْسُهُ}."},
            {"color": "grey", "title": "Substitute", "ar": "بَدَلٌ", "text": "Names the same person again: {جَاءَ أَخُوكَ زَيْدٌ}."},
        ]},
        {"t": "rule", "color": "red", "title": "Same case, own sign",
         "text": "The follower copies the case of the word before it. Its own group decides the sign. A broken plural with damma can have an adjective with wāw: {جَاءَ الطُّلَّابُ المُجْتَهِدُونَ}."},

        {"t": "h2", "text": "The adjective (نَعْتٌ)"},
        {"t": "p", "text": "The adjective copies four things: case, {ال} or no {ال}, masculine or feminine, and one, two or many."},
        {"t": "table", "head": ["Sentence", "Noun: sign", "Adjective: sign"], "rows": [
            ["جَاءَ المُعَلِّمُونَ المُجْتَهِدُونَ.", "Wāw", "Wāw"],
            ["نَجَحَ الطَّالِبَانِ الجَدِيدَانِ.", "Alif", "Alif"],
            ["نَجَحَتِ الطَّالِبَاتُ المُجْتَهِدَاتُ.", "Damma", "Damma"],
            ["جَاءَ الطُّلَّابُ المُجْتَهِدُونَ.", "Damma (broken plural)", "Wāw"],
            ["حَضَرَ القَاضِي العَادِلُ.", "Hidden damma", "Damma"],
            ["جَاءَ أَبُوكَ الكَرِيمُ.", "Wāw", "Damma"],
        ]},
        {"t": "tip", "text": "A plural of things takes a feminine singular adjective: {الكُتُبُ الجَدِيدَةُ} \"the new books\"."},

        {"t": "h2", "text": "After وَ، ثُمَّ، أَوْ (مَعْطُوفٌ)"},
        {"t": "p", "text": "{وَ} means \"and\", {ثُمَّ} means \"then\", {أَوْ} means \"or\". The word after them copies the case of the first word."},
        {"t": "examples", "items": [
            {"ar": "جَاءَ مُحَمَّدٌ وَأَخُوهُ.", "en": "Muhammad and his brother came.", "note": "{مُحَمَّدٌ}: damma. {أَخُوهُ}: wāw, a five noun."},
            {"ar": "حَضَرَ المُدِيرُ ثُمَّ المُعَلِّمُونَ.", "en": "The principal came, then the teachers.", "note": "{المُدِيرُ}: damma. {المُعَلِّمُونَ}: wāw."},
            {"ar": "جَاءَ خَالِدٌ أَوْ أَخُوهُ.", "en": "Khalid or his brother came.", "note": "{أَوْ} joins like {وَ}. Both are rafʿ."},
        ]},

        {"t": "h2", "text": "Emphasis (تَوْكِيدٌ)"},
        {"t": "p", "text": "Use {نَفْسُ} or {عَيْنُ} \"himself, herself\" for one person. Use {كُلُّ} \"all\" for a group. Add a pronoun that matches the noun."},
        {"t": "table", "head": ["Sentence", "Meaning", "Emphasis"], "rows": [
            ["جَاءَ المُدِيرُ نَفْسُهُ.", "The principal himself came.", "نَفْسُهُ"],
            ["حَضَرَتِ المُعَلِّمَةُ نَفْسُهَا.", "The teacher herself came.", "نَفْسُهَا"],
            ["جَاءَ الأَمِيرُ عَيْنُهُ.", "The prince himself came.", "عَيْنُهُ"],
            ["حَضَرَ الطُّلَّابُ كُلُّهُمْ.", "The students all came.", "كُلُّهُمْ"],
            ["نَجَحَتِ الطَّالِبَاتُ كُلُّهُنَّ.", "The female students all passed.", "كُلُّهُنَّ"],
        ]},
        {"t": "tip", "text": "{نَفْسُ}، {عَيْنُ} and {كُلُّ} are singular words, so in rafʿ they take damma. The pronoun after them is the owner."},

        {"t": "h2", "text": "The substitute (بَدَلٌ)"},
        {"t": "p", "text": "The substitute names the same person a second time, often with a name after a title or a relative."},
        {"t": "examples", "items": [
            {"ar": "جَاءَ أَخُوكَ زَيْدٌ.", "en": "Your brother Zayd came.", "note": "{أَخُوكَ}: doer, wāw. {زَيْدٌ}: substitute, damma."},
            {"ar": "خَطَبَ الخَلِيفَةُ عُمَرُ.", "en": "The caliph ʿUmar gave a speech.", "note": "{عُمَرُ} is a diptote: one damma, no tanween."},
            {"ar": "حَضَرَ صَدِيقِي خَالِدٌ.", "en": "My friend Khalid came.", "note": "{صَدِيقِي}: hidden damma. {خَالِدٌ}: damma."},
        ]},

        {"t": "h2", "text": "Followers of every rafʿ job"},
        {"t": "p", "text": "Any rafʿ word can have a follower: the topic, the information, the doer, the doer stand-in, kāna's noun and inna's information."},
        {"t": "examples", "items": [
            {"ar": "البَيْتُ الجَدِيدُ وَاسِعٌ.", "en": "The new house is wide.", "note": "Adjective of the topic."},
            {"ar": "كُتِبَ الدَّرْسُ الجَدِيدُ.", "en": "The new lesson was written.", "note": "Adjective of the doer stand-in."},
            {"ar": "كَانَ الطَّالِبَانِ المُجْتَهِدَانِ حَاضِرَيْنِ.", "en": "The two hard-working students were present.", "note": "Adjective of kāna's noun: alif."},
            {"ar": "إِنَّ المُدِيرَ رَجُلٌ كَرِيمٌ.", "en": "Indeed, the principal is a generous man.", "note": "Adjective of inna's information: damma."},
        ]},

        {"t": "h2", "text": "Worked examples: the full iʿrāb"},
        {"t": "table", "head": ["Word", "Iʿrāb"], "rows": [
            ["المُجْتَهِدُونَ", "نَعْتٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ"],
            ["وَ", "حَرْفُ عَطْفٍ مَبْنِيٌّ عَلَى الفَتْحِ"],
            ["أَخُوهُ", "مَعْطُوفٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ"],
            ["نَفْسُهُ", "تَوْكِيدٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ"],
            ["زَيْدٌ", "بَدَلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ"],
            ["الجَدِيدَانِ", "نَعْتٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الأَلِفُ لِأَنَّهُ مُثَنًّى"],
        ]},

        {"t": "summary", "title": "In short", "items": [
            "Four followers: adjective {نَعْتٌ}، after {وَ} {مَعْطُوفٌ}، emphasis {تَوْكِيدٌ}، substitute {بَدَلٌ}.",
            "A follower copies the case of the word before it. Here that case is rafʿ.",
            "Its own group gives the sign: {جَاءَ الطُّلَّابُ المُجْتَهِدُونَ} (damma, then wāw).",
            "{وَ}، {ثُمَّ}، {أَوْ} all join words the same way.",
            "Emphasis: {نَفْسُهُ}، {عَيْنُهُ} for one, {كُلُّهُمْ} for a group. Damma in rafʿ.",
            "Substitute: the same person named again: {أَخُوكَ زَيْدٌ}، {الخَلِيفَةُ عُمَرُ}.",
        ]},
    ],

    "practice": [
        {
            "title": "Iʿrāb of the sentence",
            "prompt": "جَاءَ المُعَلِّمُونَ المُجْتَهِدُونَ وَالمُدِيرُ نَفْسُهُ.",
            "en": "The hard-working teachers came, and the principal himself.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, ADJ, AND, TAWK]},
                {"key": "sign", "label": "Sign", "options": [DAM, WAW, FIXED]},
            ],
            "rows": [
                {"s": "جَاءَ", "gloss": "came", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "المُعَلِّمُونَ", "gloss": "the teachers", "ans": {"job": "doer", "sign": "waw"},
                 "why": "Doer, rafʿ. A sound masculine plural: wāw."},
                {"s": "المُجْتَهِدُونَ", "gloss": "hard-working", "ans": {"job": "adj", "sign": "waw"},
                 "why": "Adjective of the doer, so rafʿ. A sound masculine plural: wāw."},
                {"s": "المُدِيرُ", "gloss": "the principal", "ans": {"job": "and", "sign": "dam"},
                 "why": "After {وَ}, joined to the doer, so rafʿ. A singular: damma."},
                {"s": "نَفْسُهُ", "gloss": "himself", "ans": {"job": "tawk", "sign": "dam"},
                 "why": "Emphasis of {المُدِيرُ}, so rafʿ. {نَفْسُ} is singular: damma."},
            ],
        },
        {
            "title": "Which sign does the follower take?",
            "fields": [{"key": "sign", "label": "Sign of rafʿ", "options": [DAM, ALIF, WAW, HID]}],
            "rows": [
                {"s": "جَاءَ الطُّلَّابُ [المُجْتَهِدُونَ]", "gloss": "The hard-working students came.", "ans": {"sign": "waw"},
                 "why": "Adjective, rafʿ. {الطُّلَّابُ} has damma, but the adjective is a sound masculine plural: wāw."},
                {"s": "حَضَرَ المُعَلِّمُونَ وَ[المُدِيرُ]", "gloss": "The teachers and the principal came.", "ans": {"sign": "dam"},
                 "why": "After {وَ}, rafʿ. {المُدِيرُ} is singular: damma."},
                {"s": "جَاءَ القَاضِي وَ[أَخُوهُ]", "gloss": "The judge and his brother came.", "ans": {"sign": "waw"},
                 "why": "After {وَ}, rafʿ. A five noun with an owner: wāw."},
                {"s": "نَجَحَ الطَّالِبَانِ [الجَدِيدَانِ]", "gloss": "The two new students passed.", "ans": {"sign": "alif"},
                 "why": "Adjective of a dual, so a dual too. Rafʿ: alif."},
                {"s": "جَاءَ أَخُوكَ [خَالِدٌ]", "gloss": "Your brother Khalid came.", "ans": {"sign": "dam"},
                 "why": "Substitute, rafʿ. A singular name: damma."},
                {"s": "حَضَرَ الطَّبِيبُ ثُمَّ [المُحَامِي]", "gloss": "The doctor came, then the lawyer.", "ans": {"sign": "hid"},
                 "why": "After {ثُمَّ}, rafʿ. Manqūṣ: hidden damma on the {ي}."},
            ],
        },
        {
            "title": "Which form of the follower is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "جَاءَ الطُّلَّابُ ___", "gloss": "The hard-working students came.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("المُجْتَهِدُونَ", "المُجْتَهِدِينَ", "المُجْتَهِدَانِ")},
                 "why": "The adjective copies rafʿ. Many men: {المُجْتَهِدُونَ}."},
                {"s": "حَضَرَ المُدِيرُ وَ___", "gloss": "The principal and his father came.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَبُوهُ", "أَبَاهُ", "أَبِيهِ")},
                 "why": "After {وَ}, rafʿ. A five noun in rafʿ: {أَبُوهُ}."},
                {"s": "نَجَحَ الطَّالِبَانِ ___", "gloss": "The two clever students passed.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الذَّكِيَّانِ", "الذَّكِيَّيْنِ", "الذَّكِيُّونَ")},
                 "why": "The adjective of a dual is a dual, rafʿ: {الذَّكِيَّانِ}."},
                {"s": "المُهَنْدِسُونَ وَ___ حَاضِرُونَ", "gloss": "The engineers and the workers are present.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("العُمَّالُ", "العُمَّالَ", "العُمَّالِ")},
                 "why": "Joined to the topic, so rafʿ. A broken plural: damma."},
                {"s": "جَاءَ المُعَلِّمُ ___", "gloss": "The teacher himself came.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("نَفْسُهُ", "نَفْسَهُ", "نَفْسِهِ")},
                 "why": "Emphasis of the doer, so rafʿ: {نَفْسُهُ}."},
                {"s": "خَطَبَ الخَلِيفَةُ ___", "gloss": "The caliph ʿUmar gave a speech.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("عُمَرُ", "عُمَرٌ", "عُمَرَ")},
                 "why": "Substitute, rafʿ. {عُمَرُ} is a diptote: one damma, no tanween."},
            ],
        },
        {
            "title": "Which follower is it?",
            "fields": [{"key": "job", "label": "Follower", "options": [ADJ, AND, TAWK, BADAL]}],
            "rows": [
                {"s": "جَاءَ الرَّجُلُ [الكَرِيمُ]", "gloss": "The generous man came.", "ans": {"job": "adj"},
                 "why": "It describes the man: an adjective."},
                {"s": "جَاءَ الرَّجُلُ وَ[ابْنُهُ]", "gloss": "The man and his son came.", "ans": {"job": "and"},
                 "why": "Joined with {وَ}: another person."},
                {"s": "جَاءَ الرَّجُلُ [نَفْسُهُ]", "gloss": "The man himself came.", "ans": {"job": "tawk"},
                 "why": "{نَفْسُهُ} \"himself\" makes it strong: emphasis."},
                {"s": "جَاءَ أَخُوكَ [زَيْدٌ]", "gloss": "Your brother Zayd came.", "ans": {"job": "badal"},
                 "why": "The same person named again: a substitute."},
                {"s": "خَرَجَ الطُّلَّابُ [كُلُّهُمْ]", "gloss": "The students all went out.", "ans": {"job": "tawk"},
                 "why": "{كُلُّهُمْ} \"all of them\": emphasis."},
                {"s": "دَخَلَ المُدِيرُ ثُمَّ [المُعَلِّمُ]", "gloss": "The principal entered, then the teacher.", "ans": {"job": "and"},
                 "why": "Joined with {ثُمَّ} \"then\". It works like {وَ}."},
            ],
        },
        {
            "title": "Iʿrāb of a nominal sentence",
            "prompt": "البَيْتُ الجَدِيدُ وَالحَدِيقَةُ جَمِيلَانِ.",
            "en": "The new house and the garden are beautiful.",
            "fields": [
                {"key": "job", "label": "Job", "options": [TOPIC, INFO, ADJ, AND]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW]},
            ],
            "rows": [
                {"s": "البَيْتُ", "gloss": "the house", "ans": {"job": "topic", "sign": "dam"},
                 "why": "Topic, rafʿ. A singular: damma."},
                {"s": "الجَدِيدُ", "gloss": "new", "ans": {"job": "adj", "sign": "dam"},
                 "why": "Adjective of the topic, rafʿ: damma."},
                {"s": "الحَدِيقَةُ", "gloss": "the garden", "ans": {"job": "and", "sign": "dam"},
                 "why": "After {وَ}, joined to the topic, rafʿ: damma."},
                {"s": "جَمِيلَانِ", "gloss": "beautiful (two)", "ans": {"job": "info", "sign": "alif"},
                 "why": "Information about two things, so a dual. Rafʿ: alif."},
            ],
        },
        {
            "title": "Followers of other rafʿ jobs",
            "fields": [
                {"key": "job", "label": "Follower", "options": [ADJ, AND, TAWK]},
                {"key": "sign", "label": "Sign", "options": [DAM, ALIF, WAW]},
            ],
            "rows": [
                {"s": "كَانَ الطَّالِبَانِ [المُجْتَهِدَانِ] حَاضِرَيْنِ", "gloss": "The two hard-working students were present.", "ans": {"job": "adj", "sign": "alif"},
                 "why": "Adjective of kāna's noun, so rafʿ. A dual: alif."},
                {"s": "إِنَّ المُدِيرَ رَجُلٌ [كَرِيمٌ]", "gloss": "Indeed, the principal is a generous man.", "ans": {"job": "adj", "sign": "dam"},
                 "why": "Adjective of inna's information {رَجُلٌ}, so rafʿ: damma."},
                {"s": "كَانَ أَبُوكَ وَ[أَخُوكَ] مُسَافِرَيْنِ", "gloss": "Your father and your brother were travelling.", "ans": {"job": "and", "sign": "waw"},
                 "why": "Joined to kāna's noun, so rafʿ. A five noun: wāw."},
                {"s": "أَصْبَحَ المُدِيرُ [نَفْسُهُ] مَرِيضًا", "gloss": "The principal himself became ill.", "ans": {"job": "tawk", "sign": "dam"},
                 "why": "Emphasis of kāna's noun, so rafʿ: damma."},
                {"s": "إِنَّ الطُّلَّابَ مُجْتَهِدُونَ وَ[صَابِرُونَ]", "gloss": "Indeed, the students are hard-working and patient.", "ans": {"job": "and", "sign": "waw"},
                 "why": "Joined to inna's information, so rafʿ. A sound masculine plural: wāw."},
                {"s": "كُتِبَ الدَّرْسُ [الجَدِيدُ]", "gloss": "The new lesson was written.", "ans": {"job": "adj", "sign": "dam"},
                 "why": "Adjective of the doer stand-in, so rafʿ: damma."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Iʿrāb of the sentence",
            "prompt": "حَضَرَ القَاضِي العَادِلُ وَأَبُوكَ ثُمَّ المُهَنْدِسُونَ.",
            "en": "The just judge and your father came, then the engineers.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, DOER, ADJ, AND]},
                {"key": "sign", "label": "Sign", "options": [DAM, WAW, HID, FIXED]},
            ],
            "rows": [
                {"s": "حَضَرَ", "gloss": "came", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "القَاضِي", "gloss": "the judge", "ans": {"job": "doer", "sign": "hid"},
                 "why": "Doer, rafʿ. Manqūṣ: hidden damma on the {ي}."},
                {"s": "العَادِلُ", "gloss": "just", "ans": {"job": "adj", "sign": "dam"},
                 "why": "Adjective of the doer, rafʿ. A singular: damma shows."},
                {"s": "أَبُوكَ", "gloss": "your father", "ans": {"job": "and", "sign": "waw"},
                 "why": "After {وَ}, rafʿ. A five noun: wāw."},
                {"s": "المُهَنْدِسُونَ", "gloss": "the engineers", "ans": {"job": "and", "sign": "waw"},
                 "why": "After {ثُمَّ}, rafʿ. A sound masculine plural: wāw."},
            ],
        },
        {
            "title": "Which sign does the follower take?",
            "fields": [{"key": "sign", "label": "Sign of rafʿ", "options": [DAM, ALIF, WAW, HID]}],
            "rows": [
                {"s": "سَافَرَ أَبُوكَ وَ[صَدِيقُهُ]", "gloss": "Your father and his friend travelled.", "ans": {"sign": "dam"},
                 "why": "After {وَ}, rafʿ. {صَدِيقٌ} is not a five noun: damma."},
                {"s": "جَاءَ صَدِيقِي [مُحَمَّدٌ]", "gloss": "My friend Muhammad came.", "ans": {"sign": "dam"},
                 "why": "Substitute, rafʿ: damma. The hidden damma is on {صَدِيقِي}, not on the name."},
                {"s": "حَضَرَ خَالِدٌ وَ[الفَتَى]", "gloss": "Khalid and the young man came.", "ans": {"sign": "hid"},
                 "why": "After {وَ}, rafʿ. Maqṣūr: hidden damma on the alif."},
                {"s": "رَجَعَ الجُنُودُ [المُسْلِمُونَ]", "gloss": "The Muslim soldiers returned.", "ans": {"sign": "waw"},
                 "why": "Adjective, rafʿ. A sound masculine plural: wāw, even after a broken plural."},
                {"s": "فَازَتِ الطَّالِبَتَانِ [المُجْتَهِدَتَانِ]", "gloss": "The two hard-working female students won.", "ans": {"sign": "alif"},
                 "why": "Adjective of a dual, rafʿ: alif."},
                {"s": "جَاءَ الرَّجُلُ [أَبُو] خَالِدٍ", "gloss": "The man, Khalid's father, came.", "ans": {"sign": "waw"},
                 "why": "Substitute, rafʿ. A five noun with an owner: wāw."},
            ],
        },
        {
            "title": "Which form of the follower is right?",
            "fields": [{"key": "pick", "label": "Form", "options": []}],
            "rows": [
                {"s": "رَجَعَ المُسَافِرُونَ ___", "gloss": "The travellers all returned.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("كُلُّهُمْ", "كُلَّهُمْ", "كُلِّهِمْ")},
                 "why": "Emphasis of the doer, rafʿ: {كُلُّهُمْ}."},
                {"s": "فَازَ اللَّاعِبُونَ ___", "gloss": "The Saudi players won.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("السُّعُودِيُّونَ", "السُّعُودِيِّينَ", "السُّعُودِيُّ")},
                 "why": "The adjective copies rafʿ and the plural: {السُّعُودِيُّونَ}."},
                {"s": "حَضَرَ الطَّبِيبُ وَ___", "gloss": "The doctor and the two nurses came.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("المُمَرِّضَتَانِ", "المُمَرِّضَتَيْنِ", "المُمَرِّضَاتِ")},
                 "why": "After {وَ}, rafʿ. A dual in rafʿ: {المُمَرِّضَتَانِ}."},
                {"s": "جَاءَ الضُّيُوفُ ثُمَّ ___", "gloss": "The guests came, then your brother.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أَخُوكَ", "أَخَاكَ", "أَخِيكَ")},
                 "why": "After {ثُمَّ}, rafʿ. A five noun in rafʿ: {أَخُوكَ}."},
                {"s": "الطَّالِبَاتُ ___ نَاجِحَاتٌ", "gloss": "The hard-working female students are successful.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("المُجْتَهِدَاتُ", "المُجْتَهِدَاتِ", "المُجْتَهِدَاتَ")},
                 "why": "Adjective of the topic, rafʿ. A sound feminine plural: damma."},
                {"s": "إِنَّ المُعَلِّمَ رَجُلٌ ___", "gloss": "Indeed, the teacher is a patient man.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("صَابِرٌ", "صَابِرًا", "صَابِرٍ")},
                 "why": "It describes {رَجُلٌ}, inna's information, so rafʿ: {صَابِرٌ}."},
            ],
        },
        {
            "title": "Which follower is it?",
            "fields": [{"key": "job", "label": "Follower", "options": [ADJ, AND, TAWK, BADAL]}],
            "rows": [
                {"s": "جَاءَ الطَّالِبُ [عَيْنُهُ]", "gloss": "The student himself came.", "ans": {"job": "tawk"},
                 "why": "{عَيْنُهُ} \"himself\": emphasis, like {نَفْسُهُ}."},
                {"s": "حَضَرَ المُعَلِّمُ [أَحْمَدُ]", "gloss": "The teacher Ahmad came.", "ans": {"job": "badal"},
                 "why": "The same person named again: a substitute. A name cannot be an adjective."},
                {"s": "حَضَرَ المُعَلِّمُ أَوْ [المُدِيرُ]", "gloss": "The teacher or the principal came.", "ans": {"job": "and"},
                 "why": "Joined with {أَوْ} \"or\". It works like {وَ}."},
                {"s": "جَاءَ الطِّفْلُ [الصَّغِيرُ]", "gloss": "The little child came.", "ans": {"job": "adj"},
                 "why": "It describes the child: an adjective."},
                {"s": "نَجَحَ الطُّلَّابُ [كُلُّهُمْ]", "gloss": "The students all passed.", "ans": {"job": "tawk"},
                 "why": "{كُلُّهُمْ} \"all of them\": emphasis."},
                {"s": "سَافَرَ صَدِيقِي [خَالِدٌ]", "gloss": "My friend Khalid travelled.", "ans": {"job": "badal"},
                 "why": "A name for the same person: a substitute. A name cannot be an adjective."},
            ],
        },
        {
            "title": "Choose the correct sentence",
            "fields": [{"key": "pick", "label": "Sentence", "options": []}],
            "rows": [
                {"s": "The hard-working engineers came.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("جَاءَ المُهَنْدِسُونَ المُجْتَهِدِينَ.", "جَاءَ المُهَنْدِسُونَ المُجْتَهِدُونَ.", "جَاءَ المُهَنْدِسُونَ المُجْتَهِدُ.")},
                 "why": "The adjective copies rafʿ and the plural: {المُجْتَهِدُونَ}."},
                {"s": "Your father and your brother came.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("حَضَرَ أَبُوكَ وَأَخُوكَ.", "حَضَرَ أَبُوكَ وَأَخَاكَ.", "حَضَرَ أَبُوكَ وَأَخِيكَ.")},
                 "why": "The word after {وَ} copies rafʿ: {أَخُوكَ}."},
                {"s": "The students all came.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("جَاءَ الطُّلَّابُ كُلُّهُمْ.", "جَاءَ الطُّلَّابُ كُلَّهُمْ.", "جَاءَ الطُّلَّابُ كُلُّهُ.")},
                 "why": "Emphasis copies rafʿ, and the pronoun matches a group of men: {كُلُّهُمْ}."},
                {"s": "The two tall men are present.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الرَّجُلَانِ الطَّوِيلَانِ حَاضِرَانِ.", "الرَّجُلَانِ الطَّوِيلَيْنِ حَاضِرَانِ.", "الرَّجُلَانِ الطَّوِيلُونَ حَاضِرَانِ.")},
                 "why": "The adjective of a dual topic is a dual in rafʿ: {الطَّوِيلَانِ}."},
                {"s": "The just judge was famous.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("كَانَ القَاضِي العَادِلُ مَشْهُورًا.", "كَانَ القَاضِي العَادِلَ مَشْهُورًا.", "كَانَ القَاضِي العَادِلِ مَشْهُورًا.")},
                 "why": "{القَاضِي} is kāna's noun, rafʿ with a hidden damma. Its adjective shows the damma: {العَادِلُ}."},
            ],
        },
        {
            "title": "Iʿrāb of the sentence",
            "prompt": "كَانَ صَدِيقِي خَالِدٌ وَأَخُوهُ مُسَافِرَيْنِ.",
            "en": "My friend Khalid and his brother were travelling.",
            "fields": [
                {"key": "job", "label": "Job", "options": [VERB, KISM, BADAL, AND]},
                {"key": "sign", "label": "Sign", "options": [DAM, WAW, HID, FIXED]},
            ],
            "rows": [
                {"s": "كَانَ", "gloss": "was", "ans": {"job": "verb", "sign": "fixed"},
                 "why": "A past verb, fixed on fatha."},
                {"s": "صَدِيقِي", "gloss": "my friend", "ans": {"job": "kism", "sign": "hid"},
                 "why": "Kāna's noun, rafʿ. A noun with ـي \"my\": hidden damma."},
                {"s": "خَالِدٌ", "gloss": "Khalid", "ans": {"job": "badal", "sign": "dam"},
                 "why": "The same person named again: a substitute, rafʿ. Damma."},
                {"s": "أَخُوهُ", "gloss": "his brother", "ans": {"job": "and", "sign": "waw"},
                 "why": "After {وَ}, joined to kāna's noun, rafʿ. A five noun: wāw."},
            ],
        },
    ],
}
