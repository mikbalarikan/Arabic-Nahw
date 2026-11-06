# Stage 0 class exercise: one review lesson over units 1-7, done in class before the Stage 0 quiz.

LAST7 = {"key": "mark", "label": "Last mark", "options": [
    {"k": "fatha", "label": "Fatha · ـَ", "color": "pink"},
    {"k": "damma", "label": "Damma · ـُ", "color": "red"},
    {"k": "kasra", "label": "Kasra · ـِ", "color": "green"},
    {"k": "sukun", "label": "Sukūn · ـْ", "color": "navy"},
    {"k": "un", "label": "Tanween ـٌ (-un)", "color": "olive"},
    {"k": "an", "label": "Tanween ـً (-an)", "color": "olive"},
    {"k": "in", "label": "Tanween ـٍ (-in)", "color": "olive"}]}

MARK5 = {"key": "mark", "label": "Last mark", "options": [
    {"k": "fatha", "label": "Fatha ـَ", "color": "pink"},
    {"k": "damma", "label": "Single damma ـُ", "color": "red"},
    {"k": "kasra", "label": "Single kasra ـِ", "color": "green"},
    {"k": "sukun", "label": "Sukūn ـْ", "color": "navy"},
    {"k": "tanween", "label": "Tanween (doubled) ـٌ ـً ـٍ", "color": "olive"}]}

KIND = {"key": "kind", "label": "Kind", "options": [
    {"k": "ism", "label": "Ism · اِسْمٌ", "color": "blue"},
    {"k": "fil", "label": "Fiʿl · فِعْلٌ", "color": "navy"},
    {"k": "harf", "label": "Ḥarf · حَرْفٌ", "color": "grey"}]}

GENDER = {"key": "gender", "label": "Gender", "options": [
    {"k": "m", "label": "Masculine · مُذَكَّرٌ", "color": "blue"},
    {"k": "f", "label": "Feminine · مُؤَنَّثٌ", "color": "pink"}]}

DEF = {"key": "def", "label": "Definite?", "options": [
    {"k": "m", "label": "Maʿrifa · مَعْرِفَةٌ", "color": "teal"},
    {"k": "n", "label": "Nakira · نَكِرَةٌ", "color": "brown"}]}

SM = {"key": "kind", "label": "Letter after ال", "options": [
    {"k": "sun", "label": "Sun · شَمْسِيَّةٌ", "color": "gold"},
    {"k": "moon", "label": "Moon · قَمَرِيَّةٌ", "color": "navy"}]}

