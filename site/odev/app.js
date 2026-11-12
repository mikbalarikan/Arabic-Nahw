/* İrab Ödevleri: öğrenciler her dersin irab ödevini tablo hâlinde doldurup gönderir; öğretmen takip eder. */
"use strict";
const app = document.getElementById("app");
const CFG = window.IRAAB_CONFIG || {};
const ROWS = [["kb", "Kelime bilgisi"], ["g", "Cümledeki görevi"], ["i", "İrab"]];
let MAN = [], OPT = {};
const LES = {};                       // id -> lesson (public text)
const C = { mode: "local", sb: null, user: null, me: null, subs: new Map(), keys: new Map(),
  roster: null, all: null, view: null, busy: false, status: "" };
// mode: local (no backend), guest, student, teacher

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const lst = v => Array.isArray(v) ? v : [v];
const fmt = t => t ? new Date(t).toLocaleString("tr-TR", { day: "2-digit", month: "short", hour: "2-digit", minute: "2-digit" }) : "";
function store(k, v) { try { localStorage.setItem(k, v); } catch (_) {} }
function load(k) { try { return localStorage.getItem(k); } catch (_) { return null; } }

/* ============================ cloud ============================ */
async function initCloud() {
  if (!CFG.supabaseUrl || !CFG.supabaseAnonKey || !window.supabase) return;
  C.sb = window.supabase.createClient(CFG.supabaseUrl, CFG.supabaseAnonKey, { auth: { flowType: "pkce", persistSession: true, detectSessionInUrl: true } });
  C.mode = "guest";
  C.sb.auth.onAuthStateChange((ev, session) => {
    if (ev === "PASSWORD_RECOVERY") { C.view = "newpass"; route(); }
    const id = session && session.user && session.user.id;
    if (id !== (C.user && C.user.id)) { C.user = session ? session.user : null; loadAccount(); }
  });
  const { data } = await C.sb.auth.getSession();
  C.user = data.session ? data.session.user : null;
  await loadAccount(true);
}
async function loadAccount(initial) {
  C.me = null; C.subs = new Map(); C.keys = new Map(); C.roster = null; C.all = null; C.status = "";
  if (!C.user) { C.mode = "guest"; if (!initial) route(); return; }
  const { data: prof } = await C.sb.from("profiles").select("role,name").eq("id", C.user.id).maybeSingle();
  if (prof && prof.role === "teacher") {
    C.mode = "teacher"; C.me = { name: prof.name || "Öğretmen" };
  } else {
    C.mode = "student";
    const meta = C.user.user_metadata || {};
    const j = await C.sb.rpc("tr_join", { p_name: meta.name || (prof && prof.name) || "" });
    if (j.error) C.status = "Hesap yüklenemedi: " + j.error.message;
    const { data: me } = await C.sb.from("tr_students").select("*").eq("id", C.user.id).maybeSingle();
    C.me = me || { name: meta.name || "" };
    const { data: subs } = await C.sb.from("tr_submissions").select("lesson,answers,tries,submitted_at,updated_at").eq("user_id", C.user.id);
    (subs || []).forEach(s => C.subs.set(s.lesson, s));
  }
  await loadKeys();
  route();
}
async function loadKeys() {
  const { data } = await C.sb.from("tr_keys").select("lesson,key,released");
  C.keys = new Map((data || []).map(k => [k.lesson, k]));
}
async function loadRoster() {
  const [{ data: st }, { data: subs }] = await Promise.all([
    C.sb.from("tr_students").select("*").order("name"),
    C.sb.from("tr_submissions").select("user_id,lesson,answers,tries,submitted_at,updated_at"),
  ]);
  C.roster = st || [];
  C.all = {};
  (subs || []).forEach(s => { (C.all[s.user_id] ||= {})[s.lesson] = s; });
}

