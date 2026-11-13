# "Question words" video (lesson id `s3-questions`): script format and narration rules

The video follows the lesson page of Stage 3, unit 5 (`content/stage3/u5_questions.py`, its `notes` blocks),
block by block, in order. The data is in `lesson.json` (made by `video/tools/export_s3_questions.py`; `blocks[i]`
is note block `i` with its source `src` and the site's own HTML). Format and timing work as in the Naṣb video
(`video/lessons/nasb/SCRIPT_SPEC.md`): a list of short **segments**, each one spoken clause plus the visual
**cues** that fire when it starts. The voice drives the clock. Nobody types a timestamp.

## Segment

```json
{ "id": "c01-table-04", "scene": "c01-table", "lang": "ar", "text": "مَنْ فِي الْغُرْفَةِ؟", "pause": 0.5, "cues": ["cell:1.3"] }
```

- `id`: unique, `<scene>-<two digits>` in order.
- `scene`: scene id (list below).
- `lang`: `en` (narration) or `ar` (Arabic read by the same TTS voice).
- `text`: what is spoken.
  - `ar`: ONLY Arabic exactly as written in the lesson source, cut at word boundaries: a whole question or
    answer from the table or an example (`مَنْ فِي الْغُرْفَةِ؟`, `مُحَمَّدٌ`, `نَعَمْ، هَذَا بَيْتٌ`), or a word / short
    phrase written in `{...}` in the notes (`مَنْ`, `مِنْ أَيْنَ`, `بِكَمْ`, `أَيُّ`). Keep a `؟` that the source
    writes right after the last word (it is part of the run in the source). Drop a final `.` (not Arabic).
    An example line with a question and an answer is read as two `ar` segments (question, then answer).
    Never invent Arabic, never change a vowel, never add or drop `ال`. Never put Arabic inside an `en` segment.
  - `en`: English. See the narration rules.
- `pause`: silence after the segment, in seconds. Default 0.25. 0.5–0.7 after a question the viewer should
  answer in their head, 0.4–0.6 around `ar` readings.
- `cues`: visual actions that start with this segment (may be empty).

## Scenes, in order, and their cues

| Scene id | Lesson block(s) | Shows | Cues |
|---|---|---|---|
| `hero` | 0 hero | Teal hero card: eyebrow, title "Asking questions", text, watermark مَنْ؟ | `title`, `sub` |
| `c01-title` | 1 h2, 2 p | "1 Question isms: the table to learn" + the p as grey sub-line | `title`, `sub` |
| `c01-table` | 3 table | The 7-row table: Word · Meaning · Question · Answer | `row:<n>` (n = 1..7: row n appears), `cell:<n>.<c>` (gold marker on cell c = 1..4 of row n while it is spoken; the previous marker goes) |
| `c01-rule` | 4 rule (gold) | "Learn the last vowel." | `show`, `hl:<phrase>` (gold marker sweeps over that exact phrase of the box; first match) |
| `c01-tips` | 5, 6, 7 tips | The three tip boxes, stacked | `tip:1`, `tip:2`, `tip:3`, `hl:<phrase>` |
| `c02-title` | 8 h2, 9 p | "2 Question ḥarfs: هَلْ and أَ" + the p as sub-line | `title`, `sub` |
| `c02-examples` | 10 examples | The 3 example lines (Arabic · English · note) | `ex:<n>` (n = 1..3: line n appears), `say:<n>` (gold frame on the Arabic of line n while it is read) |
| `c02-cols` | 11 cols | Two cards: Question ism (gold) · Question ḥarf (grey) | `col:1`, `col:2`, `hl:<phrase>` |
| `c02-tip` | 12 tip | "Never answer ..." tip | `show`, `hl:<phrase>` |
| `c03-title` | 13 h2, 14 p | "3 With a preposition" + sub-line | `title`, `sub` |
| `c03-examples` | 15 examples | 4 example lines | `ex:1`..`ex:4`, `say:<n>` |
| `c03-tip` | 16 tip | "Without a preposition ..." tip | `show`, `hl:<phrase>` |
| `c04-title` | 17 h2 | "4 Not fixed: أَيٌّ "which"" | `title` |
| `c04-rule` | 18 rule (orange) | "أَيٌّ takes endings." | `show`, `hl:<phrase>` |
| `c04-examples` | 19 examples | 3 example lines (rafʿ, naṣb, jarr) | `ex:1`..`ex:3`, `say:<n>` |
| `c05-title` | 20 h2 | "5 Which word for which answer?" | `title` |
| `c05-table` | 21 table | 9 rows: The answer is... · Ask with | `row:1`..`row:9`, `cell:<n>.<c>` |
| `summary` | 22 summary | Dark "In short" box, 4 points | `show` (box + title), `item:1`..`item:4` |
| `outro-yourturn` | (practice titles) | The Practice tab: the 6 practice card titles | `show` |

`hl:` phrases are matched on the visible text of the scene (English words or Arabic exactly as shown), in cue
order: a repeated phrase takes the next match after the previous `hl:` (or the first match if there is none after).
Only one marker is lit at a time: a new `hl:`, `tip`, `col`, `item`, `ex`, `say` or `show` clears the previous one.
Put an `hl:` on every single Arabic word read inside a box, so the viewer sees which word is being read.
`say:<n>` frames the whole example card (Arabic, English and note). `row:<n>` adds the row to the table (the table
grows downward). `item:<n>` dims the earlier summary points.

Every block must be on screen and covered by the narration by the end of its scene. Every row, example line,
tip, card and summary point gets its own cue. The example notes "Madinah lesson 1/4/5" are shown on screen; the
voice does not need to read the lesson numbers (it may say once "This one is from the Madinah book.").

## Narration rules
- English, for English-speaking beginners. Calm teacher voice, about 145 words per minute.
- Plain, short sentences. One idea per sentence. No em-dashes, no semicolons. No "not X but Y" lines, no filler.
- Use the lesson's own words and terms: question word, question ism, question ḥarf (write "ḥarf"), ism, fixed,
  flexible, ending, last vowel, sukūn, fatha, kasra, damma, long ā, tanween, tanween fatha, Topic, owner,
  object, preposition, "place of jarr", "place of rafʿ", rafʿ, naṣb, jarr, yes/no question (say "yes or no
  question"). Write rafʿ, naṣb, ḥarf, sukūn, ā with their marks (the TTS lexicon turns them into speech).
- Stay inside Stage 3 (`content/stage3/SPEC.md`): no present verbs, nothing about inna, no grammar the lesson does
  not teach. Teach the lesson's own points in the lesson's order.
- `أَيٌّ` must come out clearly as the exception: a question ism that is NOT fixed. It is flexible, its ending
  changes with its job (rafʿ `أَيُّ`, naṣb `أَيَّ`, jarr `أَيِّ`), and the noun after it is jarr as its owner. Every
  other question word in the lesson is fixed and never changes its last vowel, also after a preposition.
- A question word after a preposition is still fixed; it is "in the place of jarr" (its ending does not change).
  Without a preposition, it has its own job; in `مَنْ فِي الْغُرْفَةِ؟` `مَنْ` is the Topic, in the place of rafʿ.
  Do not give a job (place) for any other question word than the lesson gives.
- English meanings: use the lesson's own translation where it gives one (examples, tips). For table questions
  the lesson gives no translation: a short literal one is fine ("Who is in the room?" for `مَنْ فِي الْغُرْفَةِ؟`;
  use the vocabulary of the practice cards: الْغُرْفَةِ room, الْمُدَرِّسُ the teacher, الْفَصْلِ the classroom,
  الْمَكْتَبِ the desk, الْمُدِيرِ the principal).
- Spell nothing in transliteration inside `en` text except: rafʿ, naṣb, jarr, ism, ḥarf, sukūn, tanween, fatha,
  kasra, damma, al. Names in English as the lesson writes them (Ali, Khalid, India, Madinah).
  If an Arabic word must be heard, put it in its own `ar` segment.
- Read every Arabic example once, after its English meaning. Single question words are read in `ar` segments when
  they are introduced or when their last vowel is the point.

## Model rhythm

Table row (c01-table, row 1):
```json
[
 {"id":"c01-table-03","scene":"c01-table","lang":"ar","text":"مَنْ","pause":0.35,"cues":["row:1","cell:1.1"]},
 {"id":"c01-table-04","scene":"c01-table","lang":"en","text":"Who. It asks for a person.","pause":0.3,"cues":["cell:1.2"]},
 {"id":"c01-table-05","scene":"c01-table","lang":"ar","text":"مَنْ فِي الْغُرْفَةِ؟","pause":0.4,"cues":["cell:1.3"]},
 {"id":"c01-table-06","scene":"c01-table","lang":"en","text":"Who is in the room?","pause":0.3,"cues":[]},
 {"id":"c01-table-07","scene":"c01-table","lang":"ar","text":"مُحَمَّدٌ","pause":0.4,"cues":["cell:1.4"]},
 {"id":"c01-table-08","scene":"c01-table","lang":"en","text":"Muhammad. The answer is a person.","pause":0.5,"cues":[]}
]
```

Example line (c02-examples, line 1):
```json
[
 {"id":"c02-examples-02","scene":"c02-examples","lang":"en","text":"Is this a house? Yes, this is a house.","pause":0.3,"cues":["ex:1"]},
 {"id":"c02-examples-03","scene":"c02-examples","lang":"ar","text":"هَلْ هَذَا بَيْتٌ؟","pause":0.4,"cues":["say:1"]},
 {"id":"c02-examples-04","scene":"c02-examples","lang":"ar","text":"نَعَمْ، هَذَا بَيْتٌ","pause":0.5,"cues":[]},
 {"id":"c02-examples-05","scene":"c02-examples","lang":"en","text":"Without the first word, it is a normal sentence. With it, it is a question.","pause":0.4,"cues":[]}
]
```

## Parts (rendered separately; see `parts.json`; script files in `parts/`)
`p01-intro` (hero, c01-title, c01-table) · `p02-last-vowel` (c01-rule, c01-tips) · `p03-harfs` (c02) ·
`p04-preposition` (c03) · `p05-ayy` (c04) · `p06-review` (c05, summary, outro).
