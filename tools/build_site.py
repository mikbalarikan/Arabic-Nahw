#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the static site into dist/.

    python3 tools/build_site.py

Reads the course content in content/ (Stage 0 units in content/stage0/u*.py, Stage 1/2 sets in the
other modules), validates every Stage 0 unit, and writes:
    dist/index.html, dist/app.js, dist/app.css, dist/config.js, dist/_headers
    dist/data/manifest.json        lesson list for the home page and the tracking sheet
    dist/data/lessons/<id>.json     one file per lesson: lesson page + all cards (loaded when opened)
Supabase settings come from IRAAB_SUPABASE_URL / IRAAB_SUPABASE_ANON_KEY, or from site/config.js.
"""
import glob, hashlib, html, json, os, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT, SITE, DIST = (os.path.join(ROOT, p) for p in ("content", "site", "dist"))

def fail(msg):
    print("BUILD FAILED:", msg); sys.exit(1)

def validate_units():
    bad = []
    for f in sorted(glob.glob(os.path.join(CONTENT, "stage0", "u*.py"))):
        out = subprocess.run([sys.executable, os.path.join(CONTENT, "stage0", "validate.py"), f], capture_output=True, text=True)
        if out.stdout.strip() != "OK":
            bad.append(f"{os.path.basename(f)}:\n{out.stdout}{out.stderr}")
    if bad: fail("Stage 0 validation\n" + "\n".join(bad))

def sample_html(d):
    s = d["sets"][0]; c = s["cards"][0]
    if not c.get("toks"): return ""
    jf = next(f for f in s["fields"] if f["key"] == "job")
    tok_job = {}
    for r in c["rows"]: tok_job.setdefault(r["tok"], r["ans"]["job"])
    out = []
    for i, t in enumerate(c["toks"]):
        o = next((o for o in jf["options"] if o["k"] == tok_job.get(i)), {})
        out.append(f'<span style="border-color:{o.get("b", "#ccc")}">{html.escape(t.replace("ـ", ""))}</span>')
    return " ".join(out)

def main():
    validate_units()
    os.chdir(CONTENT); sys.path.insert(0, CONTENT)
    import course
    lessons = course.stage0() + course.stage12()
    ids = [d["id"] for d in lessons]
    if len(ids) != len(set(ids)): fail("duplicate lesson ids")

    if os.path.isdir(DIST): shutil.rmtree(DIST)
    os.makedirs(os.path.join(DIST, "data", "lessons"))
    manifest = []
    for d in lessons:
        body = {"intro": d.get("intro", ""), "teacher": d.get("teacher", ""), "sets": d["sets"]}
        raw = json.dumps(body, ensure_ascii=False, separators=(",", ":"))
        v = hashlib.sha1(raw.encode()).hexdigest()[:10]
        open(os.path.join(DIST, "data", "lessons", d["id"] + ".json"), "w", encoding="utf-8").write(raw)
        manifest.append({
            "id": d["id"], "stage": d["stage"], "order": d.get("order", 0), "title": d["title"], "ar": d["ar"],
            "blurb": d["blurb"], "introLabel": d.get("introLabel", "Intro"), "hasTeacher": bool(d.get("teacher")),
            "sample": sample_html(d), "v": v,
            "sets": [{"id": s["id"], "label": s["label"], "n": len(s["cards"]), "cards": [{"n": c["n"]} for c in s["cards"]]} for s in d["sets"]],
        })
    json.dump({"lessons": manifest}, open(os.path.join(DIST, "data", "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False)

    css = open(os.path.join(SITE, "_shell.css"), encoding="utf-8").read().replace("/*BASE_CSS*/", course.base_css())
    css += open(os.path.join(SITE, "_extra.css"), encoding="utf-8").read() + open(os.path.join(SITE, "_auth.css"), encoding="utf-8").read()
    open(os.path.join(DIST, "app.css"), "w", encoding="utf-8").write(css)
    js = open(os.path.join(SITE, "app.js"), encoding="utf-8").read()
    open(os.path.join(DIST, "app.js"), "w", encoding="utf-8").write(js)

    url, key = os.environ.get("IRAAB_SUPABASE_URL", ""), os.environ.get("IRAAB_SUPABASE_ANON_KEY", "")
    if url and key:
        cfg = "window.IRAAB_CONFIG = " + json.dumps({"supabaseUrl": url, "supabaseAnonKey": key}) + ";\n"
    elif os.path.exists(os.path.join(SITE, "config.js")):
        cfg = open(os.path.join(SITE, "config.js"), encoding="utf-8").read()
    else:
        cfg = "// No Supabase settings: the site runs as an open classroom screen without accounts.\nwindow.IRAAB_CONFIG = {};\n"
    open(os.path.join(DIST, "config.js"), "w", encoding="utf-8").write(cfg)

    ver = hashlib.sha1((css + js + cfg + json.dumps(manifest)).encode()).hexdigest()[:10]
    page = open(os.path.join(SITE, "index.html"), encoding="utf-8").read().replace("__V__", ver)
    open(os.path.join(DIST, "index.html"), "w", encoding="utf-8").write(page)
    open(os.path.join(DIST, "_headers"), "w").write(
        "/data/manifest.json\n  Cache-Control: no-cache\n/index.html\n  Cache-Control: no-cache\n/config.js\n  Cache-Control: no-cache\n"
        "/data/lessons/*\n  Cache-Control: public, max-age=31536000, immutable\n")
    n_cards = sum(len(s["cards"]) for d in lessons for s in d["sets"])
    size = sum(os.path.getsize(f) for f in glob.glob(os.path.join(DIST, "**"), recursive=True) if os.path.isfile(f))
    print(f"Built dist/: {len(lessons)} lessons, {n_cards} cards, {size // 1024} KB, config: {'Supabase' if 'supabase.co' in cfg else 'none'}")

if __name__ == "__main__":
    main()
