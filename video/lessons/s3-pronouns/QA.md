# "Separate pronouns" video (s3-pronouns): QA record (13 Nov 2026)

Render: `video/out/s3-pronouns/s3-pronouns-1080p.mp4` (8:23, 1920×1080, 30 fps CFR, H.264 High yuv420p, AAC 48 kHz
stereo, faststart), `s3-pronouns-720p.mp4`, `s3-pronouns.srt` (224 cues), `s3-pronouns-chapters.txt` (9),
`s3-pronouns-thumbnail.jpg` (1280×720: the hero over the four word tiles). Site copy: `site/media/s3-pronouns/`.
Voice: Supertonic 3, style M4 (the course voice). Source: `content/stage3/u1_pronouns.py` (`notes`), exported by
`video/tools/export_s3_pronouns.py`; scenes in `video/tools/scenes_s3_pronouns.py`.

| Check | Result | How |
|---|---|---|
| Every Arabic string is exactly from the unit file | ✅ 138 checked, 0 errors (13 warnings: فِي ends in a long vowel ×11; السَّاعَةُ؟ and الوَلَدُ؟ carry the ؟ of the source) | `check_arabic.py` (lesson.json `sources`) |
| Every Arabic clip ends with the written vowel / tanween / sukūn (no pause form) | ✅ 81 / 81 ok, 0 FAIL | `check_endings.py`; 16 clips needed the `respell` last resort (هُوَ → هُوَهْ, tanween → vowel + نْ, voice input only) |
| Script: Arabic and iʿrāb, the "place" (مَحَلّ) idea, Stage 3 scope | ✅ independent reviewer: no errors; 9 wording fixes taken (هُمْ / هُنَّ differ in the last letter too, "on the last letter" for أَنْتَ / أَنْتِ, pointing word هَذَا given its meaning, "after a preposition", tanween damma on طَالِبٌ) | subagent review |
| Script: every block in the page's order, cues, style | ✅ independent reviewer: every block covered (3 paragraphs, 4 tiles, 2 + 3 cards, 12 rows, 6 tips, rule, 2-row table, 6 examples + notes, 5 summary points); all `hl:` occurrences counted; fewer highlights in the rule box, two split segments so highlights land when said | subagent review, then a continuity pass (11 listening fixes) |
| No em-dash, no semicolon, short sentences, site terms | ✅ longest sentence 14 words | reviewers + grep |
| Layout | ✅ `hyperframes check`: 0 errors in all 5 parts. Warnings: `dead_stretch` (a teaching video holds still while the voice explains), `text_below_floor` (the auditor ignores CSS zoom; on screen the smallest reading text is about 21 px), hero watermark contrast (the site's design) | `hyperframes check` |
| Visuals when said; full sentence visible while read; table band on the row read; end frames complete | ✅ after one fix round. Round 1 (181 frames: every cue and Arabic reading + every scene end, two independent reviewers): empty table box before the rows (c03, c05), Arabic highlight band hanging onto the next line (c04 cards), هُوَ فِي الفَصْلِ broken over two lines (c06 tip). Fixed: table box transparent until its rows appear, Arabic highlight band at letter height, Arabic spans never wrap; also هُوَ highlighted in the rule box and each pronoun highlighted as the summary reads it. Round 2: fixed frames re-checked | frame extraction from the joined MP4 |
| Loudness | ✅ −14.5 LUFS integrated, true peak −1.5 dBTP | `audio_tools.py mix` |
| Subtitles and chapters | ✅ 224 cues from the script, Arabic right-to-left; 9 chapters (Introduction, 1–6, In short, Practice) | `make_video.py join` |
| Plays on the site without Range support, seeks | see below | local `python3 -m http.server` + live page |

Known, accepted:
- Lists of Arabic words joined by "،" inside English text (hero line, summary point 2) run left to right, exactly as
  on the lesson page (each word is its own isolated span in an English sentence). The narration reads them in the
  same order, and the summary highlights each word as it is read.
- The capital "I" in the tile and table is the site font's glyph.
