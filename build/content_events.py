# -*- coding: utf-8 -*-

EVENT_TICKET_URL = "https://www.sevenrooms.com/events/vibebudapest/models-on-the-move-meta-2"
EVENT_TABLE_URL = "https://www.sevenrooms.com/experiences/vibebudapest/vibe-x-models-on-the-move-5074707521585152?lang=hu"
EVENT_SLUG = "dubai-style"

# ---- Instagram poszt-linkek a galéria csempékhez (kattintásra a valódi posztra/reelre visz) ----
IG_FEATURED = "https://www.instagram.com/p/DYm2IkFilaO/"
IG_FASHIONSHOW_REPORT = "https://www.instagram.com/p/DV13-0SCPjM/"
IG_POPOUT = "https://www.instagram.com/p/DVopDD_DTAr/"
IG_AFROHOUSE_ANNOUNCE = "https://www.instagram.com/p/DUgQUjGgjmC/"
IG_MOMLEROY_TEASER = "https://www.instagram.com/p/DUThgzQEhK4/"
IG_MYRAZS_RECAP = "https://www.instagram.com/p/DT8UZeBAgkQ/"
IG_AFTERPARTY_TICKETS = "https://www.instagram.com/p/DU8rIVhgjz3/"
IG_MYRAZS_TICKET_PROMO = "https://www.instagram.com/p/DXuTi24DD-C/"
IG_MYRAZS_FEATHER_MIRAGE = "https://www.instagram.com/p/DaNzhxwCTw9/"

# ---- homepage teaser (placed directly under the hero) ----
EVENT_HOME_TEASER = f"""
<!-- 02 AKTUÁLIS ESEMÉNY -->
<section class="pad rule" style="padding-top:100px;">
  <div class="wrap">
    <div class="event-head rv">
      <div>
        <span class="eyebrow">02 — AKTUÁLIS ESEMÉNYÜNK</span>
        <h2 style="margin-top:14px;">MODELS ON THE MOVE<br><em>× VIBE</em> — DUBAI STYLE</h2>
      </div>
      <div class="event-side">
        <p>2026. október 16-án a Models on the Move × VIBE Budapest — Dubai Style elhozza a dubai éjszakák stílusát és energiáját. Fabios és Mandmil Afro House szettjei, táncosok és élő előadók emelik új szintre az estét.</p>
      </div>
    </div>
    <div class="event-grid rv">
      <div class="event-plate plate photo grain">
        <video class="hero-video" autoplay muted loop playsinline poster="assets/vibe-cocktail-bg-poster.jpg">
          <source src="assets/vibe-cocktail-bg.mp4" type="video/mp4">
        </video>
      </div>
      <div class="event-info">
        <div class="event-facts">
          <div><span>DÁTUM</span><span>2026. OKTÓBER 16., PÉNTEK</span></div>
          <div><span>IDŐPONT</span><span>23:00–03:00</span></div>
          <div><span>HELYSZÍN</span><span>VIBE Budapest</span></div>
        </div>
        <div class="lineup">
          <h4>DJ LINE-UP</h4>
          <div class="dj"><span class="name">Fabios</span><span class="meta"><span class="genre">23:00–01:00 · Afro House</span></span></div>
          <div class="dj"><span class="name">Mandmil</span><span class="meta"><span class="genre">01:00–03:00 · Afro House</span></span></div>
        </div>
        <div class="event-cta">
          <a href="{EVENT_TICKET_URL}" class="btn filled magnetic" target="_blank" rel="noopener">JEGYVÁSÁRLÁS</a>
          <a href="esemenyek/{EVENT_SLUG}/" class="btn magnetic">RÉSZLETEK →</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# ---- /esemenyek/ index page (overview + gallery) ----
EVENTS_BODY = f"""
%%BREADCRUMB%%
<section class="gal-hero">
  <div class="wrap">
    <div class="rv">
      <span class="eyebrow">ESEMÉNYEK</span>
      <h1>Korábbi esték.<br>Maradandó pillanatok.</h1>
      <p>Minden Models on the Move est egy saját világ — fotók és összefoglaló videók, ahogy egyre több esemény kerül fel ide. Ha lemaradtál egy estéről, itt éled újra. Alább a legközelebbi eseményünket is megtalálod.</p>
      <a href="{EVENT_SLUG}/" class="btn filled magnetic">AKTUÁLIS ESEMÉNY: DUBAI STYLE →</a>
    </div>
  </div>
