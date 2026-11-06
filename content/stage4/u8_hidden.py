# Stage 4, Unit 8: When the vowel is hidden (الْإِعْرَابُ الْمُقَدَّرُ)

MAQ = {"k": "maq", "label": "Maqṣūr · مَقْصُورٌ", "color": "brown"}
MANQ = {"k": "manq", "label": "Manqūṣ · مَنْقُوصٌ", "color": "brown"}
MAMD = {"k": "mamd", "label": "Mamdūd · مَمْدُودٌ", "color": "olive"}
NORM = {"k": "norm", "label": "Normal", "color": "green"}
KINDS = [MAQ, MANQ, MAMD, NORM]

SEE_ALL = {"k": "all", "label": "Yes, all vowels show", "color": "green"}
SEE_NONE = {"k": "none", "label": "No, all are hidden", "color": "brown"}
SEE_FATHA = {"k": "fatha", "label": "Only fatha shows", "color": "brown"}
SEE = [SEE_ALL, SEE_NONE, SEE_FATHA]

H_D = {"k": "damma", "label": "Damma is hidden (rafʿ)", "color": "red"}
H_F = {"k": "fatha", "label": "Fatha is hidden (naṣb)", "color": "pink"}
H_K = {"k": "kasra", "label": "Kasra is hidden (jarr)", "color": "green"}
H_N = {"k": "nothing", "label": "Nothing is hidden", "color": "grey"}
HIDDEN = [H_D, H_F, H_K, H_N]

