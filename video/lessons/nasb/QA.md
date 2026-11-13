# Naṣb video: QA record (13 Nov 2026)

Render: `video/out/nasb/nasb-1080p.mp4` (15:56, 1920×1080, 30 fps CFR, H.264 High yuv420p, AAC 48 kHz stereo,
faststart), `nasb-720p.mp4`, `nasb.srt` (363 cues), `nasb-chapters.txt` (14), `nasb-thumbnail.jpg` (1280×720).
Voice: Supertonic 3, style M4 (chosen by the teacher from four auditions).

| Check | Result | How |
|---|---|---|
| Every Arabic string is exactly from `content/lesson.py` / `course.py` | ✅ 108 checked, 0 errors (4 warnings: جَزْم, حَال, فِي ×2 are written without a final vowel in the lesson) | `check_arabic.py` |
| Every Arabic clip ends with the written vowel / tanween / sukūn (no pause form) | ✅ 107 / 107 | `check_endings.py` (wav2vec2 phonemes), stricter rules after QA round 1 |
| Phoneme converter for the Arabic voice option (`ar_g2p.py`) | ✅ independent two-reviewer check + adjudication; 1 entry and 4 general rules fixed | workflow `g2p-arabic-review` |
| Script: Arabic / iʿrāb, coverage and order, style | ✅ each part drafted, checked by two independent reviewers, revised; continuity pass | workflow `nasb-narration-script` |
| Order: hero → 1 … 11 → five questions → your turn; 23 examples, 6 tips, 3 sign cards, 4 case cards, colour key, glance table | ✅ | continuity pass + final QA content check |
| Harakat visible, letters joined, right-to-left order | ✅ | frame review of all 48 scene end-frames |
| Role colours exact (site palette, from `lesson.py` `R`) | ✅ | colours come from the source; frame review |
| Short sentences, no em-dash, site terms, Stage 2 only | ✅ (one 19-word sentence split after QA) | final QA content check |
| Boxes appear when said; full sentence visible while read; "?" on the asked word; underline on the read word | ✅ after two fix rounds (round 1: hidden small-box words, missing repeat underline; round 2: underline regression) | 73 cue-time frames, adversarial verification of every finding |
| Loudness | ✅ −14.7 LUFS integrated, true peak −1.5 dBTP | `audio_tools.py mix` (compressor + two-pass loudnorm) |
| Subtitles from the script, Arabic right-to-left, ≤ 2 lines × 42 chars | ✅ | `make_video.py join` |
| Plays everywhere | ✅ moov before mdat, no video timestamp gaps | atom walk, ffprobe packet scan |

Known, accepted:
- HyperFrames layout check flags Arabic line boxes as "overflow"; zoomed frames show the glyphs inside their boxes.
- A few contrast warnings come from the site's own palette (kept unchanged on purpose) or from mid-crossfade frames.
- Long examples (21) are scaled down to fit; labels are smaller there.
- Sign-card examples sit in an LTR line as on the site.
