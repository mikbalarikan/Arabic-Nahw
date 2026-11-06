# Stage 4, Unit 6: Nouns without tanween (الْمَمْنُوعُ مِنَ الصَّرْفِ)

TAN = {"k": "tan", "label": "Takes tanween", "color": "green"}
NOTAN = {"k": "notan", "label": "No tanween (diptote)", "color": "orange"}

G_NAME = {"k": "name", "label": "A name"}
G_ADJ = {"k": "adj", "label": "Adjective أَفْعَلُ / فَعْلَانُ"}
G_ALIF = {"k": "alif", "label": "Ends in the extra ـَاءُ"}
G_PL = {"k": "pl", "label": "Plural مَفَاعِلُ / مَفَاعِيلُ"}
GROUPS = [G_NAME, G_ADJ, G_ALIF, G_PL]

N_FEM = {"k": "fem", "label": "Feminine, or ends in ة"}
N_FOR = {"k": "for", "label": "Foreign name"}
N_VERB = {"k": "verb", "label": "Verb shape"}
N_AN = {"k": "an", "label": "Ends in ـَانُ"}
N_FUAL = {"k": "fual", "label": "Shape فُعَلُ"}
NAMES = [N_FEM, N_FOR, N_VERB, N_AN, N_FUAL]

W_DIP = {"k": "dip", "label": "Jarr, diptote: fatha", "color": "orange"}
W_AL = {"k": "al", "label": "Jarr with ال or an owner: kasra", "color": "green"}
W_OBJ = {"k": "obj", "label": "Object: naṣb fatha", "color": "pink"}
W_MIS = {"k": "mis", "label": "Mistake", "color": "grey"}
WHY = [W_DIP, W_AL, W_OBJ, W_MIS]


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s4-diptotes",
    "order": 6,
    "title": "Nouns without tanween",
    "ar": "الْمَمْنُوعُ مِنَ الصَّرْفِ",
    "blurb": "Names, adjectives and plurals that never take tanween, and how to spot them.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 4 · UNIT 6", "title": "Nouns that never take tanween",
         "text": "Most nouns take tanween when they have no {ال}. A small set of nouns never does. We call them diptotes.",
         "wm": "مَسَاجِدُ"},

        {"t": "h2", "text": "What a diptote is"},
        {"t": "p", "text": "{كِتَابٌ}، {مَسْجِدٌ} and {مُحَمَّدٌ} take tanween. {مَسَاجِدُ}، {أَحْمَدُ} and {فَاطِمَةُ} never do. Arabic calls these words {الْمَمْنُوعُ مِنَ الصَّرْفِ} \"kept from tanween\"."},
        {"t": "cols", "items": [
            {"color": "green", "title": "Normal noun", "ar": "مَسْجِدٌ",
             "text": "Takes tanween and the original signs."},
            {"color": "orange", "title": "Diptote", "ar": "مَسَاجِدُ",
             "text": "One damma, never tanween."},
        ]},
        {"t": "rule", "color": "orange", "title": "Two things are different",
         "text": "A diptote never takes tanween. In jarr it takes fatha instead of kasra: {فِي مَسَاجِدَ كَثِيرَةٍ}. With {ال} or an owner it takes kasra again."},
        {"t": "table", "head": ["", "Rafʿ", "Naṣb", "Jarr"], "rows": [
            ["Diptote alone", "مَسَاجِدُ", "مَسَاجِدَ", "مَسَاجِدَ"],
            ["With ال", "الْمَسَاجِدُ", "الْمَسَاجِدَ", "الْمَسَاجِدِ"],
            ["With an owner", "مَسَاجِدُ الْمَدِينَةِ", "مَسَاجِدَ الْمَدِينَةِ", "مَسَاجِدِ الْمَدِينَةِ"],
        ]},
        {"t": "examples", "items": [
            {"ar": "صَلَّيْتُ فِي مَسَاجِدَ كَثِيرَةٍ.", "en": "I prayed in many mosques.", "note": "Jarr after {فِي}, but {مَسَاجِدَ} ends in fatha."},
            {"ar": "صَلَّيْتُ فِي مَسَاجِدِ الْمَدِينَةِ.", "en": "I prayed in the mosques of Madinah.", "note": "It has an owner, so it takes kasra: {مَسَاجِدِ}."},
        ]},
        {"t": "tip", "text": "You will practise the jarr rule in Stage 6. In this unit, learn which words are diptotes."},

        {"t": "h2", "text": "Group 1: names"},
        {"t": "p", "text": "Many names are diptotes. Learn the five kinds."},
        {"t": "table", "head": ["Kind of name", "Examples"], "rows": [
            ["Feminine names, and men's names ending in {ة}", "فَاطِمَةُ، زَيْنَبُ، مَرْيَمُ، عَائِشَةُ، حَمْزَةُ، طَلْحَةُ"],
            ["Foreign names", "إِبْرَاهِيمُ، يُوسُفُ، إِسْمَاعِيلُ"],
            ["Names with the shape of a verb", "أَحْمَدُ، يَزِيدُ"],
            ["Names ending in {ـَانُ}", "عُثْمَانُ، سُلَيْمَانُ، رَمَضَانُ"],
            ["Names on the shape {فُعَلُ}", "عُمَرُ"],
        ]},
        {"t": "p", "text": "{أَحْمَدُ} and {يَزِيدُ} look like verb forms you will meet later. {رَمَضَانُ} is the name of a month."},
        {"t": "tip", "text": "Madinah lesson 4: Arabic men's names like {مُحَمَّدٌ}، {خَالِدٌ}، {حَامِدٌ}، {عَلِيٌّ} take tanween. They have none of these five reasons."},

        {"t": "h2", "text": "Group 2: adjectives"},
        {"t": "table", "head": ["Shape", "Meaning", "Examples"], "rows": [
            ["أَفْعَلُ", "a colour", "{أَحْمَرُ} red، {أَزْرَقُ} blue، {أَبْيَضُ} white"],
            ["أَفْعَلُ", "more, bigger", "{أَكْبَرُ} bigger، {أَصْغَرُ} smaller، {أَجْمَلُ} more beautiful"],
            ["فَعْلَانُ", "a feeling", "{عَطْشَانُ} thirsty، {غَضْبَانُ} angry، {جَوْعَانُ} hungry"],
        ]},
        {"t": "examples", "items": [
            {"ar": "هَذَا قَلَمٌ أَحْمَرُ.", "en": "This is a red pen.", "note": "The noun has tanween. The adjective has none, but it still copies the damma."},
            {"ar": "الْوَلَدُ عَطْشَانُ.", "en": "The boy is thirsty.", "note": "Information in rafʿ, with one damma."},
            {"ar": "أَحْمَدُ أَكْبَرُ مِنْ خَالِدٍ.", "en": "Ahmad is bigger than Khalid.", "note": "{أَحْمَدُ} and {أَكْبَرُ} are diptotes. {خَالِدٍ} is not."},
        ]},
        {"t": "tip", "text": "{أَرْنَبٌ} \"a rabbit\" has the shape {أَفْعَلُ}, but it is a thing, not a describing word. It takes tanween."},

        {"t": "h2", "text": "Group 3: the extra ـَاءُ"},
        {"t": "p", "text": "Some nouns end in {ـَاءُ} that works like {ة}: it is an extra feminine ending. These nouns never take tanween."},
        {"t": "table", "head": ["Kind", "Examples"], "rows": [
            ["Things", "{صَحْرَاءُ} desert"],
            ["Feminine colours", "{أَحْمَرُ} → {حَمْرَاءُ}، {أَبْيَضُ} → {بَيْضَاءُ}، {أَزْرَقُ} → {زَرْقَاءُ}"],
            ["Plurals", "{أَصْدِقَاءُ} friends، {وُزَرَاءُ} ministers، {عُلَمَاءُ} scholars"],
        ]},
        {"t": "p", "text": "A few feminine words end in {ـَى} instead, like {كُبْرَى} \"biggest (f.)\". They also have no tanween. Their vowel is hidden: see unit 8."},
        {"t": "tip", "text": "In {سَمَاءٌ}، {مَاءٌ}، {هَوَاءٌ} and {غَدَاءٌ} the hamza belongs to the word. It is not the extra ending, so they take tanween. The same is true of {أَسْمَاءٌ}, the plural of {اسْمٌ}."},

        {"t": "h2", "text": "Group 4: the long plurals"},
        {"t": "p", "text": "A broken plural with two letters, then {ا}, then two letters ({مَفَاعِلُ}), or three letters with {ي} in the middle ({مَفَاعِيلُ}), is a diptote."},
        {"t": "table", "head": ["Singular", "Plural"], "rows": [
            ["مَسْجِدٌ", "مَسَاجِدُ"],
            ["مَكْتَبٌ", "مَكَاتِبُ"],
            ["مَدْرَسَةٌ", "مَدَارِسُ"],
            ["مَطْبَخٌ", "مَطَابِخُ"],
            ["مِفْتَاحٌ", "مَفَاتِيحُ"],
            ["مِنْدِيلٌ", "مَنَادِيلُ"],
        ]},
        {"t": "tip", "text": "Only the plural is a diptote. The singular {مَسْجِدٌ} takes tanween. Other broken plurals take tanween too: {كُتُبٌ}، {أَقْلَامٌ}، {رِجَالٌ}، {بُيُوتٌ}."},
        {"t": "tip", "text": "Plurals like {وُزَرَاءُ} and {عُلَمَاءُ} also have no tanween. Their reason is the extra {ـَاءُ} of group 3."},

        {"t": "h2", "text": "Look-alikes that take tanween"},
        {"t": "table", "head": ["Word", "It looks like", "Why it takes tanween"], "rows": [
            ["مُحَمَّدٌ، عَلِيٌّ، زَيْدٌ، خَالِدٌ", "a name", "Arabic men's names with no other reason."],
            ["أَرْنَبٌ", "{أَفْعَلُ}", "A thing, not an adjective."],
            ["إِنْسَانٌ، دُكَّانٌ", "{ـَانُ}", "Not a name and not an adjective."],
            ["سَمَاءٌ، مَاءٌ، أَسْمَاءٌ", "{ـَاءُ}", "The hamza belongs to the word."],
            ["كُتُبٌ، أَقْلَامٌ", "a plural", "Not on the shape {مَفَاعِلُ}."],
            ["مَسْجِدٌ، مِفْتَاحٌ", "{مَسَاجِدُ}", "Singular."],
        ]},

        {"t": "summary", "title": "In short", "items": [
            "A diptote never takes tanween: {فَاطِمَةُ}، {أَحْمَرُ}، {مَسَاجِدُ}.",
            "Names: feminine or ending in {ة}, foreign, verb shape, {ـَانُ}, {فُعَلُ}.",
            "Adjectives: {أَفْعَلُ} ({أَحْمَرُ}، {أَكْبَرُ}) and {فَعْلَانُ} ({عَطْشَانُ}).",
            "The extra {ـَاءُ}: {صَحْرَاءُ}، {حَمْرَاءُ}، {أَصْدِقَاءُ}. Long plurals: {مَسَاجِدُ}، {مَفَاتِيحُ}.",
            "In jarr it takes fatha: {فِي مَسَاجِدَ}. With {ال} or an owner, kasra: {فِي الْمَسَاجِدِ}. Practice in Stage 6.",
        ]},
    ],

    "practice": [
        {
            "title": "Take away ال: tanween or no tanween?",
            "fields": [{"key": "tan", "label": "Without ال", "options": [TAN, NOTAN]}],
            "rows": [
                {"s": "الْمَسَاجِدُ", "gloss": "the mosques", "ans": {"tan": "notan"}, "why": "A long plural: {مَسَاجِدُ}."},
                {"s": "الْكُتُبُ", "gloss": "the books", "ans": {"tan": "tan"}, "why": "A broken plural, but not on {مَفَاعِلُ}: {كُتُبٌ}."},
                {"s": "الْأَحْمَرُ", "gloss": "the red", "ans": {"tan": "notan"}, "why": "A colour on {أَفْعَلُ}: {أَحْمَرُ}."},
                {"s": "السَّمَاءُ", "gloss": "the sky", "ans": {"tan": "tan"}, "why": "The hamza belongs to the word: {سَمَاءٌ}."},
                {"s": "الصَّحْرَاءُ", "gloss": "the desert", "ans": {"tan": "notan"}, "why": "The extra {ـَاءُ}: {صَحْرَاءُ}."},
                {"s": "الْمَسْجِدُ", "gloss": "the mosque", "ans": {"tan": "tan"}, "why": "The singular takes tanween: {مَسْجِدٌ}."},
            ],
        },
        {
            "title": "Choose the right spelling",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "... فِي الْبَيْتِ", "gloss": "Fatima is in the house.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فَاطِمَةُ", "فَاطِمَةٌ")}, "why": "A feminine name: no tanween."},
                {"s": "... طَالِبٌ", "gloss": "Muhammad is a student.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُحَمَّدٌ", "مُحَمَّدُ")}, "why": "An Arabic man's name with no diptote reason: {مُحَمَّدٌ}."},
                {"s": "هَذِهِ ...", "gloss": "These are mosques.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَسَاجِدٌ", "مَسَاجِدُ")}, "why": "A long plural never takes tanween."},
                {"s": "... طَبِيبٌ", "gloss": "Yusuf is a doctor.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يُوسُفُ", "يُوسُفٌ")}, "why": "A foreign name: no tanween."},
                {"s": "... طَوِيلٌ", "gloss": "Ahmad is tall.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَحْمَدٌ", "أَحْمَدُ")}, "why": "A name with the shape of a verb: no tanween."},
                {"s": "... تَاجِرٌ", "gloss": "Khalid is a merchant.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("خَالِدٌ", "خَالِدُ")}, "why": "Like {مُحَمَّدٌ}, it takes tanween (Madinah lesson 4)."},
            ],
        },
        {
            "title": "Which group is this diptote in?",
            "fields": [{"key": "group", "label": "Group", "options": GROUPS}],
            "rows": [
                {"s": "زَيْنَبُ", "ans": {"group": "name"}, "why": "A feminine name."},
                {"s": "أَصْغَرُ", "gloss": "smaller", "ans": {"group": "adj"}, "why": "\"More small\" on {أَفْعَلُ}."},
                {"s": "صَحْرَاءُ", "gloss": "desert", "ans": {"group": "alif"}, "why": "It ends in the extra {ـَاءُ}."},
                {"s": "مَفَاتِيحُ", "gloss": "keys", "ans": {"group": "pl"}, "why": "The plural of {مِفْتَاحٌ} on {مَفَاعِيلُ}."},
                {"s": "عَطْشَانُ", "gloss": "thirsty", "ans": {"group": "adj"}, "why": "A describing word on {فَعْلَانُ}."},
                {"s": "إِبْرَاهِيمُ", "ans": {"group": "name"}, "why": "A foreign name."},
            ],
        },
        {
            "title": "Which one takes tanween without ال?",
            "fields": [{"key": "pick", "label": "Takes tanween", "options": []}],
            "rows": [
                {"s": "the offices / the pens / the keys", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْمَكَاتِبُ", "الْأَقْلَامُ", "الْمَفَاتِيحُ")},
                 "why": "{أَقْلَامٌ} is a broken plural, but not on {مَفَاعِلُ}."},
                {"s": "the thirsty / the person / the angry", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْعَطْشَانُ", "الْإِنْسَانُ", "الْغَضْبَانُ")},
                 "why": "{إِنْسَانٌ} ends in {ـَانُ} but is not a name or an adjective."},
                {"s": "the desert / the water / the red (f.)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الصَّحْرَاءُ", "الْمَاءُ", "الْحَمْرَاءُ")},
                 "why": "In {مَاءٌ} the hamza belongs to the word."},
                {"s": "the friends / the ministers / the names", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الْأَصْدِقَاءُ", "الْوُزَرَاءُ", "الْأَسْمَاءُ")},
                 "why": "{أَسْمَاءٌ}, the plural of {اسْمٌ}: its hamza belongs to the word."},
                {"s": "the houses / the mosques / the offices", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الْبُيُوتُ", "الْمَسَاجِدُ", "الْمَكَاتِبُ")},
                 "why": "{بُيُوتٌ} takes tanween. The other two are long plurals."},
            ],
        },
        {
            "title": "Which kind of name?",
            "fields": [{"key": "kind", "label": "Kind", "options": NAMES}],
            "rows": [
                {"s": "عَائِشَةُ", "ans": {"kind": "fem"}, "why": "A woman's name."},
                {"s": "يُوسُفُ", "ans": {"kind": "for"}, "why": "A foreign name."},
                {"s": "أَحْمَدُ", "ans": {"kind": "verb"}, "why": "It has the shape of a verb."},
                {"s": "عُثْمَانُ", "ans": {"kind": "an"}, "why": "It ends in {ـَانُ}."},
                {"s": "حَمْزَةُ", "ans": {"kind": "fem"}, "why": "A man's name, but it ends in {ة}."},
                {"s": "يَزِيدُ", "ans": {"kind": "verb"}, "why": "It has the shape of a verb."},
            ],
        },
        {
            "title": "Why does the word in [ ] end like this?",
            "fields": [{"key": "why", "label": "Reason", "options": WHY}],
            "rows": [
                {"s": "فِي [مَسَاجِدَ] كَثِيرَةٍ", "gloss": "in many mosques", "ans": {"why": "dip"},
                 "why": "After {فِي}, with no {ال} and no owner. A diptote takes fatha in jarr."},
                {"s": "فِي [الْمَسَاجِدِ]", "gloss": "in the mosques", "ans": {"why": "al"},
                 "why": "It has {ال}, so it takes kasra."},
                {"s": "ذَهَبْتُ إِلَى [فَاطِمَةَ].", "gloss": "I went to Fatima.", "ans": {"why": "dip"},
                 "why": "After {إِلَى}. A feminine name takes fatha in jarr."},
                {"s": "فِي [مَسَاجِدِ] الْمَدِينَةِ", "gloss": "in the mosques of Madinah", "ans": {"why": "al"},
                 "why": "It has an owner, so it takes kasra."},
                {"s": "دَخَلْنَا [مَسَاجِدَ] كَثِيرَةً.", "gloss": "We entered many mosques.", "ans": {"why": "obj"},
                 "why": "It is the object in naṣb, so it takes fatha. The diptote only has no tanween."},
                {"s": "فِي [بَيْتَ]", "gloss": "in a house", "ans": {"why": "mis"},
                 "why": "{بَيْتٌ} is not a diptote. It must be {فِي بَيْتٍ}."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Take away ال or the owner: tanween or no tanween?",
            "fields": [{"key": "tan", "label": "Alone", "options": [TAN, NOTAN]}],
            "rows": [
                {"s": "الْمَكَاتِبُ", "gloss": "the offices", "ans": {"tan": "notan"}, "why": "A long plural: {مَكَاتِبُ}."},
                {"s": "أَقْلَامُ الطَّالِبِ", "gloss": "the student's pens", "ans": {"tan": "tan"}, "why": "A broken plural, but not on {مَفَاعِلُ}: {أَقْلَامٌ}."},
                {"s": "الْغَضْبَانُ", "gloss": "the angry one", "ans": {"tan": "notan"}, "why": "An adjective on {فَعْلَانُ}: {غَضْبَانُ}."},
                {"s": "الْهَوَاءُ", "gloss": "the air", "ans": {"tan": "tan"}, "why": "The hamza belongs to the word: {هَوَاءٌ}."},
                {"s": "عُلَمَاءُ الْمَدِينَةِ", "gloss": "the scholars of Madinah", "ans": {"tan": "notan"}, "why": "The extra {ـَاءُ}: {عُلَمَاءُ}."},
                {"s": "الدُّكَّانُ", "gloss": "the shop", "ans": {"tan": "tan"}, "why": "It ends in {ـَانُ}, but it is not a name or an adjective: {دُكَّانٌ}."},
            ],
        },
        {
            "title": "Choose the right spelling",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "... طَبِيبٌ", "gloss": "Hamza is a doctor.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("حَمْزَةٌ", "حَمْزَةُ")}, "why": "A man's name ending in {ة}: no tanween."},
                {"s": "... فِي الْمَسْجِدِ", "gloss": "Ali is in the mosque.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("عَلِيٌّ", "عَلِيُّ")}, "why": "An Arabic man's name with no diptote reason."},
                {"s": "هَذِهِ ... كَبِيرَةٌ", "gloss": "This is a big desert.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("صَحْرَاءٌ", "صَحْرَاءُ")}, "why": "The extra {ـَاءُ}: no tanween. The adjective {كَبِيرَةٌ} still has tanween."},
                {"s": "هَذِهِ ...", "gloss": "These are keys.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَفَاتِيحُ", "مَفَاتِيحٌ")}, "why": "A long plural on {مَفَاعِيلُ}."},
                {"s": "... تَاجِرٌ", "gloss": "Uthman is a merchant.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("عُثْمَانٌ", "عُثْمَانُ")}, "why": "A name ending in {ـَانُ}."},
                {"s": "هَذَا قَلَمٌ ...", "gloss": "This is a red pen.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَحْمَرٌ", "أَحْمَرُ")}, "why": "The noun has tanween, but the colour {أَحْمَرُ} never does."},
            ],
        },
        {
            "title": "Which group is this diptote in?",
            "fields": [{"key": "group", "label": "Group", "options": GROUPS}],
            "rows": [
                {"s": "مَرْيَمُ", "ans": {"group": "name"}, "why": "A woman's name."},
                {"s": "جَوْعَانُ", "gloss": "hungry", "ans": {"group": "adj"}, "why": "A describing word on {فَعْلَانُ}."},
                {"s": "وُزَرَاءُ", "gloss": "ministers", "ans": {"group": "alif"}, "why": "A plural, but not on {مَفَاعِلُ}. Its reason is the extra {ـَاءُ}."},
                {"s": "مَدَارِسُ", "gloss": "schools", "ans": {"group": "pl"}, "why": "The plural of {مَدْرَسَةٌ} on {مَفَاعِلُ}."},
                {"s": "أَجْمَلُ", "gloss": "more beautiful", "ans": {"group": "adj"}, "why": "\"More\" on {أَفْعَلُ}."},
                {"s": "رَمَضَانُ", "ans": {"group": "name"}, "why": "The name of a month, ending in {ـَانُ}."},
            ],
        },
        {
            "title": "Which kind of name?",
            "fields": [{"key": "kind", "label": "Kind", "options": NAMES}],
            "rows": [
                {"s": "خَدِيجَةُ", "ans": {"kind": "fem"}, "why": "A woman's name."},
                {"s": "إِسْمَاعِيلُ", "ans": {"kind": "for"}, "why": "A foreign name."},
                {"s": "عُمَرُ", "ans": {"kind": "fual"}, "why": "The shape {فُعَلُ}."},
                {"s": "طَلْحَةُ", "ans": {"kind": "fem"}, "why": "A man's name, but it ends in {ة}."},
                {"s": "عَدْنَانُ", "ans": {"kind": "an"}, "why": "It ends in {ـَانُ}."},
                {"s": "أَسْعَدُ", "ans": {"kind": "verb"}, "why": "It has the shape of a verb, like {أَحْمَدُ}."},
            ],
        },
        {
            "title": "Which one takes tanween without ال?",
            "fields": [{"key": "pick", "label": "Takes tanween", "options": []}],
            "rows": [
                {"s": "the kitchens / the kerchiefs / the boys", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الْمَطَابِخُ", "الْمَنَادِيلُ", "الْأَوْلَادُ")},
                 "why": "{أَوْلَادٌ} is a broken plural, but not on {مَفَاعِلُ}."},
                {"s": "the white / the rabbit / the black", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْأَبْيَضُ", "الْأَرْنَبُ", "الْأَسْوَدُ")},
                 "why": "{أَرْنَبٌ} is a thing, not a colour or a describing word."},
                {"s": "the white (f.) / the sons / the blue (f.)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الْبَيْضَاءُ", "الْأَبْنَاءُ", "الزَّرْقَاءُ")},
                 "why": "In {أَبْنَاءٌ} the hamza belongs to the word. The colours end in the extra {ـَاءُ}."},
                {"s": "the desk / the offices / the schools", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الْمَكْتَبُ", "الْمَكَاتِبُ", "الْمَدَارِسُ")},
                 "why": "The singular {مَكْتَبٌ} takes tanween."},
                {"s": "the lazy / the full / the horse", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الْكَسْلَانُ", "الشَّبْعَانُ", "الْحِصَانُ")},
                 "why": "{حِصَانٌ} is a thing, not an adjective on {فَعْلَانُ}."},
            ],
        },
        {
            "title": "Why does the word in [ ] end like this?",
            "fields": [{"key": "why", "label": "Reason", "options": WHY}],
            "rows": [
                {"s": "ذَهَبَ الْمُدَرِّسُ إِلَى [مَدَارِسَ] كَثِيرَةٍ.", "gloss": "The teacher went to many schools.", "ans": {"why": "dip"},
                 "why": "After {إِلَى}, with no {ال} and no owner: fatha."},
                {"s": "جَلَسْتُ فِي [مَكَاتِبِ] الْمَدْرَسَةِ.", "gloss": "I sat in the school's offices.", "ans": {"why": "al"},
                 "why": "It has an owner, so it takes kasra."},
                {"s": "سَلَّمْتُ عَلَى [يُوسُفَ].", "gloss": "I greeted Yusuf.", "ans": {"why": "dip"},
                 "why": "After {عَلَى}. A foreign name takes fatha in jarr."},
                {"s": "خَرَجْنَا إِلَى [الصَّحْرَاءِ].", "gloss": "We went out to the desert.", "ans": {"why": "al"},
                 "why": "It has {ال}, so it takes kasra."},
                {"s": "أَخَذَ الْوَلَدُ [مَفَاتِيحَ] كَثِيرَةً.", "gloss": "The boy took many keys.", "ans": {"why": "obj"},
                 "why": "It is the object, so it takes fatha."},
                {"s": "الْكِتَابُ عَلَى [مَكْتَبَ].", "gloss": "The book is on a desk.", "ans": {"why": "mis"},
                 "why": "{مَكْتَبٌ} is singular, not a diptote. It must be {عَلَى مَكْتَبٍ}."},
            ],
        },
    ],
}
