# "Iʿrāb in the Qur'an" video (lesson id `quran-nasb`): script format and narration rules

The video follows the lesson's Intro tab (`content/quran.py`, `QN.build()`) and then walks through
the 10 verses with their answer key (`QN.key`). The data is in `lesson.json`
(made by `video/tools/export_quran_nasb.py`). Format and timing work as in the Naṣb video
(`video/lessons/nasb/SCRIPT_SPEC.md`): a list of short **segments**, each one spoken clause plus
the visual **cues** that fire when it starts. The voice drives the clock. Nobody types a timestamp.

## Segment

```json
{ "id": "v01-04", "scene": "v01", "lang": "en", "text": "Who disobeyed?", "pause": 0.5, "cues": ["ask:1"] }
```

- `id`: unique, `<scene>-<two digits>` in order.
- `scene`: scene id (list below).
- `lang`:
  - `en`: English narration (TTS).
  - `ar`: one Arabic word or short phrase read by the TTS voice, to point out an ending.
  - `qr`: **the verse fragment, recited by a real reciter** (a licensed recording, cut to the fragment).
    It is never synthetic. `text` must be exactly the verse's `sentence` from `lesson.json`.
- `text`: what is spoken. For `ar`: ONLY a word exactly as written in the verse's `words` list
  (for example `رَبَّهُ`, `الأَبْوَابَ`, `وَعَصَى`), or the hidden doer exactly as in `lesson.json`
  (`(هُوَ)`, `(هِيَ)`). In chapter 1, also a word or phrase exactly as written in the notes
  (`قَدَّتْ`, `نُوحٌ`, `غَلَّقَتِ الأَبْوَابَ` ...). Do not read box pieces with a joining stroke (`رَبَّـ`, `ـهُ`): read the whole
  written word instead. Never invent Arabic. Never put Arabic inside an `en` segment.
- `pause`: silence after the segment, in seconds. Default 0.25. Use 0.5–0.7 after a question the
  viewer should answer in their head, 0.4–0.6 around `ar` readings, 0.8 after a `qr` recitation.
- `cues`: visual actions that start with this segment (may be empty).

## About the recitation (important)
- Each verse is recited **once** (`qr`), right after its English meaning. Verse 1 is recited a second
  time at the very end of its scene, as a model ("Listen to the verse once more.").
- A reciter may stop on the last word of a fragment. Then its ending is not heard. So never say
  "listen to the ending" about a `qr` segment. Endings are pointed out only with `ar` single-word
  readings and the vowel circle (`vowel:<g>`).
- Do not comment on recitation, tajwīd, or meaning beyond the lesson's own translation. No tafsīr.
  Speak about the verses with respect and keep to grammar.
- The on-screen text is the lesson's simplified standard spelling, not the Uthmani script.
  Say once, in chapter 3, that each verse is a short piece of a longer verse.

## Scenes (kinds) and their cues

| Scene id | Kind | Shows | Cues |
|---|---|---|---|
| `hero` | hero | Teal hero card: eyebrow, title, subtitle, watermark القُرْآن | `title`, `sub` |
| `c01-title`, `c02-title`, `c03-title` | chapter | Numbered chapter heading (+ grey sub-line for chapter 3) | `title`, `sub` |
| `c01-notes` | notes | The three note cards of chapter 1 | `note:1`, `note:2`, `note:3` |
| `c01-also` | also | The yellow "Also" tip box | `show` |
| `c02-key` | colourkey | Six colour cards + old small boxes row | `key:verb`, `key:doer`, `key:obj`, `key:purp`, `key:when`, `key:state`, `old` |
| `c03-overview` | overview | The 10-verse table (verse, reference, jobs inside) | `row:1` … `row:10`, `rows` (all remaining rows at once) |
| `v01` … `v10` | verse | One verse card (see below) | see below |
| `outro-yourturn` | yourturn | "4 Your turn": the 10 fragments with endings missing | `show` |

### Verse scene cues
The verse card shows, from the top: number, English meaning and reference; the verse in coloured
group boxes; the answer-key lines (one per piece: piece, coloured pill, reason).
- `en`: number + English meaning + reference appear.
- `sentence`: the verse appears large in plain (uncoloured) boxes. Put it on the `qr` segment.
- `recite`: a thin gold frame glows around the verse while it is recited, and the reciter credit
  appears in the corner. Put it on the `qr` segment, together with `sentence` on the first one.
- `group:<g>`: group box `g` (0-based, in the order of `groups` in `lesson.json`) takes its role
  colour, with its small word labels. The hidden doer box shows with its group.
- `ask:<g>`: a soft "?" on group `g` while its question is asked.
- `vowel:<g>`: the final-vowel circle of the head word of group `g` pulses twice.
- `line:<i>`: answer-key line `i` (0-based, the order of `key_lines` in `lesson.json`) appears.

