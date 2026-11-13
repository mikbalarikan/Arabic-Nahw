# "Fixed verbs: past and order" video (lesson id `s3-verbs`): script format and narration rules

The video follows the lesson page block by block: the `notes` of `content/stage3/u6_verbs.py`
(Stage 3, unit 6), exported to `lesson.json` by `video/tools/export_s3_verbs.py`. Format and timing work
as in the Naṣb video (`video/lessons/nasb/SCRIPT_SPEC.md`): a list of short **segments**, each one
spoken clause or one Arabic reading, plus the visual **cues** that fire when it starts. The voice drives
the clock. Nobody types a timestamp. Scenes are drawn by `video/tools/scenes_s3_verbs.py` with the
site's own block HTML (`course.render_notes`) and CSS.

## Segment

```json
{ "id": "c02-table-03", "scene": "c02-table", "lang": "ar", "text": "كَتَبُوا", "pause": 0.45, "cues": ["row:2"] }
```

- `id`: unique, `<scene>-<two digits>` in order.
- `scene`: scene id (list below).
- `lang`: `en` (narration) or `ar` (Arabic read by the voice).
- `text`: what is spoken. For `ar`: ONLY a word or sentence exactly as written in the lesson notes
  (a table cell, an example sentence, a word inside `{...}`), checked by `check_arabic.py`.
  Never invent Arabic. Never put Arabic inside an `en` segment. Bare endings with a joining stroke
  (`ـتُ`, `ـُوا`) are shown, not read: read a whole verb from the lesson that carries the ending.
- `pause`: silence after the segment. Default 0.25. 0.4–0.6 around `ar` readings; inside a run of table
  readings 0.35–0.45 so the table keeps moving.
- `cues`: visual actions that start with this segment (may be empty).

## Scenes and cues

Every block of the notes is shown, in the lesson's order. A chapter title scene shows the chapter's
`h2` and its first paragraph (`p`) under it.

| Scene id | Kind | Shows (block of the notes) | Cues |
|---|---|---|---|
| `hero` | hero | Hero card: eyebrow, title, text, watermark الفِعْلُ المَبْنِيُّ | `title`, `sub` |
| `cNN-title` | chapter | Chapter NN heading + its first paragraph | `title`, `sub` |
| `c01-cols` | cols | Three verb cards (past · order · present) | `item:0` … `item:2` |
| `c01-tip` | tip | "Only past and order verbs" tip | `show` |
| `c02-table` | table | The 14-person past table | `row:0` … `row:13` |
| `c02-tip` | tip | "14 persons, 13 forms" tip | `show`, `hl:<phrase>` |
| `c02-examples` | examples | Three example lines | `ex:<i>`, `read:<i>`, `note:<i>` |
| `c03-words` | words | Eight doer-ending tiles | `item:0` … `item:7` |
| `c03-rule` | rule | Grey rule "The ـتْ of كَتَبَتْ is a ḥarf" | `show`, `hl:<phrase>` |
| `c03-cols` | cols | Hidden doer · hidden doer · attached doer | `item:0` … `item:2` |
| `c03-tip` | tip | "When a noun is the doer" tip | `show` |
| `c04-table` | table | Built on fatha / damma / sukūn | `row:0` … `row:2` |
| `c04-rule` | rule | Navy rule "Fixed on fatha" | `show`, `hl:<phrase>` |
| `c05-table` | table | Past verb · with مَا · meaning | `row:0` … `row:3` |
| `c05-rule` | rule | Grey rule "مَا is a ḥarf of negation" | `show`, `hl:<phrase>` |
| `c05-examples` | examples | Four example lines | `ex:<i>`, `read:<i>`, `note:<i>` |
| `c05-tips` | tips | Two tips: مَا "not" vs مَا "what"; لَا | `tip:0`, `tip:1` |
| `c06-table` | table | The 5 order forms | `row:0` … `row:4` |
| `c06-rule` | rule | Brown rule "Two ways to be built" | `show`, `hl:<phrase>` |
| `c06-examples` | examples | Two example lines | `ex:<i>`, `read:<i>`, `note:<i>` |
| `c07-table` | table | اُ or اِ: 8 verbs | `row:0` … `row:7` |
| `c07-tip` | tip | "Learn each order verb as a word" | `show` |
| `c08-examples` | examples | Two example lines with notes | `ex:<i>`, `read:<i>`, `note:<i>` |
| `c08-tip` | tip | "Only a bridge for speaking" | `show` |
| `sum` | summary | "In short": 7 points | `item:0` … `item:6` |
| `outro-yourturn` | yourturn | The Practice tab: its 7 card titles | `show` |

Cue details:
- `row:<r>`: table row `r` (0-based, header not counted) fades in and gets a soft gold highlight; the
  previous highlight goes. `rows` shows every row at once. `hlrow:<r>` moves the highlight to a row that
  is already shown. `cell:<r>:<c>` rings one cell. `unhl` removes the highlight.
- `ex:<i>`: example line `i` appears (Arabic + English). Its grey note waits for `note:<i>`.
  `read:<i>`: a gold frame around line `i` while its Arabic is read (put it on the `ar` segment).
- `item:<i>`: card / tile / summary point `i` appears.
- `show`: the block appears. `hl:<phrase>`: a gold marker under that phrase of the block's visible text.
- `tip:<i>`: tip box `i` of a two-tip scene appears.

## Narration rules
- English, for English-speaking students. Calm teacher voice, about 145 words per minute.
- Plain, short sentences. One idea per sentence. No em-dashes, no semicolons.
- The site's terms: past verb, order verb, present verb, fixed, built on, doer, hidden, attached pronoun,
  place of rafʿ, ḥarf (say "harf"), ism, fatha, damma, kasra, sukūn, "dropping the noon", helping alif,
  helping kasra, jarr, al (for ال, as in the Naṣb video). Write "rafʿ", "sukūn", "iʿrāb", "ḥarf" as on the site; `tts_text.py` gives the spoken form.
- Stage 3 scope: past and order verbs only. The present verb is only named ("we study it in Stage 8"),
  never shown or conjugated. Do not add grammar the notes do not teach.
- No transliteration inside `en` text except the site terms above. If a word must be heard, put it in
  an `ar` segment.
- Every block, every table row, every card, tile, example, note, tip and summary point is shown (cue) and
  covered by the narration, in the lesson's order.
- Tables: the past table is read in the lesson's groups of three (he / they two / they, then she ...):
  one short English line names the group, then each verb is read with its row lit, so it keeps a calm but
  steady pace. Order forms: each form is read once, with what it is built on and where its doer is.
  The اُ / اِ list: two groups (middle damma / no middle damma), each order verb read once while its
  "middle" cell is ringed (`cell:<r>:2`); the middle letter is shown, not spelled out in English.
- Example sentences: English meaning, then the Arabic once, slowly.
