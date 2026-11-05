/* Iʿrāb Classroom: lesson router, card engine, Supabase accounts and teacher tracking. */
"use strict";
const DASH = "—";
const AR_RE = /[؀-ۿ]/, LAT_RE = /[A-Za-z]/;
const app = document.getElementById("app");
const CFG = window.IRAAB_CONFIG || {};
let DATA = [];                // manifest lessons
const FULL = {};              // lesson id -> full lesson (intro html, sets with cards)
const state = {};             // state[lid][sid][i] = {sel, checked, answer, seen}
const cur = {};               // card index per "lid/sid"
const names = {};             // teacher run-sheet names (this screen only)

/* ============================ cloud (Supabase) ============================ */
const CLOUD = { mode: "local", sb: null, user: null, profile: null, res: new Map(), roster: null, allRes: null,
  status: "", authView: null, detail: null, busy: false };
// mode: local (no backend configured: open classroom screen), guest (signed out), student, teacher
function isTeacher() { return CLOUD.mode === "local" || CLOUD.mode === "teacher"; }
const resKey = (l, s, i) => l + "~" + s + "~" + i;
function myRec(l, s, i) { return CLOUD.res.get(resKey(l, s, i)) || null; }

async function initCloud() {
  if (!CFG.supabaseUrl || !CFG.supabaseAnonKey || !window.supabase) { CLOUD.mode = "local"; return; }
  CLOUD.sb = window.supabase.createClient(CFG.supabaseUrl, CFG.supabaseAnonKey, { auth: { flowType: "pkce", persistSession: true, detectSessionInUrl: true } });
  CLOUD.mode = "guest";
  CLOUD.sb.auth.onAuthStateChange((ev, session) => {
    if (ev === "PASSWORD_RECOVERY") { CLOUD.authView = "newpass"; refresh(); }
    if (ev === "SIGNED_IN" || ev === "SIGNED_OUT" || ev === "TOKEN_REFRESHED" || ev === "USER_UPDATED") {
      const changed = (session && session.user && session.user.id) !== (CLOUD.user && CLOUD.user.id);
      CLOUD.user = session ? session.user : null;
      if (changed) loadAccount();
    }
  });
  const { data } = await CLOUD.sb.auth.getSession();
  CLOUD.user = data.session ? data.session.user : null;
  await loadAccount(true);
}
async function loadAccount(initial) {
  CLOUD.profile = null; CLOUD.res = new Map(); CLOUD.roster = null; CLOUD.allRes = null;
  // A different account (or signing out) must not see the previous person's answers on this screen.
  for (const k in state) delete state[k];
  for (const k in cur) delete cur[k];
  if (!CLOUD.user) { CLOUD.mode = "guest"; if (!initial) refresh(); return; }
  const { data: prof, error } = await CLOUD.sb.from("profiles").select("*").eq("id", CLOUD.user.id).maybeSingle();
  if (error) { CLOUD.status = "Could not load your account. Check your connection and reload."; }
  CLOUD.profile = prof || { name: "", role: "student" };
  CLOUD.mode = CLOUD.profile.role === "teacher" ? "teacher" : "student";
  if (CLOUD.mode === "student") {
    const rows = await fetchAll(q => q.from("results").select("lesson,set_id,card,ok,total,first_ok,best,tries,seen").eq("user_id", CLOUD.user.id));
    rows.forEach(r => CLOUD.res.set(resKey(r.lesson, r.set_id, r.card), r));
  }
  refresh();
}
async function fetchAll(build) {
  const out = []; let from = 0;
  for (;;) {
    const { data, error } = await build(CLOUD.sb).range(from, from + 999);
    if (error) { CLOUD.status = "Some saved results could not be loaded."; break; }
    out.push(...data); if (data.length < 1000) break; from += 1000;
  }
  return out;
}
async function loadRoster() {
  const [{ data: profs }, rows] = await Promise.all([
    CLOUD.sb.from("profiles").select("*").order("name"),
    fetchAll(q => q.from("results").select("user_id,lesson,set_id,card,ok,total,first_ok,best,tries,seen,updated_at")),
  ]);
  CLOUD.roster = (profs || []).filter(p => p.role !== "teacher");
  const by = {}; rows.forEach(r => { (by[r.user_id] ||= {})[resKey(r.lesson, r.set_id, r.card)] = r; });
  CLOUD.allRes = by;
}
async function saveResult(d, set, i, sc, seen) {
  if (CLOUD.mode !== "student") return;
  const el = document.getElementById("savemsg");
  if (el) { el.textContent = "Saving…"; el.className = "saved"; }
  const { error } = await CLOUD.sb.rpc("record_result", { p_lesson: d.id, p_set: set.id, p_card: i, p_ok: sc.ok, p_total: sc.total, p_seen: !!seen });
  const msg = document.getElementById("savemsg");
  if (error) { if (msg) { msg.textContent = "Not saved. Check your connection and press Check again."; msg.className = "saved err"; } return; }
  const k = resKey(d.id, set.id, i), p = CLOUD.res.get(k);
  const was = p && p.seen;
  CLOUD.res.set(k, { ok: sc.ok, total: sc.total, first_ok: p ? p.first_ok : sc.ok,
    best: seen || was ? (p ? p.best : 0) : Math.max(p ? p.best : 0, sc.ok), tries: (p ? p.tries : 0) + 1, seen: !!seen || !!was });
  if (msg) { msg.textContent = "Saved"; msg.className = "saved"; }
  refreshPills(d, set);
}

