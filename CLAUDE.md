# Notes for Claude sessions working on this repo

This is the course site for an Arabic grammar (naḥw) class taught to English speakers. The teacher adds lessons over time, usually by asking Claude to write them.

## Ground rules
- `content/` is the source of truth. Never hand-edit `dist/`; it is rebuilt by `python3 tools/build_site.py`.
- Every Arabic string is fully vowelled, including the last letter. Correct iʿrāb in examples and answer keys matters more than anything else in this repo. Get a second, independent check of new Arabic content before committing it.
- Keep the teaching order:
  - Stage 0: foundations.
  - Stage 1: nominal sentence, rafʿ and jarr.
  - Stage 2: naṣb with fatha, past and order verbs only.
  - Stage 3: fixed words (pronouns, pointing words, relatives, question words, past and order verbs incl. مَا "did not", particles).
  - Stage 4: kinds of nouns (dual, sound plurals, broken plurals, diptotes, the five nouns, hidden vowel): classification and shapes only.
  - Stage 5: nouns in rafʿ (topic/information, doer, doer stand-in, kāna's noun, inna's information, followers) with all signs.
  - Stage 6: nouns in jarr (preposition, iḍāfa, followers, diptote fatha).
  - Stage 7: nouns in naṣb (object, verb's own noun, purpose, time/place, together with, state, specifier, exception, vocative, inna's noun, kāna's information).
  - Stage 8: the present verb (rafʿ, naṣb, jazm, five verbs, condition, weak endings, fixed forms).
  - Don't use forms a stage hasn't taught yet. Present verbs appear only from Stage 8 on. Rules per stage: content/stage<N>/SPEC.md; Stages 5–8 also follow content/STAGES_5_8_SPEC.md (shared option lists: copy them exactly).
- Colours are fixed across the course (see `content/stage0/SPEC.md`):
  - Topic = gold, Information = red, after a preposition = green, owner = purple, adjective = grey, after وَ = blue.
  - Verb = navy, doer = orange, object = pink, purpose = teal, time/place = brown, state = olive.
- Students' saved results are keyed by lesson id + set id + card index. Never rename lesson ids or reorder existing cards; append instead.
- Writing style for students: plain, short sentences, no em-dashes.

## Every stage ends with a class exercise, then a quiz
The last two lessons of every stage are a class exercise (review of the whole stage, done together in class) and then the stage quiz.
- Unit-file stages (`content/stage<N>/`): a unit with `"kind": "exercise"` (homework may be `[]`) followed by one with `"kind": "quiz"`; give them the two highest `order` numbers.
- Stages built in `course.py`: list the exercise id and then the quiz id last in the `order` list at the end of `stage12()` (or the stage's own builder).
- A stage plan for the course: 0 foundations · 1 rafʿ and jarr · 2 naṣb · 3 fixed words (مَبْنِيَّات) · 4 kinds of nouns · 5 marfūʿāt · 6 majrūrāt · 7 manṣūbāt · 8 the present verb. `STAGES` in `site/app.js` lists them; a stage appears on the home page once it has a lesson.
- Spelling: ال may be written with or without sukūn on the ل (both are correct); no need to add it.

## Adding a unit like Stage 0
Write `content/stage0/u<N>_<slug>.py` following `content/stage0/SPEC.md`, run `python3 content/stage0/validate.py <file>` until it prints OK, then `python3 tools/build_site.py`.
Unit files in any `content/stage<N>/` folder are picked up automatically (they need `"id": "s<N>-..."` and an `order`); add a `stage<N>()` call in `tools/build_site.py` for a new folder.
For a lesson in a later stage, add a builder function to `content/course.py`, following `stage12()`. Use either iʿrāb cards (fields `end` + `job`) or choice cards, and give the lesson `stage` 1, 2, 3 and so on. The home page and tracking sheet take their stage list from `STAGES` in `site/app.js`.

## Checks before committing
1. `python3 tools/build_site.py` succeeds (it validates every Stage 0 unit).
2. Serve `dist/` and click through the new cards: every row has exactly one correct option, and Check marks a fully correct answer as correct.
3. If `supabase/schema.sql` changed, it must stay re-runnable, and the access rules must still keep students to their own rows.