/* ============================ grading ============================ */
// answers[item][part] = [kb, g, i]; key[item][part] = [[kb...], [g...], [i...]]
function grade(answers, key) {
  let ok = 0, total = 0; const per = [];
  key.forEach((parts, a) => {
    let o = 0, t = 0;
    parts.forEach((cell, p) => cell.forEach((acc, f) => {
      t++; const v = answers && answers[a] && answers[a][p] && answers[a][p][f];
      if (v && acc.includes(v)) o++;
    }));
    per.push([o, t]); ok += o; total += t;
  });
  return { ok, total, per, pct: total ? Math.round(100 * ok / total) : 0 };
}

/* ============================ auth UI ============================ */
function authPanel() {
  if (C.mode === "local") return `<section class="panel warn"><p>Önizleme: sunucu ayarı yok, gönderim kapalı.</p></section>`;
  if (C.status) return `<section class="panel warn"><p>${esc(C.status)}</p></section>`;
  if (C.view === "newpass") return `<section class="panel"><h3>Yeni şifre</h3><form id="f-np" class="authf">
    <input id="np" type="password" minlength="8" autocomplete="new-password" placeholder="Yeni şifre (en az 8 karakter)" required>
    <button class="btn primary">Kaydet</button></form><p class="err" id="aerr"></p></section>`;
  if (C.mode !== "guest") return "";
  const v = C.view || "signup";
  if (v === "forgot") return `<section class="panel"><h3>Şifre sıfırlama</h3><form id="f-fg" class="authf">
    <input id="fe" type="email" autocomplete="email" placeholder="E-posta" required><button class="btn primary">Bağlantı gönder</button>
    <button class="btn" type="button" data-v="signin">Geri</button></form><p class="err" id="aerr"></p></section>`;
  const up = v === "signup";
  return `<section class="panel"><h3>${up ? "Kayıt ol" : "Giriş yap"}</h3>
    <p class="note">${up ? "Ödev göndermek için bir kez kayıt olun. Hocanız gönderdiğiniz ödevleri görür." : "Kayıtlı e-posta ve şifrenizle girin."}</p>
    <form id="f-au" class="authf">
      ${up ? `<input id="an" type="text" autocomplete="name" maxlength="60" placeholder="Ad Soyad" required>` : ""}
      <input id="ae" type="email" autocomplete="email" placeholder="E-posta" required>
      <input id="ap" type="password" minlength="8" autocomplete="${up ? "new-password" : "current-password"}" placeholder="Şifre${up ? " (en az 8 karakter)" : ""}" required>
      <button class="btn primary">${up ? "Kayıt ol" : "Giriş yap"}</button></form>
    <p class="alt">${up ? `Hesabınız var mı? <button class="link" type="button" data-v="signin">Giriş yapın</button>`
      : `Yeni misiniz? <button class="link" type="button" data-v="signup">Kayıt olun</button> · <button class="link" type="button" data-v="forgot">Şifremi unuttum</button>`}</p>
    <p class="err" id="aerr"></p></section>`;
}
function wireAuth() {
  app.querySelectorAll("[data-v]").forEach(b => b.onclick = () => { C.view = b.dataset.v; route(); });
  const err = m => { const e = document.getElementById("aerr"); if (e) e.textContent = m; };
  const f = document.getElementById("f-au");
  if (f) f.onsubmit = async ev => {
    ev.preventDefault(); if (C.busy) return; C.busy = true; err("");
    const email = document.getElementById("ae").value.trim(), password = document.getElementById("ap").value;
    let r;
    if ((C.view || "signup") === "signup") {
      const name = document.getElementById("an").value.trim();
      r = await C.sb.auth.signUp({ email, password, options: { data: { name, course: "tr" } } });
      if (!r.error && !r.data.session) { C.busy = false; err("E-postanıza gelen onay bağlantısına tıklayın, sonra giriş yapın."); return; }
    } else r = await C.sb.auth.signInWithPassword({ email, password });
    C.busy = false;
    if (r.error) err(/Invalid login/.test(r.error.message) ? "E-posta veya şifre hatalı." : /already registered/.test(r.error.message) ? "Bu e-posta zaten kayıtlı. Giriş yapın." : r.error.message);
    else C.view = null;
  };
  const fg = document.getElementById("f-fg");
  if (fg) fg.onsubmit = async ev => {
    ev.preventDefault();
    const { error } = await C.sb.auth.resetPasswordForEmail(document.getElementById("fe").value.trim(), { redirectTo: location.origin + location.pathname });
    err(error ? error.message : "Bu e-posta kayıtlıysa sıfırlama bağlantısı gönderildi.");
  };
  const np = document.getElementById("f-np");
  if (np) np.onsubmit = async ev => {
    ev.preventDefault();
    const { error } = await C.sb.auth.updateUser({ password: document.getElementById("np").value });
    if (error) err(error.message); else { C.view = null; route(); }
  };
}
function renderAcct() {
  const a = document.getElementById("acct");
  if (C.mode === "teacher") a.innerHTML = `<span>Öğretmen</span><a class="tb" href="#/takip">Takip tablosu</a><button class="lb" id="so">Çıkış</button>`;
  else if (C.mode === "student") { a.innerHTML = `<span><b></b></span><button class="lb" id="so">Çıkış</button>`; a.querySelector("b").textContent = C.me && C.me.name || ""; }
  else if (C.mode === "guest") { a.innerHTML = `<button class="lb" id="si">Giriş yap</button>`; document.getElementById("si").onclick = () => { C.view = "signin"; location.hash = "#/"; route(); }; }
  else a.innerHTML = "";
  const so = document.getElementById("so");
  if (so) so.onclick = () => C.sb.auth.signOut();
}

