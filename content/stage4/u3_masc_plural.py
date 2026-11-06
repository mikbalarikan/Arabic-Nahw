# Stage 4, Unit 3: The sound masculine plural (جَمْعُ الْمُذَكَّرِ السَّالِمُ)

SING = {"k": "sing", "label": "Singular · مُفْرَدٌ", "color": "grey"}
DUAL = {"k": "dual", "label": "Dual · مُثَنًّى", "color": "teal"}
SMP = {"k": "smp", "label": "Sound masc. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ", "color": "blue"}
BRK = {"k": "brk", "label": "Broken plural · جَمْعُ تَكْسِيرٍ", "color": "purple"}

LOOK = {"k": "look", "label": "Look-alike: one word", "color": "grey"}

MALE = {"k": "male", "label": "Male person", "color": "blue"}
FEMALE = {"k": "female", "label": "Female person", "color": "pink"}
THING = {"k": "thing", "label": "Thing", "color": "navy"}
YES = {"k": "yes", "label": "Yes, ـُونَ"}
NO = {"k": "no", "label": "No"}

SH1 = {"k": "un", "label": "Shape ـُونَ", "color": "blue"}
SH2 = {"k": "in", "label": "Shape ـِينَ", "color": "blue"}
NOTG = {"k": "not", "label": "Not this group", "color": "grey"}


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s4-masc-plural",
    "order": 3,
    "title": "The sound masculine plural",
    "ar": "جَمْعُ الْمُذَكَّرِ السَّالِمُ",
    "blurb": "Keep the word whole and add ـُونَ: the plural for male persons.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 4 · UNIT 3", "title": "Add ـُونَ, keep the word whole",
         "text": "Many words for men make their plural with one ending: {ـُونَ}. The singular inside stays safe and sound.",
         "wm": "مُسْلِمُونَ"},

        {"t": "h2", "text": "Sound: the singular stays whole"},
        {"t": "p", "text": "{سَالِمٌ} means \"safe, sound\". In this plural no letter of the singular moves or drops. We only add an ending."},
        {"t": "words", "items": [
            {"ar": "مُسْلِمٌ", "label": "muslimun", "sub": "a Muslim", "color": "grey"},
            {"ar": "مُسْلِمُونَ", "label": "muslimūna", "sub": "Muslims", "color": "blue"},
        ]},
        {"t": "table", "head": ["Singular", "Plural", "Meaning"], "rows": [
            ["مُسْلِمٌ", "مُسْلِمُونَ", "Muslims"],
            ["مُدَرِّسٌ", "مُدَرِّسُونَ", "teachers"],
            ["مُهَنْدِسٌ", "مُهَنْدِسُونَ", "engineers"],
            ["فَلَّاحٌ", "فَلَّاحُونَ", "farmers"],
            ["مُجْتَهِدٌ", "مُجْتَهِدُونَ", "hard-working (men)"],
            ["صَالِحٌ", "صَالِحُونَ", "good, righteous (men)"],
        ]},
        {"t": "rule", "color": "blue", "title": "How to make it",
         "text": "Take the singular. Drop the tanween. Add {ـُونَ}: {مُدَرِّسٌ} → {مُدَرِّسُونَ}. With {ال} it is the same: {الْمُدَرِّسُونَ}."},
        {"t": "tip", "text": "The plural never has tanween. Its {ن} always has a fatha: {مُسْلِمُونَ}, never {مُسْلِمُونٌ}."},

        {"t": "h2", "text": "Who can take ـُونَ?"},
        {"t": "p", "text": "The simple rule: male persons. These are words for men, like jobs ({مُدَرِّسٌ}، {مُهَنْدِسٌ}) and words that describe men ({مُجْتَهِدٌ}، {صَالِحٌ})."},
        {"t": "cols", "items": [
            {"color": "blue", "title": "Male persons: yes", "ar": "مُدَرِّسُونَ",
             "text": "{مُدَرِّسٌ} → {مُدَرِّسُونَ}"},
            {"color": "pink", "title": "Female persons: no", "ar": "مُدَرِّسَاتٌ",
             "text": "{مُدَرِّسَةٌ} takes {ـَاتٌ}. That is the next unit."},
            {"color": "navy", "title": "Things: no", "ar": "كُتُبٌ",
             "text": "{كِتَابٌ} → {كُتُبٌ}. There is no {كِتَابُونَ}."},
        ]},
        {"t": "tip", "text": "A group of men and women together also uses {ـُونَ}: {الْمُسْلِمُونَ} can mean Muslim men and women."},

        {"t": "h2", "text": "Some men's words choose a broken plural"},
        {"t": "p", "text": "Not every word for a man takes {ـُونَ}. Some have only a broken plural. Arabic chooses, so learn the plural with each word."},
        {"t": "table", "head": ["Singular", "Plural", "Group"], "rows": [
            ["رَجُلٌ", "رِجَالٌ", "broken"],
            ["طَالِبٌ", "طُلَّابٌ", "broken"],
            ["وَلَدٌ", "أَوْلَادٌ", "broken"],
            ["طَبِيبٌ", "أَطِبَّاءُ", "broken"],
            ["مُهَنْدِسٌ", "مُهَنْدِسُونَ", "sound masculine"],
        ]},
        {"t": "tip", "text": "Say {رِجَالٌ}, never {رَجُلُونَ}. When you learn a new word, learn its plural too."},

        {"t": "h2", "text": "Two shapes: ـُونَ and ـِينَ"},
        {"t": "p", "text": "This group shows its iʿrāb with letters. So it has two shapes. Here is a preview. Stages 5 to 7 teach when to use each one."},
        {"t": "table", "head": ["Shape", "Without ال", "With ال", "Used for"], "rows": [
            ["{ـُونَ}", "مُسْلِمُونَ", "الْمُسْلِمُونَ", "rafʿ (the dictionary form)"],
            ["{ـِينَ}", "مُسْلِمِينَ", "الْمُسْلِمِينَ", "naṣb and jarr (later)"],
        ]},
        {"t": "rule", "color": "red", "title": "Letters, not vowels",
         "text": "The {و} or the {ي} carries the iʿrāb. These are branch signs. The {ن} at the end keeps its fatha in both shapes."},
        {"t": "p", "text": "Preview: when no owner comes after this plural, the {ن} stays. When it is the first word of an iḍāfa, the {ن} drops: {مُدَرِّسُو الْمَدْرَسَةِ} \"the school's teachers\". You practise this later."},

        {"t": "h2", "text": "Look-alikes: one word ending in ـُونٌ or ـِينٌ"},
        {"t": "p", "text": "Some singular words end in {ـُونٌ} or {ـِينٌ}. Their {ن} is part of the word."},
        {"t": "table", "head": ["Word", "Meaning", "Its plural"], "rows": [
            ["زَيْتُونٌ", "olives (one word for the fruit)", "one olive: {زَيْتُونَةٌ}"],
            ["قَانُونٌ", "a law", "قَوَانِينُ"],
            ["مِسْكِينٌ", "a poor man", "مَسَاكِينُ"],
            ["سِكِّينٌ", "a knife", "سَكَاكِينُ"],
        ]},
        {"t": "rule", "color": "grey", "title": "Look at the last mark",
         "text": "A look-alike can take tanween: {قَانُونٌ}، {مِسْكِينٌ}. With {ال} its {ن} takes the vowel: {الْقَانُونُ}. The plural's {ن} always has a plain fatha: {مُسْلِمُونَ}، {الْمُسْلِمِينَ}."},

        {"t": "h2", "text": "In sentences"},
        {"t": "examples", "items": [
            {"ar": "الْمُدَرِّسُونَ فِي الْفَصْلِ.", "en": "The teachers are in the classroom.", "note": "{الْمُدَرِّسُونَ} is the Topic."},
            {"ar": "هَؤُلَاءِ مُهَنْدِسُونَ.", "en": "These are engineers.", "note": "{هَؤُلَاءِ} for a group of people."},
            {"ar": "الْفَلَّاحُونَ مُجْتَهِدُونَ.", "en": "The farmers are hard-working.", "note": "The Information copies the plural: {مُجْتَهِدُونَ}."},
            {"ar": "خَرَجَ الْمُسْلِمُونَ مِنَ الْمَسْجِدِ.", "en": "The Muslims went out of the mosque.", "note": "{الْمُسْلِمُونَ} is the doer. The verb before it stays {خَرَجَ}."},
        ]},

        {"t": "summary", "title": "In short", "items": [
            "Sound masculine plural: keep the singular whole and add {ـُونَ}: {مُدَرِّسٌ} → {مُدَرِّسُونَ}.",
            "It is for male persons. Things and women never take it.",
            "Some men's words have a broken plural only: {رَجُلٌ} → {رِجَالٌ}. Learn each plural.",
            "Two shapes: {ـُونَ} and {ـِينَ}. No tanween, and the {ن} has a fatha.",
            "{مِسْكِينٌ}، {قَانُونٌ}، {زَيْتُونٌ} only look like plurals.",
        ]},
    ],

    "practice": [
        {
            "title": "Make the plural",
            "fields": [{"key": "pick", "label": "Plural", "options": []}],
            "rows": [
                {"s": "مُسْلِمٌ", "gloss": "a Muslim", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُسْلِمُونَ", "مُسْلِمُونٌ", "مُسْلِمَانِ")},
                 "why": "Add {ـُونَ}. The plural has no tanween. {مُسْلِمَانِ} means two Muslims."},
                {"s": "مُدَرِّسٌ", "gloss": "a teacher", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُدَرِّسَاتٌ", "مُدَرِّسُنَ", "مُدَرِّسُونَ")},
                 "why": "Male teachers: {مُدَرِّسُونَ}. {مُدَرِّسَاتٌ} is for women teachers."},
                {"s": "مُهَنْدِسٌ", "gloss": "an engineer", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُهَنْدِسُونٌ", "مُهَنْدِسُونَ", "مُهَنْدِسَانِ")},
                 "why": "Keep the word whole and add {ـُونَ}, with a fatha on the {ن}."},
                {"s": "فَلَّاحٌ", "gloss": "a farmer", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فَلَّاحُونَ", "فَلَّاحَاتٌ", "فَلَّاحُونِ")},
                 "why": "{فَلَّاحُونَ}: the {ن} has a fatha."},
                {"s": "مُجْتَهِدٌ", "gloss": "hard-working (a man)", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُجْتَهِدَانِ", "مُجْتَهِدَاتٌ", "مُجْتَهِدُونَ")},
                 "why": "It describes men, so it takes {ـُونَ}."},
            ],
        },
        {
            "title": "Can this noun take ـُونَ?",
            "fields": [
                {"key": "who", "label": "It is a", "options": [MALE, FEMALE, THING]},
                {"key": "takes", "label": "Takes ـُونَ?", "options": [YES, NO]},
            ],
            "rows": [
                {"s": "مُدَرِّسٌ", "gloss": "a teacher", "ans": {"who": "male", "takes": "yes"},
                 "why": "A male person: {مُدَرِّسُونَ}."},
                {"s": "كِتَابٌ", "gloss": "a book", "ans": {"who": "thing", "takes": "no"},
                 "why": "A thing. Its plural is {كُتُبٌ}."},
                {"s": "مُدَرِّسَةٌ", "gloss": "a woman teacher", "ans": {"who": "female", "takes": "no"},
                 "why": "A female person. Her plural is {مُدَرِّسَاتٌ}."},
                {"s": "مُهَنْدِسٌ", "gloss": "an engineer", "ans": {"who": "male", "takes": "yes"},
                 "why": "A male person: {مُهَنْدِسُونَ}."},
                {"s": "بَابٌ", "gloss": "a door", "ans": {"who": "thing", "takes": "no"},
                 "why": "A thing. Its plural is {أَبْوَابٌ}."},
                {"s": "فَلَّاحٌ", "gloss": "a farmer", "ans": {"who": "male", "takes": "yes"},
                 "why": "A male person: {فَلَّاحُونَ}."},
            ],
        },
        {
            "title": "Real plural or look-alike?",
            "fields": [{"key": "grp", "label": "Group", "options": [SMP, LOOK]}],
            "rows": [
                {"s": "مُسْلِمُونَ", "ans": {"grp": "smp"}, "why": "{مُسْلِمٌ} + {ـُونَ}. Fatha on the {ن}, no tanween."},
                {"s": "زَيْتُونٌ", "gloss": "olives", "ans": {"grp": "look"}, "why": "It has tanween: {زَيْتُونٌ}. The {ن} is part of the word."},
                {"s": "مُدَرِّسِينَ", "ans": {"grp": "smp"}, "why": "The second shape of {مُدَرِّسُونَ}."},
                {"s": "مِسْكِينٌ", "gloss": "a poor man", "ans": {"grp": "look"}, "why": "One poor man. It has tanween. Its plural is {مَسَاكِينُ}."},
                {"s": "مُهَنْدِسُونَ", "ans": {"grp": "smp"}, "why": "{مُهَنْدِسٌ} + {ـُونَ}."},
                {"s": "سِكِّينٌ", "gloss": "a knife", "ans": {"grp": "look"}, "why": "One knife, and a thing. Things never take this plural."},
            ],
        },
        {
            "title": "Find the singular",
            "fields": [{"key": "pick", "label": "Singular", "options": []}],
            "rows": [
                {"s": "مُدَرِّسُونَ", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَدْرَسَةٌ", "مُدَرِّسٌ", "مُدَرِّسَةٌ")},
                 "why": "Take away {ـُونَ}: {مُدَرِّسٌ}. {مَدْرَسَةٌ} is a school."},
                {"s": "فَلَّاحُونَ", "ans": {"pick": "a"},
                 "opts": {"pick": pick("فَلَّاحٌ", "فَلَّاحَةٌ", "فَلَّاحَانِ")},
                 "why": "Take away {ـُونَ}: {فَلَّاحٌ}."},
                {"s": "مُسْلِمِينَ", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مُسْلِمِي", "مُسْلِمَةٌ", "مُسْلِمٌ")},
                 "why": "Take away {ـِينَ}: {مُسْلِمٌ}."},
                {"s": "مُجْتَهِدُونَ", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُجْتَهِدٌ", "مُجْتَهِدَةٌ", "مُجْتَهِدُونٌ")},
                 "why": "Take away {ـُونَ}: {مُجْتَهِدٌ}."},
                {"s": "صَالِحُونَ", "ans": {"pick": "b"},
                 "opts": {"pick": pick("صَالِحَةٌ", "صَالِحٌ", "صَالِحَانِ")},
                 "why": "Take away {ـُونَ}: {صَالِحٌ} \"good, righteous\"."},
            ],
        },
        {
            "title": "Which shape is it?",
            "fields": [{"key": "shape", "label": "Shape", "options": [SH1, SH2, NOTG]}],
            "rows": [
                {"s": "مُهَنْدِسُونَ", "ans": {"shape": "un"}, "why": "It ends in {ـُونَ}."},
                {"s": "مُهَنْدِسِينَ", "ans": {"shape": "in"}, "why": "It ends in {ـِينَ}: the other shape of the same plural."},
                {"s": "الْفَلَّاحِينَ", "ans": {"shape": "in"}, "why": "{ال} does not change the ending {ـِينَ}."},
                {"s": "الْمُدَرِّسُونَ", "ans": {"shape": "un"}, "why": "{ال} + {مُدَرِّسُونَ}."},
                {"s": "طُلَّابٌ", "ans": {"shape": "not"}, "why": "A broken plural of {طَالِبٌ}. It has tanween and no {ـُونَ}."},
                {"s": "مِسْكِينٌ", "ans": {"shape": "not"}, "why": "A look-alike: one poor man, with tanween."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "الْمُدَرِّسُونَ فِي الْفَصْلِ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("The teacher is in the classroom.", "The teachers are in the classroom.", "The school is in the classroom.")},
                 "why": "{الْمُدَرِّسُونَ} is plural: \"the teachers\"."},
                {"s": "هَؤُلَاءِ مُسْلِمُونَ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("These are Muslims.", "This is a Muslim.", "These Muslims")},
                 "why": "{مُسْلِمُونَ} has no {ال}, so this is a full sentence."},
                {"s": "الْمُهَنْدِسُونَ مُجْتَهِدُونَ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("The engineer is hard-working.", "The hard-working engineers", "The engineers are hard-working.")},
                 "why": "Topic {الْمُهَنْدِسُونَ} + Information {مُجْتَهِدُونَ}."},
                {"s": "خَرَجَ الْفَلَّاحُونَ مِنَ الْبَيْتِ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The farmers went out of the house.", "The farmer went out of the house.", "The farmers went into the house.")},
                 "why": "{الْفَلَّاحُونَ} is plural. {خَرَجَ} \"went out\" stays singular before its doer."},
            ],
        },
    ],

    "homework": [
        {
            "title": "Make the plural",
            "fields": [{"key": "pick", "label": "Plural", "options": []}],
            "rows": [
                {"s": "مُعَلِّمٌ", "gloss": "a teacher", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُعَلِّمُونٌ", "مُعَلِّمُونَ", "مُعَلِّمَاتٌ")},
                 "why": "Add {ـُونَ}, no tanween: {مُعَلِّمُونَ}."},
                {"s": "مُمَرِّضٌ", "gloss": "a male nurse", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُمَرِّضُونَ", "مُمَرِّضَانِ", "مُمَرِّضُونِ")},
                 "why": "{مُمَرِّضُونَ}: fatha on the {ن}. {مُمَرِّضَانِ} means two nurses."},
                {"s": "نَجَّارٌ", "gloss": "a carpenter", "ans": {"pick": "c"},
                 "opts": {"pick": pick("نَجَّارَاتٌ", "نُجُورٌ", "نَجَّارُونَ")},
                 "why": "A male person: keep {نَجَّارٌ} whole and add {ـُونَ}."},
                {"s": "لَاعِبٌ", "gloss": "a player", "ans": {"pick": "b"},
                 "opts": {"pick": pick("لَاعِبُنَ", "لَاعِبُونَ", "لَاعِبَانِ")},
                 "why": "The ending is {ـُونَ} with a long {و}: {لَاعِبُونَ}."},
                {"s": "مُوَظَّفٌ", "gloss": "an employee", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مُوَظَّفُونَ", "مُوَظَّفُونٌ", "مُوَظَّفَاتٌ")},
                 "why": "Male employees: {مُوَظَّفُونَ}, with no tanween."},
            ],
        },
        {
            "title": "Can this noun take ـُونَ?",
            "fields": [
                {"key": "who", "label": "It is a", "options": [MALE, FEMALE, THING]},
                {"key": "takes", "label": "Takes ـُونَ?", "options": [YES, NO]},
            ],
            "rows": [
                {"s": "رَجُلٌ", "gloss": "a man", "ans": {"who": "male", "takes": "no"},
                 "why": "A male person, but Arabic uses the broken plural {رِجَالٌ}."},
                {"s": "مُؤْمِنٌ", "gloss": "a believer", "ans": {"who": "male", "takes": "yes"},
                 "why": "A male person: {مُؤْمِنُونَ}."},
                {"s": "سَيَّارَةٌ", "gloss": "a car", "ans": {"who": "thing", "takes": "no"},
                 "why": "A thing. Its plural is {سَيَّارَاتٌ}."},
                {"s": "مُسْلِمَةٌ", "gloss": "a Muslim woman", "ans": {"who": "female", "takes": "no"},
                 "why": "A female person: {مُسْلِمَاتٌ}."},
                {"s": "وَلَدٌ", "gloss": "a boy", "ans": {"who": "male", "takes": "no"},
                 "why": "A male person, but his plural is broken: {أَوْلَادٌ}."},
                {"s": "مُسَافِرٌ", "gloss": "a traveller", "ans": {"who": "male", "takes": "yes"},
                 "why": "A male person: {مُسَافِرُونَ}."},
            ],
        },
        {
            "title": "Real plural or look-alike?",
            "fields": [{"key": "grp", "label": "Group", "options": [SMP, LOOK]}],
            "rows": [
                {"s": "قَانُونٌ", "gloss": "a law", "ans": {"grp": "look"}, "why": "It has tanween. A law is a thing. Its plural is {قَوَانِينُ}."},
                {"s": "الْمُؤْمِنُونَ", "ans": {"grp": "smp"}, "why": "{ال} + {مُؤْمِنٌ} + {ـُونَ}."},
                {"s": "الْقَانُونُ", "gloss": "the law", "ans": {"grp": "look"}, "why": "The {ن} takes a damma here. A plural's {ن} always has a fatha."},
                {"s": "الْمُجْتَهِدِينَ", "ans": {"grp": "smp"}, "why": "The {ـِينَ} shape of {الْمُجْتَهِدُونَ}."},
                {"s": "صَابُونٌ", "gloss": "soap", "ans": {"grp": "look"}, "why": "A thing with tanween. The {ن} is part of the word."},
                {"s": "الْمِسْكِينُ", "gloss": "the poor man", "ans": {"grp": "look"}, "why": "One man. The {ن} takes a damma, so it is part of the word."},
            ],
        },
        {
            "title": "Find the singular",
            "fields": [{"key": "pick", "label": "Singular", "options": []}],
            "rows": [
                {"s": "الْمُحَاسِبُونَ", "gloss": "the accountants", "ans": {"pick": "c"},
                 "opts": {"pick": pick("حِسَابٌ", "الْمُحَاسِبَةُ", "مُحَاسِبٌ")},
                 "why": "Take away {ال} and {ـُونَ}: {مُحَاسِبٌ}."},
                {"s": "خَبَّازِينَ", "gloss": "bakers", "ans": {"pick": "a"},
                 "opts": {"pick": pick("خَبَّازٌ", "خُبْزٌ", "خَبَّازِي")},
                 "why": "Take away {ـِينَ}: {خَبَّازٌ}. {خُبْزٌ} is bread."},
                {"s": "الْمُسْلِمِينَ", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَسْلَمٌ", "مُسْلِمٌ", "مُسْلِمَانِ")},
                 "why": "Take away {ال} and {ـِينَ}: {مُسْلِمٌ}."},
                {"s": "مُدِيرُونَ", "gloss": "principals", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مُدِيرَةٌ", "مُدِيرٌ", "مُدِيرُونٌ")},
                 "why": "Take away {ـُونَ}: {مُدِيرٌ}."},
                {"s": "الصَّالِحُونَ", "ans": {"pick": "a"},
                 "opts": {"pick": pick("صَالِحٌ", "صَالِحَةٌ", "صَلَاحٌ")},
                 "why": "Take away {ال} and {ـُونَ}: {صَالِحٌ}."},
            ],
        },
        {
            "title": "Which group?",
            "fields": [{"key": "grp", "label": "Group", "options": [SING, DUAL, SMP, BRK]}],
            "rows": [
                {"s": "مُهَنْدِسَانِ", "ans": {"grp": "dual"}, "why": "{ـَانِ} means two: two engineers."},
                {"s": "مُهَنْدِسِينَ", "ans": {"grp": "smp"}, "why": "Kasra before {ي}, fatha on {نَ}: the plural shape {ـِينَ}."},
                {"s": "مُدَرِّسَيْنِ", "ans": {"grp": "dual"}, "why": "Fatha before {ي}, kasra on {نِ}: the dual shape {ـَيْنِ}."},
                {"s": "رِجَالٌ", "ans": {"grp": "brk"}, "why": "The shape of {رَجُلٌ} changed inside: a broken plural."},
                {"s": "مِسْكِينٌ", "ans": {"grp": "sing"}, "why": "One poor man. The {ن} is part of the word."},
                {"s": "فَلَّاحُونَ", "ans": {"grp": "smp"}, "why": "{فَلَّاحٌ} + {ـُونَ}."},
            ],
        },
        {
            "title": "What does it mean?",
            "fields": [{"key": "pick", "label": "Meaning", "options": []}],
            "rows": [
                {"s": "الطُّلَّابُ مُجْتَهِدُونَ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The students are hard-working.", "The student is hard-working.", "The hard-working students")},
                 "why": "{الطُّلَّابُ} is a broken plural of people. Its Information takes {ـُونَ}: {مُجْتَهِدُونَ}."},
                {"s": "هَؤُلَاءِ فَلَّاحُونَ صَالِحُونَ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("These farmers are good.", "This is a good farmer.", "These are good farmers.")},
                 "why": "{فَلَّاحُونَ} has no {ال}: a sentence. {صَالِحُونَ} is its adjective."},
                {"s": "ذَهَبَ الْمُهَنْدِسُونَ إِلَى الْمَسْجِدِ.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("The engineer went to the mosque.", "The engineers went to the mosque.", "The two engineers went to the mosque.")},
                 "why": "{الْمُهَنْدِسُونَ} is plural. Two engineers would be {الْمُهَنْدِسَانِ}."},
                {"s": "الْمِسْكِينُ فِي الشَّارِعِ.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("The poor man is in the street.", "The poor men are in the street.", "The knife is in the street.")},
                 "why": "{الْمِسْكِينُ} is one man. Its {ن} takes the damma. A knife is {سِكِّينٌ}."},
                {"s": "الْمُسَافِرُونَ فِي السَّيَّارَةِ.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("The traveller is in the car.", "The travellers are in the cars.", "The travellers are in the car.")},
                 "why": "{الْمُسَافِرُونَ} is plural, {السَّيَّارَةِ} is one car."},
            ],
        },
    ],
}