/* ---------- auth UI ---------- */
function authPanel() {
  if (CLOUD.mode === "local") return "";
  if (CLOUD.status) return `<section class="reg warn"><p>${esc(CLOUD.status)}</p></section>`;
  if (CLOUD.authView === "newpass") return `<section class="reg"><h3>Choose a new password</h3>
    <form id="f-newpass" class="authf"><input id="np" type="password" autocomplete="new-password" minlength="8" placeholder="New password (8+ characters)" required>
    <button class="btn primary" type="submit">Save password</button></form><p class="autherr" id="autherr"></p></section>`;
  if (CLOUD.mode !== "guest") return "";
  const v = CLOUD.authView || "intro";
  if (v === "intro") return `<section class="reg"><h3>Join the course</h3>
    <p>Create an account once. Every card you check is then saved, and your teacher sees your homework and quiz results. You can also practise without an account.</p>
    <div class="authbtns"><button class="btn primary" type="button" data-auth="signup">Create account</button><button class="btn" type="button" data-auth="signin">Sign in</button></div></section>`;
  const signup = v === "signup";
  if (v === "forgot") return `<section class="reg"><h3>Reset your password</h3>
    <form id="f-forgot" class="authf"><input id="fe" type="email" autocomplete="email" placeholder="Your email" required>
    <button class="btn primary" type="submit">Send reset link</button><button class="btn" type="button" data-auth="signin">Back</button></form><p class="autherr" id="autherr"></p></section>`;
  return `<section class="reg"><h3>${signup ? "Create your account" : "Sign in"}</h3>
    <form id="f-auth" class="authf">
      ${signup ? `<input id="an" type="text" autocomplete="name" maxlength="60" placeholder="Your full name" required>` : ""}
      <input id="ae" type="email" autocomplete="email" placeholder="Email" required>
      <input id="ap" type="password" autocomplete="${signup ? "new-password" : "current-password"}" minlength="8" placeholder="Password${signup ? " (8+ characters)" : ""}" required>
      <button class="btn primary" type="submit">${signup ? "Create account" : "Sign in"}</button>
    </form>
    <p class="authalt">${signup ? `Have an account? <button class="linkbtn" type="button" data-auth="signin">Sign in</button>`
      : `New here? <button class="linkbtn" type="button" data-auth="signup">Create an account</button> · <button class="linkbtn" type="button" data-auth="forgot">Forgot password?</button>`}</p>
    <p class="autherr" id="autherr"></p></section>`;
}
function wireAuth() {
  app.querySelectorAll("[data-auth]").forEach(b => b.onclick = () => { CLOUD.authView = b.dataset.auth; refresh(); });
  const err = m => { const e = document.getElementById("autherr"); if (e) e.textContent = m; };
  const f = document.getElementById("f-auth");
  if (f) f.onsubmit = async ev => {
    ev.preventDefault(); if (CLOUD.busy) return; CLOUD.busy = true; err("");
    const email = document.getElementById("ae").value.trim(), password = document.getElementById("ap").value;
    let r;
    if (CLOUD.authView === "signup") {
      const name = document.getElementById("an").value.trim();
      r = await CLOUD.sb.auth.signUp({ email, password, options: { data: { name } } });
      if (!r.error && !r.data.session) { CLOUD.busy = false; err("Check your email to confirm the account, then sign in."); return; }
    } else r = await CLOUD.sb.auth.signInWithPassword({ email, password });
    CLOUD.busy = false;
    if (r.error) err(r.error.message.includes("Invalid login") ? "Email or password is wrong." : r.error.message);
    else CLOUD.authView = null;
  };
  const fg = document.getElementById("f-forgot");
  if (fg) fg.onsubmit = async ev => {
    ev.preventDefault();
    const { error } = await CLOUD.sb.auth.resetPasswordForEmail(document.getElementById("fe").value.trim(), { redirectTo: location.origin + location.pathname });
    err(error ? error.message : "If that email has an account, a reset link is on its way.");
  };
  const np = document.getElementById("f-newpass");
  if (np) np.onsubmit = async ev => {
    ev.preventDefault();
    const { error } = await CLOUD.sb.auth.updateUser({ password: document.getElementById("np").value });
    if (error) err(error.message); else { CLOUD.authView = null; refresh(); }
  };
}
function renderAcct() {
  const a = document.getElementById("acct");
  if (CLOUD.mode === "teacher") {
    a.innerHTML = `<span class="who"><span class="dotok"></span>Teacher</span><button class="tabsheet" type="button" id="toSheet">Tracking sheet</button><button class="linkbtn light" type="button" id="so">Sign out</button>`;
    document.getElementById("toSheet").onclick = () => go("tracking");
  } else if (CLOUD.mode === "student") {
    a.innerHTML = `<span class="who"><span class="dotok"></span><b></b> · saving</span><button class="linkbtn light" type="button" id="so">Sign out</button>`;
    a.querySelector("b").textContent = (CLOUD.profile && CLOUD.profile.name) || "Student";
  } else if (CLOUD.mode === "guest") {
    a.innerHTML = `<span class="who"><span class="dotoff"></span>Not saving</span><button class="linkbtn light" type="button" id="si">Sign in</button>`;
    document.getElementById("si").onclick = () => { CLOUD.authView = "signin"; go(""); };
  } else a.innerHTML = "";
  const so = document.getElementById("so");
  if (so) so.onclick = async () => { await CLOUD.sb.auth.signOut(); };
}

