# Lesson videos

Narrated videos made from the lesson pages in `content/`. The first one is the Naṣb lesson
(`nasb`, "Naṣb Colour Guide"). Everything on screen comes from the lesson source and the
site's own CSS, so the video looks like the site and cannot drift from it.

```
content/lesson.py ──export_lesson.py──▶ lessons/nasb/lesson.json
                                         lessons/nasb/script.json  ◀── written + reviewed (SCRIPT_SPEC.md)
script.json ──check_arabic.py (must be 0 errors)
script.json ──tts_generate.py──▶ lessons/nasb/audio/raw/<segment>.wav ──check_endings.py
raw/ ──audio_tools.py measure──▶ audio/clips/ + timings.json
lesson.json + script.json + timings.json ──build_composition.py──▶ build/nasb/<part>/index.html + plan.json
plan.json + clips ──audio_tools.py mix──▶ build/nasb/<part>/voice.wav (-14 LUFS for the whole lesson)
build/ ──make_video.py render──▶ out/nasb/parts/*.mp4 ──make_video.py join──▶ out/nasb/*.mp4, .srt, chapters
```

## Tools you need (no admin rights needed)
- Node 22+ and ffmpeg on `PATH` (this Mac: `~/.local/bin`).
- `npm install` in `video/` (HyperFrames, GSAP, the Noto fonts; pinned in `package.json`).
- Python 3.11 with `numpy soundfile onnxruntime supertonic` for the voice and audio steps
  (this Mac: `~/Projects/nasb-tts/.venv`). The Supertonic 3 model and the phoneme model
  (`onnx-community/wav2vec2-lv-60-espeak-cv-ft-ONNX`, `model_q4.onnx`, plus `vocab.json` from
  `facebook/wav2vec2-lv-60-espeak-cv-ft`) live outside the repo.

## Run it (from the repo root)
```bash
PY=~/Projects/nasb-tts/.venv/bin/python
python3 video/tools/export_lesson.py
python3 video/tools/assemble_script.py nasb          # joins lessons/nasb/parts/p*.json
python3 video/tools/check_arabic.py video/lessons/nasb/script.json
$PY video/tools/tts_generate.py --en supertonic:M4 --ar supertonic:M4 --verify ~/Projects/nasb-tts/models/phoneme
$PY video/tools/check_endings.py ~/Projects/nasb-tts/models/phoneme video/lessons/nasb/audio/raw   # must be 0 FAIL
$PY video/tools/audio_tools.py measure nasb
python3 video/tools/build_composition.py nasb
$PY video/tools/audio_tools.py mix nasb
python3 video/tools/make_video.py render nasb        # one part at a time; --only p01-intro,p02-verb-sentence
python3 video/tools/make_video.py join nasb
python3 video/tools/make_video.py web nasb           # the copy the course site plays (site/media/nasb/)
```
Check a part's layout before rendering: `cd video/build/nasb/p06-object && ../../../node_modules/.bin/hyperframes check .`
and look at frames with `hyperframes snapshot . --at 10,20,30`.

## On the site
`make_video.py web` writes `site/media/<id>/`: a 720p MP4 (offered as a download), the same video as
HLS segments in `hls-<hash>/`, captions (`.vtt`) and a poster, and adds the lesson to
`site/media/videos.json`. `tools/build_site.py` puts the video into that lesson's manifest entry and
the lesson page shows a closed "Watch this lesson as a video" card with chapter buttons.
Cloudflare Pages answers byte-range requests with the whole file, so a plain MP4 there cannot seek
and may not play on iPhones; that is why the player streams the HLS copy (Safari natively, other
browsers through hls.js). Every file must stay under the Pages limit of 25 MiB.

## The voice
Chosen by the teacher on 13 Nov 2026 from four auditions: **Supertonic 3, style M4** (Supertone,
BigScience OpenRAIL-M licence: say in the video description that the narration is AI-generated).
One voice reads both the English and the Arabic, fully on this Mac's CPU.

TTS voices like to read the last Arabic word in pause form (ad-dars instead of ad-darsa), which is
exactly what this lesson teaches against. So every Arabic clip is checked: `phonemes.py` turns the
clip into phonemes (wav2vec2 espeak model, ONNX) and `check_endings.py` compares the last sounds with
the written ending. `tts_generate.py --verify` retries a failing clip with small changes (a trailing
" -" or "!", speed, seed; and for -an words, the silent alif left out of the TTS input) and stores the
winning choice in `lessons/nasb/audio/choices_supertonic_M4.json`, so a re-run gives the same audio.
Other voices it supports: `kokoro:<voice>` (English) and `nabra:<sid>` (Arabic, fed by `ar_g2p.py`,
a rule-based vowelled-MSA to IPA converter that was reviewed independently).

## Rules (same as the site)
- Arabic only from `content/` (checked by `check_arabic.py`), fully vowelled, read with its last vowel
  (checked by `check_endings.py`: a clip that drops the ending, i.e. reads in pause form, fails).
- Colours, fonts and markup are the site's. `build_composition.py` only adds sizes for 1920×1080 and
  the animation states.
- Narration: plain short sentences, no em-dashes, the site's terms. Stage scope as in `CLAUDE.md`.
- Renders, audio and models are not committed (`video/.gitignore`).

## A new lesson
1. Export its data (as `export_lesson.py` does; `content/stage<N>/u*.py` lessons are `notes` blocks).
2. Write `SCRIPT_SPEC.md`-style segments with cues, review them independently, assemble.
3. Add a renderer to `build_composition.py` for any block kind it does not know yet.
