SM = {"key": "kind", "label": "Letter", "options": [
    {"k": "sun", "label": "Sun · شَمْسِيَّةٌ", "color": "gold"},
    {"k": "moon", "label": "Moon · قَمَرِيَّةٌ", "color": "navy"}]}

SHADDA = {"key": "shadda", "label": "Shadda?", "options": [
    {"k": "yes", "label": "Yes, shadda (ل silent)", "color": "orange"},
    {"k": "no", "label": "No, sukūn on ل", "color": "navy"}]}

SAY = {"key": "say", "label": "Pronunciation", "options": []}
PICK = {"key": "pick", "label": "Correct spelling", "options": []}


def o(*labels):
    return [{"k": k, "label": l} for k, l in zip("abc", labels)]


UNIT = {
    "id": "s0-sunmoon",
    "order": 5,
    "title": "Sun and moon letters",
    "ar": "الْحُرُوفُ الشَّمْسِيَّةُ وَالْقَمَرِيَّةُ",
    "blurb": "Why we say al-qamaru but ash-shamsu, and when the a- of ال drops.",
    "notes": [
        {"t": "hero", "eyebrow": "STAGE 0 · UNIT 5", "title": "One spelling, two sounds",
         "text": "{ال} is always written the same way. How you say it depends on the letter that comes next.",
         "wm": "الشَّمْسُ وَالْقَمَرُ"},

        {"t": "h2", "text": "Moon letters: the ل is heard"},
        {"t": "p", "text": "Before a moon letter you say the {ل} clearly. It carries a sukūn."},
        {"t": "words", "items": [
            {"ar": "الْقَمَرُ", "label": "al-qamaru", "sub": "the moon", "color": "navy"},
            {"ar": "الْبَابُ", "label": "al-bābu", "sub": "the door", "color": "navy"},
            {"ar": "الْكَلْبُ", "label": "al-kalbu", "sub": "the dog", "color": "navy"},
            {"ar": "الْمَسْجِدُ", "label": "al-masjidu", "sub": "the mosque", "color": "navy"}]},
        {"t": "rule", "color": "navy", "title": "Moon letter",
         "text": "The {ل} is pronounced and has a sukūn: {الْقَمَرُ} al-qamaru."},

        {"t": "h2", "text": "Sun letters: the ل is silent"},
        {"t": "p", "text": "Before a sun letter the {ل} is written but not said. The next letter is doubled instead, so it takes a shadda."},
        {"t": "words", "items": [
            {"ar": "الشَّمْسُ", "label": "ash-shamsu", "sub": "the sun", "color": "gold"},
            {"ar": "الرَّجُلُ", "label": "ar-rajulu", "sub": "the man", "color": "gold"},
            {"ar": "النَّجْمُ", "label": "an-najmu", "sub": "the star", "color": "gold"},
            {"ar": "الدِّيكُ", "label": "ad-dīku", "sub": "the rooster", "color": "gold"}]},
        {"t": "rule", "color": "gold", "title": "Sun letter",
         "text": "The {ل} is silent and has no mark. The next letter takes a shadda: {الشَّمْسُ} ash-shamsu."},
        {"t": "tip", "text": "Look for the shadda. A shadda on the letter right after {ال} means a sun letter."},

        {"t": "h2", "text": "The 14 and 14"},
        {"t": "p", "text": "The alphabet splits exactly in half. This is the table from Madinah lesson 3."},
        {"t": "table", "head": ["Moon letter", "Example", "Sun letter", "Example"], "rows": [
            ["أ", "الْأَبُ", "ت", "التَّاجِرُ"],
            ["ب", "الْبَابُ", "ث", "الثَّوْبُ"],
            ["ج", "الْجَنَّةُ", "د", "الدِّيكُ"],
            ["ح", "الْحِمَارُ", "ذ", "الذَّهَبُ"],
            ["خ", "الْخُبْزُ", "ر", "الرَّجُلُ"],
            ["ع", "الْعَيْنُ", "ز", "الزَّهْرَةُ"],
            ["غ", "الْغَدَاءُ", "س", "السَّمَكُ"],
            ["ف", "الْفَمُ", "ش", "الشَّمْسُ"],
            ["ق", "الْقَمَرُ", "ص", "الصَّدْرُ"],
            ["ك", "الْكَلْبُ", "ض", "الضَّيْفُ"],
            ["م", "الْمَاءُ", "ط", "الطَّالِبُ"],
            ["و", "الْوَلَدُ", "ظ", "الظُّهْرُ"],
            ["ه", "الْهَوَاءُ", "ل", "اللَّحْمُ"],
            ["ي", "الْيَدُ", "ن", "النَّجْمُ"]]},

        {"t": "h2", "text": "How to remember the sun letters"},
        {"t": "p", "text": "Say each sun letter and feel your tongue. They are all made with the front of the tongue, at the teeth or just behind them: {ت ث د ذ ر ز س ش ص ض ط ظ ل ن}. That is where {ل} is made too, so the {ل} melts into them."},
        {"t": "p", "text": "Moon letters are made with the lips ({ب م و ف}) or further back in the mouth ({ق ك ج خ غ ع ح ه أ ي}). The {ل} does not melt into them, so you hear it."},
        {"t": "tip", "text": "Careful with {ج}. Many English speakers say it like English 'j', near the front. It is a moon letter: {الْجَمَلُ} al-jamalu."},
        {"t": "examples", "items": [
            {"ar": "طِبْ ثُمَّ صِلْ رُحْمًا تَفُزْ ضِفْ ذَا نِعَمْ ... دَعْ سُوءَ ظَنٍّ زُرْ شَرِيفًا لِلْكَرَمْ",
             "en": "Optional rhyme from Tuḥfat al-Aṭfāl: the first letter of each word is a sun letter.",
             "note": "{ط ث ص ر ت ض ذ ن د س ظ ز ش ل}: 14 words, 14 sun letters. You do not need the meaning."}]},

        {"t": "h2", "text": "The spelling never changes"},
        {"t": "p", "text": "You always write {ال}, with both letters. Only the marks change: a sukūn on {ل} for a moon letter, a shadda on the next letter for a sun letter."},
        {"t": "examples", "items": [
            {"ar": "الشَّمْسُ وَالْقَمَرُ فِي السَّمَاءِ.", "en": "The sun and the moon are in the sky.",
             "note": "The {ل} is written in all three words. You hear it only in {الْقَمَرُ}."}]},
        {"t": "tip", "text": "Do not drop the {ل} in writing ({اشَّمْسُ} is wrong), and do not put a sukūn on it before a sun letter ({الْشَّمْسُ} is wrong)."},

        {"t": "h2", "text": "Hamzat al-waṣl: the a- drops"},
        {"t": "p", "text": "The a- of {ال} is said only when the word starts your speech. After {وَ} or any other word, the a- drops and you go straight to the {ل} or the doubled letter. It is still written."},
        {"t": "table", "head": ["Written", "Said", "English"], "rows": [
            ["الْبَيْتُ", "al-baytu", "the house (start of speech)"],
            ["وَالْبَيْتُ", "wa-l-baytu", "and the house"],
            ["وَالرَّجُلُ", "wa-r-rajulu", "and the man"],
            ["مِنَ الْبَيْتِ", "mina l-bayti", "from the house"],
            ["فِي الْمَسْجِدِ", "fi l-masjidi", "in the mosque"]]},
        {"t": "examples", "items": [
            {"ar": "الْكِتَابُ جَدِيدٌ وَالْقَلَمُ قَدِيمٌ.", "en": "The book is new and the pen is old.",
             "note": "al-kitābu jadīdun wa-l-qalamu qadīmun"},
            {"ar": "الْوَلَدُ جَالِسٌ وَالْمُدَرِّسُ وَاقِفٌ.", "en": "The boy is sitting and the teacher is standing.",
             "note": "al-waladu jālisun wa-l-mudarrisu wāqifun"}]},
        {"t": "tip", "text": "{فِي} becomes short before {ال}: fi l-masjidi (Madinah lesson 4)."},

        {"t": "summary", "title": "In four lines", "items": [
            "Moon letter: the {ل} is heard, with a sukūn: {الْقَمَرُ} al-qamaru.",
            "Sun letter: the {ل} is silent, the next letter takes a shadda: {الشَّمْسُ} ash-shamsu.",
            "14 sun letters, all made with the front of the tongue. The spelling {ال} never changes.",
            "After {وَ} or another word, the a- of {ال} drops: {وَالْبَيْتُ} wa-l-baytu."]},
    ],

    "practice": [
        {"title": "Sun or moon?", "fields": [SM], "rows": [
            {"s": "الْبَابُ", "gloss": "the door", "ans": {"kind": "moon"}, "why": "{ب} is a moon letter: the {ل} has a sukūn."},
            {"s": "الشَّمْسُ", "gloss": "the sun", "ans": {"kind": "sun"}, "why": "{ش} is a sun letter: look at the shadda."},
            {"s": "الْقَلَمُ", "gloss": "the pen", "ans": {"kind": "moon"}, "why": "{ق} is a moon letter: al-qalamu."},
            {"s": "الطَّالِبُ", "gloss": "the student", "ans": {"kind": "sun"}, "why": "{ط} is a sun letter: aṭ-ṭālibu."},
            {"s": "الدُّكَّانُ", "gloss": "the shop", "ans": {"kind": "sun"}, "why": "{د} is a sun letter: ad-dukkānu."},
            {"s": "الْمَسْجِدُ", "gloss": "the mosque", "ans": {"kind": "moon"}, "why": "{م} is a moon letter: al-masjidu."}]},

        {"title": "Which pronunciation is right?", "fields": [SAY], "rows": [
            {"s": "الْقَمَرُ", "ans": {"say": "a"}, "opts": {"say": o("al-qamaru", "aq-qamaru", "al-qamarun")},
             "why": "Moon letter: the {ل} is heard. No tanween after {ال}."},
            {"s": "الشَّمْسُ", "ans": {"say": "b"}, "opts": {"say": o("al-shamsu", "ash-shamsu", "a-shamsu")},
             "why": "Sun letter: the {ل} is silent and {ش} is doubled."},
            {"s": "الرَّجُلُ", "ans": {"say": "c"}, "opts": {"say": o("al-rajulu", "a-rajulu", "ar-rajulu")},
             "why": "Sun letter: ar-rajulu, with a double r."},
            {"s": "الْكِتَابُ", "ans": {"say": "a"}, "opts": {"say": o("al-kitābu", "ak-kitābu", "al-kitābun")},
             "why": "Moon letter: the {ل} is heard."},
            {"s": "النَّجْمُ", "ans": {"say": "b"}, "opts": {"say": o("al-najmu", "an-najmu", "an-najmun")},
             "why": "Sun letter: an-najmu."},
            {"s": "الْوَلَدُ", "ans": {"say": "a"}, "opts": {"say": o("al-waladu", "aw-waladu", "a-waladu")},
             "why": "{و} is a moon letter: al-waladu."}]},

        {"title": "Add ال: does the next letter take shadda?", "fields": [SHADDA], "rows": [
            {"s": "ال + بَيْتٌ", "ans": {"shadda": "no"}, "why": "Moon letter: {الْبَيْتُ} al-baytu."},
            {"s": "ال + دِيكٌ", "ans": {"shadda": "yes"}, "why": "Sun letter: {الدِّيكُ} ad-dīku."},
            {"s": "ال + سَرِيرٌ", "ans": {"shadda": "yes"}, "why": "Sun letter: {السَّرِيرُ} as-sarīru."},
            {"s": "ال + جَمَلٌ", "ans": {"shadda": "no"}, "why": "{ج} is a moon letter: {الْجَمَلُ} al-jamalu."},
            {"s": "ال + طَبِيبٌ", "ans": {"shadda": "yes"}, "why": "Sun letter: {الطَّبِيبُ} aṭ-ṭabību."},
            {"s": "ال + مِفْتَاحٌ", "ans": {"shadda": "no"}, "why": "Moon letter: {الْمِفْتَاحُ} al-miftāḥu."}]},

        {"title": "Sun or moon? Tap each word with ال.",
         "prompt": "الشَّمْسُ وَالْقَمَرُ فِي السَّمَاءِ.", "en": "The sun and the moon are in the sky.",
         "fields": [SM], "rows": [
            {"s": "الشَّمْسُ", "ans": {"kind": "sun"}, "why": "Shadda on {ش}: ash-shamsu."},
            {"s": "وَالْقَمَرُ", "ans": {"kind": "moon"}, "why": "Sukūn on {ل}: wa-l-qamaru."},
            {"s": "السَّمَاءِ", "ans": {"kind": "sun"}, "why": "Shadda on {س}: fi s-samāʾi."}]},

        {"title": "Which spelling is right?", "fields": [PICK], "rows": [
            {"s": "the sun", "ans": {"pick": "a"}, "opts": {"pick": o("الشَّمْسُ", "اشَّمْسُ", "الْشَّمْسُ")},
             "why": "Keep the {ل} in writing, with no sukūn: {الشَّمْسُ}."},
            {"s": "the man", "ans": {"pick": "c"}, "opts": {"pick": o("ارَّجُلُ", "الْرَّجُلُ", "الرَّجُلُ")},
             "why": "Write {ال}, then shadda on {ر}: {الرَّجُلُ}."},
            {"s": "the door", "ans": {"pick": "b"}, "opts": {"pick": o("البَّابُ", "الْبَابُ", "الْبَابٌ")},
             "why": "Moon letter: sukūn on {ل}, no shadda on {ب}, no tanween."},
            {"s": "the star", "ans": {"pick": "a"}, "opts": {"pick": o("النَّجْمُ", "انَّجْمُ", "الْنَجْمُ")},
             "why": "Sun letter: {ال} stays, {ن} takes shadda."}]},

        {"title": "After وَ: how do you say it?", "fields": [SAY], "rows": [
            {"s": "وَالْبَيْتُ", "ans": {"say": "b"}, "opts": {"say": o("wa-al-baytu", "wa-l-baytu", "wal-al-baytu")},
             "why": "After {وَ} the a- of {ال} drops: wa-l-baytu."},
            {"s": "وَالرَّجُلُ", "ans": {"say": "a"}, "opts": {"say": o("wa-r-rajulu", "wa-l-rajulu", "wa-ar-rajulu")},
             "why": "The a- drops and the {ل} stays silent: wa-r-rajulu."},
            {"s": "الْكِتَابُ (start of speech)", "ans": {"say": "c"}, "opts": {"say": o("l-kitābu", "ul-kitābu", "al-kitābu")},
             "why": "At the start of speech you say the a-: al-kitābu."},
            {"s": "وَالْمُدَرِّسُ", "ans": {"say": "a"}, "opts": {"say": o("wa-l-mudarrisu", "wa-al-mudarrisu", "wa-m-mudarrisu")},
             "why": "Moon letter, after {وَ}: wa-l-mudarrisu."}]},
    ],

    "homework": [
        {"title": "Add ال: sun or moon?", "fields": [SM], "rows": [
            {"s": "نَجْمٌ", "gloss": "star", "ans": {"kind": "sun"}, "why": "{ن} is a sun letter: {النَّجْمُ}."},
            {"s": "قَمِيصٌ", "gloss": "shirt", "ans": {"kind": "moon"}, "why": "{ق} is a moon letter: {الْقَمِيصُ}."},
            {"s": "تَاجِرٌ", "gloss": "merchant", "ans": {"kind": "sun"}, "why": "{ت} is a sun letter: {التَّاجِرُ}."},
            {"s": "وَلَدٌ", "gloss": "boy", "ans": {"kind": "moon"}, "why": "{و} is a moon letter: {الْوَلَدُ}."},
            {"s": "لَبَنٌ", "gloss": "milk", "ans": {"kind": "sun"}, "why": "{ل} is a sun letter: {اللَّبَنُ} al-labanu, one long l."},
            {"s": "حِصَانٌ", "gloss": "horse", "ans": {"kind": "moon"}, "why": "{ح} is a moon letter: {الْحِصَانُ}."}]},

        {"title": "Sun or moon?", "fields": [SM], "rows": [
            {"s": "الصَّابُونُ", "gloss": "the soap", "ans": {"kind": "sun"}, "why": "{ص} is a sun letter: aṣ-ṣābūnu."},
            {"s": "الْفَجْرُ", "gloss": "dawn", "ans": {"kind": "moon"}, "why": "{ف} is a moon letter: al-fajru."},
            {"s": "الذَّهَبُ", "gloss": "the gold", "ans": {"kind": "sun"}, "why": "{ذ} is a sun letter: adh-dhahabu."},
            {"s": "الْجَامِعَةُ", "gloss": "the university", "ans": {"kind": "moon"}, "why": "{ج} is a moon letter: al-jāmiʿatu."},
            {"s": "الضَّيْفُ", "gloss": "the guest", "ans": {"kind": "sun"}, "why": "{ض} is a sun letter: aḍ-ḍayfu."},
            {"s": "الْيَدُ", "gloss": "the hand", "ans": {"kind": "moon"}, "why": "{ي} is a moon letter: al-yadu."}]},

        {"title": "Which pronunciation is right?", "fields": [SAY], "rows": [
            {"s": "الدَّفْتَرُ", "ans": {"say": "c"}, "opts": {"say": o("al-daftaru", "ad-daftarun", "ad-daftaru")},
             "why": "Sun letter, and no tanween after {ال}: ad-daftaru."},
            {"s": "الْجَمَلُ", "ans": {"say": "a"}, "opts": {"say": o("al-jamalu", "aj-jamalu", "a-jamalu")},
             "why": "{ج} is a moon letter: al-jamalu."},
            {"s": "السُّوقُ", "ans": {"say": "b"}, "opts": {"say": o("al-sūqu", "as-sūqu", "a-sūqu")},
             "why": "Sun letter: as-sūqu."},
            {"s": "الْعَمُّ", "ans": {"say": "a"}, "opts": {"say": o("al-ʿammu", "aʿ-ʿammu", "al-ʿammun")},
             "why": "{ع} is a moon letter. The shadda here is on {م}, part of the word itself."},
            {"s": "التُّفَّاحُ", "ans": {"say": "c"}, "opts": {"say": o("al-tuffāḥu", "a-tuffāḥu", "at-tuffāḥu")},
             "why": "Sun letter: at-tuffāḥu."},
            {"s": "الْخُبْزُ", "ans": {"say": "b"}, "opts": {"say": o("akh-khubzu", "al-khubzu", "al-khubzun")},
             "why": "{خ} is a moon letter: al-khubzu."}]},

        {"title": "Add ال: does the next letter take shadda?", "fields": [SHADDA], "rows": [
            {"s": "ال + زَهْرَةٌ", "ans": {"shadda": "yes"}, "why": "Sun letter: {الزَّهْرَةُ} az-zahratu."},
            {"s": "ال + غُرْفَةٌ", "ans": {"shadda": "no"}, "why": "Moon letter: {الْغُرْفَةُ} al-ghurfatu."},
            {"s": "ال + صَدِيقٌ", "ans": {"shadda": "yes"}, "why": "Sun letter: {الصَّدِيقُ} aṣ-ṣadīqu."},
            {"s": "ال + كَلْبٌ", "ans": {"shadda": "no"}, "why": "Moon letter: {الْكَلْبُ} al-kalbu."},
            {"s": "ال + ثَوْبٌ", "ans": {"shadda": "yes"}, "why": "Sun letter: {الثَّوْبُ} ath-thawbu."},
            {"s": "ال + فَصْلٌ", "ans": {"shadda": "no"}, "why": "Moon letter: {الْفَصْلُ} al-faṣlu."}]},

        {"title": "Sun or moon? Tap each word with ال.",
         "prompt": "التَّاجِرُ فِي السُّوقِ وَالْمُدِيرُ فِي الْمَدْرَسَةِ.", "en": "The merchant is in the market and the principal is in the school.",
         "fields": [SM], "rows": [
            {"s": "التَّاجِرُ", "ans": {"kind": "sun"}, "why": "Shadda on {ت}: at-tājiru."},
            {"s": "السُّوقِ", "ans": {"kind": "sun"}, "why": "Shadda on {س}: fi s-sūqi."},
            {"s": "وَالْمُدِيرُ", "ans": {"kind": "moon"}, "why": "Sukūn on {ل}: wa-l-mudīru."},
            {"s": "الْمَدْرَسَةِ", "ans": {"kind": "moon"}, "why": "Sukūn on {ل}: fi l-madrasati."}]},

        {"title": "Inside a sentence: how is it said?", "fields": [SAY], "rows": [
            {"s": "وَالْمَطْبَخُ", "ans": {"say": "a"}, "opts": {"say": o("wa-l-maṭbakhu", "wa-al-maṭbakhu", "wa-m-maṭbakhu")},
             "why": "Moon letter, and the a- drops after {وَ}."},
            {"s": "وَالسُّكَّرُ", "ans": {"say": "c"}, "opts": {"say": o("wa-l-sukkaru", "wa-as-sukkaru", "wa-s-sukkaru")},
             "why": "Sun letter, and the a- drops after {وَ}: wa-s-sukkaru."},
            {"s": "مِنَ الْبَيْتِ", "ans": {"say": "b"}, "opts": {"say": o("mina al-bayti", "mina l-bayti", "min al-baytu")},
             "why": "The a- drops after {مِنَ}: mina l-bayti."},
            {"s": "فِي الشَّارِعِ", "ans": {"say": "a"}, "opts": {"say": o("fi sh-shāriʿi", "fī al-shāriʿi", "fi l-shāriʿi")},
             "why": "Sun letter, and the a- drops: fi sh-shāriʿi."},
            {"s": "وَالرَّأْسُ", "ans": {"say": "b"}, "opts": {"say": o("wa-l-raʾsu", "wa-r-raʾsu", "wa-ar-raʾsu")},
             "why": "Sun letter, and the a- drops: wa-r-raʾsu."}]},
    ],
}
