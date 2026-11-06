# Stage 3, Unit 3: Pointing words (أَسْمَاءُ الْإِشَارَةِ)

FIXED = {"k": "fixed", "label": "Fixed · مَبْنِيٌّ", "color": "teal"}
FLEX = {"k": "flex", "label": "Flexible · مُعْرَبٌ", "color": "orange"}

TOPIC = {"k": "topic", "label": "Topic · مُبْتَدَأٌ", "color": "gold"}
DOER = {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"}
OBJ = {"k": "obj", "label": "Object · مَفْعُولٌ بِهِ", "color": "pink"}
PREP = {"k": "prep", "label": "After a preposition", "color": "green"}
OWNER = {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}
JOBS = [TOPIC, DOER, OBJ, PREP, OWNER]

P_RAF = {"k": "raf", "label": "Place of rafʿ", "color": "red"}
P_NASB = {"k": "nasb", "label": "Place of naṣb", "color": "pink"}
P_JARR = {"k": "jarr", "label": "Place of jarr", "color": "green"}
PLACES = [P_RAF, P_NASB, P_JARR]

SENT = {"k": "sent", "label": "Full sentence", "color": "red"}
PHRASE = {"k": "phrase", "label": "Phrase, not finished", "color": "grey"}

NEAR = {"k": "near", "label": "Near", "color": "teal"}
FAR = {"k": "far", "label": "Far", "color": "navy"}
MS = {"k": "ms", "label": "One male or thing", "color": "blue"}
FS = {"k": "fs", "label": "One female or thing", "color": "pink"}
PL = {"k": "pl", "label": "Plural (people)", "color": "purple"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s3-demonstratives",
    "order": 3,
    "title": "Pointing words",
    "ar": "أَسْمَاءُ الْإِشَارَةِ",
    "blurb": "This, that, these and those: learn the table, then use the words in sentences.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 3 · UNIT 3", "title": "This, that, these, those",
         "text": "A pointing word shows which thing or person you mean. It is fixed: its last letter never changes.",
         "wm": "هَذَا"},

        {"t": "h2", "text": "The table to learn"},
        {"t": "p", "text": "Arabic has a word for near things and a word for far things. Each one also changes for male, female and plural."},
        {"t": "table", "head": ["", "One male or thing", "One female or thing", "Plural (people)"], "rows": [
            ["Near", "{هَذَا} this", "{هَذِهِ} this", "{هَؤُلَاءِ} these"],
            ["Far", "{ذَلِكَ} that", "{تِلْكَ} that", "{أُولَئِكَ} those"],
        ]},
        {"t": "words", "items": [
            {"ar": "هُنَا", "label": "hunā", "sub": "here", "color": "teal"},
            {"ar": "هُنَاكَ", "label": "hunāka", "sub": "there", "color": "teal"},
        ]},
        {"t": "p", "text": "{هُنَا} and {هُنَاكَ} point to a place. Madinah lesson 5: {هُوَ تَحْتَ الْمَكْتَبِ هُنَاكَ} \"It is under the desk, over there.\""},
        {"t": "rule", "color": "teal", "title": "Learn the last vowel too",
         "text": "{هَذَا} ends in alif, {هَذِهِ} and {هَؤُلَاءِ} in kasra, {ذَلِكَ}، {تِلْكَ}، {أُولَئِكَ} and {هُنَاكَ} in fatha. These endings never change."},
        {"t": "tip", "text": "{هَؤُلَاءِ} and {أُولَئِكَ} are for groups of people, male or female: {هَؤُلَاءِ طُلَّابٌ}، {هَؤُلَاءِ نِسَاءٌ}. For plural things Arabic normally uses {هَذِهِ}: {هَذِهِ كُتُبٌ} \"these are books\"."},

        {"t": "h2", "text": "Reading tips: hidden and extra letters"},
        {"t": "p", "text": "Some pointing words are not read exactly as they are written. The Qur'an shows the hidden alif with a small alif on top: {هٰذَا}."},
        {"t": "table", "head": ["Written", "Said", "Why"], "rows": [
            ["هَذَا", "hādhā", "A long ā after {هـ} is said but not written."],
            ["هَذِهِ", "hādhihi", "The same hidden ā after {هـ}."],
            ["هَؤُلَاءِ", "hāʾulāʾi", "The same hidden ā after {هـ}."],
            ["ذَلِكَ", "dhālika", "A long ā after {ذ} is said but not written."],
            ["أُولَئِكَ", "ulāʾika", "The {و} is written but not read. A long ā after {ل} is said but not written."],
        ]},
        {"t": "tip", "text": "Do not write the hidden alif yourself. {هَاذَا} and {ذَالِكَ} are spelling mistakes."},

        {"t": "h2", "text": "\"This is a book\" or \"this book\"?"},
        {"t": "p", "text": "Look at the noun after the pointing word. Does it have {ال}?"},
        {"t": "cols", "items": [
            {"color": "gold", "title": "No ال: a sentence", "ar": "هَذَا كِتَابٌ",
             "text": "\"This is a book.\" {هَذَا} is the Topic and {كِتَابٌ} is the Information."},
            {"color": "teal", "title": "With ال: a phrase", "ar": "هَذَا الْكِتَابُ",
             "text": "\"this book\". It is not finished yet. Add Information: {هَذَا الْكِتَابُ جَدِيدٌ}."},
        ]},
        {"t": "examples", "items": [
            {"ar": "هَذَا بَيْتٌ.", "en": "This is a house.", "note": "A full sentence."},
            {"ar": "هَذَا الْبَيْتُ قَرِيبٌ.", "en": "This house is near.", "note": "{هَذَا الْبَيْتُ} is the Topic part. {قَرِيبٌ} is the Information."},
            {"ar": "تِلْكَ سَيَّارَةٌ.", "en": "That is a car.", "note": "A full sentence."},
            {"ar": "تِلْكَ السَّيَّارَةُ جَدِيدَةٌ.", "en": "That car is new.", "note": "{تِلْكَ السَّيَّارَةُ} means \"that car\"."},
        ]},
        {"t": "tip", "text": "To say \"this is THE book\", put {هُوَ} or {هِيَ} in the middle: {هَذَا هُوَ الْكِتَابُ}، {هَذِهِ هِيَ السَّاعَةُ}."},
        {"t": "tip", "text": "A noun in iḍāfa has no {ال}, so it makes a sentence: {هَذَا بَيْتُ حَامِدٍ} \"This is Hamid's house.\" (Madinah lesson 5)"},

        {"t": "h2", "text": "هَذَا or هَذِهِ? Follow the noun"},
        {"t": "p", "text": "Choose the pointing word by the noun you point to. Is it near or far? Male or female? One or a group of people?"},
        {"t": "examples", "items": [
            {"ar": "هَذَا قَلَمٌ وَهَذِهِ سَاعَةٌ.", "en": "This is a pen and this is a watch.", "note": "{قَلَمٌ} is masculine, {سَاعَةٌ} is feminine."},
            {"ar": "ذَلِكَ مَسْجِدٌ وَتِلْكَ مَدْرَسَةٌ.", "en": "That is a mosque and that is a school.", "note": "Far: {ذَلِكَ} for masculine, {تِلْكَ} for feminine."},
            {"ar": "هَؤُلَاءِ طُلَّابٌ وَأُولَئِكَ رِجَالٌ.", "en": "These are students and those are men.", "note": "Groups of people: {هَؤُلَاءِ}، {أُولَئِكَ}."},
            {"ar": "هَذِهِ بِنْتٌ.", "en": "This is a girl.", "note": "{بِنْتٌ} has no {ة}, but it is feminine. Use {هَذِهِ}."},
        ]},

        {"t": "h2", "text": "Its place in the sentence"},
        {"t": "p", "text": "A pointing word is fixed, but it still has a job. The job gives it a place. The noun after it shows the ending that the pointing word cannot show."},
        {"t": "examples", "items": [
            {"ar": "هَذَا كِتَابٌ.", "en": "This is a book.", "note": "{هَذَا} is the Topic. Fixed, in the place of rafʿ."},
            {"ar": "دَخَلَ هَذَا الرَّجُلُ الْمَسْجِدَ.", "en": "This man entered the mosque.", "note": "{هَذَا} is the doer. Place of rafʿ. See the damma on {الرَّجُلُ}."},
            {"ar": "فَتَحَ الطَّالِبُ هَذَا الْبَابَ.", "en": "The student opened this door.", "note": "{هَذَا} is the object. Place of naṣb. See the fatha on {الْبَابَ}."},
            {"ar": "فِي هَذَا الْبَيْتِ", "en": "in this house", "note": "{هَذَا} comes after a preposition. Place of jarr. See the kasra on {الْبَيْتِ}."},
            {"ar": "كِتَابُ هَذَا الطَّالِبِ", "en": "this student's book", "note": "{هَذَا} is the owner. Place of jarr."},
        ]},
        {"t": "cols", "items": [
            {"color": "red", "title": "Place of rafʿ", "ar": "فِي مَحَلِّ رَفْعٍ", "text": "Topic, Information, doer."},
            {"color": "pink", "title": "Place of naṣb", "ar": "فِي مَحَلِّ نَصْبٍ", "text": "Object, and the other naṣb jobs."},
            {"color": "green", "title": "Place of jarr", "ar": "فِي مَحَلِّ جَرٍّ", "text": "After a preposition, or the owner."},
        ]},

        {"t": "h2", "text": "Not fixed: هَذَانِ and هَاتَانِ"},
        {"t": "rule", "color": "orange", "title": "The words for \"these two\" change",
         "text": "{هَذَانِ} (two males) and {هَاتَانِ} (two females) are flexible. In naṣb and jarr they become {هَذَيْنِ} and {هَاتَيْنِ}. You learn them with the dual in Stage 4."},
        {"t": "table", "head": ["Form", "Two males", "Two females"], "rows": [
            ["Rafʿ", "هَذَانِ", "هَاتَانِ"],
            ["Naṣb and jarr", "هَذَيْنِ", "هَاتَيْنِ"],
        ]},

        {"t": "summary", "title": "In short", "items": [
            "Near: {هَذَا}، {هَذِهِ}، {هَؤُلَاءِ}. Far: {ذَلِكَ}، {تِلْكَ}، {أُولَئِكَ}. Place: {هُنَا}، {هُنَاكَ}.",
            "Choose by the noun: near or far, male or female, one or a group of people.",
            "{هَذَا كِتَابٌ} is a sentence. {هَذَا الْكِتَابُ} is a phrase: \"this book\".",
            "Pointing words are fixed, but they have a place: rafʿ, naṣb or jarr.",
            "{هَذَانِ} and {هَاتَانِ} are not fixed. They wait for Stage 4.",
        ]},
    ],

    "practice": [
        {
            "title": "Choose the pointing word",
            "fields": [{"key": "pick", "label": "Pointing word", "options": []}],
            "rows": [
                {"s": "... قَلَمٌ", "gloss": "This is a pen. (near)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("هَذَا", "هَذِهِ", "ذَلِكَ")}, "why": "Near and masculine: {هَذَا قَلَمٌ}."},
                {"s": "... سَاعَةٌ", "gloss": "This is a watch. (near)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هَذَا", "هَذِهِ", "تِلْكَ")}, "why": "{سَاعَةٌ} ends in {ة}. It is feminine and near: {هَذِهِ}."},
                {"s": "... مَسْجِدٌ", "gloss": "That is a mosque. (far)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هَذَا", "ذَلِكَ", "تِلْكَ")}, "why": "Far and masculine: {ذَلِكَ مَسْجِدٌ}."},
                {"s": "... سَيَّارَةٌ", "gloss": "That is a car. (far)", "ans": {"pick": "c"},
                 "opts": {"pick": pick("ذَلِكَ", "هَذِهِ", "تِلْكَ")}, "why": "Far and feminine: {تِلْكَ سَيَّارَةٌ}."},
                {"s": "... طُلَّابٌ", "gloss": "These are students. (near)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هَذَا", "هَؤُلَاءِ", "أُولَئِكَ")}, "why": "A near group of people: {هَؤُلَاءِ طُلَّابٌ}."},
                {"s": "... رِجَالٌ", "gloss": "Those are men. (far)", "ans": {"pick": "c"},
                 "opts": {"pick": pick("هَؤُلَاءِ", "ذَلِكَ", "أُولَئِكَ")}, "why": "A far group of people: {أُولَئِكَ رِجَالٌ}."},
            ],
        },
        {
            "title": "Near or far? Who for?",
            "fields": [
                {"key": "dist", "label": "Near or far", "options": [NEAR, FAR]},
                {"key": "who", "label": "Who for", "options": [MS, FS, PL]},
            ],
            "rows": [
                {"s": "هَذَا", "ans": {"dist": "near", "who": "ms"}, "why": "{هَذَا} \"this\": near, one male or thing."},
                {"s": "تِلْكَ", "ans": {"dist": "far", "who": "fs"}, "why": "{تِلْكَ} \"that\": far, one female or thing."},
                {"s": "هَؤُلَاءِ", "ans": {"dist": "near", "who": "pl"}, "why": "{هَؤُلَاءِ} \"these\": near, a group of people."},
                {"s": "ذَلِكَ", "ans": {"dist": "far", "who": "ms"}, "why": "{ذَلِكَ} \"that\": far, one male or thing."},
                {"s": "هَذِهِ", "ans": {"dist": "near", "who": "fs"}, "why": "{هَذِهِ} \"this\": near, one female or thing."},
                {"s": "أُولَئِكَ", "ans": {"dist": "far", "who": "pl"}, "why": "{أُولَئِكَ} \"those\": far, a group of people."},
            ],
        },
        {
            "title": "Sentence or phrase?",
            "fields": [{"key": "kind", "label": "Kind", "options": [SENT, PHRASE]}],
            "rows": [
                {"s": "هَذَا كِتَابٌ", "ans": {"kind": "sent"}, "why": "No {ال} after {هَذَا}: \"This is a book.\""},
                {"s": "هَذَا الْكِتَابُ", "ans": {"kind": "phrase"}, "why": "With {ال}: \"this book\". We still need the Information."},
                {"s": "هَذَا الْكِتَابُ جَدِيدٌ", "ans": {"kind": "sent"}, "why": "\"This book is new.\" {جَدِيدٌ} is the Information."},
                {"s": "تِلْكَ سَيَّارَةٌ", "ans": {"kind": "sent"}, "why": "No {ال}: \"That is a car.\""},
                {"s": "تِلْكَ السَّيَّارَةُ", "ans": {"kind": "phrase"}, "why": "With {ال}: \"that car\". Not finished."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "ذَلِكَ مَسْجِدٌ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("This is a mosque.", "That is a mosque.", "that mosque")},
                 "why": "{ذَلِكَ} is far, and {مَسْجِدٌ} has no {ال}: a sentence."},
                {"s": "هَذِهِ الْغُرْفَةُ نَظِيفَةٌ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("This room is clean.", "This is a clean room.", "That room is clean.")},
                 "why": "{هَذِهِ الْغُرْفَةُ} is \"this room\". {نَظِيفَةٌ} is the Information."},
                {"s": "أُولَئِكَ طُلَّابٌ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("These are students.", "That is a student.", "Those are students.")},
                 "why": "{أُولَئِكَ} is far and plural: \"those\"."},
                {"s": "الْكِتَابُ هُنَا.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The book is here.", "The book is there.", "This is the book.")},
                 "why": "{هُنَا} means \"here\". \"There\" is {هُنَاكَ}."},
                {"s": "تِلْكَ السَّيَّارَةُ جَدِيدَةٌ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("That is a new car.", "That car is new.", "This car is new.")},
                 "why": "{تِلْكَ السَّيَّارَةُ} is \"that car\". \"That is a new car\" would be {تِلْكَ سَيَّارَةٌ جَدِيدَةٌ}."},
            ],
        },
        {
            "title": "Fixed or flexible?",
            "fields": [{"key": "type", "label": "Type", "options": [FIXED, FLEX]}],
            "rows": [
                {"s": "هَذَا", "gloss": "this", "ans": {"type": "fixed"}, "why": "A pointing word. It always ends in alif."},
                {"s": "هَذِهِ", "gloss": "this (f.)", "ans": {"type": "fixed"}, "why": "It always ends in kasra."},
                {"s": "هَذَانِ", "gloss": "these two", "ans": {"type": "flex"},
                 "why": "The exception. {هَذَانِ} becomes {هَذَيْنِ} in naṣb and jarr. Stage 4."},
                {"s": "هَؤُلَاءِ", "gloss": "these", "ans": {"type": "fixed"}, "why": "Plural in meaning, but fixed. It always ends in kasra."},
                {"s": "الْكِتَابُ", "gloss": "the book", "ans": {"type": "flex"}, "why": "A normal noun. It can be {الْكِتَابِ} after {فِي}."},
                {"s": "تِلْكَ", "gloss": "that (f.)", "ans": {"type": "fixed"}, "why": "It always ends in fatha."},
            ],
        },
        {
            "title": "Job and place of the word in [ ]",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "place", "label": "Place", "options": PLACES},
            ],
            "rows": [
                {"s": "[هَذَا] قَلَمٌ.", "gloss": "This is a pen.", "ans": {"job": "topic", "place": "raf"},
                 "why": "We talk about {هَذَا}. Topic, place of rafʿ."},
                {"s": "فِي [هَذَا] الْبَيْتِ", "gloss": "in this house", "ans": {"job": "prep", "place": "jarr"},
                 "why": "It comes after {فِي}. Place of jarr. {الْبَيْتِ} shows the kasra."},
                {"s": "كِتَابُ [هَذَا] الطَّالِبِ جَدِيدٌ.", "gloss": "This student's book is new.", "ans": {"job": "owner", "place": "jarr"},
                 "why": "The student owns the book. Owner, place of jarr."},
                {"s": "دَخَلَ [هَذَا] الرَّجُلُ الْمَسْجِدَ.", "gloss": "This man entered the mosque.", "ans": {"job": "doer", "place": "raf"},
                 "why": "This man did the action. Doer, place of rafʿ."},
                {"s": "فَتَحَ الطَّالِبُ [هَذَا] الْبَابَ.", "gloss": "The student opened this door.", "ans": {"job": "obj", "place": "nasb"},
                 "why": "The door was opened. Object, place of naṣb. {الْبَابَ} shows the fatha."},
                {"s": "[تِلْكَ] سَيَّارَةُ الْمُدِيرِ.", "gloss": "That is the principal's car.", "ans": {"job": "topic", "place": "raf"},
                 "why": "We talk about {تِلْكَ}. Topic, place of rafʿ."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Choose the pointing word",
            "fields": [{"key": "pick", "label": "Pointing word", "options": []}],
            "rows": [
                {"s": "... بِنْتٌ", "gloss": "near", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هَذَا", "هَذِهِ", "هَؤُلَاءِ")}, "why": "{بِنْتٌ} has no {ة}, but a girl is feminine: {هَذِهِ بِنْتٌ}."},
                {"s": "... الْغُرْفَةُ نَظِيفَةٌ", "gloss": "far", "ans": {"pick": "c"},
                 "opts": {"pick": pick("ذَلِكَ", "هَذِهِ", "تِلْكَ")}, "why": "Far and feminine: {تِلْكَ الْغُرْفَةُ نَظِيفَةٌ} \"That room is clean.\""},
                {"s": "... أَوْلَادٌ", "gloss": "near", "ans": {"pick": "a"},
                 "opts": {"pick": pick("هَؤُلَاءِ", "هَذَا", "أُولَئِكَ")}, "why": "A near group of people: {هَؤُلَاءِ أَوْلَادٌ}."},
                {"s": "... الرَّجُلُ تَاجِرٌ", "gloss": "far", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تِلْكَ", "ذَلِكَ", "أُولَئِكَ")}, "why": "One man, far: {ذَلِكَ الرَّجُلُ تَاجِرٌ} \"That man is a merchant.\""},
                {"s": "... نِسَاءٌ", "gloss": "far", "ans": {"pick": "b"},
                 "opts": {"pick": pick("ذَلِكَ", "أُولَئِكَ", "هَؤُلَاءِ")}, "why": "A far group of people. {أُولَئِكَ} is for men and for women. {هَؤُلَاءِ} is near."},
                {"s": "... الْمُدَرِّسَةُ فِي الْفَصْلِ", "gloss": "near", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هَذَا", "هَذِهِ", "تِلْكَ")}, "why": "{الْمُدَرِّسَةُ} ends in {ة}. Near and feminine: {هَذِهِ}."},
            ],
        },
        {
            "title": "Sentence or phrase?",
            "fields": [{"key": "kind", "label": "Kind", "options": [SENT, PHRASE]}],
            "rows": [
                {"s": "ذَلِكَ الْبَيْتُ بَعِيدٌ", "ans": {"kind": "sent"}, "why": "\"That house is far.\" {بَعِيدٌ} is the Information."},
                {"s": "هَؤُلَاءِ الطُّلَّابُ", "ans": {"kind": "phrase"}, "why": "With {ال}: \"these students\". Not finished."},
                {"s": "هَؤُلَاءِ طُلَّابٌ", "ans": {"kind": "sent"}, "why": "No {ال}: \"These are students.\""},
                {"s": "هَذِهِ هِيَ الْحَقِيبَةُ", "ans": {"kind": "sent"}, "why": "{هِيَ} in the middle makes a sentence: \"This is the bag.\""},
                {"s": "فِي ذَلِكَ الْمَسْجِدِ", "ans": {"kind": "phrase"}, "why": "\"in that mosque\". There is no Topic and Information here."},
                {"s": "أُولَئِكَ الرِّجَالُ فِي السُّوقِ", "ans": {"kind": "sent"}, "why": "\"Those men are in the market.\" {فِي السُّوقِ} is the Information."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "هَؤُلَاءِ أَوْلَادٌ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("These are boys.", "Those are boys.", "this boy")},
                 "why": "{هَؤُلَاءِ} is near and plural. {أَوْلَادٌ} has no {ال}: a sentence."},
                {"s": "ذَلِكَ الرَّجُلُ طَبِيبٌ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("That is a doctor.", "This man is a doctor.", "That man is a doctor.")},
                 "why": "{ذَلِكَ الرَّجُلُ} is \"that man\". {طَبِيبٌ} is the Information."},
                {"s": "الْمُدَرِّسُ هُنَاكَ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("The teacher is here.", "The teacher is there.", "that teacher")},
                 "why": "{هُنَاكَ} means \"there\"."},
                {"s": "هَذَا هُوَ الْمُدِيرُ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("This is the principal.", "this principal", "That is the principal.")},
                 "why": "{هُوَ} in the middle gives \"this is THE principal\"."},
                {"s": "تِلْكَ بِنْتُ الْمُدَرِّسِ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("This is the teacher's daughter.", "Those are the teacher's daughters.", "That is the teacher's daughter.")},
                 "why": "{بِنْتُ الْمُدَرِّسِ} is an iḍāfa with no {ال} on {بِنْتُ}, so it is a sentence, like {هَذَا بَيْتُ حَامِدٍ}."},
                {"s": "أُولَئِكَ الطُّلَّابُ فِي الْمَسْجِدِ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("Those are students in the mosque.", "Those students are in the mosque.", "These students are in the mosque.")},
                 "why": "{أُولَئِكَ الطُّلَّابُ} is \"those students\". {فِي الْمَسْجِدِ} is the Information."},
            ],
        },
        {
            "title": "Fixed or flexible?",
            "fields": [{"key": "type", "label": "Type", "options": [FIXED, FLEX]}],
            "rows": [
                {"s": "فِي [ذَلِكَ] الْبَيْتِ", "gloss": "in that house", "ans": {"type": "fixed"}, "why": "After {فِي} it stays {ذَلِكَ}. Only {الْبَيْتِ} shows the kasra."},
                {"s": "هَاتَانِ", "gloss": "these two (f.)", "ans": {"type": "flex"},
                 "why": "The exception. {هَاتَانِ} becomes {هَاتَيْنِ} in naṣb and jarr. Stage 4."},
                {"s": "شَكَرَ الْمُدِيرُ [أُولَئِكَ] الطُّلَّابَ.", "gloss": "The principal thanked those students.", "ans": {"type": "fixed"}, "why": "It is the object, but it stays {أُولَئِكَ}. Only {الطُّلَّابَ} shows the fatha."},
                {"s": "هُنَاكَ", "gloss": "there", "ans": {"type": "fixed"}, "why": "It always ends in fatha."},
                {"s": "بَيْتٌ", "gloss": "a house", "ans": {"type": "flex"}, "why": "A normal noun. After {فِي} it becomes {بَيْتٍ}."},
                {"s": "هُنَا", "gloss": "here", "ans": {"type": "fixed"}, "why": "It always ends in alif."},
            ],
        },
        {
            "title": "Job and place of the word in [ ]",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "place", "label": "Place", "options": PLACES},
            ],
            "rows": [
                {"s": "ذَهَبَ الْوَلَدُ إِلَى [تِلْكَ] الْمَدْرَسَةِ.", "gloss": "The boy went to that school.", "ans": {"job": "prep", "place": "jarr"},
                 "why": "It comes after {إِلَى}. Place of jarr. {الْمَدْرَسَةِ} shows the kasra."},
                {"s": "[هَؤُلَاءِ] طُلَّابٌ.", "gloss": "These are students.", "ans": {"job": "topic", "place": "raf"},
                 "why": "We talk about {هَؤُلَاءِ}. Topic, place of rafʿ. Its kasra is fixed and is not a jarr sign."},
                {"s": "كَتَبَ [هَؤُلَاءِ] الطُّلَّابُ الدَّرْسَ.", "gloss": "These students wrote the lesson.", "ans": {"job": "doer", "place": "raf"},
                 "why": "These students did the writing. Doer, place of rafʿ. {الطُّلَّابُ} shows the damma."},
                {"s": "فَتَحَ الْمُدَرِّسُ [ذَلِكَ] الْبَابَ.", "gloss": "The teacher opened that door.", "ans": {"job": "obj", "place": "nasb"},
                 "why": "The door was opened. Object, place of naṣb."},
                {"s": "بَابُ [هَذِهِ] الْغُرْفَةِ مَفْتُوحٌ.", "gloss": "The door of this room is open.", "ans": {"job": "owner", "place": "jarr"},
                 "why": "The door belongs to the room. Owner, place of jarr."},
                {"s": "خَرَجَ [أُولَئِكَ] الْأَوْلَادُ مِنَ الْمَسْجِدِ.", "gloss": "Those boys went out of the mosque.", "ans": {"job": "doer", "place": "raf"},
                 "why": "Those boys did the action. Doer, place of rafʿ. Its fatha is fixed and is not a naṣb sign."},
            ],
        },
        {
            "title": "Choose the right spelling",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "... تُجَّارٌ", "gloss": "These are merchants.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("هَؤُلَاءُ", "هَؤُلَاءَ", "هَؤُلَاءِ")}, "why": "{هَؤُلَاءِ} always ends in kasra."},
                {"s": "... جَامِعَةٌ", "gloss": "That is a university.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تِلْكَ", "تِلْكِ", "تَلْكَ")}, "why": "{تِلْكَ}: kasra on {ت}, fatha at the end."},
                {"s": "... حَقِيبَةٌ", "gloss": "This is a bag.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هَاذِهِ", "هَذِهِ", "هَذِهُ")}, "why": "The ā after {هـ} is not written, and the ending is always kasra."},
                {"s": "... أَوْلَادٌ", "gloss": "Those are boys.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("أُولَئِكَ", "أُولَئِكِ", "أُلَائِكَ")}, "why": "Written with {و}, said ulāʾika. It always ends in fatha."},
                {"s": "... دُكَّانٌ", "gloss": "That is a shop.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("ذَالِكَ", "ذَلِكِ", "ذَلِكَ")}, "why": "The ā after {ذ} is not written, and the ending is always fatha."},
            ],
        },
    ],
}
