#!/usr/bin/env python3
"""Audio steps between TTS and render.

  measure  video/lessons/<id>/audio/raw/<seg>.wav -> trimmed 48 kHz mono clips in audio/clips/
           and video/lessons/<id>/timings.json  ({seg: {"dur": seconds}})
  mix      plan.json + audio/clips/ -> video/build/<id>/<part>/voice.wav (each segment placed
           at its planned time). The whole lesson is mastered in one pass (gentle compression,
           two-pass EBU R128 loudnorm, true peak -1.5 dBTP) and cut back into parts.

Usage:
  python3 video/tools/audio_tools.py measure [lesson_id]
  python3 video/tools/audio_tools.py mix [lesson_id] [--lufs -14]
Needs numpy and soundfile (uv run --with numpy --with soundfile ...), and ffmpeg on PATH.
"""
import json, subprocess, sys, tempfile
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parents[2]
SR = 48000
FADE = 0.012          # short fades at clip edges, no clicks
SIL_DB = -45.0        # trim threshold relative to the clip's peak
KEEP = 0.04           # keep this much air around the trimmed speech


def resample(path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         check=True, capture_output=True).stdout
    return np.frombuffer(out, dtype=np.float32).copy()


def trim(a):
    if not len(a):
        return a
    peak = np.max(np.abs(a)) or 1.0
    win = int(0.01 * SR)
    env = np.sqrt(np.convolve(a ** 2, np.ones(win) / win, mode="same"))
    on = np.where(env > peak * 10 ** (SIL_DB / 20))[0]
    if not len(on):
        return a
    s = max(0, on[0] - int(KEEP * SR)); e = min(len(a), on[-1] + int(KEEP * SR))
    a = a[s:e].copy()
    f = int(FADE * SR)
    a[:f] *= np.linspace(0, 1, f); a[-f:] *= np.linspace(1, 0, f)
    return a


def measure(lid):
    d = ROOT / "video" / "lessons" / lid
    raw, clips = d / "audio" / "raw", d / "audio" / "clips"
    clips.mkdir(parents=True, exist_ok=True)
    script = json.loads((d / "script.json").read_text(encoding="utf-8"))
    timings, missing = {}, []
    for s in script["segments"]:
        p = raw / f"{s['id']}.wav"
        if not p.exists():
            missing.append(s["id"]); continue
        a = trim(resample(p))
        sf.write(clips / f"{s['id']}.wav", a, SR, subtype="PCM_24")
        timings[s["id"]] = dict(dur=round(len(a) / SR, 3))
    (d / "timings.json").write_text(json.dumps(timings, indent=1), encoding="utf-8")
    print(f"timings.json: {len(timings)} clips, {sum(t['dur'] for t in timings.values()) / 60:.1f} min of speech"
          + (f"; MISSING {len(missing)}: {missing[:8]}" if missing else ""))
    return 1 if missing else 0


def master(raw, out, target):
    """Gentle speech compression, then two-pass EBU R128 loudnorm to `target` LUFS, true peak -1.5 dBTP."""
    chain = ("highpass=f=70,acompressor=threshold=-24dB:ratio=3:attack=6:release=120:makeup=4dB,"
             "alimiter=limit=0.5:attack=3:release=60:level=false")
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(raw), "-af",
                        f"{chain},loudnorm=I={target}:TP=-1.5:LRA=9:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    js = r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}") + 1]
    m = json.loads(js)
    ln = (f"loudnorm=I={target}:TP=-1.5:LRA=9:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-af", f"{chain},{ln}", "-ar", str(SR),
                    "-c:a", "pcm_s24le", str(out)], check=True)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(out), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    I = float(r.stderr.rsplit("I:", 1)[1].split("LUFS")[0])
    tp = float(r.stderr.rsplit("Peak:", 1)[1].split("dBFS")[0])
    return I, tp


def mix(lid, lufs=-14.0):
    d = ROOT / "video" / "lessons" / lid
    out = ROOT / "video" / "build" / lid
    plan = json.loads((out / "plan.json").read_text(encoding="utf-8"))
    if plan.get("estimated"):
        sys.exit("plan.json was built with estimated lengths: run measure, then build_composition, then mix")
    bufs = []
    for part in plan["parts"]:
        buf = np.zeros(int(round(part["duration"] * SR)), dtype=np.float32)
        for s in part["segments"]:
            a, sr = sf.read(d / "audio" / "clips" / f"{s['id']}.wav", dtype="float32")
            i = int(round(s["t"] * SR))
            buf[i:i + len(a)] += a[:max(0, len(buf) - i)]
        bufs.append(buf)
    # master the whole lesson at once (one loudness for every part), then cut it back into parts
    with tempfile.TemporaryDirectory() as td:
        raw, done = Path(td) / "all.wav", Path(td) / "all_master.wav"
        sf.write(raw, np.concatenate(bufs), SR, subtype="FLOAT")
        I, tp = master(raw, done, lufs)
        full, _ = sf.read(done, dtype="float32")
    k = 0
    for part, buf in zip(plan["parts"], bufs):
        sf.write(out / part["id"] / "voice.wav", full[k:k + len(buf)], SR, subtype="PCM_24")
        k += len(buf)
    print(f"mixed {len(bufs)} parts: {I:.1f} LUFS integrated, true peak {tp:.1f} dBFS (target {lufs} LUFS)")


if __name__ == "__main__":
    a = sys.argv[1:]
    cmd = a.pop(0)
    lufs = -14.0
    if "--lufs" in a:
        k = a.index("--lufs"); lufs = float(a[k + 1]); del a[k:k + 2]
    lid = a[0] if a else "nasb"
    sys.exit(measure(lid) if cmd == "measure" else mix(lid, lufs))
