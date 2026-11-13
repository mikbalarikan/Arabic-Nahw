# "Particles" video (s3-particles): QA record (13 Nov 2026)

Render: `video/out/s3-particles/s3-particles-1080p.mp4` (8:01, 1920×1080, 30 fps, H.264 + AAC 48 kHz, faststart),
`s3-particles-720p.mp4`, `s3-particles.srt` (215 cues), `s3-particles-chapters.txt` (9), `s3-particles-thumbnail.jpg`.
Site copy (`make_video.py web`): `site/media/s3-particles/` (720p MP4 6.4 MiB, HLS, VTT, poster), entry in `site/media/videos.json`.
Voice: Supertonic 3, style M4. Source: the `notes` blocks of `content/stage3/u7_particles.py` (all 29 blocks, in order).

| Check | Result | How |
|---|---|---|
| Every Arabic string is exactly from the unit file | ✅ 89 checked, 0 errors (16 warnings: words that end in a long vowel, فِي حَتَّى لَا بَلَى, or are followed by ؟ / ،) | `check_arabic.py` (lesson.json `sources`) |
| Every Arabic clip ends with the written vowel / tanween / sukūn | ✅ 80 / 80 | `check_endings.py` (wav2vec2 phonemes) |
| Inside sounds of the clips the ending check cannot see | ✅ أَمَا read a-m-ā, not أَمَّا (3 clips, other seed); أَوِ اللَّبَنَ read "awillabana" (3 clips, voice-only spelling أَوِلَّبَنَ) | `voice_s3_particles.py` (phoneme rules, choices in `audio/choices_voicefix_s3_particles.json`) |
| One-letter ḥarfs joined to a word (بِـ لِـ كَـ وَ فَ أَ) never read alone | ✅ the whole word or sentence is read | script review |
| Script: Arabic / iʿrāb, Stage 3 scope (every ḥarf fixed, no place; what each group does to the next word as the lesson says it; no inna, no present verbs) | ✅ no must-fix; wording fixes applied | independent reviewer 1 |
| Script: coverage and order of all blocks, cues, highlights, style (short sentences, no em-dash, site terms) | ✅ every block, row, card, example, note and summary line covered and cued; all 19+ highlights match the visible text | independent reviewer 2, then revision |
| Continuity (back references, terms, phrases a TTS voice reads badly) | ✅ applied: "the ḥarf that means …" instead of "the ḥarf for …", "particle" linked to "ḥarf" in the intro, etc. | continuity pass |
| Visuals while spoken: row shown and marked while read, full Arabic sentence visible while read, boxes when said, nothing cut off | ✅ after one fix round | 165 cue-time and scene end-frames, two independent reviewers |
| Loudness | ✅ −14.5 LUFS integrated, true peak −1.5 dBTP (mix) | `audio_tools.py mix`, ebur128 on the final file |
| Site: the lesson page plays the video, chapter buttons seek, on a server WITHOUT Range support | ✅ `python3 -m http.server` (Range → 200): HLS via hls.js, play, chapter 3 → 2:51 | browser check |
| Live: https://arabic-nahw.pages.dev/#s3-particles | ✅ manifest has the video (HLS `hls-b57dc7a9`); plays, chapter 6 → 5:52 | browser check after deploy |

Fix round 1 (from the frame QA): the Arabic lists in the five group cards are read right to left in the video
(the site writes them in an LTR line, see below); table wash and header no longer stick out of the rounded card;
Arabic-only table columns have right-aligned headers; the Arabic in a box title (When to use بَلَى) is bold like the
rest; worked-example cards use a fixed Arabic column; the watermark الحُرُوفُ lights up while it is read.

Shared tools:
- None left in this lesson's commit: the versions on `main` (from the other Stage 3 videos) already contain what this
  video needs (`sources` in lesson.json for check_arabic; a final ؟ / ، is not part of the ending; alif maqṣūra ى
  counts as a long-vowel ending). The 80 clips were checked again with main's check_endings: 80 ok.

Known, accepted:
- HyperFrames warns about dead stretches (a table row stays still while it is read) and type below 28 px (the top
  bar, the eyebrow): same as the other lesson videos.
- `text_occluded` at two moments: mid-crossfade between two scenes, and a ":" next to a highlighted Arabic word in
  the green rule box; the frames show both fine.
- أَوْ on its own never came out right in 24 attempts × 8 spellings, so the narration says "the ḥarf that means or"
  and reads أَوِ اللَّبَنَ and the full example instead.

For the teacher (content, not changed here):
- In the lesson's group cards the Arabic lists (`{مِنْ}، {إِلَى}، {فِي} …`) sit in an English (LTR) line, so on the site
  they read left to right with the "…" on the right. The video shows them right to left.
- The Question card's heading is الِاسْتِفْهَامُ, while the other cards say حُرُوفُ … / حَرْفُ ….
