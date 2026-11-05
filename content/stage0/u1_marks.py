# Stage 0 · Unit 1: Reading the marks (الْحَرَكَاتُ)

LAST = {"key": "mark", "label": "Last mark", "options": [
    {"k": "fatha", "label": "Fatha · ـَ", "color": "pink"},
    {"k": "damma", "label": "Damma · ـُ", "color": "red"},
    {"k": "kasra", "label": "Kasra · ـِ", "color": "green"},
    {"k": "sukun", "label": "Sukūn · ـْ", "color": "navy"}]}

LAST7 = {"key": "mark", "label": "Last mark", "options": [
    {"k": "fatha", "label": "Fatha · ـَ", "color": "pink"},
    {"k": "damma", "label": "Damma · ـُ", "color": "red"},
    {"k": "kasra", "label": "Kasra · ـِ", "color": "green"},
    {"k": "sukun", "label": "Sukūn · ـْ", "color": "navy"},
    {"k": "un", "label": "Tanween ـٌ (-un)", "color": "olive"},
    {"k": "an", "label": "Tanween ـً (-an)", "color": "olive"},
    {"k": "in", "label": "Tanween ـٍ (-in)", "color": "olive"}]}

TAN = {"key": "tan", "label": "Tanween", "options": [
    {"k": "un", "label": "ـٌ (-un)", "color": "olive"},
    {"k": "an", "label": "ـً (-an)", "color": "olive"},
    {"k": "in", "label": "ـٍ (-in)", "color": "olive"},
    {"k": "none", "label": "No tanween"}]}

INSIDE = {"key": "inside", "label": "Inside the word", "options": [
    {"k": "shadda", "label": "Shadda · ـّ", "color": "orange"},
    {"k": "sukun", "label": "Sukūn · ـْ", "color": "navy"},
    {"k": "both", "label": "Both"},
    {"k": "neither", "label": "Neither"}]}

