-- Iʿrāb Classroom: Supabase schema.
-- Run once in the Supabase dashboard: SQL Editor -> New query -> paste -> Run.
-- Safe to re-run: every object is created with "if not exists" or "create or replace".

-- ---------- tables ----------
create table if not exists public.profiles (
  id          uuid primary key references auth.users on delete cascade,
  name        text not null default '',
  email       text,
  role        text not null default 'student' check (role in ('student', 'teacher')),
  joined_at   timestamptz not null default now(),
  last_active timestamptz
);

create table if not exists public.results (
  user_id    uuid not null references public.profiles(id) on delete cascade,
  lesson     text not null,          -- lesson id, e.g. 's0-marks', 'quiz'
  set_id     text not null,          -- 'practice', 'homework', 'cards'
  card       int  not null,          -- 0-based card index in the set
  ok         int  not null,          -- items correct on the latest check
  total      int  not null,          -- items on the card
  first_ok   int  not null,          -- items correct on the first check
  best       int  not null,          -- best check before the answer was opened
  tries      int  not null default 1,
  seen       boolean not null default false,  -- answer opened at some point
  updated_at timestamptz not null default now(),
  primary key (user_id, lesson, set_id, card)
);

-- ---------- helpers ----------
-- private schema: not exposed through the API, so nobody can call these helpers directly.
create schema if not exists private;
grant usage on schema private to authenticated;
create or replace function private.is_teacher()
returns boolean language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role = 'teacher');
$$;
revoke execute on function private.is_teacher() from public, anon;
grant  execute on function private.is_teacher() to authenticated;
drop function if exists public.is_teacher() cascade;

-- New sign-up -> profile row (name comes from the sign-up form).
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, name, email)
  values (new.id, coalesce(nullif(trim(new.raw_user_meta_data->>'name'), ''), split_part(new.email, '@', 1)), new.email)
  on conflict (id) do nothing;
  return new;
end $$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

-- One call per "Check" press: keeps first try, best try (before the answer was opened) and the try count.
create or replace function public.record_result(p_lesson text, p_set text, p_card int, p_ok int, p_total int, p_seen boolean)
returns void language plpgsql security invoker set search_path = public as $$
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  insert into public.results as r (user_id, lesson, set_id, card, ok, total, first_ok, best, tries, seen, updated_at)
  values (auth.uid(), p_lesson, p_set, p_card, p_ok, p_total, p_ok, case when p_seen then 0 else p_ok end, 1, p_seen, now())
  on conflict (user_id, lesson, set_id, card) do update set
    ok         = excluded.ok,
    total      = excluded.total,
    best       = case when p_seen or r.seen then r.best else greatest(r.best, excluded.ok) end,
    tries      = r.tries + 1,
    seen       = r.seen or p_seen,
    updated_at = now();
  update public.profiles set last_active = now() where id = auth.uid();
end $$;

-- ---------- row level security ----------
alter table public.profiles enable row level security;
alter table public.results  enable row level security;

drop policy if exists "profiles: read own or teacher" on public.profiles;
create policy "profiles: read own or teacher" on public.profiles
  for select using (id = auth.uid() or private.is_teacher());
drop policy if exists "profiles: update own" on public.profiles;
create policy "profiles: update own" on public.profiles
  for update using (id = auth.uid()) with check (id = auth.uid());
drop policy if exists "profiles: teacher deletes" on public.profiles;
create policy "profiles: teacher deletes" on public.profiles
  for delete using (private.is_teacher());

drop policy if exists "results: read own or teacher" on public.results;
create policy "results: read own or teacher" on public.results
  for select using (user_id = auth.uid() or private.is_teacher());
drop policy if exists "results: insert own" on public.results;
create policy "results: insert own" on public.results
  for insert with check (user_id = auth.uid());
drop policy if exists "results: update own" on public.results;
create policy "results: update own" on public.results
  for update using (user_id = auth.uid()) with check (user_id = auth.uid());
drop policy if exists "results: teacher deletes" on public.results;
create policy "results: teacher deletes" on public.results
  for delete using (private.is_teacher());

-- Students may change only their name (never their role).
revoke update on public.profiles from authenticated, anon;
grant  update (name, last_active) on public.profiles to authenticated;
revoke insert on public.profiles from authenticated, anon;
-- Functions are not callable by signed-out visitors; the trigger function is not callable at all.
revoke execute on function public.handle_new_user() from public, anon, authenticated;
revoke execute on function public.record_result(text, text, int, int, int, boolean) from public, anon;
grant  execute on function public.record_result(text, text, int, int, int, boolean) to authenticated;

-- ---------- where the class is now ----------
-- One row: the id of the lesson the class is on. Everyone can read it; only the teacher changes it
-- (the site calls set_class_now(), which runs with the caller's rights).
create table if not exists public.class_state (
  id         smallint primary key default 1 check (id = 1),
  lesson     text not null,
  updated_at timestamptz not null default now(),
  updated_by uuid references auth.users(id)
);
insert into public.class_state (id, lesson) values (1, 'nasb') on conflict do nothing;
alter table public.class_state enable row level security;
drop policy if exists "class_state: anyone reads" on public.class_state;
create policy "class_state: anyone reads" on public.class_state
  for select to anon, authenticated using (true);
revoke insert, update, delete, truncate, references, trigger on public.class_state from public, anon, authenticated;
grant  select on public.class_state to anon, authenticated;
-- Only the teacher can update the row (checked by the policy); nobody can insert or delete.
grant  update (lesson, updated_at, updated_by) on public.class_state to authenticated;
drop policy if exists "class_state: teacher updates" on public.class_state;
create policy "class_state: teacher updates" on public.class_state
  for update to authenticated using (private.is_teacher()) with check (private.is_teacher());

create or replace function public.set_class_now(p_lesson text)
returns void language plpgsql security invoker set search_path = public as $$
begin
  if not private.is_teacher() then
    raise exception 'Only the teacher can change where the class is.' using errcode = '42501';
  end if;
  update public.class_state set lesson = p_lesson, updated_at = now(), updated_by = auth.uid() where id = 1;
end $$;
revoke execute on function public.set_class_now(text) from public, anon;
grant  execute on function public.set_class_now(text) to authenticated;

-- ---------- make yourself the teacher ----------
-- After you create your own account on the site, run (with your email):
--   update public.profiles set role = 'teacher' where email = 'you@example.com';
