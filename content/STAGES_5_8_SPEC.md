# Stages 5–8: shared writing rules

Stages 5–8 use the SAME unit-file format as Stages 0, 3 and 4. Read, in this order:
1. /home/claude/arabic-nahw/CLAUDE.md (ground rules)
2. /home/claude/arabic-nahw/content/stage0/SPEC.md (file format: UNIT dict, note blocks, cards, fields, rows, opts, colours, {Arabic} markup)
3. /home/claude/arabic-nahw/content/stage4/SPEC.md (noun groups, branch signs, "original but hidden")
4. One finished unit as a model, e.g. /home/claude/arabic-nahw/content/stage4/u2_dual.py
5. The SPEC.md of your own stage folder (unit list, scope, extra colours)
The rules below replace the scope rules of the older SPECs where they differ.
Writing ال with or without sukūn on the ل is both fine.

## What students know by now
Stage 0 foundations; Stage 1 nominal sentence (Topic + Information in rafʿ), jarr after a preposition and of the owner,
adjective / وَ copy; Stage 2 verb sentence with past and order verbs (doer rafʿ; object, purpose, time/place, state in
naṣb by fatha); Stage 3 all main fixed words and the idea of a fixed word's "place" (فِي مَحَلِّ رَفْعٍ / نَصْبٍ / جَرٍّ);
Stage 4 the noun groups and their shapes as a preview: singular, dual (ـَانِ/ـَيْنِ), sound masc. plural (ـُونَ/ـِينَ),
sound fem. plural (ـَاتٌ/ـَاتٍ), broken plural, diptote, the five nouns (أَبُو/أَبَا/أَبِي…), hidden vowel
(maqṣūr, manqūṣ, noun + ـي "my"; "original but hidden"), mamdūd.
Stages 5, 6 and 7 now DRILL which shape and which sign each group takes in rafʿ, jarr and naṣb, job by job.
Stage 8 does the same for the present verb.

## Core method of Stages 5–8 (teach it, then reuse it)
Job → case → sign. "Find the job. The job gives the case. The kind of noun gives the sign."
Every iʿrāb answer has three parts: the job (e.g. doer), the case (rafʿ), and the sign (damma / alif / wāw / hidden damma).
The classic sentence students should be able to say: "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ".
Use this formula in notes and in "why" lines (in English, with the Arabic formula where it helps).

## Scope rules
- Every Arabic word fully vowelled, including the last letter. Correct iʿrāb in every answer key matters more than anything.
- Stages 5, 6, 7: NO present-tense verbs anywhere (not in sentences, not in Qur'an examples). Past and order verbs only;
  passive past (كُتِبَ، فُتِحَ) is allowed from Stage 5 on. Stage 8 is where present verbs come in.
- Cards drill the stage's own case. Other words in a sentence may carry any correct shape (e.g. in Stage 5 the khabar
  of kāna may be مُجْتَهِدِينَ), but do not ASK about another stage's case except for review in a clearly labelled card
  (Stage 7 and 8 may review everything earlier).
- Use common, correct vocabulary (Madinah Book 1 words where possible) and the standard plurals listed in stage4/SPEC.md.
  If you are not sure of a form or an iʿrāb, don't use the item. Avoid disputed analyses and advanced cases
  (mulḥaq forms like عِشْرُونَ / أُولُو / بَنُونَ unless your stage SPEC allows them; the five nouns' rare dialect forms;
  ambiguous khabar/ḥāl, badal/naʿt or tamyīz/ḥāl readings). Every row must have exactly ONE defensible answer per field.
- Qur'an examples are welcome in notes (cite sūra:āya, e.g. "(al-Fātiḥa 1:2)"), only if you are certain of the
  text and vowelling and they contain nothing out of scope. Do not put Qur'an text in cards unless certain.
- Writing style for students: plain, short sentences, no em-dashes, no "not X but Y", no filler. English everywhere
  except Arabic examples.

## Card styles to use (mix them in every unit)
A. iʿrāb of a sentence: "prompt" = the sentence, "en" = translation, rows = the words to analyse (s = one word as
   written in the sentence), two fields: "job" and "sign" (or "case" and "sign"). Not every word needs a row; fixed
   words may get a row with sign "Fixed".
