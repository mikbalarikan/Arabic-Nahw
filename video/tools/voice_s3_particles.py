#!/usr/bin/env python3
"""Voice fixes for a few Arabic clips of the lesson video "Particles" (s3-particles).

tts_generate.py --verify only checks the LAST sound of a clip. For these clips the Supertonic M4 voice also
gets an inside sound wrong, which the phoneme check shows:
  - أَمَا ("did not" + question) was read like أَمَّا (amma). A different seed / speed fixes it.
  - أَوِ اللَّبَنَ was read "a-u llabana" with every seed. Here the voice is given a spelling of the same sounds
    (أَوِلَّبَنَ, as it is spoken) that it reads correctly; voice input only, the screen text and the script stay
    exactly as in the lesson. أَوْ on its own never came out right (24 attempts x 8 spellings), so the script
    does not read it alone.
Each clip is retried until its phonemes show the right inside sounds AND the right ending; the winning input and
attempt are stored in audio/choices_voicefix_s3_particles.json, so a re-run gives the same audio.

Run after tts_generate.py (it overwrites only the clips listed here):
  ~/Projects/nasb-tts/.venv/bin/python video/tools/voice_s3_particles.py [segment_id ...]
"""
import json, re, sys
from pathlib import Path

import soundfile as sf

sys.path.insert(0, str(Path(__file__).parent))
import tts_generate as T  # noqa: E402
from tts_text import speak_ar  # noqa: E402
from check_endings import expected, judge  # noqa: E402
from phonemes import Phonemizer  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
LESSON = ROOT / "video" / "lessons" / "s3-particles"

AMA = lambda p: re.match(r"^(ʔ )?a m (aː|a) ", p) is not None                      # a-m-ā, not a-mm-a
AWI = lambda p: re.search(r"[aɑæɐʌ]ː? w (i|iː|ɪ|e)", p) is not None and "b a b" not in p  # awi, no stutter

# segment -> (inside-sound rule, voice inputs to try, in order: the lesson text first)
FIXES = {
    "c04-table-14": (AMA, None),
    "c04-tip-02": (AMA, None),
    "c04-tip-09": (AMA, None),
    "c03-table-12": (AWI, ["اِشْرَبِ المَاءَ أَوِ اللَّبَنَ", "اِشْرَبِ المَاءَ أَوِلَّبَنَ", "اِشْرَبِ المَاءَ اَوِلَّبَنَ"]),
    "c03-examples-07": (AWI, ["اِشْرَبِ المَاءَ أَوِ اللَّبَنَ", "اِشْرَبِ المَاءَ أَوِلَّبَنَ", "اِشْرَبِ المَاءَ اَوِلَّبَنَ"]),
    "c03-examples-14": (AWI, ["أَوِ اللَّبَنَ", "أَوِلَّبَنَ", "اَوِلَّبَنَ"]),
}


def main(only):
    segs = {s["id"]: s for s in json.loads((LESSON / "script.json").read_text(encoding="utf-8"))["segments"]}
    models = Path.home() / "Projects/nasb-tts/models"
    tts = T.Supertonic(models, "M4", 16)
    ph = Phonemizer(str(models / "phoneme"))
    raw = LESSON / "audio" / "raw"
    store = LESSON / "audio" / "choices_voicefix_s3_particles.json"
    done = json.loads(store.read_text(encoding="utf-8")) if store.exists() else {}
    attempts = list(T.ATTEMPTS) + [(sfx, 0.7, 40 + k) for k in range(10) for sfx in (" -", "!")]
    for sid in only or FIXES:
        rule, inputs = FIXES[sid]
        last = speak_ar(segs[sid]["text"]).split()[-1]
        tries = [(i, a) for i in (inputs or [speak_ar(segs[sid]["text"])]) for a in attempts]
        if sid in done:
            tries = [(done[sid]["input"], tuple(done[sid]["attempt"]))] + tries
        tmp = raw / f"_{sid}.wav"
        for text, att in tries:
            sf.write(tmp, tts.ar(text, att), tts.sr)
            p = ph(tmp)
            if judge(expected(last), p, last)[0] and rule(p):
                tmp.replace(raw / f"{sid}.wav")
                done[sid] = dict(input=text, attempt=list(att), phonemes=p)
                print(f"ok   {sid:<16} {text} {att} [{p}]", flush=True)
                break
        else:
            tmp.unlink(missing_ok=True)
            print(f"NONE {sid}", flush=True)
    store.write_text(json.dumps(done, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
