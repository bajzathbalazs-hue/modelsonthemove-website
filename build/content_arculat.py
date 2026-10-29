# -*- coding: utf-8 -*-
# Arculat és webfejlesztés — brief 4.4, betűre pontosan.

def _notice(items):
    """'Amire a legtöbben nem gondolnak' blokk — (lead, rest) tuple-lista."""
    rows = "\n".join(
        f'      <p style="margin-top:18px;"><b style="color:var(--bronze-bright);">{lead}</b> {rest}</p>'
        for lead, rest in items
    )
    return f'<div class="wrap" style="max-width:720px;">{rows}\n    </div>'


ARCULAT_BODY = """
%%BREADCRUMB%%
<div class="wrap" style="text-align:center;padding-top:10px;">
  <nav class="svc-tabs rv" style="margin:0 auto 20px;">
    <a href="#arculat">Arculat</a><a href="#weboldal">Weboldal</a><a href="#webshop">Webshop</a><a href="#folyamat">Folyamat</a><a href="#gyik">GYIK</a>
  </nav>
</div>
<section class="subhero" id="arculat">
  <div class="wrap">
    <span class="eyebrow rv">ARCULAT ÉS WEBFEJLESZTÉS</span>
    <h1 class="rv">A márkádtól a weboldaladig, egy kézből.</h1>
    <p class="lead rv">Megtervezzük, hogyan nézzen ki a márkád, és felépítjük azt az oldalt, amelyből ügyfelek lesznek. Az első ötlettől az élesítésig mindent intézünk.</p>
    <div class="ctas rv"><a href="../kapcsolat/" class="btn filled magnetic">Ingyenes konzultációt kérek</a></div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KINEK AJÁNLJUK</span></div>
    <ul class="who-for rv-stagger">
      <li><b style="color:var(--ivory);">Induló vállalkozásoknak,</b> amelyek az első naptól profi megjelenést szeretnének.</li>
      <li><b style="color:var(--ivory);">Működő cégeknek,</b> amelyeknek az arculata vagy a weboldala már nem tükrözi, hol tartanak.</li>
      <li><b style="color:var(--ivory);">Webshopoknak,</b> amelyek több rendelést és kevesebb kézi munkát szeretnének.</li>
      <li><b style="color:var(--ivory);">Márkáknak,</b> amelyek egy termékhez vagy kampányhoz keresnek gyors, célzott oldalt.</li>
    </ul>
  </div>
</section>

<section class="subhero" style="padding-top:40px;padding-bottom:50px;">
  <div class="wrap">
    <span class="eyebrow rv">A) ARCULATTERVEZÉS</span>
    <h1 class="rv" style="font-size:clamp(28px,4.6vw,56px);">Egy márka, amelyet első pillantásra felismernek.</h1>
    <p class="lead rv">A pozicionálástól a céges ruházatig megtervezzük a teljes arculatodat, hogy minden felületen egységesen és prémium módon jelenj meg.</p>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="feature-list">
      <div class="feature">
        <div class="num">01</div>
        <div><h3>Márkastratégia</h3>
          <ul class="bullet-list">
            <li>Értékek, pozicionálás és megkülönböztető üzenet</li>
            <li>Versenytársak és piac vizuális elemzése</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">02</div>
        <div><h3>Verbális arculat</h3>
          <ul class="bullet-list">
            <li>Névötletek, ha új márkát indítasz</li>
            <li>Szlogen és kulcsüzenetek</li>
            <li>A márka hangneme: hogyan szólsz az ügyfeleidhez</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">03</div>
        <div><h3>Vizuális arculat</h3>
          <ul class="bullet-list">
            <li>Logó: fő változat, egyszerűsített változat, ikon, fekete-fehér verzió</li>
            <li>Színpaletta nyomdai és digitális színkódokkal</li>
            <li>Betűtípusok és tipográfiai rendszer</li>
            <li>Képi világ, ikonok, grafikai elemek</li>
            <li>Arculati kézikönyv, hogy bárki helyesen használja a márkádat</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">04</div>
        <div><h3>Nyomdai és irodai anyagok</h3>
          <ul class="bullet-list">
            <li>Névjegykártya, levélpapír, boríték</li>
            <li>Szórólap, plakát, roll-up</li>
            <li>Katalógus és termékprospektus</li>
            <li>Nyomdai előkészítés és egyeztetés a nyomdával</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">05</div>
        <div><h3>Digitális anyagok</h3>
          <ul class="bullet-list">
            <li>E-mail-aláírás</li>
            <li>Prezentációsablon</li>
            <li>Közösségimédia-sablonok és borítóképek</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">06</div>
        <div><h3>Márkajelenlét a valóságban</h3>
          <ul class="bullet-list">
            <li>Céges ruházat: póló, pulóver, munkaruha</li>
            <li>Autódekoráció és matrica</li>
            <li>Cégtábla és irodai dekoráció</li>
            <li>Csomagolás és címke</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">07</div>
        <div><h3>Bevezetés</h3>
          <ul class="bullet-list">
            <li>Bevezetési terv: melyik felületen mikor cseréljük az új arculatra</li>
            <li>Átadás minden szükséges fájlformátumban, rendezett mappaszerkezetben</li>
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
    ("Egy logó önmagában még nem arculat.", "Szabályok nélkül minden plakát, poszt és névjegy kicsit másképp néz ki, és a márka szétesik."),
    ("A nyomdai és a digitális szín nem ugyanaz.", "Ami a képernyőn tökéletes, nyomtatva fakó lehet, ha a fájlt nem megfelelően készítik elő."),
    ("Egy név lehet foglalt.", "Új márkanévnél érdemes még a tervezés előtt ellenőrizni a domaint, a közösségimédia-neveket és a védjegyet."),
]) + """
  </div>
