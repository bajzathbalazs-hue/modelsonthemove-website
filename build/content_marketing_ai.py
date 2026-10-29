# -*- coding: utf-8 -*-
# Marketing és AI — brief 4.5, betűre pontosan.

def _notice(items):
    rows = "\n".join(
        f'      <p style="margin-top:18px;"><b style="color:var(--bronze-bright);">{lead}</b> {rest}</p>'
        for lead, rest in items
    )
    return f'<div class="wrap" style="max-width:720px;">{rows}\n    </div>'


MARKETING_AI_BODY = """
%%BREADCRUMB%%
<section class="subhero">
  <div class="wrap">
    <span class="eyebrow rv">MARKETING ÉS AI</span>
    <h1 class="rv">Marketing, amelyből bevétel lesz, nem csak elérés.</h1>
    <p class="lead rv">Megtervezzük, felépítjük és hónapról hónapra menedzseljük a marketingedet. Te a vállalkozásodra figyelsz, mi az eredményekre.</p>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KINEK AJÁNLJUK</span></div>
    <ul class="who-for rv-stagger">
      <li><b style="color:var(--ivory);">Cégeknek, amelyek több ajánlatkérést szeretnének,</b> nem csak több lájkot.</li>
      <li><b style="color:var(--ivory);">Webshopoknak,</b> amelyek nyereségesen szeretnék növelni az eladásaikat.</li>
      <li><b style="color:var(--ivory);">Vállalkozásoknak,</b> amelyeknek a hirdetései futnak, de nem hoznak eredményt.</li>
      <li><b style="color:var(--ivory);">Csapatoknak,</b> amelyek AI-jal szeretnének gyorsabban dolgozni.</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="feature-list">
      <div class="feature">
        <div class="num">1</div>
        <div><h3>Alapozás</h3>
          <ul class="bullet-list">
            <li>Teljes átvilágítás: weboldal, hirdetési fiókok, közösségi oldalak</li>
            <li>Piac- és versenytárselemzés</li>
            <li>Célcsoport és vásárlói út feltérképezése</li>
            <li>Ajánlat és fő üzenet kidolgozása: miért pont téged válasszanak</li>
            <li>Csatornastratégia és a költségkeret elosztása</li>
            <li>Mérhető célok (KPI) rögzítése</li>
            <li>Mérés beállítása még az első hirdetés előtt</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">2</div>
        <div><h3>Keresőoptimalizálás (SEO)</h3>
          <ul class="bullet-list">
            <li>Kulcsszókutatás és tartalomstratégia</li>
            <li>Oldalankénti optimalizálás</li>
            <li>Blog és szakmai cikkek írása</li>
            <li>Helyi SEO: Google Cégprofil, térképes találatok</li>
            <li>Értékelésgyűjtési folyamat kialakítása</li>
            <li>Linképítés minőségi oldalakról</li>
            <li>Láthatóság az AI-alapú keresőkben is (ChatGPT, Google AI-áttekintés)</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">3</div>
        <div><h3>Google Ads</h3>
          <ul class="bullet-list">
            <li>Fiókstruktúra felépítése</li>
            <li>Hirdetések a Google-keresésben, a Google Shoppingban, a YouTube-on és a Google teljes hirdetési hálózatán (Performance Max)</li>
            <li>Remarketing: újra elérjük azokat, akik már jártak nálad</li>
            <li>Kizáró kulcsszavak, hogy ne fizess érdektelen keresésekért</li>
            <li>Hirdetésszövegek, kiegészítő elemek (linkek, telefonszám, kiemelések) és a költés okos beállítása</li>
            <li>Folyamatos tesztelés: két változatból mindig a jobbat tartjuk meg (A/B teszt)</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">4</div>
        <div><h3>Meta- és TikTok-hirdetések</h3>
          <ul class="bullet-list">
            <li>Kreatívok tervezése és gyártása</li>
            <li>Közönségépítés: érdeklődési kör, hasonló közönség, remarketing</li>
            <li>Tölcsérépítés: ismertség, megfontolás, vásárlás</li>
            <li>Kreatívtesztelés, a nyertesek skálázása</li>
            <li>Pontos mérés a Conversions API-val</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">5</div>
        <div><h3>Közösségi média</h3>
          <ul class="bullet-list">
            <li>Havi tartalomnaptár</li>
            <li>Posztok, Reels- és TikTok-videók</li>
            <li>Kommentek és üzenetek kezelése</li>
            <li>Influencer-együttműködések szervezése</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">6</div>
        <div><h3>E-mail-marketing</h3>
          <ul class="bullet-list">
            <li>Feliratkozói lista építése</li>
            <li>Hírlevelek</li>
            <li>Automatizmusok: üdvözlő levél, kosárelhagyás, újravásárlás</li>
            <li>Szegmentálás érdeklődés és vásárlás szerint</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">7</div>
        <div><h3>Konverzióoptimalizálás</h3>
          <ul class="bullet-list">
            <li>Hőtérképes elemzés</li>
            <li>Landing oldalak és űrlapok tesztelése és javítása</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">8</div>
        <div><h3>Riport és kapcsolattartás</h3>
          <ul class="bullet-list">
            <li>Érthető havi riport szakzsargon nélkül</li>
            <li>Havi egyeztetés</li>
            <li>Negyedéves stratégiai felülvizsgálat</li>
            <li>Élő riportfelület, amelyet bármikor megnézhetsz</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">AMIRE A LEGTÖBBEN NEM GONDOLNAK</span></div>
""" + _notice([
    ("A hirdetési fiók legyen a tiéd.", "Nálunk minden fiók a te nevedre szól. Ha egyszer továbblépsz, az adataid és az eredményeid veled maradnak. [Tulajdonosi jóváhagyásra vár.]"),
    ("A több elérés nem feltétlenül jelent több vevőt.", "Nem a megtekintéseket optimalizáljuk, hanem az ajánlatkéréseket és az eladásokat."),
    ("A hirdetés csak annyit ér, amennyit az oldal.", "Ha a landing oldal gyenge, a legjobb kampány is elfolyatja a pénzt. Ezért mindkettőt egy kézben tartjuk."),
    ("A kreatív kifárad.", "Ugyanaz a hirdetés néhány hét után veszít a hatásából, ezért folyamatosan újat tesztelünk."),
]) + """
  </div>
</section>

<!-- AI ÉS AUTOMATIZÁCIÓ CÉGEKNEK -->
<section class="subhero" style="padding-top:90px;">
  <div class="wrap">
    <span class="eyebrow rv">AI ÉS AUTOMATIZÁCIÓ CÉGEKNEK</span>
    <h1 class="rv" style="font-size:clamp(26px,4vw,48px);">Szakmai tapasztalat és mesterséges intelligencia, egy csapatban.</h1>
    <p class="lead rv">Megmutatjuk, hogyan dolgozhat helyetted az AI, vagy beállítjuk úgy, hogy neked már csak használnod kelljen.</p>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="feature-list">
      <div class="feature">
        <div class="num">01</div>
        <div><h3>AI-oktatás cégeknek</h3>
          <ul class="bullet-list">
            <li>Gyakorlati képzés a csapatodnak, a saját munkafolyamataitokra szabva</li>
            <li>Hatékony utasításírás (promptolás) a mindennapi feladatokhoz</li>
            <li>Biztonságos használat: milyen adat adható meg, és milyen nem</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">02</div>
        <div><h3>Személyre szabott AI-megoldások</h3>
          <ul class="bullet-list">
            <li>Saját céges AI-asszisztens a cégetek tudásával és hangnemével</li>
            <li>Kész sablonok ajánlatíráshoz, e-mailekhez, szövegekhez és riportokhoz</li>
            <li>Mi beállítjuk, ti csak használjátok</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">03</div>
        <div><h3>Automatizációk</h3>
          <ul class="bullet-list">
            <li>Az ajánlatkérések automatikus rendezése és továbbítása</li>
            <li>Ismétlődő e-mailek, emlékeztetők és visszaigazolások</li>
            <li>Riportok és kimutatások automatikus elkészítése</li>
            <li>Közösségimédia-posztok ütemezése</li>
            <li>A rendszereid összekötése, hogy ne kelljen kézzel adatot másolni</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">AMIRE A LEGTÖBBEN NEM GONDOLNAK</span></div>
""" + _notice([
    ("Az AI nem helyettesíti a szakértelmet, hanem megsokszorozza.", "Jó irányítással napi órákat spórol, rossz irányítással hibát gyárt."),
]) + """
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Nézzük meg, hol hagysz pénzt az asztalon.</h2>
    <div class="ctas"><a href="../kapcsolat/" class="btn filled magnetic">INGYENES KONZULTÁCIÓT KÉREK</a></div>
  </div>
</section>
"""
