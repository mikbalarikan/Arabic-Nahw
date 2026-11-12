-- İrab Ödevleri (/odev/): Türkçe ders için ödev tabloları.
-- schema.sql'den SONRA çalıştırın (private.is_teacher() oradan gelir). Tekrar çalıştırılabilir.
-- Öğretmen hesabı aynıdır: public.profiles içinde role = 'teacher' olan hesap.

-- ---------- tables ----------
create table if not exists public.tr_students (
  id          uuid primary key references auth.users on delete cascade,
  name        text not null default '',
  email       text,
  joined_at   timestamptz not null default now(),
  last_active timestamptz
);

-- One row per student per lesson. answers: [item][part] -> [kelime bilgisi, görev, irab]
create table if not exists public.tr_submissions (
  user_id      uuid not null references public.tr_students(id) on delete cascade,
  lesson       text not null,
  answers      jsonb not null,
  tries        int  not null default 1,
  submitted_at timestamptz not null default now(),
  updated_at   timestamptz not null default now(),
  primary key (user_id, lesson)
);

-- Answer keys. Students can read a key only after the teacher releases it.
create table if not exists public.tr_keys (
  lesson     text primary key,
  key        jsonb not null,
  released   boolean not null default false,
  updated_at timestamptz not null default now()
);

-- ---------- sign-up ----------
-- Accounts created on /odev/ carry course = 'tr' in their metadata: they get a tr_students row
-- and no public.profiles row, so they never appear on the English tracking sheet.
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
declare nm text := coalesce(nullif(trim(new.raw_user_meta_data->>'name'), ''), split_part(new.email, '@', 1));
begin
  if new.raw_user_meta_data->>'course' = 'tr' then
    insert into public.tr_students (id, name, email) values (new.id, nm, new.email) on conflict (id) do nothing;
  else
    insert into public.profiles (id, name, email) values (new.id, nm, new.email) on conflict (id) do nothing;
  end if;
  return new;
end $$;
revoke execute on function public.handle_new_user() from public, anon, authenticated;

-- Join the Turkish class with an existing account (e.g. made before this page existed).
create or replace function public.tr_join(p_name text)
returns void language plpgsql security definer set search_path = public as $$
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  insert into public.tr_students (id, name, email)
  select auth.uid(), left(coalesce(nullif(trim(p_name), ''), split_part(u.email, '@', 1)), 80), u.email
  from auth.users u where u.id = auth.uid()
  on conflict (id) do update set last_active = now();
end $$;
revoke execute on function public.tr_join(text) from public, anon;
grant  execute on function public.tr_join(text) to authenticated;

-- Submit (or resubmit) a lesson. Locked once the key is released.
create or replace function public.tr_submit(p_lesson text, p_answers jsonb)
returns void language plpgsql security invoker set search_path = public as $$
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  if exists (select 1 from public.tr_keys where lesson = p_lesson and released) then
    raise exception 'Cevap anahtarı açıldı; bu ödev artık değiştirilemez.' using errcode = '42501';
  end if;
  insert into public.tr_submissions as s (user_id, lesson, answers)
  values (auth.uid(), p_lesson, p_answers)
  on conflict (user_id, lesson) do update set answers = excluded.answers, tries = s.tries + 1, updated_at = now();
  update public.tr_students set last_active = now() where id = auth.uid();
end $$;
revoke execute on function public.tr_submit(text, jsonb) from public, anon;
grant  execute on function public.tr_submit(text, jsonb) to authenticated;

create or replace function public.tr_release(p_lesson text, p_on boolean)
returns void language plpgsql security invoker set search_path = public as $$
begin
  if not private.is_teacher() then raise exception 'Only the teacher.' using errcode = '42501'; end if;
  update public.tr_keys set released = p_on, updated_at = now() where lesson = p_lesson;
end $$;
revoke execute on function public.tr_release(text, boolean) from public, anon;
grant  execute on function public.tr_release(text, boolean) to authenticated;

-- ---------- row level security ----------
alter table public.tr_students    enable row level security;
alter table public.tr_submissions enable row level security;
alter table public.tr_keys        enable row level security;

drop policy if exists "tr_students: read own or teacher" on public.tr_students;
create policy "tr_students: read own or teacher" on public.tr_students
  for select using (id = auth.uid() or private.is_teacher());
drop policy if exists "tr_students: update own" on public.tr_students;
create policy "tr_students: update own" on public.tr_students
  for update using (id = auth.uid()) with check (id = auth.uid());
drop policy if exists "tr_students: teacher deletes" on public.tr_students;
create policy "tr_students: teacher deletes" on public.tr_students
  for delete using (private.is_teacher());
revoke insert, update on public.tr_students from authenticated, anon;
grant  select, delete on public.tr_students to authenticated;
grant  update (name, last_active) on public.tr_students to authenticated;

drop policy if exists "tr_sub: read own or teacher" on public.tr_submissions;
create policy "tr_sub: read own or teacher" on public.tr_submissions
  for select using (user_id = auth.uid() or private.is_teacher());
drop policy if exists "tr_sub: insert own" on public.tr_submissions;
create policy "tr_sub: insert own" on public.tr_submissions
  for insert with check (user_id = auth.uid());
drop policy if exists "tr_sub: update own" on public.tr_submissions;
create policy "tr_sub: update own" on public.tr_submissions
  for update using (user_id = auth.uid()) with check (user_id = auth.uid());
drop policy if exists "tr_sub: teacher deletes" on public.tr_submissions;
create policy "tr_sub: teacher deletes" on public.tr_submissions
  for delete using (private.is_teacher());
revoke all on public.tr_submissions from anon;
grant  select, insert, update, delete on public.tr_submissions to authenticated;

drop policy if exists "tr_keys: teacher or released" on public.tr_keys;
create policy "tr_keys: teacher or released" on public.tr_keys
  for select to authenticated using (released or private.is_teacher());
drop policy if exists "tr_keys: teacher updates" on public.tr_keys;
create policy "tr_keys: teacher updates" on public.tr_keys
  for update to authenticated using (private.is_teacher()) with check (private.is_teacher());
revoke all on public.tr_keys from anon;
revoke insert, delete, truncate on public.tr_keys from authenticated;
grant  select on public.tr_keys to authenticated;
grant  update (released, updated_at) on public.tr_keys to authenticated;

-- Keys are loaded with supabase/tr_keys.sql (generated by: python3 tools/tr_keys_sql.py).
