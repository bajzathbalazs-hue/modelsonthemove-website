# -*- coding: utf-8 -*-
from content_events import ACTIVE_EVENT, PAST_EVENTS
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
# Jelenleg nem jelenik meg a főoldalon (ld. 3-pilléres átépítés terve) — a
# generálás megmarad, ha később egy pillér-oldalon újra bevetnénk.
HOME_FAQ_HTML, HOME_FAQ_JSONLD = faq_list(HOME_FAQ)

if ACTIVE_EVENT:
    _event_badge = f"""    <a href="esemenyek/" class="hero-current">
      <span class="dot"></span>
      <span>KÖVETKEZŐ ESEMÉNYÜNK</span>
      <b>{ACTIVE_EVENT['name']} — {ACTIVE_EVENT['date_label']} · {ACTIVE_EVENT['venue']}</b>
      <span class="arrow">→</span>
    </a>
"""
else:
    _event_badge = ""

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
    <h1 class="hero-tag" style="font-family:var(--serif);font-size:clamp(20px,2.6vw,30px);max-width:640px;color:var(--ivory);line-height:1.35;margin-top:22px;">Buli- és rendezvényszervezés. Weboldal- és marketingmegoldások.</h1>
    <p class="hero-tag">Teljes körű eseményszervezés, weboldal- és webshop-tervezés, komplex céges kampányok és teljes marketing menedzsment — modellekkel és influencerekkel kiegészítve, egy összehangolt csapattól.</p>
    <div class="hero-ctas">
      <a href="kapcsolat/" class="btn filled magnetic">BESZÉLJÜNK A CÉGEDRŐL</a>
    </div>
""" + _event_badge + """  </div>
</section>

<!-- 02 HÁROM PILLÉR -->
<section class="pad rule" id="pillars" style="padding-top:100px;">
  <div class="wrap">
    <div class="pillar-grid rv-stagger">
      <div class="pillar-card glow-card">
        <div class="plate photo dim-top" style="position:absolute;inset:0;z-index:-1;opacity:.4;background-image:url('assets/vibe-mainroom.jpg');"></div>
        <span class="n">01</span>
        <h3>Események</h3>
        <p>Válogatott vendégkör, kiemelt budapesti helyszínek, esték, amelyekről még napokig beszélnek.</p>
        <a href="esemenyek/" class="go">JEGYVÁSÁRLÁS →</a>
      </div>
      <div class="pillar-card glow-card">
        <div class="plate photo dim-top" style="position:absolute;inset:0;z-index:-1;opacity:.4;background-image:url('assets/svc-marketing-ugynokseg.png');"></div>
        <span class="n">02</span>
        <h3>Web és marketing</h3>
        <p>Weboldalak és marketingstratégia ugyanazzal a gondossággal, amellyel egy estét felépítünk.</p>
        <a href="marketing-ugynokseg/" class="go">AJÁNLATKÉRÉS →</a>
      </div>
      <div class="pillar-card glow-card">
        <div class="plate photo dim-top" style="position:absolute;inset:0;z-index:-1;opacity:.4;background-image:url('assets/svc-influencer-marketing.png');"></div>
        <span class="n">03</span>
        <h3>Influencer és tartalom</h3>
        <p>Hiteles arcok, profi fotó- és videótartalom: a márka története úgy, ahogyan megérdemli.</p>
        <a href="modellugynokseg/" class="go">EGYÜTTMŰKÖDÉS INDÍTÁSA →</a>
      </div>
    </div>
  </div>
</section>

<!-- 03 BIZALMI SÁV -->
<section class="pad rule">
  <div class="wrap">
    <div class="stat-row rv-stagger" style="margin-top:0;">
      <div><b>10</b><span>GONDOZOTT WEBOLDAL</span></div>
      <div><b>30–40</b><span>INFLUENCER ÉS MODELL PARTNER</span></div>
      <div><b>""" + str(len(PAST_EVENTS)) + """</b><span>MEGRENDEZETT ESEMÉNY</span></div>
      <div><b>~334 000</b><span>MEGTEKINTÉS EGY ESEMÉNY-KAMPÁNYBAN</span></div>
      <div><b>~160 000</b><span>ELÉRT EMBER</span></div>
    </div>
  </div>
</section>

