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
    <div class="sec-head rv" style="margin-bottom:40px;">
      <p>Nem egy hosszú szolgáltatáslistát adunk át, hanem egy csapatot, amelyik ezt mind elvégzi helyetted — a kezdeti alapoktól a havi riportig.</p>
    </div>
    <div class="feature-list">
      <div class="feature">
        <div class="num">1</div>
        <div><h3>Alapozás</h3>
          <ul class="bullet-list">
            <li>Átvilágítjuk a weboldaladat, a hirdetési fiókjaidat és a közösségi oldalaidat</li>
            <li>Kidolgozzuk, miért pont téged válasszanak a versenytársaid helyett</li>
            <li>Mérhető célokat tűzünk ki, és a mérést még az első hirdetés előtt bekötjük</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">2</div>
        <div><h3>Keresőoptimalizálás (SEO)</h3>
          <ul class="bullet-list">
            <li>Kulcsszókutatás és tartalomstratégia, hogy a megfelelő keresésekre találjanak rád</li>
            <li>Helyi SEO: Google Cégprofil, térképes találatok, értékelésgyűjtés</li>
            <li>Megjelenés az AI-alapú keresőkben is (ChatGPT, Google AI-áttekintés)</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">3</div>
        <div><h3>Google Ads</h3>
          <ul class="bullet-list">
            <li>Hirdetések a Google-keresésben, a Shoppingban, a YouTube-on és a Google teljes hálózatán</li>
            <li>Remarketing, hogy újra elérjük azokat, akik már jártak nálad</li>
            <li>Folyamatos tesztelés: két változatból mindig a jobbat tartjuk meg</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">4</div>
        <div><h3>Meta- és TikTok-hirdetések</h3>
          <ul class="bullet-list">
            <li>Kreatívok tervezése és gyártása</li>
            <li>Közönségépítés: érdeklődési kör, hasonló közönség, remarketing</li>
            <li>Pontosabb mérés, amely a böngészők korlátozásai mellett is működik</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">5</div>
        <div><h3>Közösségi média</h3>
          <ul class="bullet-list">
            <li>Havi tartalomnaptár, posztok, Reels- és TikTok-videók</li>
            <li>Kommentek és üzenetek kezelése</li>
            <li>Influencer-együttműködések szervezése</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">6</div>
        <div><h3>E-mail-marketing</h3>
          <ul class="bullet-list">
            <li>Feliratkozói lista építése és hírlevelek</li>
            <li>Automatizmusok: üdvözlő levél, kosárelhagyás, újravásárlás</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">7</div>
        <div><h3>Konverzióoptimalizálás</h3>
          <ul class="bullet-list">
            <li>Hőtérképes elemzés, hogy lássuk, hol akadnak el a látogatók</li>
            <li>Landing oldalak és űrlapok folyamatos tesztelése és javítása</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">8</div>
        <div><h3>Riport és kapcsolattartás</h3>
          <ul class="bullet-list">
            <li>Érthető havi riport, szakzsargon nélkül, havi egyeztetéssel</li>
            <li>Élő riportfelület, amelyet bármikor megnézhetsz</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">HOGYAN DOLGOZUNK</span></div>
    <div class="phase-table-wrap rv">
      <table class="phase-table">
        <tr><th>Fázis</th><th>Mit csinálunk</th><th>Mit kapsz</th></tr>
        <tr><td>1. Átvilágítás</td><td>Megnézzük, mi működik és mi nem.</td><td>Írásos átvilágítás konkrét javaslatokkal</td></tr>
        <tr><td>2. Stratégia</td><td>Kijelöljük a célokat, a csatornákat és a keretet.</td><td>Marketingterv mérhető célokkal, jóváhagyásra</td></tr>
        <tr><td>3. Beállítás</td><td>Bekötjük a mérést, felépítjük a kampányokat.</td><td>Működő mérés és kampányok</td></tr>
        <tr><td>4. Futtatás és optimalizálás</td><td>Hetente figyelünk, tesztelünk és javítunk.</td><td>Folyamatosan javuló eredmények</td></tr>
        <tr><td>5. Riport</td><td>Havonta közösen értékelünk.</td><td>Érthető havi riport és következő lépések</td></tr>
      </table>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">EGYÜTTMŰKÖDÉSI FORMÁK</span></div>
    <ul class="bullet-list" style="margin:0 auto;">
      <li><b style="color:var(--ivory);">Stratégiai csomag:</b> átvilágítás és marketingterv, amelyet a saját csapatod valósít meg.</li>
      <li><b style="color:var(--ivory);">Havi partnerség:</b> folyamatos menedzsment, havi díjért.</li>
      <li><b style="color:var(--ivory);">Kampány:</b> egy termék, esemény vagy szezon köré épített, meghatározott idejű kampány.</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">AMIRE A LEGTÖBBEN NEM GONDOLNAK</span></div>
