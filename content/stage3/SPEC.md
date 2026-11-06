# Stage 3 · Fixed words (مَبْنِيَّاتٌ): writing rules

Stage 3 uses the SAME file format as Stage 0. Read /home/claude/arabic-nahw/content/stage0/SPEC.md first for the
data format (UNIT dict, note blocks, cards, fields, rows, opts, colours, {Arabic} markup), then the rules below,
which replace the Stage 0 scope rules where they differ.

## Where Stage 3 sits in the course
Students have finished:
- Stage 0: marks, ism/fiʿl/ḥarf, gender, maʿrifa/nakira, sun/moon letters, adjective and iḍāfa, what iʿrāb is,
  fixed (مَبْنِيٌّ) vs flexible (مُعْرَبٌ).
- Stage 1: nominal sentence: Topic مُبْتَدَأٌ + Information خَبَرٌ (rafʿ), jarr after a preposition, jarr of the owner
  (مُضَافٌ إِلَيْهِ), adjectives and words after وَ copy the word they follow.
- Stage 2: the verb sentence with past and order verbs: doer فَاعِلٌ (rafʿ), and naṣb by fatha for
  object مَفْعُولٌ بِهِ, purpose مَفْعُولٌ لِأَجْلِهِ, time/place مَفْعُولٌ فِيهِ, state حَالٌ.
After Stage 3 comes Stage 4 (kinds of nouns: singular, dual, sound plurals, diptotes, the five nouns), then
marfūʿāt, majrūrāt, manṣūbāt, and the iʿrāb of the present verb.

Stage 3's goal: students MEMORISE the main groups of fixed words, so that in every later lesson the fixed parts
of a sentence are instantly clear and their vocabulary grows. Teach each group as a table to learn, with meaning,
then practise recognising, choosing and using the forms.

## Key idea to teach (unit 1, then reuse)
A fixed word never changes its ending, but it still has a job in the sentence. Its job gives it a "place" (مَحَلٌّ):
  هُوَ طَالِبٌ: {هُوَ} is the Topic, fixed, "in the place of rafʿ" (فِي مَحَلِّ رَفْعٍ).
  كِتَابُهُ جَدِيدٌ: {ـهُ} is the owner, fixed, in the place of jarr (فِي مَحَلِّ جَرٍّ).
  رَأَيْتُهُ / ضَرَبَهُ-type: an attached pronoun as object is in the place of naṣb (فِي مَحَلِّ نَصْبٍ).
Use this sparingly but consistently: cards may ask "job" and "place" (rafʿ / naṣb / jarr) of a fixed word.

## Scope rules for Stage 3
- Every Arabic word fully vowelled, including the last letter. Spelling style as in Stages 1–2: ال without sukūn on
  the ل is fine (الكِتَابُ), but be consistent inside one unit.
- Fixed words themselves may be dual or plural in meaning (أَنْتُمَا، هُمْ، هَؤُلَاءِ، الَّذِينَ، كَتَبُوا، اُكْتُبُوا).
  That is the point of the stage. Their FORM is fixed and is taught as vocabulary.
- Nouns (muʿrab words) in examples stay simple: singular nouns with normal endings. Where a plural fixed word
  needs a plural noun (هَؤُلَاءِ طُلَّابٌ), use only BROKEN plurals that take normal endings: طُلَّابٌ، رِجَالٌ، أَوْلَادٌ، كُتُبٌ،
  أَقْلَامٌ، بُيُوتٌ، دُرُوسٌ، أَصْدِقَاءُ is a diptote, avoid it. Never duals of nouns (كِتَابَانِ), never sound plurals
  (مُسْلِمُونَ، مُسْلِمَاتٌ), never the five nouns (أَبُوكَ), never diptotes in jarr, no present-tense verbs.
- Things that are NOT fixed and must be flagged as exceptions, not taught as fixed: هَذَانِ / هَاتَانِ and اللَّذَانِ /
  اللَّتَانِ (they change for case: Stage 4), أَيٌّ (question word that is muʿrab), the present verb.
- Separate naṣb pronouns (إِيَّاكَ...) are out of scope. Inna and her sisters are out of scope (a later stage).
- Verbs: past verb (all 14 persons) and order verb (5 forms: اُكْتُبْ، اُكْتُبِي، اُكْتُبَا، اُكْتُبُوا، اُكْتُبْنَ) are in scope as fixed
  forms. Use sound, regular verbs for tables (كَتَبَ، ذَهَبَ، جَلَسَ، فَتَحَ، دَرَسَ، خَرَجَ). Avoid weak verbs (قَالَ، دَعَا، رَمَى)
  in tables; they are fine as vocabulary in a sentence only in their 3rd-person forms if needed.
- Prefer vocabulary from Madinah Book 1 lessons 1–5 (extraction files listed in stage0/SPEC.md).
- Writing style: plain, short sentences for beginners, no em-dashes, no "not X but Y", no filler.

## Ids and files
Files go in /home/claude/arabic-nahw/content/stage3/ as u<N>_<slug>.py with "id": "s3-<slug>" and "order": N.
Notes: hero first, a summary box at the end, one memorisation table per group ("table" block), examples.
Practice: 6 cards. Homework: 6 cards with different items, a little harder. 3–6 rows per card.
Validate: python3 /home/claude/arabic-nahw/content/stage0/validate.py <file>  (must print OK).

## Colours for Stage 3 (use consistently)
pronoun = blue, demonstrative = teal, relative = purple, question ism = gold, ḥarf = grey, past verb = navy,
order verb = brown, place of rafʿ = red, place of naṣb = pink, place of jarr = green. Not-fixed exception = orange.
