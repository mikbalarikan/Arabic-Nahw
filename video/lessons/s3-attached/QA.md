# "Attached pronouns" video (s3-attached): QA record (13 Nov 2026)

Source: `content/stage3/u2_attached.py` (Stage 3 unit 2, its 35 `notes` blocks = the lesson page).
Render: `video/out/s3-attached/s3-attached-1080p.mp4` (10:03, 1920×1080, 30 fps, H.264, AAC 48 kHz), `-720p.mp4`,
`s3-attached.srt` (279 cues), `s3-attached-chapters.txt` (9 chapters), thumbnail. On the site: `site/media/s3-attached/`
(720p MP4 for download, HLS for playback, VTT captions, poster). Voice: Supertonic 3, style M4 (the course voice).

| Check | Result | How |
|---|---|---|
| Every Arabic string is exactly from the lesson source | ✅ 272 checked, 0 errors (13 warnings: words ending in a long ī with no mark, as written in the lesson: فِي, كِتَابِي, لِي, مِنِّي) | `check_arabic.py` (now also allows `content/stage*/u*.py`) |
| No attached pronoun read on its own, no joining-stroke form, no single letter | ✅ pronouns are named in English ("the pronoun for he") and framed on screen; only whole written words are read (كِتَابُهُ, عَلَيْهِ, لَهُ ...) | script rules in `SCRIPT_SPEC.md`, both reviews |
| Every Arabic clip ends with its written vowel / tanween / sukūn | ✅ 98 / 98 | `check_endings.py` (wav2vec2 phonemes) |
| لِي and مِنِّي heard as "lī", "minnī" (the check passes any long-vowel ending) | ✅ chose the attempt whose phonemes are `l iː`, `m i n iː` (the first try sounded like "lēyē") | 14 attempts each, phonemes compared |
| Script: iʿrāb, "in the place of jarr / naṣb", Stage 3 scope | ✅ 0 errors; 4 wording fixes (order verb "read it" is an order, the helping kasra "is not jarr", the kasra of عَلَيْهِ "is not a sign of jarr", "the word for a letter you write is feminine") | independent Arabic/iʿrāb reviewer |
| Coverage and order: hero, 7 chapters, 3 tables (12 + 5 + 3 rows), 19 examples with notes, 4 rules, 5 tips, 5 summary items | ✅ every piece is revealed by a cue (the build stops otherwise); 17 findings fixed (English column of 6 table rows, missing frames, pauses, clearer wording) | independent fidelity/style reviewer, then a continuity pass |
| Short sentences, no em-dash or semicolon, allowed transliteration only | ✅ | reviews + grep |
| Layout: nothing cut off, site colours and markup | ✅ all 28 scene end-frames checked | `hyperframes snapshot` at every scene end |
| Full sentence visible while read; gold frame on the word being read or named | ✅ after one fix round (98 cue frames, two independent reviewers: 3 frames lost their frame when the same word was named and then read; sentence frames touched the letters; preposition-table headers did not line up with their cells; a frame crossed the line above in rule boxes) | 98 frames at the middle of every Arabic reading, then 18 re-shot frames |
| Loudness | ✅ −14.5 LUFS integrated, true peak -1.5 dBTP | `audio_tools.py mix` |
| Final MP4 matches the checked frames | ✅ 10 frames pulled from `s3-attached-1080p.mp4` across all chapters | ffmpeg |
| Plays on the site without byte ranges, chapter buttons seek | ✅ HLS through hls.js, 9 chapter buttons; "6 On a verb" jumped to 7:22 and kept playing | `python3 -m http.server` (answers Range requests with 200, like Pages), lesson page, video card |

Known, accepted:
- The table cells keep the site's styling; in the video the headers of the Arabic columns are aligned with their cells.
- A gold frame fades out about 0.4 s after its segment, so it can still be fading when the next word lights up.
- Rows of a table appear one by one; the table frame is drawn at its full height from the start (as in the Naṣb glance table).
- "Rule" boxes and tips quote Arabic with the Arabic comma inside English text, so a list like عَلَيْهِ، إِلَيْهَا reads right to left
  inside the line, exactly as on the lesson page.
