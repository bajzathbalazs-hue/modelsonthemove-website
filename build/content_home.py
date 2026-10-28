# -*- coding: utf-8 -*-
from content_events import EVENT_HOME_TEASER
from shell import faq_list

HOME_FAQ = [
    ("Csak teljes körű együttműködést vállaltok, vagy egy konkrét részfeladatot is?",
     "Mindkettőt. Van, aki a teljes marketingjét vagy egy komplett eseményét ránk bízza, és van, aki csak egy konkrét részfeladatra — pl. modellközvetítésre, egy videóra vagy a közösségi médiára — keres minket."),
    ("Nem tudom pontosan, mire van szükségem — akkor is érdemes megkeresni titeket?",
     "Igen, sőt ez a leggyakoribb eset. Mondd el a célt vagy a projektet, mi segítünk kibontani, milyen szolgáltatásokra és emberekre lesz szükség hozzá."),
    ("Vannak előre meghatározott csomagjaitok és áraitok?",
     "Nincsenek sablon csomagok. Minden ajánlat a projekt, a cél és a terjedelem alapján, egyedileg készül egy rövid egyeztetés után."),
    ("Csak nightlife-eseményekben van tapasztalatotok, vagy üzleti rendezvényekben is?",
     "A saját rendezvényeink nightlife-közeliek, de a modellközvetítés, a marketing és a rendezvényszervezés szolgáltatásunk is kiterjed üzleti eseményekre, nyitókra, termékbemutatókra és céges alkalmakra."),
    ("Mennyi idővel korábban érdemes megkeresni titeket?",
     "Minél komplexebb a projekt (esemény, több szereplős produkció), annál előbb érdemes elindítani az egyeztetést — de rövidebb határidejű megkeresésekben is segítünk, ha a naptárunk engedi."),
]
HOME_FAQ_HTML, HOME_FAQ_JSONLD = faq_list(HOME_FAQ)