</section>

<section class="pad rule" id="aktualis" style="padding-top:60px;">
  <div class="wrap">
    <div class="event-head rv">
      <h2>MODELS ON<br>THE MOVE <em>× VIBE</em></h2>
      <div class="event-side">
        <p>2026. október 16. — Dubai Style. Fabios és Mandmil Afro House szettjei, táncosok, élő előadók és bottle service egy estén a VIBE Budapestben.</p>
      </div>
    </div>
    <div class="event-grid rv">
      <div class="event-plate plate photo grain">
        <video class="hero-video" autoplay muted loop playsinline poster="../assets/vibe-cocktail-bg-poster.jpg">
          <source src="../assets/vibe-cocktail-bg.mp4" type="video/mp4">
        </video>
      </div>
      <div class="event-info">
        <div class="event-facts">
          <div><span>DÁTUM</span><span>2026. OKTÓBER 16.</span></div>
          <div><span>IDŐPONT</span><span>23:00–03:00</span></div>
          <div><span>HELYSZÍN</span><span>VIBE Budapest</span></div>
        </div>
        <div class="event-cta">
          <a href="{EVENT_SLUG}/" class="btn filled magnetic">RÉSZLETEK, JEGYEK, ASZTALFOGLALÁS →</a>
        </div>
        <div class="campaign-strip">
          <div class="plate photo grain" style="background-image:url('../assets/vibe-champagne-cellar.jpg');"></div>
          <div class="plate photo grain" style="background-image:url('../assets/vibe-nightclub-wide.jpg');"></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">ELŐZŐ ESTÉINK</span><h2>A galéria.</h2></div>
    <div class="gallery-grid rv-stagger">

      <button type="button" class="gtile wide glow-card" data-ig-permalink="{IG_FEATURED}">
        <div class="plate photo grain" style="background-image:url('../assets/ig-featured-momleroy.jpg')"></div>
        <span class="gtile-badge">▶ INSTAGRAM</span>
        <div class="gtile-meta">
          <h3>MOM Leroy — Fashion Show &amp; Afro House Night</h3>
          <span>@models_on_the_move · Instagram</span>
        </div>
      </button>

      <div class="gtile wide glow-card">
        <div class="plate photo grain" style="background-image:url('../assets/leroy-szezonnyito.jpg')"></div>
        <div class="gtile-meta">
          <h3>Szezonnyitó — Day Time Party &amp; Fashion Show</h3>
          <span>MOM Leroy Bistro · 2026.05.29.</span>
        </div>
      </div>

      <div class="gtile glow-card">
        <video class="gtile-video" autoplay muted loop playsinline controls poster="../assets/hero-myrazs-poster.jpg">
          <source src="../assets/hero-myrazs.mp4" type="video/mp4">
        </video>
        <span class="gtile-badge">▶ VIDEÓ</span>
        <div class="gtile-meta">
          <h3>Szezonnyitó — Összefoglaló videó</h3>
          <span>MOM Leroy Bistro</span>
        </div>
      </div>

      <div class="gtile glow-card">
        <div class="plate photo grain" style="background-image:url('../assets/leroy-fashionshow.jpg')"></div>
        <div class="gtile-meta">
          <h3>Models on the Move × The Pop Out</h3>
          <span>MOM Leroy Bistro</span>
        </div>
      </div>

      <button type="button" class="gtile glow-card" data-ig-permalink="{IG_MYRAZS_RECAP}">
        <div class="plate photo grain" style="background-image:url('../assets/ig-myrazs-recap.jpg')"></div>
        <span class="gtile-badge">INSTAGRAM</span>
        <div class="gtile-meta">
          <h3>Myrázs — Fashion Show &amp; After Party</h3>
          <span>MOM Leroy · Január 9.</span>
        </div>
      </button>

      <button type="button" class="gtile glow-card" data-ig-permalink="{IG_FASHIONSHOW_REPORT}">
        <div class="plate photo grain" style="background-image:url('../assets/ig-fashionshow-videoreport.jpg')"></div>
        <span class="gtile-badge">▶ INSTAGRAM</span>
        <div class="gtile-meta">
          <h3>Fashion Show — Video Report</h3>
          <span>@mavreels</span>
        </div>
      </button>

      <button type="button" class="gtile glow-card" data-ig-permalink="{IG_AFROHOUSE_ANNOUNCE}">
        <div class="plate photo grain" style="background-image:url('../assets/ig-afrohouse-announce.jpg')"></div>
        <span class="gtile-badge">▶ INSTAGRAM</span>
        <div class="gtile-meta">
          <h3>Afro House Night</h3>
          <span>@models_on_the_move</span>
        </div>
      </button>

      <button type="button" class="gtile glow-card" data-ig-permalink="{IG_MOMLEROY_TEASER}">
        <div class="plate photo grain" style="background-image:url('../assets/ig-momleroy-teaser.jpg')"></div>
        <span class="gtile-badge">▶ INSTAGRAM</span>
        <div class="gtile-meta">
          <h3>MOM Leroy Bistro</h3>
          <span>@momleroy</span>
        </div>
      </button>

      <button type="button" class="gtile glow-card" data-ig-permalink="{IG_AFTERPARTY_TICKETS}">
        <div class="plate photo grain" style="background-image:url('../assets/ig-afterparty-tickets.jpg')"></div>
        <span class="gtile-badge">▶ INSTAGRAM</span>
        <div class="gtile-meta">
          <h3>Models on the Move After Party</h3>
          <span>@models_on_the_move</span>
        </div>
      </button>

      <button type="button" class="gtile glow-card" data-ig-permalink="{IG_MYRAZS_TICKET_PROMO}">
        <div class="plate photo grain" style="background-image:url('../assets/ig-myrazs-ticket-promo.jpg')"></div>
        <span class="gtile-badge">▶ INSTAGRAM</span>
        <div class="gtile-meta">
          <h3>Myrázs</h3>
          <span>@myrazs.by.mira</span>
        </div>
      </button>

      <button type="button" class="gtile glow-card" data-ig-permalink="{IG_MYRAZS_FEATHER_MIRAGE}">
        <div class="plate photo grain" style="background-image:url('../assets/ig-myrazs-feather-mirage.jpg')"></div>
        <span class="gtile-badge">▶ INSTAGRAM</span>
        <div class="gtile-meta">
          <h3>Myrázs — Feather Mirage kollekció</h3>
          <span>@myrazs.by.mira</span>
        </div>
      </button>

    </div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Szerveznél hasonló estét a márkádnak?</h2>
    <div class="ctas"><a href="../rendezvenyszervezes/" class="btn filled magnetic">TERVEZZÜK MEG EGYÜTT</a></div>
  </div>
