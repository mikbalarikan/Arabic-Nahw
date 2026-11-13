# "Separate pronouns" video (lesson id `s3-pronouns`): script format and narration rules

Stage 3, unit 1. The video follows the lesson page (`content/stage3/u1_pronouns.py`, its `notes` blocks) in order,
block by block. The data is in `lesson.json` (made by `video/tools/export_s3_pronouns.py`; every block keeps the
site's own HTML). Format and timing work as in the Naṣb video (`video/lessons/nasb/SCRIPT_SPEC.md`): a list of
short **segments**, each one spoken clause plus the visual **cues** that fire when it starts. The voice drives the
clock. Nobody types a timestamp.

## Segment

```json
{ "id": "c03-table-04", "scene": "c03-table", "lang": "en", "text": "First person, one. I.", "pause": 0.3, "cues": ["row:1"] }
```

- `id`: unique, `<scene>-<two digits>` in order.
- `scene`: scene id (list below).
- `lang`: `en` (narration) or `ar` (Arabic reading by the same voice).
- `text`: what is spoken. For `ar`: ONLY Arabic exactly as written in the lesson source (a pronoun from the
  table, a word from a tile or a box, a whole example sentence without its final full stop, or a phrase such as
  `فِي مَحَلِّ رَفْعٍ`). Never invent Arabic, never change a vowel, never put Arabic inside an `en` segment.
  `python3 video/tools/check_arabic.py video/lessons/s3-pronouns/script.json` must report 0 errors.
- `pause`: silence after the segment, in seconds. Default 0.25. 0.4–0.6 around Arabic readings, 0.5–0.7 after a
  question the viewer should answer in their head, 0.7–0.9 at the end of a scene.
- `cues`: visual actions that start with this segment (may be empty).

## Scenes and their cues

| Scene id | Lesson block(s) | Shows | Cues |
|---|---|---|---|
| `hero` | hero | Teal hero card: eyebrow, title, line, watermark الضَّمَائِرُ | `title`, `sub` |
| `c01-title` … `c06-title` | h2 | Numbered chapter heading | `title` |
| `c01-why` | 3 × p, words | The three paragraphs, then four word tiles | `p:1` `p:2` `p:3`, `word:1` … `word:4` |
| `c02-cols` | cols | Two cards: Fixed, Flexible | `col:1`, `col:2` |
| `c03-table` | p, table | "Learn this table by heart", then the 12-row table | `p:1`, `head`, `row:1` … `row:12` |
| `c03-tip1` | tip | Watch the small vowels | `show` |
| `c03-tip2` | tip | Side note: built on one fixed mark | `show` |
| `c04-groups` | cols | Three cards: speaker, listener, absent | `col:1` `col:2` `col:3` |
| `c04-tip1` | tip | هُوَ and هِيَ for things | `show` |
| `c04-tip2` | tip | Two people; mixed groups | `show` |
| `c05-rule` | p, rule | The paragraph, then the red rule box "The place of rafʿ" | `p:1`, `rule` |
| `c05-steps` | p, table | "Two steps", then the 2-row table | `p:1`, `head`, `row:1`, `row:2` |
| `c05-tip` | tip | Three places | `show` |
| `c06-examples` | p, examples | The paragraph, then the six example rows | `p:1`, `ex:1` … `ex:6`, `note:1` … `note:6` |
| `c06-tip` | tip | A pronoun can replace a noun | `show` |
| `summary` | summary | The teal "In short" box | `li:1` … `li:5` |
| `outro-yourturn` | (Practice tab) | The six practice card titles | `show` |

Cues for every scene that holds text:
- `hl:<phrase>` gives `<phrase>` (exact visible text of the block, English or Arabic) a gold highlighter stroke.
  Use it on the Arabic word while it is read, and on the key words of a rule. If the same phrase appears more
  than once in the scene, add `@2`, `@3` for the 2nd, 3rd occurrence (`hl:هُوَ@2`). Highlights stay on.
- `row:<n>` makes table row n appear and puts a soft gold "now" band on it. The band moves to the next row on the
  next `row:` cue. A row should appear on the segment that starts talking about it.
- `ex:<n>` shows example row n (Arabic + English). `note:<n>` shows its grey note line. Put `note:<n>` on the
  segment that starts explaining the note.
- `show` on a tip scene shows the whole tip box.

Every block of the lesson must be shown (cue) AND covered by the narration, in the lesson's order: all paragraphs,
all four tiles, both column cards, all 12 table rows, all tips, the rule box, both rows of the two-step table,
all six examples with their notes, the five summary points. The summary may be read close to word for word.

## Narration rules
- English, for English-speaking students. Calm teacher voice, about 145 words per minute.
- Plain, short sentences. One idea per sentence. No em-dashes, no semicolons, no "not X but Y".
- Use the site's terms exactly: fixed, flexible, pronoun, Topic, Information, after a preposition, owner, job,
  place ("in the place of rafʿ"), person (1st person the speaker, 2nd person the listener, 3rd person the absent
  one), masculine, feminine, rafʿ (write "rafʿ"), naṣb (write "naṣb"), jarr, damma, fatha, kasra, sukūn, shadda,
  tanween, al.
- Stage 3 scope (`content/stage3/SPEC.md`): no present verbs, no attached pronouns as a topic here, no separate naṣb
  pronouns (إِيَّا…), no inna. Do not add grammar the lesson does not teach. The idea of "place" (مَحَلّ) is the
  key idea: a fixed word cannot show rafʿ on its ending, so its job gives it a place. In this unit the twelve
  pronouns are always the Topic, so always in the place of rafʿ. Say nothing about naṣb or jarr places beyond
  what the tip says (there are three places).
- Spell no Arabic in transliteration inside `en` text, except: rafʿ, naṣb, jarr, al, tanween, sukūn, shadda.
  If an Arabic word must be heard, put it in its own `ar` segment. Say the English meaning next to it.
- Read each pronoun in Arabic when its table row appears (`row:n` on the English segment, the `ar` reading right
  after it). Read each example sentence in Arabic once, after its English meaning.
- "m or f" in the table: say "a man or a woman" or "masculine or feminine". "m or mixed": "men, or men and women".

## Model: the first rows of the table

```json
[
 {"id":"c03-table-01","scene":"c03-table","lang":"en","text":"Learn this table by heart.","pause":0.25,"cues":["p:1"]},
 {"id":"c03-table-02","scene":"c03-table","lang":"en","text":"Read it aloud, top to bottom, every day this week.","pause":0.4,"cues":["head"]},
 {"id":"c03-table-03","scene":"c03-table","lang":"en","text":"First person, the speaker alone. I.","pause":0.3,"cues":["row:1"]},
 {"id":"c03-table-04","scene":"c03-table","lang":"ar","text":"أَنَا","pause":0.5,"cues":[]},
 {"id":"c03-table-05","scene":"c03-table","lang":"en","text":"The speaker with others. We.","pause":0.3,"cues":["row:2"]},
 {"id":"c03-table-06","scene":"c03-table","lang":"ar","text":"نَحْنُ","pause":0.5,"cues":[]}
]
```

## Scene ids, in order
`hero`, `c01-title`, `c01-why`, `c02-title`, `c02-cols`, `c03-title`, `c03-table`, `c03-tip1`, `c03-tip2`,
`c04-title`, `c04-groups`, `c04-tip1`, `c04-tip2`, `c05-title`, `c05-rule`, `c05-steps`, `c05-tip`,
`c06-title`, `c06-examples`, `c06-tip`, `summary`, `outro-yourturn`.

## Parts (rendered separately; see `parts.json`) and script files
`p01-intro` (hero, c01, c02) · `p02-table` (c03) · `p03-groups` (c04) · `p04-place` (c05) ·
`p05-sentences` (c06, summary, outro). Script parts: `parts/p1-intro.json` … `parts/p5-sentences.json`
(`{"segments": [...]}`), joined by `python3 video/tools/assemble_script.py s3-pronouns`.
