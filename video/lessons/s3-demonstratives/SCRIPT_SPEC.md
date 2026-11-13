# Pointing words video (s3-demonstratives): script format and narration rules

The video follows the lesson page (`content/stage3/u3_demonstratives.py`, its `notes` blocks) in order:
hero, chapters 1 to 6 with every block, the "In short" box, then an invitation to the Practice tab.
Same machinery as the Naṣb video (`video/lessons/nasb/SCRIPT_SPEC.md`): the voice drives the clock.
The script is a list of short **segments**; each is one spoken clause (English) or one Arabic reading,
plus the visual **cues** that fire when it starts.

## Segment

```json
{ "id": "c01-table-03", "scene": "c01-table", "lang": "ar", "text": "هَذَا", "pause": 0.4, "cues": ["mark:0"] }
```

- `id`: unique, `<scene>-<two digits>` in order.
- `scene`: one of the scene ids below, in the order below.
- `lang`: `en` (narration) or `ar` (Arabic reading).
- `text`: what is spoken. For `ar`: ONLY an exact Arabic string that is on screen in that scene (see the scene
  inventory `INVENTORY.txt`: every "mark" is such a string). Never invent Arabic, never build a new phrase.
  Never put Arabic inside an `en` segment: split it into its own `ar` segment.
  Do not read single letters (هـ، ذ، و، ل، ة) or ال in an `ar` segment: describe them in English
  ("the letter ha", "the letter waw", "ta marbuta", "al").
- `pause`: silence after the segment in seconds. Default 0.25. 0.4 to 0.6 around Arabic readings,
  0.5 to 0.7 after a question the viewer should answer in their head.
- `cues`: visual actions that start with this segment (may be empty).

## Scenes, in order, and their cues

`INVENTORY.txt` lists every scene with its lesson blocks (the exact text on screen) and its numbered Arabic
**marks**. Every scene accepts `mark:<k>`: the Arabic element k of that scene gets a gold highlight while the
segment plays. An `ar` segment with no mark cue lights the first element whose text is exactly the segment's
text, so a mark cue is only needed to pick a later duplicate (for example the second هُنَا) or to point at a word
while English is spoken.

| Scene id | Kind | Shows (lesson block) | Cues |
|---|---|---|---|
| `hero` | hero | Hero card "This, that, these, those", watermark هَذَا | `title`, `sub` |
| `c01-title` | chapter | "1 The table to learn" + paragraph (block 2) as its sub-line | `title`, `sub` |
| `c01-table` | table | Near/Far × one male/one female/plural table (block 3). Header shows from the start | `row:1` (Near), `row:2` (Far), `mark:k` |
| `c01-words` | words | Tiles هُنَا here, هُنَاكَ there (block 4) + the Madinah paragraph (block 5) | `word:1`, `word:2`, `p`, `mark:k` |
| `c01-rule` | box | Teal rule "Learn the last vowel too" (block 6) | `show`, `hl:<phrase>`, `mark:k` |
| `c01-tip` | box | Tip: هَؤُلَاءِ / أُولَئِكَ for people; هَذِهِ for plural things (block 7) | `show`, `hl:<phrase>`, `mark:k` |
| `c02-title` | chapter | "2 Reading tips: hidden and extra letters" + paragraph (block 9, with هٰذَا) | `title`, `sub`, `mark:0` |
| `c02-table` | table | Written / Said / Why, five rows (block 10) | `row:1` … `row:5`, `mark:k` |
| `c02-tip` | box | Tip: do not write the hidden alif (block 11) | `show`, `hl:<phrase>`, `mark:k` |
| `c03-title` | chapter | "3 "This is a book" or "this book"?" + paragraph (block 13) | `title`, `sub` |
| `c03-cols` | cols | Two cards: No ال: a sentence / With ال: a phrase (block 14) | `col:1`, `col:2`, `mark:k` |
| `c03-examples` | examples | Four example rows (block 15): Arabic, English, note | `ex:1` … `ex:4`, `mark:k` |
| `c03-tips` | tips | Two tips (blocks 16, 17): هُوَ / هِيَ in the middle; iḍāfa | `tip:1`, `tip:2`, `mark:k` |
| `c04-title` | chapter | "4 هَذَا or هَذِهِ? Follow the noun" + paragraph (block 19) | `title`, `sub` |
| `c04-examples` | examples | Four example rows (block 20) | `ex:1` … `ex:4`, `mark:k` |
| `c05-title` | chapter | "5 Its place in the sentence" + paragraph (block 22) | `title`, `sub` |
| `c05-examples` | examples | Five example rows (block 23) | `ex:1` … `ex:5`, `mark:k` |
| `c05-cols` | cols | Three cards: place of rafʿ / naṣb / jarr (block 24) | `col:1`, `col:2`, `col:3`, `mark:k` |
| `c06-title` | chapter | "6 Not fixed: هَذَانِ and هَاتَانِ" (no sub-line) | `title` |
| `c06-rule` | box | Orange rule "The words for "these two" change" (block 26) | `show`, `hl:<phrase>`, `mark:k` |
| `c06-table` | table | Form / Two males / Two females (block 27) | `row:1` (Rafʿ), `row:2` (Naṣb and jarr), `mark:k` |
| `summary` | summary | "In short" box, five points (block 28); the title shows from the start | `item:1` … `item:5`, `mark:k` |
| `outro-yourturn` | yourturn | "Your turn": the six Practice card titles | `show` |

