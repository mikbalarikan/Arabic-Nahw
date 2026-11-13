# Relative pronouns video (s3-relatives): QA record (13 Nov 2026)

Lesson: Stage 3, unit 4 `s3-relatives` (`content/stage3/u4_relatives.py`, its `notes` = the lesson page).
Render: `video/out/s3-relatives/s3-relatives-1080p.mp4` (9:19, 1920×1080, 30 fps CFR, H.264 + AAC 48 kHz, faststart),
`s3-relatives-720p.mp4`, `s3-relatives.srt` (224 cues), `s3-relatives-chapters.txt` (8 chapters), poster
`s3-relatives-thumbnail.jpg`. On the site: `site/media/s3-relatives/` (720p MP4, HLS, VTT, poster).
Voice: Supertonic 3, style M4 (English and Arabic).

## Pipeline
`export_s3_relatives.py` → `lesson.json` (26 blocks, rendered by the site's own `course.render_notes`, asserted equal
to the lesson page) → `SCRIPT_SPEC.md` + `parts/p1…p6` → `script.json` (20 scenes, 217 segments, 89 Arabic) →
`tts_generate.py --verify` → `check_endings.py` → `audio_tools.py measure` → `build_composition.py` with the lesson's
scene module `tools/scenes_s3_relatives.py` and `parts.json` (6 parts) → `mix` → `make_video.py render / join / web`.
Shared tools: only `check_arabic.py` changed (lesson.json `"sources"`, the same change as the other Stage 3 videos);
nasb and quran-nasb give the same result before and after (108 strings / 0 errors / 4 warnings; 49 / 0 / 0).

| Check | Result | How |
|---|---|---|
| Every Arabic string is exactly from the lesson source | ✅ 89 checked, 0 errors (46 warnings = words that end in a long-vowel letter, written so in the lesson) | `check_arabic.py` |
| Every Arabic clip ends with the written vowel / tanween / sukūn (no pause form) | ✅ 89 / 89 ok, 0 FAIL | `check_endings.py` (wav2vec2 phonemes); `tts_generate.py --verify` |
| Script: Arabic and iʿrāb | ✅ independent reviewer: every `ar` text exact; grammar correct; اللَّذَانِ / اللَّتَانِ always "not fixed, flexible, اللَّذَيْنِ / اللَّتَيْنِ in naṣb and jarr, Stage 4"; nothing implies الَّذِينَ changes | review 1, then revision |
| Script: fidelity, order, cues, style | ✅ independent reviewer: every block in page order (hero, 4 table rows, 2 cards, 5 tips, 2 rules, 15 examples with notes, dual rule + table, 5 summary points); every cue on the segment that first talks about it | review 2, then revision |
| Continuity (one read-through after revision) | ✅ 6 wording fixes ("stand alone" scoped against the hero's "never stands alone"; the one exception named in the hero; clear "it") | continuity pass |
| Short sentences, no em-dash, no semicolon, Stage 3 scope, no present verbs | ✅ | reviews + script check |
| Layout: nothing cut off, Arabic vowelled and joined, site colours and markup | ✅ | `hyperframes check` (0 errors after marking Arabic glyph boxes, as quran-nasb does) + snapshots of every scene |
| Boxes / rows / examples appear when said; full Arabic item visible and lit while read; every element visible at scene end | ✅ after one fix round | round 1: 181 frames (every cue segment + every scene end-frame) from the joined MP4, two independent visual reviewers; round 2: a third reviewer confirmed all 5 fixes on ~50 new frames, no regressions |
| Loudness | ✅ −14.4 LUFS integrated, true peak −1.5 dBTP | `audio_tools.py mix`, ebur128 on the joined file |
| Site: plays and seeks from a server without Range support | ✅ HLS (blob source), chapter 5 button → 6:12 and keeps playing; web MP4 7.3 MiB, 57 HLS files | `python3 -m http.server` on `dist/`, then the live page |

## Fixes from the reviews
Script (before any audio): the hero no longer says the ending "never" changes (the dual pair is named as the one
exception); "stand alone" for مَنْ / مَا is explained as "no noun before them, a ṣila still after them"; spoken
ambiguities removed ("the word who joins…", "the verb he passed", "the words for the two who change"); "one male or
one masculine thing"; "the clause comes straight after the noun" (not "the verb"); padding cut; pauses before Arabic
raised to 0.4 s.

Video (QA round 1 → round 2): an underline that came 8 s before its phrase was moved to its own segment (c05-tip
split in two); the gold glow is now a band inside the word's own line (it spilled over table lines and card borders
because Noto Sans Arabic's line box is tall) and fades before the scene cuts; on the dark "In short" panel the glow is
a solid gold bar (see-through gold looked olive, the course colour for "state"); the dual table's Arabic is centred
under its headers; the poster's watermark is no longer clipped.

## Known, accepted
- HyperFrames flags the site's own orange rule title (#b05705 on #fff0df, 4.46:1) and text under its 28 px "phone
  floor": these are the course's fixed colours and sizes, unchanged on purpose (as in nasb and quran-nasb).
- In the two tips that list Arabic words inside an English sentence, the Arabic commas sit as on the lesson page.
- On the dark "In short" panel the gold bar under الَّذِي touches the two dots of its ي (summary-03, -18); the word stays readable.
- اللَّتَانِ is read 0.8 s before the chapter-6 title scene ends, so its glow is still fading in that scene's last frame.
- The small chapter heading stays at the top while the content is centred, which leaves an empty band above short lists.
