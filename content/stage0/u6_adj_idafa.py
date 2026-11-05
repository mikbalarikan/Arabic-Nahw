TYPE = {"key": "type", "label": "What is it?", "options": [
    {"k": "phr", "label": "Noun + adjective · صِفَةٌ", "color": "grey"},
    {"k": "idf", "label": "Iḍāfa · إِضَافَةٌ", "color": "purple"},
    {"k": "sen", "label": "Full sentence", "color": "red"}]}

ROLE = {"key": "role", "label": "Role", "options": [
    {"k": "mudaf", "label": "Muḍāf · مُضَافٌ", "color": "teal"},
    {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ", "color": "purple"},
    {"k": "none", "label": "Neither"}]}

PICK = {"key": "pick", "label": "Correct form", "options": []}
OWN = {"key": "owner", "label": "The owner", "options": []}
MEAN = {"key": "mean", "label": "Meaning", "options": []}


def o(*labels):
    return [{"k": k, "label": l} for k, l in zip("abcd", labels)]


UNIT = {
    "id": "s0-adj-idafa",
    "order": 6,
    "title": "Adjective and iḍāfa",
    "ar": "الصِّفَةُ وَالْإِضَافَةُ",
    "blurb": "The big house, the house is big, the man's house: three patterns, three meanings.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 0 · UNIT 6", "title": "Two nouns side by side",
         "text": "Two words together can be a noun with an adjective, a full sentence, or an iḍāfa. The {ال} and the tanween tell you which.",
         "wm": "الصِّفَةُ وَالْإِضَافَةُ"},

        {"t": "h2", "text": "The adjective comes after its noun"},
        {"t": "p", "text": "An adjective, ṣifa {صِفَةٌ}, describes a noun. In Arabic it comes after the noun. English puts it before."},
        {"t": "examples", "items": [
            {"ar": "بَيْتٌ كَبِيرٌ", "en": "a big house", "note": "Word by word: 'house big'."},
            {"ar": "قَلَمٌ جَدِيدٌ", "en": "a new pen"},
            {"ar": "رَجُلٌ غَنِيٌّ", "en": "a rich man"}]},

        {"t": "h2", "text": "The adjective copies its noun"},
        {"t": "rule", "color": "grey", "title": "Copy the noun",
         "text": "The ṣifa copies its noun in definiteness ({ال} or tanween) and in gender ({ة} or no {ة}). Later it will copy the case too."},
        {"t": "table", "head": ["", "Masculine", "Feminine"], "rows": [
            ["Nakira", "بَيْتٌ كَبِيرٌ", "مَدْرَسَةٌ كَبِيرَةٌ"],
            ["", "a big house", "a big school"],
            ["Maʿrifa", "الْبَيْتُ الْكَبِيرُ", "الْمَدْرَسَةُ الْكَبِيرَةُ"],
            ["", "the big house", "the big school"]]},
        {"t": "examples", "items": [
            {"ar": "الْوَلَدُ الصَّغِيرُ", "en": "the small boy", "note": "Both have {ال}. Both are masculine."},
            {"ar": "سَاعَةٌ جَدِيدَةٌ", "en": "a new watch", "note": "Both have tanween. Both end in {ة}."},
            {"ar": "الْغُرْفَةُ النَّظِيفَةُ", "en": "the clean room"}]},
        {"t": "tip", "text": "The ṣifa follows the noun's real gender. {الْبِنْتُ} has no {ة} but is feminine, so: {الْبِنْتُ الْجَمِيلَةُ} 'the beautiful girl'."},

        {"t": "h2", "text": "Iḍāfa: 'X of Y'"},
        {"t": "p", "text": "Two nouns can also mean 'the X of Y' or 'Y's X'. This is an iḍāfa {إِضَافَةٌ}. The first word is the owned thing. The second is the owner."},
        {"t": "cols", "items": [
            {"color": "teal", "title": "Muḍāf (first)", "ar": "مُضَافٌ", "text": "The owned thing. No {ال}, no tanween: {كِتَابُ}"},
            {"color": "purple", "title": "Owner (second)", "ar": "مُضَافٌ إِلَيْهِ", "text": "Takes jarr, a kasra: {بِلَالٍ}, {الْإِمَامِ}"}]},
        {"t": "examples", "items": [
            {"ar": "كِتَابُ بِلَالٍ", "en": "Bilal's book"},
            {"ar": "بَيْتُ الْإِمَامِ", "en": "the imam's house"},
            {"ar": "بَابُ الْمَسْجِدِ", "en": "the door of the mosque"},
            {"ar": "مِفْتَاحُ السَّيَّارَةِ", "en": "the car key"}]},

        {"t": "h2", "text": "The first word: no ال, no tanween"},
        {"t": "rule", "color": "teal", "title": "Muḍāf",
         "text": "The muḍāf never takes {ال} and never takes tanween. When its owner is definite, the muḍāf is definite too."},
        {"t": "table", "head": ["Wrong", "Right", "Why"], "rows": [
            ["الْكِتَابُ الطَّالِبِ", "كِتَابُ الطَّالِبِ", "No {ال} on the first word"],
            ["كِتَابٌ الطَّالِبِ", "كِتَابُ الطَّالِبِ", "No tanween on the first word"],
            ["كِتَابُ الطَّالِبُ", "كِتَابُ الطَّالِبِ", "The owner needs kasra"]]},
        {"t": "tip", "text": "This is the Madinah lesson 5 exercise {صَحِّحِ التَّرَاكِيبَ}: correct the phrases."},

        {"t": "h2", "text": "The owner takes kasra"},
        {"t": "p", "text": "The owner is always in jarr. With {ال} it ends in kasra. Without {ال} it ends in kasra tanween."},
        {"t": "table", "head": ["Alone", "As owner", "English"], "rows": [
            ["بِلَالٌ", "كِتَابُ بِلَالٍ", "Bilal's book"],
            ["مُحَمَّدٌ", "بَيْتُ مُحَمَّدٍ", "Muhammad's house"],
            ["الْإِمَامُ", "بَيْتُ الْإِمَامِ", "the imam's house"],
            ["الْمُدَرِّسُ", "قَلَمُ الْمُدَرِّسِ", "the teacher's pen"]]},
        {"t": "tip", "text": "Names like {فَاطِمَةُ} and {زَيْنَبُ} behave differently as owners. For now we use names like {بِلَالٌ}, {حَامِدٌ} and {خَالِدٌ}."},

        {"t": "h2", "text": "Phrase, sentence or iḍāfa?"},
        {"t": "p", "text": "This is the key contrast of Stage 0. Look at the {ال} and the last vowels."},
        {"t": "table", "head": ["Arabic", "Pattern", "Meaning", "Type"], "rows": [
            ["الْبَيْتُ الْكَبِيرُ", "{ال} + {ال}, same ending", "the big house", "Noun + adjective (a phrase)"],
            ["بَيْتٌ كَبِيرٌ", "tanween + tanween", "a big house", "Noun + adjective (a phrase)"],
            ["الْبَيْتُ كَبِيرٌ", "{ال} + tanween", "The house is big.", "Full sentence"],
            ["بَيْتُ الرَّجُلِ", "bare first word + kasra", "the man's house", "Iḍāfa"]]},
        {"t": "rule", "color": "red", "title": "The quick test",
         "text": "First word with {ال}, second with tanween: a sentence. Second word copies the first: an adjective. First word bare, second in kasra: an iḍāfa."},
        {"t": "examples", "items": [
            {"ar": "بَيْتُ الرَّجُلِ كَبِيرٌ.", "en": "The man's house is big.", "note": "An iḍāfa, then the Information {كَبِيرٌ}."},
            {"ar": "بَابُ الْمَسْجِدِ مَفْتُوحٌ وَبَابُ الْمَدْرَسَةِ مُغْلَقٌ.", "en": "The mosque door is open and the school door is closed."}]},

        {"t": "summary", "title": "In four lines", "items": [
            "The ṣifa comes after its noun and copies it: {بَيْتٌ كَبِيرٌ}, {الْبَيْتُ الْكَبِيرُ}, {مَدْرَسَةٌ كَبِيرَةٌ}.",
            "Iḍāfa: the first word has no {ال} and no tanween: {كِتَابُ الطَّالِبِ}.",
            "The owner takes kasra: {كِتَابُ بِلَالٍ}, {بَيْتُ الْإِمَامِ}.",
            "{الْبَيْتُ الْكَبِيرُ} the big house, {الْبَيْتُ كَبِيرٌ} the house is big, {بَيْتُ الرَّجُلِ} the man's house."]},
    ],

    "practice": [
        {"title": "Adjective phrase, iḍāfa or sentence?", "fields": [TYPE], "rows": [
            {"s": "الْقَلَمُ الْجَدِيدُ", "ans": {"type": "phr"}, "why": "Both have {ال} and the same ending: 'the new pen'."},
            {"s": "الْقَلَمُ جَدِيدٌ", "ans": {"type": "sen"}, "why": "{ال} then tanween: 'The pen is new.'"},
            {"s": "قَلَمُ الْوَلَدِ", "ans": {"type": "idf"}, "why": "Bare first word, owner in kasra: 'the boy's pen'."},
            {"s": "كِتَابٌ صَغِيرٌ", "ans": {"type": "phr"}, "why": "Both have tanween: 'a small book'."},
            {"s": "الْبَابُ مَفْتُوحٌ", "ans": {"type": "sen"}, "why": "{ال} then tanween: 'The door is open.'"},
            {"s": "بَابُ الْبَيْتِ", "ans": {"type": "idf"}, "why": "Bare first word, owner in kasra: 'the door of the house'."}]},

        {"title": "Pick the correct adjective", "fields": [PICK], "rows": [
            {"s": "الْبَيْتُ … · the big house", "ans": {"pick": "a"}, "opts": {"pick": o("الْكَبِيرُ", "كَبِيرٌ", "الْكَبِيرَةُ")},
             "why": "Copy {ال} and the masculine: {الْبَيْتُ الْكَبِيرُ}."},
            {"s": "مَدْرَسَةٌ … · a big school", "ans": {"pick": "b"}, "opts": {"pick": o("كَبِيرٌ", "كَبِيرَةٌ", "الْكَبِيرَةُ")},
             "why": "Copy the tanween and the {ة}: {مَدْرَسَةٌ كَبِيرَةٌ}."},
            {"s": "الْغُرْفَةُ … · the clean room", "ans": {"pick": "c"}, "opts": {"pick": o("النَّظِيفُ", "نَظِيفَةٌ", "النَّظِيفَةُ")},
             "why": "Copy {ال} and the {ة}: {الْغُرْفَةُ النَّظِيفَةُ}."},
            {"s": "وَلَدٌ … · a small boy", "ans": {"pick": "a"}, "opts": {"pick": o("صَغِيرٌ", "الصَّغِيرُ", "صَغِيرَةٌ")},
             "why": "Copy the tanween, masculine: {وَلَدٌ صَغِيرٌ}."},
            {"s": "السَّاعَةُ … · the new watch", "ans": {"pick": "b"}, "opts": {"pick": o("جَدِيدَةٌ", "الْجَدِيدَةُ", "الْجَدِيدُ")},
             "why": "Copy {ال} and the {ة}: {السَّاعَةُ الْجَدِيدَةُ}."}]},

        {"title": "Correct the iḍāfa: which is right?", "fields": [PICK], "rows": [
            {"s": "the student's pen", "ans": {"pick": "c"}, "opts": {"pick": o("الْقَلَمُ الطَّالِبِ", "قَلَمٌ الطَّالِبِ", "قَلَمُ الطَّالِبِ")},
             "why": "The muḍāf has no {ال} and no tanween: {قَلَمُ الطَّالِبِ}."},
            {"s": "Bilal's book", "ans": {"pick": "a"}, "opts": {"pick": o("كِتَابُ بِلَالٍ", "كِتَابٌ بِلَالٍ", "الْكِتَابُ بِلَالٍ")},
             "why": "Bare muḍāf, owner in kasra tanween: {كِتَابُ بِلَالٍ}."},
            {"s": "the imam's house", "ans": {"pick": "b"}, "opts": {"pick": o("بَيْتُ الْإِمَامُ", "بَيْتُ الْإِمَامِ", "الْبَيْتُ الْإِمَامِ")},
             "why": "The owner takes kasra: {بَيْتُ الْإِمَامِ}."},
            {"s": "the door of the mosque", "ans": {"pick": "a"}, "opts": {"pick": o("بَابُ الْمَسْجِدِ", "بَابٌ الْمَسْجِدِ", "بَابُ الْمَسْجِدُ")},
             "why": "No tanween on the muḍāf, kasra on the owner: {بَابُ الْمَسْجِدِ}."}]},

        {"title": "Muḍāf, owner or neither? Tap each word.",
         "prompt": "بَيْتُ الْمُدَرِّسِ بَعِيدٌ وَبَيْتُ التَّاجِرِ قَرِيبٌ.",
         "en": "The teacher's house is far and the merchant's house is near.",
         "fields": [ROLE], "rows": [
            {"s": "بَيْتُ", "ans": {"role": "mudaf"}, "why": "No {ال}, no tanween, followed by its owner."},
            {"s": "الْمُدَرِّسِ", "ans": {"role": "owner"}, "why": "It owns the house, so it takes kasra."},
            {"s": "بَعِيدٌ", "ans": {"role": "none"}, "why": "The Information of the sentence: 'is far'."},
            {"s": "وَبَيْتُ", "ans": {"role": "mudaf"}, "why": "A second iḍāfa starts here: bare {بَيْتُ}."},
            {"s": "التَّاجِرِ", "ans": {"role": "owner"}, "why": "It owns the house, so it takes kasra."},
            {"s": "قَرِيبٌ", "ans": {"role": "none"}, "why": "The Information: 'is near'."}]},

        {"title": "Which word is the owner?", "fields": [OWN], "rows": [
            {"s": "مِفْتَاحُ السَّيَّارَةِ", "ans": {"owner": "b"}, "opts": {"owner": o("مِفْتَاحُ", "السَّيَّارَةِ", "No owner")},
             "why": "The key belongs to the car. {السَّيَّارَةِ} has kasra."},
            {"s": "الْبَيْتُ الْكَبِيرُ", "ans": {"owner": "c"}, "opts": {"owner": o("الْبَيْتُ", "الْكَبِيرُ", "No owner")},
             "why": "Both have {ال} and the same ending: an adjective, no iḍāfa."},
            {"s": "اِسْمُ الْوَلَدِ", "ans": {"owner": "b"}, "opts": {"owner": o("اِسْمُ", "الْوَلَدِ", "No owner")},
             "why": "'The boy's name'. {الْوَلَدِ} has kasra."},
            {"s": "الطَّالِبُ مَرِيضٌ", "ans": {"owner": "c"}, "opts": {"owner": o("الطَّالِبُ", "مَرِيضٌ", "No owner")},
             "why": "A sentence: 'The student is sick.' No iḍāfa."},
            {"s": "حَقِيبَةُ الْمُدَرِّسِ", "ans": {"owner": "b"}, "opts": {"owner": o("حَقِيبَةُ", "الْمُدَرِّسِ", "No owner")},
             "why": "'The teacher's bag'. {الْمُدَرِّسِ} has kasra."}]},

        {"title": "What does it mean?", "fields": [MEAN], "rows": [
            {"s": "الْوَلَدُ الطَّوِيلُ", "ans": {"mean": "a"}, "opts": {"mean": o("the tall boy", "The boy is tall.", "the tall one's boy")},
             "why": "Both words have {ال}: an adjective phrase."},
            {"s": "الْوَلَدُ طَوِيلٌ", "ans": {"mean": "b"}, "opts": {"mean": o("the tall boy", "The boy is tall.", "a tall boy")},
             "why": "{ال} then tanween: a full sentence."},
            {"s": "اِبْنُ الرَّجُلِ", "ans": {"mean": "c"}, "opts": {"mean": o("The son is a man.", "the son man", "the man's son")},
             "why": "Bare first word, owner in kasra: an iḍāfa."},
            {"s": "قَمِيصٌ نَظِيفٌ", "ans": {"mean": "a"}, "opts": {"mean": o("a clean shirt", "The shirt is clean.", "the clean shirt")},
             "why": "Both have tanween: 'a clean shirt'."}]},
    ],

    "homework": [
        {"title": "Adjective phrase, iḍāfa or sentence?", "fields": [TYPE], "rows": [
            {"s": "السَّيَّارَةُ الْجَدِيدَةُ", "ans": {"type": "phr"}, "why": "Both have {ال}, both feminine: 'the new car'."},
            {"s": "سَيَّارَةُ الْمُدِيرِ", "ans": {"type": "idf"}, "why": "Bare first word, owner in kasra: 'the principal's car'."},
            {"s": "السَّيَّارَةُ جَدِيدَةٌ", "ans": {"type": "sen"}, "why": "{ال} then tanween: 'The car is new.'"},
            {"s": "حَقِيبَةٌ ثَقِيلَةٌ", "ans": {"type": "phr"}, "why": "Both have tanween: 'a heavy bag'."},
            {"s": "اِسْمُ الطَّالِبِ", "ans": {"type": "idf"}, "why": "Bare first word, owner in kasra: 'the student's name'."},
            {"s": "الشَّارِعُ قَرِيبٌ", "ans": {"type": "sen"}, "why": "{ال} then tanween: 'The street is near.'"}]},

        {"title": "Pick the correct form", "fields": [PICK], "rows": [
            {"s": "الطَّالِبُ … · the sick student", "ans": {"pick": "a"}, "opts": {"pick": o("الْمَرِيضُ", "مَرِيضٌ", "الْمَرِيضَةُ")},
             "why": "Copy {ال}, masculine: {الطَّالِبُ الْمَرِيضُ}."},
            {"s": "حَقِيبَةٌ … · a heavy bag", "ans": {"pick": "c"}, "opts": {"pick": o("ثَقِيلٌ", "الثَّقِيلَةُ", "ثَقِيلَةٌ")},
             "why": "Copy the tanween and the {ة}: {حَقِيبَةٌ ثَقِيلَةٌ}."},
            {"s": "الْبِنْتُ … · the beautiful girl", "ans": {"pick": "b"}, "opts": {"pick": o("الْجَمِيلُ", "الْجَمِيلَةُ", "جَمِيلَةٌ")},
             "why": "{الْبِنْتُ} is feminine without {ة}, so the ṣifa takes {ة}: {الْبِنْتُ الْجَمِيلَةُ}."},
            {"s": "رَجُلٌ … · a rich man", "ans": {"pick": "a"}, "opts": {"pick": o("غَنِيٌّ", "الْغَنِيُّ", "غَنِيَّةٌ")},
             "why": "Copy the tanween, masculine: {رَجُلٌ غَنِيٌّ}."},
            {"s": "الْمَطْبَخُ … · the clean kitchen", "ans": {"pick": "b"}, "opts": {"pick": o("نَظِيفٌ", "النَّظِيفُ", "النَّظِيفَةُ")},
             "why": "Copy {ال}, masculine: {الْمَطْبَخُ النَّظِيفُ}."},
            {"s": "الْبَيْتُ … · The house is big.", "ans": {"pick": "c"}, "opts": {"pick": o("الْكَبِيرُ", "كَبِيرَةٌ", "كَبِيرٌ")},
             "why": "A sentence, so no {ال} on the second word: {الْبَيْتُ كَبِيرٌ}."}]},

        {"title": "Correct the phrase (Madinah lesson 5)", "fields": [PICK], "rows": [
            {"s": "Fix: بِنْتُ حَامِدٌ", "ans": {"pick": "a"}, "opts": {"pick": o("بِنْتُ حَامِدٍ", "بِنْتٌ حَامِدٍ", "الْبِنْتُ حَامِدٍ")},
             "why": "The owner takes kasra tanween: {بِنْتُ حَامِدٍ}."},
            {"s": "Fix: اِسْمُ الْوَلَدَ", "ans": {"pick": "c"}, "opts": {"pick": o("اِسْمٌ الْوَلَدِ", "الِاسْمُ الْوَلَدِ", "اِسْمُ الْوَلَدِ")},
             "why": "The owner takes kasra, not fatha: {اِسْمُ الْوَلَدِ}."},
            {"s": "Fix: بَابٌ السَّيَّارَةِ", "ans": {"pick": "b"}, "opts": {"pick": o("الْبَابُ السَّيَّارَةِ", "بَابُ السَّيَّارَةِ", "بَابُ السَّيَّارَةُ")},
             "why": "No tanween on the muḍāf: {بَابُ السَّيَّارَةِ}."},
            {"s": "Fix: الرَّسُولُ اللهِ", "ans": {"pick": "a"}, "opts": {"pick": o("رَسُولُ اللهِ", "رَسُولٌ اللهِ", "الرَّسُولُ اللهُ")},
             "why": "No {ال} on the muḍāf: {رَسُولُ اللهِ}."},
            {"s": "Fix: اِبْنُ الْمُدَرِّسٍ", "ans": {"pick": "b"}, "opts": {"pick": o("اِبْنٌ الْمُدَرِّسِ", "اِبْنُ الْمُدَرِّسِ", "اِبْنُ الْمُدَرِّسُ")},
             "why": "An owner with {ال} takes a single kasra: {اِبْنُ الْمُدَرِّسِ}."}]},

        {"title": "Muḍāf, owner or neither? Tap each word.",
         "prompt": "اِبْنُ الْمُدَرِّسِ طَبِيبٌ وَابْنُ الْإِمَامِ تَاجِرٌ.",
         "en": "The teacher's son is a doctor and the imam's son is a merchant.",
         "fields": [ROLE], "rows": [
            {"s": "اِبْنُ", "ans": {"role": "mudaf"}, "why": "No {ال}, no tanween, followed by its owner."},
            {"s": "الْمُدَرِّسِ", "ans": {"role": "owner"}, "why": "Kasra: 'the teacher's'."},
            {"s": "طَبِيبٌ", "ans": {"role": "none"}, "why": "The Information: 'is a doctor'."},
            {"s": "وَابْنُ", "ans": {"role": "mudaf"}, "why": "A second iḍāfa. After {وَ} the i- drops: wa-bnu."},
            {"s": "الْإِمَامِ", "ans": {"role": "owner"}, "why": "Kasra: 'the imam's'."},
            {"s": "تَاجِرٌ", "ans": {"role": "none"}, "why": "The Information: 'is a merchant'."}]},

        {"title": "Find the owner, if there is one", "fields": [OWN], "rows": [
            {"s": "بَابُ الْمَدْرَسَةِ مُغْلَقٌ", "ans": {"owner": "b"}, "opts": {"owner": o("بَابُ", "الْمَدْرَسَةِ", "مُغْلَقٌ", "No owner")},
             "why": "'The school door is closed.' {الْمَدْرَسَةِ} has kasra."},
            {"s": "الْوَلَدُ الصَّغِيرُ", "ans": {"owner": "c"}, "opts": {"owner": o("الْوَلَدُ", "الصَّغِيرُ", "No owner")},
             "why": "Both have {ال} and damma: an adjective phrase."},
            {"s": "عَمُّ الطَّالِبِ غَنِيٌّ", "ans": {"owner": "b"}, "opts": {"owner": o("عَمُّ", "الطَّالِبِ", "غَنِيٌّ", "No owner")},
             "why": "'The student's uncle is rich.' {الطَّالِبِ} has kasra."},
            {"s": "الْحَقِيبَةُ الثَّقِيلَةُ", "ans": {"owner": "c"}, "opts": {"owner": o("الْحَقِيبَةُ", "الثَّقِيلَةُ", "No owner")},
             "why": "Both have {ال} and damma: 'the heavy bag'."},
            {"s": "سَيَّارَةُ عَبَّاسٍ", "ans": {"owner": "b"}, "opts": {"owner": o("سَيَّارَةُ", "عَبَّاسٍ", "No owner")},
             "why": "'Abbas's car'. {عَبَّاسٍ} has kasra tanween."},
            {"s": "الْكِتَابُ جَدِيدٌ", "ans": {"owner": "c"}, "opts": {"owner": o("الْكِتَابُ", "جَدِيدٌ", "No owner")},
             "why": "A sentence: 'The book is new.'"}]},

        {"title": "What does it mean?", "fields": [MEAN], "rows": [
            {"s": "الْمُدَرِّسُ الْجَدِيدُ", "ans": {"mean": "b"}, "opts": {"mean": o("The teacher is new.", "the new teacher", "the teacher of the new one")},
             "why": "Both have {ال}: an adjective phrase."},
            {"s": "الْمُدَرِّسُ جَدِيدٌ", "ans": {"mean": "a"}, "opts": {"mean": o("The teacher is new.", "the new teacher", "a new teacher")},
             "why": "{ال} then tanween: a sentence."},
            {"s": "بَيْتُ الْمُدَرِّسِ جَدِيدٌ", "ans": {"mean": "c"}, "opts": {"mean": o("the teacher's new house", "The house is the new teacher's.", "The teacher's house is new.")},
             "why": "An iḍāfa, then the Information {جَدِيدٌ} with tanween."},
            {"s": "خَالُ حَامِدٍ فَقِيرٌ", "ans": {"mean": "a"}, "opts": {"mean": o("Hamid's (maternal) uncle is poor.", "Hamid's poor (maternal) uncle", "The uncle is poor Hamid.")},
             "why": "{خَالُ حَامِدٍ} is an iḍāfa. {فَقِيرٌ} with tanween is the Information."}]},
    ],
}