B. "Which form is right?" rows with per-row "opts" (e.g. جَاءَ ___ (المُسْلِمُونَ / المُسْلِمِينَ / المُسْلِمَاتِ)). Here
   choosing the shape for a case IS the point (unlike Stage 4).
C. Word lists: "Which sign does this word take here?" with a short phrase in "s" and the target word in [brackets].
D. Find-the-job cards: rows are words of a sentence, one field "job".
3–6 rows per card. Wrong options = real beginner mistakes, never tricks. Homework items differ from practice items.

## Canonical option lists (copy these EXACTLY, same keys, labels and colours, so every unit and quiz matches)
Take only the options a card needs, but never rename a key or change a label.

SIGN options (field key "sign"):
  {"k": "dam",   "label": "Damma · ضَمَّةٌ",                 "color": "red"}
  {"k": "fat",   "label": "Fatha · فَتْحَةٌ",                "color": "pink"}
  {"k": "kas",   "label": "Kasra · كَسْرَةٌ",                "color": "green"}
  {"k": "suk",   "label": "Sukūn · سُكُونٌ",                 "color": "navy"}
  {"k": "alif",  "label": "Alif · الأَلِفُ",                  "color": "teal"}
  {"k": "waw",   "label": "Wāw · الوَاوُ",                   "color": "blue"}
  {"k": "ya",    "label": "Yāʾ · اليَاءُ",                   "color": "purple"}
  {"k": "hid",   "label": "Hidden vowel · مُقَدَّرَةٌ",         "color": "brown"}
  {"k": "nun",   "label": "Nūn stays · ثُبُوتُ النُّونِ",        "color": "olive"}     (Stage 8)
  {"k": "drop",  "label": "Nūn drops · حَذْفُ النُّونِ",         "color": "orange"}    (Stage 8)
  {"k": "weak",  "label": "Weak letter drops · حَذْفُ حَرْفِ العِلَّةِ", "color": "gold"}  (Stage 8)
  {"k": "fixed", "label": "Fixed · مَبْنِيٌّ",                  "color": "grey"}
  Rule for the "hid" option: use it for the hidden damma/fatha/kasra of maqṣūr, manqūṣ (rafʿ and jarr only;
  in naṣb the fatha shows on the ي: رَأَيْتُ القَاضِيَ → "fat"), and noun + ـي "my". The "why" line names which
  vowel is hidden ("hidden damma"). For the dual and sound masc. plural the sign is the letter (alif/wāw/yāʾ),
  never "hid". Five nouns: wāw / alif / yāʾ. Sound fem. plural in naṣb: kasra. Diptote in jarr: fatha.

CASE options (field key "case"):
  {"k": "raf",  "label": "Rafʿ · رَفْعٌ",   "color": "red"}
  {"k": "nasb", "label": "Naṣb · نَصْبٌ",  "color": "pink"}
  {"k": "jarr", "label": "Jarr · جَرٌّ",   "color": "green"}
  {"k": "jazm", "label": "Jazm · جَزْمٌ",  "color": "navy"}   (Stage 8)

KIND options (field key "kind"), when a card asks which group a noun is in:
  {"k": "sing", "label": "Singular · مُفْرَدٌ",                     "color": "grey"}
  {"k": "dual", "label": "Dual · مُثَنًّى",                         "color": "teal"}
  {"k": "smp",  "label": "Sound m. plural · جَمْعُ مُذَكَّرٍ سَالِمٌ",  "color": "blue"}
  {"k": "sfp",  "label": "Sound f. plural · جَمْعُ مُؤَنَّثٍ سَالِمٌ",  "color": "pink"}
  {"k": "brk",  "label": "Broken plural · جَمْعُ تَكْسِيرٍ",          "color": "purple"}
  {"k": "dip",  "label": "Diptote · مَمْنُوعٌ مِنَ الصَّرْفِ",         "color": "orange"}
  {"k": "five", "label": "Five nouns · الأَسْمَاءُ الخَمْسَةُ",        "color": "gold"}
  {"k": "hidv", "label": "Hidden vowel",                          "color": "brown"}

