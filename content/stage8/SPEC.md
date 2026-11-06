# Stage 8 · The present verb (إِعْرَابُ الفِعْلِ المُضَارِعِ)

Read /home/claude/arabic-nahw/content/STAGES_5_8_SPEC.md first (shared rules, canonical options). This file adds the Stage 8 plan.
Present verbs are now IN scope (only here). All noun iʿrāb from Stages 5–7 is known and may appear and be reviewed.

Goal: the present verb is the only verb that is muʿrab. It has three cases: rafʿ, naṣb, jazm (never jarr).
- It starts with one of أ ن ي ت (أَنَيْتُ). Used for "is doing / will do".
- Rafʿ when no particle of naṣb or jazm comes before it: damma (يَكْتُبُ), hidden damma on a weak ending (يَدْعُو، يَرْمِي، يَسْعَى),
  nūn stays for the five verbs (يَكْتُبَانِ، تَكْتُبَانِ، يَكْتُبُونَ، تَكْتُبُونَ، تَكْتُبِينَ).
- Naṣb after أَنْ، لَنْ، كَيْ، لِـ (لَامُ التَّعْلِيلِ)، حَتَّى، إِذَنْ: fatha (لَنْ يَكْتُبَ; shows on و/ي: لَنْ يَدْعُوَ، لَنْ يَرْمِيَ; hidden on alif: لَنْ يَسْعَى),
  nūn drops for the five verbs (لَنْ يَكْتُبُوا).
- Jazm after لَمْ، لَمَّا، لَامُ الأَمْرِ (لِيَكْتُبْ)، لَا النَّاهِيَةُ (لَا تَكْتُبْ), and إِنْ of condition (two verbs: إِنْ تَدْرُسْ تَنْجَحْ):
  sukūn (لَمْ يَكْتُبْ), weak letter drops (لَمْ يَدْعُ، لَمْ يَرْمِ، لَمْ يَسْعَ), nūn drops (لَمْ يَكْتُبُوا).
- Fixed present verb: with nūn of women (يَكْتُبْنَ: fixed on sukūn) and with the nūn of emphasis (لَيَكْتُبَنَّ: fixed on fatha).
  This is why the present verb is muʿrab "only when nothing is attached".
- Sign keys to use: dam, fat, suk, hid, nun, drop, weak, fixed. Case keys: raf, nasb, jazm.
- Particle colours: naṣb particles = pink, jazm particles = navy. Verb rows are coloured by case via the options.

| file | id | order | title | content |
|---|---|---|---|---|
| u1_present.py | s8-present | 1 | Meet the present verb | form (أَنَيْتُ), meaning, the full table of يَكْتُبُ for all persons (أَكْتُبُ، نَكْتُبُ، تَكْتُبُ، تَكْتُبِينَ، يَكْتُبُ، تَكْتُبُ، تَكْتُبَانِ، يَكْتُبَانِ، تَكْتُبُونَ، يَكْتُبُونَ، تَكْتُبْنَ، يَكْتُبْنَ), past vs present vs order; it is muʿrab, with 3 cases; when it is fixed (nūn of women, nūn of emphasis) |
| u2_rafa.py | s8-rafa | 2 | The present verb in rafʿ | default rafʿ with no particle: damma; hidden damma on يَدْعُو، يَرْمِي، يَسْعَى; verb sentence with a present verb (يَكْتُبُ الطَّالِبُ الدَّرْسَ) with full iʿrāb of the nouns too |
| u3_five_verbs.py | s8-five-verbs | 3 | The five verbs | الأَفْعَالُ الخَمْسَةُ (يَفْعَلَانِ، تَفْعَلَانِ، يَفْعَلُونَ، تَفْعَلُونَ، تَفْعَلِينَ): rafʿ by the nūn staying, naṣb and jazm by the nūn dropping; the alif / wāw / yāʾ is the doer (in the place of rafʿ); contrast يَكْتُبْنَ (fixed) |
| u4_nasb.py | s8-nasb | 4 | The present verb in naṣb | the particles أَنْ، لَنْ، كَيْ، لِـ، حَتَّى، إِذَنْ with meanings; signs: fatha, fatha on و/ي, hidden fatha on alif, nūn drops |
| u5_jazm.py | s8-jazm | 5 | The present verb in jazm | لَمْ، لَمَّا، لَامُ الأَمْرِ، لَا النَّاهِيَةُ (contrast لَا النَّافِيَةُ: لَا يَكْتُبُ stays rafʿ); signs: sukūn, nūn drops; لَمْ يَكْتُبْ = مَا كَتَبَ |
| u6_condition.py | s8-condition | 6 | Two verbs in jazm | إِنْ of condition: the condition verb and the answer verb both in jazm (إِنْ تَدْرُسْ تَنْجَحْ، إِنْ تَجْتَهِدُوا تَنْجَحُوا); also مَنْ and مَا as condition words (مَنْ يَجْتَهِدْ يَنْجَحْ); keep the answer a plain present verb (no فَـ answers) |
| u7_weak.py | s8-weak | 7 | Verbs with a weak ending | يَدْعُو، يَرْجُو، يَرْمِي، يَمْشِي، يَسْعَى، يَنْسَى across the three cases (rafʿ hidden damma; naṣb fatha shows on و/ي, hidden on alif; jazm weak letter drops); table of 3 verbs × 3 cases; plus the fixed present verb review (nūn of women, nūn of emphasis) |
| u8_exercise.py | s8-exercise | 8 | Stage 8 class exercise | kind "exercise", 10 practice cards, homework []; may review the whole course in 2 cards |
| u9_quiz.py | s8-quiz | 9 | Stage 8 quiz | kind "quiz", 8 practice + 6 homework |

Scope notes:
- Avoid hollow and doubled verbs in jazm (لَمْ يَقُلْ، لَمْ يَمُدَّ) unless certain; they are fine as vocabulary in rafʿ.
- Avoid سَ / سَوْفَ analysis beyond "future, no effect on the case". Avoid أَنْ hidden after لِـ / حَتَّى theory: simply say
  "after لِـ and حَتَّى the verb is in naṣb".
- No فَاءُ السَّبَبِيَّةِ, no لَمْ + present with weak middle letter, no jussive of doubled verbs.
