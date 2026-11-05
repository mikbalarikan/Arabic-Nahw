# Stage 0 unit format (Iʿrāb Classroom)

Stage 0 is revision and catch-up for students who missed the first classes of an Arabic grammar (naḥw) course.
Students are English speakers. They also study the Madinah Arabic Reader Book 1 (lessons 1–5 done), so reuse
its vocabulary and sentence patterns wherever possible:
  /tmp/claude-0/-home-claude/e84f6610-cb59-54d3-8640-efa415bef314/scratchpad/madinah_L1-3.md
  /tmp/claude-0/-home-claude/e84f6610-cb59-54d3-8640-efa415bef314/scratchpad/madinah_L4-5.md
Read both files before writing.

After Stage 0 the course continues with Stage 1: the nominal sentence (Topic مُبْتَدَأ + Information خَبَر, both rafʿ),
jarr after a preposition (فِي، عَلَى، مِنْ، إِلَى), jarr of the owner in iḍāfa, and adjectives / words after وَ copying
the ending of the noun they follow. Stage 0 must give a newcomer everything Stage 1 assumes.

## Scope rules (strict)
- Every Arabic word fully vowelled, including the last letter (كِتَابٌ, الْكِتَابُ). Use the Madinah spelling style
  (ال written as الْ or ال is fine; be consistent within a unit). No tatweel except where showing a lone mark (ـَ).
- Nouns: singular only. No duals, no plurals (exception: none). No present-tense verbs. Past verbs only as examples
  of fiʿl (كَتَبَ، ذَهَبَ، خَرَجَ، جَلَسَ، دَخَلَ، قَرَأَ، فَتَحَ، شَرِبَ) — never ask for their iʿrāb.
- Avoid words whose endings break the simple rules: no diptote names in jarr (أَحْمَد، فَاطِمَة after a preposition
  or as owner), no words ending in ـى or ـي that hide the vowel (مُوسَى، الْقَاضِي) except كُرْسِيٌّ (shadda ي is fine),
  no five nouns (أَبُوكَ، أَخُو). Feminine names without tanween (فَاطِمَةُ، زَيْنَبُ، آمِنَةُ) are fine in rafʿ only.
- Terms (keep exactly): ism اِسْمٌ, fiʿl فِعْلٌ, ḥarf حَرْفٌ; masculine مُذَكَّرٌ, feminine مُؤَنَّثٌ; maʿrifa مَعْرِفَةٌ (definite),
  nakira نَكِرَةٌ (indefinite); sun letters الْحُرُوفُ الشَّمْسِيَّةُ, moon letters الْحُرُوفُ الْقَمَرِيَّةُ;
  adjective صِفَةٌ; iḍāfa إِضَافَةٌ, muḍāf مُضَافٌ, muḍāf ilayh مُضَافٌ إِلَيْهِ ("owner" in class); iʿrāb إِعْرَابٌ;
  fixed مَبْنِيٌّ, flexible مُعْرَبٌ; rafʿ رَفْعٌ, naṣb نَصْبٌ, jarr جَرٌّ, jazm جَزْمٌ; marks: fatha, damma, kasra, sukūn,
  shadda, tanween. Topic مُبْتَدَأٌ, Information خَبَرٌ.
- The class's core idea: role → form → sign. "Every word has a job in the sentence. The job gives it a colour,
  and the colour tells you its last vowel."
- Writing style: plain, short, direct sentences for beginners. No em-dashes, no "not X but Y" framing, no filler.
  English everywhere except the Arabic examples. Keep each explanation short; teach through examples.

## File format
Write one Python file per unit in /home/claude/quiz/stage0/, named u<N>_<slug>.py, defining a dict UNIT.
Inline Arabic inside English text goes in curly braces: "The {ال} makes a noun definite." (rendered as bold Arabic).
Never put braces around English.

UNIT = {
  "id": "s0-marks",            # ascii letters, digits, hyphens; starts with "s0-"
  "order": 1,                   # unit number in Stage 0
  "title": "Reading the marks", # short English name
  "ar": "الْحَرَكَاتُ",           # Arabic name of the unit, vowelled
  "blurb": "One sentence for the lesson tile.",
  "notes": [ ...blocks... ],    # the lesson page, 4–8 sections
  "practice": [ ...cards... ],  # 6 cards, done in class
  "homework": [ ...cards... ],  # 6 cards, different items from practice, a little harder
}