SHOWS = {"k": "shows", "label": "Shows its vowel", "color": "green"}
HIDES = {"k": "hides", "label": "Vowel hidden", "color": "brown"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s4-hidden",
    "order": 8,
    "title": "When the vowel is hidden",
    "ar": "الْإِعْرَابُ الْمُقَدَّرُ",
    "blurb": "Nouns ending in alif or in ي, and nouns with ـي \"my\": their case vowel is there, but we cannot see it.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 4 · UNIT 8", "title": "A vowel we cannot see",
         "text": "Some nouns cannot show a vowel on their last letter. The case is still there. We say the vowel is assumed: {مُقَدَّرٌ}.",
         "wm": "الْفَتَى"},

        {"t": "h2", "text": "Three groups and one contrast"},
        {"t": "p", "text": "Every flexible noun is in rafʿ, naṣb or jarr. Usually we see the sign. In these groups the last letter cannot carry it. The sign is still the original one (damma, fatha, kasra), only hidden."},
        {"t": "cols", "items": [
            {"color": "brown", "title": "Maqṣūr", "ar": "الْفَتَى", "text": "Ends in alif. All vowels hidden."},
            {"color": "brown", "title": "Manqūṣ", "ar": "الْقَاضِي", "text": "Ends in {ي} after kasra. Damma and kasra hidden."},
            {"color": "brown", "title": "With ـي \"my\"", "ar": "كِتَابِي", "text": "All vowels hidden."},
            {"color": "olive", "title": "Mamdūd", "ar": "السَّمَاءُ", "text": "Ends in {ـَاءُ}. Nothing hidden."},
        ]},

        {"t": "h2", "text": "الْمَقْصُورُ: ends in alif"},
        {"t": "p", "text": "A maqṣūr noun ends in alif, written {ى} or {ا}. An alif cannot carry a vowel, so all three vowels are hidden."},
        {"t": "words", "items": [
            {"ar": "الْفَتَى", "sub": "the young man", "color": "brown"},
            {"ar": "مُوسَى", "sub": "Musa", "color": "brown"},
            {"ar": "الْمُسْتَشْفَى", "sub": "the hospital", "color": "brown"},
            {"ar": "الْعَصَا", "sub": "the stick", "color": "brown"},
        ]},
        {"t": "table", "head": ["Case", "Form", "What happens"], "rows": [
            ["Rafʿ", "الْفَتَى", "Damma hidden"],
            ["Naṣb", "الْفَتَى", "Fatha hidden"],
            ["Jarr", "الْفَتَى", "Kasra hidden"],
        ]},
        {"t": "examples", "items": [
            {"ar": "الْفَتَى طَالِبٌ.", "en": "The young man is a student.", "note": "Topic in rafʿ. The damma is hidden."},
            {"ar": "ذَهَبَ الطَّبِيبُ إِلَى الْمُسْتَشْفَى.", "en": "The doctor went to the hospital.", "note": "Jarr after {إِلَى}. The kasra is hidden."},
            {"ar": "أَخَذَ الرَّجُلُ الْعَصَا.", "en": "The man took the stick.", "note": "Object in naṣb. The fatha is hidden."},
        ]},
        {"t": "tip", "text": "With no {ال} the tanween sits on the letter before the alif: {فَتًى}، {عَصًا}، {مُسْتَشْفًى}. It is the same word. {مُوسَى} is a foreign name, so it has no tanween (unit 6)."},

        {"t": "h2", "text": "الْمَنْقُوصُ: ends in ي after kasra"},
        {"t": "p", "text": "A manqūṣ noun ends in {ي} with kasra before it. Damma and kasra are too heavy on this {ي}, so they are hidden. Fatha is light, so it shows."},
        {"t": "words", "items": [
            {"ar": "الْقَاضِي", "sub": "the judge", "color": "brown"},
            {"ar": "الْمُحَامِي", "sub": "the lawyer", "color": "brown"},
            {"ar": "النَّادِي", "sub": "the club", "color": "brown"},
        ]},
        {"t": "table", "head": ["Case", "Form", "What happens"], "rows": [
            ["Rafʿ", "الْقَاضِي", "Damma hidden"],
            ["Naṣb", "الْقَاضِيَ", "Fatha shows"],
            ["Jarr", "الْقَاضِي", "Kasra hidden"],
        ]},
        {"t": "examples", "items": [
            {"ar": "الْمُحَامِي فِي النَّادِي.", "en": "The lawyer is in the club.", "note": "Both vowels are hidden: damma on {الْمُحَامِي}, kasra on {النَّادِي}."},
            {"ar": "رَأَيْتُ الْقَاضِيَ.", "en": "I saw the judge.", "note": "Object in naṣb. The fatha shows."},
        ]},
        {"t": "tip", "text": "Preview: with no {ال}, in rafʿ and jarr the {ي} drops and the tanween sits under the letter before: {قَاضٍ}، {مُحَامٍ}، {نَادٍ}. It is the same word."},
        {"t": "tip", "text": "{كُرْسِيٌّ} ends in {ي} with shadda. It is not manqūṣ. It shows all its vowels."},

        {"t": "h2", "text": "The noun with ـي \"my\""},
        {"t": "p", "text": "You met {كِتَابِي} in Stage 3. The pronoun {ـي} needs a kasra before it. That kasra takes the place of the case vowel, so the case vowel is hidden in all three cases."},
        {"t": "examples", "items": [
            {"ar": "كِتَابِي جَدِيدٌ.", "en": "My book is new.", "note": "Rafʿ. The damma is hidden."},
            {"ar": "فَتَحْتُ كِتَابِي.", "en": "I opened my book.", "note": "Naṣb. The fatha is hidden."},
            {"ar": "الْقَلَمُ فِي بَيْتِي.", "en": "The pen is in my house.", "note": "Jarr. The kasra you see belongs to {ـي}. The case kasra is hidden."},
        ]},
        {"t": "tip", "text": "The same happens with the five nouns: {أَبِي}، {أَخِي} (unit 7)."},

        {"t": "h2", "text": "الْمَمْدُودُ: nothing is hidden"},
        {"t": "p", "text": "A mamdūd noun ends in alif and then hamza: {سَمَاءٌ}، {هَوَاءٌ}، {صَحْرَاءُ}. The hamza is a real letter. It carries the vowel, so we see it."},
        {"t": "examples", "items": [
            {"ar": "السَّمَاءُ جَمِيلَةٌ.", "en": "The sky is beautiful.", "note": "The damma shows on the hamza."},
            {"ar": "نَظَرْتُ إِلَى السَّمَاءِ.", "en": "I looked at the sky.", "note": "The kasra shows."},
        ]},
        {"t": "tip", "text": "Some mamdūd nouns are diptotes ({صَحْرَاءُ}), so they have no tanween. Their vowel still shows."},

        {"t": "h2", "text": "Can we see the vowel?"},
        {"t": "table", "head": ["Group", "Example", "Rafʿ", "Naṣb", "Jarr"], "rows": [
            ["Maqṣūr", "الْفَتَى", "hidden", "hidden", "hidden"],
            ["Manqūṣ", "الْقَاضِي", "hidden", "shows", "hidden"],
            ["With ـي", "كِتَابِي", "hidden", "hidden", "hidden"],
            ["Mamdūd", "السَّمَاءُ", "shows", "shows", "shows"],
            ["Normal", "الْكِتَابُ", "shows", "shows", "shows"],
        ]},

        {"t": "summary", "title": "In short", "items": [
            "Maqṣūr ends in alif ({الْفَتَى}، {الْعَصَا}): all three vowels are hidden. Nakira: {فَتًى}.",
            "Manqūṣ ends in {ي} after kasra ({الْقَاضِي}): damma and kasra hidden, fatha shows ({الْقَاضِيَ}). Nakira: {قَاضٍ}.",
            "With {ـي} \"my\" ({كِتَابِي}): all three vowels are hidden.",
            "Mamdūd ends in {ـَاءُ} ({السَّمَاءُ}): the hamza carries the vowel. Nothing is hidden.",
        ]},
    ],

    "practice": [
        {
            "title": "Maqṣūr, manqūṣ, mamdūd or normal?",
            "fields": [{"key": "kind", "label": "Kind", "options": KINDS}],
            "rows": [
                {"s": "الْفَتَى", "gloss": "the young man", "ans": {"kind": "maq"}, "why": "It ends in alif ({ى})."},
                {"s": "الْقَاضِي", "gloss": "the judge", "ans": {"kind": "manq"}, "why": "It ends in {ي} after kasra."},
                {"s": "السَّمَاءُ", "gloss": "the sky", "ans": {"kind": "mamd"}, "why": "It ends in alif and hamza."},
                {"s": "الْكِتَابُ", "gloss": "the book", "ans": {"kind": "norm"}, "why": "It ends in {ب}, which carries the damma."},
                {"s": "الْعَصَا", "gloss": "the stick", "ans": {"kind": "maq"}, "why": "It ends in alif, written {ا}."},
                {"s": "النَّادِي", "gloss": "the club", "ans": {"kind": "manq"}, "why": "It ends in {ي} after kasra."},
            ],
        },
        {
            "title": "Can we see the case vowel?",
            "fields": [{"key": "see", "label": "Vowels", "options": SEE}],
            "rows": [
                {"s": "الْمُسْتَشْفَى", "gloss": "the hospital", "ans": {"see": "none"}, "why": "Maqṣūr: all three are hidden."},
                {"s": "الْمُحَامِي", "gloss": "the lawyer", "ans": {"see": "fatha"}, "why": "Manqūṣ: {الْمُحَامِيَ} shows fatha. Damma and kasra are hidden."},
                {"s": "الصَّحْرَاءُ", "gloss": "the desert", "ans": {"see": "all"}, "why": "Mamdūd: the hamza carries every vowel."},
                {"s": "قَلَمِي", "gloss": "my pen", "ans": {"see": "none"}, "why": "With {ـي} \"my\": all three are hidden."},
                {"s": "الْكُرْسِيُّ", "gloss": "the chair", "ans": {"see": "all"}, "why": "The {ي} has shadda. It carries every vowel."},
                {"s": "مُوسَى", "gloss": "Musa", "ans": {"see": "none"}, "why": "Maqṣūr: it ends in alif."},
            ],
        },
        {
            "title": "What is hidden in the word in [ ]?",
            "fields": [{"key": "hid", "label": "Hidden", "options": HIDDEN}],
            "rows": [
                {"s": "[الْفَتَى] طَالِبٌ.", "gloss": "The young man is a student.", "ans": {"hid": "damma"},
                 "why": "Topic in rafʿ. The alif hides the damma."},
                {"s": "ذَهَبْتُ إِلَى [الْمُسْتَشْفَى].", "gloss": "I went to the hospital.", "ans": {"hid": "kasra"},
                 "why": "Jarr after {إِلَى}. The alif hides the kasra."},
                {"s": "رَأَيْتُ [الْقَاضِيَ].", "gloss": "I saw the judge.", "ans": {"hid": "nothing"},
                 "why": "Object in naṣb. A manqūṣ noun shows fatha."},
                {"s": "[الْقَاضِي] فِي الْمَسْجِدِ.", "gloss": "The judge is in the mosque.", "ans": {"hid": "damma"},
                 "why": "Topic in rafʿ. The damma is hidden on the {ي}."},
                {"s": "فَتَحَ [مُوسَى] الْبَابَ.", "gloss": "Musa opened the door.", "ans": {"hid": "damma"},
                 "why": "Doer in rafʿ. The alif hides the damma."},
                {"s": "نَظَرْتُ إِلَى [السَّمَاءِ].", "gloss": "I looked at the sky.", "ans": {"hid": "nothing"},
                 "why": "Mamdūd: the kasra shows on the hamza."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "الْفَتَى فِي الْمَسْجِدِ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The young man is in the mosque.", "The judge is in the mosque.", "The stick is in the mosque.")},
                 "why": "{الْفَتَى} is \"the young man\"."},
                {"s": "الْعَصَا عَلَى الْمَكْتَبِ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("The key is on the desk.", "The stick is on the desk.", "The stick is under the desk.")},
                 "why": "{الْعَصَا} is \"the stick\". {عَلَى} is \"on\"."},
                {"s": "ذَهَبَ الْمُحَامِي إِلَى النَّادِي.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("The judge went to the club.", "The lawyer went to the hospital.", "The lawyer went to the club.")},
                 "why": "{الْمُحَامِي} \"the lawyer\", {النَّادِي} \"the club\"."},
                {"s": "الْقَاضِي فِي الْمُسْتَشْفَى.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The judge is in the hospital.", "The lawyer is in the hospital.", "The judge is in the club.")},
                 "why": "{الْقَاضِي} \"the judge\", {الْمُسْتَشْفَى} \"the hospital\"."},
                {"s": "كِتَابِي جَدِيدٌ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("Your book is new.", "My book is new.", "The book is new.")},
                 "why": "{ـي} means \"my\"."},
            ],
        },
        {
            "title": "Same word with tanween",
            "fields": [{"key": "pick", "label": "Same word", "options": []}],
            "rows": [
                {"s": "الْفَتَى → without ال", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فَتًى", "فَتٌ", "فَتَى")}, "why": "Maqṣūr: the tanween sits on {ت}, and the {ى} stays."},
                {"s": "الْقَاضِي → without ال", "ans": {"pick": "c"},
                 "opts": {"pick": pick("قَاضِيٌ", "قَاضٌ", "قَاضٍ")}, "why": "Manqūṣ: the {ي} drops and the tanween is under {ض}."},
                {"s": "عَصًا → with ال", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْعَصُ", "الْعَصَا", "الْعَصَاءُ")}, "why": "The same maqṣūr word: {الْعَصَا}. There is no hamza."},
                {"s": "مُحَامٍ → with ال", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الْمُحَامِي", "الْمُحَامُ", "الْمُحَامِيَةُ")}, "why": "With {ال} the {ي} comes back: {الْمُحَامِي}. {الْمُحَامِيَةُ} is a woman lawyer."},
                {"s": "الْمُسْتَشْفَى → without ال", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُسْتَشْفَاءٌ", "مُسْتَشْفًى", "مُسْتَشْفٌ")}, "why": "Maqṣūr: the tanween sits on {ف}, and the {ى} stays."},
            ],
        },
        {
            "title": "Does each word show its case vowel?",
            "prompt": "كِتَابِي عَلَى مَكْتَبِ الْقَاضِي فِي النَّادِي.",
            "en": "My book is on the judge's desk in the club.",
            "fields": [{"key": "show", "label": "Case vowel", "options": [SHOWS, HIDES]}],
            "rows": [
                {"s": "كِتَابِي", "ans": {"show": "hides"}, "why": "With {ـي} \"my\": the damma is hidden."},
                {"s": "مَكْتَبِ", "ans": {"show": "shows"}, "why": "A normal noun after {عَلَى}: we see the kasra."},
                {"s": "الْقَاضِي", "ans": {"show": "hides"}, "why": "The owner, in jarr. Manqūṣ hides the kasra."},
                {"s": "النَّادِي", "ans": {"show": "hides"}, "why": "After {فِي}, in jarr. Manqūṣ hides the kasra."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Maqṣūr, manqūṣ, mamdūd or normal?",
            "fields": [{"key": "kind", "label": "Kind", "options": KINDS}],
            "rows": [
                {"s": "الْهُدَى", "gloss": "the guidance", "ans": {"kind": "maq"}, "why": "It ends in alif ({ى})."},
                {"s": "الرَّاعِي", "gloss": "the shepherd", "ans": {"kind": "manq"}, "why": "It ends in {ي} after kasra."},
                {"s": "الْغَدَاءُ", "gloss": "the lunch", "ans": {"kind": "mamd"}, "why": "It ends in alif and hamza."},
                {"s": "الْعَرَبِيُّ", "gloss": "the Arab", "ans": {"kind": "norm"}, "why": "The {ي} has shadda and carries the damma."},
                {"s": "الدُّنْيَا", "gloss": "this world", "ans": {"kind": "maq"}, "why": "It ends in alif, written {ا}."},
                {"s": "الْوَادِي", "gloss": "the valley", "ans": {"kind": "manq"}, "why": "It ends in {ي} after kasra."},
            ],
        },
        {
            "title": "Can we see the case vowel?",
            "fields": [{"key": "see", "label": "Vowels", "options": SEE}],
            "rows": [
                {"s": "الْهَوَاءُ", "gloss": "the air", "ans": {"see": "all"}, "why": "Mamdūd: the hamza carries every vowel."},
                {"s": "الْمَاشِي", "gloss": "the walker", "ans": {"see": "fatha"}, "why": "Manqūṣ: only fatha shows ({الْمَاشِيَ})."},
                {"s": "بَيْتِي", "gloss": "my house", "ans": {"see": "none"}, "why": "With {ـي} \"my\": all three are hidden."},
                {"s": "عِيسَى", "gloss": "Isa", "ans": {"see": "none"}, "why": "Maqṣūr: it ends in alif."},
                {"s": "الصَّبِيُّ", "gloss": "the boy", "ans": {"see": "all"}, "why": "The {ي} has shadda. It carries every vowel."},
                {"s": "أَخِي", "gloss": "my brother", "ans": {"see": "none"}, "why": "With {ـي} \"my\": all three are hidden (unit 7)."},
            ],
        },
        {
            "title": "What is hidden in the word in [ ]?",
            "fields": [{"key": "hid", "label": "Hidden", "options": HIDDEN}],
            "rows": [
                {"s": "[عِيسَى] نَبِيٌّ.", "gloss": "Isa is a prophet.", "ans": {"hid": "damma"},
                 "why": "Topic in rafʿ. The alif hides the damma."},
                {"s": "ذَهَبْنَا إِلَى [الْوَادِي].", "gloss": "We went to the valley.", "ans": {"hid": "kasra"},
                 "why": "Jarr after {إِلَى}. Manqūṣ hides the kasra."},
                {"s": "شَكَرَ الْمُدِيرُ [الرَّاعِيَ].", "gloss": "The principal thanked the shepherd.", "ans": {"hid": "nothing"},
                 "why": "Object in naṣb. A manqūṣ noun shows fatha."},
                {"s": "فَتَحْتُ [كِتَابِي].", "gloss": "I opened my book.", "ans": {"hid": "fatha"},
                 "why": "Object in naṣb. With {ـي} the fatha is hidden."},
                {"s": "[الْمَاءُ] بَارِدٌ.", "gloss": "The water is cold.", "ans": {"hid": "nothing"},
                 "why": "The hamza is a real letter. The damma shows on it."},
                {"s": "[الدُّنْيَا] جَمِيلَةٌ.", "gloss": "This world is beautiful.", "ans": {"hid": "damma"},
                 "why": "Topic in rafʿ. The alif hides the damma."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "الرَّاعِي فِي الْوَادِي.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The shepherd is in the valley.", "The judge is in the valley.", "The shepherd is in the club.")},
                 "why": "{الرَّاعِي} \"the shepherd\", {الْوَادِي} \"the valley\"."},
                {"s": "هَذَا فَتًى طَوِيلٌ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("This young man is tall.", "That is a tall young man.", "This is a tall young man.")},
                 "why": "{فَتًى} has no {ال}, so {هَذَا} starts a sentence: \"This is a tall young man.\""},
                {"s": "هَذَا قَاضٍ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("this judge", "This is a judge.", "This is the judge.")},
                 "why": "{قَاضٍ} is {الْقَاضِي} with no {ال}: \"a judge\"."},
                {"s": "ذَهَبَ أَبِي إِلَى الْمُسْتَشْفَى.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("My father went to the hospital.", "Your father went to the hospital.", "My father went to the club.")},
                 "why": "{أَبِي} \"my father\", {الْمُسْتَشْفَى} \"the hospital\"."},
                {"s": "قَلَمِي فِي حَقِيبَتِي.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("My pen is in your bag.", "My pen is in my bag.", "Your pen is in my bag.")},
                 "why": "Both words end in {ـي} \"my\"."},
            ],
        },
        {
            "title": "Same word with or without tanween",
            "fields": [{"key": "pick", "label": "Same word", "options": []}],
            "rows": [
                {"s": "وَادٍ → with ال", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الْوَادِي", "الْوَادُ", "الْوِدَادُ")}, "why": "With {ال} the {ي} comes back: {الْوَادِي}."},
                {"s": "الرَّاعِي → without ال", "ans": {"pick": "c"},
                 "opts": {"pick": pick("رَاعِيٌ", "رَاعٌ", "رَاعٍ")}, "why": "Manqūṣ: the {ي} drops and the tanween is under {ع}."},
                {"s": "هُدًى → with ال", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْهُدُ", "الْهُدَى", "الْهُدَاءُ")}, "why": "The same maqṣūr word. There is no hamza."},
                {"s": "الْمَاشِي → without ال", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَاشٍ", "مَاشِيٌ", "مَاشٌ")}, "why": "Manqūṣ: the {ي} drops and the tanween is under {ش}."},
                {"s": "نَادٍ → with ال", "ans": {"pick": "b"},
                 "opts": {"pick": pick("النَّادُ", "النَّادِي", "النِّدَاءُ")}, "why": "With {ال} the {ي} comes back. {النِّدَاءُ} \"the call\" is another word."},
            ],
        },
        {
            "title": "Does each word show its case vowel?",
            "prompt": "الرَّاعِي فِي الصَّحْرَاءِ وَأَخِي فِي الْوَادِي.",
            "en": "The shepherd is in the desert, and my brother is in the valley.",
            "fields": [{"key": "show", "label": "Case vowel", "options": [SHOWS, HIDES]}],
            "rows": [
                {"s": "الرَّاعِي", "ans": {"show": "hides"}, "why": "Topic in rafʿ. Manqūṣ hides the damma."},
                {"s": "الصَّحْرَاءِ", "ans": {"show": "shows"}, "why": "Mamdūd with {ال}: we see the kasra on the hamza."},
                {"s": "أَخِي", "ans": {"show": "hides"}, "why": "With {ـي} \"my\": the damma is hidden."},
                {"s": "الْوَادِي", "ans": {"show": "hides"}, "why": "After {فِي}, in jarr. Manqūṣ hides the kasra."},
            ],
        },
    ],
}