Every key line of every verse must be shown (cue) by the end of its scene. Lines for particles (وَ, فَ,
مِنْ …) and fixed pieces may be shown two or three at a time, with one short sentence
("And is a particle. It never changes."). The naṣb word of each verse always gets its own question,
its own `ar` reading and its own sentence.

## Narration rules
- English, for English-speaking students. Calm teacher voice, about 145 words per minute.
- Plain, short sentences. One idea per sentence. No em-dashes, no semicolons.
- Use the site's terms exactly: verb, doer, hidden doer, object, purpose, time / place (say "time
  or place", or "time" when the lesson says time), state, fixed, particle, owner (ownership),
  owned, attached pronoun, adjective, "after a preposition", "after wa" for وَ, rafʿ, naṣb, jarr,
  damma, fatha, kasra, sukūn, tanween, al.
- Stay inside Stage 2: past verbs and order verbs only, no present verbs. Fatha (with or without
  tanween) is the only sign of naṣb. Do not add grammar the lesson does not teach. Names that take
  no tanween: say only what the lesson says ("Some names never take tanween. One damma or one
  fatha only."). Do not use the word "diptote".
- Teach the lesson's own reasons (the key lines), in the key's order where it reads well, using
  its questions: who? what? whom? when? how?
- Use the lesson's translation for each verse (`tr`), word for word, when giving its meaning.
  Say the surah name from `ref_en` ("From Surah Ta-Ha."). Do not read the verse numbers aloud.
- Spell nothing in transliteration inside `en` text except: iʿrāb (the lesson's title word), rafʿ,
  naṣb, jarr, al, wa, tanween, sukūn, and the surah names. If an Arabic word must be heard, put it in an `ar` segment.
- Names in English as the lesson writes them: Adam, Nuh, Sulayman, Dawud. For Allah as doer, follow
  the lesson: "He" (capital in text), hidden doer (هُوَ).

## Model: verse 1 (all other verses follow this rhythm, a little faster)

```json
[
 {"id":"v01-01","scene":"v01","lang":"en","text":"Verse one. From Surah Ta-Ha. And Adam disobeyed his Lord.","pause":0.5,"cues":["en"]},
 {"id":"v01-02","scene":"v01","lang":"qr","text":"وَعَصَى آدَمُ رَبَّهُ","pause":0.8,"cues":["sentence","recite"]},
 {"id":"v01-03","scene":"v01","lang":"en","text":"First, the verb. Disobeyed. It is a past verb, so it is fixed.","pause":0.3,"cues":["group:0","line:1"]},
 {"id":"v01-04","scene":"v01","lang":"en","text":"The wa before it means and. It is a particle. It never changes.","pause":0.3,"cues":["line:0"]},
 {"id":"v01-05","scene":"v01","lang":"en","text":"Who disobeyed?","pause":0.5,"cues":["ask:1"]},
 {"id":"v01-06","scene":"v01","lang":"ar","text":"آدَمُ","pause":0.4,"cues":["group:1","vowel:1"]},
 {"id":"v01-07","scene":"v01","lang":"en","text":"Adam. He is the doer, so he takes rafʿ, with damma.","pause":0.3,"cues":["line:2"]},
 {"id":"v01-08","scene":"v01","lang":"en","text":"Only one damma, no tanween. Some names never take tanween.","pause":0.4,"cues":[]},
 {"id":"v01-09","scene":"v01","lang":"en","text":"Whom did he disobey?","pause":0.6,"cues":["ask:2"]},
 {"id":"v01-10","scene":"v01","lang":"ar","text":"رَبَّهُ","pause":0.4,"cues":["group:2","vowel:2"]},
 {"id":"v01-11","scene":"v01","lang":"en","text":"His Lord. That is the object, so it takes naṣb. Its sign is fatha.","pause":0.3,"cues":["line:3"]},
 {"id":"v01-12","scene":"v01","lang":"en","text":"His is an attached pronoun at the end of the word. It is the owner, and it is fixed.","pause":0.3,"cues":["line:4"]},
 {"id":"v01-13","scene":"v01","lang":"en","text":"Because Lord is owned, it has no tanween. Just one fatha.","pause":0.4,"cues":[]},
 {"id":"v01-14","scene":"v01","lang":"en","text":"Listen to the verse once more.","pause":0.3,"cues":[]},
 {"id":"v01-15","scene":"v01","lang":"qr","text":"وَعَصَى آدَمُ رَبَّهُ","pause":0.9,"cues":["recite"]}
]
```

## Scene ids, in order
`hero`, `c01-title`, `c01-notes`, `c01-also`, `c02-title`, `c02-key`, `c03-title`, `c03-overview`,
`v01` … `v10`, `outro-yourturn`.

## Parts (rendered separately; see `parts.json`)
`p01-intro` (hero, c01) · `p02-key-verses` (c02, c03) · `p03-verses-1-3` · `p04-verses-4-6` ·
`p05-verses-7-8` · `p06-verses-9-10` (+ outro).