### Note blocks (each a dict with "t")
- {"t":"hero", "eyebrow":"STAGE 0 · UNIT 1", "title":"Short headline", "text":"One or two sentences.", "wm":"الْحَرَكَاتُ"}
  Exactly one, first.
- {"t":"h2", "text":"Section title"}            numbered automatically
- {"t":"p", "text":"Paragraph with {عربي}."}
- {"t":"rule", "color":"<color>", "title":"Rule title", "text":"The rule in one or two sentences."}
- {"t":"tip", "text":"A warning or tip."}
- {"t":"cols", "items":[{"color":"<color>", "title":"English", "ar":"عَرَبِيٌّ", "text":"short text with {عربي}"} , ...]}
     2–6 small coloured cards side by side (like a colour key)
- {"t":"words", "items":[{"ar":"كِتَابٌ", "label":"kitābun", "sub":"a book", "color":"<color>"}, ...]}
     a row of big word tiles; label/sub optional
- {"t":"examples", "items":[{"ar":"هَذَا كِتَابٌ.", "en":"This is a book.", "note":"optional short note with {عربي}"}]}
- {"t":"table", "head":["Col","Col"], "rows":[["cell with {عربي}", "cell"], ...]}  Arabic-only cells may be plain Arabic.
- {"t":"summary", "title":"In three questions", "items":["Line with {عربي}", "..."]}   teal box, use once at the end

<color> is one of: blue, pink, gold, navy, teal, green, red, purple, orange, brown, grey, olive.
Use colours consistently: in the whole Stage 0 use
  ism=blue, fiʿl=navy, ḥarf=grey; masculine=blue, feminine=pink; maʿrifa=teal, nakira=brown;
  sun=gold, moon=navy; adjective=grey (same as class), muḍāf ilayh/owner=purple, muḍāf=teal;
  rafʿ/damma=red, naṣb/fatha=pink, jarr/kasra=green, jazm/sukūn=navy, shadda=orange, tanween=olive;
  Topic=gold, Information=red (as in Stage 1).

### Cards
A card is one interactive exercise: a list of rows; for each row the student taps one option per field.
{
  "title": "Ism, fiʿl or ḥarf?",       # short English instruction shown on the card
  "prompt": "ذَهَبَ الطَّالِبُ إِلَى الْمَسْجِدِ",   # OPTIONAL: an Arabic sentence shown big above the rows
  "en": "The student went to the mosque.",       # OPTIONAL English translation of the prompt
  "fields": [                           # 1 or 2 fields; each row is answered in every field
     {"key":"kind", "label":"Kind", "options":[
        {"k":"ism",  "label":"Ism · اِسْمٌ",  "color":"blue"},
        {"k":"fil",  "label":"Fiʿl · فِعْلٌ", "color":"navy"},
        {"k":"harf", "label":"Ḥarf · حَرْفٌ", "color":"grey"}]}
  ],
  "rows": [
     {"s":"ذَهَبَ", "gloss":"went", "ans":{"kind":"fil"}, "why":"A past action: ذَهَبَ 'he went'."},
     ...
  ]
}
- 3–6 rows per card. "s" is the Arabic item (a word or a short phrase), "gloss" an optional English meaning,
  "ans" maps every field key to the correct option "k", "why" is the one-line reason shown in the answer key
  (use {عربي} for Arabic inside it).
- A row may replace a field's options for itself (for "which form is right?" items):
     {"s":"كِتَابٌ → the book", "ans":{"pick":"b"}, "opts":{"pick":[{"k":"a","label":"الْكِتَابٌ"},{"k":"b","label":"الْكِتَابُ"},{"k":"c","label":"كِتَابُ"}]}, "why":"..."}
  In that case the card's field still needs a key and label but its options may be []. Arabic labels are fine.
- Option keys are short ascii. Options may omit "color" (they render neutral).
- Mix card styles: whole-sentence word classification (with "prompt"), single-word lists, and "which is right?" rows.
- Make wrong options plausible (the common beginner mistakes), never trick questions.
- Homework must not repeat practice items.

## Check your work
Run:  python3 /home/claude/quiz/stage0/validate.py /home/claude/quiz/stage0/u<N>_<slug>.py
It must print OK. Then re-read every Arabic string once for vowels on every letter that needs one, especially the last letter.
