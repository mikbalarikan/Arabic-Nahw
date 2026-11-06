# Stage 4 · Kinds of nouns (أَقْسَامُ الأَسْمَاءِ): writing rules

Stage 4 uses the SAME file format as Stages 0 and 3. Read /home/claude/arabic-nahw/content/stage0/SPEC.md for the
data format (UNIT dict, note blocks, cards, fields, rows, opts, colours, {Arabic} markup) and
/home/claude/arabic-nahw/content/stage3/SPEC.md for how Stage 3 was written. The rules below replace the scope
rules of those files where they differ. Writing ال with or without sukūn on the ل is both fine.

## Where Stage 4 sits
Students know: the marks; ism/fiʿl/ḥarf; gender; maʿrifa/nakira; adjective and iḍāfa; the four cases;
the nominal sentence (Topic + Information, rafʿ); jarr after a preposition and of the owner; adjective/وَ copy;
the verb sentence with past and order verbs (doer rafʿ; object, purpose, time/place, state in naṣb by fatha);
and all the main fixed words (pronouns, pointing words, relatives, question words, past/order verb forms,
negative مَا, particles), including the idea of a fixed word's "place".
So far every noun they met took the ORIGINAL signs (العَلَامَاتُ الأَصْلِيَّةُ): damma for rafʿ, fatha for naṣb, kasra for jarr.

After Stage 4 come Stage 5 (nouns in rafʿ), 6 (jarr), 7 (naṣb): there each group's exact signs are taught in detail.

## Stage 4's goal
Students learn to CLASSIFY nouns by how they behave in iʿrāb, and to FORM the groups:
singular (مُفْرَدٌ), dual (مُثَنًّى), sound masculine plural (جَمْعُ مُذَكَّرٍ سَالِمٌ), sound feminine plural
(جَمْعُ مُؤَنَّثٍ سَالِمٌ), broken plural (جَمْعُ تَكْسِيرٍ), diptote (المَمْنُوعُ مِنَ الصَّرْفِ), the five nouns (الأَسْمَاءُ الخَمْسَةُ),
and nouns whose vowel is hidden (المَقْصُورُ، المَنْقُوصُ، and the noun with ـي "my"; المَمْدُودُ for contrast).
Key idea for the whole stage: some groups show iʿrāb with "branch signs" (عَلَامَاتٌ فَرْعِيَّةٌ: letters, or a
different vowel) instead of the original signs. A hidden vowel (maqṣūr, manqūṣ, noun + ـي) is NOT a branch sign:
it is the original sign, only hidden (مُقَدَّرَةٌ). Say "original, but hidden". Stage 4 shows WHICH words are in each group
and the SHAPES each group has, as a preview table; it does not drill which shape goes with which case.
Cards therefore ask: which group is this word in? what is its singular / dual / plural? is this a real dual or
plural or only looks like one? which noun can take tanween? which shape belongs to this group?
Cards may show a group's shapes (e.g. مُسْلِمُونَ / مُسْلِمِينَ) but must not ask the student to choose a shape
for a case. Exception: the dictionary (rafʿ) form is fine to ask for (the plural of مُعَلِّمٌ is مُعَلِّمُونَ).

## Scope rules for Stage 4
- Every Arabic word fully vowelled, including the last letter.
- In scope as items: duals, sound plurals, broken plurals, diptotes, the five nouns, maqṣūr/manqūṣ/mamdūd.
- Example SENTENCES stay simple and use only what students know: nominal sentences and past/order verbs;
  no present-tense verbs. If a sentence contains a dual, sound plural, five noun or diptote, prefer it in rafʿ
  (its dictionary shape), or say clearly that its other shape comes in Stage 6/7.
- Use common, correct vocabulary (Madinah Book 1 words where possible; extraction files are listed in stage0/SPEC.md).
  Plurals must be the standard ones: كِتَابٌ → كُتُبٌ، بَيْتٌ → بُيُوتٌ، قَلَمٌ → أَقْلَامٌ، طَالِبٌ → طُلَّابٌ، رَجُلٌ → رِجَالٌ، وَلَدٌ → أَوْلَادٌ، مَسْجِدٌ → مَسَاجِدُ،
  مِفْتَاحٌ → مَفَاتِيحُ، صَدِيقٌ → أَصْدِقَاءُ، مُدَرِّسٌ → مُدَرِّسُونَ، مُسْلِمٌ → مُسْلِمُونَ، مُهَنْدِسٌ → مُهَنْدِسُونَ، مُدَرِّسَةٌ → مُدَرِّسَاتٌ، سَيَّارَةٌ → سَيَّارَاتٌ.
  If you are not sure of a plural, don't use the word.
- Avoid words whose classification is disputed or advanced (mulḥaq forms like عِشْرُونَ، أُولُو، بَنُونَ, nouns with two
  common plurals where only one is offered, plurals of plurals). Keep traps fair and standard
  (e.g. أَصْوَاتٌ / أَبْيَاتٌ / أَوْقَاتٌ end in ـات but are broken plurals; إِنْسَانٌ / عُثْمَانُ end in ـان but are not duals;
  مِسْكِينٌ ends in ـين but is singular).
- Writing style: plain, short sentences for beginners, no em-dashes, no "not X but Y", no filler.

## Ids, files, counts
Files in /home/claude/arabic-nahw/content/stage4/ as u<N>_<slug>.py, "id": "s4-<slug>", "order": N.
Units 1–8: notes 5–8 sections (hero first, summary at the end; include a table for each group), 6 practice cards,
6 homework cards (different items, a little harder), 3–6 rows per card.
Unit 9 is the class exercise ("kind": "exercise", order 9, 10 practice cards, "homework": []).
Unit 10 is the stage quiz ("kind": "quiz", order 10, 8 practice cards + 6 homework cards).
Validate each file: python3 /home/claude/arabic-nahw/content/stage0/validate.py <file>  (must print OK).

## Colours for Stage 4 (use consistently across all units)
singular = grey, dual = teal, sound masculine plural = blue, sound feminine plural = pink, broken plural = purple,
diptote = orange, five nouns = gold, hidden vowel (maqṣūr / manqūṣ / ـي) = brown, mamdūd = olive.
Original signs = green, branch signs = red.
