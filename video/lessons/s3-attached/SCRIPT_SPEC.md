# "Attached pronouns" video (lesson id `s3-attached`): script format and narration rules

Stage 3, unit 2. The video follows the lesson page (the `notes` blocks of `content/stage3/u2_attached.py`)
block by block, in order. The data is in `lesson.json` (made by `video/tools/export_s3_attached.py`; block
`i` = `notes[i]`). Format and timing work as in the Naṣb video (`video/lessons/nasb/SCRIPT_SPEC.md`):
a list of short **segments**, each one spoken clause plus the visual **cues** that fire when it starts.
The voice drives the clock. Nobody types a timestamp.

## Segment

```json
{ "id": "c02-owner-04", "scene": "c02-owner", "lang": "ar", "text": "كِتَابُهُ", "pause": 0.5, "cues": ["ar:كِتَابُهُ"] }
```

- `id`: unique, `<scene>-<two digits>` in order.
- `scene`: scene id (table below). Scenes come in the order of the table.
- `lang`: `en` (English narration) or `ar` (Arabic, read by the same voice).
- `text`: what is spoken.
  - For `ar`: ONLY an exact string from the lesson source: a whole word as written (`كِتَابُهُ`, `عَلَيْهِ`,
    `فَتَحَهُ`), or a whole example sentence without its final full stop (`كِتَابُهُ جَدِيدٌ`), or one side of
    an arrow example (`كِتَابُ زَيْدٍ`, then `كِتَابُهُ`), or a phrase as written (`فِي مَحَلِّ جَرٍّ`).
    No punctuation in `ar` text. Never invent Arabic.
  - **Attached pronouns are never read on their own.** `ـهُ`, `ـكَ`, `ـي`, `عَلَيْـ`, `لِ` and the like are
    written with a joining stroke or are only a letter: do not read them. Read a whole written word that
    contains the pronoun instead (`كِتَابُهُ`, `عَلَيْهِ`, `لَهُ`). Single letters (`ة`, `ت`, `ن`, `ي`, `ال`) are not read either.
  - Never put Arabic inside an `en` segment. Never write transliteration in `en` text, except the course terms
    below. To name a pronoun in English, use its meaning: "the pronoun for he", "the pronoun for you, one man",
    "the pronoun for I" (or "the pronoun for me"), "the pronoun for they, men". The screen marks it while it is named.
- `pause`: silence after the segment, in seconds. Default 0.25. Use 0.5–0.7 after a question the viewer should
  answer in their head, and 0.4–0.6 before and after Arabic readings.
- `cues`: visual actions that start with this segment (may be empty).

## Scenes and their cues

Every scene except `hero` and the chapter titles shows the chapter heading at the top and the listed blocks below
it. **Every piece of a scene starts hidden and must be revealed by a cue** (the build stops otherwise): each block
(`b:<k>`), each example row (`ex:<k>`) and its note (`note:<k>`), each table row (`row:<k>` or `rows`), each summary item (`li:<k>`).

| Scene id | Lesson blocks (index: kind) | What it shows |
|---|---|---|
| `hero` | 0: hero | Teal hero card: eyebrow, title "Pronouns that hold on", sentence with كِتَابُهُ, عَلَيْهِ, فَتَحَهُ |
| `c01-title` | 1: h2 | "1 The twelve attached pronouns" |
| `c01-intro` | 2: p | "An attached pronoun cannot stand alone ..." |
| `c01-table` | 3: table | The 12 pronouns: Pronoun · Who · On a noun · English (12 rows) |
| `c01-tip` | 4: tip | Compare with unit 1 (أَنْتُمَا and ـكُمَا ...), the ـكَ family and the ـهُ family |
| `c02-title` | 5: h2 | "2 On a noun: the owner" |
| `c02-owner` | 6: p, 7: examples (3) | "A pronoun on a noun shows who owns it ..." + 3 examples |
| `c02-rule` | 8: rule (green) | "No ال, no tanween" |
| `c02-endings` | 9: p, 10: examples (3) | "The noun still shows its own ending ..." + 3 examples |
| `c02-tip` | 11: tip | ة written as ت before a pronoun |
| `c03-title` | 12: h2 | "3 With ـي the ending is hidden" |
| `c03-hidden` | 13: p, 14: examples (2) | "The pronoun ـي always needs a kasra ..." + 2 examples |
| `c03-rule` | 15: rule (blue) | "Do not read the ending before ـي" |
| `c04-title` | 16: h2 | "4 On a preposition" |
| `c04-prep` | 17: p, 18: examples (3) | "A pronoun after a preposition is jarr ..." + 3 examples |
| `c04-forms` | 19: p, 20: table | "Some prepositions change their shape ..." + table (5 rows: فِي، عَلَى، إِلَى، مِنْ، لِ) |
| `c04-rule` | 21: rule (grey) | "Three changes to remember" |
| `c05-title` | 22: h2 | "5 When ـهُ becomes ـهِ" |
| `c05-rule` | 23: rule (blue) | "After kasra or ي" |
| `c05-ex` | 24: p, 25: examples (3) | "The same happens to ـهُمَا، ـهُمْ، ـهُنَّ" + 3 examples |
| `c05-tip` | 26: tip | "It is the same pronoun ..." |
| `c06-title` | 27: h2 | "6 On a verb: the object" |
| `c06-intro` | 28: p | "A pronoun from this table on a past verb or an order verb is the object ..." |
| `c06-ex` | 29: examples (5) | 5 examples |
| `c06-tips` | 30: tip, 31: tip | Past-verb doer endings (unit 6); "me" on a verb is ـنِي |
| `c07-title` | 32: h2 | "7 Three places, one table" |
| `c07-table` | 33: table | Joined to · Job · Place · Example (3 rows) |
| `c07-summary` | 34: summary | "In short": 5 items |

