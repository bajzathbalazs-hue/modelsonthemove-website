window.MOTM_CONFIG = {
  baseUrl: "https://modelsonthemove.hu",
  analytics: {
    ga4MeasurementId: "G-EGGQF205M5",
    googleSearchConsole: "",    /* TODO: Search Console verifikációs kód */
    metaPixelId: "",            /* TODO: Meta Pixel azonosító */
    googleAdsConversionId: ""   /* TODO: Google Ads konverziókövetési azonosító */
  }
};

/* ============ nav scroll state ============ */
const nav = document.getElementById('nav');
if(nav){ window.addEventListener('scroll', ()=> nav.classList.toggle('scrolled', window.scrollY > 40)); }

/* ============ mobile menu ============ */
const burgerBtn = document.getElementById('burgerBtn');
const mobileMenu = document.getElementById('mobileMenu');
const mobileClose = document.getElementById('mobileClose');
function openMenu(){ mobileMenu.style.display='flex'; document.body.style.overflow='hidden'; burgerBtn.classList.add('open'); burgerBtn.setAttribute('aria-expanded','true'); }
function closeMenu(){ mobileMenu.style.display='none'; document.body.style.overflow=''; burgerBtn.classList.remove('open'); burgerBtn.setAttribute('aria-expanded','false'); }
if(burgerBtn){
  burgerBtn.addEventListener('click', ()=> burgerBtn.classList.contains('open') ? closeMenu() : openMenu());
  mobileClose.addEventListener('click', closeMenu);
  document.querySelectorAll('.mlink').forEach(a=>a.addEventListener('click', closeMenu));
  document.addEventListener('keydown', (e)=>{ if(e.key==='Escape' && burgerBtn.classList.contains('open')) closeMenu(); });
}

/* ============ legal modals ============ */
function openLegal(id){
  const el = document.getElementById(id);
  if(!el) return;
  el.classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeLegal(el){
  el.classList.remove('open');
  document.body.style.overflow = '';
}
document.querySelectorAll('[data-open]').forEach(btn=>{
  btn.addEventListener('click', ()=> openLegal(btn.dataset.open));
});
document.querySelectorAll('.legal-overlay').forEach(overlay=>{
  overlay.addEventListener('click', (e)=>{ if(e.target === overlay) closeLegal(overlay); });
  const closeBtn = overlay.querySelector('[data-close]');
  if(closeBtn) closeBtn.addEventListener('click', ()=> closeLegal(overlay));
});
window.addEventListener('keydown', (e)=>{
  if(e.key === 'Escape'){
    document.querySelectorAll('.legal-overlay.open').forEach(o=>closeLegal(o));
  }
});

/* ============ autoplay videók megbízható elindítása (mobilon a natív autoplay
   attribútum gyakran nem elég, kézzel is el kell indítani, ill. amikor a
   képernyőn kívüli videó scrollal bekerül a nézetbe) ============ */
(function(){
  const vids = Array.from(document.querySelectorAll('video[autoplay]'));
  if(!vids.length) return;
  function tryPlay(v){
    v.muted = true;
    v.setAttribute('muted','');
    v.playsInline = true;
    const p = v.play();
    if(p && p.catch) p.catch(()=>{});
  }
  vids.forEach(tryPlay);
  document.addEventListener('DOMContentLoaded', ()=> vids.forEach(tryPlay));
  window.addEventListener('load', ()=> vids.forEach(tryPlay));
  const vio = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{ if(e.isIntersecting) tryPlay(e.target); });
  },{threshold:.1});
  vids.forEach(v=>vio.observe(v));
  document.addEventListener('visibilitychange', ()=>{
    if(!document.hidden) vids.forEach(tryPlay);
  });
  /* automatikus, interakció nélküli ismétlés: ha az első próbálkozások
     elakadnak (pl. a böngésző még nem "melegítette be" az oldalt), ~300ms-
     enként újrapróbáljuk, amíg mindegyik videó el nem indul — így nem kell
     megvárni, amíg a látogató érint/görget valamit */
  let retryCount = 0;
  const retryTimer = setInterval(()=>{
    retryCount++;
    const stillPaused = vids.filter(v=>v.paused);
    if(!stillPaused.length || retryCount>20){ clearInterval(retryTimer); return; }
    stillPaused.forEach(tryPlay);
  }, 300);
  /* végső tartalék: ha a fentiek is mind lepattannak, az első bármilyen
     érintésre/scrollra is újrapróbáljuk — ez már garantáltan túljut a
     policy-blokkon */
  const retryOnInteraction = () => { vids.forEach(tryPlay); };
  ['touchstart','pointerdown','scroll','click','keydown'].forEach(evt=>{
    window.addEventListener(evt, retryOnInteraction, {once:true, passive:true});
  });
})();