</section>

<!-- B) WEBFEJLESZTÉS -->
<section class="subhero" id="weboldal" style="padding-top:90px;">
  <div class="wrap">
    <span class="eyebrow rv">B) WEBFEJLESZTÉS</span>
    <h1 class="rv" style="font-size:clamp(28px,4.6vw,56px);">Weboldal, amely dolgozik helyetted.</h1>
    <p class="lead rv">Gyors, elegáns és mérhető oldalakat építünk, amelyekből a látogatóid ügyfelek lesznek.</p>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MIT KÉSZÍTÜNK</span></div>
    <div class="process-grid rv-stagger">
      <div class="process-step"><h4>Bemutatkozó oldal</h4><p>Megmutatja, ki vagy, és miért érdemes téged választani.</p></div>
      <div class="process-step"><h4>Landing oldal</h4><p>Egyetlen termékre, szolgáltatásra vagy kampányra fókuszál, egyetlen céllal.</p></div>
      <div class="process-step"><h4>Webshop</h4><p>A termékfeltöltéstől a kifizetett rendelésig minden működik.</p></div>
      <div class="process-step"><h4>Megújítás</h4><p>A meglévő oldaladat gyorsabbá, szebbé és eredményesebbé tesszük.</p></div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv">
      <h2 style="font-size:clamp(22px,3vw,32px);">Te elmondod, mit szeretnél. Mi minden mást elintézünk.</h2>
      <p>Egy profi weboldal mögött több tucat lépés áll. Ezeket mind elvégezzük, hogy neked ne kelljen.</p>
    </div>
    <div class="feature-list">
      <div class="feature">
        <div class="num">1</div>
        <div><h3>Stratégia és tervezés</h3>
          <ul class="bullet-list">
            <li>Célok és mérhető eredmények meghatározása</li>
            <li>Célcsoport és vásárlói típusok feltérképezése</li>
            <li>Versenytárselemzés</li>
            <li>Kulcsszókutatás még a tervezés előtt, hogy az oldal szerkezete a keresésekre épüljön</li>
            <li>Oldaltérkép és felhasználói út megtervezése</li>
            <li>Drótváz (az oldal vázlata), majd látványterv, végül kattintható prototípus jóváhagyásra</li>
            <li>Egységes designrendszer: színek, betűtípusok, gombok, elemek</li>
            <li>Mobilra tervezés elsőként, mert a látogatók többsége telefonról érkezik</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">2</div>
        <div><h3>Tartalom</h3>
          <ul class="bullet-list">
            <li>Értékesítő és keresőbarát szövegírás</li>
            <li>Apró szövegek is: gombok, hibaüzenetek, visszaigazolások</li>
            <li>Fotózás és videó, igény szerint</li>
            <li>Képek tömörítése modern formátumba, hogy gyorsan töltsenek</li>
            <li>Képleírások a keresők és a látássérült látogatók számára</li>
            <li>Egyedi köszönőoldal és hibaoldal (404)</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">3</div>
        <div><h3>Fejlesztés és sebesség</h3>
          <ul class="bullet-list">
            <li>Minden képernyőméretre igazodó megjelenés</li>
            <li>Gyors betöltés a Google sebességmutatói szerint (Core Web Vitals)</li>
            <li>Technikai gyorsítás: a képek csak akkor töltődnek be, amikor a látogató odagörget, és az oldal a hozzá legközelebbi szerverről érkezik (CDN)</li>
            <li>Akadálymentesség, hogy mindenki használni tudja az oldalt (WCAG nemzetközi szabvány)</li>
            <li>Tesztelés minden fontosabb böngészőben, telefonon, tableten és számítógépen</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">4</div>
        <div><h3>Biztonság</h3>
          <ul class="bullet-list">
            <li>SSL-tanúsítvány (a lakat a címsorban)</li>
            <li>Biztonsági beállítások a támadások ellen</li>
            <li>Spamvédelem az űrlapokon</li>
            <li>Automatikus biztonsági mentés</li>
            <li>A céges e-mail-cím hitelesítése, hogy a leveleid ne a spam mappában landoljanak</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">5</div>
        <div><h3>Keresőoptimalizálás (technikai SEO)</h3>
          <ul class="bullet-list">
            <li>Egyedi oldalcímek és leírások minden aloldalhoz</li>
            <li>Beszédes, tiszta webcímek</li>
            <li>Átirányítások a régi oldalról, hogy a meglévő helyezések ne vesszenek el</li>
            <li>Beállítások, amelyekből a Google tudja, mely oldalaidat vegye fel a találatai közé, és melyik változatot tekintse elsődlegesnek (sitemap, robots.txt, kanonikus címek)</li>
            <li>Strukturált adatok, hogy a Google gazdagabb találatként mutassa az oldaladat (értékelések, árak, események, kérdések)</li>
            <li>Megosztási előnézet: szép kép és cím, ha valaki Facebookon vagy Messengeren továbbküldi az oldalt</li>
            <li>Google Search Console és Bing Webmaster Tools beállítása, indexelés ellenőrzése</li>
            <li>Google Cégprofil beállítása vagy rendbetétele</li>
            <li>Belső linkstruktúra kialakítása</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">6</div>
        <div><h3>Mérés és analitika</h3>
          <ul class="bullet-list">
            <li>GA4 és Google Tag Manager bekötése</li>
            <li>Hozzájárulási mód (Consent Mode v2), hogy a mérés a GDPR-nak megfelelően működjön</li>
            <li>Konverziók beállítása: űrlapküldés, telefonhívás, vásárlás</li>
            <li>A Facebook-, az Instagram- és a TikTok-hirdetések mérőkódjainak bekötése (Meta Pixel, Conversions API, TikTok Pixel)</li>
            <li>A Google-hirdetések eredményeinek mérése (Google Ads konverziókövetés)</li>
            <li>Egységes linkjelölés (UTM), hogy minden kampány eredménye külön látsszon</li>
            <li>Hőtérkép és felvétel arról, hol kattintanak és hol akadnak el a látogatók</li>
            <li>Áttekinthető, élő riportfelület (dashboard)</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">7</div>
        <div><h3>Jogi biztonság (ügyvéd bevonásával)</h3>
          <ul class="bullet-list">
            <li>Általános szerződési feltételek (ÁSZF)</li>
            <li>Adatkezelési tájékoztató a GDPR szerint</li>
            <li>Sütitájékoztató és sütikezelő sáv</li>
            <li>Impresszum a kötelező szolgáltatói adatokkal</li>
            <li>Webshopnál: elállási tájékoztató és nyilatkozatminta, panaszkezelési és fogyasztói tájékoztatók</li>
          </ul>
        </div>
      </div>
      <div class="feature" id="webshop">
        <div class="num">8</div>
        <div><h3>Webshop</h3>
          <ul class="bullet-list">
            <li>Termékfeltöltés változatokkal, kategóriákkal és szűrőkkel</li>
            <li>Készletkezelés</li>
            <li>Online fizetés: bankkártya, Apple Pay, Google Pay</li>
            <li>Szállítás: futár, csomagautomata, személyes átvétel</li>
            <li>Számlázóprogram-bekötés, automatikus számla</li>
            <li>Automatikus e-mailek: visszaigazolás, szállítás, kosárelhagyás</li>
            <li>Kuponok és akciók</li>
            <li>Termékfeed a Google Shoppinghoz és a Meta-katalógushoz</li>
            <li>ÁFA- és szállítási díjak helyes beállítása</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">9</div>
        <div><h3>Élesítés és átadás</h3>
          <ul class="bullet-list">
            <li>Domain és tárhely intézése, DNS-beállítások</li>
            <li>Külön tesztkörnyezet, hogy az élő oldal soha ne álljon le</li>
            <li>Élesítés előtti ellenőrzőlista</li>
            <li>Átadás, betanítás és rövid használati útmutató</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">10</div>
        <div><h3>Üzemeltetés</h3>
          <ul class="bullet-list">
            <li>Rendszeres frissítések és biztonsági mentések</li>
            <li>Folyamatos elérhetőségfigyelés</li>
            <li>Havi teljesítményjelentés</li>
            <li>Kisebb módosítások menet közben</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule" id="folyamat">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">HOGYAN DOLGOZUNK</span></div>
    <div class="phase-table-wrap rv">
      <table class="phase-table">
        <tr><th>Fázis</th><th>Mit csinálunk</th><th>Mit kapsz</th><th>Jóváhagyás</th></tr>
        <tr><td>1. Feltárás</td><td>Megismerjük a célodat, a közönségedet és a versenytársaidat.</td><td>Írásos projektterv: célok, oldaltérkép, funkciólista, ütemezés</td><td class="check">✓</td></tr>
        <tr><td>2. Tervezés</td><td>Felépítjük a szerkezetet és a látványt.</td><td>Drótváz, látványterv, kattintható prototípus</td><td class="check">✓</td></tr>
        <tr><td>3. Fejlesztés</td><td>Megépítjük az oldalt, a szövegeket és a méréseket.</td><td>Működő tesztoldal, amelyet bármikor megnézhetsz</td><td class="check">✓</td></tr>
        <tr><td>4. Tesztelés és élesítés</td><td>Minden eszközön és böngészőben ellenőrizzük, majd élesítjük.</td><td>Élő oldal, bekötött mérés, átadási útmutató</td><td class="check">✓</td></tr>
        <tr><td>5. Utánkövetés</td><td>Az első hónapokban figyeljük az eredményeket, és finomhangolunk.</td><td>Teljesítményjelentés és javaslatok</td><td class="check">–</td></tr>
      </table>
    </div>
    <p style="margin-top:22px;text-align:center;font-size:13px;color:var(--ivory-dimmer);font-style:italic;">Minden fázis végén megmutatjuk, mi készült el. Csak a jóváhagyásod után lépünk tovább, így a végeredmény nem érhet meglepetésként.</p>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">EGYÜTTMŰKÖDÉSI FORMÁK</span></div>
    <ul class="bullet-list" style="margin:0 auto;">
      <li><b style="color:var(--ivory);">Egyszeri projekt:</b> arculat, weboldal vagy webshop, rögzített tartalommal és határidővel.</li>
      <li><b style="color:var(--ivory);">Projekt és havi üzemeltetés:</b> elkészítjük, majd havi díjért karbantartjuk és továbbfejlesztjük.</li>
      <li><b style="color:var(--ivory);">Megújítás és audit:</b> átvizsgáljuk a meglévő oldaladat, és javítjuk, ami visszafogja.</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MIÉRT VELÜNK</span></div>
    <ul class="bullet-list" style="margin:0 auto;">
      <li><b style="color:var(--ivory);">Egy kapcsolattartó:</b> nem kell öt embernek elmagyaráznod ugyanazt.</li>
      <li><b style="color:var(--ivory);">Minden egy kézben:</b> arculat, design, fejlesztés, szöveg, fotó és jogi háttér.</li>
      <li><b style="color:var(--ivory);">Mérhető eredmény:</b> pontosan látod, honnan érkeznek az ügyfeleid.</li>
      <li><b style="color:var(--ivory);">Érthető nyelv:</b> szakzsargon nélkül magyarázunk el mindent.</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">AMIRE A LEGTÖBBEN NEM GONDOLNAK</span></div>