HOME_BODY = """
<!-- 01 HERO -->
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
    <h1 class="hero-tag" style="font-family:var(--serif);font-size:clamp(20px,2.6vw,30px);max-width:640px;color:var(--ivory);line-height:1.35;margin-top:22px;">Embereket. Márkákat. Élményeket kapcsolunk össze.</h1>
    <p class="hero-tag">Modellek és influencerek, teljes körű marketing, kreatív produkciók és események egyetlen összehangolt budapesti csapattól.</p>
    <div class="hero-ctas">
      <a href="kapcsolat/" class="btn filled magnetic">BESZÉLJÜNK A CÉGEDRŐL</a>
      <a href="#pillars" class="btn magnetic">FEDEZD FEL, MIVEL FOGLALKOZUNK</a>
    </div>
    <a href="esemenyek/" class="hero-current">
      <span class="dot"></span>
      <span>KÖVETKEZŐ ESEMÉNYÜNK</span>
      <b>Hamarosan érkezünk a részletekkel.</b>
      <span class="arrow">→</span>
    </a>
  </div>
</section>
""" + EVENT_HOME_TEASER + """
<!-- 03 RÖVID POZICIONÁLÁS -->
<section class="pad">
  <div class="wrap">
    <div class="sec-head rv" style="max-width:820px;">
      <span class="eyebrow">POZICIONÁLÁS</span>
      <h2>Több mint egy modell-<br>vagy marketingügynökség.</h2>
      <p style="max-width:640px;">Nem egy szolgáltatás. Összehangolt emberek. Modellek, influencerek, fotósok, videósok, események — egy irányból, egy célra.</p>
      <p style="max-width:640px;font-weight:600;color:var(--ivory);">Egy feladatra is megkereshetsz. Vagy hosszú távra, teljes körűen.</p>
      <div class="stat-row rv-stagger">
        <div><b>2025</b><span>ALAPÍTVA</span></div>
        <div><b>3</b><span>SZERVEZETT ESEMÉNY</span></div>
        <div><b>40+</b><span>MODELL A HÁLÓZATBAN</span></div>
        <div><b>20–30</b><span>INFLUENCER PARTNER</span></div>
        <div><b>8–10</b><span>EGYÜTTMŰKÖDŐ MÁRKA</span></div>
      </div>
    </div>
  </div>
</section>

<!-- 03 HÁROM FŐ TERÜLET -->
<section class="pad rule" id="pillars" style="padding-top:100px;">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">04 — MIVEL FOGLALKOZUNK</span>
      <h2>Három terület.<br>Egy összehangolt csapat.</h2>
    </div>
    <div class="pillar-grid rv-stagger">
      <div class="pillar-card glow-card">
        <div class="plate photo dim-top" style="position:absolute;inset:0;z-index:-1;opacity:.4;background-image:url('assets/vibe-cellar-detail.jpg');"></div>
        <span class="n">01</span>
        <h3>Modellek és influencerek</h3>
        <p>Modelleket, influencereket, tartalomkészítőket és reklámarcokat kapcsolunk össze márkákkal, kampányokkal, fotózásokkal, forgatásokkal és eseményekkel.</p>
        <ul>
          <li>Modellközvetítés és casting</li>
          <li>Influencerközvetítés</li>
          <li>Influencer kampányok</li>
          <li>Menedzsment és képviselet</li>
          <li>Modellek forgatásokhoz, fotózásokhoz és eseményekhez</li>
        </ul>
        <a href="modellugynokseg/" class="go">MODELLEK ÉS INFLUENCEREK →</a>
      </div>
      <div class="pillar-card glow-card">
        <div class="plate photo dim-top" style="position:absolute;inset:0;z-index:-1;opacity:.4;background-image:url('assets/vibe-cellar-wide.jpg');"></div>
        <span class="n">02</span>
        <h3>Marketing és márkaépítés</h3>
        <p>A stratégiától a napi megvalósításig összehangoljuk a márkád digitális és kreatív jelenlétét.</p>
        <ul>
          <li>Marketingstratégia és teljes marketingmenedzsment</li>
          <li>Weboldal és webáruház</li>
          <li>SEO és PPC</li>
          <li>Közösségi média</li>
          <li>Fotó- és videógyártás</li>
          <li>Arculat és márkaépítés</li>
        </ul>
        <a href="marketing-ugynokseg/" class="go">MARKETING SZOLGÁLTATÁSOK →</a>
      </div>
      <div class="pillar-card glow-card">
        <div class="plate photo dim-top" style="position:absolute;inset:0;z-index:-1;opacity:.4;background-image:url('assets/vibe-mainroom.jpg');"></div>
        <span class="n">03</span>
        <h3>Események és produkciók</h3>
        <p>A koncepciótól a megvalósításig egy kézben koordináljuk a helyszínt, a szereplőket, a kreatív partnereket és az esemény kommunikációját.</p>
        <ul>
          <li>Márka- és termékbemutatók</li>
          <li>Étterem- és helyszínnyitók</li>
          <li>Influencer események</li>
          <li>Divatbemutatók</li>
          <li>Reklámforgatások</li>
          <li>Céges és egyedi VIP események</li>
        </ul>
        <a href="rendezvenyszervezes/" class="go">ESEMÉNYEK ÉS PRODUKCIÓK →</a>
      </div>
    </div>
  </div>
</section>

<!-- 04B PILLANATOK GALÉRIA -->
<section class="pad rule" style="padding-bottom:70px;">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">PILLANATOK</span><h2>Ízelítő az estéinkből.</h2></div>
  </div>
  <div class="hscroll rv-stagger">
    <a class="gcard wide" href="esemenyek/dubai-style/">
      <div class="plate photo grain" style="background-image:url('assets/vibe-mainroom.jpg');"></div>
      <div class="meta"><h4>Dubai Style</h4><span class="loc">VIBE Budapest</span></div>
    </a>
    <a class="gcard" href="esemenyek/myrazs-fashion-show/">
      <div class="plate photo grain" style="background-image:url('assets/ig-myrazs-recap.jpg');"></div>
      <div class="meta"><h4>Myrázs Divatbemutató</h4><span class="loc">MOM Leroy Bistro</span></div>
    </a>
    <a class="gcard" href="esemenyek/dubai-style/">
      <div class="plate photo grain" style="background-image:url('assets/vibe-redroom-group.jpg');background-position:center 15%;"></div>
      <div class="meta"><h4>Dubai Style</h4><span class="loc">VIBE Budapest</span></div>
    </a>
    <a class="gcard" href="esemenyek/dubai-style/">
      <div class="plate photo grain" style="background-image:url('assets/vibe-bartrio-final.jpg');background-position:center 30%;"></div>
      <div class="meta"><h4>Dubai Style</h4><span class="loc">VIBE Budapest</span></div>
    </a>
  </div>
  <div class="wrap">
    <p style="margin-top:24px;font-size:12.5px;color:var(--ivory-dimmer);">Több fotó hamarosan — a legutóbbi estéink friss anyagait töltjük fel.</p>
  </div>
</section>

<!-- 04 TELJES KÖRŰ MARKETINGMENEDZSMENT -->
<section class="pad rule" style="background:linear-gradient(180deg,transparent,rgba(224,90,50,.05),transparent);padding-top:110px;padding-bottom:110px;">
  <div class="wrap">
    <div class="sec-head rv" style="max-width:640px;margin-bottom:0;">
      <span class="eyebrow">TELJES KÖRŰ MARKETINGMENEDZSMENT</span>
      <h2>A külső marketingcsapatod.</h2>
      <p style="font-family:var(--serif);font-size:19px;color:var(--bronze-bright);margin-top:20px;">Nem kell öt különböző szolgáltató — egy jól összehangolt csapat, a modellektől a hirdetésekig.</p>
      <div style="margin-top:34px;">
        <a href="kapcsolat/" class="btn filled magnetic">BESZÉLJÜNK A CÉGEDRŐL</a>
      </div>
    </div>
  </div>
</section>

<!-- 04C STATEMENT -->
<section class="statement">
  <div class="plate grain">
    <video class="hero-video" autoplay muted loop playsinline preload="auto" poster="assets/vibe-cocktail-bg-poster.jpg">
      <source src="assets/vibe-cocktail-bg.mp4" type="video/mp4">
    </video>
  </div>
  <div class="statement-inner rv">
    <h2>EZ NEM CSAK EGY ESTE.<br><span class="thin">ez egy élmény, amit felépítünk.</span></h2>
    <p class="brandline">MODELS ON THE MOVE × A BUDAPESTI ÉJSZAKA</p>
  </div>
</section>

<!-- 05 HOGYAN DOLGOZUNK -->
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">HOGYAN DOLGOZUNK</span>
      <h2>Egy kapcsolat. A szükséges csapat.<br>Teljes koordináció.</h2>
    </div>
    <div class="process-grid rv-stagger">
      <div class="process-step"><span class="idx">01</span><h4>Megismerjük a célt</h4><p>Nem csomagot adunk el. Megismerjük a márkát, a célt, a közönséget.</p></div>
      <div class="process-step"><span class="idx">02</span><h4>Összeállítjuk a megoldást</h4><p>Szolgáltatás, szakember, modell, partner — pontosan, amire szükség van.</p></div>
      <div class="process-step"><span class="idx">03</span><h4>Megvalósítjuk és koordináljuk</h4><p>Egy kézben az egész: kommunikáció, tartalom, produkció.</p></div>
      <div class="process-step"><span class="idx">04</span><h4>Mérünk és továbbfejlesztünk</h4><p>Mérünk, finomítunk, fejlesztünk — folyamatosan.</p></div>
    </div>
  </div>
</section>

<!-- 06 KINEK DOLGOZUNK -->
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">KINEK DOLGOZUNK</span>
      <h2>Márkák, amelyeknek<br>számít a megjelenés.</h2>
    </div>
    <div class="audience-row rv-stagger">
      <span class="tag">Vendéglátás</span><span class="tag">Szállodák</span><span class="tag">Szórakozóhelyek</span>
      <span class="tag">Autó</span><span class="tag">Ingatlan</span><span class="tag">Divat</span>
      <span class="tag">Szépségápolás</span><span class="tag">Lifestyle</span><span class="tag">Prémium szolgáltatások</span>
      <span class="tag">Termékbevezetések</span>
    </div>
  </div>
</section>

<!-- 07 ESEMÉNYEK ÉS PRODUKCIÓK -->
<section class="pad rule">
  <div class="wrap">
    <div class="event-two-col rv">
      <div>
        <div class="sec-head" style="margin:0 0 26px;">
          <span class="eyebrow">ESEMÉNYEK ÉS PRODUKCIÓK</span>
          <h2>Egy ötletből<br>teljes élmény.</h2>
          <p style="max-width:480px;">Saját estéink mellett márkák eseményeit is megszervezzük — helyszíntől a dekorációig, egy kézben.</p>
        </div>
        <div class="audience-row" style="margin-top:26px;">
          <span class="tag">Márka- és termékbemutatók</span><span class="tag">Divatbemutatók</span>
          <span class="tag">Reklámforgatások</span><span class="tag">VIP események</span>
        </div>
        <div class="ctas" style="margin-top:34px;">
          <a href="esemenyek/" class="btn filled magnetic">NÉZD MEG AZ ESEMÉNYEINKET</a>
          <a href="rendezvenyszervezes/" class="btn magnetic">TERVEZZÜK MEG EGYÜTT</a>
        </div>
      </div>
      <a href="esemenyek/" class="plate photo grain glow-card" style="aspect-ratio:4/5;display:block;background-image:url('assets/vibe-redroom-group.jpg');background-position:center 15%;"></a>
    </div>
  </div>
</section>

<!-- 08 MIÉRT MI -->
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MIÉRT MI</span><h2>Miben más ez, mint egy hagyományos megoldás.</h2></div>
    <div class="compare-grid rv-stagger">
      <div class="compare-col">
        <h4>Hagyományos megoldás</h4>
        <ul>
          <li>Külön ügynökség modellekhez, marketinghez, eseményekhez</li>
          <li>Sok körös egyeztetés, lassú válaszok</li>
          <li>Sablon csomagok, nem a te projektedre szabva</li>
          <li>Nem mindig egyértelmű, ki miért felel</li>
        </ul>
      </div>
      <div class="compare-col compare-col--us">
        <h4>Models on the Move</h4>
        <ul>
          <li>Egy csapat, egy kapcsolattartó mindenre</li>
          <li>Gyors, közvetlen egyeztetés</li>
          <li>Minden ajánlat a projektedre szabva</li>
          <li>Végig tudod, kivel beszélsz</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- 09 GYAKORI KÉRDÉSEK -->
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">GYAKORI KÉRDÉSEK</span><h2>Amit a legtöbben kérdeznek.</h2></div>
    <div class="rv">""" + HOME_FAQ_HTML + """</div>
  </div>
</section>

<!-- 10 ZÁRÓ AJÁNLATKÉRŐ -->
<section class="cta-band rule">
  <div class="wrap rv">
    <span class="eyebrow">BESZÉLJÜNK</span>
    <h2 style="margin-top:18px;">Mondd el, mit szeretnél elérni.</h2>
    <p style="max-width:520px;margin:0 auto 34px;font-size:14.5px;color:var(--ivory-dim);line-height:1.8;">Nem kell pontosan tudnod, melyik szolgáltatásra van szükséged. Írd le a célt vagy a projektet, és beszéljük át személyesen.</p>
    <div class="ctas">
      <a href="kapcsolat/" class="btn filled magnetic">BESZÉLJÜNK A CÉGEDRŐL</a>
    </div>
  </div>
</section>
"""
