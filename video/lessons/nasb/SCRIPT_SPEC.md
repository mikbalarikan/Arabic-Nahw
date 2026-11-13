# Naṣb video: script format and narration rules

The video follows the lesson page (`content/lesson.py`) in order. The voice drives the clock:
the script is a list of short **segments**. Each segment is one spoken clause (English) or one
Arabic reading, plus the visual **cues** that fire when it starts. Audio is generated per
segment, measured, and the scene timing comes from those lengths. Nobody types a timestamp.

## Segment

```json
{ "id": "c06-ex1-04", "scene": "c06-ex1", "lang": "en",
  "text": "What did he write?", "pause": 0.6, "cues": ["ask:2"] }
```

- `id`: unique, `<scene>-<two digits>` in order.
- `scene`: scene id (see below).
- `lang`: `en` (narration) or `ar` (Arabic reading).
- `text`: what is spoken. For `ar`, ONLY an exact string from the lesson (a full example sentence,
  or a single word exactly as it appears in a word box or reason line). Never invent Arabic.
  Never put Arabic inside an `en` segment: split it into its own `ar` segment.
- `pause`: silence after the segment, in seconds. Default 0.25. Use 0.5–0.7 after a question
  the viewer should answer in their head, and 0.4–0.6 before and after Arabic readings.
- `cues`: visual actions that start with this segment (may be empty).

## Scenes (kinds) and their cues

| Scene kind | Shows | Cues |
|---|---|---|
| `hero` | Teal hero card: eyebrow, title, subtitle, watermark النَّصْب | `title`, `sub` |
| `chapter` | Numbered chapter heading + its grey sub-line | `title`, `sub` |
| `cases` | Four case cards A–D | `case:A` … `case:D` |
| `scope` | "Today we keep it simple" box, two bullets | `scope:1`, `scope:2` |
| `rules` | Verb · fixed and Doer · rafʿ rule cards | `rule:verb`, `rule:doer` |
| `example` | One example card (see below) | see below |
| `careful` | The "Careful" tip box | `show` |
| `signs` | Three sign cards | `sign:1`, `sign:2`, `sign:3` |
| `colourkey` | Six colour cards + old small boxes row | `key:verb`, `key:doer`, `key:obj`, `key:purp`, `key:when`, `key:state`, `old` |
| `glance` | Four-row table | `row:obj`, `row:purp`, `row:when`, `row:state` |
| `rulebox` | The chapter's coloured Rule box (chapters 6–9) or sub-line (10) | `show`, `hl:<phrase>` (highlights a phrase of the rule text) |
| `five` | "Iʿrāb in five questions" box | `q:1` … `q:5` |
| `yourturn` | Invitation to the Practice tab | `show` |

