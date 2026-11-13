# "Particles" video (Stage 3, unit 7, lesson id `s3-particles`): script format and narration rules

The video follows the lesson page (the `notes` blocks of `content/stage3/u7_particles.py`) block by block, in
order. The data is in `lesson.json` (made by `video/tools/export_s3_particles.py`; every block is rendered by the
site's own `course.render_notes`). Format and timing work as in the Naṣb video
(`video/lessons/nasb/SCRIPT_SPEC.md`): a list of short **segments**, each one spoken clause plus the visual
**cues** that fire when it starts. The voice drives the clock. Nobody types a timestamp.

## Segment

```json
{ "id": "c02-table-03", "scene": "c02-table", "lang": "ar", "text": "خَرَجَ مِنَ البَيْتِ", "pause": 0.5, "cues": [] }
```

- `id`: unique, `<scene>-<two digits>` in order.
- `lang`: `en` (English narration) or `ar` (Arabic read by the same voice).
- `text` for `ar`: ONLY Arabic exactly as written in the unit file: a whole table cell, a whole `{...}` word or
  phrase, or a sentence of a cell without its final full stop (the voice reads the last vowel; `check_arabic.py`
  must give 0 errors). A question keeps its `؟`. A cell may be split at `،` (`نَعَمْ، هَذَا بَيْتٌ`).
  Never invent Arabic. Never put Arabic inside an `en` segment.
- **One-letter ḥarfs written joined to the next word** (`بِـ`، `لِـ`، `كَـ`، `وَ`، `فَ`، the question `أَ`) are
  never read on their own and never in an invented separated form. Read the whole written word or the example
  sentence that contains them (`كَتَبْتُ بِالقَلَمِ`، `لِلمُدَرِّسِ`، `فَخَالِدٌ`، `أَهَذَا بَيْتٌ؟`).
- `pause`: silence after the segment, in seconds. Default 0.25. 0.4–0.6 around Arabic readings,
  0.5–0.7 after a question.

## Scenes, in order (ids come from `lesson.json` `scenes`)

| Scene id | Kind | Block(s) shown | Cues |
|---|---|---|---|
| `hero` | hero | hero card, watermark الحُرُوفُ | `title`, `sub` |
| `c01-title` | chapter | h2 1 + its paragraph as grey sub-line | `title`, `sub`, `hl:<phrase>` |
| `c01-rule` | rulebox | grey rule "How we say it" | `show`, `hl:<phrase>` |
| `c01-cols` | cols | the five groups | `col:1` … `col:5` |
| `c02-title` | chapter | h2 2 (jarr) + paragraph | `title`, `sub`, `hl:` |
| `c02-table` | table | 9 jarr ḥarfs | `row:<n>`, `rows`, `mark:<n>` |
| `c02-rule` | rulebox | green rule "Two small changes before ال" | `show`, `hl:` |
| `c02-tip` | tip | tip: بِـ، لِـ، كَـ are joined; لِلمُدَرِّسِ | `show`, `hl:` |
| `c03-title` | chapter | h2 3 (joining) + paragraph | `title`, `sub`, `hl:` |
| `c03-table` | table | 5 joining ḥarfs | `row:<n>`, `mark:<n>` |
| `c03-examples` | exlist | the two worked examples | `ex:1`, `ex:2`, `note:1`, `note:2` |
| `c04-title` | chapter | h2 4 (answer) | `title` |
| `c04-table` | table | نَعَمْ، لَا، بَلَى | `row:<n>`, `mark:<n>` |
| `c04-rule` | rulebox | olive rule "When to use بَلَى" | `show`, `hl:` |
| `c04-tip` | tip | tip: أَ + مَا + ذَهَبْتَ | `show`, `hl:` |
| `c05-title` | chapter | h2 5 (question) + paragraph | `title`, `sub`, `hl:` |
| `c05-table` | table | هَلْ، أَ | `row:<n>`, `mark:<n>` |
| `c06-title` | chapter | h2 6 (calling) + paragraph | `title`, `sub`, `hl:` |
| `c06-table` | table | five called nouns | `row:<n>`, `mark:<n>` |
| `c06-tip` | tip | tip: Madinah lesson 5 | `show`, `hl:` |
| `c07-title` | chapter | h2 7 (look-alikes) + paragraph | `title`, `sub`, `hl:` |
| `c07-table` | table | ḥarf / ism pairs | `row:<n>`, `mark:<n>` |
| `summary` | summary | "In short" box | `q:1` … `q:5` |

Cue details:
- `title` / `sub`: the heading / the grey sub-line (the lesson paragraph) fade in.
- `show`: the rule or tip box fades in.
- `hl:<phrase>`: a gold marker sweeps over `<phrase>`, matched on the visible text of the box (it may contain
  Arabic exactly as shown, e.g. `hl:مِنْ becomes مِنَ`). Highlights stay on.
- `col:<n>`: group card n appears (1 jarr, 2 joining, 3 answer, 4 question, 5 calling).
- `row:<n>`: table row n (1-based, header not counted) appears. `rows`: all rows at once.
- `mark:<n>`: a soft gold wash on row n while it is talked about (moves from the previous row); `mark:0` clears it.
- `ex:<n>`: worked example n (Arabic + English meaning) appears. `note:<n>`: its grey note appears.
- `q:<n>`: summary line n appears.

Every block must be shown by the end of its scene: every table row, every column card, every example and note,
every summary line.

## Narration rules
- English, for English-speaking students. Calm teacher voice, about 145 words per minute.
- Plain, short sentences. One idea per sentence. No em-dashes, no semicolons. No "not X but Y".
- Use the lesson's terms: ḥarf (plural ḥarfs), ism (isms), fixed, place (in the place of rafʿ / naṣb / jarr),
  iʿrāb, jarr, joining, answer, question, calling, damma, fatha, kasra, sukūn, tanween, al, wa.
  Write `ḥarf` in lower case (also at the start of a sentence put an article before it: "A ḥarf ...").
- Transliteration inside `en` text only for: ḥarf, ism, iʿrāb, rafʿ, naṣb, jarr, al, wa, tanween, sukūn, and the
  names Muhammad, Khalid, Hamid, Yasir, Ali, Aminah, Bilal, Madinah. Any other Arabic that must be heard goes into
  an `ar` segment.
- Stage 3 scope (`content/stage3/SPEC.md`): no present verbs, no inna and her sisters, no grammar the lesson does
  not teach. Particles are always fixed and have no place of iʿrāb. What a ḥarf does to the next word is said only
  as the lesson says it: jarr ḥarfs → the next noun is jarr; joining ḥarfs → the next word copies the ending of the
  word before; يَا → a name or single noun takes one damma, no tanween, fixed, in the place of naṣb.
- The helping vowel before al (مِنَ، عَنِ، أَوِ) is a small change for speaking; it is not iʿrāb.
- Each table row: the row appears and is marked, the ḥarf is read in Arabic (unless it is a joined one-letter
  ḥarf), its meaning is said, then the example is read in Arabic, with a short English meaning.

## Parts (rendered separately; see `parts.json`)
`p01-intro` (hero, c01) · `p02-jarr` (c02) · `p03-joining` (c03) · `p04-answer-question` (c04, c05) ·
`p05-calling-lookalikes` (c06, c07, summary).