/* ============ cookie-consent sáv (GA4) ============ */
(function(){
  const KEY = 'motm-cookie-consent';
  const banner = document.getElementById('cookieBanner');
  if(!banner) return;
  const saved = localStorage.getItem(KEY);
  function grant(){
    if(window.gtag){
      gtag('consent', 'update', { analytics_storage: 'granted' });
    }
  }
  if(saved === 'accepted'){ grant(); }
  else if(saved !== 'declined'){ banner.classList.add('show'); }
  const acceptBtn = document.getElementById('cookieAccept');
  const declineBtn = document.getElementById('cookieDecline');
  if(acceptBtn) acceptBtn.addEventListener('click', ()=>{
    localStorage.setItem(KEY, 'accepted');
    grant();
    banner.classList.remove('show');
  });
  if(declineBtn) declineBtn.addEventListener('click', ()=>{
    localStorage.setItem(KEY, 'declined');
    banner.classList.remove('show');
  });
})();

/* ============ CTA-szint rendszer (1/2/3) — brief "2. A látogatói út és a
   CTA-szintek" szakasza. Minden tárolóhozzáférés try/catch-ben, hogy a
   böngésző storage-tiltása esetén is simán működjön az oldal (ekkor az
   1. szintű alap-CTA marad érvényben). ============ */
(function(){
  function safeGet(storage, key){ try{ return storage.getItem(key); }catch(e){ return null; } }
  function safeSet(storage, key, val){ try{ storage.setItem(key, val); }catch(e){} }
  function hasConsent(){ return safeGet(localStorage, 'motm-cookie-consent') === 'accepted'; }
  function gaEvent(name, params){ if(window.gtag) gtag('event', name, params||{}); }

  let pageCount = parseInt(safeGet(sessionStorage,'motm_pagecount') || '0', 10) + 1;
  safeSet(sessionStorage, 'motm_pagecount', String(pageCount));

  let sessionStart = safeGet(sessionStorage, 'motm_session_start');
  if(!sessionStart){ sessionStart = String(Date.now()); safeSet(sessionStorage, 'motm_session_start', sessionStart); }
  function timeOnSiteSec(){ return Math.round((Date.now() - parseInt(sessionStart,10)) / 1000); }

  let visited = [];
  try{ visited = JSON.parse(safeGet(sessionStorage, 'motm_visited') || '[]'); }catch(e){}
  if(visited.indexOf(location.pathname) === -1){
    visited.push(location.pathname);
    safeSet(sessionStorage, 'motm_visited', JSON.stringify(visited));
  }
  const visitedRolunkOrKorabbi = visited.some(p => p.indexOf('/rolunk/') !== -1 || p.indexOf('/korabbi-esemenyek/') !== -1);

  // 66%-os görgetési mélység — csak a 4 nagy szolgáltatás-oldalon számít
  let deepScroll = safeGet(sessionStorage, 'motm_deepscroll') === '1';
  if(document.body.hasAttribute('data-service-page') && !deepScroll){
    window.addEventListener('scroll', function onScroll(){
      const doc = document.documentElement;
      const pct = (window.scrollY + window.innerHeight) / doc.scrollHeight;
      if(pct >= 0.66){
        deepScroll = true;
        safeSet(sessionStorage, 'motm_deepscroll', '1');
        window.removeEventListener('scroll', onScroll);
      }
    }, {passive:true});
  }

  // 7 napon belüli visszatérés — csak süti-hozzájárulás után (localStorage)
  let returning7d = false;
  if(hasConsent()){
    const lastVisit = safeGet(localStorage, 'motm_last_visit');
    if(lastVisit && (Date.now() - parseInt(lastVisit,10)) < 7*24*60*60*1000){ returning7d = true; }
    safeSet(localStorage, 'motm_last_visit', String(Date.now()));
  }

  function computeTier(){
    const tier3Signals = [pageCount >= 4, timeOnSiteSec() > 120, visitedRolunkOrKorabbi, returning7d].filter(Boolean).length;
    if(tier3Signals >= 2) return 3;
    if(deepScroll || pageCount >= 3) return 2;
    return 1;
  }

  function applyTier(tier){
    document.querySelectorAll('[data-tier-cta]').forEach(function(el){
      try{
        const variants = JSON.parse(el.dataset.tierCta);
        const v = variants[tier] || variants['1'];
        if(v){ el.textContent = v.label; el.setAttribute('href', v.href); }
      }catch(e){}
    });
    gaEvent('cta_tier_active', {tier: tier});
    if(tier === 3) showTier3Bar();
  }

  function showTier3Bar(){
    if(document.getElementById('tier3Bar')) return;
    if(safeGet(sessionStorage, 'motm_tier3_dismissed') === '1') return;
    const bar = document.createElement('div');
    bar.id = 'tier3Bar';
    bar.className = 'tier3-bar';
    bar.innerHTML = '<p>Látjuk, hogy komolyan gondolod. Három perc, és személyre szabott javaslatot kapsz.</p>'
      + '<div class="tier3-bar-ctas"><a href="/projekt-inditasa/" class="btn filled magnetic">INDÍTSUK EL A PROJEKTED</a>'
      + '<button type="button" class="tier3-bar-close" aria-label="Bezárás">&times;</button></div>';
    document.body.appendChild(bar);
    requestAnimationFrame(function(){ bar.classList.add('show'); });
    bar.querySelector('.tier3-bar-close').addEventListener('click', function(){
      bar.classList.remove('show');
      safeSet(sessionStorage, 'motm_tier3_dismissed', '1');
      setTimeout(function(){ bar.remove(); }, 400);
    });
    gaEvent('cta_tier3_bar_shown', {});
  }

  applyTier(computeTier());
})();