/* ============================ router ============================ */
async function route() {
  renderAcct();
  const h = location.hash.replace(/^#\/?/, "").split("/");
  document.getElementById("crumb").textContent = "";
  if (h[0] === "d" && h[1]) return renderLesson(h[1], h[2] === "u" ? h[3] : null);
  if (h[0] === "takip") return renderSheet();
  renderHome();
}
window.addEventListener("hashchange", () => { window.scrollTo(0, 0); route(); });

/* ============================ home ============================ */
function status(m) {
  const k = C.keys.get(m.id), s = C.subs.get(m.id);
  if (C.mode === "teacher") {
    const n = C.all ? Object.values(C.all).filter(x => x[m.id]).length : null;
    return `${k ? (k.released ? `<span class="pill key">Anahtar açık</span>` : `<span class="pill">Anahtar kapalı</span>`) : `<span class="pill">Anahtar yüklenmedi</span>`}
      ${n !== null ? `<span class="pill">${n} gönderim</span>` : ""}`;
  }
  if (!s) return k && k.released ? `<span class="pill">Süre bitti</span>` : `<span class="pill wait">Bekliyor</span>`;
  if (k && k.released) { const g = grade(s.answers, k.key); return `<span class="pill ok">Puan: %${g.pct}</span>`; }
  return `<span class="pill ok">Gönderildi</span> <span class="note">${fmt(s.updated_at)}</span>`;
}
function renderHome() {
  if (C.mode === "teacher" && !C.roster) loadRoster().then(() => { if (!location.hash.replace(/^#\/?/, "")) renderHome(); });
  app.innerHTML = `<section class="hero"><h1>İrab Ödevleri</h1>
    <p>Bakara Sûresi Eşliğinde Kur'ân Dilbilgisi. Her dersin sonundaki ayetlerin irabını tabloda seçin ve gönderin. Cevap anahtarı açılana kadar ödevinizi düzeltip yeniden gönderebilirsiniz.</p></section>
    ${authPanel()}
    <div class="shelf">${MAN.map(m => `<a class="tile" href="#/d/${m.id}">
      <span class="k">İRAB BÖLÜMÜ ${m.irab} · ÇALIŞMA ${m.calisma}</span>
      <h3>${esc(m.title)}</h3><span class="note">${m.n} ayet · ${m.cells / 3} kelime parçası</span>
      <span class="st">${status(m)}</span></a>`).join("")}</div>`;
  wireAuth();
}

/* ============================ lesson ============================ */
async function getLesson(id) {
  if (LES[id]) return LES[id];
  const m = MAN.find(x => x.id === id); if (!m) return null;
  const r = await fetch(`data/${id}.json?v=${m.v}`);
  return (LES[id] = await r.json());
}
const draftKey = id => `odev-${id}-${C.user ? C.user.id : "anon"}`;
function emptyAnswers(L) { return L.items.map(it => it.words.flat().map(() => ["", "", ""])); }

async function renderLesson(id, uid) {
  const L = await getLesson(id);
  if (!L) { app.innerHTML = `<div class="empty">Ders bulunamadı. <a href="#/">Ana sayfa</a></div>`; return; }
  document.getElementById("crumb").textContent = `İrab Bölümü ${L.irab}`;
  const k = C.keys.get(id), key = k && k.key;
  let answers, editable = false, show = null, who = "";
  if (C.mode === "teacher") {
    if (!C.roster) await loadRoster();
    if (uid) {
      const st = C.roster.find(s => s.id === uid), s = C.all[uid] && C.all[uid][id];
      who = st ? st.name : "Öğrenci";
      answers = s ? s.answers : emptyAnswers(L); show = key ? "grade" : "plain";
      if (!s) who += " (göndermedi)";
    } else { answers = key ? key.map(it => it.map(c => c.map(v => v[0]))) : emptyAnswers(L); show = "key"; }
  } else {
    const s = C.subs.get(id);
    if (k && k.released) { answers = s ? s.answers : emptyAnswers(L); show = "grade"; }
    else {
      editable = true;
      const d = load(draftKey(id));
      answers = d ? JSON.parse(d) : s ? s.answers : emptyAnswers(L);
    }
  }
  const g = key && show === "grade" ? grade(answers, key) : null;

  let head = `<div class="lhead"><h1>${esc(L.title)}</h1><span class="k">İrab Bölümü ${L.irab} · Çalışma ${L.calisma}</span></div>`;
  if (C.mode === "teacher") {
    const subs = C.roster.map(s => ({ s, x: C.all[s.id] && C.all[s.id][id] })).filter(o => o.x);
    head += `<section class="panel">
      ${uid ? `<p><b>${esc(who)}</b> · ${g ? `Puan %${g.pct} (${g.ok}/${g.total})` : ""} <a class="btn" href="#/d/${id}">Anahtara dön</a></p>` :
      `<p>${key ? "Aşağıda cevap anahtarı gösteriliyor." : "Bu dersin anahtarı henüz yüklenmedi."}
        ${k ? `<button class="btn ${k.released ? "" : "gold"}" id="rel">${k.released ? "Anahtarı öğrencilerden gizle" : "Anahtarı öğrencilere aç (gönderimler kilitlenir)"}</button>` : ""}</p>`}
      <p class="note">Gönderenler (${subs.length}/${C.roster.length}): ${subs.map(o => `<a href="#/d/${id}/u/${o.s.id}">${esc(o.s.name)}</a>${key ? ` %${grade(o.x.answers, key).pct}` : ""}`).join(" · ") || "henüz yok"}</p></section>`;
  } else {
    head += authPanel();
    const s = C.subs.get(id);
    if (show === "grade") head += `<section class="panel"><p>${s ? `Puanınız: <b>%${g.pct}</b> (${g.ok}/${g.total} hücre doğru). Yanlış hücrelerin altında doğru cevap yazıyor.` : "Bu ödevi göndermediniz. Cevap anahtarı aşağıda."}</p></section>`;
    else head += `<p class="note">Her kelime parçası için üç seçim yapın. Parantez içindeki gizli zamirler de (ör. (هُوَ)) değerlendirilir. Seçimleriniz bu cihazda otomatik saklanır; göndermeyi unutmayın.</p>`;
  }

  app.innerHTML = head + L.items.map((it, a) => itemHTML(it, a, answers[a], editable, show, key && key[a], g && g.per[a])).join("") +
    (editable ? `<div class="submitbar"><button class="btn primary" id="send" ${C.mode !== "student" ? "disabled" : ""}>${C.subs.get(id) ? "Yeniden gönder" : "Gönder"}</button>
      <span class="msg" id="msg">${C.mode === "student" ? (C.subs.get(id) ? `Son gönderim: ${fmt(C.subs.get(id).updated_at)}` : "") : "Göndermek için önce kayıt olun veya giriş yapın."}</span></div>` : "");
  wireAuth();
  if (editable) {
    app.querySelectorAll("select").forEach(sel => sel.onchange = () => {
      const [a, p, f] = sel.dataset.c.split(".").map(Number);
      answers[a][p][f] = sel.value; sel.classList.toggle("empty", !sel.value);
      store(draftKey(id), JSON.stringify(answers));
    });
    const b = document.getElementById("send");
    if (b) b.onclick = () => submit(id, L, answers);
  }
  const rel = document.getElementById("rel");
  if (rel) rel.onclick = async () => {
    const { error } = await C.sb.rpc("tr_release", { p_lesson: id, p_on: !k.released });
    if (error) alertMsg(error.message); else { await loadKeys(); route(); }
  };
}
function alertMsg(m) { const e = document.getElementById("msg"); if (e) { e.textContent = m; e.className = "msg err"; } else C.status = m; }

function itemHTML(it, a, ans, editable, show, key, per) {
  const words = it.words;                    // RTL: first word on the right (table dir=rtl)
  let flat = 0;
  const cols = words.map(parts => parts.map(p => ({ p, i: flat++ })));
  const r1 = cols.map(ps => ps.length > 1 ? `<th class="w" colspan="${ps.length}">${esc(ps.filter(x => !x.p.h).map(x => x.p.t).join(""))}</th>`
    : `<th class="w" rowspan="2">${esc(ps[0].p.t)}</th>`).join("");
  const r2 = cols.map(ps => ps.length > 1 ? ps.map(x => `<th class="p ${x.p.h ? "h" : ""}">${esc(x.p.t)}</th>`).join("") : "").join("");
  const body = ROWS.map(([f, label], fi) => `<tr><th class="row" dir="ltr">${label}</th>${cols.flat().map(x => {
    const v = (ans && ans[x.i] && ans[x.i][fi]) || "";
    const acc = key && key[x.i] && key[x.i][fi];
    let cls = "";
    if (show === "grade" && acc) cls = acc.includes(v) ? "ok" : "bad";
    if (editable) return `<td dir="ltr"><select data-c="${a}.${x.i}.${fi}" class="${v ? "" : "empty"}" aria-label="${label}">
      <option value="">—</option>${OPT[f].map(o => `<option${o === v ? " selected" : ""}>${esc(o)}</option>`).join("")}</select></td>`;
    const alt = show === "key" && acc && acc.length > 1 ? `<div class="ans">ya da: ${esc(acc.slice(1).join(", "))}</div>` : "";
    return `<td dir="ltr" class="${cls}"><div class="v">${esc(v || "—")}</div>${cls === "bad" ? `<div class="ans">✓ ${esc(acc.join(" / "))}</div>` : ""}${alt}</td>`;
  }).join("")}</tr>`).join("");
  const text = words.map(ps => ps.filter(p => !p.h).map(p => p.t).join("")).join(" ");
  return `<section class="item"><div class="item-h"><span class="n">${it.n}.</span><span class="ref">${esc(it.ref)}</span>
      ${per ? `<span class="sc pill ${per[0] === per[1] ? "ok" : ""}">${per[0]}/${per[1]}</span>` : ""}</div>
    <div class="ayah" dir="rtl" lang="ar">${esc(text)}</div>${it.tr ? `<div class="tr">${esc(it.tr)}</div>` : ""}
    <div class="scroll" dir="rtl"><table class="irab" dir="rtl"><tr><th class="row" rowspan="2"></th>${r1}</tr><tr>${r2}</tr>${body}</table></div></section>`;
}

async function submit(id, L, answers) {
  if (C.busy) return;
  const empty = answers.flat(2).filter(v => !v).length;
  if (empty && !confirm(`${empty} boş hücre var. Yine de gönderilsin mi?`)) return;
  C.busy = true;
  const msg = document.getElementById("msg"); msg.className = "msg"; msg.textContent = "Gönderiliyor…";
  const { error } = await C.sb.rpc("tr_submit", { p_lesson: id, p_answers: answers });
  C.busy = false;
  if (error) { msg.className = "msg err"; msg.textContent = "Gönderilemedi: " + error.message; return; }
  const now = new Date().toISOString(), p = C.subs.get(id);
  C.subs.set(id, { lesson: id, answers: JSON.parse(JSON.stringify(answers)), tries: (p ? p.tries : 0) + 1, submitted_at: p ? p.submitted_at : now, updated_at: now });
  msg.textContent = `Gönderildi ✓ ${fmt(now)}. Anahtar açılana kadar değiştirip yeniden gönderebilirsiniz.`;
  document.getElementById("send").textContent = "Yeniden gönder";
}

/* ============================ teacher sheet ============================ */
async function renderSheet() {
  if (C.mode !== "teacher") { location.hash = "#/"; return; }
  document.getElementById("crumb").textContent = "Takip tablosu";
  app.innerHTML = `<div class="empty">Yükleniyor…</div>`;
  await Promise.all([loadRoster(), loadKeys()]);
  const cell = (s, m) => {
    const x = C.all[s.id] && C.all[s.id][m.id]; if (!x) return `<td>—</td>`;
    const k = C.keys.get(m.id);
    const t = k ? `%${grade(x.answers, k.key).pct}` : "✓";
    return `<td><a href="#/d/${m.id}/u/${s.id}">${t}</a><div class="sub">${fmt(x.updated_at)}</div></td>`;
  };
  app.innerHTML = `<div class="lhead"><h1>Takip tablosu</h1><span class="k">${C.roster.length} öğrenci</span>
      <button class="btn" id="csv">CSV indir</button></div>
    <p class="note">Yüzdeler cevap anahtarına göre otomatik hesaplanır (anahtar öğrencilere kapalıyken de). Bir hücreye tıklayınca öğrencinin cevapları açılır.</p>
    <div class="scroll"><table class="sheet"><tr><th>Öğrenci</th>${MAN.map(m => `<th title="${esc(m.title)}">İB ${m.irab}</th>`).join("")}<th></th></tr>
    ${C.roster.map(s => `<tr><td>${esc(s.name)}<div class="sub">${esc(s.email || "")}</div></td>${MAN.map(m => cell(s, m)).join("")}
      <td><button class="link" data-del="${s.id}">Sil</button></td></tr>`).join("")}</table></div>`;
  document.getElementById("csv").onclick = () => {
    const rows = [["Ad Soyad", "E-posta", ...MAN.map(m => "İB " + m.irab)]].concat(C.roster.map(s => [s.name, s.email || "",
      ...MAN.map(m => { const x = C.all[s.id] && C.all[s.id][m.id], k = C.keys.get(m.id); return !x ? "" : k ? grade(x.answers, k.key).pct : "gönderildi"; })]));
    const csv = rows.map(r => r.map(v => `"${String(v).replace(/"/g, '""')}"`).join(",")).join("\n");
    const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob(["﻿" + csv], { type: "text/csv" })); a.download = "irab-odevleri.csv"; a.click();
  };
  app.querySelectorAll("[data-del]").forEach(b => b.onclick = async () => {
    const s = C.roster.find(x => x.id === b.dataset.del);
    if (!confirm(`${s.name} ve tüm gönderimleri silinsin mi?`)) return;
    const { error } = await C.sb.from("tr_students").delete().eq("id", s.id);
    if (error) alert(error.message); else renderSheet();
  });
}

/* ============================ start ============================ */
(async () => {
  try {
    const r = await fetch("data/manifest.json", { cache: "no-cache" }); const j = await r.json();
    MAN = j.lessons; OPT = j.options;
  } catch (e) { app.innerHTML = `<div class="empty">Ders listesi yüklenemedi.</div>`; return; }
  await initCloud();
  route();
})();
