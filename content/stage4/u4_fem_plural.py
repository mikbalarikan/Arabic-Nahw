# Stage 4, Unit 4: The sound feminine plural (جَمْعُ الْمُؤَنَّثِ السَّالِمُ)

SING = {"k": "sing", "label": "Singular · مُفْرَدٌ", "color": "grey"}
DUAL = {"k": "dual", "label": "Dual · مُثَنًّى", "color": "teal"}
SMP = {"k": "smp", "label": "Sound masc. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ", "color": "blue"}
SFP = {"k": "sfp", "label": "Sound fem. plural · جَمْعُ مُؤَنَّثٍ سَالِمٌ", "color": "pink"}
BRK = {"k": "brk", "label": "Broken plural · جَمْعُ تَكْسِيرٍ", "color": "purple"}

OKF = {"k": "ok", "label": "A real form of this plural", "color": "pink"}
BADF = {"k": "bad", "label": "Impossible: fatha at the end", "color": "grey"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s4-fem-plural",
    "order": 4,
    "title": "The sound feminine plural",
    "ar": "جَمْعُ الْمُؤَنَّثِ السَّالِمُ",
    "blurb": "Drop the ة and add ـَاتٌ: the plural for women and for many things.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 4 · UNIT 4", "title": "Drop ة, add ـَاتٌ",
         "text": "Many words make their plural with the ending {ـَاتٌ}. The rest of the singular stays whole.",
         "wm": "مُدَرِّسَاتٌ"},

        {"t": "h2", "text": "Drop ة, add ـَاتٌ"},
        {"t": "words", "items": [
            {"ar": "مُدَرِّسَةٌ", "label": "mudarrisatun", "sub": "a woman teacher", "color": "grey"},
            {"ar": "مُدَرِّسَاتٌ", "label": "mudarrisātun", "sub": "women teachers", "color": "pink"},
        ]},
        {"t": "rule", "color": "pink", "title": "How to make it",
         "text": "If the word ends in {ة}, drop the {ة}. Then add {ـَاتٌ}: {سَيَّارَةٌ} → {سَيَّارَاتٌ}. With {ال}: {السَّيَّارَاتُ}."},
        {"t": "tip", "text": "Do not keep the {ة}. {مُدَرِّسَةَاتٌ} is wrong."},
        {"t": "table", "head": ["Singular", "Plural", "Meaning"], "rows": [
            ["مُدَرِّسَةٌ", "مُدَرِّسَاتٌ", "women teachers"],
            ["طَالِبَةٌ", "طَالِبَاتٌ", "women students"],
            ["مُسْلِمَةٌ", "مُسْلِمَاتٌ", "Muslim women"],
            ["سَيَّارَةٌ", "سَيَّارَاتٌ", "cars"],
            ["طَاوِلَةٌ", "طَاوِلَاتٌ", "tables"],
            ["سَاعَةٌ", "سَاعَاتٌ", "watches, hours"],
        ]},

        {"t": "h2", "text": "Who and what takes ـَاتٌ?"},
        {"t": "cols", "items": [
            {"color": "pink", "title": "Women", "ar": "مُمَرِّضَاتٌ",
             "text": "{مُمَرِّضَةٌ}، {مُهَنْدِسَةٌ}، {طَالِبَةٌ}"},
            {"color": "pink", "title": "Many things with ة", "ar": "سَيَّارَاتٌ",
             "text": "{سَيَّارَةٌ}، {طَاوِلَةٌ}، {سَاعَةٌ}"},
            {"color": "pink", "title": "Some masculine things", "ar": "حَمَّامَاتٌ",
             "text": "{حَمَّامٌ}، {اِمْتِحَانٌ}، {حَيَوَانٌ}: no {ة}, just add {ـَاتٌ}."},
        ]},
        {"t": "table", "head": ["Singular", "Plural", "Meaning"], "rows": [
            ["حَمَّامٌ", "حَمَّامَاتٌ", "bathrooms"],
            ["اِمْتِحَانٌ", "اِمْتِحَانَاتٌ", "exams"],
            ["حَيَوَانٌ", "حَيَوَانَاتٌ", "animals"],
        ]},
        {"t": "tip", "text": "Not every word with {ة} takes {ـَاتٌ}: {مَدْرَسَةٌ} → {مَدَارِسُ}، {مَدِينَةٌ} → {مُدُنٌ}. Learn the plural with each word."},
        {"t": "tip", "text": "Careful: {بِنْتٌ} \"a girl\" → {بَنَاتٌ} \"girls\". This plural takes {ـَاتٌ}, but the start of the word changes a little."},

        {"t": "h2", "text": "Two shapes, never a fatha"},
        {"t": "p", "text": "Here is a preview of its shapes. Stages 5 to 7 teach when to use each one."},
        {"t": "table", "head": ["Shape", "Without ال", "With ال", "Used for"], "rows": [
            ["{ـَاتٌ}", "مُسْلِمَاتٌ", "الْمُسْلِمَاتُ", "rafʿ (the dictionary form)"],
            ["{ـَاتٍ}", "مُسْلِمَاتٍ", "الْمُسْلِمَاتِ", "naṣb and jarr (later)"],
        ]},
        {"t": "rule", "color": "red", "title": "This group never takes fatha",
         "text": "Rafʿ has damma. Naṣb and jarr both have kasra. So a word like {الْمُسْلِمَاتَ} with a fatha at the end is always wrong."},

        {"t": "h2", "text": "The trap: ت from the root"},
        {"t": "p", "text": "Some broken plurals also end in {ـَاتٌ}. Their {ت} belongs to the word itself."},
        {"t": "table", "head": ["Plural", "Singular", "Group"], "rows": [
            ["أَصْوَاتٌ", "صَوْتٌ", "broken: voices, sounds"],
            ["أَبْيَاتٌ", "بَيْتٌ", "broken: lines of poetry"],
            ["أَوْقَاتٌ", "وَقْتٌ", "broken: times"],
            ["أَمْوَاتٌ", "مَيِّتٌ", "broken: dead people"],
        ]},
        {"t": "rule", "color": "purple", "title": "The test",
         "text": "Take away {ـَاتٌ}. Is a real singular left (add {ة} back if needed)? {سَاعَاتٌ} → {سَاعَةٌ}: yes, sound. {أَصْوَاتٌ} → {أَصْوَ}: no word. The {ت} is from {صَوْتٌ}, so it is broken."},
        {"t": "tip", "text": "{بَيْتٌ} \"a house\" has the plural {بُيُوتٌ}. When {بَيْتٌ} means a line of poetry, its plural is {أَبْيَاتٌ}."},

        {"t": "h2", "text": "In sentences"},
        {"t": "examples", "items": [
            {"ar": "الْمُدَرِّسَاتُ فِي الْفَصْلِ.", "en": "The women teachers are in the classroom.", "note": "{الْمُدَرِّسَاتُ} is the Topic."},
            {"ar": "هَؤُلَاءِ طَالِبَاتٌ.", "en": "These are women students.", "note": "{هَؤُلَاءِ} for a group of people."},
            {"ar": "الطَّالِبَاتُ مُجْتَهِدَاتٌ.", "en": "The women students are hard-working.", "note": "The Information copies the plural: {مُجْتَهِدَاتٌ}."},
            {"ar": "هَذِهِ سَيَّارَاتٌ جَدِيدَةٌ.", "en": "These are new cars.", "note": "Plural things use {هَذِهِ} and a feminine singular adjective."},
            {"ar": "الْحَمَّامَاتُ نَظِيفَةٌ.", "en": "The bathrooms are clean.", "note": "{حَمَّامٌ} is masculine, but bathrooms are things, so the Information is {نَظِيفَةٌ}."},
        ]},

        {"t": "summary", "title": "In short", "items": [
            "Sound feminine plural: drop {ة} and add {ـَاتٌ}: {مُدَرِّسَةٌ} → {مُدَرِّسَاتٌ}.",
            "It is for women, many things with {ة}, and some masculine things: {حَمَّامٌ} → {حَمَّامَاتٌ}.",
            "Two shapes: {ـَاتٌ} and {ـَاتٍ}. Never a fatha at the end.",
            "Test: take away {ـَاتٌ}. No real singular left? Then it is broken: {أَصْوَاتٌ}، {أَوْقَاتٌ}.",
            "Some words with {ة} have a broken plural: {مَدْرَسَةٌ} → {مَدَارِسُ}. Learn each plural.",
        ]},
    ],

    "practice": [
        {
            "title": "Make the plural",
            "fields": [{"key": "pick", "label": "Plural", "options": []}],
            "rows": [
                {"s": "مُدَرِّسَةٌ", "gloss": "a woman teacher", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُدَرِّسَةَاتٌ", "مُدَرِّسَاتٌ", "مُدَرِّسُونَ")},
                 "why": "Drop {ة}, add {ـَاتٌ}. {مُدَرِّسُونَ} is for men."},
                {"s": "طَالِبَةٌ", "gloss": "a woman student", "ans": {"pick": "a"},
                 "opts": {"pick": pick("طَالِبَاتٌ", "طَالِبَتَاتٌ", "طَالِبَتَانِ")},
                 "why": "Drop {ة}, add {ـَاتٌ}. {طَالِبَتَانِ} means two students."},
                {"s": "سَيَّارَةٌ", "gloss": "a car", "ans": {"pick": "c"},
                 "opts": {"pick": pick("سَيَّارُونَ", "سَيَّارَةُونَ", "سَيَّارَاتٌ")},
                 "why": "A thing never takes {ـُونَ}: {سَيَّارَاتٌ}."},
                {"s": "سَاعَةٌ", "gloss": "a watch, an hour", "ans": {"pick": "a"},
                 "opts": {"pick": pick("سَاعَاتٌ", "سَاعَاتَ", "سَاعَتَاتٌ")},
                 "why": "Drop {ة}, add {ـَاتٌ}: {سَاعَاتٌ}."},
                {"s": "مُسْلِمَةٌ", "gloss": "a Muslim woman", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُسْلِمُونَ", "مُسْلِمَاتٌ", "مُسْلِمَتَانِ")},
                 "why": "Women: {مُسْلِمَاتٌ}."},
                {"s": "حَمَّامٌ", "gloss": "a bathroom", "ans": {"pick": "c"},
                 "opts": {"pick": pick("حَمَّامُونَ", "حَمَّامَانِ", "حَمَّامَاتٌ")},
                 "why": "No {ة} to drop. Just add {ـَاتٌ}: {حَمَّامَاتٌ}."},
            ],
        },
        {
            "title": "Sound feminine plural or broken?",
            "fields": [{"key": "grp", "label": "Group", "options": [SFP, BRK]}],
            "rows": [
                {"s": "سَاعَاتٌ", "ans": {"grp": "sfp"}, "why": "Take away {ـَاتٌ}, add {ة}: {سَاعَةٌ}. A real singular."},
                {"s": "أَصْوَاتٌ", "ans": {"grp": "brk"}, "why": "Without {ـَاتٌ} we get {أَصْوَ}: no word. The singular is {صَوْتٌ}."},
                {"s": "طَالِبَاتٌ", "ans": {"grp": "sfp"}, "why": "{طَالِبَةٌ} → {طَالِبَاتٌ}."},
                {"s": "أَوْقَاتٌ", "ans": {"grp": "brk"}, "why": "The {ت} is from {وَقْتٌ}. The shape changed: broken."},
                {"s": "طَاوِلَاتٌ", "ans": {"grp": "sfp"}, "why": "{طَاوِلَةٌ} → {طَاوِلَاتٌ}."},
                {"s": "أَبْيَاتٌ", "ans": {"grp": "brk"}, "why": "The {ت} is from {بَيْتٌ} \"a line of poetry\". Broken."},
            ],
        },
        {
            "title": "Find the singular",
            "fields": [{"key": "pick", "label": "Singular", "options": []}],
            "rows": [
                {"s": "مُهَنْدِسَاتٌ", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُهَنْدِسٌ", "مُهَنْدِسَةٌ", "هَنْدَسَةٌ")},
                 "why": "Women engineers. Take away {ـَاتٌ} and add {ة} back: {مُهَنْدِسَةٌ}."},
                {"s": "أَصْوَاتٌ", "ans": {"pick": "a"},
                 "opts": {"pick": pick("صَوْتٌ", "أَصْوَةٌ", "صَوْتَةٌ")},
                 "why": "A broken plural. Its singular is {صَوْتٌ}."},
                {"s": "اِمْتِحَانَاتٌ", "ans": {"pick": "c"},
                 "opts": {"pick": pick("اِمْتِحَانَةٌ", "مُمْتَحِنٌ", "اِمْتِحَانٌ")},
                 "why": "A masculine thing with no {ة}. Take away {ـَاتٌ}: {اِمْتِحَانٌ}."},
                {"s": "مُمَرِّضَاتٌ", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُمَرِّضَةٌ", "مُمَرِّضٌ", "مُمَرِّضَتَانِ")},
                 "why": "Women nurses: {مُمَرِّضَةٌ}."},
                {"s": "أَوْقَاتٌ", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَوْقَةٌ", "وَقْتٌ", "وَقْتَةٌ")},
                 "why": "A broken plural. Its singular is {وَقْتٌ}."},
            ],
        },
        {
            "title": "Which group?",
            "fields": [{"key": "grp", "label": "Group", "options": [SING, SMP, SFP, BRK]}],
            "rows": [
                {"s": "مُدَرِّسَاتٌ", "ans": {"grp": "sfp"}, "why": "{مُدَرِّسَةٌ} → {مُدَرِّسَاتٌ}."},
                {"s": "مُدَرِّسُونَ", "ans": {"grp": "smp"}, "why": "{مُدَرِّسٌ} + {ـُونَ}: men teachers."},
                {"s": "سَاعَةٌ", "ans": {"grp": "sing"}, "why": "One watch."},
                {"s": "أَوْقَاتٌ", "ans": {"grp": "brk"}, "why": "It ends in {ـَاتٌ}, but the {ت} is from {وَقْتٌ}."},
                {"s": "حَمَّامَاتٌ", "ans": {"grp": "sfp"}, "why": "{حَمَّامٌ} + {ـَاتٌ}."},
                {"s": "طُلَّابٌ", "ans": {"grp": "brk"}, "why": "The shape of {طَالِبٌ} changed inside."},
            ],
        },
        {
            "title": "A real form or impossible?",
            "fields": [{"key": "form", "label": "Form", "options": [OKF, BADF]}],
            "rows": [
                {"s": "سَيَّارَاتٌ", "ans": {"form": "ok"}, "why": "The dictionary shape, with damma tanween."},
                {"s": "سَيَّارَاتٍ", "ans": {"form": "ok"}, "why": "The other shape, with kasra tanween."},
                {"s": "السَّيَّارَاتَ", "ans": {"form": "bad"}, "why": "This group never takes fatha. Naṣb uses kasra: {السَّيَّارَاتِ}."},
                {"s": "السَّيَّارَاتِ", "ans": {"form": "ok"}, "why": "Kasra: a real shape of this plural."},
                {"s": "طَالِبَاتًا", "ans": {"form": "bad"}, "why": "Fatha tanween is impossible here. The shapes are {طَالِبَاتٌ} and {طَالِبَاتٍ}."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "الْمُدَرِّسَاتُ فِي الْفَصْلِ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The women teachers are in the classroom.", "The woman teacher is in the classroom.", "The schools are in the classroom.")},
                 "why": "{الْمُدَرِّسَاتُ} is the plural of {الْمُدَرِّسَةُ}."},
                {"s": "هَذِهِ سَاعَاتٌ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("This is a watch.", "These watches", "These are watches.")},
                 "why": "Plural things use {هَذِهِ}. No {ال}, so it is a sentence."},
                {"s": "الطَّالِبَاتُ مُجْتَهِدَاتٌ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("The hard-working women students", "The women students are hard-working.", "The woman student is hard-working.")},
                 "why": "Topic {الطَّالِبَاتُ} + Information {مُجْتَهِدَاتٌ}."},
                {"s": "أَصْوَاتُ الطُّلَّابِ جَمِيلَةٌ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The students' voices are beautiful.", "The student's voice is beautiful.", "The students' times are beautiful.")},
                 "why": "{أَصْوَاتُ} is the plural of {صَوْتٌ}. Times would be {أَوْقَاتُ}."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Make the plural",
            "fields": [{"key": "pick", "label": "Plural", "options": []}],
            "rows": [
                {"s": "مُعَلِّمَةٌ", "gloss": "a woman teacher", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُعَلِّمُونَ", "مُعَلِّمَةَاتٌ", "مُعَلِّمَاتٌ")},
                 "why": "Drop {ة}, add {ـَاتٌ}."},
                {"s": "طَائِرَةٌ", "gloss": "a plane", "ans": {"pick": "a"},
                 "opts": {"pick": pick("طَائِرَاتٌ", "طَائِرُونَ", "طَائِرَتَانِ")},
                 "why": "A thing with {ة}: {طَائِرَاتٌ}. {طَائِرَتَانِ} means two planes."},
                {"s": "مَطَارٌ", "gloss": "an airport", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَطَارُونَ", "مَطَارَاتٌ", "مَطَارَةٌ")},
                 "why": "A masculine thing that takes {ـَاتٌ}: {مَطَارَاتٌ}."},
                {"s": "حَيَوَانٌ", "gloss": "an animal", "ans": {"pick": "c"},
                 "opts": {"pick": pick("حَيَوَانَانِ", "حَيَوَانُونَ", "حَيَوَانَاتٌ")},
                 "why": "No {ة}. Just add {ـَاتٌ}: {حَيَوَانَاتٌ}."},
                {"s": "جَامِعَةٌ", "gloss": "a university", "ans": {"pick": "a"},
                 "opts": {"pick": pick("جَامِعَاتٌ", "جَامِعَاتًا", "جَامِعَتَاتٌ")},
                 "why": "Drop {ة}, add {ـَاتٌ}. This group never has fatha tanween."},
                {"s": "ثَلَّاجَةٌ", "gloss": "a fridge", "ans": {"pick": "b"},
                 "opts": {"pick": pick("ثَلَّاجُونَ", "ثَلَّاجَاتٌ", "ثَلَّاجَةَاتٌ")},
                 "why": "Drop {ة}, add {ـَاتٌ}: {ثَلَّاجَاتٌ}."},
            ],
        },
        {
            "title": "Sound feminine plural or broken?",
            "fields": [{"key": "grp", "label": "Group", "options": [SFP, BRK]}],
            "rows": [
                {"s": "أَمْوَاتٌ", "ans": {"grp": "brk"}, "why": "Without {ـَاتٌ} we get {أَمْوَ}: no word. The singular is {مَيِّتٌ}."},
                {"s": "دَرَّاجَاتٌ", "gloss": "bicycles", "ans": {"grp": "sfp"}, "why": "{دَرَّاجَةٌ} → {دَرَّاجَاتٌ}."},
                {"s": "بُيُوتٌ", "ans": {"grp": "brk"}, "why": "It ends in {ت}, but the {ت} is from {بَيْتٌ}. The shape changed."},
                {"s": "نَظَّارَاتٌ", "gloss": "pairs of glasses", "ans": {"grp": "sfp"}, "why": "{نَظَّارَةٌ} → {نَظَّارَاتٌ}."},
                {"s": "مُوَظَّفَاتٌ", "ans": {"grp": "sfp"}, "why": "{مُوَظَّفَةٌ} \"a woman employee\" → {مُوَظَّفَاتٌ}."},
            ],
        },
        {
            "title": "Find the singular",
            "fields": [{"key": "pick", "label": "Singular", "options": []}],
            "rows": [
                {"s": "مَكْتَبَاتٌ", "gloss": "libraries", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَكْتَبٌ", "مَكْتَبَةٌ", "كِتَابٌ")},
                 "why": "Take away {ـَاتٌ}, add {ة}: {مَكْتَبَةٌ}. {مَكْتَبٌ} \"a desk\" has a broken plural."},
                {"s": "شَرِكَاتٌ", "gloss": "companies", "ans": {"pick": "a"},
                 "opts": {"pick": pick("شَرِكَةٌ", "شَرِيكٌ", "شَرِكٌ")},
                 "why": "Take away {ـَاتٌ}, add {ة}: {شَرِكَةٌ}."},
                {"s": "اِجْتِمَاعَاتٌ", "gloss": "meetings", "ans": {"pick": "c"},
                 "opts": {"pick": pick("اِجْتِمَاعَةٌ", "جَامِعَةٌ", "اِجْتِمَاعٌ")},
                 "why": "A masculine thing with no {ة}: {اِجْتِمَاعٌ}."},
                {"s": "حَافِلَاتٌ", "gloss": "buses", "ans": {"pick": "a"},
                 "opts": {"pick": pick("حَافِلَةٌ", "حَافِلٌ", "حَافِلَتَانِ")},
                 "why": "Take away {ـَاتٌ}, add {ة}: {حَافِلَةٌ}."},
                {"s": "أَمْوَاتٌ", "gloss": "dead people", "ans": {"pick": "b"},
                 "opts": {"pick": pick("أَمْوَةٌ", "مَيِّتٌ", "مَوْتَةٌ")},
                 "why": "A broken plural. Its singular is {مَيِّتٌ}."},
            ],
        },
        {
            "title": "Which group?",
            "fields": [{"key": "grp", "label": "Group", "options": [SING, DUAL, SMP, SFP, BRK]}],
            "rows": [
                {"s": "مُعَلِّمَاتٌ", "ans": {"grp": "sfp"}, "why": "{مُعَلِّمَةٌ} → {مُعَلِّمَاتٌ}."},
                {"s": "مُعَلِّمُونَ", "ans": {"grp": "smp"}, "why": "{مُعَلِّمٌ} + {ـُونَ}: men teachers."},
                {"s": "مُعَلِّمَتَانِ", "ans": {"grp": "dual"}, "why": "{ـَتَانِ} means two women teachers."},
                {"s": "أَصْوَاتٌ", "ans": {"grp": "brk"}, "why": "The {ت} is from {صَوْتٌ}: broken."},
                {"s": "مَطَارَاتٌ", "ans": {"grp": "sfp"}, "why": "{مَطَارٌ} + {ـَاتٌ}."},
                {"s": "طَاوِلَةٌ", "ans": {"grp": "sing"}, "why": "One table."},
            ],
        },
        {
            "title": "A real form or impossible?",
            "fields": [{"key": "form", "label": "Form", "options": [OKF, BADF]}],
            "rows": [
                {"s": "الْجَامِعَاتِ", "ans": {"form": "ok"}, "why": "Kasra: a real shape of this plural."},
                {"s": "حَيَوَانَاتًا", "ans": {"form": "bad"}, "why": "Never fatha tanween. Naṣb uses kasra: {حَيَوَانَاتٍ}."},
                {"s": "الطَّائِرَاتُ", "ans": {"form": "ok"}, "why": "The dictionary shape with {ال}: damma."},
                {"s": "مُسْلِمَاتٍ", "ans": {"form": "ok"}, "why": "Kasra tanween: a real shape."},
                {"s": "الْمُعَلِّمَاتَ", "ans": {"form": "bad"}, "why": "Never a fatha at the end: {الْمُعَلِّمَاتِ}."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "هَؤُلَاءِ مُمَرِّضَاتٌ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("These nurses", "These are women nurses.", "This is a woman nurse.")},
                 "why": "{هَؤُلَاءِ} for people. No {ال}, so it is a sentence."},
                {"s": "الْحَيَوَانَاتُ فِي الشَّارِعِ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The animals are in the street.", "The animal is in the street.", "The cars are in the street.")},
                 "why": "{الْحَيَوَانَاتُ} is the plural of {حَيَوَانٌ}."},
                {"s": "تِلْكَ سَيَّارَاتٌ جَدِيدَةٌ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("That car is new.", "Those cars are new.", "Those are new cars.")},
                 "why": "Plural things use {تِلْكَ} for far. {سَيَّارَاتٌ} has no {ال}: a sentence, and {جَدِيدَةٌ} is its adjective."},
                {"s": "خَرَجَتِ الطَّالِبَاتُ مِنَ الْجَامِعَةِ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("The woman student went out of the university.", "The women students went out of the university.", "The women students went to the university.")},
                 "why": "{الطَّالِبَاتُ} is plural. {مِنَ} means \"out of, from\"."},
            ],
        },
    ],
}
