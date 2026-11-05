# Stage 0 · Unit 2: Ism, fiʿl and ḥarf (الْكَلِمَةُ: اِسْمٌ وَفِعْلٌ وَحَرْفٌ)

KIND = {"key": "kind", "label": "Kind", "options": [
    {"k": "ism", "label": "Ism · اِسْمٌ", "color": "blue"},
    {"k": "fil", "label": "Fiʿl · فِعْلٌ", "color": "navy"},
    {"k": "harf", "label": "Ḥarf · حَرْفٌ", "color": "grey"}]}

SIGN = {"key": "sign", "label": "Sign", "options": [
    {"k": "al", "label": "It has ال"},
    {"k": "tan", "label": "It has tanween", "color": "olive"},
    {"k": "prep", "label": "After a preposition", "color": "green"},
    {"k": "ya", "label": "After يَا"}]}

PICK = {"key": "pick", "label": "Answer", "options": []}

UNIT = {
    "id": "s0-kalima",
    "order": 2,
    "title": "Ism, fiʿl and ḥarf",
    "ar": "الْكَلِمَةُ: اِسْمٌ وَفِعْلٌ وَحَرْفٌ",
    "blurb": "Every Arabic word is an ism, a fiʿl or a ḥarf. Learn the signs that tell them apart.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 0 · UNIT 2", "title": "Three kinds of word",
         "text": "Every Arabic word belongs to one of three kinds. Grammar starts by knowing which kind you are reading.",
         "wm": "اِسْمٌ فِعْلٌ حَرْفٌ"},

        {"t": "h2", "text": "One word, one kind"},
        {"t": "cols", "items": [
            {"color": "blue", "title": "Ism", "ar": "اِسْمٌ", "text": "A name: a person, thing, place or quality. {كِتَابٌ}، {مُحَمَّدٌ}، {جَدِيدٌ}"},
            {"color": "navy", "title": "Fiʿl", "ar": "فِعْلٌ", "text": "An action with a time. {ذَهَبَ} he went"},
            {"color": "grey", "title": "Ḥarf", "ar": "حَرْفٌ", "text": "A small word. It has meaning only with other words. {فِي} in"}]},
        {"t": "examples", "items": [
            {"ar": "ذَهَبَ الطَّالِبُ إِلَى الْمَسْجِدِ.", "en": "The student went to the mosque.",
             "note": "{ذَهَبَ} fiʿl, {الطَّالِبُ} ism, {إِلَى} ḥarf, {الْمَسْجِدِ} ism."}]},

        {"t": "h2", "text": "The ism and its four signs"},
        {"t": "p", "text": "An ism names something. It can be a person ({طَبِيبٌ}), a thing ({قَلَمٌ}), a place ({الْمَدْرَسَةُ}) or a quality ({كَبِيرٌ})."},
        {"t": "table", "head": ["Sign", "Example", "Meaning"], "rows": [
            ["It can take {ال}", "{الْبَيْتُ}", "the house"],
            ["It can take tanween", "{بَيْتٌ}", "a house"],
            ["It can come after a preposition", "{فِي الْبَيْتِ}", "in the house"],
            ["It can come after {يَا}", "{يَا وَلَدُ}", "O boy"]]},
        {"t": "rule", "color": "blue", "title": "One sign is enough",
         "text": "If a word can take any one of these signs, it is an ism. A fiʿl or a ḥarf never takes them."},

        {"t": "h2", "text": "Fixed isms"},
        {"t": "p", "text": "Some isms never take {ال} or tanween. They still stand for a person or a thing, so they are isms. "
                           "Their ending never changes. We call them fixed ({مَبْنِيٌّ})."},
        {"t": "words", "items": [
            {"ar": "هَذَا", "sub": "this", "color": "blue"},
            {"ar": "ذَلِكَ", "sub": "that", "color": "blue"},
            {"ar": "هُوَ", "sub": "he, it", "color": "blue"},
            {"ar": "هِيَ", "sub": "she, it", "color": "blue"},
            {"ar": "أَنَا", "sub": "I", "color": "blue"},
            {"ar": "أَنْتَ", "sub": "you", "color": "blue"},
            {"ar": "مَنْ", "sub": "who?", "color": "blue"},
            {"ar": "مَا", "sub": "what?", "color": "blue"},
            {"ar": "أَيْنَ", "sub": "where?", "color": "blue"}]},
        {"t": "examples", "items": [
            {"ar": "مِنْ أَيْنَ أَنْتَ؟", "en": "Where are you from?", "note": "{أَيْنَ} comes after the preposition {مِنْ}. That is an ism sign."},
            {"ar": "هَذَا كِتَابٌ.", "en": "This is a book.", "note": "{هَذَا} stands for the book, so it is an ism."}]},

        {"t": "h2", "text": "The fiʿl"},
        {"t": "p", "text": "A fiʿl is an action that happened at a time. In Stage 0 we only see past verbs. Most end in a fatha."},
        {"t": "words", "items": [
            {"ar": "ذَهَبَ", "sub": "he went", "color": "navy"},
            {"ar": "خَرَجَ", "sub": "he went out", "color": "navy"},
            {"ar": "كَتَبَ", "sub": "he wrote", "color": "navy"},
            {"ar": "جَلَسَ", "sub": "he sat", "color": "navy"},
            {"ar": "دَخَلَ", "sub": "he entered", "color": "navy"},
            {"ar": "فَتَحَ", "sub": "he opened", "color": "navy"}]},
        {"t": "tip", "text": "A fiʿl never takes {ال} or tanween, and it never comes after a preposition or {يَا}."},

        {"t": "h2", "text": "The ḥarf"},
        {"t": "p", "text": "A ḥarf links or changes other words. On its own it means very little."},
        {"t": "words", "items": [
            {"ar": "فِي", "sub": "in", "color": "grey"},
            {"ar": "عَلَى", "sub": "on", "color": "grey"},
            {"ar": "مِنْ", "sub": "from", "color": "grey"},
            {"ar": "إِلَى", "sub": "to", "color": "grey"},
            {"ar": "وَ", "sub": "and", "color": "grey"},
            {"ar": "أَ", "sub": "question: is…?", "color": "grey"},
            {"ar": "يَا", "sub": "O (calling)", "color": "grey"},
            {"ar": "لَا", "sub": "no", "color": "grey"},
            {"ar": "نَعَمْ", "sub": "yes", "color": "grey"}]},
        {"t": "tip", "text": "{وَ} and {أَ} are written joined to the next word: {وَذَلِكَ}، {أَهَذَا}. They are still separate words."},
        {"t": "tip", "text": "Watch the first vowel. {مِنْ} (min, from) is a ḥarf. {مَنْ} (man, who?) is an ism."},

        {"t": "h2", "text": "Sorting a whole sentence"},
        {"t": "examples", "items": [
            {"ar": "أَهَذَا بَيْتٌ؟ نَعَمْ، هَذَا بَيْتٌ.", "en": "Is this a house? Yes, this is a house.",
             "note": "{أَ} ḥarf, {هَذَا} ism, {بَيْتٌ} ism, {نَعَمْ} ḥarf."},
            {"ar": "خَرَجَ الْمُدَرِّسُ مِنَ الْفَصْلِ.", "en": "The teacher went out of the classroom.",
             "note": "{خَرَجَ} fiʿl, {الْمُدَرِّسُ} ism, {مِنَ} ḥarf, {الْفَصْلِ} ism."}]},

        {"t": "summary", "title": "In three questions", "items": [
            "Can it take {ال}, tanween, a preposition before it, or {يَا}? Then it is an ism.",
            "Is it an action in the past, like {ذَهَبَ}? Then it is a fiʿl.",
            "Does it only work with other words, like {فِي} or {وَ}? Then it is a ḥarf."]},
    ],

    "practice": [
        {"title": "Ism, fiʿl or ḥarf?",
         "prompt": "أَهَذَا بَيْتٌ؟ لَا، هَذَا مَسْجِدٌ.",
         "en": "Is this a house? No, this is a mosque.",
         "fields": [KIND],
         "rows": [
             {"s": "أَ", "gloss": "is…? (question)", "ans": {"kind": "harf"}, "why": "{أَ} turns a sentence into a question. It needs other words."},
             {"s": "هَذَا", "gloss": "this", "ans": {"kind": "ism"}, "why": "{هَذَا} stands for a thing. It is a fixed ism."},
             {"s": "بَيْتٌ", "gloss": "a house", "ans": {"kind": "ism"}, "why": "It has tanween and names a thing."},
             {"s": "لَا", "gloss": "no", "ans": {"kind": "harf"}, "why": "{لَا} answers a question. It names nothing."},
             {"s": "مَسْجِدٌ", "gloss": "a mosque", "ans": {"kind": "ism"}, "why": "It has tanween and names a place."}]},

        {"title": "Ism, fiʿl or ḥarf?",
         "prompt": "ذَهَبَ الطَّالِبُ إِلَى الْمَسْجِدِ.",
         "en": "The student went to the mosque.",
         "fields": [KIND],
         "rows": [
             {"s": "ذَهَبَ", "gloss": "went", "ans": {"kind": "fil"}, "why": "A past action: {ذَهَبَ} he went."},
             {"s": "الطَّالِبُ", "gloss": "the student", "ans": {"kind": "ism"}, "why": "It has {ال} and names a person."},
             {"s": "إِلَى", "gloss": "to", "ans": {"kind": "harf"}, "why": "A preposition. It means to only with a word after it."},
             {"s": "الْمَسْجِدِ", "gloss": "the mosque", "ans": {"kind": "ism"}, "why": "It has {ال} and comes after a preposition."}]},

        {"title": "Ism, fiʿl or ḥarf?",
         "prompt": "أَيْنَ الْكِتَابُ؟ هُوَ عَلَى الْمَكْتَبِ.",
         "en": "Where is the book? It is on the desk.",
         "fields": [KIND],
         "rows": [
             {"s": "أَيْنَ", "gloss": "where?", "ans": {"kind": "ism"}, "why": "A fixed ism. It can follow a preposition: {مِنْ أَيْنَ}."},
             {"s": "الْكِتَابُ", "gloss": "the book", "ans": {"kind": "ism"}, "why": "It has {ال} and names a thing."},
             {"s": "هُوَ", "gloss": "it", "ans": {"kind": "ism"}, "why": "{هُوَ} stands for the book. It is a fixed ism."},
             {"s": "عَلَى", "gloss": "on", "ans": {"kind": "harf"}, "why": "A preposition. It needs a word after it."},
             {"s": "الْمَكْتَبِ", "gloss": "the desk", "ans": {"kind": "ism"}, "why": "It has {ال} and comes after {عَلَى}."}]},

        {"title": "Sort the single words",
         "fields": [KIND],
         "rows": [
             {"s": "قَلَمٌ", "gloss": "a pen", "ans": {"kind": "ism"}, "why": "It has tanween and names a thing."},
             {"s": "كَتَبَ", "gloss": "he wrote", "ans": {"kind": "fil"}, "why": "A past action."},
             {"s": "مِنْ", "gloss": "from", "ans": {"kind": "harf"}, "why": "A preposition with kasra: min."},
             {"s": "جَلَسَ", "gloss": "he sat", "ans": {"kind": "fil"}, "why": "A past action."},
             {"s": "نَعَمْ", "gloss": "yes", "ans": {"kind": "harf"}, "why": "An answer word. It names nothing."},
             {"s": "ذَلِكَ", "gloss": "that", "ans": {"kind": "ism"}, "why": "It points to a thing. A fixed ism."}]},

        {"title": "Which sign shows it is an ism?",
         "fields": [SIGN],
         "rows": [
             {"s": "الْبَابُ", "gloss": "the door", "ans": {"sign": "al"}, "why": "It starts with {ال}."},
             {"s": "رَجُلٌ", "gloss": "a man", "ans": {"sign": "tan"}, "why": "It ends in tanween: rajulun."},
             {"s": "يَا خَالِدُ", "gloss": "O Khālid", "ans": {"sign": "ya"}, "why": "{خَالِدُ} comes after {يَا}. After {يَا} the name has one damma."},
             {"s": "مِنْ أَيْنَ", "gloss": "from where? (look at the second word)", "ans": {"sign": "prep"}, "why": "{أَيْنَ} comes after the preposition {مِنْ}."},
             {"s": "حِصَانٌ", "gloss": "a horse", "ans": {"sign": "tan"}, "why": "It ends in tanween: ḥiṣānun."}]},

        {"title": "Ism, fiʿl or ḥarf?",
         "prompt": "خَرَجَ الْمُدَرِّسُ مِنَ الْفَصْلِ.",
         "en": "The teacher went out of the classroom.",
         "fields": [KIND],
         "rows": [
             {"s": "خَرَجَ", "gloss": "went out", "ans": {"kind": "fil"}, "why": "A past action: {خَرَجَ} he went out."},
             {"s": "الْمُدَرِّسُ", "gloss": "the teacher", "ans": {"kind": "ism"}, "why": "It has {ال} and names a person."},
             {"s": "مِنَ", "gloss": "from", "ans": {"kind": "harf"}, "why": "This is {مِنْ}. Before {ال} it is read {مِنَ}."},
             {"s": "الْفَصْلِ", "gloss": "the classroom", "ans": {"kind": "ism"}, "why": "It has {ال} and comes after a preposition."}]},
    ],

    "homework": [
        {"title": "Ism, fiʿl or ḥarf?",
         "prompt": "مِنْ أَيْنَ أَنْتَ؟ أَنَا مِنَ الْهِنْدِ.",
         "en": "Where are you from? I am from India.",
         "fields": [KIND],
         "rows": [
             {"s": "مِنْ", "gloss": "from", "ans": {"kind": "harf"}, "why": "A preposition: min."},
             {"s": "أَيْنَ", "gloss": "where?", "ans": {"kind": "ism"}, "why": "A fixed ism. Here it comes after {مِنْ}."},
             {"s": "أَنْتَ", "gloss": "you", "ans": {"kind": "ism"}, "why": "It stands for a person. A fixed ism."},
             {"s": "أَنَا", "gloss": "I", "ans": {"kind": "ism"}, "why": "It stands for a person. A fixed ism."},
             {"s": "الْهِنْدِ", "gloss": "India", "ans": {"kind": "ism"}, "why": "The name of a place, with {ال}, after a preposition."}]},

        {"title": "Ism, fiʿl or ḥarf?",
         "prompt": "خَرَجَ حَامِدٌ مِنَ الْغُرْفَةِ وَذَهَبَ إِلَى الْحَمَّامِ.",
         "en": "Ḥāmid went out of the room and went to the bathroom.",
         "fields": [KIND],
         "rows": [
             {"s": "خَرَجَ", "gloss": "went out", "ans": {"kind": "fil"}, "why": "A past action."},
             {"s": "حَامِدٌ", "gloss": "Ḥāmid", "ans": {"kind": "ism"}, "why": "A name with tanween."},
             {"s": "الْغُرْفَةِ", "gloss": "the room", "ans": {"kind": "ism"}, "why": "It has {ال} and comes after {مِنَ}."},
             {"s": "وَ", "gloss": "and", "ans": {"kind": "harf"}, "why": "{وَ} joins words. It is written joined to {ذَهَبَ}."},
             {"s": "ذَهَبَ", "gloss": "went", "ans": {"kind": "fil"}, "why": "A past action, after {وَ}."},
             {"s": "إِلَى", "gloss": "to", "ans": {"kind": "harf"}, "why": "A preposition."}]},

        {"title": "Ism, fiʿl or ḥarf?",
         "prompt": "أَذَهَبَ عَلِيٌّ إِلَى الْمُدِيرِ؟ نَعَمْ.",
         "en": "Did ʿAlī go to the principal? Yes.",
         "fields": [KIND],
         "rows": [
             {"s": "أَ", "gloss": "question", "ans": {"kind": "harf"}, "why": "The question {أَ}, written joined to {ذَهَبَ}."},
             {"s": "ذَهَبَ", "gloss": "went", "ans": {"kind": "fil"}, "why": "A past action. {أَ} in front does not change that."},
             {"s": "عَلِيٌّ", "gloss": "ʿAlī", "ans": {"kind": "ism"}, "why": "A name with tanween: ʿaliyyun."},
             {"s": "إِلَى", "gloss": "to", "ans": {"kind": "harf"}, "why": "A preposition."},
             {"s": "الْمُدِيرِ", "gloss": "the principal", "ans": {"kind": "ism"}, "why": "It has {ال} and comes after {إِلَى}."},
             {"s": "نَعَمْ", "gloss": "yes", "ans": {"kind": "harf"}, "why": "An answer word."}]},

        {"title": "Sort the single words",
         "fields": [KIND],
         "rows": [
             {"s": "مَا", "gloss": "what?", "ans": {"kind": "ism"}, "why": "It stands for a thing: {مَا هَذَا؟} A fixed ism."},
             {"s": "شَرِبَ", "gloss": "he drank", "ans": {"kind": "fil"}, "why": "A past action."},
             {"s": "هِيَ", "gloss": "she, it", "ans": {"kind": "ism"}, "why": "It stands for a person or thing. A fixed ism."},
             {"s": "قَرَأَ", "gloss": "he read", "ans": {"kind": "fil"}, "why": "A past action."},
             {"s": "يَا", "gloss": "O (calling)", "ans": {"kind": "harf"}, "why": "It calls the ism after it. It names nothing."},
             {"s": "وَ", "gloss": "and", "ans": {"kind": "harf"}, "why": "It joins words."}]},

        {"title": "Pick the right word",
         "fields": [PICK],
         "rows": [
             {"s": "Which word is a fiʿl?", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "الْمِفْتَاحُ"}, {"k": "b", "label": "فَتَحَ"}, {"k": "c", "label": "عَلَى"}]},
              "why": "{فَتَحَ} he opened: a past action. {الْمِفْتَاحُ} the key has {ال}."},
             {"s": "Which word is an ism?", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "مِنْ"}, {"k": "b", "label": "مَنْ"}, {"k": "c", "label": "إِلَى"}]},
              "why": "{مَنْ} (man) means who? and is an ism. {مِنْ} (min) is a ḥarf."},
             {"s": "Which word is a ḥarf?", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "أَنْتَ"}, {"k": "b", "label": "فِي"}, {"k": "c", "label": "الطَّبِيبُ"}]},
              "why": "{فِي} in is a preposition. {أَنْتَ} is a fixed ism."},
             {"s": "Which word is an ism?", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "لَا"}, {"k": "b", "label": "الْيَدُ"}, {"k": "c", "label": "كَتَبَ"}]},
              "why": "{الْيَدُ} the hand has {ال}."},
             {"s": "Which word is a fiʿl?", "ans": {"pick": "c"},
              "opts": {"pick": [{"k": "a", "label": "هَذَا"}, {"k": "b", "label": "نَعَمْ"}, {"k": "c", "label": "دَخَلَ"}]},
              "why": "{دَخَلَ} he entered: a past action."}]},

        {"title": "Which sign shows it is an ism?",
         "fields": [SIGN],
         "rows": [
             {"s": "الْقَمَرُ", "gloss": "the moon", "ans": {"sign": "al"}, "why": "It starts with {ال}."},
             {"s": "جَمَلٌ", "gloss": "a camel", "ans": {"sign": "tan"}, "why": "It ends in tanween: jamalun."},
             {"s": "يَا شَيْخُ", "gloss": "O Sheikh", "ans": {"sign": "ya"}, "why": "{شَيْخُ} comes after {يَا}. It has no {ال} and no tanween here."},
             {"s": "مِنْ هُنَا", "gloss": "from here (look at the second word)", "ans": {"sign": "prep"}, "why": "{هُنَا} here comes after {مِنْ}. It is a fixed ism."},
             {"s": "يَا أُسْتَاذُ", "gloss": "O teacher", "ans": {"sign": "ya"}, "why": "{أُسْتَاذُ} comes after {يَا}."}]},
    ],
}
