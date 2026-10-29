# -*- coding: utf-8 -*-
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.dirname(HERE)

BASE_URL = "https://modelsonthemove.hu"
# Saját domain aktív (GitHub Pages CNAME + DNS A/CNAME rekordok). Ha vissza kellene
# állni a github.io címre, ezt az egy konstanst kell visszaírni — minden
# canonical/OG/sitemap URL innen származik.

SITE_NAME = "Models on the Move"

GA4_MEASUREMENT_ID = "G-EGGQF205M5"

# Consent Mode v2: alapból minden tárolás elutasítva, amíg a látogató el nem
# fogadja a cookie-sávon (lásd COOKIE_BANNER a SCRIPT-ben) — így a gtag.js
# betöltődik és a GA4 property adatokat lát, de személyes/cookie-alapú
# méréshez a beleegyezés megadásáig nem jut hozzá.
GA4_SNIPPET = f"""<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{ dataLayer.push(arguments); }}
gtag('consent', 'default', {{
  'analytics_storage': 'denied',
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied'
}});
gtag('js', new Date());
gtag('config', '{GA4_MEASUREMENT_ID}', {{ 'anonymize_ip': true }});
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_MEASUREMENT_ID}"></script>"""

# Jegyértékesítés: Cooltix (korábban SevenRooms). A widget.js figyeli a
# [data-cooltix-event-products] gombokat és rákattintva nyitja meg a
# jegy-/asztalvásárló felületet — nincs hozzá közvetlen URL.
COOLTIX_EVENT_PRODUCT_ID = "6abfc851b1af33780adbc91b"
COOLTIX_WIDGET_SCRIPT = '<script src="https://static.cooltix.com/widget.js" defer></script>'
COOLTIX_WIDGET_URL = f"https://cooltix.com/widget/event-products/{COOLTIX_EVENT_PRODUCT_ID}"

with open(os.path.join(HERE, "shared_style.css"), encoding="utf-8") as f:
    SHARED_STYLE = f.read()
with open(os.path.join(HERE, "ext_style.css"), encoding="utf-8") as f:
    EXT_STYLE = f.read()
with open(os.path.join(HERE, "legal_modals.html"), encoding="utf-8") as f:
    LEGAL_MODALS = f.read()

FULL_STYLE = SHARED_STYLE + "\n" + EXT_STYLE

# Fő navigáció — a "Models on the Move – weboldal-brief és szövegek (1. változat)"
# 10-oldalas sitemapja szerint (2026.10.29). A "Korábbi események" nem önálló
# nav-elem, hanem az Események oldalról érhető el (hogy a fejléc ne legyen
# túlzsúfolt) — lásd content_events.py.
MAIN_NAV = [
    ("esemenyek", "events", "Események"),
    ("arculat-es-webfejlesztes", "arculat", "Arculat és webfejlesztés"),
    ("marketing-es-ai", "marketing", "Marketing és AI"),
    ("influencer-egyuttmukodes", "influencer", "Influencer-együttműködés"),
    ("tartalomgyartas", "tartalom", "Tartalomgyártás"),
    ("rolunk", "about", "Rólunk"),
    ("kapcsolat", "contact", "Kapcsolat"),
]


def head(title, description, canonical_path, depth=0, og_image="assets/hero-myrazs-poster.jpg", robots="index,follow", extra_jsonld=""):
    """canonical_path: '' for home, or 'modellugynokseg/' etc (trailing slash, no leading slash)."""
    canonical = BASE_URL + "/" + canonical_path
    r = _root(depth)
    org_jsonld = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Models on the Move",
  "url": "%s/",
  "logo": "%s/assets/motm_logo_dark.png",
  "description": "Modellek és influencerek, marketing és márképítés, események és produkciók — egy összehangolt budapesti csapattól.",
  "areaServed": "HU",
  "telephone": "+36309404148"
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Models on the Move",
  "image": "%s/assets/motm_logo_dark.png",
  "url": "%s/",
  "telephone": "+36309404148",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Kléh István utca 3.",
    "addressLocality": "Budapest",
    "postalCode": "1126",
    "addressCountry": "HU"
  },
  "areaServed": "Magyarország"
}
</script>""" % (BASE_URL, BASE_URL, BASE_URL, BASE_URL)

    return f"""<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Models on the Move">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE_URL}/{og_image}">