### Example scene cues
The example card shows, from top: number + English meaning, the Arabic sentence in coloured
group boxes, the reason lines, and the tip (if any).
- `en`: the English meaning appears.
- `sentence`: the plain Arabic sentence appears large (no boxes yet).
- `read:<w>`: thin gold underline under word `w` (0-based, in reading order, hidden doer not counted) while it is spoken.
- `group:<g>`: group box `g` (0-based, in the order of the lesson's groups: verb first) takes its role colour, with its small word labels.
- `ask:<g>`: a soft "?" focus on group `g` while its question is asked.
- `vowel:<g>`: the final-vowel circle of the head word of group `g` pulses twice.
- `line:<i>`: reason line `i` (0-based, lesson order) appears with its coloured pill.
- `tip`: the tip box appears.

Every reason line and every tip of the lesson must be shown (cue) AND covered by the narration.

## Narration rules
- English, for English-speaking students. Calm teacher voice, about 145 words per minute.
- Plain, short sentences. One idea per sentence. No em-dashes, no semicolons.
- Use the site's terms exactly: verb, doer, object, purpose, time / place (say "time or place"),
  state, fixed, owner / owned, adjective, "after a preposition", "after wa" for وَ in English text
  (say "after wa"), rafʿ (write "rafʿ", say it as "raf"), naṣb ("nasb"), jarr, damma, fatha, kasra,
  sukūn, tanween, ال (in English text write "al").
- Stay inside Stage 2: past verbs and order verbs only, no present verbs; fatha is the only sign of naṣb.
  Do not add grammar the lesson does not teach.
- Teach the lesson's own reasons, in the lesson's order, using its questions (what? whom? why? when? where? how?).
- Spell nothing in transliteration inside `en` text except: rafʿ, naṣb, jarr, al, wa, tanween, sukūn.
  If a word must be heard, put it in an `ar` segment.
- Read every example sentence in Arabic once, slowly, after its English meaning. In the first
  example of each chapter, read it again at the end. Single words are read in `ar` segments when they
  are being explained.

## Example rhythm (example 1, the model for all others)

```json
[
 {"id":"c06-ex1-01","scene":"c06-ex1","lang":"en","text":"Example one. The student wrote the lesson.","pause":0.4,"cues":["en"]},
 {"id":"c06-ex1-02","scene":"c06-ex1","lang":"ar","text":"كَتَبَ الطَّالِبُ الدَّرْسَ","pause":0.6,"cues":["sentence"]},
 {"id":"c06-ex1-03","scene":"c06-ex1","lang":"en","text":"First, the verb. Wrote. It is a past verb, so it is fixed.","pause":0.3,"cues":["group:0"]},
 {"id":"c06-ex1-04","scene":"c06-ex1","lang":"en","text":"Who wrote?","pause":0.5,"cues":["ask:1"]},
 {"id":"c06-ex1-05","scene":"c06-ex1","lang":"ar","text":"الطَّالِبُ","pause":0.3,"cues":["group:1","vowel:1"]},
 {"id":"c06-ex1-06","scene":"c06-ex1","lang":"en","text":"The student. That is the doer, so it takes damma.","pause":0.3,"cues":["line:0"]},
 {"id":"c06-ex1-07","scene":"c06-ex1","lang":"en","text":"What did he write?","pause":0.6,"cues":["ask:2"]},
 {"id":"c06-ex1-08","scene":"c06-ex1","lang":"ar","text":"الدَّرْسَ","pause":0.3,"cues":["group:2","vowel:2"]},
 {"id":"c06-ex1-09","scene":"c06-ex1","lang":"en","text":"The lesson. That is the object, so it ends in fatha.","pause":0.4,"cues":["line:1"]},
 {"id":"c06-ex1-10","scene":"c06-ex1","lang":"en","text":"Listen to the ending once more.","pause":0.3,"cues":[]},
 {"id":"c06-ex1-11","scene":"c06-ex1","lang":"ar","text":"كَتَبَ الطَّالِبُ الدَّرْسَ","pause":0.8,"cues":["read:2"]}
]
```

Later examples in a chapter move faster: the verb and the doer can be one short sentence
("The verb is fixed, and the doer takes damma."), unless the doer or verb is the point of the line.

## Scene ids
`hero`, `c01-title`, `c01-cases`, `c01-scope`, `c02-title`, `c02-rules`, `c02-exA`, `c02-exB`,
`c02-careful`, `c03-title`, `c03-signs`, `c04-title`, `c04-key`, `c05-title`, `c05-glance`,
`c06-title`, `c06-rule`, `c06-ex1` … `c06-ex4`, `c07-title`, `c07-rule`, `c07-ex5` … `c07-ex7`,
`c08-title`, `c08-rule`, `c08-ex8` … `c08-ex12`, `c09-title`, `c09-rule`, `c09-ex13` … `c09-ex16`,
`c10-title`, `c10-ex17`, `c10-ex18`, `c11-title`, `c11-ex19` … `c11-ex21`, `c11-five`, `outro-yourturn`.
A tip belongs to its example scene (cue `tip`).