/* ============================ data ============================ */
async function loadManifest() {
  const r = await fetch("data/manifest.json", { cache: "no-cache" });
  DATA = (await r.json()).lessons;
}
async function full(d) {
  if (FULL[d.id]) return FULL[d.id];
  const r = await fetch(`data/lessons/${d.id}.json?v=${d.v}`);
  const x = await r.json();
  FULL[d.id] = { ...d, ...x };
  return FULL[d.id];
}
function fullSet(d, sid) { return FULL[d.id] && FULL[d.id].sets.find(s => s.id === sid); }

/* ============================ helpers ============================ */
function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }
function st(lid, sid, i) { const a = (state[lid] ||= {}), b = (a[sid] ||= {}); return (b[i] ||= { sel: {}, checked: false, answer: false, seen: false }); }
function store(k, v) { try { localStorage.setItem(k, v); } catch (_) {} }
function load(k) { try { return localStorage.getItem(k); } catch (_) { return null; } }
// "Continue" lesson is remembered per account, not per device.
function lastKey() { return "iraab-last" + (CLOUD.user ? "-" + CLOUD.user.id : ""); }
function fieldsOf(set, c) { return c.fields || set.fields; }
function optsOf(f, r) { return (r.opts && r.opts[f.key]) || f.options; }
function isAr(lbl) { return AR_RE.test(lbl) && !LAT_RE.test(lbl); }
function scoreOf(set, lid, i) {
  const s = st(lid, set.id, i), c = set.cards[i], fs = fieldsOf(set, c);
  let ok = 0;
  c.rows.forEach((r, j) => { const x = s.sel[j] || {}; if (fs.every(f => x[f.key] === r.ans[f.key])) ok++; });
  return { ok, total: c.rows.length };
}
function cardStatus(d, sid, i) {
  const s = st(d.id, sid, i), set = fullSet(d, sid);
  if (s.checked && set) { const v = scoreOf(set, d.id, i); return v.ok === v.total ? "done" : "part"; }
  const rec = myRec(d.id, sid, i);
  if (rec) return rec.best === rec.total ? "done" : "part";
  return "";
}
function setProgress(d, s) {
  const n = s.n ?? s.cards.length;   // manifest sets carry n; full lesson sets carry the cards
  let done = 0, tried = 0;
  for (let i = 0; i < n; i++) { const k = cardStatus(d, s.id, i); if (k) tried++; if (k === "done") done++; }
  return { done, tried, n };
}

/* ============================ routing ============================ */
function views(d) {
  const v = [{ id: "intro", label: d.introLabel || "Intro" }];
  d.sets.forEach(s => v.push({ id: s.id, label: s.label, set: true }));
  if (isTeacher()) v.push({ id: "key", label: "Answer key" });
  if (d.hasTeacher && isTeacher()) v.push({ id: "teacher", label: "Teacher" });
  return v;
}
function parse() {
  const h = decodeURIComponent(location.hash.slice(1));
  if (h === "tracking") return { tracking: true };
  for (const d of DATA) {
    if (h === d.id) return { d, v: "intro" };
    for (const v of views(d)) if (h === d.id + "-" + v.id) return { d, v: v.id, set: v.set };
  }
  return null;
}
function go(hash) { if (location.hash.slice(1) === hash) route(); else if (!hash) { history.pushState(null, "", location.pathname + location.search); route(); } else location.hash = hash; }
window.addEventListener("hashchange", () => route());
document.getElementById("brand").onclick = () => go("");
let routeSeq = 0;
function refresh() { renderAcct(); route(true); }
async function route(keepScroll) {
  const seq = ++routeSeq;
  const r = parse();
  const tabs = document.getElementById("tabs"), crumb = document.getElementById("crumb");
  if (!r) { tabs.innerHTML = ""; crumb.textContent = ""; renderHome(); if (!keepScroll) window.scrollTo(0, 0); return; }
  if (r.tracking) {
    tabs.innerHTML = ""; crumb.textContent = "Tracking sheet";
    if (CLOUD.mode !== "teacher") { app.innerHTML = `<div class="empty">The tracking sheet is for the teacher's account.</div>`; return; }
    app.innerHTML = `<div class="empty">Loading the class list…</div>`;
    await loadRoster(); if (seq !== routeSeq) return; renderTracking(); return;
  }
  const { d, v } = r;
  store(lastKey(), d.id + "-" + v);
  crumb.textContent = d.title;
  tabs.innerHTML = views(d).map(x => `<button class="tab" type="button" aria-current="${x.id === v}" data-h="${x.id === "intro" ? d.id : d.id + "-" + x.id}">${esc(x.label)}</button>`).join("");
  tabs.querySelectorAll(".tab").forEach(b => b.onclick = () => go(b.dataset.h));
  if (!FULL[d.id]) app.innerHTML = `<div class="empty">Loading ${esc(d.title)}…</div>`;
  let fd;
  try { fd = await full(d); } catch (_) { app.innerHTML = `<div class="empty">This lesson could not be loaded. Check your connection and reload.</div>`; return; }
  if (seq !== routeSeq) return;
  if (r.set) renderStage(fd, fd.sets.find(s => s.id === v));
  else if (v === "key") renderKey(fd);
  else if (v === "teacher") renderTeacher(fd);
  else renderStatic(fd);
  if (!keepScroll) window.scrollTo(0, 0);
}