</section>

<div class="ig-modal" id="igModal" role="dialog" aria-modal="true" aria-label="Instagram bejegyzés">
  <div class="ig-modal-backdrop" data-ig-close></div>
  <div class="ig-modal-panel">
    <button type="button" class="ig-modal-close" data-ig-close aria-label="Bezárás">&times;</button>
    <div class="ig-modal-body" id="igModalBody"></div>
  </div>
</div>
<script>
(function(){{
  var modal = document.getElementById('igModal');
  var body = document.getElementById('igModalBody');
  function tryProcess(retries){{
    if(window.instgrm){{ window.instgrm.Embeds.process(); }}
    else if(retries > 0){{ setTimeout(function(){{ tryProcess(retries - 1); }}, 300); }}
  }}
  function openModal(permalink){{
    body.innerHTML = '<blockquote class="instagram-media" data-instgrm-permalink="' + permalink + '" data-instgrm-version="14" style="margin:0;width:100%;"></blockquote>';
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    tryProcess(10);
  }}
  function closeModal(){{
    modal.classList.remove('open');
    document.body.style.overflow = '';
    body.innerHTML = '';
  }}
  document.querySelectorAll('[data-ig-permalink]').forEach(function(el){{
    el.addEventListener('click', function(){{ openModal(el.getAttribute('data-ig-permalink')); }});
  }});
  modal.querySelectorAll('[data-ig-close]').forEach(function(el){{
    el.addEventListener('click', closeModal);
  }});
  document.addEventListener('keydown', function(e){{ if(e.key === 'Escape' && modal.classList.contains('open')) closeModal(); }});
}})();
</script>
<script async src="https://www.instagram.com/embed.js"></script>
"""

# ---- dedicated event detail page: /esemenyek/dubai-style/ ----
EVENT_DETAIL_BODY = f"""
<style>
.event-hero-bg{{background-image:url('../../assets/dubai-style-flyer.jpg');background-position:center 22%;}}
@media(max-width:680px){{.event-hero-bg{{background-image:url('../../assets/dubai-style-flyer-portrait.jpg');background-position:center top;}}}}
</style>
<section class="hero" style="min-height:82vh;">
  <div class="plate photo event-hero-bg"></div>
  <a href="../" class="event-hero-back rv" style="position:absolute;top:110px;left:48px;z-index:3;">← ÖSSZES ESEMÉNY</a>
  <div class="hero-inner" style="padding-bottom:44px;">
    <div class="hero-ctas rv">
      <a href="{EVENT_TICKET_URL}" class="btn filled magnetic" target="_blank" rel="noopener">JEGYVÁSÁRLÁS</a>
      <a href="{EVENT_TABLE_URL}" class="btn magnetic" target="_blank" rel="noopener">ASZTALFOGLALÁS</a>
    </div>
  </div>
