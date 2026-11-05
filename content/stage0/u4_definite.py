MN = {"key": "def", "label": "Definite?", "options": [
    {"k": "m", "label": "Maʿrifa · مَعْرِفَةٌ", "color": "teal"},
    {"k": "n", "label": "Nakira · نَكِرَةٌ", "color": "brown"}]}

OKBAD = {"key": "check", "label": "Right or wrong?", "options": [
    {"k": "ok", "label": "Correct"},
    {"k": "bad", "label": "Mistake"}]}

PICK = {"key": "pick", "label": "Correct form", "options": []}

UNIT = {
    "id": "s0-definite",
    "order": 4,
    "title": "Definite and indefinite",
    "ar": "الْمَعْرِفَةُ وَالنَّكِرَةُ",
    "blurb": "A book or the book? Tanween, ال, names and pronouns.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 0 · UNIT 4", "title": "A book or the book?",
         "text": "Every ism is either indefinite, 'a book', or definite, 'the book'. The start and the end of the word tell you which.",
         "wm": "الْمَعْرِفَةُ وَالنَّكِرَةُ"},

        {"t": "h2", "text": "Nakira: 'a book'"},
        {"t": "p", "text": "A nakira {نَكِرَةٌ} is any one thing, not a known one. In English we say 'a' or 'an'. In Arabic the sign is tanween on the last letter."},
        {"t": "words", "items": [
            {"ar": "كِتَابٌ", "label": "kitābun", "sub": "a book", "color": "brown"},
            {"ar": "بَيْتٌ", "label": "baytun", "sub": "a house", "color": "brown"},
            {"ar": "قَلَمٌ", "label": "qalamun", "sub": "a pen", "color": "brown"},
            {"ar": "مَدْرَسَةٌ", "label": "madrasatun", "sub": "a school", "color": "brown"}]},
        {"t": "examples", "items": [
            {"ar": "هَذَا كِتَابٌ.", "en": "This is a book.", "note": "The tanween on {كِتَابٌ} means 'a'."},
            {"ar": "مَا ذَلِكَ؟ ذَلِكَ نَجْمٌ.", "en": "What is that? That is a star."}]},

        {"t": "h2", "text": "Maʿrifa with ال: 'the book'"},
        {"t": "p", "text": "A maʿrifa {مَعْرِفَةٌ} is a known, specific thing: 'the book'. The most common way to make one is to put {ال} in front."},
        {"t": "rule", "color": "teal", "title": "Adding ال",
         "text": "Put {ال} in front. The tanween drops, and the last letter keeps a single vowel: {كِتَابٌ} becomes {الْكِتَابُ}."},
        {"t": "table", "head": ["Nakira", "Maʿrifa", "English"], "rows": [
            ["كِتَابٌ", "الْكِتَابُ", "a book / the book"],
            ["بَيْتٌ", "الْبَيْتُ", "a house / the house"],
            ["قَلَمٌ", "الْقَلَمُ", "a pen / the pen"],
            ["مَدْرَسَةٌ", "الْمَدْرَسَةُ", "a school / the school"],
            ["وَلَدٌ", "الْوَلَدُ", "a boy / the boy"]]},
        {"t": "rule", "color": "red", "title": "Never both",
         "text": "A word never has {ال} and tanween together. {الْكِتَابٌ} is always wrong. Write {الْكِتَابُ}."},

        {"t": "h2", "text": "Other definite words"},
        {"t": "p", "text": "Some words are definite without {ال}. They point to one known person or thing."},
        {"t": "cols", "items": [
            {"color": "teal", "title": "Names", "ar": "مُحَمَّدٌ", "text": "{خَالِدٌ}, {حَامِدٌ}, {آمِنَةُ}"},
            {"color": "teal", "title": "Pronouns", "ar": "هُوَ", "text": "{هِيَ}, {أَنَا}, {أَنْتَ}"},
            {"color": "teal", "title": "Pointing words", "ar": "هَذَا", "text": "{ذَلِكَ}"},
            {"color": "teal", "title": "Owned by a definite noun", "ar": "كِتَابُ الطَّالِبِ", "text": "the student's book (unit 6)"}]},
        {"t": "tip", "text": "{مُحَمَّدٌ} has tanween, but it is still definite. It means Muhammad, one known person, not 'a Muhammad'. On a name, tanween does not mean 'a' (Madinah lesson 4)."},
        {"t": "p", "text": "Feminine names like {آمِنَةُ} and {زَيْنَبُ} have no tanween at all. They are definite too."},

        {"t": "h2", "text": "Preview: the owned word"},
        {"t": "p", "text": "In {كِتَابُ الطَّالِبِ} 'the student's book', the first word has no {ال} and no tanween. It is definite because it belongs to a definite word. Unit 6 covers this."},
        {"t": "examples", "items": [
            {"ar": "كِتَابُ الطَّالِبِ", "en": "the student's book"},
            {"ar": "بَيْتُ الْإِمَامِ", "en": "the imam's house"},
            {"ar": "كِتَابُ مُحَمَّدٍ", "en": "Muhammad's book"}]},

        {"t": "h2", "text": "Why it matters"},
        {"t": "p", "text": "Most simple sentences start with a maʿrifa and end with a nakira. Stage 1 builds on this pattern."},
        {"t": "examples", "items": [
            {"ar": "الْبَابُ مَفْتُوحٌ.", "en": "The door is open.", "note": "{الْبَابُ} is maʿrifa. {مَفْتُوحٌ} is nakira."},
            {"ar": "الْكِتَابُ جَدِيدٌ.", "en": "The book is new."},
            {"ar": "مُحَمَّدٌ طَالِبٌ.", "en": "Muhammad is a student.", "note": "Both have tanween. {مُحَمَّدٌ} is a name, so it is maʿrifa. {طَالِبٌ} is nakira."}]},
        {"t": "tip", "text": "Adjectives like {مَفْتُوحٌ} 'open' are nakira, but English does not say 'a' with them."},

        {"t": "summary", "title": "In four lines", "items": [
            "Tanween usually means nakira: {كِتَابٌ} 'a book'.",
            "{ال} makes a maʿrifa, and the tanween drops: {الْكِتَابُ} 'the book'.",
            "Names, pronouns, {هَذَا} and {ذَلِكَ} are maʿrifa, even {مُحَمَّدٌ} with its tanween.",
            "Never {ال} and tanween together: {الْكِتَابٌ} is wrong."]},
    ],

    "practice": [
        {"title": "Maʿrifa or nakira?", "fields": [MN], "rows": [
            {"s": "كِتَابٌ", "gloss": "book", "ans": {"def": "n"}, "why": "Tanween and no {ال}: 'a book'."},
            {"s": "الْقَلَمُ", "gloss": "pen", "ans": {"def": "m"}, "why": "It has {ال}: 'the pen'."},
            {"s": "بَيْتٌ", "gloss": "house", "ans": {"def": "n"}, "why": "Tanween: 'a house'."},
            {"s": "الْمَسْجِدُ", "gloss": "mosque", "ans": {"def": "m"}, "why": "It has {ال}: 'the mosque'."},
            {"s": "مَدْرَسَةٌ", "gloss": "school", "ans": {"def": "n"}, "why": "Tanween on {ة}: 'a school'."},
            {"s": "الْغُرْفَةُ", "gloss": "room", "ans": {"def": "m"}, "why": "It has {ال}: 'the room'."}]},

        {"title": "Maʿrifa or nakira? (no ال here)", "fields": [MN], "rows": [
            {"s": "هُوَ", "gloss": "he", "ans": {"def": "m"}, "why": "A pronoun is always maʿrifa."},
            {"s": "مُحَمَّدٌ", "gloss": "Muhammad", "ans": {"def": "m"}, "why": "A name is maʿrifa. Its tanween does not mean 'a'."},
            {"s": "هَذَا", "gloss": "this", "ans": {"def": "m"}, "why": "A pointing word is maʿrifa."},
            {"s": "وَلَدٌ", "gloss": "boy", "ans": {"def": "n"}, "why": "An ordinary noun with tanween: 'a boy'."},
            {"s": "آمِنَةُ", "gloss": "Amina", "ans": {"def": "m"}, "why": "A name is maʿrifa."},
            {"s": "سَاعَةٌ", "gloss": "watch", "ans": {"def": "n"}, "why": "An ordinary noun with tanween: 'a watch'."}]},

        {"title": "Add ال: which form is right?", "fields": [PICK], "rows": [
            {"s": "كِتَابٌ → the book", "ans": {"pick": "b"},
             "opts": {"pick": [{"k": "a", "label": "الْكِتَابٌ"}, {"k": "b", "label": "الْكِتَابُ"}, {"k": "c", "label": "كِتَابُ"}]},
             "why": "{ال} in, tanween out: {الْكِتَابُ}."},
            {"s": "بَيْتٌ → the house", "ans": {"pick": "a"},
             "opts": {"pick": [{"k": "a", "label": "الْبَيْتُ"}, {"k": "b", "label": "الْبَيْتٌ"}, {"k": "c", "label": "بَيْتُ"}]},
             "why": "One damma only after {ال}: {الْبَيْتُ}."},
            {"s": "قَلَمٌ → the pen", "ans": {"pick": "c"},
             "opts": {"pick": [{"k": "a", "label": "قَلَمُ"}, {"k": "b", "label": "الْقَلَمٌ"}, {"k": "c", "label": "الْقَلَمُ"}]},
             "why": "{الْقَلَمُ}: {ال} and a single damma."},
            {"s": "مَدْرَسَةٌ → the school", "ans": {"pick": "b"},
             "opts": {"pick": [{"k": "a", "label": "الْمَدْرَسَةٌ"}, {"k": "b", "label": "الْمَدْرَسَةُ"}, {"k": "c", "label": "مَدْرَسَةُ"}]},
             "why": "The {ة} keeps a single damma: {الْمَدْرَسَةُ}."},
            {"s": "مِفْتَاحٌ → the key", "ans": {"pick": "a"},
             "opts": {"pick": [{"k": "a", "label": "الْمِفْتَاحُ"}, {"k": "b", "label": "الْمِفْتَاحٌ"}, {"k": "c", "label": "مِفْتَاحُ"}]},
             "why": "{الْمِفْتَاحُ}: no tanween after {ال}."}]},

        {"title": "Spot the mistake", "fields": [OKBAD], "rows": [
            {"s": "الْكِتَابٌ", "ans": {"check": "bad"}, "why": "{ال} and tanween together. Write {الْكِتَابُ}."},
            {"s": "الْبَابُ", "ans": {"check": "ok"}, "why": "{ال} with a single damma. Correct."},
            {"s": "الْقَمِيصٌ", "ans": {"check": "bad"}, "why": "{ال} and tanween together. Write {الْقَمِيصُ}."},
            {"s": "حِمَارٌ", "ans": {"check": "ok"}, "why": "No {ال}, so tanween is right: 'a donkey'."},
            {"s": "الْمَطْبَخُ", "ans": {"check": "ok"}, "why": "{ال} with a single damma. Correct."}]},

        {"title": "Maʿrifa or nakira? Tap each word.",
         "prompt": "الْكِتَابُ جَدِيدٌ وَالْقَلَمُ قَدِيمٌ.", "en": "The book is new and the pen is old.",
         "fields": [MN], "rows": [
            {"s": "الْكِتَابُ", "gloss": "the book", "ans": {"def": "m"}, "why": "It has {ال}."},
            {"s": "جَدِيدٌ", "gloss": "new", "ans": {"def": "n"}, "why": "Tanween, no {ال}."},
            {"s": "الْقَلَمُ", "gloss": "the pen", "ans": {"def": "m"}, "why": "It has {ال}. The {وَ} in front does not change that."},
            {"s": "قَدِيمٌ", "gloss": "old", "ans": {"def": "n"}, "why": "Tanween, no {ال}."}]},

        {"title": "Maʿrifa or nakira? Tap each word.",
         "prompt": "هَذَا كِتَابٌ وَذَلِكَ قَلَمٌ.", "en": "This is a book and that is a pen.",
         "fields": [MN], "rows": [
            {"s": "هَذَا", "gloss": "this", "ans": {"def": "m"}, "why": "A pointing word is maʿrifa."},
            {"s": "كِتَابٌ", "gloss": "a book", "ans": {"def": "n"}, "why": "Tanween: 'a book'."},
            {"s": "ذَلِكَ", "gloss": "that", "ans": {"def": "m"}, "why": "A pointing word is maʿrifa."},
            {"s": "قَلَمٌ", "gloss": "a pen", "ans": {"def": "n"}, "why": "Tanween: 'a pen'."}]},
    ],

    "homework": [
        {"title": "Maʿrifa or nakira?", "fields": [MN], "rows": [
            {"s": "خَالِدٌ", "gloss": "Khalid", "ans": {"def": "m"}, "why": "A name. Tanween on a name does not make it nakira."},
            {"s": "الدُّكَّانُ", "gloss": "shop", "ans": {"def": "m"}, "why": "It has {ال}: 'the shop'."},
            {"s": "حَقِيبَةٌ", "gloss": "bag", "ans": {"def": "n"}, "why": "An ordinary noun with tanween: 'a bag'."},
            {"s": "أَنْتَ", "gloss": "you", "ans": {"def": "m"}, "why": "A pronoun is maʿrifa."},
            {"s": "أَنَا", "gloss": "I", "ans": {"def": "m"}, "why": "A pronoun is maʿrifa."},
            {"s": "جَمَلٌ", "gloss": "camel", "ans": {"def": "n"}, "why": "An ordinary noun with tanween: 'a camel'."}]},

        {"title": "What makes it definite?", "fields": [{"key": "why", "label": "Reason", "options": [
            {"k": "al", "label": "Has ال", "color": "teal"},
            {"k": "name", "label": "A name", "color": "teal"},
            {"k": "pron", "label": "A pronoun", "color": "teal"},
            {"k": "point", "label": "هَذَا / ذَلِكَ", "color": "teal"},
            {"k": "owned", "label": "Owned by a definite word", "color": "teal"},
            {"k": "none", "label": "Not definite (nakira)", "color": "brown"}]}],
         "rows": [
            {"s": "الْمُدِيرُ", "gloss": "principal", "ans": {"why": "al"}, "why": "It starts with {ال}."},
            {"s": "حَامِدٌ", "gloss": "Hamid", "ans": {"why": "name"}, "why": "A name, even with tanween."},
            {"s": "هِيَ", "gloss": "she", "ans": {"why": "pron"}, "why": "{هِيَ} is a pronoun."},
            {"s": "ذَلِكَ", "gloss": "that", "ans": {"why": "point"}, "why": "{ذَلِكَ} points to one known thing."},
            {"s": "بَيْتُ الْإِمَامِ", "gloss": "the imam's house (first word)", "ans": {"why": "owned"}, "why": "{بَيْتُ} has no {ال} and no tanween. It belongs to {الْإِمَامِ}, which is definite."},
            {"s": "دَفْتَرٌ", "gloss": "notebook", "ans": {"why": "none"}, "why": "An ordinary noun with tanween: 'a notebook'."}]},

        {"title": "Add ال: which form is right?", "fields": [PICK], "rows": [
            {"s": "حَقِيبَةٌ → the bag", "ans": {"pick": "c"},
             "opts": {"pick": [{"k": "a", "label": "الْحَقِيبَةٌ"}, {"k": "b", "label": "حَقِيبَةُ"}, {"k": "c", "label": "الْحَقِيبَةُ"}]},
             "why": "{الْحَقِيبَةُ}: {ال} and a single damma on {ة}."},
            {"s": "كُرْسِيٌّ → the chair", "ans": {"pick": "b"},
             "opts": {"pick": [{"k": "a", "label": "الْكُرْسِيٌّ"}, {"k": "b", "label": "الْكُرْسِيُّ"}, {"k": "c", "label": "كُرْسِيُّ"}]},
             "why": "Keep the shadda, drop the tanween: {الْكُرْسِيُّ}."},
            {"s": "مَكْتَبٌ → the desk", "ans": {"pick": "a"},
             "opts": {"pick": [{"k": "a", "label": "الْمَكْتَبُ"}, {"k": "b", "label": "الْمَكْتَبٌ"}, {"k": "c", "label": "مَكْتَبُ"}]},
             "why": "{الْمَكْتَبُ}: no tanween after {ال}."},
            {"s": "فَصْلٌ → the classroom", "ans": {"pick": "b"},
             "opts": {"pick": [{"k": "a", "label": "فَصْلُ"}, {"k": "b", "label": "الْفَصْلُ"}, {"k": "c", "label": "الْفَصْلٌ"}]},
             "why": "{الْفَصْلُ}: {ال} and a single damma."},
            {"s": "جَمَلٌ → the camel", "ans": {"pick": "c"},
             "opts": {"pick": [{"k": "a", "label": "الْجَمَلٌ"}, {"k": "b", "label": "جَمَلُ"}, {"k": "c", "label": "الْجَمَلُ"}]},
             "why": "{الْجَمَلُ}, as in Madinah lesson 3."}]},

        {"title": "Spot the mistake", "fields": [OKBAD], "rows": [
            {"s": "الْوَلَدٌ", "ans": {"check": "bad"}, "why": "{ال} and tanween together. Write {الْوَلَدُ}."},
            {"s": "الْجَامِعَةُ", "ans": {"check": "ok"}, "why": "{ال} with a single damma. Correct."},
            {"s": "الْغُرْفَةٌ", "ans": {"check": "bad"}, "why": "{ال} and tanween together. Write {الْغُرْفَةُ}."},
            {"s": "سَعِيدٌ", "ans": {"check": "ok"}, "why": "A name with tanween is correct, and it is definite."},
            {"s": "الْكُرْسِيُّ", "ans": {"check": "ok"}, "why": "{ال} with a single damma on the shadda {ي}. Correct."},
            {"s": "الْحِصَانٌ", "ans": {"check": "bad"}, "why": "{ال} and tanween together. Write {الْحِصَانُ}."}]},

        {"title": "Maʿrifa or nakira? Tap each word.",
         "prompt": "الْبَيْتُ قَرِيبٌ وَالدُّكَّانُ بَعِيدٌ.", "en": "The house is near and the shop is far.",
         "fields": [MN], "rows": [
            {"s": "الْبَيْتُ", "gloss": "the house", "ans": {"def": "m"}, "why": "It has {ال}."},
            {"s": "قَرِيبٌ", "gloss": "near", "ans": {"def": "n"}, "why": "Tanween, no {ال}."},
            {"s": "الدُّكَّانُ", "gloss": "the shop", "ans": {"def": "m"}, "why": "It has {ال}."},
            {"s": "بَعِيدٌ", "gloss": "far", "ans": {"def": "n"}, "why": "Tanween, no {ال}."}]},

        {"title": "Maʿrifa or nakira? Watch the tanween.",
         "prompt": "يَاسِرٌ طَالِبٌ وَزَيْنَبُ مُدَرِّسَةٌ.", "en": "Yasir is a student and Zaynab is a teacher.",
         "fields": [MN], "rows": [
            {"s": "يَاسِرٌ", "gloss": "Yasir", "ans": {"def": "m"}, "why": "A name. The tanween does not mean 'a'."},
            {"s": "طَالِبٌ", "gloss": "a student", "ans": {"def": "n"}, "why": "An ordinary noun with tanween: 'a student'."},
            {"s": "زَيْنَبُ", "gloss": "Zaynab", "ans": {"def": "m"}, "why": "A name, with no tanween."},
            {"s": "مُدَرِّسَةٌ", "gloss": "a teacher (f.)", "ans": {"def": "n"}, "why": "An ordinary noun with tanween: 'a teacher'."}]},
    ],
}