/* ============================ home ============================ */
function tile(d) {
  const nCards = d.sets.reduce((a, s) => a + s.n, 0);
  let mine = "";
  if (CLOUD.mode === "student") {
    const done = d.sets.reduce((a, s) => a + setProgress(d, s).done, 0);
    mine = `<div class="prog" aria-hidden="true"><i style="width:${Math.round(100 * done / nCards)}%"></i></div><span class="mine">${done} of ${nCards} cards fully correct</span>`;
  }
  const setBtns = d.sets.map((s, k) => `<button class="btn ${k === 0 ? "primary" : ""}" type="button" data-h="${d.id}-${s.id}">${esc(s.label)}</button>`).join("");
  const unit = d.stage === 0;
  return `<article class="tile ${unit ? "unit" : ""}">
    ${unit ? `<div class="unitno">UNIT ${d.order}</div>` : ""}
    <div class="tile-top"><h3>${esc(d.title)}</h3><span class="count">${nCards} cards</span></div>
    ${unit ? `<div class="sample" dir="rtl">${esc(d.ar)}</div>` : `<div class="tar" dir="rtl">${esc(d.ar)}</div><div class="sample" dir="rtl">${d.sample || ""}</div>`}
    <p>${esc(d.blurb)}</p>${mine}
    <div class="tile-actions"><button class="btn" type="button" data-h="${d.id}">${esc(d.introLabel || "Intro")}</button>${setBtns}
      ${isTeacher() ? `<button class="btn" type="button" data-h="${d.id}-key">Answer key</button>` : ""}</div></article>`;
}
function stageSection(title, ar, chips, list, cls) {
  return `<section class="stage"><div class="stage-h"><h2>${title}</h2><span class="sar" dir="rtl">${ar}</span>
    <div class="cases-mini">${chips}</div></div><div class="shelf ${cls || ""}">${list.map(tile).join("")}</div></section>`;
}
function renderHome() {
  const last = load(lastKey());
  const lastD = last && DATA.find(d => last === d.id + "-intro" || views(d).some(v => last === d.id + "-" + v.id));
  const chip = t => `<span class="cm-chip on">${t}</span>`;
  const byStage = s => DATA.filter(d => d.stage === s).sort((a, b) => (a.order || 0) - (b.order || 0));
  app.innerHTML = `${authPanel()}
  <section class="home-hero">
    <div class="eyebrow">ARABIC GRAMMAR · LESSONS, HOMEWORK AND QUIZZES</div>
    <h1>${isTeacher() ? "Choose a lesson<br>to open in class" : "Your iʿrāb course"}</h1>
    <p>New to the class? Start with Stage 0. Every card is live: tap an ending or an answer for each item, then check it.${isTeacher() ? " Use ← and → to move between cards." : ""}</p>
    <div class="wm" aria-hidden="true">الإِعْرَاب</div>
    <div class="how-strip"><span><b>1</b> Read the lesson</span><span><b>2</b> Practice in class</span><span><b>3</b> Homework at home</span><span><b>4</b> Check and see why</span>
    ${lastD ? `<button class="btn gold" type="button" data-h="${last.endsWith("-intro") ? lastD.id : last}" style="margin-left:auto">Continue: ${esc(lastD.title)}</button>` : ""}</div>
  </section>
  ${stageSection("Stage 0 · Foundations", "مَدْخَلٌ إِلَى النَّحْوِ", chip("الكَلِمَة") + chip("ال") + chip("الإِعْرَاب"), byStage(0), "s0")}
  ${stageSection("Stage 1 · Rafʿ and jarr", "الجُمْلَةُ الاسْمِيَّةُ", chip("رَفْع") + chip("جَرّ"), byStage(1))}
  ${stageSection("Stage 2 · Naṣb", "الجُمْلَةُ الفِعْلِيَّةُ", chip("رَفْع") + chip("نَصْب") + chip("جَرّ"), byStage(2))}`;
  app.querySelectorAll("[data-h]").forEach(b => b.onclick = () => go(b.dataset.h));
  wireAuth();
}

