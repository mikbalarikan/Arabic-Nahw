#!/usr/bin/env python3
"""Render the parts, add the voice, and make the delivery files.

  render   each video/build/<id>/<part>/ -> video/out/<id>/parts/<part>.mp4 (silent, then muxed
           with that part's voice.wav). Parts are rendered one at a time (8 GB RAM).
  join     all parts -> video/out/<id>/<id>-1080p.mp4 (+ 720p), subtitles (.srt from the script,
           not from speech recognition), YouTube chapter list.
  web      the copy the course site serves: site/media/<id>/<id>.mp4 (720p, small enough for
           Cloudflare Pages' 25 MiB file limit), <id>.vtt captions, <id>.jpg poster, and the lesson's
           entry in site/media/videos.json (chapters for the player).

Usage:
  python3 video/tools/make_video.py render [lesson_id] [--only part,part]
  python3 video/tools/make_video.py join   [lesson_id]
  python3 video/tools/make_video.py web    [lesson_id]
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


PAGES_LIMIT = 25 * 1024 * 1024


def web(lid):
    out = ROOT / "video" / "out" / lid
    media = ROOT / "site" / "media" / lid
    media.mkdir(parents=True, exist_ok=True)
    mp4 = media / f"{lid}.mp4"
    # slides with gentle motion: a still-image tuned 720p encode keeps text sharp at about 120 kbps
    run(["ffmpeg", "-v", "error", "-y", "-i", out / f"{lid}-1080p.mp4", "-vf", "scale=1280:720:flags=lanczos",
         "-c:v", "libx264", "-preset", "veryslow", "-tune", "stillimage", "-crf", "27", "-g", "300", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "64k", "-ac", "1", "-ar", "48000", "-movflags", "+faststart", mp4])
    if mp4.stat().st_size > PAGES_LIMIT * 0.95:
        sys.exit(f"{mp4} is {mp4.stat().st_size / 2**20:.1f} MiB, too close to the 25 MiB Pages limit")
    srt = (out / f"{lid}.srt").read_text(encoding="utf-8")
    vtt = "WEBVTT\n\n" + re.sub(r"(\d\d:\d\d:\d\d),(\d\d\d)", r"\1.\2", srt)
    (media / f"{lid}.vtt").write_text(vtt, encoding="utf-8")
    run(["ffmpeg", "-v", "error", "-y", "-i", out / f"{lid}-thumbnail.jpg", "-q:v", "4", media / f"{lid}.jpg"])
    chapters = []
    for line in (out / f"{lid}-chapters.txt").read_text(encoding="utf-8").splitlines():
        t, title = line.split(" ", 1)
        m, sec = t.split(":")
        chapters.append(dict(t=int(m) * 60 + int(sec), title=title))
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp4)],
                               capture_output=True, text=True, check=True).stdout)
    reg_path = ROOT / "site" / "media" / "videos.json"
    reg = json.loads(reg_path.read_text(encoding="utf-8")) if reg_path.exists() else {}
    reg[lid] = dict(src=f"media/{lid}/{lid}.mp4", poster=f"media/{lid}/{lid}.jpg", captions=f"media/{lid}/{lid}.vtt",
                    duration=round(dur), chapters=chapters)
    reg_path.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"web: {mp4.relative_to(ROOT)} {mp4.stat().st_size / 2**20:.1f} MiB, {len(chapters)} chapters, {dur / 60:.1f} min")


if __name__ == "__main__":
    a = sys.argv[1:]
    cmd = a.pop(0)
    only = None
    if "--only" in a:
        k = a.index("--only"); only = set(a[k + 1].split(",")); del a[k:k + 2]
    lid = a[0] if a else "nasb"
    {"render": lambda: render(lid, only), "join": lambda: join(lid), "web": lambda: web(lid)}[cmd]()