<meta property="og:locale" content="hu_HU">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{BASE_URL}/{og_image}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Yellowtail&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="preconnect" href="https://api.fontshare.com">
<link href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@400,500,700,800,900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/site.css">
{org_jsonld}
{extra_jsonld}
{GA4_SNIPPET}
{COOLTIX_WIDGET_SCRIPT}
</head>
"""


def _root(depth):
    """depth=0 -> '', depth=1 -> '../' (used for asset/link paths from subpages)."""
    return "../" * depth


def nav(depth=0, active=""):
    r = _root(depth)
    def cls(key):
        return ' style="color:var(--bronze-bright);"' if active == key else ""
    main_links = "\n    ".join(
        f'<a href="{r}{slug}/"{cls(key)}>{label.upper()}</a>' for slug, key, label in MAIN_NAV
    )
    m_main_links = "\n    ".join(
        f'<a href="{r}{slug}/" class="mlink">{label}</a>' for slug, key, label in MAIN_NAV
    )
    return f"""
<a href="#main" class="skip-link">Ugrás a tartalomhoz</a>
<nav id="nav">
  <a href="{r}index.html" aria-label="Models on the Move — kezdőlap"><img class="wordmark-img" src="{r}assets/motm_logo_dark.png" alt="Models on the Move"></a>
  <div class="nav-links">
    {main_links}
  </div>
  <div class="nav-right">
    <a href="{r}projekt-inditasa/" class="btn filled">PROJEKT INDÍTÁSA</a>
  </div>
  <button class="burger" id="burgerBtn" aria-label="Menü" aria-expanded="false" aria-controls="mobileMenu"><span></span><span></span><span></span></button>
</nav>

<div class="mobile-menu" id="mobileMenu">
  <button class="mobile-close" id="mobileClose">BEZÁR ✕</button>
  <div class="mmenu-body">
    {m_main_links}
    <a href="{r}projekt-inditasa/" class="btn filled mlink" style="margin-top:8px;">PROJEKT INDÍTÁSA</a>
  </div>
</div>
"""


def breadcrumb(items, depth=1):
    """items: list of (label, path or None for current)."""
    r = _root(depth)
    parts = [f'<a href="{r}index.html">Főoldal</a>']
    for label, path in items:
        parts.append('<span class="sep">/</span>')
        if path:
            parts.append(f'<a href="{r}{path}">{label}</a>')
        else:
            parts.append(f'<span class="cur" aria-current="page">{label}</span>')
    inner = " ".join(parts)
    return f'<div class="wrap"><nav class="breadcrumb" aria-label="Morzsamenü">{inner}</nav></div>'


def footer(depth=0):
    r = _root(depth)
    nav_links = "\n        ".join(f'<a href="{r}{slug}/">{label}</a>' for slug, _key, label in MAIN_NAV)
    return f"""
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img class="wordmark-img lg" src="{r}assets/motm_logo_dark.png" alt="Models on the Move">
        <p style="margin-top:10px;font-size:13px;color:var(--ivory-dim);font-weight:600;">Események. Arculat és weboldal. Marketing. Influencerek.</p>
        <p style="margin-top:12px;font-size:12.5px;color:var(--ivory-dimmer);max-width:260px;line-height:1.7;">Élményt és láthatóságot teremtünk. Budapest.</p>
      </div>
      <div>
        <h5>OLDALAK</h5>
        {nav_links}
      </div>
      <div>
        <h5>MODELS ON THE MOVE</h5>
        <a href="{r}projekt-inditasa/">Projekt indítása</a>
        <a href="{r}rolunk/">Rólunk</a>
        <a href="{r}kapcsolat/">Kapcsolat</a>
      </div>
      <div>
        <h5>KÖVESS</h5>
        <a href="https://www.instagram.com/models_on_the_move/" target="_blank" rel="noopener">Instagram</a>
        <a href="https://www.facebook.com/profile.php?id=61586682312593" target="_blank" rel="noopener">Facebook</a>
        <a href="https://www.tiktok.com/@models.on.the.move" target="_blank" rel="noopener">TikTok</a>
      </div>
    </div>
    <div class="foot-bottom">
      <div>© 2026 MODELS ON THE MOVE</div>
      <div class="foot-legal">
        <button type="button" class="legal-link" data-open="modal-impressum">IMPRESSZUM</button>
        <button type="button" class="legal-link" data-open="modal-privacy">ADATKEZELÉS</button>
        <button type="button" class="legal-link" data-open="modal-terms">ÁSZF</button>
      </div>
    </div>
  </div>
</footer>