/* ============================ static views ============================ */
function renderStatic(d) {
  app.innerHTML = `${authPanel()}<div class="view">${d.intro || ""}
    <div class="ic-foot" style="justify-content:center;margin-top:24px">${d.sets.map((x, k) => `<button class="btn ${k ? "" : "primary"}" type="button" data-h="${d.id}-${x.id}">${esc(x.label)} →</button>`).join("")}</div></div>`;
  app.querySelectorAll(".ic-foot [data-h]").forEach(b => b.onclick = () => go(b.dataset.h));
  wireAuth();
}
function optLabel(f, r, k) { return optsOf(f, r).find(o => o.k === k) || { label: k }; }
function autoKey(set, c) {
  const fs = fieldsOf(set, c);
  return `<div class="autokey">${c.rows.map(r => `<div class="ak"><span class="aw">${esc(r.s)}</span><span class="aa">${fs.map(f => {
    const o = optLabel(f, r, r.ans[f.key]);
    return `<span class="${isAr(o.label) ? "arl" : ""}" style="border-color:${o.b || "#0f5257"};background:${o.bg || "#f2f8f8"};color:${o.t || "#0f5257"}">${esc(o.label)}</span>`;
  }).join("")}</span><span class="ay">${r.why || ""}</span></div>`).join("")}</div>`;
}
function keyOf(set, c) { return c.key || autoKey(set, c); }
function renderKey(d) {
  app.innerHTML = `<div class="view"><h2><span class="num">✓</span>Answer key · ${esc(d.title)}</h2>
    ${d.sets.map(s => `<h3 class="sh">${esc(s.label)}</h3><div class="key-list">${s.cards.map(c => c.key ? c.key :
      `<div class="kcard"><div class="khead"><span class="qn">${esc(c.n)}</span><span class="en">${esc(c.head.en)}</span></div>${c.prompt ? `<div class="ic-prompt" style="font-size:26px">${esc(c.prompt)}</div>` : ""}${autoKey(s, c)}</div>`).join("")}</div>`).join("")}</div>`;
}
function renderTeacher(d) {
  const set = d.sets[0];
  const rows = set.cards.map((c, i) => {
    const s = st(d.id, set.id, i), sc = scoreOf(set, d.id, i);
    const status = !s.checked ? `<span class="st-none">not checked</span>` : sc.ok === sc.total ? `<span class="st-ok">${sc.ok} / ${sc.total} ✓</span>` : `<span class="st-part">${sc.ok} / ${sc.total}</span>`;
    return `<tr><td><b>${esc(c.n)}</b></td><td style="color:#a87805">${esc(c.head.tag)}</td><td>${c.rows.length}</td>
      <td><input id="name-${d.id}-${i}" type="text" placeholder="Student name" value="${esc(names[d.id + i] || "")}" data-k="${d.id + i}" aria-label="Student for ${esc(c.n)}"></td>
      <td>${status}</td><td><button class="btn go" type="button" data-i="${i}">Open</button></td></tr>`;
  }).join("");
  app.innerHTML = `<div class="view">${d.teacher || ""}<h3 class="sh">Live results</h3>
    <p class="sub">Fills in as each card is checked on this screen. Words correct = ending and job both right.</p>
    <div class="res-wrap"><table class="res"><tr><th>Card</th><th>Level</th><th>Words</th><th>Student</th><th>Result</th><th></th></tr>${rows}</table></div></div>`;
  app.querySelectorAll("input[data-k]").forEach(inp => inp.oninput = () => names[inp.dataset.k] = inp.value);
  app.querySelectorAll(".go").forEach(b => b.onclick = () => { cur[d.id + "/" + set.id] = +b.dataset.i; go(d.id + "-" + set.id); });
}

