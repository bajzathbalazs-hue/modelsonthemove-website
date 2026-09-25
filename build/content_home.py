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
    <video class="hero-video" autoplay muted loop playsinline poster="assets/hero-myrazs-poster.jpg">
      <source src="assets/hero-myrazs.mp4" type="video/mp4">
    </video>
  </div>
  <div class="blob gold" style="width:560px;height:560px;top:-140px;left:-140px;" aria-hidden="true"></div>
  <div class="blob ember" style="width:480px;height:480px;bottom:-140px;right:-120px;" aria-hidden="true"></div>
  <div class="blob ice" style="width:340px;height:340px;top:30%;right:8%;" aria-hidden="true"></div>
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
    <a href="esemenyek/dubai-style/" class="hero-current">
      <span class="dot"></span>
      <span>JELENLEGI ESEMÉNYÜNK</span>
      <b>MODELS ON THE MOVE × VIBE — DUBAI STYLE — 2026.10.16.</b>
      <span class="arrow">→</span>
    </a>
    <div class="hero-trio">
      <div><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="3.5"/><path d="M5 21c0-4 3-7 7-7s7 3 7 7"/></svg><span>MODELLEK ÉS INFLUENCEREK</span></div>
      <div><svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h10"/><circle cx="19" cy="18" r="2"/></svg><span>MARKETING ÉS MÁRKAÉPÍTÉS</span></div>
      <div><svg viewBox="0 0 24 24"><path d="M4 4h16v4H4zM4 10h10v10H4zM16 10h4v10h-4z"/></svg><span>ESEMÉNYEK ÉS PRODUKCIÓK</span></div>
    </div>
  </div>
</section>
""" + EVENT_HOME_TEASER + """
<!-- 03 RÖVID POZICIONÁLÁS -->
<section class="pad">
  <div class="wrap">
    <div class="sec-head rv" style="max-width:820px;">
      <span class="eyebrow">POZICIONÁLÁS</span>
      <h2>Több mint egy modell-<br>vagy marketingügynökség.</h2>
      <p style="max-width:720px;">A Models on the Move ott kapcsolja össze az üzletet a kreatív világgal, ahol egy kampányhoz, márkához vagy eseményhez nem egyetlen szolgáltatásra, hanem jól összehangolt emberekre van szükség.</p>
      <p style="max-width:720px;">Segítünk megtalálni a megfelelő modelleket és influencereket, felépítjük a kommunikációt, elkészítjük a szükséges fotókat, videókat és digitális felületeket, valamint a teljes produkciót vagy eseményt is koordináljuk.</p>
      <p style="max-width:720px;font-weight:600;color:var(--ivory);">Egyetlen részfeladattal és hosszú távú, teljes körű együttműködéssel is megkereshetsz minket.</p>
      <div class="stat-row rv">
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
    <div class="pillar-grid rv">
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

<!-- 04 TELJES KÖRŰ MARKETINGMENEDZSMENT -->
<section class="pad rule" style="background:linear-gradient(180deg,transparent,rgba(224,90,50,.05),transparent);">
  <div class="wrap">
    <div class="sec-head rv" style="max-width:760px;">
      <span class="eyebrow">TELJES KÖRŰ MARKETINGMENEDZSMENT</span>
      <h2>A külső marketingcsapatod.</h2>
      <p style="font-family:var(--serif);font-size:19px;color:var(--bronze-bright);margin-top:20px;">Nem kell öt különböző szolgáltató. Egy jól összehangolt csapat kell.</p>
      <p style="max-width:680px;">Ha nem külön szolgáltatókat szeretnél koordinálni, a vállalkozásod teljes marketingtevékenységét is ránk bízhatod.</p>
      <p style="max-width:680px;">Stratégiát készítünk, kezeljük a digitális felületeidet, tartalmat gyártunk, fejlesztjük a weboldaladat, optimalizáljuk a keresőben való jelenlétedet, kezeljük a hirdetéseidet, és szükség esetén modelleket, influencereket, fotóst, videóst vagy további kreatív szakembereket vonunk be.</p>
      <p style="max-width:680px;font-weight:700;color:var(--ivory);font-size:16px;">Te a vállalkozásoddal foglalkozol. Mi összehangoljuk a marketingedet.</p>
      <div style="margin-top:34px;">
        <a href="kapcsolat/" class="btn filled magnetic">BESZÉLJÜNK A CÉGEDRŐL</a>
      </div>
    </div>
  </div>
</section>

<!-- 05 HOGYAN DOLGOZUNK -->
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">HOGYAN DOLGOZUNK</span>
      <h2>Egy kapcsolat. A szükséges csapat.<br>Teljes koordináció.</h2>
    </div>
    <div class="process-grid rv">
      <div class="process-step"><span class="idx">01</span><h4>Megismerjük a célt</h4><p>Nem előre gyártott csomagot próbálunk eladni. Először megértjük a márkát, a célközönséget és az üzleti feladatot.</p></div>
      <div class="process-step"><span class="idx">02</span><h4>Összeállítjuk a megoldást</h4><p>Kiválasztjuk a szükséges szolgáltatásokat, szakembereket, modelleket, influencereket és partnereket.</p></div>
      <div class="process-step"><span class="idx">03</span><h4>Megvalósítjuk és koordináljuk</h4><p>Egy kézben tartjuk a kommunikációt, a tartalomgyártást, a digitális felületeket vagy a teljes produkciót.</p></div>
      <div class="process-step"><span class="idx">04</span><h4>Mérünk és továbbfejlesztünk</h4><p>A hosszú távú együttműködéseknél az eredmények alapján folyamatosan javítjuk a rendszert.</p></div>
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
    <div class="audience-row rv">
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
    <div class="sec-head rv" style="max-width:760px;">
      <span class="eyebrow">ESEMÉNYEK ÉS PRODUKCIÓK</span>
      <h2>Egy ötletből teljes élmény.</h2>
      <p style="max-width:680px;">Saját Models on the Move rendezvényeink mellett márkák és vállalkozások eseményeinek, kampányainak és produkcióinak teljes körű megszervezését is vállaljuk.</p>
      <p style="max-width:680px;">Budapesti helyszínekkel, modellekkel, influencerekkel, DJ-kkel, fotósokkal, videósokkal, dekorációs és további kreatív partnerekkel dolgozunk együtt, így a koncepciótól a megvalósításig egy kézben tudjuk koordinálni a projektet.</p>
    </div>
    <div class="audience-row rv" style="margin-bottom:50px;">
      <span class="tag">Márka- és termékbemutatók</span><span class="tag">Étterem- és helyszínnyitók</span>
      <span class="tag">Influencer események</span><span class="tag">Divatbemutatók</span>
      <span class="tag">Kampányfotózások</span><span class="tag">Reklámforgatások</span>
      <span class="tag">Céges rendezvények</span><span class="tag">Egyedi VIP események</span>
    </div>
    <div class="rv" style="text-align:center;padding:50px 0;border-top:1px solid var(--line);">
      <p style="font-family:var(--serif);font-size:clamp(22px,3.2vw,32px);max-width:680px;margin:0 auto 30px;line-height:1.4;">Mondd el, mit szeretnél létrehozni. Mi megtaláljuk hozzá az embereket, a helyszínt és a megoldást.</p>
      <a href="rendezvenyszervezes/" class="btn filled magnetic">TERVEZZÜK MEG EGYÜTT</a>
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
  <div class="blob gold" style="width:420px;height:420px;top:-100px;left:10%;" aria-hidden="true"></div>
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
