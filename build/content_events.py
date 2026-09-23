# -*- coding: utf-8 -*-

EVENTS_BODY = """
%%BREADCRUMB%%
<section class="gal-hero">
  <div class="wrap">
    <div class="rv">
      <span class="eyebrow">ESEMÉNYEK</span>
      <h1>Korábbi esték.<br>Maradandó pillanatok.</h1>
      <p>Minden Models on the Move est egy saját világ — fotók és összefoglaló videók, ahogy egyre több esemény kerül fel ide. Ha lemaradtál egy estéről, itt éled újra. Alább a legközelebbi eseményünket is megtalálod.</p>
      <a href="#aktualis" class="btn filled magnetic">AKTUÁLIS ESEMÉNY</a>
    </div>
  </div>
</section>

<section class="pad rule" id="aktualis" style="padding-top:60px;">
  <div class="wrap">
    <div class="event-head rv">
      <h2>MODELS ON<br>THE MOVE <em>× VIBE</em></h2>
      <div class="event-side">
        <p>Egy este, ahol a Models on the Move márka minden eleme találkozik: modellek, VIP közönség és prémium produkció a VIBE Budapestben.</p>
      </div>
    </div>
    <div class="event-grid rv">
      <div class="event-plate plate photo grain" style="background-image:url('../assets/hero-champagne.jpg');"></div>
      <div class="event-info">
        <div class="event-facts">
          <div><span>DÁTUM</span><span>2026. OKTÓBER 16.</span></div>
          <div><span>HELYSZÍN</span><span>VIBE Budapest</span></div>
        </div>
        <div class="event-cta">
          <a href="../kapcsolat/" class="btn filled magnetic">ASZTALFOGLALÁS</a>
        </div>
        <div class="campaign-strip">
          <div class="plate photo grain" style="background-image:url('../assets/vibe-cellar-wide.jpg');"></div>
          <div class="plate photo grain" style="background-image:url('../assets/vibe-jungle.jpg');"></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">ELŐZŐ ESTÉINK</span><h2>A galéria.</h2></div>
    <div class="gallery-grid rv">

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

      <div class="gtile soon"><div class="plate plate--bronze"></div><span class="soon-label">FOTÓ HAMAROSAN</span></div>
      <div class="gtile soon"><div class="plate plate--night"></div><span class="soon-label">▶ VIDEÓ HAMAROSAN</span></div>
      <div class="gtile soon"><div class="plate plate--forest"></div><span class="soon-label">FOTÓ HAMAROSAN</span></div>
      <div class="gtile soon"><div class="plate plate--jewel"></div><span class="soon-label">FOTÓ HAMAROSAN</span></div>
      <div class="gtile soon"><div class="plate plate--champagne"></div><span class="soon-label">▶ VIDEÓ HAMAROSAN</span></div>

    </div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Szerveznél hasonló estét a márkádnak?</h2>
    <div class="ctas"><a href="../rendezvenyszervezes/" class="btn filled magnetic">TERVEZZÜK MEG EGYÜTT</a></div>
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