""" + _notice([
    ("A hirdetési fiók legyen a tiéd.", "Nálunk minden fiók a te nevedre szól. Ha egyszer továbblépsz, az adataid és az eredményeid veled maradnak."),
    ("A több elérés nem feltétlenül jelent több vevőt.", "Nem a megtekintéseket optimalizáljuk, hanem az ajánlatkéréseket és az eladásokat."),
    ("A hirdetés csak annyit ér, amennyit az oldal.", "Ha a landing oldal gyenge, a legjobb kampány is elpazarolja a költségkeretet. Ezért mindkettőt egy kézben tartjuk."),
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
            <li>Gyakorlati képzés a csapatodnak, a cégednél használt munkafolyamatokra szabva</li>
            <li>Hatékony utasításírás (promptolás) a mindennapi feladatokhoz</li>
            <li>Biztonságos használat: milyen adat adható meg, és milyen nem</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">02</div>
        <div><h3>Személyre szabott AI-megoldások</h3>
          <ul class="bullet-list">
            <li>Saját céges AI-asszisztens a céged tudásával és hangnemével</li>
            <li>Kész sablonok ajánlatíráshoz, e-mailekhez, szövegekhez és riportokhoz</li>
            <li>Mi beállítjuk, neked már csak használnod kell.</li>
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
    ("A céges adat nem való bármelyik AI-ba.", "Szabályok nélkül a munkatársak akaratlanul is bizalmas információt adhatnak meg. Ezt az oktatás és a belső szabályzat előzi meg."),
]) + """
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KINEK NEM AJÁNLJUK</span></div>
    <div class="who-not rv">
      <p>Akkor valószínűleg nem mi vagyunk a jó választás, ha:</p>
      <ul>
        <li>egy hónap alatt garantált eredményt vársz, mérés és tesztelés nélkül;</li>
        <li>csak lájkokat és követőket szeretnél, üzleti cél nélkül.</li>
      </ul>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">GYAKORI KÉRDÉSEK</span></div>
    <div class="faq-list">
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Mennyi idő alatt látszik eredmény?<span class="plus"></span></button>
        <div class="faq-a"><p>A fizetett hirdetéseknél általában néhány héten belül, a keresőoptimalizálásnál jellemzően néhány hónap alatt.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">A hirdetési költség benne van a díjatokban?<span class="plus"></span></button>
        <div class="faq-a"><p>Nem. A hirdetési költséget közvetlenül a platformoknak fizeted, a mi díjunk ettől független.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Mennyi időre szól az együttműködés?<span class="plus"></span></button>
        <div class="faq-a"><p>Legalább három hónapra, mert ennyi idő kell ahhoz, hogy a hirdetések és a mérés beérjenek, és valós eredményt láss.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Ki látja az adatokat?<span class="plus"></span></button>
        <div class="faq-a"><p>Te. Minden fiók és riport a te hozzáférésedben van.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">EZ IS ÉRDEKELHET</span></div>
    <div class="cross-links rv-stagger">
      <a class="cross-link" href="../arculat-es-webfejlesztes/"><span class="k">Arculat és webfejlesztés</span><p>Egy oldal, amely a hirdetésekből érkező látogatókat ügyféllé teszi.</p></a>
      <a class="cross-link" href="../influencer-egyuttmukodes/"><span class="k">Influencer-együttműködés</span><p>Hiteles arcok a kampányaidhoz.</p></a>
    </div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Nézzük meg, hol vész el a bevételed.</h2>
    <div class="ctas"><a href="../kapcsolat/" class="btn filled magnetic">Ingyenes konzultációt kérek</a></div>
  </div>
</section>
"""
