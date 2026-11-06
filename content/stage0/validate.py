import sys, re, runpy
COLORS = {"blue","pink","gold","navy","teal","green","red","purple","orange","brown","grey","olive"}
AR = re.compile(r"[؀-ۿ]")
HARAKA = set("ًٌٍَُِّْ")
errs = []
def err(m): errs.append(m)
def check_ar_vowelled(s, where):
    for w in re.findall(r"[ء-يً-ْٰـ]+", s):
        letters = [c for c in w if "ء" <= c <= "ي"]
        marks = [c for c in w if c in HARAKA]
        if len(letters) >= 3 and not marks:
            err(f"{where}: unvowelled Arabic word {w!r}")
def walk_text(s, where):
    if not isinstance(s, str): err(f"{where}: expected string"); return
    if "—" in s: err(f"{where}: em-dash found")
    for m in re.findall(r"\{([^}]*)\}", s):
        if not AR.search(m): err(f"{where}: braces around non-Arabic {m!r}")
    check_ar_vowelled(s, where)
for path in sys.argv[1:]:
    U = runpy.run_path(path)["UNIT"]
    for k in ("id","order","title","ar","blurb","notes","practice"):
        if k not in U: err(f"missing {k}")
    if "homework" not in U and U.get("kind") != "exercise": err("missing homework")
    if not re.fullmatch(r"s[0-9]+-[a-z0-9-]+", U.get("id","")): err("bad id")
    notes = U.get("notes", [])
    if not notes or notes[0].get("t") != "hero": err("notes must start with hero")
    for i, b in enumerate(notes):
        t = b.get("t"); w = f"notes[{i}]({t})"
        if t not in {"hero","h2","p","rule","tip","cols","words","examples","table","summary"}: err(f"{w}: unknown block"); continue
        for key in ("title","text","eyebrow"):
            if key in b: walk_text(b[key], f"{w}.{key}")
        if "color" in b and b["color"] not in COLORS: err(f"{w}: bad color {b['color']}")
        for j, it in enumerate(b.get("items", [])):
            if isinstance(it, str): walk_text(it, f"{w}.items[{j}]"); continue
            for key, v in it.items():
                if key == "color":
                    if v not in COLORS: err(f"{w}.items[{j}]: bad color {v}")
                else: walk_text(v, f"{w}.items[{j}].{key}")
        for r, row in enumerate(b.get("rows", [])):
            for c, cell in enumerate(row): walk_text(cell, f"{w}.rows[{r}][{c}]")
    kind = U.get("kind", "unit")
    if kind not in ("unit", "exercise", "quiz"): err("kind must be unit, exercise or quiz")
    for setname in ("practice","homework"):
        cards = U.get(setname, [])
        if setname == "homework" and kind == "exercise" and not cards: continue   # a class exercise may have no homework
        if len(cards) < 4: err(f"{setname}: fewer than 4 cards")
        for ci, c in enumerate(cards):
            w = f"{setname}[{ci}]"
            walk_text(c.get("title",""), w+".title")
            if "prompt" in c: walk_text(c["prompt"], w+".prompt")
            fields = c.get("fields", [])
            if not 1 <= len(fields) <= 2: err(f"{w}: needs 1-2 fields")
            fk = {}
            for f in fields:
                if not re.fullmatch(r"[a-z0-9_]+", f.get("key","")): err(f"{w}: bad field key")
                fk[f["key"]] = {o["k"] for o in f.get("options", [])}
                for o in f.get("options", []):
                    if o.get("color") and o["color"] not in COLORS: err(f"{w}: bad option color {o['color']}")
            rows = c.get("rows", [])
            if not 3 <= len(rows) <= 6: err(f"{w}: needs 3-6 rows (has {len(rows)})")
            for ri, r in enumerate(rows):
                rw = f"{w}.rows[{ri}]"
                walk_text(r.get("s",""), rw+".s"); walk_text(r.get("why",""), rw+".why")
                if not r.get("why"): err(f"{rw}: missing why")
                ans = r.get("ans", {})
                for key, opts in fk.items():
                    ro = {o["k"] for o in r.get("opts", {}).get(key, [])} or opts
                    if key not in ans: err(f"{rw}: missing ans for {key}")
                    elif ans[key] not in ro: err(f"{rw}: ans {ans[key]!r} not among options {sorted(ro)}")
                    if not ro: err(f"{rw}: field {key} has no options")
print("OK" if not errs else "\n".join(errs))
