#!/usr/bin/env python3
"""Render the parts, add the voice, and make the delivery files.

  render   each video/build/<id>/<part>/ -> video/out/<id>/parts/<part>.mp4 (silent, then muxed
           with that part's voice.wav). Parts are rendered one at a time (8 GB RAM).
  join     all parts -> video/out/<id>/<id>-1080p.mp4 (+ 720p), subtitles (.srt from the script,
           not from speech recognition), YouTube chapter list, thumbnail frame.

Usage:
  python3 video/tools/make_video.py render [lesson_id] [--only part,part]
  python3 video/tools/make_video.py join   [lesson_id]
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HF = ROOT / "video" / "node_modules" / ".bin" / "hyperframes"


def run(cmd, **kw):
    print("+", " ".join(str(c) for c in cmd), flush=True)
    return subprocess.run([str(c) for c in cmd], check=True, **kw)


def render(lid, only=None):
    build = ROOT / "video" / "build" / lid
    plan = json.loads((build / "plan.json").read_text(encoding="utf-8"))
    out = ROOT / "video" / "out" / lid / "parts"
    out.mkdir(parents=True, exist_ok=True)
    for part in plan["parts"]:
        pid = part["id"]
        if only and pid not in only:
            continue
        silent = out / f"{pid}-silent.mp4"
        run([HF, "render", str(build / pid), "-o", silent, "--fps", "30", "--quality", "high"])
        voice = build / pid / "voice.wav"
        if voice.exists():  # a playable copy of this part on its own (chapters can also be published one by one)
            run(["ffmpeg", "-v", "error", "-y", "-i", silent, "-i", voice, "-map", "0:v", "-map", "1:a",
                 "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-r", "30",
                 "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart",
                 out / f"{pid}.mp4"])


MAXLINE = 42


def wrap(text):
    """At most two lines of about MAXLINE characters, broken at spaces."""
    if len(text) <= MAXLINE:
        return [text]
    words, best = text.split(), None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        score = max(len(a), len(b))
        if best is None or score < best[0]:
            best = (score, [a, b])
    return best[1]


def split_cue(text, t0, t1):
    """Cues longer than two lines are split at sentence ends, timed by length."""
    if len(text) <= 2 * MAXLINE:
        return [(t0, t1, text)]
    parts, cur = [], ""
    for sent in re.split(r"(?<=[.?!])\s+", text):
        if cur and len(cur) + 1 + len(sent) > 2 * MAXLINE:
            parts.append(cur); cur = sent
        else:
            cur = (cur + " " + sent).strip()
    parts.append(cur)
    total, out, a = sum(len(p) for p in parts), [], t0
    for p in parts:
        b = a + (t1 - t0) * len(p) / total
        out.append((round(a, 3), round(b, 3), p)); a = b
    return out


def ts(t, sep=","):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}".replace(".", sep)


def join(lid):
    build = ROOT / "video" / "build" / lid
    plan = json.loads((build / "plan.json").read_text(encoding="utf-8"))
    script = {s["id"]: s for s in json.loads((ROOT / "video/lessons" / lid / "script.json").read_text(encoding="utf-8"))["segments"]}
    out = ROOT / "video" / "out" / lid
    # one continuous encode: the silent part renders joined at a constant 30 fps, and the parts'
    # mastered voice tracks joined sample-exactly, so there are no gaps at the joins
    lst = out / "parts.txt"
    lst.write_text("".join(f"file 'parts/{p['id']}-silent.mp4'\n" for p in plan["parts"]))
    vlst = out / "voices.txt"
    vlst.write_text("".join(f"file '{build / p['id'] / 'voice.wav'}'\n" for p in plan["parts"]))
    full = out / f"{lid}-1080p.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-f", "concat", "-safe", "0", "-i", vlst,
         "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
         "-fps_mode", "cfr", "-r", "30", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-shortest",
         "-movflags", "+faststart", full])
    run(["ffmpeg", "-v", "error", "-y", "-i", full, "-vf", "scale=1280:720:flags=lanczos", "-c:v", "libx264", "-preset", "slow",
         "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", out / f"{lid}-720p.mp4"])
    # subtitles and chapters from the script and the plan
    srt, chapters, off, n = [], [], 0.0, 0
    for p in plan["parts"]:
        for c in p["chapters"]:
            chapters.append((off + c["t"], c["title"]))
        for s in p["segments"]:
            n += 1
            text = script[s["id"]]["text"]
            t0, t1 = off + s["t"], off + s["t"] + s["len"] + 0.15
            for k, (a, b, chunk) in enumerate(split_cue(text, t0, t1)):
                n += 1 if k else 0
                lines = wrap(chunk)
                if s["lang"] == "ar":
                    lines = ["\u202b" + l + "\u202c" for l in lines]  # keep Arabic right-to-left in players
                srt.append(f"{n}\n{ts(a)} --> {ts(b)}\n" + "\n".join(lines) + "\n")
        off += p["duration"]
    (out / f"{lid}.srt").write_text("\n".join(srt), encoding="utf-8")
    yt = []
    for t, title in chapters:
        m, s = divmod(int(t), 60)
        clean = re.sub(r"\s+", " ", title)
        yt.append(f"{m}:{s:02d} {clean}")
    if yt:
        yt[0] = "0:00" + yt[0][yt[0].index(" "):]
    (out / f"{lid}-chapters.txt").write_text("\n".join(yt) + "\n", encoding="utf-8")
    print(f"done: {full.name}, 720p, {len(srt)} subtitles, {len(yt)} chapters, total {off / 60:.1f} min")


if __name__ == "__main__":
    a = sys.argv[1:]
    cmd = a.pop(0)
    only = None
    if "--only" in a:
        k = a.index("--only"); only = set(a[k + 1].split(",")); del a[k:k + 2]
    lid = a[0] if a else "nasb"
    render(lid, only) if cmd == "render" else join(lid)
