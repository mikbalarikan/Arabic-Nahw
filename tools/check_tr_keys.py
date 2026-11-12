#!/usr/bin/env python3
"""Validate a Turkish i'rab key file against the option lists and the Quran morphology."""
import json, re, sys, unicodedata
KB = ["isim","alem (özel isim)","mastar","ismi fail","ismi mefûl","ismi işaret","ismi mevsul","soru ismi","munfasıl zamir","muttasıl zamir","gizli zamir","mazi fiil","muzari fiil","emir fiil","harfi cer","atıf harfi","inne ve benzerleri","olumsuzluk edatı","cezm edatı","nasb edatı","soru harfi","diğer harf/edat"]
G = ["mübteda","haber","fiil","fail","naibi fail","mefûlün bih","mefûlün mutlak","mefûlün fîh (zarf)","hal","sıfat","muzafun ileyh","mecrur (harfi cerden sonra)","ma'tuf","bedel","innenin ismi","innenin haberi","nakıs fiil (kâne vb.)","kânenin ismi","kânenin haberi","münada","temyiz","görevi yok (harf)"]
I = ["merfu","mansub","mecrur","meczum","mebni"]
import os
MORPH = os.environ.get("QURAN_MORPH", "/home/claude/data/quran-morphology.txt")  # Quranic Arabic Corpus morphology (mustafa0x/quran-morphology)
words = {}
for line in open(MORPH, encoding="utf-8"):
    p = line.rstrip("\n").split("\t")
    if len(p) < 4: continue
    s, a, w, k = p[0].split(":")
    words.setdefault(f"{s}:{a}:{w}", []).append((p[1], p[2], p[3].split("|")))

def lst(v): return v if isinstance(v, list) else [v]

def check(path):
    d = json.load(open(path, encoding="utf-8")); errs = []; warns = []
    for it in d["items"]:
        tag = f"#{it['n']} {it.get('ref')}"
        want = []
        for s, a, w1, w2 in it["src"]:
            for w in range(w1, w2 + 1):
                loc = f"{s}:{a}:{w}"
                if loc not in words: errs.append(f"{tag}: {loc} yok")
                want.append(loc)
        got = [w["loc"] for w in it["words"]]
        if got != want: errs.append(f"{tag}: kelime listesi src ile uyuşmuyor: {got} vs {want}")
        for w in it["words"]:
            segs = words.get(w["loc"], [])
            full = "".join(x[0] for x in segs)
            joined = "".join(p["t"] for p in w["parts"] if not p.get("hidden"))
            if joined != full: errs.append(f"{tag} {w['loc']}: parçalar '{joined}' != '{full}'")
            for p in w["parts"]:
                for key, opts in (("kb", KB), ("g", G), ("i", I)):
                    if key not in p: errs.append(f"{tag} {w['loc']} '{p['t']}': {key} eksik"); continue
                    for v in lst(p[key]):
                        if v not in opts: errs.append(f"{tag} {w['loc']} '{p['t']}': {key}='{v}' listede yok")
            # morphology case / mood check on the stem segment
            for (txt, pos, feats) in segs:
                if "PREF" in feats or "SUFF" in feats: continue
                case = next((c for c in ("NOM", "ACC", "GEN") if c in feats), None)
                mood = next((f.split(":")[1] for f in feats if f.startswith("MOOD:")), None)
                exp = None
                if pos == "N" and case and not ({"PRON","DEM","REL"} & set(feats)):
                    exp = {"NOM": "merfu", "ACC": "mansub", "GEN": "mecrur"}[case]
                elif pos == "V" and "IMPF" in feats and mood:
                    exp = {"IND": "merfu", "SUBJ": "mansub", "JUS": "meczum"}[mood]
                elif pos == "V" and ("PERF" in feats or "IMPV" in feats):
                    exp = "mebni"
                if exp is None: continue
                # find the part containing this segment text
                cand = [p for p in w["parts"] if not p.get("hidden") and txt and txt in p["t"]]
                if not cand: continue
                p = cand[0]
                # The corpus tags by surface vowel: a sound feminine plural in naṣb (kasra) shows as GEN,
                # a diptote in jarr (fatha) shows as ACC. Those disagreements are warnings, not errors.
                surface = (exp == "mecrur" and "mansub" in lst(p["i"]) and ("FP" in feats or "F" in feats or "P" in feats)) or \
                          (exp == "mansub" and "mecrur" in lst(p["i"]) and "INDEF" not in feats)
                if exp not in lst(p["i"]) and surface:
                    warns.append(f"{tag} {w['loc']} '{p['t']}': irab {p['i']}, morfoloji {exp} (yüzey harekesi; kontrol edin)")
                elif exp not in lst(p["i"]):
                    (warns if exp == "mebni" or pos == "V" and "IMPF" in feats else errs).append(
                        f"{tag} {w['loc']} '{p['t']}': irab {p['i']} ama morfoloji {exp}")
    for e in errs: print("HATA:", e)
    for w in warns: print("UYARI:", w)
    print(f"{path}: {len(d['items'])} madde, {len(errs)} hata, {len(warns)} uyarı")
    return not errs

if __name__ == "__main__":
    ok = all([check(p) for p in sys.argv[1:]])
    sys.exit(0 if ok else 1)