JOB options (field key "job"). Course colours are fixed; jobs that are new in these stages are added here:
  {"k": "topic", "label": "Topic · مُبْتَدَأٌ",                  "color": "gold"}
  {"k": "info",  "label": "Information · خَبَرٌ",                "color": "red"}
  {"k": "verb",  "label": "Verb · فِعْلٌ",                       "color": "navy"}
  {"k": "doer",  "label": "Doer · فَاعِلٌ",                      "color": "orange"}
  {"k": "naib",  "label": "Doer stand-in · نَائِبُ الفَاعِلِ",       "color": "orange"}
  {"k": "kism",  "label": "Kāna's noun · اِسْمُ كَانَ",             "color": "gold"}
  {"k": "kkhab", "label": "Kāna's information · خَبَرُ كَانَ",       "color": "red"}
  {"k": "iism",  "label": "Inna's noun · اِسْمُ إِنَّ",              "color": "gold"}
  {"k": "ikhab", "label": "Inna's information · خَبَرُ إِنَّ",        "color": "red"}
  {"k": "prep",  "label": "After a preposition · اِسْمٌ مَجْرُورٌ",    "color": "green"}
  {"k": "owner", "label": "Owner · مُضَافٌ إِلَيْهِ",               "color": "purple"}
  {"k": "adj",   "label": "Adjective · نَعْتٌ",                   "color": "grey"}
  {"k": "and",   "label": "After وَ (and) · مَعْطُوفٌ",              "color": "blue"}
  {"k": "tawk",  "label": "Emphasis · تَوْكِيدٌ",                  "color": "grey"}
  {"k": "badal", "label": "Substitute · بَدَلٌ",                   "color": "grey"}
  {"k": "obj",   "label": "Object · مَفْعُولٌ بِهِ",                "color": "pink"}
  {"k": "mutl",  "label": "Verb's own noun · مَفْعُولٌ مُطْلَقٌ",      "color": "purple"}
  {"k": "purp",  "label": "Purpose · مَفْعُولٌ لِأَجْلِهِ",            "color": "teal"}
  {"k": "when",  "label": "Time/place · مَفْعُولٌ فِيهِ",            "color": "brown"}
  {"k": "maah",  "label": "Together with · مَفْعُولٌ مَعَهُ",         "color": "blue"}
  {"k": "state", "label": "State · حَالٌ",                       "color": "olive"}
  {"k": "tamy",  "label": "Specifier · تَمْيِيزٌ",                 "color": "gold"}
  {"k": "exc",   "label": "Exception · مُسْتَثْنًى",               "color": "red"}
  {"k": "voc",   "label": "Called · مُنَادًى",                    "color": "green"}
  {"k": "part",  "label": "Particle · حَرْفٌ",                     "color": "grey"}
  In one card's field, choose options whose colours are different from each other where possible
  (e.g. do not put "tamy" and "topic" on the same card unless needed; if you must, that is fine, the labels differ).
  When an item could be read two ways (e.g. ʿaṭf after وَ vs. maʿah), don't use it, or make the sentence unambiguous.

## Notes, ids, counts
- Files: content/stage<N>/u<k>_<slug>.py, "id": "s<N>-<slug>", "order": k. Never reuse an id from another stage.
- Units: notes 5–8 sections (hero first with eyebrow "STAGE N · UNIT k", a summary block at the end, at least one
  table of shapes/signs, worked examples showing the full iʿrāb formula), 6 practice cards, 6 homework cards
  (different items, a little harder), 3–6 rows per card.
- Class exercise (kind "exercise"): review of the whole stage, 10 practice cards, "homework": [], second-highest order.
- Stage quiz (kind "quiz"): 8 practice cards + 6 homework cards, highest order, title "Stage N quiz".
- Validate each file: python3 /home/claude/arabic-nahw/content/stage0/validate.py <file>   (must print OK).
- Do not edit files outside your assigned list. Do not run git.

## Final self-check before you report
Re-read every Arabic string: every letter that needs a vowel has one, the last letter has its case vowel,
tanween only where the word takes it (no tanween with ال, in iḍāfa, on diptotes), nūn of dual/SMP dropped in iḍāfa
(كِتَابَا الطَّالِبِ، مُعَلِّمُو المَدْرَسَةِ). For every row: is exactly one option correct in each field?
