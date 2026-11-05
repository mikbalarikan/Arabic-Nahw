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
create or replace function public.is_teacher()
returns boolean language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role = 'teacher');
$$;

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
  for select using (id = auth.uid() or public.is_teacher());
drop policy if exists "profiles: update own" on public.profiles;
create policy "profiles: update own" on public.profiles
  for update using (id = auth.uid()) with check (id = auth.uid());
drop policy if exists "profiles: teacher deletes" on public.profiles;
create policy "profiles: teacher deletes" on public.profiles
  for delete using (public.is_teacher());

drop policy if exists "results: read own or teacher" on public.results;
create policy "results: read own or teacher" on public.results
  for select using (user_id = auth.uid() or public.is_teacher());
drop policy if exists "results: insert own" on public.results;
create policy "results: insert own" on public.results
  for insert with check (user_id = auth.uid());
drop policy if exists "results: update own" on public.results;
create policy "results: update own" on public.results
  for update using (user_id = auth.uid()) with check (user_id = auth.uid());
drop policy if exists "results: teacher deletes" on public.results;
create policy "results: teacher deletes" on public.results
  for delete using (public.is_teacher());

-- Students may change only their name (never their role).
revoke update on public.profiles from authenticated, anon;
grant  update (name, last_active) on public.profiles to authenticated;
revoke insert on public.profiles from authenticated, anon;
grant execute on function public.record_result(text, text, int, int, int, boolean) to authenticated;

-- ---------- make yourself the teacher ----------
-- After you create your own account on the site, run (with your email):
--   update public.profiles set role = 'teacher' where email = 'you@example.com';
