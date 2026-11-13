# Relative pronouns video (s3-relatives): script format and narration rules

The video follows the lesson page of Stage 3, unit 4 (`content/stage3/u4_relatives.py`, its `notes` blocks,
exported to `lesson.json` by `video/tools/export_s3_relatives.py`) block by block, in order. Same machinery as the
Naṣb video (`video/lessons/nasb/SCRIPT_SPEC.md`): the voice drives the clock, the script is a list of short
**segments**, each one spoken clause (English) or one Arabic reading, plus the visual **cues** that fire when it
starts. Nobody types a timestamp.

## Segment

```json
{ "id": "c02-ex-03", "scene": "c02-ex", "lang": "ar", "text": "جَاءَ الطَّالِبُ الَّذِي نَجَحَ", "pause": 0.6, "cues": ["ar:0"] }
```

- `id`: unique, `<scene>-<two digits>` in order.
- `scene`: one of the scene ids below, in the order below.
- `lang`: `en` (narration) or `ar` (Arabic reading).
- `text`: what is spoken. For `ar`, ONLY an exact string from the lesson: one of the numbered Arabic items of
  the scene (list at the end), or a word / phrase that appears inside one, exactly as written there.
  Never invent Arabic. Never put Arabic inside an `en` segment: split it into its own `ar` segment.
  Leave out a final `.` or `؟` of an example sentence (the voice check reads the last vowel).
- `pause`: silence after the segment, in seconds. Default 0.25. 0.5–0.7 after a question the viewer should
  answer in their head, 0.4–0.6 before and after Arabic readings.
- `cues`: visual actions that start with this segment (may be empty).

## Scene kinds and their cues

| Kind | Shows | Cues |
|---|---|---|
| `hero` | Teal hero card: eyebrow, title, the hero sentence, watermark الَّذِي | `title`, `sub` |
| `chapter` | Numbered chapter heading, and (chapters 2–5) the chapter's opening paragraph as a grey sub-line | `title`, `sub` |
| `table` | The table to learn: header visible, 4 rows hidden | `row:1` … `row:4` |
| `cols` | Two purple cards: General: who (مَنْ), General: what (مَا) | `col:1`, `col:2` |
| `box` | One tip box or rule box, hidden at first | `show` |
| `boxes` | Two boxes one under the other (`c03-tips`: two tips; `c06-forms`: the orange rule, then the dual table) | `show:1`, `show:2` |
| `examples` | A list of example rows: Arabic right, English left, the grey note under the English | `ex:<i>` (row i, 1-based, Arabic + English appear), `note:<i>` (its note appears) |
| `summary` | The dark "In short" box, its 5 points hidden | `li:1` … `li:5`, `practice` (the Practice tab in the top bar lights up) |

Cues every scene kind has:
- `ar:<n>`: a soft gold glow on Arabic item `n` of the scene while it is read (it fades after the segment).
  Put it on the `ar` segment that reads that item. Items are listed per scene at the end of this file.
- `hl:<phrase>`: a gold underline sweeps under an English phrase of the box / list (exact visible text,
  e.g. `hl:never changes`). It stays. Not for `chapter` or `hero` scenes.

Every block must be shown (cue) AND covered by the narration: every table row, both cards, every tip, every rule,
every example with its note, every summary point. Nothing may appear before it is talked about, and everything
must be visible before the scene ends.

## Scenes, in order
`hero`, `c01-title`, `c01-table`, `c01-cols`, `c01-tip`, `c01-rule`,
`c02-title`, `c02-ex`, `c02-tip`,
`c03-title`, `c03-ex`, `c03-tips`,
`c04-title`, `c04-ex`,
`c05-title`, `c05-ex`, `c05-tip`,
`c06-title`, `c06-forms`, `summary`.

Parts (rendered separately, `parts.json`): p01 hero + chapter 1 · p02 chapter 2 · p03 chapter 3 · p04 chapter 4 ·
p05 chapter 5 · p06 chapter 6 + In short. Script files: `parts/p1-….json` … `parts/p6-….json`
(`{"segments": [...]}`), joined by `assemble_script.py s3-relatives`.

## Narration rules
- English, for English-speaking beginners. Calm teacher voice, about 145 words per minute.
- Plain, short sentences. One idea per sentence. No em-dashes, no semicolons, no "not X but Y", no filler.
- Use the lesson's terms exactly: relative, fixed, flexible, clause, ṣila (write "ṣila"), place of rafʿ / naṣb /
  jarr (write "rafʿ", "naṣb"), adjective, al (for ال in English text), question word, doer, dual.
- Stage 3 scope (`content/stage3/SPEC.md`): no present verbs, no grammar the lesson does not teach.
  اللَّذَانِ and اللَّتَانِ are NOT fixed: say so exactly as the lesson does (flexible, they change in naṣb and jarr,
  they come with the dual in Stage 4). Never call them fixed. Never call الَّذِينَ flexible.
- Follow the lesson's own wording and order; explain, do not add new rules or new examples.
- Transliteration in `en` text only for: rafʿ, naṣb, jarr, al, ṣila. If an Arabic word must be heard, put it in an
  `ar` segment.
- Read every example sentence in Arabic once, after its English meaning (or before, then the meaning).
  Read each table word in Arabic when it is introduced. Single words are read in `ar` segments when explained.
- A Qur'an verse: none in this unit.

