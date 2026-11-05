# Notes for Claude sessions working on this repo

This is the course site for an Arabic grammar (naḥw) class taught to English speakers. The teacher adds lessons over time, usually by asking Claude to write them.

## Ground rules
- `content/` is the source of truth. Never hand-edit `dist/`; it is rebuilt by `python3 tools/build_site.py`.
- Every Arabic string is fully vowelled, including the last letter. Correct iʿrāb in examples and answer keys matters more than anything else in this repo. Get a second, independent check of new Arabic content before committing it.
- Keep the teaching order:
  - Stage 0: foundations.
  - Stage 1: nominal sentence, rafʿ and jarr.
  - Stage 2: naṣb with fatha, past and order verbs only.
  - Planned next: one chapter per group (dual, sound masculine plural, sound feminine plural, and so on).
  - Don't use forms a stage hasn't taught yet: present verbs, duals, plurals, diptotes in jarr, the five nouns.
- Colours are fixed across the course (see `content/stage0/SPEC.md`):
  - Topic = gold, Information = red, after a preposition = green, owner = purple, adjective = grey, after وَ = blue.
  - Verb = navy, doer = orange, object = pink, purpose = teal, time/place = brown, state = olive.
- Students' saved results are keyed by lesson id + set id + card index. Never rename lesson ids or reorder existing cards; append instead.
- Writing style for students: plain, short sentences, no em-dashes.

## Adding a unit like Stage 0
Write `content/stage0/u<N>_<slug>.py` following `content/stage0/SPEC.md`, run `python3 content/stage0/validate.py <file>` until it prints OK, then `python3 tools/build_site.py`.
Stage 0 files are picked up automatically (they need `"id": "s0-..."` and an `order`).
For a lesson in a later stage, add a builder function to `content/course.py`, following `stage12()`. Use either iʿrāb cards (fields `end` + `job`) or choice cards, and give the lesson `stage` 1, 2, 3 and so on. The home page shows stages 0–2; add a `stageSection` line in `site/app.js` for a new stage.

## Checks before committing
1. `python3 tools/build_site.py` succeeds (it validates every Stage 0 unit).
2. Serve `dist/` and click through the new cards: every row has exactly one correct option, and Check marks a fully correct answer as correct.
3. If `supabase/schema.sql` changed, it must stay re-runnable, and the access rules must still keep students to their own rows.
