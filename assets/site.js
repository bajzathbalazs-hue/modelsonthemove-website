window.MOTM_CONFIG = {
  baseUrl: "https://bajzathbalazs-hue.github.io/modelsonthemove-website",
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

/* ============ scroll reveal ============ */
const io = new IntersectionObserver((entries)=>{
  entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
},{threshold:.15});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));

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