## Arabic items per scene (for `ar:<n>` and for exact `ar` text)
- `hero` (hero, blocks 0): no Arabic items
- `c01-title` (chapter, blocks 1): no Arabic items
- `c01-table` (table, blocks 2): `ar:0` الَّذِي · `ar:1` الطَّالِبُ الَّذِي نَجَحَ · `ar:2` الَّتِي · `ar:3` الْبِنْتُ الَّتِي نَجَحَتْ · `ar:4` الَّذِينَ · `ar:5` الطُّلَّابُ الَّذِينَ نَجَحُوا · `ar:6` اللَّاتِي · `ar:7` اللَّوَاتِي · `ar:8` النِّسَاءُ اللَّاتِي نَجَحْنَ
- `c01-cols` (cols, blocks 3): `ar:0` مَنْ · `ar:1` جَاءَ مَنْ نَجَحَ · `ar:2` مَا · `ar:3` قَرَأْتُ مَا كَتَبَ الْمُدَرِّسُ
- `c01-tip` (box, blocks 4): `ar:0` الَّذِي · `ar:1` الَّتِي · `ar:2` الَّذِينَ · `ar:3` ل · `ar:4` اللَّاتِي · `ar:5` اللَّوَاتِي
- `c01-rule` (box, blocks 5): `ar:0` الَّذِينَ · `ar:1` الَّذِينَ · `ar:2` الَّذِي · `ar:3` الَّتِي
- `c02-title` (chapter, blocks 6, 7): `ar:0` الَّذِي · `ar:1` صِلَةٌ
- `c02-ex` (examples, blocks 8): `ar:0` جَاءَ الطَّالِبُ الَّذِي نَجَحَ. · `ar:1` نَجَحَ · `ar:2` هَذِهِ هِيَ الْبِنْتُ الَّتِي كَتَبَتِ الدَّرْسَ. · `ar:3` كَتَبَتِ الدَّرْسَ · `ar:4` الْكِتَابُ الَّذِي عَلَى الْمَكْتَبِ جَدِيدٌ. · `ar:5` عَلَى الْمَكْتَبِ · `ar:6` خَرَجَ الرِّجَالُ الَّذِينَ جَلَسُوا فِي الْمَسْجِدِ. · `ar:7` جَلَسُوا فِي الْمَسْجِدِ
- `c02-tip` (box, blocks 9): `ar:0` نَجَحَ · `ar:1` الطَّالِبُ الَّذِي بَيْتُهُ قَرِيبٌ
- `c03-title` (chapter, blocks 10, 11): `ar:0` ال
- `c03-ex` (examples, blocks 12): `ar:0` الْوَلَدُ الَّذِي فِي الْبَيْتِ · `ar:1` الَّذِي · `ar:2` السَّاعَةُ الَّتِي عَلَى السَّرِيرِ · `ar:3` السَّاعَةُ · `ar:4` الَّتِي · `ar:5` الْأَوْلَادُ الَّذِينَ خَرَجُوا · `ar:6` الَّذِينَ · `ar:7` النِّسَاءُ اللَّاتِي خَرَجْنَ · `ar:8` اللَّاتِي
- `c03-tips` (boxes, blocks 13, 14): `ar:0` الَّذِي خَرَجَ · `ar:1` الَّتِي خَرَجَتْ · `ar:2` الَّذِينَ خَرَجُوا · `ar:3` اللَّاتِي خَرَجْنَ · `ar:4` ال · `ar:5` جَاءَ طَالِبٌ نَجَحَ
- `c04-title` (chapter, blocks 15, 16): `ar:0` مَنْ · `ar:1` مَا · `ar:2` مَنْ · `ar:3` مَا · `ar:4` ؟
- `c04-ex` (examples, blocks 17): `ar:0` مَنْ نَجَحَ؟ · `ar:1` جَاءَ مَنْ نَجَحَ. · `ar:2` نَجَحَ · `ar:3` مَا عَلَى الْمَكْتَبِ؟ · `ar:4` اِقْرَأْ مَا عَلَى الْمَكْتَبِ.
- `c05-title` (chapter, blocks 18, 19): no Arabic items
- `c05-ex` (examples, blocks 20): `ar:0` جَاءَ الطَّالِبُ الَّذِي نَجَحَ. · `ar:1` الطَّالِبُ · `ar:2` الَّذِي · `ar:3` شَكَرَ الْمُدِيرُ الطَّالِبَ الَّذِي نَجَحَ. · `ar:4` الطَّالِبَ · `ar:5` الَّذِي · `ar:6` ذَهَبْتُ إِلَى الطَّالِبِ الَّذِي نَجَحَ. · `ar:7` الطَّالِبِ · `ar:8` الَّذِي
- `c05-tip` (box, blocks 21): `ar:0` مَنْ · `ar:1` مَا · `ar:2` جَاءَ مَنْ نَجَحَ · `ar:3` مَنْ
- `c06-title` (chapter, blocks 22): `ar:0` اللَّذَانِ · `ar:1` اللَّتَانِ
- `c06-forms` (boxes, blocks 23, 24): `ar:0` اللَّذَانِ · `ar:1` اللَّتَانِ · `ar:2` اللَّذَيْنِ · `ar:3` اللَّتَيْنِ · `ar:4` اللَّذَانِ · `ar:5` اللَّتَانِ · `ar:6` اللَّذَيْنِ · `ar:7` اللَّتَيْنِ
- `summary` (summary, blocks 25): `ar:0` الَّذِي · `ar:1` الَّتِي · `ar:2` الَّذِينَ · `ar:3` اللَّاتِي · `ar:4` اللَّوَاتِي · `ar:5` مَنْ · `ar:6` مَا · `ar:7` صِلَةٌ · `ar:8` الَّذِي نَجَحَ · `ar:9` اللَّذَانِ · `ar:10` اللَّتَانِ