Cues:
- `title` (chapter scenes): the heading appears. Put it on the first segment.
- hero: `title` (title appears), `sub` (the sentence appears), `ar:<text>`.
- `b:<k>`: the scene's k-th block appears (0-based, in the order of the table above). A table appears with its
  header row only; an example list appears empty; a summary appears with its title only.
- `ex:<k>`: example row k of the scene (Arabic and English) appears. `note:<k>`: its grey note line appears.
- `row:<k>`: table row k (0-based, without the header) appears. `rows`: all rows appear one after another.
- `li:<k>`: summary item k appears.
- `ar:<text>`: a gold frame lights up, for the length of this segment, around the element whose whole text is exactly
  `<text>` (a word in `{}` such as `ـهُ` or `عَلَيْهِ`, an Arabic table cell, an example sentence without its full stop,
  or one side of an arrow example). If the same text appears more than once in the scene, `<text>#2` is the second
  one (in page order: top to bottom; in a table row, right-hand Arabic cells come in the order of the source row).
  Use it on the `ar` segment that reads the word, and on an `en` segment that names a pronoun or a letter.
  The build stops if no element has exactly that text.
- `hl:<phrase>`: a phrase of the scene's English text gets a yellow marker that stays (as in the Naṣb rule boxes).
  The phrase must be copied exactly from the block text as shown on screen. Use it for the key words of rule boxes and tips.

## Narration rules
- English, for English-speaking students. Calm teacher voice, about 145 words per minute.
- Plain, short sentences. One idea per sentence. No em-dashes, no semicolons.
- Use the site's terms exactly: attached pronoun, separate pronoun, fixed, flexible, owner, iḍāfa ("the first word of
  an iḍāfa"), after a preposition, object, doer, Topic, past verb, order verb, rafʿ, naṣb, jarr, damma, fatha, kasra,
  sukūn, tanween, al (write "al" for ال). "In the place of jarr" and "in the place of naṣb" are the lesson's words
  for مَحَلّ: a fixed word does not change its ending, so we say which place it stands in.
- Allowed transliteration in `en` text: rafʿ, naṣb, jarr, al, tanween, sukūn, iḍāfa, Zayd. Nothing else.
- Stay inside Stage 3 (`content/stage3/SPEC.md`): past verbs and order verbs only, no present verbs. Do not add
  grammar the lesson does not teach (no ـنِي details beyond the tip, no doer pronouns of past verbs beyond the tip).
- Cover every block, in order, with its own content: every sentence of every p, rule and tip, every table row,
  every example (its Arabic, its English and its note), every summary item. You may say a block's sentence in your
  own plain words, but do not change its meaning and do not skip any part.
- Read every example in Arabic once, after its English meaning (both sides of an arrow example). Read the
  "On a noun" word of every row of the first table, and the four forms of every row of the preposition table.
  The other Arabic words (in tips, rules, notes, summary) are read when the narration explains them, as long as
  they are whole written words.
- iʿrāb must be exact. Attached pronouns are fixed: say "in the place of jarr" / "in the place of naṣb", never that
  the pronoun "takes kasra" or "is jarr with kasra". The noun before the pronoun is flexible and shows its own ending
  (except before ـي).

## Parts (rendered separately; `parts.json`)
`p01-intro` (hero, c01), `p02-noun` (c02), `p03-hidden` (c03), `p04-prep` (c04), `p05-hu-hi` (c05),
`p06-verb` (c06), `p07-summary` (c07).
