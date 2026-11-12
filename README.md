# Iʿrāb Classroom

The course site for the Arabic grammar (naḥw) classes: lesson pages, interactive practice cards, homework and quizzes. Students sign in and their results are saved. The teacher sees everyone's results on a tracking sheet.

- **Site:** static files, built from `content/` and hosted on Cloudflare Pages.
- **Accounts and results:** Supabase (sign-in plus a Postgres database).
- **Content:** Python data files. A new lesson is one file; push it to GitHub and the site rebuilds itself.

```
content/            course content (the source of truth)
  stage0/u*.py      Stage 0 units: lesson page + practice + homework (one file each)
  stage0/SPEC.md    format and scope rules for writing a unit
  stage0/validate.py  checks a unit file (the build runs it on every unit)
  colour_guide.py   Stage 1 lesson (Iʿrāb Colour Guide) + its exercise
  build.py, build_ex.py, quran_nominal.py   Stage 1 sets (quiz, class exercise, Qur'an rafʿ/jarr)
  lesson.py, quran.py                       Stage 2 sets (naṣb lesson, Qur'an naṣb)
  course.py         collects every lesson for the build
site/               the app: index.html, app.js, CSS pieces, config example
supabase/schema.sql database tables and access rules (run once)
tools/build_site.py builds dist/ (what Cloudflare serves)
```

## One-time setup (about 15 minutes)

### 1. Supabase (accounts and results)
1. Create a free project at supabase.com. Pick a region near your students. Save the database password somewhere safe.
2. **SQL Editor → New query:** paste all of `supabase/schema.sql` and click **Run**.
3. **Authentication → Sign In / Providers → Email:** turn **off** "Confirm email". Students then get in right after sign-up. Supabase's built-in email sender only sends a few emails per hour, which is too few for a class.
4. **Project Settings → API:** the **Project URL** and the **anon public** key go into `site/config.js` (already filled in for the course project).

### 2. Cloudflare Pages (the site)
1. **Workers & Pages → Create → Pages → Connect to Git** → pick this repository.
2. Build settings:
   - Framework preset: **None**
   - Build command: `python3 tools/build_site.py`
   - Build output directory: `dist`
3. **Environment variables** (Production and Preview):
   - `PYTHON_VERSION` = `3.11`
   - The Supabase address and anon key are already in `site/config.js`. Set `IRAAB_SUPABASE_URL` and `IRAAB_SUPABASE_ANON_KEY` only if you move to another Supabase project.
4. Deploy. The site is served at `https://<project>.pages.dev`. To use your own domain, go to **Custom domains → Set up a domain**.
5. Back in Supabase, open **Authentication → URL Configuration**. Set **Site URL** to the site address and add it under **Redirect URLs**. Password-reset links need this.

### 3. Make yourself the teacher
1. Open the site and click **Create account** with your own email.
2. In the Supabase SQL Editor, run:
   ```sql
   update public.profiles set role = 'teacher' where email = 'your@email.com';
   ```
3. Reload the site. You now see the answer keys, the Teacher run sheets and the **Tracking sheet**. Your own checks are never saved, so projecting in class is safe.

### 4. Students
Share the site link. Each student clicks **Create account** (name, email, password) once. Without an account they can still practise, but nothing is saved.

## How results are saved
- Each **Check** on a card stores: the latest score, the score on the first try, the best score from before the answer was opened, the number of tries, and whether the answer was opened.
- Students can't see the Answer key tab. **Show answer** unlocks only after they press Check.
- **Who can see what** (enforced by the database, not just the page):
  - A student can read and write only their own results and can change only their own name, never their role.
  - The teacher reads everyone's.
  - Signed-out visitors can't read or write anything.
- The tracking sheet shows one row per student and one column per practice, homework or quiz set. It has a **Download CSV** button and a **Remove student** button. Removing a student deletes their profile and results; the login itself stays until you delete it in Supabase under **Authentication → Users**.

## Adding or changing content
1. Edit or add a file in `content/`. A new Stage 0 style unit is a new `content/stage0/u<N>_<slug>.py`; see `content/stage0/SPEC.md` for the format.
2. Check it locally:
   ```bash
   python3 content/stage0/validate.py content/stage0/u9_example.py   # must print OK
   python3 tools/build_site.py                                         # builds dist/
   python3 -m http.server 8000 -d dist                                 # open http://localhost:8000
   ```
   Without Supabase settings the local site runs as an open classroom screen (no sign-in), which is fine for checking content.
3. Commit and push. Cloudflare rebuilds and the change is live in about a minute.

Each card's results are stored by lesson id, set id and card position. Adding new cards at the end of a set is safe. Don't rename a lesson `id` or reorder existing cards after students have answered them, or their old results will point at the wrong cards.

## Costs and limits
- **Cloudflare Pages:** free plan, unlimited bandwidth for static files, 500 builds per month.
- **Supabase:** free plan, 500 MB database and 50,000 monthly users, which is far more than a class needs.
  - A free project is **paused after a week with no activity**; restore it from the dashboard if that happens.
  - Two lessons a week keeps it active. Holidays are the risk.
  - Pro ($25/month) removes the pause.

## Türkçe irab ödevleri (`/odev/`)
Türkçe ders için ayrı bir sayfa: `https://<site>/odev/`. Kaynak: "Bakara Sûresi Eşliğinde Kur'ân Dilbilgisi", İrab Bölümü 9–26 (s. 211 ve sonrası), her Çalışma'daki "ilk N ayetin irabını yapınız" maddeleri.
- Öğrenci Ad Soyad + e-posta + şifre ile kayıt olur (`tr_students`; İngilizce takip tablosunda görünmez).
- Her ayet parçası kelime/ek bazında tablo: Kelime bilgisi, Cümledeki görevi, İrab açılır listeleri. Gönder → `tr_submissions`. Anahtar açılana kadar yeniden gönderilebilir.
- Cevap anahtarı statik dosyalarda yok; yalnızca Supabase `tr_keys` tablosunda. Öğretmen ders sayfasında "Anahtarı öğrencilere aç" der; o anda gönderimler kilitlenir, öğrenciler puanlarını ve doğru cevapları görür. Öğretmen her zaman yüzdeleri ve Takip tablosunu (CSV) görür.
- Kurulum (bir kez, SQL Editor): `supabase/tr_schema.sql`, sonra `supabase/tr_keys.sql`.
- İçerik: `content/tr/irab<k>.json` (format `content/tr/SPEC.md`). Değiştirince `python3 tools/build_tr.py --sql > supabase/tr_keys.sql` ve o dosyayı yeniden çalıştırın. Kontrol: `QURAN_MORPH=<quran-morphology.txt> python3 tools/check_tr_keys.py content/tr/*.json`.