/* ============ scroll reveal ============ */
const io = new IntersectionObserver((entries)=>{
  entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
},{threshold:.15});
document.querySelectorAll('.rv, .rv-stagger').forEach(el=>io.observe(el));

/* ============ magnetic buttons (desktop only) ============ */
if(window.matchMedia('(hover:hover) and (pointer:fine)').matches){
  document.querySelectorAll('.magnetic').forEach(btn=>{
    btn.addEventListener('mousemove', (e)=>{
      const r = btn.getBoundingClientRect();
      const x = (e.clientX - r.left - r.width/2) * .2;
      const y = (e.clientY - r.top - r.height/2) * .3;
      btn.style.transform = `translate(${x}px, ${y}px)`;
    });
    btn.addEventListener('mouseleave', ()=> btn.style.transform = '');
  });
}

/* ============ chip multi-select / single-select (any .chips container) ============
   .chips = szabad többszörös választás. .chips.chips-single = csak egy chip
   lehet aktív (a meglévő kijelölés törlődik, mielőtt az újat bejelölnénk) —
   így radio-gomb-szerű viselkedés, a meglévő chip-vizuál megtartásával. */
document.querySelectorAll('.chips .chip-opt').forEach(c=>{
  c.setAttribute('role','checkbox'); c.setAttribute('aria-checked','false'); c.setAttribute('tabindex','0');
  function toggle(){
    const group = c.closest('.chips');
    const single = group && group.classList.contains('chips-single');
    if(single && !c.classList.contains('on')){
      group.querySelectorAll('.chip-opt.on').forEach(o=>{ o.classList.remove('on'); o.setAttribute('aria-checked','false'); });
    }
    const on = c.classList.toggle('on');
    c.setAttribute('aria-checked', on?'true':'false');
  }
  c.addEventListener('click', toggle);
  c.addEventListener('keydown', (e)=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); toggle(); } });
});

/* ============ kapcsolat-űrlap: a hivatkozó oldal (document.referrer) alapján
   automatikusan bejelöli a megfelelő "miben segíthetünk" chipet, ha a
   látogató egy konkrét szolgáltatás-oldalról érkezett ============ */
(function(){
  const bizChips = document.getElementById('bizChips');
  if(!bizChips || !document.referrer) return;
  const slugToChip = {
    'modellugynokseg': 'modell',
    'influencer-marketing': 'influencer',
    'marketing-ugynokseg': 'teljes-marketing',
    'rendezvenyszervezes': 'rendezveny',
    'reklamfilm-keszites': 'foto-video',
    'weboldal-keszites': 'weboldal',
    'kozossegi-media-kezeles': 'social'
  };
  const match = Object.keys(slugToChip).find(slug => document.referrer.indexOf('/'+slug+'/') !== -1);
  if(!match) return;
  const chip = bizChips.querySelector('.chip-opt[data-value="'+slugToChip[match]+'"]');
  if(chip && !chip.classList.contains('on')){ chip.click(); }
})();