UNIT = {
    "id": "s0-marks",
    "order": 1,
    "title": "Reading the marks",
    "ar": "الْحَرَكَاتُ",
    "blurb": "The short vowels, sukūn, shadda, tanween and the long vowels: the marks you read on every last letter.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 0 · UNIT 1", "title": "Read the last letter",
         "text": "Arabic grammar is read from small marks on the letters. This unit teaches every mark you need.",
         "wm": "الْحَرَكَاتُ"},

        {"t": "h2", "text": "Why the marks matter"},
        {"t": "p", "text": "Every word has a job in the sentence. The job gives it a colour, and the colour tells you its last vowel. "
                           "The grammar of the ending is called {إِعْرَابٌ}. You see it on the last letter of the word."},
        {"t": "examples", "items": [
            {"ar": "الْبَيْتُ جَدِيدٌ.", "en": "The house is new.", "note": "{الْبَيْتُ} ends in a damma."},
            {"ar": "الْكِتَابُ فِي الْبَيْتِ.", "en": "The book is in the house.", "note": "After {فِي} the same word ends in a kasra: {الْبَيْتِ}."}]},
        {"t": "rule", "color": "teal", "title": "Look at the last letter",
         "text": "The middle of a word stays the same. The last mark changes with the job. So first learn to read the marks."},

        {"t": "h2", "text": "The three short vowels"},
        {"t": "cols", "items": [
            {"color": "pink", "title": "Fatha", "ar": "ـَ", "text": "A small line above. Sound: a. {ذَهَبَ} dhahaba"},
            {"color": "red", "title": "Damma", "ar": "ـُ", "text": "A small و above. Sound: u. {الْقَلَمُ} al-qalamu"},
            {"color": "green", "title": "Kasra", "ar": "ـِ", "text": "A small line below. Sound: i. {الْمَسْجِدِ} al-masjidi"}]},
        {"t": "words", "items": [
            {"ar": "كَتَبَ", "label": "kataba", "sub": "fatha on every letter", "color": "pink"},
            {"ar": "الْبَابُ", "label": "al-bābu", "sub": "ends in damma", "color": "red"},
            {"ar": "الْمَكْتَبِ", "label": "al-maktabi", "sub": "ends in kasra", "color": "green"}]},

        {"t": "h2", "text": "Sukūn and shadda"},
        {"t": "cols", "items": [
            {"color": "navy", "title": "Sukūn", "ar": "ـْ", "text": "A small circle. The letter has no vowel. {كَلْبٌ} kalbun"},
            {"color": "orange", "title": "Shadda", "ar": "ـّ", "text": "A small w shape. Say the letter twice. {مُدَرِّسٌ} mudarrisun"}]},
        {"t": "words", "items": [
            {"ar": "مِنْ", "label": "min", "sub": "sukūn on the last letter", "color": "navy"},
            {"ar": "مَكْتَبٌ", "label": "maktabun", "sub": "sukūn on ك", "color": "navy"},
            {"ar": "سُكَّرٌ", "label": "sukkarun", "sub": "shadda on ك", "color": "orange"},
            {"ar": "كُرْسِيٌّ", "label": "kursiyyun", "sub": "shadda on the last letter", "color": "orange"}]},
        {"t": "tip", "text": "A shadda letter still has a vowel. It sits on top of the shadda or under it: {مُدَرِّسٌ} has a kasra under the shadda."},

        {"t": "h2", "text": "Tanween: the -n ending"},
        {"t": "p", "text": "Tanween is a doubled short vowel on the last letter. You read it as the vowel plus n. "
                           "It shows the noun is indefinite: {كِتَابٌ} means a book."},
        {"t": "table", "head": ["Mark", "Sound", "Example"], "rows": [
            ["ـٌ (damma tanween)", "-un", "{كِتَابٌ} kitābun"],
            ["ـً (fatha tanween)", "-an", "{كِتَابًا} kitāban"],
            ["ـٍ (kasra tanween)", "-in", "{كِتَابٍ} kitābin"]]},
        {"t": "tip", "text": "Fatha tanween comes with an extra alif: {كِتَابًا}. The alif is not read as a long ā. After {ة} there is no extra alif: {مَدْرَسَةً}."},
        {"t": "rule", "color": "olive", "title": "{ال} and tanween never meet",
         "text": "Add {ال} and the tanween goes. One single vowel is left: {كِتَابٌ} becomes {الْكِتَابُ}."},

        {"t": "h2", "text": "Long vowels: ا و ي"},
        {"t": "p", "text": "A long vowel is a full letter. It is held twice as long as a short vowel. The letter before it carries the matching short vowel."},
        {"t": "table", "head": ["Short", "Long", "Example"], "rows": [
            ["ـَ a", "ـَا ā", "{بَابٌ} bābun"],
            ["ـُ u", "ـُو ū", "{سُوقٌ} sūqun"],
            ["ـِ i", "ـِي ī", "{قَمِيصٌ} qamīṣun"]]},
        {"t": "examples", "items": [
            {"ar": "قَلَمٌ", "en": "qalamun: a pen", "note": "Only short vowels."},
            {"ar": "طَبِيبٌ", "en": "ṭabībun: a doctor", "note": "Long ī from {ي}."},
            {"ar": "مَفْتُوحٌ", "en": "maftūḥun: open", "note": "Long ū from {و}."}]},
        {"t": "tip", "text": "The alif of {ال} is not a long vowel. In {الْبَابُ} the long ā is the alif in the middle."},

        {"t": "h2", "text": "Reading a whole sentence"},
        {"t": "examples", "items": [
            {"ar": "ذَهَبَ الطَّالِبُ إِلَى الْمَسْجِدِ.", "en": "The student went to the mosque.",
             "note": "Last marks of {ذَهَبَ}، {الطَّالِبُ}، {الْمَسْجِدِ}: fatha, damma, kasra."},
            {"ar": "أَيْنَ الْكِتَابُ؟ هُوَ عَلَى الْمَكْتَبِ.", "en": "Where is the book? It is on the desk.",
             "note": "{الْكِتَابُ} ends in damma. {الْمَكْتَبِ} ends in kasra."},
            {"ar": "هَذَا قَلَمٌ.", "en": "This is a pen.", "note": "{قَلَمٌ} ends in damma tanween."}]},

        {"t": "summary", "title": "In three questions", "items": [
            "Which short vowel is on the last letter: fatha, damma or kasra? Or is it a sukūn?",
            "Is it doubled (tanween ـٌ ـً ـٍ)? Then the word has no {ال}.",
            "Is a vowel long? Look for {ا}, {و} or {ي} after the letter."]},
    ],

    "practice": [
        {"title": "Which mark is on the last letter?",
         "fields": [LAST],
         "rows": [
             {"s": "الْقَلَمُ", "gloss": "the pen", "ans": {"mark": "damma"}, "why": "The {م} has a damma: al-qalamu."},
             {"s": "كَتَبَ", "gloss": "he wrote", "ans": {"mark": "fatha"}, "why": "The last {ب} has a fatha: kataba."},
             {"s": "الْمَكْتَبِ", "gloss": "the desk (in عَلَى الْمَكْتَبِ)", "ans": {"mark": "kasra"}, "why": "The {ب} has a kasra below: al-maktabi."},
             {"s": "مِنْ", "gloss": "from", "ans": {"mark": "sukun"}, "why": "The {ن} has a small circle: min."},
             {"s": "الْوَلَدُ", "gloss": "the boy", "ans": {"mark": "damma"}, "why": "The {د} has a damma: al-waladu."},
             {"s": "هُوَ", "gloss": "he", "ans": {"mark": "fatha"}, "why": "The {و} has a fatha: huwa."}]},

        {"title": "Which tanween, or none?",
         "fields": [TAN],
         "rows": [
             {"s": "كِتَابٌ", "gloss": "a book", "ans": {"tan": "un"}, "why": "Two dammas: kitābun."},
             {"s": "الْكِتَابُ", "gloss": "the book", "ans": {"tan": "none"}, "why": "It has {ال}, so one damma only."},
             {"s": "حِصَانٍ", "gloss": "a horse", "ans": {"tan": "in"}, "why": "Two kasras below: ḥiṣānin."},
             {"s": "قَلَمًا", "gloss": "a pen", "ans": {"tan": "an"}, "why": "Two fathas with the extra alif: qalaman."},
             {"s": "الْمَسْجِدِ", "gloss": "the mosque", "ans": {"tan": "none"}, "why": "One kasra and {ال}: al-masjidi."},
             {"s": "رَجُلٌ", "gloss": "a man", "ans": {"tan": "un"}, "why": "Two dammas: rajulun."}]},

        {"title": "Which long vowel letter is in the word?",
         "fields": [{"key": "long", "label": "Long vowel", "options": [
             {"k": "alif", "label": "ا (ā)"}, {"k": "waw", "label": "و (ū)"},
             {"k": "ya", "label": "ي (ī)"}, {"k": "none", "label": "None"}]}],
         "rows": [
             {"s": "بَابٌ", "gloss": "a door", "ans": {"long": "alif"}, "why": "{بَا} is bā, a long ā."},
             {"s": "قَمِيصٌ", "gloss": "a shirt", "ans": {"long": "ya"}, "why": "{مِي} is mī, a long ī."},
             {"s": "سُوقٌ", "gloss": "a market", "ans": {"long": "waw"}, "why": "{سُو} is sū, a long ū."},
             {"s": "قَلَمٌ", "gloss": "a pen", "ans": {"long": "none"}, "why": "qa-la-mun: three short vowels."},
             {"s": "رَسُولٌ", "gloss": "a messenger", "ans": {"long": "waw"}, "why": "{سُو} is sū: rasūlun."},
             {"s": "كَلْبٌ", "gloss": "a dog", "ans": {"long": "none"}, "why": "kal-bun: a sukūn, no long vowel."}]},

        {"title": "Which spelling matches the sound?",
         "fields": [{"key": "pick", "label": "Spelling", "options": []}],
         "rows": [
             {"s": "kitābun", "gloss": "a book", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "كَتَبَ"}, {"k": "b", "label": "كِتَابٌ"}, {"k": "c", "label": "كِتَابُ"}]},
              "why": "ki, long tā, then bun with tanween: {كِتَابٌ}."},
             {"s": "al-qalamu", "gloss": "the pen", "ans": {"pick": "a"},
              "opts": {"pick": [{"k": "a", "label": "الْقَلَمُ"}, {"k": "b", "label": "الْقَلَمٌ"}, {"k": "c", "label": "قَلَمٌ"}]},
              "why": "{ال} with one damma at the end: {الْقَلَمُ}."},
             {"s": "baitin", "gloss": "a house", "ans": {"pick": "c"},
              "opts": {"pick": [{"k": "a", "label": "بَيْتٌ"}, {"k": "b", "label": "بَيْتِ"}, {"k": "c", "label": "بَيْتٍ"}]},
              "why": "-in is kasra tanween: {بَيْتٍ}."},
             {"s": "ṭabībun", "gloss": "a doctor", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "طَبِبٌ"}, {"k": "b", "label": "طَبِيبٌ"}, {"k": "c", "label": "طَبِيبُ"}]},
              "why": "The long ī needs {ي}, and -un needs tanween: {طَبِيبٌ}."},
             {"s": "waladun", "gloss": "a boy", "ans": {"pick": "a"},
              "opts": {"pick": [{"k": "a", "label": "وَلَدٌ"}, {"k": "b", "label": "وَلْدٌ"}, {"k": "c", "label": "وَالِدٌ"}]},
              "why": "wa-la-dun: short vowels only, no sukūn: {وَلَدٌ}."}]},

        {"title": "Shadda or sukūn inside the word? (ignore the last letter)",
         "fields": [INSIDE],
         "rows": [
             {"s": "مُدَرِّسٌ", "gloss": "a teacher", "ans": {"inside": "shadda"}, "why": "{رّ} is said twice: mudarrisun."},
             {"s": "كَلْبٌ", "gloss": "a dog", "ans": {"inside": "sukun"}, "why": "{لْ} has no vowel: kalbun."},
             {"s": "رَجُلٌ", "gloss": "a man", "ans": {"inside": "neither"}, "why": "ra-ju-lun: a vowel on every letter."},
             {"s": "مَكْتَبٌ", "gloss": "a desk", "ans": {"inside": "sukun"}, "why": "{كْ} has no vowel: maktabun."},
             {"s": "جَنَّةٌ", "gloss": "a garden", "ans": {"inside": "shadda"}, "why": "{نّ} is said twice: jannatun."},
             {"s": "دِيكٌ", "gloss": "a rooster", "ans": {"inside": "neither"}, "why": "dī-kun: a long ī, no sukūn or shadda."}]},

        {"title": "Last vowel and tanween",
         "fields": [
             {"key": "mark", "label": "Vowel", "options": [
                 {"k": "fatha", "label": "Fatha", "color": "pink"},
                 {"k": "damma", "label": "Damma", "color": "red"},
                 {"k": "kasra", "label": "Kasra", "color": "green"}]},
             {"key": "tan", "label": "Tanween?", "options": [
                 {"k": "yes", "label": "Yes", "color": "olive"}, {"k": "no", "label": "No"}]}],
         "rows": [
             {"s": "بَيْتٌ", "ans": {"mark": "damma", "tan": "yes"}, "why": "Two dammas: baitun."},
             {"s": "الْبَيْتُ", "ans": {"mark": "damma", "tan": "no"}, "why": "One damma with {ال}: al-baitu."},
             {"s": "بَيْتٍ", "ans": {"mark": "kasra", "tan": "yes"}, "why": "Two kasras: baitin."},
             {"s": "الْبَيْتِ", "ans": {"mark": "kasra", "tan": "no"}, "why": "One kasra with {ال}: al-baiti."},
             {"s": "بَيْتًا", "ans": {"mark": "fatha", "tan": "yes"}, "why": "Two fathas and the extra alif: baitan."}]},
    ],

    "homework": [
        {"title": "Name the last mark exactly",
         "fields": [LAST7],
         "rows": [
             {"s": "لَبَنٌ", "gloss": "milk", "ans": {"mark": "un"}, "why": "Two dammas: labanun."},
             {"s": "نَعَمْ", "gloss": "yes", "ans": {"mark": "sukun"}, "why": "The {م} has a sukūn: naʿam."},
             {"s": "جَلَسَ", "gloss": "he sat", "ans": {"mark": "fatha"}, "why": "The {س} has one fatha: jalasa."},
             {"s": "مَسْجِدًا", "gloss": "a mosque", "ans": {"mark": "an"}, "why": "Two fathas with the extra alif: masjidan."},
             {"s": "حَجَرٍ", "gloss": "a stone", "ans": {"mark": "in"}, "why": "Two kasras: ḥajarin."},
             {"s": "الْمُدِيرِ", "gloss": "the principal (in إِلَى الْمُدِيرِ)", "ans": {"mark": "kasra"}, "why": "{ال} and one kasra: al-mudīri."}]},

        {"title": "Shadda, sukūn, both or neither? (ignore the last letter)",
         "fields": [INSIDE],
         "rows": [
             {"s": "تُفَّاحٌ", "gloss": "apple", "ans": {"inside": "shadda"}, "why": "{فّ} is said twice: tuffāḥun."},
             {"s": "مَطْبَخٌ", "gloss": "a kitchen", "ans": {"inside": "sukun"}, "why": "{طْ} has no vowel: maṭbakhun."},
             {"s": "جَمَلٌ", "gloss": "a camel", "ans": {"inside": "neither"}, "why": "ja-ma-lun: a vowel on every letter."},
             {"s": "الْحَمَّامُ", "gloss": "the bathroom", "ans": {"inside": "both"}, "why": "Sukūn on the {ل} of {ال}, shadda on {م}: al-ḥammāmu."},
             {"s": "مُهَنْدِسٌ", "gloss": "an engineer", "ans": {"inside": "sukun"}, "why": "{نْ} has no vowel: muhandisun."},
             {"s": "دُكَّانٌ", "gloss": "a shop", "ans": {"inside": "shadda"}, "why": "{كّ} is said twice: dukkānun."}]},

        {"title": "Find the word",
         "fields": [{"key": "pick", "label": "Word", "options": []}],
         "rows": [
             {"s": "Which word has a long ā?", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "كَتَبَ"}, {"k": "b", "label": "كِتَابٌ"}, {"k": "c", "label": "كَلْبٌ"}]},
              "why": "{كِتَابٌ} has {ا} after {ت}: kitābun. {كَتَبَ} has three short fathas."},
             {"s": "Which word has a long ī?", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "جَمَلٌ"}, {"k": "b", "label": "جَمِيلٌ"}, {"k": "c", "label": "جَلَسَ"}]},
              "why": "{جَمِيلٌ} has {ي} after {م}: jamīlun."},
             {"s": "Which word has a long ū?", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "مَكْتَبٌ"}, {"k": "b", "label": "مَكْسُورٌ"}, {"k": "c", "label": "مَسْجِدٌ"}]},
              "why": "{مَكْسُورٌ} has {و} after {س}: maksūrun."},
             {"s": "Which word has no long vowel?", "ans": {"pick": "a"},
              "opts": {"pick": [{"k": "a", "label": "حَجَرٌ"}, {"k": "b", "label": "حِمَارٌ"}, {"k": "c", "label": "حِصَانٌ"}]},
              "why": "ḥa-ja-run: all short. The other two have a long ā."},
             {"s": "Which word has two long vowels?", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "مِفْتَاحٌ"}, {"k": "b", "label": "صَابُونٌ"}, {"k": "c", "label": "مِنْدِيلٌ"}]},
              "why": "{صَابُونٌ} has ā and ū: ṣābūnun. The others have one each."}]},

        {"title": "Which tanween? Is there an extra alif?",
         "fields": [TAN, {"key": "alif", "label": "Extra alif?", "options": [
             {"k": "yes", "label": "Yes"}, {"k": "no", "label": "No"}]}],
         "rows": [
             {"s": "غُرْفَةٌ", "gloss": "a room", "ans": {"tan": "un", "alif": "no"}, "why": "Two dammas on {ة}: ghurfatun."},
             {"s": "سَاعَةٍ", "gloss": "a watch", "ans": {"tan": "in", "alif": "no"}, "why": "Two kasras on {ة}: sāʿatin."},
             {"s": "سَيَّارَةً", "gloss": "a car", "ans": {"tan": "an", "alif": "no"}, "why": "Fatha tanween on {ة} takes no extra alif: sayyāratan."},
             {"s": "قَمِيصًا", "gloss": "a shirt", "ans": {"tan": "an", "alif": "yes"}, "why": "Fatha tanween on a normal letter adds {ا}: qamīṣan."},
             {"s": "الْحَقِيبَةُ", "gloss": "the bag", "ans": {"tan": "none", "alif": "no"}, "why": "{ال} means no tanween: al-ḥaqībatu."},
             {"s": "دَفْتَرٍ", "gloss": "a notebook", "ans": {"tan": "in", "alif": "no"}, "why": "Two kasras: daftarin."}]},

        {"title": "Which spelling is right?",
         "fields": [{"key": "pick", "label": "Spelling", "options": []}],
         "rows": [
             {"s": "al-bābu", "gloss": "the door", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "الْبَابٌ"}, {"k": "b", "label": "الْبَابُ"}, {"k": "c", "label": "بَابُ"}]},
              "why": "{ال} and tanween never meet: {الْبَابُ}."},
             {"s": "kitāban", "gloss": "a book", "ans": {"pick": "a"},
              "opts": {"pick": [{"k": "a", "label": "كِتَابًا"}, {"k": "b", "label": "كِتَابً"}, {"k": "c", "label": "كِتَابَا"}]},
              "why": "Fatha tanween plus the extra alif: {كِتَابًا}."},
             {"s": "madrasatan", "gloss": "a school", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "مَدْرَسَةًا"}, {"k": "b", "label": "مَدْرَسَةً"}, {"k": "c", "label": "مَدْرَسَتًا"}]},
              "why": "On {ة} there is no extra alif: {مَدْرَسَةً}."},
             {"s": "kursiyyun", "gloss": "a chair", "ans": {"pick": "a"},
              "opts": {"pick": [{"k": "a", "label": "كُرْسِيٌّ"}, {"k": "b", "label": "كُرْسِيٌ"}, {"k": "c", "label": "كُرْسِيُّ"}]},
              "why": "yy needs a shadda, and -un needs tanween: {كُرْسِيٌّ}."},
             {"s": "sukkarun", "gloss": "sugar", "ans": {"pick": "b"},
              "opts": {"pick": [{"k": "a", "label": "سُكَرٌ"}, {"k": "b", "label": "سُكَّرٌ"}, {"k": "c", "label": "سُكَّرُ"}]},
              "why": "kk needs a shadda, and -un needs tanween: {سُكَّرٌ}."},
             {"s": "qiṭṭun", "gloss": "a cat", "ans": {"pick": "c"},
              "opts": {"pick": [{"k": "a", "label": "قِطٌ"}, {"k": "b", "label": "قِطُّ"}, {"k": "c", "label": "قِطٌّ"}]},
              "why": "Shadda for ṭṭ and two dammas for -un: {قِطٌّ}."}]},

        {"title": "Name the last mark of each word",
         "prompt": "خَرَجَ طَالِبٌ مِنَ الْبَيْتِ وَذَهَبَ إِلَى مَسْجِدٍ.",
         "en": "A student went out of the house and went to a mosque.",
         "fields": [LAST7],
         "rows": [
             {"s": "خَرَجَ", "gloss": "went out", "ans": {"mark": "fatha"}, "why": "One fatha on {ج}: kharaja."},
             {"s": "طَالِبٌ", "gloss": "a student", "ans": {"mark": "un"}, "why": "Two dammas: ṭālibun."},
             {"s": "مِنَ", "gloss": "from", "ans": {"mark": "fatha"}, "why": "Before {ال}, {مِنْ} is read {مِنَ}: mina l-baiti."},
             {"s": "الْبَيْتِ", "gloss": "the house", "ans": {"mark": "kasra"}, "why": "One kasra with {ال}: al-baiti."},
             {"s": "مَسْجِدٍ", "gloss": "a mosque", "ans": {"mark": "in"}, "why": "Two kasras: masjidin."}]},
    ],
}