</section>

<section class="pad rule" style="padding-top:70px;padding-bottom:70px;">
  <div class="wrap">
    <div class="hero-kicker rv"><span class="dot"></span><span class="eyebrow">MODELS ON THE MOVE × VIBE BUDAPEST</span></div>
    <h1 class="rv" style="font-family:var(--sans);font-weight:800;text-transform:uppercase;font-size:clamp(38px,7vw,90px);line-height:.98;letter-spacing:-.01em;margin-top:18px;">DUBAI STYLE.</h1>
    <p class="rv" style="font-size:15.5px;line-height:1.85;color:var(--ivory-dim);max-width:620px;margin-top:26px;">A divat világa találkozik a VIBE karakteres hangulatával — Fabios és Mandmil Afro House szettjei, táncosok és élő előadók emelik új szintre az estét. Exkluzív italok, bottle service és snackek egész este.</p>
    <div class="hero-meta rv">
      <div><b>2026.10.16.</b><span>DÁTUM · PÉNTEK</span></div>
      <div><b>23:00–03:00</b><span>IDŐPONT</span></div>
      <div><b>VIBE Budapest</b><span>HELYSZÍN</span></div>
      <div><b>18+</b><span>KORHATÁR</span></div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="event-two-col rv">
      <div>
        <span class="eyebrow">AZ ESTE</span>
        <h2 style="font-family:var(--serif);font-size:clamp(26px,3.6vw,40px);font-weight:400;margin-top:14px;line-height:1.2;">Egy este Dubaiból,<br>Budapest szívében.</h2>
        <p style="font-size:15px;line-height:1.9;color:var(--ivory-dim);margin-top:24px;max-width:520px;">2026. október 16-án a Models on the Move × VIBE Budapest — Dubai Style elhozza a dubai éjszakák stílusát és energiáját Budapestre.</p>
        <p style="font-size:15px;line-height:1.9;color:var(--ivory-dim);margin-top:18px;max-width:520px;">A divat világa találkozik a VIBE karakteres hangulatával: Fabios és Mandmil Afro House szettjei, táncosok és élő előadók emelik új szintre az éjszakát.</p>
        <p style="font-size:15px;line-height:1.9;color:var(--ivory-dim);margin-top:18px;max-width:520px;">Exkluzív italok, bottle service és snackek egész este — a választás a tiéd, az élmény az asztalodnál folytatódik.</p>

        <div class="lineup" style="margin-top:40px;">
          <h4>DJ LINE-UP</h4>
          <div class="dj"><span class="name">Fabios</span><span class="meta"><span class="genre">Afro House</span><span class="ig">23:00–01:00</span></span></div>
          <div class="dj"><span class="name">Mandmil</span><span class="meta"><span class="genre">Afro House</span><span class="ig">01:00–03:00</span></span></div>
        </div>

        <div class="event-facts" style="margin-top:40px;max-width:480px;">
          <div><span>DÁTUM</span><span>2026. október 16., péntek</span></div>
          <div><span>IDŐPONT</span><span>23:00–03:00</span></div>
          <div><span>HELYSZÍN</span><span>VIBE Budapest</span></div>
          <div><span>DRESS CODE</span><span>Elegáns party stílus</span></div>
          <div><span>KORHATÁR</span><span>18+</span></div>
        </div>
      </div>

      <div>
        <span class="eyebrow">JEGYEK ÉS ASZTALFOGLALÁS</span>
        <h3 style="font-family:var(--sans);font-weight:800;text-transform:uppercase;font-size:19px;margin-top:14px;margin-bottom:22px;">Állójegyek</h3>
        <div class="ticket-tiers">
          <div class="tier soldout"><span class="k">Early Bird <span class="tier-badge">ELFOGYOTT</span></span><span class="v">4 000 Ft</span></div>
          <div class="tier"><span class="k">Elővételes jegy</span><span class="v">6 000 Ft</span></div>
          <div class="tier"><span class="k">Helyszíni jegy</span><span class="v">8 000 Ft</span></div>
        </div>
        <p style="font-family:var(--mono);font-size:10.5px;letter-spacing:.05em;color:var(--peach-bright);margin-top:14px;">Az Early Bird jegyek egy nap alatt elfogytak — elővételes jegyek még elérhetők.</p>
        <div class="event-cta-row">
          <a href="{EVENT_TICKET_URL}" class="btn filled magnetic" target="_blank" rel="noopener">JEGYVÁSÁRLÁS</a>
        </div>

        <h3 style="font-family:var(--sans);font-weight:800;text-transform:uppercase;font-size:19px;margin-top:50px;margin-bottom:16px;">Asztaljegyek</h3>
        <p style="font-size:14px;line-height:1.85;color:var(--ivory-dim);max-width:480px;">Ha az állójegy helyett inkább ülőhelyet szeretnél, foglald le az asztalodat — a részleteket és az elérhető asztalokat a foglalási oldalon találod. Az asztalok limitált számban foglalhatók.</p>
        <div class="note-box">
          <b>Fontos:</b> az asztalfoglalás díja nem fogyasztási minimum — a foglalási díj egyben a belépődet is tartalmazza. Ha asztalt foglalsz, külön állójegyet már nem kell vásárolnod.
        </div>
        <div class="event-cta-row">
          <a href="{EVENT_TABLE_URL}" class="btn magnetic" target="_blank" rel="noopener">ASZTALFOGLALÁS</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">A HELYSZÍN</span><h2>Ízelítő a VIBE hangulatából.</h2>
      <p>Az esemény napján és utána itt jelennek meg a friss fotók és az összefoglaló videó is.</p>
    </div>
    <div class="gallery-grid rv-stagger">
      <div class="gtile wide glow-card"><div class="plate photo grain" style="background-image:url('../../assets/vibe-jungle-lounge.jpg');"></div></div>
      <div class="gtile glow-card"><div class="plate photo grain" style="background-image:url('../../assets/vibe-bartrio-final.jpg');background-position:center 30%;"></div></div>
      <div class="gtile glow-card"><div class="plate photo grain" style="background-image:url('../../assets/vibe-redroom-group.jpg');background-position:center 15%;"></div></div>
      <div class="gtile glow-card"><div class="plate photo grain" style="background-image:url('../../assets/vibe-table-group.jpg');background-position:center 15%;"></div></div>
      <div class="gtile glow-card"><div class="plate photo grain" style="background-image:url('../../assets/vibe-cellar-table.jpg');"></div></div>
      <div class="gtile soon"><div class="plate plate--forest"></div><span class="soon-label">▶ VIDEÓ HAMAROSAN</span></div>
    </div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Biztosítsd a helyed, és légy részese a VIBE energiájának.</h2>
    <div class="ctas">
      <a href="{EVENT_TICKET_URL}" class="btn filled magnetic" target="_blank" rel="noopener">JEGYVÁSÁRLÁS</a>
      <a href="{EVENT_TABLE_URL}" class="btn magnetic" target="_blank" rel="noopener">ASZTALFOGLALÁS</a>
    </div>
  </div>
</section>
"""

REDIRECT_HTML = """<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url=esemenyek/">
<link rel="canonical" href="{base}/esemenyek/">
<title>Models on the Move — Események</title>
</head>
<body>
<p>Ez az oldal átköltözött: <a href="esemenyek/">Models on the Move — Események</a>.</p>
</body>
</html>
"""
