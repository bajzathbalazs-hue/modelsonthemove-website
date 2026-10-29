# -*- coding: utf-8 -*-
# Főoldal — "Models on the Move – weboldal-brief és szövegek (1. változat)",
# 2026.10.29, 4.1 szakasz szerint, betűre pontosan.

HOME_BODY = """
<!-- NYITÓ BLOKK -->
<section class="hero" id="top">
  <div class="plate photo grain">
    <video class="hero-video" autoplay muted loop playsinline preload="auto" fetchpriority="high" poster="assets/hero-myrazs-poster.jpg">
      <source src="assets/hero-myrazs.mp4" type="video/mp4">
    </video>
  </div>
  <div class="hero-inner">
    <div class="hero-kicker"><span class="dot"></span><span class="eyebrow">MODELS ON THE MOVE — BUDAPEST</span></div>
    <div class="collab">
      <span class="m1">MODELS ON THE MOVE</span>
    </div>
    <h1 class="hero-tag" style="font-family:var(--serif);font-size:clamp(22px,2.8vw,32px);max-width:640px;color:var(--ivory);line-height:1.35;margin-top:22px;">Élményt és láthatóságot teremtünk.</h1>
    <p class="hero-tag">Prémium eseményeket szervezünk, és abban is segítünk, hogy a vállalkozásod az online térben is ugyanilyen erős benyomást keltsen.</p>
    <div class="hero-ctas">
      <a href="esemenyek/" class="btn filled magnetic">A KÖVETKEZŐ ESEMÉNY</a>
      <a href="kapcsolat/" class="btn magnetic">INGYENES KONZULTÁCIÓT KÉREK</a>
    </div>
  </div>
</section>

<!-- SZÁMOK SÁV -->
<section class="pad rule">
  <div class="wrap">
    <div class="stat-row rv-stagger" style="margin-top:0;">
      <div><b>4</b><span>MEGRENDEZETT ESEMÉNY</span></div>
      <div><b>300–400</b><span>VENDÉG ESEMÉNYENKÉNT</span></div>
      <div><b>16</b><span>ÁLLANDÓ INFLUENCERPARTNER</span></div>
      <div><b>≈790 000</b><span>ELÉRHETŐ KÖVETŐ</span></div>
      <div><b>330 000+</b><span>MEGTEKINTÉS EGYETLEN KAMPÁNYBAN</span></div>
    </div>
  </div>
</section>

<!-- HÁROM PILLÉR -->
<section class="pad rule" id="pillars" style="padding-top:100px;">
  <div class="wrap">
    <div class="pillar-grid rv-stagger">
      <div class="pillar-card glow-card">
        <div class="plate photo dim-top" style="position:absolute;inset:0;z-index:-1;opacity:.4;background-image:url('assets/vibe-mainroom.jpg');"></div>
        <span class="n">01</span>
        <h3>Események</h3>
        <p>Esték, amelyekről még hetekig beszélnek. Válogatott közönség, prémium helyszín, VIP-asztalok, és ha szeretnéd, luxusautóval érkezel.</p>
        <a href="esemenyek/" class="go">MEGNÉZEM AZ ESEMÉNYEKET →</a>
      </div>
      <div class="pillar-card glow-card">
        <div class="plate photo dim-top" style="position:absolute;inset:0;z-index:-1;opacity:.4;background-image:url('assets/svc-weboldal-keszites.png');"></div>
        <span class="n">02</span>
        <h3>Arculat, weboldal és marketing cégeknek</h3>
        <p>A logótól a weboldalon át a hirdetésekig mindent egy kézben tartunk, mesterséges intelligenciával felgyorsítva.</p>
        <a href="kapcsolat/" class="go">INGYENES KONZULTÁCIÓT KÉREK →</a>
      </div>
      <div class="pillar-card glow-card">
        <div class="plate photo dim-top" style="position:absolute;inset:0;z-index:-1;opacity:.4;background-image:url('assets/svc-influencer-marketing.png');"></div>
        <span class="n">03</span>
        <h3>Influencer és tartalomgyártás</h3>
        <p>Tartalom, amelynél megáll a görgetés. Szépségkirálynőkből, olimpikonokból, modellekből és ismert tartalomgyártókból álló hálózatunkkal oda visszük a márkádat, ahol a figyelem van.</p>
        <a href="influencer-egyuttmukodes/" class="go">EGYÜTTMŰKÖDÉST KEZDEMÉNYEZEK →</a>
      </div>
    </div>
  </div>
</section>

<!-- AMIT MÁR BIZONYÍTOTTUNK -->
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">AMIT MÁR BIZONYÍTOTTUNK</span>
      <h2>Legutóbbi eseményünk kampányidőszakában 332 ezer megtekintést értünk el, 81 ezer egyedi nézővel.</h2>
      <p>A nézők 87,6%-a új közönség volt, vagyis nem a meglévő követőinkből érkezett.</p>
    </div>
  </div>
</section>

<!-- KIKNEK DOLGOZUNK -->
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KIKNEK DOLGOZUNK</span>
      <h2>Prémium autókereskedelmi, ingatlankezelési és ipari vállalkozásoknak, kivitelező cégeknek, egy olaszországi gyártó cégnek, valamint olasz élelmiszereket és divatárut forgalmazó webshopoknak építünk arculatot, weboldalt és marketinget.</h2>
      <p>Eddig 10+ céges projektet valósítottunk meg.</p>
    </div>
    <div class="industry-grid rv-stagger">
      <div class="industry-card"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 11l1.5-4.5A2 2 0 0 1 8.4 5h7.2a2 2 0 0 1 1.9 1.5L19 11M4 11h16v5a1 1 0 0 1-1 1h-1v-2H6v2H5a1 1 0 0 1-1-1v-5Z"/><circle cx="7.5" cy="17" r="1.3"/><circle cx="16.5" cy="17" r="1.3"/></svg><span>Autókereskedelem</span></div>
      <div class="industry-card"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 21V9l8-6 8 6v12M4 21h16M9 21v-7h6v7"/></svg><span>Ingatlankezelés</span></div>
      <div class="industry-card"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 21V11l5 3v-3l5 3V8l6 3v10H3Z"/></svg><span>Ipar</span></div>
      <div class="industry-card"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 19a8 8 0 0 1 16 0M4 19h16M11 5v4"/></svg><span>Kivitelezés</span></div>
      <div class="industry-card"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M3 12h3M18 12h3M4.9 19.1 7 17M17 7l2.1-2.1"/></svg><span>Olasz gyártó</span></div>
      <div class="industry-card"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 7h12l-1 13H7L6 7Z"/><path d="M9 7V5a3 3 0 0 1 6 0v2"/></svg><span>Élelmiszer-webshop</span></div>
      <div class="industry-card"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2.5a1.5 1.5 0 1 0-1.3 2.2L12 6l-9 5.5 1 1.7L12 9v9H8v1.5h8V18h-4V9l8 3.2 1-1.7L13.3 4.7A1.5 1.5 0 0 0 12 2.5Z"/></svg><span>Divatwebshop</span></div>
    </div>
  </div>
</section>

<!-- KIK VAGYUNK -->
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KIK VAGYUNK</span><h2>Bajzáth Balázs és Molnár Míra vagyunk.</h2>
      <p>[Szerepek: később pontosítjuk.] Mindent személyesen viszünk, így pontosan tudod, kivel dolgozol.</p>
    </div>
    <div style="margin-top:10px;text-align:center;"><a href="rolunk/" class="btn magnetic">RÓLUNK →</a></div>
  </div>
</section>

<!-- ESZKÖZSÁV -->
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">ESZKÖZÖK</span><h2>A legjobb eszközökkel dolgozunk.</h2>
      <p>Szakmai tudásunkat a legmodernebb eszközökkel és mesterséges intelligenciával ötvözzük, hogy gyorsabban, pontosabban és mérhetőbben dolgozzunk. Ezekkel az eszközökkel dolgozunk.</p>
    </div>
    <div class="audience-row rv-stagger" style="justify-content:center;">
      <span class="tag">Shopify</span><span class="tag">Framer</span><span class="tag">Netlify</span><span class="tag">GitHub</span>
      <span class="tag">Ahrefs</span><span class="tag">Claude</span><span class="tag">ChatGPT</span><span class="tag">Canva</span>
      <span class="tag">Notion</span><span class="tag">Google Ads</span><span class="tag">Google Analytics</span><span class="tag">Google Workspace</span>
      <span class="tag">Meta</span><span class="tag">TikTok</span><span class="tag">Adobe</span><span class="tag">Figma</span>
    </div>
  </div>
</section>

<!-- ZÁRÓ BLOKK -->
<section class="cta-band rule">
  <div class="wrap rv">
    <span class="eyebrow">KEZDJÜK EL</span>
    <h2 style="margin-top:18px;">Van egy ötleted? Beszéljük meg.</h2>
    <p style="max-width:520px;margin:0 auto 34px;font-size:14.5px;color:var(--ivory-dim);line-height:1.8;">Egy rövid, kötetlen beszélgetés során átnézzük, hol tartasz, és mi lenne a következő jó lépés.</p>
    <div class="ctas">
      <a href="kapcsolat/" class="btn filled magnetic" data-tier-cta='{"1":{"label":"ÍRJ NEKÜNK","href":"kapcsolat/"},"2":{"label":"INGYENES KONZULTÁCIÓT KÉREK","href":"kapcsolat/"},"3":{"label":"INDÍTSUK EL A PROJEKTED","href":"projekt-inditasa/"}}'>ÍRJ NEKÜNK</a>
    </div>
  </div>
</section>
"""