<!-- 04 VÁLOGATOTT MUNKÁK -->
<section class="pad rule" style="padding-bottom:70px;">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">VÁLOGATOTT MUNKÁINK</span><h2>Egy est, egy weboldal, egy kampány — ugyanazzal a mércével.</h2></div>
  </div>
  <div class="hscroll rv-stagger">
    <a class="gcard wide" href="esemenyek/dubai-style/">
      <div class="plate photo grain" style="background-image:url('assets/vibe-mainroom.jpg');"></div>
      <div class="meta"><h4>Dubai Style</h4><span class="loc">Esemény · VIBE Budapest</span></div>
    </a>
    <a class="gcard" href="esemenyek/myrazs-fashion-show/">
      <div class="plate photo grain" style="background-image:url('assets/ig-myrazs-recap.jpg');"></div>
      <div class="meta"><h4>Myrázs Divatbemutató</h4><span class="loc">Esemény · MOM Leroy Bistro</span></div>
    </a>
    <a class="gcard" href="esemenyek/dubai-style/">
      <div class="plate photo grain" style="background-image:url('assets/vibe-redroom-group.jpg');background-position:center 15%;"></div>
      <div class="meta"><h4>Dubai Style</h4><span class="loc">Esemény · VIBE Budapest</span></div>
    </a>
    <a class="gcard" href="esemenyek/dubai-style/">
      <div class="plate photo grain" style="background-image:url('assets/vibe-bartrio-final.jpg');background-position:center 30%;"></div>
      <div class="meta"><h4>Dubai Style</h4><span class="loc">Esemény · VIBE Budapest</span></div>
    </a>
  </div>
  <div class="wrap">
    <p style="margin-top:24px;font-size:12.5px;color:var(--ivory-dimmer);">Weboldal- és kampány-anyagokkal hamarosan bővül a válogatás.</p>
  </div>
</section>

<!-- 05 RÓLUNK RÖVIDEN -->
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">AKIK MÖGÖTTE ÁLLNAK</span><h2>Két ember, egy közös vízió.</h2></div>
    <div class="model-block rv" style="align-items:start;">
      <div>
        <h3 style="font-family:var(--serif);font-size:19px;color:var(--bronze-bright);">Molnár Mira</h3>
        <p style="margin-top:10px;font-size:14.5px;line-height:1.8;color:var(--ivory-dim);">Modellként és a hazai influencer-világ aktív szereplőjeként fogja össze a modellekkel és kreatív együttműködésekkel kapcsolatos területet.</p>
      </div>
      <div>
        <h3 style="font-family:var(--serif);font-size:19px;color:var(--bronze-bright);">Bajzáth Balázs</h3>
        <p style="margin-top:10px;font-size:14.5px;line-height:1.8;color:var(--ivory-dim);">A Models on the Move üzleti és stratégiai oldaláért felel — a vállalati kapcsolatoktól a digitális megoldásokig ő koordinálja a megvalósítást.</p>
      </div>
    </div>
    <div style="margin-top:34px;"><a href="rolunk/" class="btn magnetic">RÓLUNK →</a></div>
  </div>
</section>

<!-- 06 KEZDJÜK EL — beágyazott rövid kapcsolat-űrlap -->
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KAPCSOLAT</span><h2>Kezdjük el.</h2>
      <p>Írd meg, miben segíthetünk — rövid időn belül személyesen jelentkezünk.</p>
    </div>
    <form class="form-panel rv" id="homeForm" name="kapcsolat-rovid" data-netlify="true" data-netlify-honeypot="company" data-motm-form data-msg-id="homeMsg" data-event="home_contact_submit" novalidate style="max-width:640px;margin:0 auto;">
      <input type="hidden" name="form-name" value="kapcsolat-rovid">
      <input type="hidden" name="page_url" value="">
      <input type="hidden" name="referrer_url" value="">
      <div class="hp-field" aria-hidden="true"><label>Cégnév (ne töltsd ki)</label><input type="text" name="company" tabindex="-1" autocomplete="off"></div>
      <div class="row2">
        <div class="field"><label for="h-name">NÉV</label><input id="h-name" name="name" type="text" required></div>
        <div class="field"><label for="h-email">E-MAIL</label><input id="h-email" name="email" type="email" required></div>
      </div>
      <div class="row2">
        <div class="field"><label for="h-phone">TELEFONSZÁM (OPCIONÁLIS)</label><input id="h-phone" name="phone" type="tel"></div>
        <div class="field"><label for="h-topic">MIBEN SEGÍTHETÜNK?</label>
          <select id="h-topic" name="topic" required>
            <option value="" disabled selected>Válassz...</option>
            <option value="Esemény és asztalfoglalás">Esemény és asztalfoglalás</option>
            <option value="Web és marketing">Web és marketing</option>
            <option value="Influencer és tartalom">Influencer és tartalom</option>
          </select>
        </div>
      </div>
      <div class="field"><label for="h-msg">ÜZENET</label><textarea id="h-msg" name="message" required></textarea></div>
      <label class="check"><input type="checkbox" name="consent" required> Elfogadom az Adatvédelmi tájékoztatót.</label>
      <div class="submit-row">
        <button type="submit" class="btn filled magnetic">ÜZENET KÜLDÉSE</button>
      </div>
      <div class="form-msg" id="homeMsg"><h4>KÖSZÖNJÜK.</h4><p>Hamarosan jelentkezünk.</p></div>
    </form>
  </div>
</section>
"""