/* ============================ card stage ============================ */
function renderStage(d, set) {
  const ck = d.id + "/" + set.id, i = Math.min(cur[ck] ?? 0, set.cards.length - 1), c = set.cards[i], s = st(d.id, set.id, i);
  const fs = fieldsOf(set, c), irab = !!c.toks;
  const pills = set.cards.map((x, k) => `<button class="pillnav ${cardStatus(d, set.id, k)} ${k === i ? "cur" : ""}" type="button" data-k="${k}" aria-label="Card ${esc(x.n)}">${esc(x.n.replace(/^[QEPH]/, ""))}</button>`).join("");
  const tagCls = /[A-Za-z]/.test(c.head.tag || "") ? "tag ref" : "tag";
  let top = "";
  if (irab) top = `<div class="ic-sent" id="sent">${c.toks.map((t, ti) => `<span class="tok">${c.rows.map((r, j) => [r, j]).filter(([r]) => r.tok === ti)
      .map(([r, j]) => `<span class="pc" data-r="${j}">${esc(r.s)}</span>`).join("")}</span>`).join(" ")}</div>`;
  else if (c.prompt) top = `<div class="ic-prompt">${esc(c.prompt)}</div>${c.promptEn ? `<div class="ic-prompt-en">“${esc(c.promptEn)}”</div>` : ""}`;
  const help = irab ? `<div class="ic-help"><span><b>Ending:</b> tap a circle (— = never changes)</span><span><b>Job:</b> tap a colour. The sentence colours itself.</span></div>` : "";
  const rec = myRec(d.id, set.id, i);
  const rows = c.rows.map((r, j) => {
    const x = s.sel[j] || {};
    const groups = fs.map(f => {
      const opts = optsOf(f, r);
      const lbl = !irab && fs.length > 1 && f.label ? `<span class="fl">${esc(f.label)}</span>` : "";
      if (f.type === "end") return `<div class="fg ends">${lbl}${opts.map(o => `<button class="eb ${x[f.key] === o.k ? "sel" : ""}" type="button" data-r="${j}" data-f="${f.key}" data-v="${esc(o.k)}" aria-pressed="${x[f.key] === o.k}" aria-label="ending ${o.k === DASH ? "none" : esc(o.k)}">${esc(o.label)}</button>`).join("")}</div>`;
      return `<div class="fg">${lbl}${opts.map(o => {
        const on = x[f.key] === o.k, col = o.b ? `border-color:${o.b};color:${o.t};background:${on ? o.b : o.bg}` : "";
        return `<button class="jb ${o.b ? "" : "neutral"} ${isAr(o.label) ? "arlab" : ""} ${on ? "sel" : ""}" type="button" data-r="${j}" data-f="${f.key}" data-v="${esc(o.k)}" aria-pressed="${on}" style="${col}">${esc(o.label)}</button>`;
      }).join("")}</div>`;
    }).join("");
    const word = `<span class="rwd">${esc(r.s)}${r.gloss ? `<span class="gl">${esc(r.gloss)}</span>` : ""}</span>`;
    return `<div class="row ${irab ? "irab" : "gen"}" id="row-${j}"><span class="rn">${j + 1}</span>${word}<div class="fields">${groups}</div>${r.why ? `<div class="why">${r.why}</div>` : ""}</div>`;
  }).join("");
  const canAnswer = isTeacher() || s.checked || (rec && rec.tries > 0);
  const p = setProgress(d, set);
  app.innerHTML = `${authPanel()}
  <div class="setnote"><h2>${esc(set.label)}</h2><span>${p.done} of ${p.n} cards fully correct${CLOUD.mode === "student" ? " · saved to your record" : ""}</span></div>
  <div class="stage-top"><div class="pills">${pills}</div>
    <div class="navbtns"><button class="btn" type="button" id="prev" ${i === 0 ? "disabled" : ""}>← Prev</button><button class="btn" type="button" id="next" ${i === set.cards.length - 1 ? "disabled" : ""}>Next →</button></div></div>
  <article class="icard">
    <div class="ic-head"><span class="qn">${esc(c.n)}</span><span class="en">${irab ? `“${esc(c.head.en)}”` : esc(c.head.en)}</span>${c.head.tag ? `<span class="${tagCls}">${esc(c.head.tag)}</span>` : ""}</div>
    ${top}${c.note ? `<div class="ic-note">${esc(c.note)}</div>` : ""}${help}
    <div class="rows">${rows}</div>
    <div class="ic-foot">
      <button class="btn primary" type="button" id="check">Check</button>
      <button class="btn" type="button" id="ans" ${canAnswer ? "" : "disabled"}>${s.answer ? "Hide answer" : "Show answer"}</button>
      <button class="btn" type="button" id="clear">Clear card</button>
      <span id="savemsg" class="saved"></span><span class="score" id="score"></span>
    </div>
    ${!canAnswer ? `<p class="lockmsg" id="lockmsg">Check your answers first. Then you can open the answer.</p>` : ""}
    ${rec && !s.checked ? `<p class="lockmsg">Saved before: ${rec.best} / ${rec.total} correct after ${rec.tries} ${rec.tries === 1 ? "try" : "tries"}.</p>` : ""}
    <div class="answer" id="answer" ${s.answer ? "" : "hidden"}><p class="answer-h">Answer</p>${keyOf(set, c)}</div>
  </article>`;
  paint(d, set, i); wireAuth();
  app.querySelectorAll(".pillnav").forEach(b => b.onclick = () => { cur[ck] = +b.dataset.k; renderStage(d, set); });
  document.getElementById("prev").onclick = () => step(d, set, -1);
  document.getElementById("next").onclick = () => step(d, set, 1);
  app.querySelectorAll(".rows button[data-f]").forEach(b => b.onclick = () => pick(d, set, i, +b.dataset.r, b.dataset.f, b.dataset.v));
  document.getElementById("check").onclick = () => {
    s.checked = true; const sc = scoreOf(set, d.id, i);
    saveResult(d, set, i, sc, s.seen);
    paint(d, set, i); refreshPills(d, set);
    document.getElementById("ans").disabled = false; const lm = document.getElementById("lockmsg"); if (lm) lm.remove();
  };
  document.getElementById("ans").onclick = () => { s.answer = !s.answer; if (s.answer) s.seen = true; renderStage(d, set); if (s.answer) document.getElementById("answer").scrollIntoView({ behavior: "smooth", block: "nearest" }); };
  document.getElementById("clear").onclick = () => { state[d.id][set.id][i] = { sel: {}, checked: false, answer: false, seen: s.seen }; renderStage(d, set); };
}
function step(d, set, k) { const ck = d.id + "/" + set.id, n = (cur[ck] ?? 0) + k; if (n >= 0 && n < set.cards.length) { cur[ck] = n; renderStage(d, set); } }
function pick(d, set, i, r, field, val) {
  const s = st(d.id, set.id, i), x = (s.sel[r] ||= {}), c = set.cards[i], f = fieldsOf(set, c).find(f => f.key === field);
  x[field] = x[field] === val ? undefined : val;
  s.checked = false;
  const opts = optsOf(f, c.rows[r]);
  document.querySelectorAll(`#row-${r} button[data-f="${field}"]`).forEach(b => {
    const on = b.dataset.v === x[field];
    b.classList.toggle("sel", on); b.setAttribute("aria-pressed", on);
    const o = opts.find(o => o.k === b.dataset.v); if (o && o.b && f.type !== "end") b.style.background = on ? o.b : o.bg;
  });
  paint(d, set, i); refreshPills(d, set);
}
function paint(d, set, i) {
  const s = st(d.id, set.id, i), c = set.cards[i], fs = fieldsOf(set, c);
  const cf = set.colourField && fs.find(f => f.key === set.colourField);
  c.rows.forEach((r, j) => {
    const x = s.sel[j] || {};
    if (cf) {
      const o = x[cf.key] && cf.options.find(o => o.k === x[cf.key]);
      const pc = app.querySelector(`.pc[data-r="${j}"]`);
      if (pc) { pc.style.backgroundColor = o ? o.bg : ""; pc.style.boxShadow = o ? `inset 0 -4px 0 ${o.b}` : ""; }
    }
    const row = document.getElementById("row-" + j);
    row.classList.remove("ok", "bad", "showwhy");
    row.querySelectorAll(".right,.wrong,.want").forEach(b => b.classList.remove("right", "wrong", "want"));
    if (!s.checked) return;
    const good = fs.every(f => x[f.key] === r.ans[f.key]);
    row.classList.add(good ? "ok" : "bad");
    fs.forEach(f => row.querySelectorAll(`button.sel[data-f="${f.key}"]`).forEach(b => b.classList.add(b.dataset.v === r.ans[f.key] ? "right" : "wrong")));
    if (s.answer) {
      row.classList.add("showwhy");
      fs.forEach(f => row.querySelector(`button[data-f="${f.key}"][data-v="${CSS.escape(r.ans[f.key])}"]`)?.classList.add("want"));
    }
  });
  const sc = document.getElementById("score"), v = scoreOf(set, d.id, i);
  if (s.checked) { sc.textContent = `${v.ok} / ${v.total} correct` + (v.ok === v.total ? " ✓" : ""); sc.className = "score " + (v.ok === v.total ? "ok" : "part"); }
  else { const filled = c.rows.filter((r, j) => fs.every(f => (s.sel[j] || {})[f.key])).length; sc.textContent = `${filled} / ${v.total} answered`; sc.className = "score"; }
}
function refreshPills(d, set) {
  app.querySelectorAll(".pillnav").forEach(b => {
    const cls = cardStatus(d, set.id, +b.dataset.k);
    b.classList.toggle("done", cls === "done"); b.classList.toggle("part", cls === "part");
  });
}
document.addEventListener("keydown", ev => {
  if (ev.target.closest && ev.target.closest("input, textarea")) return;
  const r = parse(); if (!r || !r.set || !FULL[r.d.id]) return;
  const set = FULL[r.d.id].sets.find(s => s.id === r.v);
  if (ev.key === "ArrowRight") step(FULL[r.d.id], set, 1);
  if (ev.key === "ArrowLeft") step(FULL[r.d.id], set, -1);
});

