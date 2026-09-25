# -*- coding: utf-8 -*-
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.dirname(HERE)

BASE_URL = "https://modelsonthemove.hu"
# Saját domain aktív (GitHub Pages CNAME + DNS A/CNAME rekordok). Ha vissza kellene
# állni a github.io címre, ezt az egy konstanst kell visszaírni — minden
# canonical/OG/sitemap URL innen származik.

SITE_NAME = "Models on the Move"

with open(os.path.join(HERE, "shared_style.css"), encoding="utf-8") as f:
    SHARED_STYLE = f.read()
with open(os.path.join(HERE, "ext_style.css"), encoding="utf-8") as f:
    EXT_STYLE = f.read()
with open(os.path.join(HERE, "legal_modals.html"), encoding="utf-8") as f:
    LEGAL_MODALS = f.read()

FULL_STYLE = SHARED_STYLE + "\n" + EXT_STYLE

SERVICES_NAV = [
    ("modellugynokseg", "Modellek és casting"),
    ("influencer-marketing", "Influencer marketing"),
    ("marketing-ugynokseg", "Teljes körű marketing"),
    ("rendezvenyszervezes", "Rendezvényszervezés"),
    ("reklamfilm-keszites", "Reklámfilm és videó"),
    ("weboldal-keszites", "Weboldalkészítés"),
    ("kozossegi-media-kezeles", "Közösségi média"),
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
  "email": "hello@modelsonthemove.hu",
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
  "email": "hello@modelsonthemove.hu",
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
</head>
"""


def _root(depth):
    """depth=0 -> '', depth=1 -> '../' (used for asset/link paths from subpages)."""
    return "../" * depth


def nav(depth=0, active=""):
    r = _root(depth)
    subitems = "\n".join(
        f'      <a href="{r}{slug}/"><small>Szolgáltatás</small>{label}</a>'
        for slug, label in SERVICES_NAV
    )
    def cls(key):
        return ' style="color:var(--bronze-bright);"' if active == key else ""
    return f"""
<a href="#main" class="skip-link">Ugrás a tartalomhoz</a>
<nav id="nav">
  <a href="{r}index.html" aria-label="Models on the Move — kezdőlap"><img class="wordmark-img" src="{r}assets/motm_logo_dark.png" alt="Models on the Move"></a>
  <div class="nav-links">
    <div class="has-sub" id="navSubWrap">
      <button class="sub-toggle" id="navSubBtn" aria-expanded="false" aria-controls="navSubmenu">SZOLGÁLTATÁSOK<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></button>
      <div class="submenu" id="navSubmenu" role="menu">
{subitems}
      </div>
    </div>
    <a href="{r}esemenyek/"{cls('events')}>ESEMÉNYEK</a>
    <a href="{r}munkaink/"{cls('works')}>MUNKÁINK</a>
    <a href="{r}rolunk/"{cls('about')}>RÓLUNK</a>
    <a href="{r}kapcsolat/"{cls('contact')}>KAPCSOLAT</a>
  </div>
  <div class="nav-right">
    <a href="{r}kapcsolat/" class="btn filled">BESZÉLJÜNK A CÉGEDRŐL</a>
  </div>
  <button class="burger" id="burgerBtn" aria-label="Menü" aria-expanded="false" aria-controls="mobileMenu"><span></span><span></span><span></span></button>
</nav>

<div class="mobile-menu" id="mobileMenu">
  <button class="mobile-close" id="mobileClose">BEZÁR ✕</button>
  <div class="mmenu-body">
    <button class="msub-toggle mlink" id="mSubBtn" aria-expanded="false" aria-controls="mSubPanel">SZOLGÁLTATÁSOK <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></button>
    <div class="msub-panel" id="mSubPanel">
{chr(10).join(f'      <a href="{r}{slug}/" class="mlink">{label}</a>' for slug, label in SERVICES_NAV)}
    </div>
    <div class="mmenu-rule" aria-hidden="true"></div>
    <a href="{r}esemenyek/" class="mlink">ESEMÉNYEK</a>
    <a href="{r}munkaink/" class="mlink">MUNKÁINK</a>
    <a href="{r}rolunk/" class="mlink">RÓLUNK</a>
    <a href="{r}kapcsolat/" class="mlink">KAPCSOLAT</a>
    <a href="{r}kapcsolat/" class="btn filled mlink" style="margin-top:8px;">BESZÉLJÜNK A CÉGEDRŐL</a>
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
    svc_links = "\n        ".join(f'<a href="{r}{slug}/">{label}</a>' for slug, label in SERVICES_NAV)
    return f"""
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img class="wordmark-img lg" src="{r}assets/motm_logo_dark.png" alt="Models on the Move">
        <p style="margin-top:10px;font-size:13px;color:var(--ivory-dim);font-weight:600;">Modellek. Influencerek. Marketing. Események.</p>
        <p style="margin-top:12px;font-size:12.5px;color:var(--ivory-dimmer);max-width:260px;line-height:1.7;">Embereket, márkákat és élményeket kapcsolunk össze. Budapest.</p>
      </div>
      <div>
        <h5>SZOLGÁLTATÁSOK</h5>
        {svc_links}
      </div>
      <div>
        <h5>MODELS ON THE MOVE</h5>
        <a href="{r}esemenyek/">Események</a>
        <a href="{r}munkaink/">Munkáink</a>
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
  /* TODO: állítsd be az éles form-beküldési endpointot (pl. egy saját szerverless függvény
     vagy egy form-kezelő szolgáltatás URL-je). Amíg üres marad, az űrlapok NEM állítják,
     hogy sikeresen elküldték az adatot — helyette egy tájékoztató üzenetet mutatnak. */
  formEndpoint: "",
  analytics: {
    ga4MeasurementId: "",       /* TODO: Google Analytics 4 mérési azonosító */
    googleSearchConsole: "",    /* TODO: Search Console verifikációs kód */
    metaPixelId: "",            /* TODO: Meta Pixel azonosító */
    googleAdsConversionId: ""   /* TODO: Google Ads konverziókövetési azonosító */
  }
};

/* ============ nav scroll state ============ */
const nav = document.getElementById('nav');
if(nav){ window.addEventListener('scroll', ()=> nav.classList.toggle('scrolled', window.scrollY > 40)); }

/* ============ desktop services dropdown (click + keyboard, not hover-only) ============ */
(function(){
  const wrap = document.getElementById('navSubWrap');
  const btn = document.getElementById('navSubBtn');
  if(!wrap || !btn) return;
  function close(){ wrap.setAttribute('aria-expanded','false'); btn.setAttribute('aria-expanded','false'); }
  function open(){ wrap.setAttribute('aria-expanded','true'); btn.setAttribute('aria-expanded','true'); }
  btn.addEventListener('click', (e)=>{ e.stopPropagation(); btn.getAttribute('aria-expanded')==='true' ? close() : open(); });
  document.addEventListener('click', (e)=>{ if(!wrap.contains(e.target)) close(); });
  document.addEventListener('keydown', (e)=>{ if(e.key==='Escape') close(); });
})();

/* ============ mobile menu ============ */
const burgerBtn = document.getElementById('burgerBtn');
const mobileMenu = document.getElementById('mobileMenu');
const mobileClose = document.getElementById('mobileClose');
function openMenu(){ mobileMenu.style.display='flex'; document.body.style.overflow='hidden'; burgerBtn.classList.add('open'); burgerBtn.setAttribute('aria-expanded','true'); }
function closeMenu(){ mobileMenu.style.display='none'; document.body.style.overflow=''; burgerBtn.classList.remove('open'); burgerBtn.setAttribute('aria-expanded','false'); }
if(burgerBtn){
  burgerBtn.addEventListener('click', ()=> burgerBtn.classList.contains('open') ? closeMenu() : openMenu());
  mobileClose.addEventListener('click', closeMenu);
  document.querySelectorAll('.mlink').forEach(a=>a.addEventListener('click', (e)=>{ if(!a.classList.contains('msub-toggle')) closeMenu(); }));
  document.addEventListener('keydown', (e)=>{ if(e.key==='Escape' && burgerBtn.classList.contains('open')) closeMenu(); });
}
const mSubBtn = document.getElementById('mSubBtn');
const mSubPanel = document.getElementById('mSubPanel');
if(mSubBtn){
  mSubBtn.addEventListener('click', ()=>{
    const open = mSubPanel.classList.toggle('open');
    mSubBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
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

/* ============ chip multi-select (any .chips container) ============ */
document.querySelectorAll('.chips .chip-opt').forEach(c=>{
  c.setAttribute('role','checkbox'); c.setAttribute('aria-checked','false'); c.setAttribute('tabindex','0');
  function toggle(){ const on = c.classList.toggle('on'); c.setAttribute('aria-checked', on?'true':'false'); }
  c.addEventListener('click', toggle);
  c.addEventListener('keydown', (e)=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); toggle(); } });
});

/* ============ FAQ accordion ============ */
document.querySelectorAll('.faq-item').forEach(item=>{
  const q = item.querySelector('.faq-q');
  q.addEventListener('click', ()=>{
    const open = item.getAttribute('aria-expanded') === 'true';
    item.closest('.faq-list').querySelectorAll('.faq-item').forEach(i=>i.setAttribute('aria-expanded','false'));
    item.setAttribute('aria-expanded', open ? 'false' : 'true');
  });
});

/* ============ generic form handling (honeypot + validation + configurable endpoint) ============ */
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
    const endpoint = window.MOTM_CONFIG && window.MOTM_CONFIG.formEndpoint;

    if(!endpoint){
      if(msg){
        msg.classList.add('show','notice');
        msg.querySelector('h4').textContent = opts.pendingTitle || 'Az űrlap-beküldés jelenleg beállítás alatt áll.';
        msg.querySelector('p').textContent = opts.pendingText || 'Kérjük, addig írj közvetlenül a hello@modelsonthemove.hu címre, vagy hívj minket — a fenti adatok elküldve NEM kerültek rögzítésre.';
        msg.querySelector('h4').classList.add('err');
      }
      return;
    }

    if(btn){ btn.disabled = true; btn.textContent = 'KÜLDÉS...'; }
    try{
      const data = Object.fromEntries(new FormData(form).entries());
      const res = await fetch(endpoint, {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(data)
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
        msg.querySelector('p').textContent = 'Kérjük, próbáld újra, vagy írj a hello@modelsonthemove.hu címre.';
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


def service_page(d):
    """d: dict with keys slug, nav_label, seo_title, meta_desc, h1, position, lead,
    sections (list of (h2,[paragraphs])), related (list of slugs), faq (list of (q,a)),
    dual_path (bool, optional)."""
    faq_html, faqld = faq_list(d["faq"])

    feature_rows = []
    for i, (h3, paras) in enumerate(d["sections"], start=1):
        p_html = "\n".join(f"<p>{p}</p>" for p in paras)
        feature_rows.append(f"""      <div class="feature">
        <div class="num">{i:02d}</div>
        <div><h3>{h3}</h3>{p_html}</div>
      </div>""")
    features_html = '<div class="feature-list rv-stagger">\n' + "\n".join(feature_rows) + "\n    </div>"

    related_html = ""
    if d.get("related"):
        cards = []
        for slug in d["related"]:
            label = dict(SERVICES_NAV).get(slug, slug)
            cards.append(f'<a href="../{slug}/" class="related-card glow-card"><span class="k">Kapcsolódó szolgáltatás</span><h4>{label}</h4></a>')
        related_html = f"""
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KAPCSOLÓDÓ SZOLGÁLTATÁSOK</span></div>
    <div class="related-grid rv-stagger">{"".join(cards)}</div>
  </div>
</section>"""

    dual_path_html = ""
    if d.get("dual_path"):
        dual_path_html = f"""
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KÉT ÚT</span><h2>Márkaként keresel modellt,<br>vagy modellként jelentkeznél?</h2></div>
    <div class="dualpath rv">
      <div class="path-card">
        <div class="k">Márkáknak és ügynökségeknek</div>
        <h3>Modellt keresek</h3>
        <p>Kampányhoz, fotózáshoz, forgatáshoz vagy eseményhez keresel modellt, hostesst vagy reklámarcot? Küldd el a projekt részleteit, és 1-2 munkanapon belül jelentkezünk.</p>
        <a href="../kapcsolat/" class="btn filled magnetic">MODELLT KERESEK</a>
      </div>
      <div class="path-card">
        <div class="k">Modelleknek és influencereknek</div>
        <h3>Modellnek jelentkezem</h3>
        <p>Modellként, hostessként vagy influencerként csatlakoznál a Models on the Move hálózatához? Töltsd ki a jelentkezési űrlapot alább.</p>
        <a href="#jelentkezes" class="btn magnetic">MODELLNEK JELENTKEZEM</a>
      </div>
    </div>
  </div>
</section>
{MODEL_APPLICATION_FORM}"""

    body = f"""
{breadcrumb([(d['nav_label'], None)], depth=1)}
<section class="subhero">
  <div class="wrap">
    <span class="eyebrow rv">SZOLGÁLTATÁS</span>
    <h1 class="rv">{d['h1']}</h1>
    <p class="position rv">{d['position']}</p>
    <p class="lead rv">{d['lead']}</p>
    <div class="ctas rv">
      <a href="../kapcsolat/" class="btn filled magnetic">{d.get('cta_text','BESZÉLJÜNK A PROJEKTRŐL')}</a>
    </div>
  </div>
</section>
{dual_path_html}
<section class="pad rule">
  <div class="wrap">
    {features_html}
  </div>
</section>
{related_html}
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">GYAKORI KÉRDÉSEK</span></div>
    <div class="rv">{faq_html}</div>
  </div>
</section>
<section class="cta-band rule">
  <div class="wrap rv">
    <h2>{d.get('closing', 'Beszéljünk a projektről.')}</h2>
    <div class="ctas"><a href="../kapcsolat/" class="btn filled magnetic">{d.get('cta_text','BESZÉLJÜNK A PROJEKTRŐL')}</a></div>
  </div>
</section>
"""
    extra_jsonld = f"""
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","name":{_jsonstr(d['h1'])},"serviceType":{_jsonstr(d['nav_label'])},"provider":{{"@type":"Organization","name":"Models on the Move"}},"areaServed":"Magyarország","description":{_jsonstr(d['meta_desc'])}}}
</script>
{faqld}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"Főoldal","item":"{BASE_URL}/"}},
{{"@type":"ListItem","position":2,"name":{_jsonstr(d['nav_label'])},"item":"{BASE_URL}/{d['slug']}/"}}
]}}
</script>"""
    return page(
        title=d["seo_title"],
        description=d["meta_desc"],
        canonical_path=d["slug"] + "/",
        body=body,
        depth=1,
        active="services",
        extra_jsonld=extra_jsonld,
    )


MODEL_APPLICATION_FORM = """
<section class="pad rule" id="jelentkezes">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MODELLNEK JELENTKEZEM</span><h2>Mutatkozz be röviden.</h2>
      <p>Nem kell hivatásos portfólió — pár jó minőségű kép és néhány mondat rólad elég az első lépéshez.</p>
    </div>
    <div class="wrap rv" style="padding:0;max-width:640px;">
      <form class="form-panel" data-motm-form data-msg-id="modelMsg" data-event="model_application_submit" novalidate>
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


def page(title, description, canonical_path, body, depth=None, active="", og_image="assets/hero-myrazs-poster.jpg", robots="index,follow", extra_jsonld=""):
    if depth is None:
        depth = 0 if canonical_path == "" else canonical_path.count("/")
    r = _root(depth)
    return (
        head(title, description, canonical_path, depth=depth, og_image=og_image, robots=robots, extra_jsonld=extra_jsonld)
        + "<body>\n"
        + nav(depth=depth, active=active)
        + '\n<main id="main">\n'
        + body
        + "\n</main>\n"
        + footer(depth=depth)
        + f'\n<script src="{r}assets/site.js"></script>\n'
        + "\n</body>\n</html>\n"
    )
