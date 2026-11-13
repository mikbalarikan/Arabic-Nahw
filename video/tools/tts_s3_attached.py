#!/usr/bin/env python3
"""Voice for the "Attached pronouns" video (s3-attached), safe to re-run after script edits.

tts_generate.py keeps an existing clip whatever its text. This wrapper remembers the text each clip was made
from (audio/texts.json). Before tts_generate.py runs, every clip is matched to the current script by its text
(so renumbered segments keep their audio and their saved attempt); clips nobody uses any more are deleted.
Only new or changed segments are synthesised.

Usage: ~/Projects/nasb-tts/.venv/bin/python video/tools/tts_s3_attached.py [--scenes c06-]
"""
import json, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "video" / "lessons" / "s3-attached"
RAW = D / "audio" / "raw"
MAN = D / "audio" / "texts.json"
CHO = D / "audio" / "choices_supertonic_M4.json"

segs = json.loads((D / "script.json").read_text(encoding="utf-8"))["segments"]
RAW.mkdir(parents=True, exist_ok=True)
man = json.loads(MAN.read_text(encoding="utf-8")) if MAN.exists() else {}
cho = json.loads(CHO.read_text(encoding="utf-8")) if CHO.exists() else {}
now = {s["id"]: f'{s["lang"]}|{s["text"]}' for s in segs}
# set every existing clip aside, then bring back the ones whose text is still in the script
old = RAW / "_old"
old.mkdir(exist_ok=True)
for w in RAW.glob("*.wav"):
    w.rename(old / w.name)
by_text = {}
for i, t in man.items():
    if (old / f"{i}.wav").exists():
        by_text.setdefault(t, i)
new_cho, kept = {}, 0
for i, t in now.items():
    j = by_text.get(t)
    if j is not None:
        shutil.copy(old / f"{j}.wav", RAW / f"{i}.wav")
        kept += 1
        if j in cho:
            new_cho[i] = cho[j]
shutil.rmtree(old)
CHO.write_text(json.dumps(new_cho, ensure_ascii=False, indent=1))
print(f"{kept} clips kept, {len(now) - kept} to make", flush=True)
cmd = [sys.executable, str(ROOT / "video/tools/tts_generate.py"), "--en", "supertonic:M4", "--ar", "supertonic:M4",
       "--verify", str(Path.home() / "Projects/nasb-tts/models/phoneme"), "--lesson", "s3-attached"] + sys.argv[1:]
subprocess.run(cmd, check=True)
MAN.write_text(json.dumps({i: t for i, t in now.items() if (RAW / f"{i}.wav").exists()}, ensure_ascii=False, indent=1),
               encoding="utf-8")