Rules for cues:
- Everything that is on screen must appear by a cue (rows, tiles, paragraph, cards, example rows, tips, summary
  items, boxes with `show`) at the moment the narration reaches it, never later than it is read.
- An Arabic string must be visible (its row / card / box already shown) when it is read.
- `hl:<phrase>`: an exact phrase of the box's English text (as in INVENTORY.txt), highlighted in gold
  while said. Use at most 3 per box. Phrases must be unique in the box and must not cross Arabic.
- Every block of the lesson must be shown AND covered by the narration: every row, every example's English
  meaning and its note, every tip, every summary point. Example notes are read in English (with the Arabic
  word in its own `ar` segment where the note names one).

## Narration rules
- English, for English-speaking students. Calm teacher voice, about 145 words per minute.
- Plain, short sentences. One idea per sentence. No em-dashes, no semicolons.
- Site terms exactly: pointing word, near, far, fixed, flexible, Topic, Information, doer, object, owner,
  after a preposition, place of rafʿ / naṣb / jarr, damma, fatha, kasra, alif, sukūn, tanween, al (for ال),
  iḍāfa, phrase, sentence. Write "rafʿ" (said raf), "naṣb" (nasb), "jarr".
- Stay inside Stage 3 (`content/stage3/SPEC.md`): only past verbs in examples (as the lesson has), no present verbs.
  هَذَانِ and هَاتَانِ are the exception the lesson flags: they are NOT fixed (flexible), become هَذَيْنِ / هَاتَيْنِ in
  naṣb and jarr, and are learnt with the dual in Stage 4. Say exactly that and no more (no dual grammar).
  A pointing word never shows rafʿ, naṣb or jarr on itself: the noun after it shows the ending.
  The kasra of هَذِهِ / هَؤُلَاءِ and the fatha of ذَلِكَ / تِلْكَ / أُولَئِكَ are fixed endings, not signs of jarr or naṣb.
- Transliteration: the "Said" column of chapter 2 shows how the words sound. Do not spell it in English text;
  let the viewer hear the word in an `ar` segment instead (the voice is given the hidden-alif spelling).
  Allowed Latin terms only: rafʿ, naṣb, jarr, al, iḍāfa, tanween, sukūn, alif, damma, fatha, kasra,
  and the letter names ha, dhal, lam, waw, ta marbuta. Say "Hamid" for حَامِد in English. "Madinah lesson 5" may be said.
- Teach the lesson's own reasons, in its order. Do not add grammar it does not teach.
- Read every Arabic example sentence once, slowly, after its English meaning (in chapters 3 to 5).
  Read the six table words in chapter 1 one by one with their meaning. In chapter 2 read each written word
  once so the viewer hears the hidden ā.
- The Qur'an is only mentioned (the small alif on هٰذَا). No verse is recited.

## Parts (rendered separately, `parts.json`)
`p01-table` (hero, c01), `p02-reading` (c02, c03), `p03-follow-place` (c04, c05), `p04-not-fixed` (c06, summary, outro).
