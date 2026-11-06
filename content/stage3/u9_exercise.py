# Stage 3: class exercise (review of units 1-7, done together in class before the Stage 3 quiz)


def pick(*labels):
    return [{"k": k, "label": l} for k, l in zip("abc", labels)]


JOBS = [
    {"k": "topic", "label": "Topic · مُبْتَدَأٌ", "color": "gold"},
    {"k": "doer", "label": "Doer · فَاعِلٌ", "color": "orange"},
    {"k": "obj", "label": "Object · مَفْعُولٌ بِهِ", "color": "pink"},
    {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"},
    {"k": "prep", "label": "After a preposition", "color": "green"},
    {"k": "harf", "label": "Ḥarf (no iʿrāb job)", "color": "grey"},
]

PLACES = [
    {"k": "raf", "label": "Place of rafʿ · فِي مَحَلِّ رَفْعٍ", "color": "red"},
    {"k": "nasb", "label": "Place of naṣb · فِي مَحَلِّ نَصْبٍ", "color": "pink"},
    {"k": "jarr", "label": "Place of jarr · فِي مَحَلِّ جَرٍّ", "color": "green"},
    {"k": "none", "label": "No place · لَا مَحَلَّ لَهُ", "color": "grey"},
]


UNIT = {
    "id": "s3-exercise",
    "order": 8,
    "kind": "exercise",
    "title": "Stage 3 class exercise",
    "ar": "تَمْرِينُ المَبْنِيَّاتِ",
    "blurb": "Ten mixed cards on all seven groups of fixed words, done together in class before the Stage 3 quiz.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 3 · CLASS EXERCISE", "title": "All the fixed words together",
         "text": "Ten cards that mix every Stage 3 unit. We do them together in class, before the Stage 3 quiz.",
         "wm": "المَبْنِيَّاتُ"},

        {"t": "h2", "text": "How we do it in class"},
        {"t": "p", "text": "Work in pairs, or come to the board. One student reads the Arabic aloud and gives the answer. The partner says why, or corrects it. Then swap for the next row."},
        {"t": "tip", "text": "Say the job first, then the place: \"Doer, in the place of rafʿ.\" For a ḥarf say: no place."},
        {"t": "tip", "text": "If a card is hard, open its unit and read the table again before the quiz."},

        {"t": "h2", "text": "The seven groups"},
        {"t": "cols", "items": [
            {"color": "blue", "title": "1. Separate pronouns", "ar": "الضَّمَائِرُ المُنْفَصِلَةُ",
             "text": "{أَنَا} to {هُنَّ}. As the Topic: place of rafʿ."},
            {"color": "blue", "title": "2. Attached pronouns", "ar": "الضَّمَائِرُ المُتَّصِلَةُ",
             "text": "{ـي} {ـكَ} {ـهُ}. Jarr on a noun or ḥarf, naṣb on a verb."},
            {"color": "teal", "title": "3. Pointing words", "ar": "أَسْمَاءُ الإِشَارَةِ",
             "text": "{هَذَا} {تِلْكَ} {هَؤُلَاءِ} {هُنَا}. Not fixed: {هَذَانِ}."},
            {"color": "purple", "title": "4. Relatives", "ar": "الأَسْمَاءُ المَوْصُولَةُ",
             "text": "{الَّذِي} {الَّتِي} {الَّذِينَ} {اللَّاتِي} {مَنْ} {مَا}. Not fixed: {اللَّذَانِ}."},
            {"color": "gold", "title": "5. Question words", "ar": "أَدَوَاتُ الِاسْتِفْهَامِ",
             "text": "Isms {مَنْ} {مَتَى} {أَيْنَ} {كَمْ}, ḥarfs {هَلْ} {أَ}. Not fixed: {أَيٌّ}."},
            {"color": "navy", "title": "6. Fixed verbs", "ar": "المَاضِي وَالأَمْرُ",
             "text": "Past {كَتَبْتُ}, order {اُكْتُبْ}, and {مَا} + past: {مَا كَتَبَ} \"he did not write\"."},
            {"color": "grey", "title": "7. Particles", "ar": "الحُرُوفُ",
             "text": "Jarr, joining, answer, question and {يَا}. A ḥarf has no place."},
        ]},

        {"t": "summary", "title": "Remember", "items": [
            "A fixed word never changes its ending.",
            "A fixed ism still has a job, and the job gives it a place: rafʿ, naṣb or jarr.",
            "A ḥarf has no place: {لَا مَحَلَّ لَهُ مِنَ الإِعْرَابِ}.",
            "{مَا} can be \"what\" (an ism, units 4 and 5) or \"did not\" before a past verb (a ḥarf, unit 6).",
            "Not fixed: {هَذَانِ}، {اللَّذَانِ}، {أَيٌّ}, and the present verb.",
        ]},
    ],

    "practice": [
        # 1 · unit 1: separate pronouns
        {
            "title": "Choose the pronoun",
            "fields": [{"key": "pick", "label": "Pronoun", "options": []}],
            "rows": [
                {"s": "[الإِمَامُ] فِي المَسْجِدِ", "gloss": "The imam is in the mosque.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("هُوَ", "هِيَ", "هُمْ")}, "why": "One man, absent: {هُوَ فِي المَسْجِدِ}."},
                {"s": "[النِّسَاءُ] فِي الغُرْفَةِ", "gloss": "The women are in the room.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("هُمْ", "هُمَا", "هُنَّ")}, "why": "Three or more women, absent: {هُنَّ}."},
                {"s": "To Hamid and Ali: ... فِي الفَصْلِ.", "gloss": "You two are in the classroom.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("هُمَا", "أَنْتُمْ", "أَنْتُمَا")}, "why": "Two people you talk to: {أَنْتُمَا}. {هُمَا} is for two who are absent."},
                {"s": "[أَنَا وَحَامِدٌ] فِي السُّوقِ", "gloss": "Hamid and I are in the market.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("نَحْنُ", "هُمَا", "أَنْتُمَا")}, "why": "The speaker is in the group: {نَحْنُ}."},
                {"s": "[الحَقِيبَةُ] عَلَى الكُرْسِيِّ", "gloss": "The bag is on the chair.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هُوَ", "هِيَ", "أَنْتِ")}, "why": "{الحَقِيبَةُ} is feminine: {هِيَ}."},
                {"s": "To Aminah: ... مُدَرِّسَةٌ.", "gloss": "You are a teacher.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("أَنْتَ", "هِيَ", "أَنْتِ")}, "why": "One woman you talk to: {أَنْتِ}, with kasra on the {ت}."},
            ],
        },
        # 2 · unit 2: attached pronouns
        {
            "title": "Join the attached pronoun",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "عَلَى + ـكُنَّ", "gloss": "on you (women)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("عَلَيْكُنَّ", "عَلَاكُنَّ", "عَلَيْهِنَّ")}, "why": "{عَلَى} becomes {عَلَيْـ}, then {ـكُنَّ}. {عَلَيْهِنَّ} is \"on them (women)\"."},
                {"s": "إِلَى + ـهُمْ", "gloss": "to them (men)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("إِلَيْهُمْ", "إِلَيْهِمْ", "إِلَاهُمْ")}, "why": "{إِلَى} becomes {إِلَيْـ}. After {ي}, {ـهُمْ} becomes {ـهِمْ}."},
                {"s": "لِ + ـنَا", "gloss": "for us", "ans": {"pick": "c"},
                 "opts": {"pick": pick("لِنَا", "لِينَا", "لَنَا")}, "why": "{لِ} becomes {لَ} before a pronoun: {لَنَا}."},
                {"s": "قَلَمٌ + ـي", "gloss": "my pen", "ans": {"pick": "a"},
                 "opts": {"pick": pick("قَلَمِي", "قَلَمُي", "القَلَمِي")}, "why": "Kasra before {ـي}, and no {ال} or tanween: {قَلَمِي}."},
                {"s": "غُرْفَةٌ + ـكِ", "gloss": "your room (one woman)", "ans": {"pick": "b"},
                 "opts": {"pick": pick("غُرْفَةُكِ", "غُرْفَتُكِ", "غُرْفَتُكَ")}, "why": "The {ة} is written {ت}, and {ـكِ} has kasra: {غُرْفَتُكِ}."},
                {"s": "اُكْتُبْ + ـهَا", "gloss": "write it (the letter)", "ans": {"pick": "c"},
                 "opts": {"pick": pick("اُكْتُبُهَا", "اُكْتُبِهَا", "اُكْتُبْهَا")}, "why": "The order verb keeps its sukūn: {اُكْتُبْهَا}. {ـهَا} is the object."},
            ],
        },
        # 3 · unit 3: pointing words
        {
            "title": "Choose the pointing word",
            "fields": [{"key": "pick", "label": "Pointing word", "options": []}],
            "rows": [
                {"s": "... الوَلَدُ مَرِيضٌ.", "gloss": "This boy is sick.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("هَذَا", "هَذِهِ", "هَؤُلَاءِ")}, "why": "Near, one male: {هَذَا الوَلَدُ}."},
                {"s": "... مِفْتَاحٌ.", "gloss": "That is a key.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("تِلْكَ", "ذَلِكَ", "هَذِهِ")}, "why": "Far and masculine: {ذَلِكَ مِفْتَاحٌ}."},
                {"s": "... سَاعَةُ المُدِيرِ.", "gloss": "That is the principal's watch.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("تِلْكَ", "ذَلِكَ", "أُولَئِكَ")}, "why": "Far and feminine: {تِلْكَ}. {سَاعَةُ المُدِيرِ} has no {ال} on {سَاعَةُ}, so this is a sentence."},
                {"s": "... الرِّجَالُ تُجَّارٌ.", "gloss": "These men are merchants.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("هَذَا", "أُولَئِكَ", "هَؤُلَاءِ")}, "why": "A near group of people: {هَؤُلَاءِ}. {أُولَئِكَ} is \"those\"."},
                {"s": "حَامِدٌ ...", "gloss": "Hamid is there.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هُنَا", "هُنَاكَ", "ذَلِكَ")}, "why": "\"There\" is {هُنَاكَ}. {هُنَا} is \"here\"."},
                {"s": "... أَقْلَامٌ.", "gloss": "These are pens.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("هَؤُلَاءِ", "هَذِهِ", "هَذَا")}, "why": "Pens are things, not people. For plural things Arabic uses {هَذِهِ}."},
            ],
        },
        # 4 · unit 4: relatives
        {
            "title": "Choose the relative word",
            "fields": [{"key": "pick", "label": "Relative", "options": []}],
            "rows": [
                {"s": "الطَّبِيبُ ... فِي الغُرْفَةِ مِنَ الهِنْدِ.", "gloss": "The doctor who is in the room is from India.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الَّذِي", "الَّتِي", "الَّذِينَ")}, "why": "{الطَّبِيبُ} is one male: {الَّذِي}."},
                {"s": "خَرَجَتِ البِنْتُ ... فَتَحَتِ النَّافِذَةَ.", "gloss": "The girl who opened the window went out.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("الَّذِي", "اللَّاتِي", "الَّتِي")}, "why": "One girl, and the verb {فَتَحَتِ} is feminine: {الَّتِي}."},
                {"s": "جَلَسَ الطُّلَّابُ ... كَتَبُوا الدَّرْسَ.", "gloss": "The students who wrote the lesson sat down.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("الَّذِينَ", "الَّذِي", "اللَّاتِي")}, "why": "A group of males, and the verb is {كَتَبُوا}: {الَّذِينَ}."},
                {"s": "النِّسَاءُ ... فِي المَسْجِدِ مِنَ المَدِينَةِ.", "gloss": "The women who are in the mosque are from the city.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("الَّتِي", "اللَّاتِي", "الَّذِينَ")}, "why": "A group of women: {اللَّاتِي}."},
                {"s": "قَرَأْتُ ... فِي الحَقِيبَةِ.", "gloss": "I read what is in the bag.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَنْ", "مَا", "الَّذِينَ")}, "why": "A thing: {مَا} \"what\". {مَنْ} and {الَّذِينَ} are for people."},
                {"s": "شَكَرْتُ ... فَتَحَ البَابَ.", "gloss": "I thanked the one who opened the door.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَنْ", "مَا", "الَّتِي")}, "why": "A person, and {فَتَحَ} is masculine: {مَنْ} \"the one who\"."},
            ],
        },
        # 5 · unit 5: question words
        {
            "title": "Choose the question word",
            "fields": [{"key": "pick", "label": "Question word", "options": []}],
            "rows": [
                {"s": "... دَخَلَ الفَصْلَ؟ المُدَرِّسُ.", "gloss": "Who came into the classroom? The teacher.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَا", "مَنْ", "مَتَى")}, "why": "The answer is a person: {مَنْ}."},
                {"s": "... رَجُلًا فِي المَسْجِدِ؟", "gloss": "How many men are in the mosque?", "ans": {"pick": "a"},
                 "opts": {"pick": pick("كَمْ", "كَيْفَ", "بِكَمْ")}, "why": "A number: {كَمْ}, then one noun with tanween fatha: {رَجُلًا}. {بِكَمْ} asks a price."},
                {"s": "... جَلَسْتُمْ؟ فِي المَطْبَخِ.", "gloss": "Where did you (pl) sit? In the kitchen.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("مَتَى", "لِمَاذَا", "أَيْنَ")}, "why": "The answer is a place: {أَيْنَ}."},
                {"s": "... خَرَجْتِ مِنَ البَيْتِ؟ فِي اللَّيْلِ.", "gloss": "When did you (f) leave the house? At night.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَتَى", "مَنْ", "كَمْ")}, "why": "The answer is a time: {مَتَى}."},
                {"s": "... فَتَحْتَ النَّافِذَةَ؟", "gloss": "Why did you open the window?", "ans": {"pick": "b"},
                 "opts": {"pick": pick("مَاذَا", "لِمَاذَا", "مَنْ")}, "why": "\"Why\": {لِمَاذَا}, \"for what?\"."},
                {"s": "... فَتَحَ الوَلَدُ؟ فَتَحَ البَابَ.", "gloss": "What did the boy open? He opened the door.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("كَيْفَ", "أَيْنَ", "مَاذَا")}, "why": "The answer is a thing, before a verb: {مَاذَا}."},
            ],
        },
        # 6 · unit 6: past verb, order verb, مَا + past
        {
            "title": "Past, order or \"did not\": choose the verb",
            "fields": [{"key": "pick", "label": "Right form", "options": []}],
            "rows": [
                {"s": "أَنْتُنَّ + خَرَجَ", "gloss": "you (f pl) went out", "ans": {"pick": "b"},
                 "opts": {"pick": pick("خَرَجْنَ", "خَرَجْتُنَّ", "خَرَجْتُمْ")}, "why": "{أَنْتُنَّ} takes {ـتُنَّ}: {خَرَجْتُنَّ}. {خَرَجْنَ} is \"they (f) went out\"."},
                {"s": "هُمَا + دَرَسَ", "gloss": "they two (men) studied", "ans": {"pick": "a"},
                 "opts": {"pick": pick("دَرَسَا", "دَرَسْتُمَا", "دَرَسَتَا")}, "why": "Two absent men: {دَرَسَا}. {دَرَسَتَا} is for two women."},
                {"s": "Sit! (to women)", "ans": {"pick": "c"},
                 "opts": {"pick": pick("جَلَسْنَ", "اُجْلُسْنَ", "اِجْلِسْنَ")}, "why": "Middle kasra, so {اِ}. To women: {اِجْلِسْنَ}. {جَلَسْنَ} is the past."},
                {"s": "Study! (to a man)", "ans": {"pick": "a"},
                 "opts": {"pick": pick("اُدْرُسْ", "اِدْرَسْ", "دَرَسَ")}, "why": "Middle damma, so {اُ}: {اُدْرُسْ}, built on sukūn."},
                {"s": "he did not drink", "ans": {"pick": "c"},
                 "opts": {"pick": pick("لَا شَرِبَ", "مَا شَرِبَتْ", "مَا شَرِبَ")}, "why": "\"Did not\" with a past verb is {مَا}. {شَرِبَتْ} is \"she\"."},
                {"s": "we did not enter", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مَا دَخَلْنَا", "مَا دَخَلْنَ", "لَا دَخَلْنَا")}, "why": "{مَا} + {دَخَلْنَا}. {دَخَلْنَ} is \"they (f) entered\"."},
            ],
        },
        # 7 · unit 7: particles
        {
            "title": "Choose the right ḥarf",
            "fields": [{"key": "pick", "label": "Ḥarf", "options": []}],
            "rows": [
                {"s": "خَرَجَ الطَّالِبُ ... المَسْجِدِ.", "gloss": "The student went out of the mosque.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("مِنَ", "ثُمَّ", "يَا")}, "why": "\"Out of\": {مِنْ}, which becomes {مِنَ} before {ال}."},
                {"s": "الدَّرْسُ ... الشَّمْسِ.", "gloss": "The lesson is about the sun.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("عَلَى", "عَنِ", "أَوِ")}, "why": "\"About\": {عَنْ}, which becomes {عَنِ} before {ال}."},
                {"s": "دَخَلَ حَامِدٌ ... عَلِيٌّ.", "gloss": "Hamid came in, then later Ali.", "ans": {"pick": "c"},
                 "opts": {"pick": pick("إِلَى", "أَوْ", "ثُمَّ")}, "why": "\"Then, after a while\": {ثُمَّ}. {عَلِيٌّ} copies the damma of {حَامِدٌ}."},
                {"s": "أَمَا كَتَبْتِ الدَّرْسَ؟ …، كَتَبْتُهُ.", "gloss": "Didn't you (f) write the lesson? Yes, I wrote it.", "ans": {"pick": "b"},
                 "opts": {"pick": pick("نَعَمْ", "بَلَى", "لَا")}, "why": "{أَ} + {مَا} \"did not\" makes a \"not\" question. Yes to it is {بَلَى}."},
                {"s": "… آمِنَةُ، اُكْتُبِي.", "gloss": "Aminah, write.", "ans": {"pick": "a"},
                 "opts": {"pick": pick("يَا", "هَلْ", "عَلَى")}, "why": "Calling Aminah: {يَا آمِنَةُ}."},
                {"s": "… جَلَسَ حَامِدٌ فِي الفَصْلِ؟", "gloss": "Did Hamid sit in the classroom?", "ans": {"pick": "c"},
                 "opts": {"pick": pick("نَعَمْ", "بَلْ", "هَلْ")}, "why": "A yes/no question starts with {هَلْ}."},
            ],
        },
        # 8 · mixed: the two kinds of مَا (units 2, 4, 6, 7)
        {
            "title": "Two kinds of مَا: job and place",
            "prompt": "هَلْ قَرَأْتَ الدَّرْسَ؟ لَا، مَا قَرَأْتُ مَا كَتَبْتَ لِي.",
            "en": "Did you read the lesson? No, I did not read what you wrote for me.",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "place", "label": "Place", "options": PLACES},
            ],
            "rows": [
                {"s": "مَا (before قَرَأْتُ)", "ans": {"job": "harf", "place": "none"},
                 "why": "After {لَا} \"no\", it means \"did not\" before {قَرَأْتُ}. A ḥarf, with no place."},
                {"s": "ـتُ (in قَرَأْتُ)", "ans": {"job": "doer", "place": "raf"},
                 "why": "{ـتُ} \"I\" did the reading. Doer, in the place of rafʿ."},
                {"s": "مَا (before كَتَبْتَ)", "ans": {"job": "obj", "place": "nasb"},
                 "why": "Read what? This {مَا} \"what\" is an ism, the object of {قَرَأْتُ}. Place of naṣb."},
                {"s": "ـتَ (in كَتَبْتَ)", "ans": {"job": "doer", "place": "raf"},
                 "why": "{ـتَ} \"you\" did the writing. Doer, in the place of rafʿ."},
                {"s": "ـي (in لِي)", "ans": {"job": "prep", "place": "jarr"},
                 "why": "{ـي} comes after {لِ}. In the place of jarr."},
            ],
        },
        # 9 · mixed: pointing word, attached pronouns, يَا, order verb (units 2, 3, 6, 7)
        {
            "title": "Job and place of each fixed word",
            "prompt": "هَذِهِ حَقِيبَتُكِ يَا آمِنَةُ، اِفْتَحِيهَا.",
            "en": "This is your bag, Aminah. Open it.",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "place", "label": "Place", "options": PLACES},
            ],
            "rows": [
                {"s": "هَذِهِ", "ans": {"job": "topic", "place": "raf"},
                 "why": "We talk about {هَذِهِ}. Topic, in the place of rafʿ."},
                {"s": "ـكِ (in حَقِيبَتُكِ)", "ans": {"job": "owner", "place": "jarr"},
                 "why": "\"Your\" bag: {ـكِ} is the owner, in the place of jarr."},
                {"s": "يَا", "ans": {"job": "harf", "place": "none"},
                 "why": "{يَا} is the calling ḥarf. It has no place."},
                {"s": "ـي (in اِفْتَحِيهَا)", "ans": {"job": "doer", "place": "raf"},
                 "why": "{ـي} is \"you (f)\", the doer of the order. Place of rafʿ."},
                {"s": "ـهَا (in اِفْتَحِيهَا)", "ans": {"job": "obj", "place": "nasb"},
                 "why": "Open what? {ـهَا} \"it\", the bag. Object, in the place of naṣb."},
            ],
        },
        # 10 · mixed: pronouns, question word, pointing word, ḥarf (units 1, 3, 5, 7)
        {
            "title": "Where from? Job and place",
            "prompt": "مِنْ أَيْنَ أَنْتُمْ؟ نَحْنُ مِنْ هَذِهِ المَدِينَةِ.",
            "en": "Where are you from? We are from this city.",
            "fields": [
                {"key": "job", "label": "Job", "options": JOBS},
                {"key": "place", "label": "Place", "options": PLACES},
            ],
            "rows": [
                {"s": "مِنْ (in مِنْ أَيْنَ)", "ans": {"job": "harf", "place": "none"},
                 "why": "{مِنْ} is a jarr ḥarf. A ḥarf has no place."},
                {"s": "أَيْنَ", "ans": {"job": "prep", "place": "jarr"},
                 "why": "{أَيْنَ} comes after {مِنْ}. A fixed question ism, in the place of jarr."},
                {"s": "أَنْتُمْ", "ans": {"job": "topic", "place": "raf"},
                 "why": "We ask about {أَنْتُمْ}. It is the Topic, in the place of rafʿ, even though it comes last."},
                {"s": "نَحْنُ", "ans": {"job": "topic", "place": "raf"},
                 "why": "{نَحْنُ} starts the answer. Topic, in the place of rafʿ."},
                {"s": "هَذِهِ", "ans": {"job": "prep", "place": "jarr"},
                 "why": "{هَذِهِ} comes after {مِنْ}. Place of jarr. {المَدِينَةِ} shows the kasra."},
            ],
        },
    ],

    "homework": [],
}
