# "Question words" video (s3-questions): QA record (13 Nov 2026)

Render: `video/out/s3-questions/s3-questions-1080p.mp4` (7:19, 1920×1080, 30 fps, H.264 + AAC 48 kHz),
`s3-questions-720p.mp4`, `s3-questions.srt` (207 cues), `s3-questions-chapters.txt` (9 chapters),
`s3-questions-thumbnail.jpg`. Site copy: `site/media/s3-questions/` (720p MP4 + HLS + VTT + poster).
Voice: Supertonic 3, style M4 (the course voice). Source: `content/stage3/u5_questions.py` (notes blocks 0–22).

| Check | Result | How |
|---|---|---|
| Every Arabic string is exactly from the lesson source | ✅ 122 checked (89 `ar` segments + 33 `hl:` cues), 0 errors. 27 warnings: 23 words followed by ؟ or ، (the checker reads the mark as "no vowel"), فِي ×4 (written without a final mark in the source) | `check_arabic.py` (now also reads `lesson.json` `sources`) |
| Every Arabic clip ends with its written vowel / tanween / sukūn (no pause form) | ✅ 89 / 89, 0 FAIL | `check_endings.py` (wav2vec2 phonemes) |
| Lone one-letter clips (أَ ×4, لِ ×1) read as one syllable | ✅ after an audition: the default attempt read أَ as "a-ʔa" (two syllables); fixed choice "أَ." at speed 0.7 (one "a") and "لِ،" at 0.85 ("li"), stored in `choices_supertonic_M4.json` | envelope + phonemes of 12 variants each |
| Script: Arabic and iʿrāb | ✅ independent reviewer: no wrong grammar or Arabic; 8 clarity points applied (e.g. "the noun is jarr" instead of an ambiguous "it is jarr" after أَيُّ; "All of these are fixed" so the summary does not contradict أَيٌّ) | subagent review |
| Script: coverage, order, cues, style | ✅ independent reviewer: every block, row, example, tip, card and summary point cued and spoken in lesson order; 13 points applied (fragments like "For." rewritten, filler removed, one repeated "Madinah book" line dropped) | subagent review |
| Continuity (heard top to bottom) | ✅ 12 points applied (unclear "it" / "this one", lines ending on a bare preposition) | subagent pass |
| أَيٌّ flagged as the one flexible question ism | ✅ chapter 4 + summary: rafʿ أَيُّ, naṣb أَيَّ (object), jarr أَيِّ (after فِي), the noun after it is jarr as its owner | Arabic review |
| Short sentences, no em-dash or semicolon, Stage 3 scope (no present verbs) | ✅ | grep + reviews |
| Spoken text visible, markers on the right item, nothing cut off, END frames complete | ✅ after one fix round (below) | two independent frame reviewers, 172 cue and scene-end frames; fixes re-checked on 17 frames |
| `hyperframes check` | 0 layout errors. Accepted: contrast of the site's own gold rule title (#a87805 on #fff5d6, 3.6:1) and orange (4.46:1); text-size, "dead stretch" and "no sound" craft hints (the voice is muxed later) | `hyperframes check` per part |
| Loudness | ✅ −14.5 LUFS integrated, true peak −1.5 dBFS | `audio_tools.py mix` |

QA round 1 findings, all fixed before the final render:
- Tables: the empty table frame was full height while rows appeared → rows are now added one by one, the
  table grows downward from a fixed top. Headers over Arabic columns now align right like their cells.
  The gold cell marker poked out of the rounded corners → table clipped to its radius. In the 9-row table
  marks of neighbouring rows touched → more row height, smaller zoom.
- Gold markers stayed lit and piled up (5 at once in the rule box) → only one marker is lit at a time, and
  every single Arabic word read inside a box now gets its own marker (rule, tips, examples, summary); on
  Arabic the marker is a thin bar under the letters, so no vowel mark is covered.
- Summary: nothing showed which point was being read → earlier points dim when the next one starts.
- Example cards: Arabic sat against the English column with empty space on the left → Arabic centred in its
  column, wider gap; the أَ in the "written joined" note was too small → note Arabic larger.

Known, accepted:
- The site writes the answer's full stop inside the Arabic (`{مُحَمَّدٌ.} a person`), so a dot shows between the
  Arabic and the English in table 1, as on the site.
- The rule box title "أَيٌّ takes endings." runs straight into "أَيٌّ "which" is...", as on the site.
- The last gold frame / cell marker stays on the last item read at a scene's end.