{LEGAL_MODALS}
"""


SCRIPT = """
<script>
window.MOTM_CONFIG = {
  baseUrl: "%BASE_URL%",
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
</script>
""".replace("%BASE_URL%", BASE_URL)


def faq_list(items):
    rows = []
    for q, a in items:
        rows.append(f"""      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">{q}<span class="plus"></span></button>
        <div class="faq-a"><p>{a}</p></div>
      </div>""")
    faqld_items = ",\n".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}' % (
            _jsonstr(q), _jsonstr(a)
        ) for q, a in items
    )
    faqld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' +
             faqld_items + ']}</script>')
    return ('<div class="faq-list">\n' + "\n".join(rows) + "\n    </div>", faqld)


def _jsonstr(s):
    import json as _json
    return _json.dumps(s)


MODEL_APPLICATION_FORM = """
<section class="pad rule" id="jelentkezes">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MODELLNEK JELENTKEZEM</span><h2>Mutatkozz be röviden.</h2>
      <p>Nem kell hivatásos portfólió — pár jó minőségű kép és néhány mondat rólad elég az első lépéshez.</p>
    </div>
    <div class="wrap rv" style="padding:0;max-width:640px;">
      <form class="form-panel" name="modell-jelentkezes" data-netlify="true" data-netlify-honeypot="company_website" data-motm-form data-msg-id="modelMsg" data-event="model_application_submit" novalidate>
        <input type="hidden" name="form-name" value="modell-jelentkezes">
        <input type="hidden" name="page_url" value="">
        <input type="hidden" name="referrer_url" value="">
        <div class="hp-field" aria-hidden="true"><label>Cégnév (ne töltsd ki)</label><input type="text" name="company_website" tabindex="-1" autocomplete="off"></div>
        <div class="row2">
          <div class="field"><label for="ma-name">TELJES NÉV</label><input id="ma-name" name="name" type="text" required></div>
          <div class="field"><label for="ma-birth">SZÜLETÉSI ÉV</label><input id="ma-birth" name="birthYear" type="number" min="1950" max="2015" required></div>
        </div>
        <div class="row2">
          <div class="field"><label for="ma-email">E-MAIL</label><input id="ma-email" name="email" type="email" required></div>
          <div class="field"><label for="ma-phone">TELEFONSZÁM</label><input id="ma-phone" name="phone" type="tel" required></div>
        </div>
        <div class="row2">
          <div class="field"><label for="ma-city">VÁROS</label><input id="ma-city" name="city" type="text" required></div>
          <div class="field"><label for="ma-ig">INSTAGRAM VAGY PORTFÓLIÓ URL</label><input id="ma-ig" name="portfolio" type="text" required></div>
        </div>
        <div class="field"><label for="ma-bio">RÖVID BEMUTATKOZÁS</label><textarea id="ma-bio" name="bio" required></textarea></div>
        <label class="check"><input type="checkbox" name="consent" required> Elfogadom az Adatvédelmi tájékoztatót. A jelentkezés nem jelent automatikus együttműködést.</label>
        <div class="submit-row">
          <button type="submit" class="btn filled magnetic">JELENTKEZEM</button>
        </div>
        <div class="form-msg" id="modelMsg"><h4>JELENTKEZÉSED MEGÉRKEZETT.</h4><p>Köszönjük. Amennyiben illesz egy aktuális projekthez, felvesszük veled a kapcsolatot.</p></div>
      </form>
    </div>
  </div>
</section>
"""


COOKIE_BANNER = """
<div class="cookie-banner" id="cookieBanner" role="dialog" aria-live="polite" aria-label="Süti-tájékoztató">
  <p>Az oldal látogatottsági statisztikákhoz sütiket használ (Google Analytics). Elfogadod?</p>
  <div class="cookie-actions">
    <button type="button" class="btn" id="cookieDecline">Elutasítom</button>
    <button type="button" class="btn filled" id="cookieAccept">Elfogadom</button>
  </div>
</div>
"""


def page(title, description, canonical_path, body, depth=None, active="", og_image="assets/hero-myrazs-poster.jpg", robots="index,follow", extra_jsonld=""):
    if depth is None:
        depth = 0 if canonical_path == "" else canonical_path.count("/")
    r = _root(depth)
    # data-service-page: a CTA-szint rendszer (ld. SCRIPT) ezen a 4 "mélyebb"
    # szolgáltatás-oldalon figyeli a 66%-os görgetési mélységet (brief 2. szakasz).
    is_service_page = active in ("arculat", "marketing", "influencer", "tartalom")
    body_attrs = f' data-depth="{depth}"' + (' data-service-page="1"' if is_service_page else "")
    return (
        head(title, description, canonical_path, depth=depth, og_image=og_image, robots=robots, extra_jsonld=extra_jsonld)
        + f"<body{body_attrs}>\n"
        + COOKIE_BANNER
        + nav(depth=depth, active=active)
        + '\n<main id="main">\n'
        + body
        + "\n</main>\n"
        + footer(depth=depth)
        + f'\n<script src="{r}assets/site.js"></script>\n'
        + "\n</body>\n</html>\n"
    )