/* ============ FAQ accordion ============ */
document.querySelectorAll('.faq-item').forEach(item=>{
  const q = item.querySelector('.faq-q');
  q.addEventListener('click', ()=>{
    const open = item.getAttribute('aria-expanded') === 'true';
    item.closest('.faq-list').querySelectorAll('.faq-item').forEach(i=>i.setAttribute('aria-expanded','false'));
    item.setAttribute('aria-expanded', open ? 'false' : 'true');
  });
});

/* ============ generic form handling (honeypot + validation + Netlify Forms beküldés) ============ */
/* Az űrlapok a Netlify Forms szolgáltatását használják (nincs külön szerver/endpoint
   szükséges) — a <form> elemeken a data-netlify="true" + name attribútum és a rejtett
   form-name mező teszi lehetővé, hogy a Netlify build-bot regisztrálja és a beállított
   e-mail-értesítésen (Netlify admin → Forms) keresztül kézbesítse a beküldéseket.
   Form detection a Netlify admin felületén manuálisan bekapcsolva — ez a build
   az első, ami már detektált állapotban fut, hogy a bot ténylegesen regisztrálja
   a két űrlapot (kapcsolat, modell-jelentkezes). */
function motmEncode(data){
  return Object.keys(data).map(k => encodeURIComponent(k) + '=' + encodeURIComponent(data[k])).join('&');
}
function motmHandleForm(form, opts){
  opts = opts || {};
  form.addEventListener('submit', async (e)=>{
    e.preventDefault();
    const hp = form.querySelector('.hp-field input');
    if(hp && hp.value){ return; } /* honeypot triggered — silently drop */

    let valid = true;
    form.querySelectorAll('[required]').forEach(el=>{
      const field = el.closest('.field') || el.closest('.check');
      const empty = el.type === 'checkbox' ? !el.checked : !el.value.trim();
      if(field){ field.classList.toggle('error', empty); }
      if(empty) valid = false;
    });
    if(!valid){
      const firstError = form.querySelector('.field.error, .check.error');
      if(firstError) firstError.scrollIntoView({behavior:'smooth', block:'center'});
      return;
    }

    const btn = form.querySelector('button[type=submit]');
    const msg = document.getElementById(opts.msgId);
    const servicesField = form.querySelector('[name="services"]');
    if(servicesField){
      const chips = form.querySelectorAll('.chips .chip-opt.on');
      servicesField.value = Array.from(chips).map(c=>c.textContent.trim()).join(', ');
    }
    const pageUrlField = form.querySelector('[name="page_url"]');
    if(pageUrlField) pageUrlField.value = location.href;
    const referrerField = form.querySelector('[name="referrer_url"]');
    if(referrerField) referrerField.value = document.referrer || 'Közvetlen látogatás / nincs hivatkozó oldal';
    const data = Object.fromEntries(new FormData(form).entries());

    if(btn){ btn.disabled = true; btn.textContent = 'KÜLDÉS...'; }
    try{
      const res = await fetch('/', {
        method: 'POST',
        headers: {'Content-Type':'application/x-www-form-urlencoded'},
        body: motmEncode(data)
      });
      if(!res.ok) throw new Error('bad status');
      form.style.display = 'none';
      if(msg){ msg.classList.add('show'); }
      if(window.gtag && opts.eventName){ window.gtag('event', opts.eventName); }
    }catch(err){
      if(btn){ btn.disabled = false; btn.textContent = opts.submitLabel || 'ÚJRA PRÓBÁLOM'; }
      if(msg){
        msg.classList.add('show','notice');
        msg.querySelector('h4').textContent = 'Hiba történt a küldés közben.';
        msg.querySelector('h4').classList.add('err');
        msg.querySelector('p').textContent = 'Kérjük, próbáld újra, vagy hívj minket: +36 30 940 4148.';
      }
    }
  });
}
document.querySelectorAll('form[data-motm-form]').forEach(form=>{
  motmHandleForm(form, {
    msgId: form.dataset.msgId,
    eventName: form.dataset.event,
    pendingTitle: form.dataset.pendingTitle,
    pendingText: form.dataset.pendingText
  });
});
