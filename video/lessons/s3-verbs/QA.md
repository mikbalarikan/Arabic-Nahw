# "Fixed verbs: past and order" video (s3-verbs): QA record (13 Nov 2026)

Render: `video/out/s3-verbs/s3-verbs-1080p.mp4` (8:31, 1920×1080, 30 fps, 224 subtitle cues), `s3-verbs.srt`, `s3-verbs-chapters.txt`
(11 chapters), thumbnail. Site copy: `site/media/s3-verbs/` (720p MP4 7.3 MiB, HLS, VTT, poster).
Voice: Supertonic 3, style M4 (English and Arabic). 221 segments, 72 Arabic readings, 33 scenes in 6 parts.

| Check | Result | How |
|---|---|---|
| Every Arabic string is exactly from `content/stage3/u6_verbs.py` | ✅ 74 checked, 0 errors (12 warnings: words ending in a long-vowel letter ـوا / ـا / ـي and the ؟ / ، after a word, which have no mark on the last letter) | `check_arabic.py` (`sources` in lesson.json) |
| Every Arabic clip ends with its written ending | ✅ 72 / 72 | `check_endings.py`, now also hears long endings: ـُوا must end in u, ـَا in a, ـِي in i (before, these passed without listening) |
| Every Arabic clip is whole, and the order verbs start with the right helping alif | ✅ 72 / 72 after re-making 11 clips | `check_clips_s3_verbs.py` (see below) |
| Script: Arabic / iʿrāb of the 14 past and 5 order forms, built-on claims, doer claims | ✅ no error in the forms; 9 wording fixes (e.g. "last letter" meant two letters; "the ending for two" was ambiguous) | independent reviewer 1 |
| Script: every block, row, card, tile, example, note, tip and summary point shown and said, in order; style; cue indexes and `hl:` phrases | ✅ after 15 fixes (repetition in the order table and doer tiles, "this word" with nothing marked, outro naming a task not on the Practice tab) | independent reviewer 2, then a continuity read of the whole script |
| Stage 3 scope (present verb only named), short sentences, no em-dash | ✅ | both reviewers |
| Layout | ✅ `hyperframes check`: no layout errors; Arabic text boxes marked `data-layout-allow-overflow` as in quran-nasb | 6 parts |
| Boxes / rows / rings appear when said; the read sentence is whole and framed while read; nothing cut off | ✅ after one fix round | 197 frames (every cue + every scene end), two independent reviewers; fixed frames re-checked |
| Loudness | ✅ −14.5 LUFS integrated, true peak −1.5 dBTP | `audio_tools.py mix` |

## Arabic clips: what went wrong and how it was fixed
- The voice read the helping alif of the order verbs as "a" or "i": اُكْتُبْ as "aktub", اُكْتُبُوا as "iktubū". Chapter 7 teaches
  exactly this vowel, so `check_clips_s3_verbs.py` checks the first vowel of every clip that starts with اُ / اِ. Spelling it
  أُكْتُبْ for the voice did not help (still "aktub"); a bare hamza with the vowel, ءُكْتُبْ / ءِ, gives "uktub" every time.
  That is the voice input only (stored in `audio/choices_supertonic_M4.json` under `<id>|clip`); the screen shows اُكْتُبْ.
- `هَلْ كَتَبْتَ الدَّرْسَ؟ لَا، مَا كَتَبْتُهُ` came out as "… mā katabtu": the ـهُ "it" was lost, but the ending check passed
  because the clip still ended in u. The new whole-clip check compares every clip with `ar_g2p.py`'s reading (coarse sound
  classes, similarity ≥ 0.72, and the last four sounds) and caught it; the clip was re-made ("… mā katabtuhu").
- Re-make these clips with `check_clips_s3_verbs.py MODEL --fix [--redo --only id]`, not with `tts_generate.py --force`.

## Fixed after the frame review
- Table frames now grow with their rows (no empty white body); headers of Arabic columns are right-aligned over their Arabic;
  the Doer column of the order table has one alignment and size; the gold ring of the previous row goes when the next row
  is read (two rings showed at once); the example cell of the "built on" table is ringed while its verbs are read.
- مَا is marked inside نَحْنُ مَا خَرَجْنَا مِنَ البَيْتِ when it is read; the grey rule title is one step darker; card titles,
  tips and notes wrap without a lone last word; the marker of the c06 rule no longer hangs under an Arabic letter.

## Known, accepted
- The note under example 3 of chapter 2 says "See … below", as on the lesson page (the video shows the page's text; the
  narration says "we come back to it in chapter five").
- `hyperframes check` contrast error on the hero card at its fade in/out (mid-crossfade) and on the site's faint watermark.
- In a few sentences the voice puts a glottal stop before ال after a pause-free word (اِفْتَحِ البَابَ: "iftaḥi ʔal-bāba"); the
  helping kasra itself is heard. The question in example 4 of chapter 5 pauses on الدَّرْسَ before ؟.
- A sub-line under a chapter title appears whole while its first sentence is read.