JOB = {"key": "job", "label": "Job", "options": [
    {"k": "topic", "label": "Topic · مُبْتَدَأٌ", "color": "gold"},
    {"k": "info", "label": "Information · خَبَرٌ", "color": "red"},
    {"k": "prep", "label": "After a preposition", "color": "green"},
    {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"}]}

FORM = {"key": "form", "label": "Form", "options": [
    {"k": "raf", "label": "Rafʿ · رَفْعٌ", "color": "red"},
    {"k": "jarr", "label": "Jarr · جَرٌّ", "color": "green"}]}

PICK = {"key": "pick", "label": "Correct form", "options": []}


def o(*labels):
    return [{"k": k, "label": l} for k, l in zip("abc", labels)]


UNIT = {
    "id": "s0-exercise",
    "order": 8,
    "kind": "exercise",
    "title": "Stage 0 class exercise",
    "ar": "تَمْرِينُ الْمَرْحَلَةِ",
    "blurb": "Ten cards that review all seven Stage 0 units together in class, before the Stage 0 quiz.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 0 · CLASS EXERCISE", "title": "Put Stage 0 together",
         "text": "Ten cards on everything from Stage 0. We do them together in class, one card at a time.",
         "wm": "تَمْرِينٌ"},

        {"t": "h2", "text": "How we do it in class"},
        {"t": "p", "text": "Work in pairs, or come to the board one by one. Say each answer out loud and give the reason. "
                           "Then tap your answer and press Check. We do this before the Stage 0 quiz, so mistakes here are welcome."},
        {"t": "tip", "text": "The cards get harder as you go. Cards 6, 7 and 10 use a whole sentence and ask two things about each word."},

        {"t": "h2", "text": "The seven topics"},
        {"t": "cols", "items": [
            {"color": "olive", "title": "1. Marks", "ar": "الْحَرَكَاتُ", "text": "Read the last mark: fatha, damma, kasra, sukūn or tanween."},
            {"color": "blue", "title": "2. Kinds of word", "ar": "اِسْمٌ فِعْلٌ حَرْفٌ", "text": "Every word is an ism, a fiʿl or a ḥarf."},
            {"color": "pink", "title": "3. Gender", "ar": "مُذَكَّرٌ مُؤَنَّثٌ", "text": "{ة} usually means feminine. Use {هُوَ} or {هِيَ}."},
            {"color": "teal", "title": "4. Definite", "ar": "مَعْرِفَةٌ نَكِرَةٌ", "text": "{ال} or a name: maʿrifa. Tanween on a noun: nakira."},
            {"color": "gold", "title": "5. Sun and moon", "ar": "شَمْسِيَّةٌ قَمَرِيَّةٌ", "text": "Sun letter: shadda, silent {ل}. Moon letter: {لْ} is heard."},
            {"color": "purple", "title": "6. Adjective and iḍāfa", "ar": "صِفَةٌ إِضَافَةٌ", "text": "The ṣifa copies its noun. The muḍāf has no {ال} and no tanween."},
            {"color": "red", "title": "7. Iʿrāb", "ar": "إِعْرَابٌ", "text": "Job, then form, then sign: Topic and Information rafʿ, after a preposition or owner jarr."}]},

        {"t": "summary", "title": "For every word, ask", "items": [
            "What kind of word is it, and what is its last mark?",
            "Is it masculine or feminine, maʿrifa or nakira?",
            "What is its job? The job gives the form, and the form gives the last vowel."]},
    ],

    "practice": [
        # 1. Unit 1: marks
        {"title": "Which mark is on the last letter?",
         "fields": [LAST7],
         "rows": [
             {"s": "الْكَلْبُ", "gloss": "the dog", "ans": {"mark": "damma"}, "why": "One damma with {ال}: al-kalbu."},
             {"s": "خَفِيفٌ", "gloss": "light", "ans": {"mark": "un"}, "why": "Two dammas: khafīfun."},
             {"s": "هُنَاكَ", "gloss": "there", "ans": {"mark": "fatha"}, "why": "The {ك} has one fatha: hunāka."},
             {"s": "الدُّكَّانِ", "gloss": "the shop (in فِي الدُّكَّانِ)", "ans": {"mark": "kasra"}, "why": "One kasra with {ال}: ad-dukkāni."},
             {"s": "دِيكًا", "gloss": "a rooster", "ans": {"mark": "an"}, "why": "Two fathas with the extra alif: dīkan."},
             {"s": "لَحْمٍ", "gloss": "meat", "ans": {"mark": "in"}, "why": "Two kasras below: laḥmin."}]},

        # 2. Unit 2: ism, fiʿl, ḥarf
        {"title": "Ism, fiʿl or ḥarf?",
         "prompt": "أَيْنَ ذَهَبَ الْوَزِيرُ؟ ذَهَبَ إِلَى الْعِرَاقِ.",
         "en": "Where did the minister go? He went to Iraq.",
         "fields": [KIND],
         "rows": [
             {"s": "أَيْنَ", "gloss": "where?", "ans": {"kind": "ism"}, "why": "A fixed ism. It can come after a preposition: {مِنْ أَيْنَ}."},
             {"s": "ذَهَبَ", "gloss": "went", "ans": {"kind": "fil"}, "why": "A past action: he went."},
             {"s": "الْوَزِيرُ", "gloss": "the minister", "ans": {"kind": "ism"}, "why": "It has {ال} and names a person."},
             {"s": "إِلَى", "gloss": "to", "ans": {"kind": "harf"}, "why": "A preposition. It needs a word after it."},
             {"s": "الْعِرَاقِ", "gloss": "Iraq", "ans": {"kind": "ism"}, "why": "The name of a place, with {ال}, after {إِلَى}."}]},

        # 3. Unit 3: gender
        {"title": "Masculine or feminine?",
         "fields": [GENDER],
         "rows": [
             {"s": "الْجَنَّةُ", "gloss": "the garden, Paradise", "ans": {"gender": "f"}, "why": "It ends in {ة}."},
             {"s": "الْخَالُ", "gloss": "the maternal uncle", "ans": {"gender": "m"}, "why": "No {ة}, and a man."},
             {"s": "صَفِيَّةُ", "gloss": "Ṣafiyyah", "ans": {"gender": "f"}, "why": "A girl's name with {ة}. It has one damma, no tanween."},
             {"s": "عَيْنٌ", "gloss": "an eye", "ans": {"gender": "f"}, "why": "Careful: no {ة}, but {عَيْنٌ} is feminine, like {يَدٌ}."},
             {"s": "الرَّأْسُ", "gloss": "the head", "ans": {"gender": "m"}, "why": "No {ة}: masculine."},
             {"s": "الْوَجْهُ", "gloss": "the face", "ans": {"gender": "m"}, "why": "No {ة}: masculine. The last letter is {ه}, not {ة}."}]},

        # 4. Unit 4: maʿrifa and nakira
        {"title": "Maʿrifa or nakira?",
         "fields": [DEF],
         "rows": [
             {"s": "إِمَامٌ", "gloss": "an imam", "ans": {"def": "n"}, "why": "Tanween on a noun: an imam."},
             {"s": "الْحِمَارُ", "gloss": "the donkey", "ans": {"def": "m"}, "why": "It has {ال}: the donkey."},
             {"s": "فَيْصَلٌ", "gloss": "Fayṣal", "ans": {"def": "m"}, "why": "A name is maʿrifa. Its tanween does not mean 'a'."},
             {"s": "شَيْخٌ", "gloss": "a sheikh", "ans": {"def": "n"}, "why": "Tanween on a noun: a sheikh."},
             {"s": "رُقَيَّةُ", "gloss": "Ruqayyah", "ans": {"def": "m"}, "why": "A name is maʿrifa, with or without tanween."},
             {"s": "وَاقِفٌ", "gloss": "standing", "ans": {"def": "n"}, "why": "No {ال}, with tanween. English does not say 'a' here, but it is nakira."}]},

        # 5. Unit 5: sun and moon letters
        {"title": "Sun or moon letter after ال?",
         "fields": [SM],
         "rows": [
             {"s": "اللَّبَنُ", "gloss": "the milk", "ans": {"kind": "sun"}, "why": "{ل} is a sun letter. The {ل} after {ال} has a shadda: al-labanu."},
             {"s": "الْهَوَاءُ", "gloss": "the air", "ans": {"kind": "moon"}, "why": "{لْ} has a sukūn and is heard: al-hawāʾu."},
             {"s": "الثَّوْبُ", "gloss": "the robe", "ans": {"kind": "sun"}, "why": "Shadda on {ث}: ath-thawbu."},
             {"s": "الْغَدَاءُ", "gloss": "the lunch", "ans": {"kind": "moon"}, "why": "{لْ} has a sukūn: al-ghadāʾu."},
             {"s": "الظُّهْرُ", "gloss": "noon", "ans": {"kind": "sun"}, "why": "Shadda on {ظ}: aẓ-ẓuhru."},
             {"s": "الْفَمُ", "gloss": "the mouth", "ans": {"kind": "moon"}, "why": "{لْ} has a sukūn: al-famu."}]},

        # 6. Mixed: units 1 + 2 (kind of word + last mark)
        {"title": "Kind of word and last mark",
         "prompt": "خَرَجَ الشَّيْخُ مِنَ الْمَسْجِدِ وَذَهَبَ إِلَى بَيْتِ مَسْعُودٍ.",
         "en": "The sheikh went out of the mosque and went to Masʿūd's house.",
         "fields": [KIND, MARK5],
         "rows": [
             {"s": "خَرَجَ", "gloss": "went out", "ans": {"kind": "fil", "mark": "fatha"}, "why": "A past action. Its last letter {ج} has a fatha."},
             {"s": "الشَّيْخُ", "gloss": "the sheikh", "ans": {"kind": "ism", "mark": "damma"}, "why": "It has {ال}, so one damma and no tanween."},
             {"s": "مِنَ", "gloss": "from", "ans": {"kind": "harf", "mark": "fatha"}, "why": "A preposition. Before {ال}, {مِنْ} is read {مِنَ}."},
             {"s": "الْمَسْجِدِ", "gloss": "the mosque", "ans": {"kind": "ism", "mark": "kasra"}, "why": "It has {ال} and comes after {مِنَ}: one kasra."},
             {"s": "بَيْتِ", "gloss": "house of", "ans": {"kind": "ism", "mark": "kasra"}, "why": "It comes after {إِلَى}. It is a muḍāf, so one kasra and no tanween."},
             {"s": "مَسْعُودٍ", "gloss": "Masʿūd", "ans": {"kind": "ism", "mark": "tanween"}, "why": "A name with two kasras: masʿūdin."}]},

        # 7. Mixed: units 3 + 4 (gender + definiteness)
        {"title": "Gender and definiteness",
         "prompt": "الْحَقِيبَةُ خَفِيفَةٌ وَالْحَجَرُ ثَقِيلٌ.",
         "en": "The bag is light and the stone is heavy.",
         "fields": [GENDER, DEF],
         "rows": [
             {"s": "الْحَقِيبَةُ", "gloss": "the bag", "ans": {"gender": "f", "def": "m"}, "why": "It ends in {ة}, and it has {ال}."},
             {"s": "خَفِيفَةٌ", "gloss": "light", "ans": {"gender": "f", "def": "n"}, "why": "It has {ة} to match the bag, and tanween."},
             {"s": "الْحَجَرُ", "gloss": "the stone", "ans": {"gender": "m", "def": "m"}, "why": "No {ة}, and it has {ال}."},
             {"s": "ثَقِيلٌ", "gloss": "heavy", "ans": {"gender": "m", "def": "n"}, "why": "No {ة} to match the stone, and tanween."}]},

        # 8. Unit 6: adjective and iḍāfa
        {"title": "Which is right?",
         "fields": [PICK],
         "rows": [
             {"s": "الْبَابُ … · the closed door", "ans": {"pick": "a"},
              "opts": {"pick": o("الْمُغْلَقُ", "مُغْلَقٌ", "الْمُغْلَقَةُ")},
              "why": "The ṣifa copies {الْبَابُ}: {ال} and no {ة}. With {مُغْلَقٌ} it means 'The door is closed.'"},
             {"s": "سَاعَةٌ … · a broken watch", "ans": {"pick": "b"},
              "opts": {"pick": o("مَكْسُورٌ", "مَكْسُورَةٌ", "الْمَكْسُورَةُ")},
              "why": "{سَاعَةٌ} is feminine and nakira, so {مَكْسُورَةٌ} with {ة} and tanween."},
             {"s": "the man's donkey", "ans": {"pick": "c"},
              "opts": {"pick": o("الْحِمَارُ الرَّجُلِ", "حِمَارٌ الرَّجُلِ", "حِمَارُ الرَّجُلِ")},
              "why": "The muḍāf has no {ال} and no tanween: {حِمَارُ الرَّجُلِ}."},
             {"s": "The kerchief is dirty.", "ans": {"pick": "b"},
              "opts": {"pick": o("الْمِنْدِيلُ الْوَسِخُ", "الْمِنْدِيلُ وَسِخٌ", "مِنْدِيلُ وَسِخٍ")},
              "why": "{ال} on the first word and tanween on the second make a sentence."},
             {"s": "the boy's maternal uncle", "ans": {"pick": "a"},
              "opts": {"pick": o("خَالُ الْوَلَدِ", "خَالُ الْوَلَدُ", "الْخَالُ الْوَلَدِ")},
              "why": "No {ال} on the muḍāf, and the owner takes a kasra: {الْوَلَدِ}."}]},

        # 9. Unit 7: iʿrāb
        {"title": "Job and form of the word in [ ]",
         "fields": [JOB, FORM],
         "rows": [
             {"s": "[السُّكَّرُ] حُلْوٌ", "gloss": "The sugar is sweet.", "ans": {"job": "topic", "form": "raf"}, "why": "The sentence starts with it. The Topic is rafʿ: one damma."},
             {"s": "التُّفَّاحُ [لَذِيذٌ]", "gloss": "Apples are delicious.", "ans": {"job": "info", "form": "raf"}, "why": "It tells us about {التُّفَّاحُ}. The Information is rafʿ."},
             {"s": "الْقِطُّ عَلَى [الْكُرْسِيِّ]", "gloss": "The cat is on the chair.", "ans": {"job": "prep", "form": "jarr"}, "why": "It comes after {عَلَى}, so it is jarr: kasra under the shadda."},
             {"s": "مِفْتَاحُ [الدُّكَّانِ] صَغِيرٌ", "gloss": "The key of the shop is small.", "ans": {"job": "owner", "form": "jarr"}, "why": "It is the owner after {مِفْتَاحُ}, so it is jarr."},
             {"s": "[سَاعَةُ] الْمُدِيرِ عَلَى الْمَكْتَبِ", "gloss": "The principal's watch is on the desk.", "ans": {"job": "topic", "form": "raf"}, "why": "The muḍāf starts the sentence. It is the Topic, so rafʿ: one damma."},
             {"s": "اِسْمُ الطَّبِيبِ [مَسْعُودٌ]", "gloss": "The doctor's name is Masʿūd.", "ans": {"job": "info", "form": "raf"}, "why": "It tells us the name. The Information is rafʿ: {مَسْعُودٌ}."}]},

        # 10. Mixed: units 6 + 7 (iḍāfa + job and form)
        {"title": "Job and form of each word",
         "prompt": "قَمِيصُ الْوَلَدِ وَسِخٌ وَثَوْبُ الشَّيْخِ فِي الْحَقِيبَةِ.",
         "en": "The boy's shirt is dirty and the sheikh's robe is in the bag.",
         "fields": [JOB, FORM],
         "rows": [
             {"s": "قَمِيصُ", "gloss": "shirt of", "ans": {"job": "topic", "form": "raf"}, "why": "The muḍāf starts the sentence. It is the Topic: rafʿ."},
             {"s": "الْوَلَدِ", "gloss": "the boy", "ans": {"job": "owner", "form": "jarr"}, "why": "The owner after {قَمِيصُ}: jarr."},
             {"s": "وَسِخٌ", "gloss": "dirty", "ans": {"job": "info", "form": "raf"}, "why": "It tells us about the shirt. The Information is rafʿ."},
             {"s": "ثَوْبُ", "gloss": "robe of (after وَ)", "ans": {"job": "topic", "form": "raf"}, "why": "A new sentence starts after {وَ}. {ثَوْبُ} is its Topic: rafʿ."},
             {"s": "الشَّيْخِ", "gloss": "the sheikh", "ans": {"job": "owner", "form": "jarr"}, "why": "The owner after {ثَوْبُ}: jarr."},
             {"s": "الْحَقِيبَةِ", "gloss": "the bag", "ans": {"job": "prep", "form": "jarr"}, "why": "It comes after {فِي}, so it is jarr. The Information is the whole phrase {فِي الْحَقِيبَةِ}."}]},
    ],

    "homework": [],
}