""" + _notice([
    ("Egy lassú oldal ügyfelet veszít.", "Ha néhány másodpercnél tovább tölt, a látogatók jelentős része bezárja."),
    ("Mérés nélkül vakon repülsz.", "Bekötött mérés nélkül nem tudod, melyik hirdetésed hoz pénzt, és melyik csak viszi."),
    ("A sütisáv nem formalitás.", "Helyes beállítás nélkül jogi kockázatot vállalsz, és a mérési adataid is hiányosak lesznek."),
    ("Az oldalcsere elviheti a Google-helyezéseidet.", "Pontos átirányítások nélkül az évek alatt felépített láthatóság napok alatt eltűnhet."),
    ("A webshopoknak akadálymentesnek kell lenniük.", "Az EU akadálymentességi irányelve 2025 nyara óta a mikrovállalkozások kivételével a webshopokra is kötelező."),
]) + """
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KINEK NEM AJÁNLJUK</span></div>
    <div class="who-not rv">
      <p>Akkor valószínűleg nem mi vagyunk a jó választás, ha:</p>
      <ul>
        <li>csak a legolcsóbb megoldást keresed, és a minőség másodlagos;</li>
        <li>holnapra kell egy kész oldal;</li>
        <li>nem szeretnél részt venni a jóváhagyásokban.</li>
      </ul>
    </div>
  </div>
