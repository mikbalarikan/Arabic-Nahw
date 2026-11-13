# Pointing words video (s3-demonstratives): QA record (13 Nov 2026)

Render: `video/out/s3-demonstratives/s3-demonstratives-1080p.mp4` (7:17, 1920×1080, 30 fps, H.264 + AAC 48 kHz),
`-720p.mp4`, `.srt` (228 cues), `-chapters.txt` (9), thumbnail (hero over the table to learn).
Site copy: `site/media/s3-demonstratives/` (720p MP4, HLS, VTT, poster) and its entry in `site/media/videos.json`.
Voice: Supertonic 3, style M4 (as nasb and quran-nasb). Source: `content/stage3/u3_demonstratives.py` (`notes`).

| Check | Result | How |
|---|---|---|
| Every block of the lesson page in order: hero, 6 chapters, 3 tables, 2 word tiles, 2 rule boxes, 5 tips, 5 col cards, 13 examples, the 5-point summary, then the Practice tab | ✅ 23 scenes, 228 segments | scene map in `scenes_s3_demonstratives.py`, INVENTORY.txt, fidelity review |
| Every Arabic string is exactly from the lesson source | ✅ 91 checked, 0 errors (4 warnings: فِي is written without a final mark) | `check_arabic.py` (lesson.json `sources`) |
| Every Arabic clip ends with the written vowel / tanween (no pause form) | ✅ 91 / 91 ok, 0 FAIL | `check_endings.py` |
| Hidden long ā of هَذَا، هَذِهِ، هَؤُلَاءِ، ذَلِكَ، هَذَانِ، هَذَيْنِ is said; the و of أُولَئِكَ is not | ✅ voice input uses the small (dagger) alif the lesson shows on هٰذَا, and أُلَائِكَ (a lesson spelling) for أُولَئِكَ; screen and subtitles keep the lesson's spelling | `say.json` + probe (clip lengths and phonemes: هَذَا read short without it) |
| Script: Arabic / iʿrāb (incl. هَذَانِ / هَاتَانِ flagged as NOT fixed, flexible, هَذَيْنِ / هَاتَيْنِ in naṣb and jarr, Stage 4) | ✅ no must-fix; 1 should-fix (أُولَئِكَ pronunciation) applied | independent reviewer 1 |
| Script: fidelity, order, cues, style (short sentences, no em-dash, site terms, Stage 3 only) | ✅ 15 findings applied (pauses before Arabic, full sentences after Arabic words, "Madinah lesson 5", summary split …) | independent reviewer 2, then continuity read |
| Full sentence visible while read; elements shown when said; gold highlight on the word being read (right duplicate) | ✅ 191 frames (every Arabic reading, every reveal cue, every scene end-frame) | two independent frame reviewers (parts 1–2, 3–4) |
| Layout: nothing cut off, Arabic phrases never broken across lines, harakāt visible | ✅ after one fix round | frame review round 1 → fixes → snapshots of the fixed frames |
| Loudness | ✅ −14.6 LUFS integrated, true peak −1.5 dBFS | `audio_tools.py mix` |
| Plays on the site without Range support, chapter buttons seek | ✅ local: plays (HLS), "5 Its place" seeks to 4:41 and keeps playing; live (def4069): plays, "6 Not fixed" seeks to 6:05 and keeps playing | `python3 -m http.server` on dist/, then https://arabic-nahw.pages.dev/#s3-demonstratives |

Fix round 1 (frame review): the inline gold highlight was taller than its line and covered the lines above and
below (sub-lines, example notes, rule box, summary), table-cell highlights spilled past the table border, the
highlight looked olive on the dark summary panel, the tanween of رَفْعٍ touched the line below, and c05-cols opened
on an empty stage. Fixed: inline Arabic is an inline-block no taller than its line, table cells get an inset
ring, the summary uses solid gold with dark text, more space under the place cards' Arabic, `col:1` on the first line.
Earlier, from the end-frame snapshots: an Arabic phrase wrapped across two lines (c03-cols) and the three place
cards squeezed their titles; fixed with `white-space: nowrap` on inline Arabic and a stacked card header.

Known, accepted:
- 4 clips use the existing `respell` fallback of `tts_generate.py` (voice input only): هُوَ (c03-tips-03),
  سَاعَةٌ (end of c04-examples-02), رَفْعٍ (c05-cols-03), جَرٍّ (c05-cols-09). Same method the teacher approved for quran-nasb.
- The hidden-alif and أُولَئِكَ pronunciation is checked by clip length and the phoneme model only, not by ear.
- HyperFrames check: contrast warnings come from the site's own palette (orange rule title #b05705 on #fff0df, 4.46:1)
  or mid-fade frames; Arabic glyph boxes taller than their line boxes are marked `data-layout-allow-overflow`.
- A space before "،" / "." after inline Arabic and the lowercase English of phrase examples ("in this house") are
  the lesson page's own text, kept as on the site.