/* ============================ tracking sheet ============================ */
function columns() {
  const cols = [];
  [0, 1, 2].forEach(sg => DATA.filter(d => d.stage === sg).sort((a, b) => (a.order || 0) - (b.order || 0))
    .forEach(d => d.sets.forEach(s => cols.push({ d, s, stage: sg }))));
  return cols;
}
function setStats(rec, d, s) {
  let done = 0, tried = 0, best = 0, total = 0;
  for (let i = 0; i < s.n; i++) { const r = rec && rec[resKey(d.id, s.id, i)]; if (r) { tried++; best += r.best; total += r.total; if (r.best === r.total) done++; } }
  return { done, tried, n: s.n, pct: total ? Math.round(100 * best / total) : null };
}
function cellHtml(x) {
  if (!x.tried) return `<span class="cell none">—</span>`;
  const cls = x.done === x.n && x.pct === 100 ? "c3" : x.pct >= 75 ? "c2" : x.pct >= 50 ? "c1" : "c0";
  return `<span class="cell ${cls}" title="${x.tried} of ${x.n} cards tried, ${x.pct}% of items correct">${x.done}/${x.n}<br><small>${x.pct}%</small></span>`;
}
function fmtDate(t) { try { return t ? new Date(t).toLocaleDateString(undefined, { day: "numeric", month: "short" }) : ""; } catch (_) { return ""; } }
function renderTracking() {
  const cols = columns(), roster = CLOUD.roster || [], res = CLOUD.allRes || {};
  const stageNames = ["Stage 0", "Stage 1", "Stage 2"];
  const grp = [0, 1, 2].map(sg => { const n = cols.filter(c => c.stage === sg).length; return n ? `<th colspan="${n}">${stageNames[sg]}</th>` : ""; }).join("");
  const head = cols.map(c => `<th title="${esc(c.d.title)} · ${esc(c.s.label)}">${esc(c.d.stage === 0 ? "U" + c.d.order : c.d.title.replace(/^Iʿrāb /, "").slice(0, 16))}<br><small>${esc(c.s.label)}</small></th>`).join("");
  const body = roster.map(r => `<tr><td class="stu"><b></b><small></small><button class="btn det" type="button" data-id="${esc(r.id)}">Details</button></td>${cols.map(c => `<td>${cellHtml(setStats(res[r.id], c.d, c.s))}</td>`).join("")}</tr>`).join("");
  app.innerHTML = `<div class="trk-top"><h2>Tracking sheet</h2><p class="sub">${roster.length} student${roster.length === 1 ? "" : "s"}. Each cell: cards fully correct / cards in the set, and % of items right (best try before opening the answer).</p>
    <span class="sp"></span><button class="btn" type="button" id="reload">Refresh</button><button class="btn" type="button" id="csv">Download CSV</button></div>
    ${roster.length ? `<div class="trk-wrap"><table class="trk"><thead><tr class="grp"><th class="stu"></th>${grp}</tr><tr><th class="stu">Student</th>${head}</tr></thead><tbody>${body}</tbody></table></div>`
      : `<div class="trk-wrap"><div class="empty">No students yet. Share the site link; each student creates an account on first visit.</div></div>`}
    <div id="detail"></div>`;
  app.querySelectorAll("td.stu").forEach((td, k) => {
    const r = roster[k];
    td.querySelector("b").textContent = r.name || "Unnamed";
    td.querySelector("small").textContent = [r.email, r.last_active ? "active " + fmtDate(r.last_active) : ""].filter(Boolean).join(" · ");
  });
  app.querySelectorAll(".det").forEach(b => b.onclick = () => { CLOUD.detail = b.dataset.id; renderDetail(roster.find(r => r.id === b.dataset.id)); });
  document.getElementById("reload").onclick = () => route(true);
  document.getElementById("csv").onclick = () => exportCsv(roster, cols);
  if (CLOUD.detail) { const r = roster.find(r => r.id === CLOUD.detail); if (r) renderDetail(r); }
}
function renderDetail(r) {
  const box = document.getElementById("detail"); if (!box || !r) return;
  const rec = (CLOUD.allRes || {})[r.id] || {};
  const sets = columns().map(c => {
    const cards = c.s.cards.map((card, i) => { const x = rec[resKey(c.d.id, c.s.id, i)];
      return x ? `<span class="${x.best === x.total ? "ok" : "part"}" title="first try ${x.first_ok}/${x.total}, ${x.tries} tries${x.seen ? ", answer opened" : ""}">${esc(card.n)} ${x.best}/${x.total}</span>` : `<span>${esc(card.n)}</span>`; }).join("");
    return `<div class="dset"><b>${esc(c.d.title)} · ${esc(c.s.label)}</b><div class="dcards">${cards}</div></div>`;
  }).join("");
  box.innerHTML = `<div class="detail"><h3></h3><p class="sub">Joined ${fmtDate(r.joined_at)}. Green = fully correct. Hover a card for first try and number of tries.</p>
    <div class="dsets">${sets}</div>
    <div class="ic-foot"><button class="btn" type="button" id="closeDet">Close</button><span style="flex:1"></span>
    <span id="rmzone"><button class="btn danger" type="button" id="rm">Remove student…</button></span></div></div>`;
  box.querySelector("h3").textContent = r.name || "Unnamed";
  document.getElementById("closeDet").onclick = () => { CLOUD.detail = null; box.innerHTML = ""; };
  document.getElementById("rm").onclick = () => {
    const z = document.getElementById("rmzone");
    z.innerHTML = `<span class="lockmsg">Delete this student's profile and all their results?</span> <button class="btn danger" type="button" id="rmyes">Delete</button> <button class="btn" type="button" id="rmno">Keep</button>`;
    document.getElementById("rmno").onclick = () => renderDetail(r);
    document.getElementById("rmyes").onclick = async () => {
      const { error } = await CLOUD.sb.from("profiles").delete().eq("id", r.id);
      if (error) { z.textContent = "Could not delete. Try again."; return; }
      CLOUD.detail = null; route(true);
    };
  };
  box.scrollIntoView({ behavior: "smooth", block: "nearest" });
}
function exportCsv(roster, cols) {
  const q = v => `"${String(v ?? "").replace(/"/g, '""')}"`;
  const res = CLOUD.allRes || {};
  const lines = [["Student", "Email", "Joined", "Last active", ...cols.map(c => `${c.d.title} - ${c.s.label}`)].map(q).join(",")];
  roster.forEach(r => lines.push([r.name, r.email, (r.joined_at || "").slice(0, 10), (r.last_active || "").slice(0, 10),
    ...cols.map(c => { const x = setStats(res[r.id], c.d, c.s); return x.tried ? `${x.done}/${x.n} (${x.pct}%)` : ""; })].map(q).join(",")));
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob(["﻿" + lines.join("\n")], { type: "text/csv" }));
  a.download = `iraab-results-${new Date().toISOString().slice(0, 10)}.csv`;
  document.body.appendChild(a); a.click(); a.remove();
}

/* ============================ boot ============================ */
(async function boot() {
  if (CFG.supabaseUrl && CFG.supabaseAnonKey) CLOUD.mode = "guest";
  try { await loadManifest(); } catch (_) { app.innerHTML = `<div class="empty">The course could not be loaded. Check your connection and reload.</div>`; return; }
  renderAcct(); route();
  try { await initCloud(); } catch (e) { CLOUD.mode = "local"; CLOUD.status = ""; console.error(e); }
  refresh();
})();