</section>

<section class="pad rule" id="gyik">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">GYAKORI KÉRDÉSEK</span></div>
    <div class="faq-list">
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Mennyi idő alatt készül el?<span class="plus"></span></button>
        <div class="faq-a"><p>A projekt méretétől függően 3 héttől 3 hónapig.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Később magam is szerkeszthetem?<span class="plus"></span></button>
        <div class="faq-a"><p>Igen. Megmutatjuk, hogyan frissítheted a szövegeket és a képeket.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Mire van szükség tőlem?<span class="plus"></span></button>
        <div class="faq-a"><p>Néhány alapinformációra a vállalkozásodról, és a jóváhagyásokra. A többit mi intézzük.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Kié lesz az oldal és a domain?<span class="plus"></span></button>
        <div class="faq-a"><p>A tiéd. Minden fiók, domain és fájl a te nevedre szól.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Mi van, ha valami nem tetszik?<span class="plus"></span></button>
        <div class="faq-a"><p>Minden fázisban jelezheted, és a jóváhagyás előtt javítjuk.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">EZ IS ÉRDEKELHET</span></div>
    <div class="cross-links rv-stagger">
      <a class="cross-link" href="../marketing-es-ai/"><span class="k">Marketing és AI</span><p>Az új oldaladra hozzuk a látogatókat.</p></a>
      <a class="cross-link" href="../tartalomgyartas/"><span class="k">Tartalomgyártás</span><p>Fotók és videók az oldaladra.</p></a>
    </div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Készen állsz egy márkára és egy oldalra, amely ügyfelet hoz?</h2>
    <div class="ctas"><a href="../projekt-inditasa/" class="btn filled magnetic">Elindítom a projektem</a></div>
  </div>
</section>
"""
