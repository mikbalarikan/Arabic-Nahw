# Stage 0 · Unit 3: Masculine and feminine (الْمُذَكَّرُ وَالْمُؤَنَّثُ)

GENDER = {"key": "gender", "label": "Gender", "options": [
    {"k": "m", "label": "Masculine · مُذَكَّرٌ", "color": "blue"},
    {"k": "f", "label": "Feminine · مُؤَنَّثٌ", "color": "pink"}]}

PRON = {"key": "pron", "label": "Answer with", "options": [
    {"k": "huwa", "label": "هُوَ", "color": "blue"},
    {"k": "hiya", "label": "هِيَ", "color": "pink"}]}

TAN = {"key": "tan", "label": "Tanween?", "options": [
    {"k": "yes", "label": "Yes", "color": "olive"},
    {"k": "no", "label": "No"}]}

PICK = {"key": "pick", "label": "Spelling", "options": []}

UNIT = {
    "id": "s0-gender",
    "order": 3,
    "title": "Masculine and feminine",
    "ar": "الْمُذَكَّرُ وَالْمُؤَنَّثُ",
    "blurb": "Every noun is masculine or feminine. Learn the sign ة, the feminine names, and when to say هُوَ or هِيَ.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 0 · UNIT 3", "title": "Every noun has a gender",
         "text": "In Arabic every noun is masculine or feminine, even a pen or a watch. The gender decides the words around it.",
         "wm": "مُذَكَّرٌ مُؤَنَّثٌ"},

        {"t": "h2", "text": "Two genders"},
        {"t": "cols", "items": [
            {"color": "blue", "title": "Masculine", "ar": "مُذَكَّرٌ", "text": "{الْكِتَابُ}، {الْوَلَدُ}، {الْبَيْتُ}"},
            {"color": "pink", "title": "Feminine", "ar": "مُؤَنَّثٌ", "text": "{السَّاعَةُ}، {الْمَدْرَسَةُ}، {آمِنَةُ}"}]},
        {"t": "p", "text": "Things have a gender too. {الْقَلَمُ} the pen is masculine. {الْغُرْفَةُ} the room is feminine."},

        {"t": "h2", "text": "The main sign: ة"},
        {"t": "p", "text": "Most feminine nouns end in {ة}, called tāʾ marbūṭa. With a vowel it is read as t: madrasatun."},
        {"t": "words", "items": [
            {"ar": "مَدْرَسَةٌ", "label": "madrasatun", "sub": "a school", "color": "pink"},
            {"ar": "غُرْفَةٌ", "label": "ghurfatun", "sub": "a room", "color": "pink"},
            {"ar": "سَاعَةٌ", "label": "sāʿatun", "sub": "a watch", "color": "pink"},
            {"ar": "سَيَّارَةٌ", "label": "sayyāratun", "sub": "a car", "color": "pink"},
            {"ar": "حَقِيبَةٌ", "label": "ḥaqībatun", "sub": "a bag", "color": "pink"},
            {"ar": "جَامِعَةٌ", "label": "jāmiʿatun", "sub": "a university", "color": "pink"}]},
        {"t": "rule", "color": "pink", "title": "No ة? Usually masculine",
         "text": "A noun without {ة} is usually masculine: {بَيْتٌ}، {قَلَمٌ}، {مَسْجِدٌ}، {كِتَابٌ}."},

        {"t": "h2", "text": "Feminine names: no tanween"},
        {"t": "p", "text": "Most masculine names take tanween. Feminine names never take tanween: {آمِنَةُ} has one damma only. Some feminine names have no {ة}: {زَيْنَبُ}، {مَرْيَمُ}."},
        {"t": "table", "head": ["Masculine name", "Feminine name"], "rows": [
            ["{مُحَمَّدٌ}", "{فَاطِمَةُ}"],
            ["{خَالِدٌ}", "{آمِنَةُ}"],
            ["{حَامِدٌ}", "{زَيْنَبُ}"],
            ["{يَاسِرٌ}", "{مَرْيَمُ}"]]},
        {"t": "tip", "text": "Never write {فَاطِمَةٌ} or {زَيْنَبٌ}. A feminine name ends in one damma: {أَيْنَ زَيْنَبُ؟}"},

        {"t": "h2", "text": "Feminine without ة"},
        {"t": "p", "text": "A few feminine nouns have no {ة}. Learn them by heart."},
        {"t": "words", "items": [
            {"ar": "الشَّمْسُ", "sub": "the sun", "color": "pink"},
            {"ar": "الْعَيْنُ", "sub": "the eye", "color": "pink"},
            {"ar": "الْيَدُ", "sub": "the hand", "color": "pink"},
            {"ar": "الْبِنْتُ", "sub": "the girl", "color": "pink"}]},
        {"t": "tip", "text": "{الْقَمَرُ} the moon is masculine. {الشَّمْسُ} the sun is feminine."},

        {"t": "h2", "text": "هُوَ or هِيَ"},
        {"t": "p", "text": "For a masculine noun say {هُوَ}. For a feminine noun say {هِيَ}. For things, both mean it."},
        {"t": "examples", "items": [
            {"ar": "أَيْنَ الْكِتَابُ؟ هُوَ عَلَى الْمَكْتَبِ.", "en": "Where is the book? It is on the desk.", "note": "{الْكِتَابُ} is masculine."},
            {"ar": "أَيْنَ السَّاعَةُ؟ هِيَ عَلَى السَّرِيرِ.", "en": "Where is the watch? It is on the bed.", "note": "{السَّاعَةُ} ends in {ة}."},
            {"ar": "أَيْنَ آمِنَةُ؟ هِيَ فِي الْبَيْتِ.", "en": "Where is Āminah? She is in the house.", "note": "A girl's name."},
            {"ar": "أَيْنَ الْوَلَدُ؟ هُوَ فِي الْمَسْجِدِ.", "en": "Where is the boy? He is in the mosque.", "note": "A boy."}]},
        {"t": "rule", "color": "teal", "title": "Find the noun first",
         "text": "Look at the noun in the question. Decide its gender. Then choose {هُوَ} or {هِيَ}."},

        {"t": "h2", "text": "A look ahead"},
        {"t": "examples", "items": [
            {"ar": "مَدْرَسَةٌ كَبِيرَةٌ", "en": "a big school",
             "note": "The describing word also takes {ة} after a feminine noun. You will learn this in Unit 6."}]},

        {"t": "summary", "title": "In three questions", "items": [
            "Does the noun end in {ة}? Then it is almost always feminine.",
            "Is it a girl's name, or one of {الشَّمْسُ}، {الْعَيْنُ}، {الْيَدُ}، {الْبِنْتُ}? Then it is feminine too.",
            "Masculine or feminine? Use {هُوَ} for masculine and {هِيَ} for feminine."]},
    ],

    "practice": [
        {"title": "Masculine or feminine?",
         "fields": [GENDER],
         "rows": [
             {"s": "الْبَيْتُ", "gloss": "the house", "ans": {"gender": "m"}, "why": "No {ة}: masculine."},
             {"s": "الْمَدْرَسَةُ", "gloss": "the school", "ans": {"gender": "f"}, "why": "It ends in {ة}."},
             {"s": "الْقَلَمُ", "gloss": "the pen", "ans": {"gender": "m"}, "why": "No {ة}: masculine."},
             {"s": "السَّاعَةُ", "gloss": "the watch", "ans": {"gender": "f"}, "why": "It ends in {ة}."},
             {"s": "الْفَصْلُ", "gloss": "the classroom", "ans": {"gender": "m"}, "why": "No {ة}: masculine."},
             {"s": "الْحَقِيبَةُ", "gloss": "the bag", "ans": {"gender": "f"}, "why": "It ends in {ة}."}]},

        {"title": "Names: gender and tanween",
         "fields": [GENDER, TAN],
         "rows": [
             {"s": "مُحَمَّدٌ", "gloss": "Muḥammad", "ans": {"gender": "m", "tan": "yes"}, "why": "A man's name with tanween: muḥammadun."},
             {"s": "آمِنَةُ", "gloss": "Āminah", "ans": {"gender": "f", "tan": "no"}, "why": "A woman's name. One damma only."},
             {"s": "خَالِدٌ", "gloss": "Khālid", "ans": {"gender": "m", "tan": "yes"}, "why": "A man's name with tanween."},
             {"s": "زَيْنَبُ", "gloss": "Zaynab", "ans": {"gender": "f", "tan": "no"}, "why": "A woman's name without {ة}. Still no tanween."},
             {"s": "يَاسِرٌ", "gloss": "Yāsir", "ans": {"gender": "m", "tan": "yes"}, "why": "A man's name with tanween."},
             {"s": "فَاطِمَةُ", "gloss": "Fāṭimah", "ans": {"gender": "f", "tan": "no"}, "why": "A woman's name with {ة}. One damma only."}]},

        {"title": "Answer with هُوَ or هِيَ",
         "fields": [PRON],
         "rows": [
             {"s": "أَيْنَ الْوَلَدُ؟", "gloss": "Where is the boy?", "ans": {"pron": "huwa"}, "why": "{الْوَلَدُ} is masculine: {هُوَ فِي الْمَسْجِدِ}."},
             {"s": "أَيْنَ آمِنَةُ؟", "gloss": "Where is Āminah?", "ans": {"pron": "hiya"}, "why": "A girl's name: {هِيَ فِي الْبَيْتِ}."},
             {"s": "أَيْنَ السَّاعَةُ؟", "gloss": "Where is the watch?", "ans": {"pron": "hiya"}, "why": "{السَّاعَةُ} ends in {ة}: {هِيَ عَلَى السَّرِيرِ}."},
             {"s": "أَيْنَ الْمُدَرِّسُ؟", "gloss": "Where is the teacher?", "ans": {"pron": "huwa"}, "why": "{الْمُدَرِّسُ} is masculine: {هُوَ فِي الْفَصْلِ}."},
             {"s": "أَيْنَ السَّيَّارَةُ؟", "gloss": "Where is the car?", "ans": {"pron": "hiya"}, "why": "{السَّيَّارَةُ} ends in {ة}."},
             {"s": "أَيْنَ الْكُرْسِيُّ؟", "gloss": "Where is the chair?", "ans": {"pron": "huwa"}, "why": "{الْكُرْسِيُّ} has no {ة}: masculine."}]},

        {"title": "Which spelling is right?",
         "fields": [PICK],
         "rows": [
             {"s": "Āminah", "ans": {"pick": "a"},
              "opts": {"pick": [{"k": "a", "label": "آمِنَةُ"}, {"k": "b", "label": "آمِنَةٌ"}]},
              "why": "A feminine name takes no tanween: {آمِنَةُ}."},
             {"s": "a school", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "مَدْرَسَةُ"}, {"k": "b", "label": "مَدْرَسَةٌ"}]},
              "why": "A common noun with {ة} keeps its tanween: {مَدْرَسَةٌ}. Feminine names drop it."},
             {"s": "Muḥammad", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "مُحَمَّدُ"}, {"k": "b", "label": "مُحَمَّدٌ"}]},
              "why": "A masculine name takes tanween: {مُحَمَّدٌ}."},
             {"s": "Zaynab", "ans": {"pick": "a"},
              "opts": {"pick": [{"k": "a", "label": "زَيْنَبُ"}, {"k": "b", "label": "زَيْنَبٌ"}]},
              "why": "A feminine name, even without {ة}: {زَيْنَبُ}."},
             {"s": "the room", "ans": {"pick": "c"},
              "opts": {"pick": [{"k": "a", "label": "الْغُرْفَةٌ"}, {"k": "b", "label": "غُرْفَةُ"}, {"k": "c", "label": "الْغُرْفَةُ"}]},
              "why": "{ال} with one damma: {الْغُرْفَةُ}."}]},

        {"title": "Masculine or feminine? (every noun in the sentence)",
         "prompt": "الْوَلَدُ فِي الْمَطْبَخِ وَآمِنَةُ فِي الْغُرْفَةِ.",
         "en": "The boy is in the kitchen and Āminah is in the room.",
         "fields": [GENDER],
         "rows": [
             {"s": "الْوَلَدُ", "gloss": "the boy", "ans": {"gender": "m"}, "why": "A boy, no {ة}."},
             {"s": "الْمَطْبَخِ", "gloss": "the kitchen", "ans": {"gender": "m"}, "why": "No {ة}: masculine."},
             {"s": "آمِنَةُ", "gloss": "Āminah", "ans": {"gender": "f"}, "why": "A girl's name with {ة}."},
             {"s": "الْغُرْفَةِ", "gloss": "the room", "ans": {"gender": "f"}, "why": "It ends in {ة}."}]},

        {"title": "Careful: feminine without ة",
         "fields": [GENDER],
         "rows": [
             {"s": "الشَّمْسُ", "gloss": "the sun", "ans": {"gender": "f"}, "why": "Feminine with no {ة}. Learn it by heart."},
             {"s": "الْقَمَرُ", "gloss": "the moon", "ans": {"gender": "m"}, "why": "No {ة} and masculine."},
             {"s": "الْيَدُ", "gloss": "the hand", "ans": {"gender": "f"}, "why": "Feminine with no {ة}."},
             {"s": "الْبَابُ", "gloss": "the door", "ans": {"gender": "m"}, "why": "No {ة} and masculine."},
             {"s": "الْبِنْتُ", "gloss": "the girl", "ans": {"gender": "f"}, "why": "A girl is feminine. The {ت} here is a normal letter."},
             {"s": "الْوَلَدُ", "gloss": "the boy", "ans": {"gender": "m"}, "why": "A boy is masculine."}]},
    ],

    "homework": [
        {"title": "Masculine or feminine?",
         "fields": [GENDER],
         "rows": [
             {"s": "الصَّلَاةُ", "gloss": "the prayer", "ans": {"gender": "f"}, "why": "It ends in {ة}."},
             {"s": "الْعَيْنُ", "gloss": "the eye", "ans": {"gender": "f"}, "why": "Feminine with no {ة}."},
             {"s": "الْمِفْتَاحُ", "gloss": "the key", "ans": {"gender": "m"}, "why": "No {ة}: masculine."},
             {"s": "الْكَعْبَةُ", "gloss": "the Kaʿbah", "ans": {"gender": "f"}, "why": "It ends in {ة}."},
             {"s": "الدَّفْتَرُ", "gloss": "the notebook", "ans": {"gender": "m"}, "why": "No {ة}: masculine."},
             {"s": "الزَّهْرَةُ", "gloss": "the flower", "ans": {"gender": "f"}, "why": "It ends in {ة}."}]},

        {"title": "Answer with هُوَ or هِيَ",
         "fields": [PRON],
         "rows": [
             {"s": "أَيْنَ رُقَيَّةُ؟", "gloss": "Where is Ruqayyah?", "ans": {"pron": "hiya"}, "why": "A girl's name: {هِيَ}."},
             {"s": "أَيْنَ التَّاجِرُ؟", "gloss": "Where is the merchant?", "ans": {"pron": "huwa"}, "why": "{التَّاجِرُ} is masculine: {هُوَ فِي الدُّكَّانِ}."},
             {"s": "أَيْنَ الْقَمِيصُ؟", "gloss": "Where is the shirt?", "ans": {"pron": "huwa"}, "why": "{الْقَمِيصُ} has no {ة}: masculine."},
             {"s": "أَيْنَ سَيَّارَةُ الْمُدَرِّسِ؟", "gloss": "Where is the teacher's car?", "ans": {"pron": "hiya"}, "why": "The question is about the car, {سَيَّارَةُ}. It is feminine."},
             {"s": "أَيْنَ عَبَّاسٌ؟", "gloss": "Where is ʿAbbās?", "ans": {"pron": "huwa"}, "why": "A man's name with tanween."},
             {"s": "أَيْنَ بِنْتُ خَالِدٍ؟", "gloss": "Where is Khālid's daughter?", "ans": {"pron": "hiya"}, "why": "The question is about {بِنْتُ}, the daughter. She is feminine."}]},

        {"title": "Names: gender and tanween",
         "fields": [GENDER, TAN],
         "rows": [
             {"s": "عَمَّارٌ", "gloss": "ʿAmmār", "ans": {"gender": "m", "tan": "yes"}, "why": "A man's name with tanween."},
             {"s": "مَرْيَمُ", "gloss": "Maryam", "ans": {"gender": "f", "tan": "no"}, "why": "A woman's name without {ة}. No tanween."},
             {"s": "سَعِيدٌ", "gloss": "Saʿīd", "ans": {"gender": "m", "tan": "yes"}, "why": "A man's name with tanween."},
             {"s": "خَدِيجَةُ", "gloss": "Khadījah", "ans": {"gender": "f", "tan": "no"}, "why": "A woman's name with {ة}. One damma only."},
             {"s": "عَلِيٌّ", "gloss": "ʿAlī", "ans": {"gender": "m", "tan": "yes"}, "why": "A man's name with tanween: ʿaliyyun."},
             {"s": "عَائِشَةُ", "gloss": "ʿĀʾishah", "ans": {"gender": "f", "tan": "no"}, "why": "A woman's name with {ة}. One damma only."}]},

        {"title": "Masculine or feminine? (every noun in the sentence)",
         "prompt": "بِنْتُ حَامِدٍ فِي الْجَامِعَةِ وَابْنُ مُحَمَّدٍ فِي الْمَسْجِدِ.",
         "en": "Ḥāmid's daughter is at the university and Muḥammad's son is in the mosque.",
         "fields": [GENDER],
         "rows": [
             {"s": "بِنْتُ", "gloss": "daughter", "ans": {"gender": "f"}, "why": "Feminine with no {ة}."},
             {"s": "حَامِدٍ", "gloss": "Ḥāmid", "ans": {"gender": "m"}, "why": "A man's name."},
             {"s": "الْجَامِعَةِ", "gloss": "the university", "ans": {"gender": "f"}, "why": "It ends in {ة}."},
             {"s": "اِبْنُ", "gloss": "son", "ans": {"gender": "m"}, "why": "A son is masculine."},
             {"s": "الْمَسْجِدِ", "gloss": "the mosque", "ans": {"gender": "m"}, "why": "No {ة}: masculine."}]},

        {"title": "Which spelling is right?",
         "fields": [PICK],
         "rows": [
             {"s": "Ṣafiyyah is in the house.", "ans": {"pick": "a"},
              "opts": {"pick": [{"k": "a", "label": "صَفِيَّةُ فِي الْبَيْتِ."}, {"k": "b", "label": "صَفِيَّةٌ فِي الْبَيْتِ."}]},
              "why": "A feminine name takes no tanween: {صَفِيَّةُ}."},
             {"s": "a university", "ans": {"pick": "a"},
              "opts": {"pick": [{"k": "a", "label": "جَامِعَةٌ"}, {"k": "b", "label": "جَامِعَةُ"}, {"k": "c", "label": "جَامِعَتٌ"}]},
              "why": "An indefinite noun takes tanween, and the ending is written {ة}: {جَامِعَةٌ}."},
             {"s": "Bilāl is in the mosque.", "ans": {"pick": "a"},
              "opts": {"pick": [{"k": "a", "label": "بِلَالٌ فِي الْمَسْجِدِ."}, {"k": "b", "label": "بِلَالُ فِي الْمَسْجِدِ."}]},
              "why": "A masculine name takes tanween: {بِلَالٌ}."},
             {"s": "Where is Khadījah?", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "أَيْنَ خَدِيجَةٌ؟"}, {"k": "b", "label": "أَيْنَ خَدِيجَةُ؟"}, {"k": "c", "label": "أَيْنَ خَدِيجَهُ؟"}]},
              "why": "Write {ة} with one damma: {خَدِيجَةُ}. {ه} is a different letter."}]},

        {"title": "Is the pronoun right?",
         "fields": [{"key": "ok", "label": "Pronoun", "options": [
             {"k": "right", "label": "Right", "color": "green"},
             {"k": "wrong", "label": "Wrong", "color": "red"}]}],
         "rows": [
             {"s": "أَيْنَ الطَّبِيبُ؟ هُوَ فِي الْمَسْجِدِ.", "gloss": "Where is the doctor? He is in the mosque.", "ans": {"ok": "right"}, "why": "{الطَّبِيبُ} is masculine, so {هُوَ}."},
             {"s": "أَيْنَ الْمِنْدِيلُ؟ هِيَ عَلَى السَّرِيرِ.", "gloss": "Where is the kerchief? It is on the bed.", "ans": {"ok": "wrong"}, "why": "{الْمِنْدِيلُ} has no {ة}. It is masculine: {هُوَ}."},
             {"s": "أَيْنَ الصَّابُونُ؟ هِيَ فِي الْحَمَّامِ.", "gloss": "Where is the soap? It is in the bathroom.", "ans": {"ok": "wrong"}, "why": "{الصَّابُونُ} is masculine: {هُوَ}."},
             {"s": "أَيْنَ عَائِشَةُ؟ هِيَ فِي الْغُرْفَةِ.", "gloss": "Where is ʿĀʾishah? She is in the room.", "ans": {"ok": "right"}, "why": "A girl's name, so {هِيَ}."},
             {"s": "أَيْنَ الْكَعْبَةُ؟ هُوَ فِي الْمَسْجِدِ.", "gloss": "Where is the Kaʿbah? It is in the mosque.", "ans": {"ok": "wrong"}, "why": "{الْكَعْبَةُ} ends in {ة}. It is feminine: {هِيَ}."},
             {"s": "أَيْنَ الْمُهَنْدِسُ؟ هُوَ فِي الشَّارِعِ.", "gloss": "Where is the engineer? He is in the street.", "ans": {"ok": "right"}, "why": "{الْمُهَنْدِسُ} is masculine, so {هُوَ}."}]},
    ],
}
