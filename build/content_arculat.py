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
<section class="subhero">
  <div class="wrap">
    <span class="eyebrow rv">ARCULATTERVEZÉS</span>
    <h1 class="rv">Egy márka, amelyet első pillantásra felismernek.</h1>
    <p class="lead rv">A logótól a céges ruházatig megtervezzük a teljes arculatodat, hogy minden felületen egységesen és prémium módon jelenj meg.</p>
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
            <li>A márka hangneme: hogyan szólsz az ügyfeleidhez</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">02</div>
        <div><h3>Arculati alapelemek</h3>
          <ul class="bullet-list">
            <li>Logó: fő változat, egyszerűsített változat, ikon, fekete-fehér verzió</li>
            <li>Színpaletta és betűtípusok</li>
            <li>Arculati kézikönyv, hogy bárki helyesen használja a márkádat</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">03</div>
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
        <div class="num">04</div>
        <div><h3>Digitális anyagok</h3>
          <ul class="bullet-list">
            <li>E-mail-aláírás</li>
            <li>Prezentációsablon</li>
            <li>Közösségimédia-sablonok és borítóképek</li>
          </ul>
        </div>
      </div>
      <div class="feature">
        <div class="num">05</div>
        <div><h3>Márkajelenlét a valóságban</h3>
          <ul class="bullet-list">
            <li>Céges ruházat: póló, pulóver, munkaruha</li>
            <li>Autódekoráció és matrica</li>
            <li>Cégtábla és irodai dekoráció</li>
            <li>Csomagolás és címke</li>
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
]) + """
  </div>
</section>

<!-- B) WEBFEJLESZTÉS -->
<section class="subhero" style="padding-top:90px;">
  <div class="wrap">
    <span class="eyebrow rv">WEBFEJLESZTÉS</span>
    <h1 class="rv" style="font-size:clamp(28px,4.6vw,56px);">Weboldal, amely dolgozik helyetted.</h1>
    <p class="lead rv">Gyors, elegáns és mérhető oldalakat építünk, amelyekből a látogatóid ügyfelek lesznek. Az első ötlettől az élesítésig mindent intézünk.</p>
    <div class="ctas rv"><a href="../kapcsolat/" class="btn filled magnetic">INGYENES KONZULTÁCIÓT KÉREK</a></div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MIT KÉSZÍTÜNK</span></div>
    <div class="process-grid rv-stagger">
      <div class="process-step"><h4>Bemutatkozó oldal</h4><p>Megmutatja, kik vagytok, és miért érdemes titeket választani.</p></div>
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
            <li>Drótváz, majd látványterv, végül kattintható prototípus jóváhagyásra</li>
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
            <li>Gyorsasági optimalizálás a Google mutatói (Core Web Vitals) szerint</li>
            <li>Késleltetett képbetöltés, gyorsítótárazás, tartalomkézbesítő hálózat (CDN)</li>
            <li>Akadálymentesség nemzetközi szabvány (WCAG) szerint</li>
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
            <li>Oldaltérkép a keresőknek (sitemap), robots.txt, kanonikus címek</li>
            <li>Strukturált adatok, hogy a Google gazdagabb találatként mutasson (értékelések, árak, események, kérdések)</li>
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
            <li>Meta Pixel és Conversions API, TikTok Pixel</li>
            <li>Google Ads konverziókövetés</li>
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
      <div class="feature">
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

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">HOGYAN DOLGOZUNK</span></div>
    <div class="process-grid rv-stagger">
      <div class="process-step"><span class="idx">01</span><h4>Konzultáció</h4><p>Megismerjük a célodat és a közönségedet.</p></div>
      <div class="process-step"><span class="idx">02</span><h4>Terv</h4><p>Elkészítjük a szerkezetet és a látványtervet, és csak a jóváhagyásod után haladunk tovább.</p></div>
      <div class="process-step"><span class="idx">03</span><h4>Fejlesztés</h4><p>Felépítjük az oldalt, a szövegeket és a méréseket.</p></div>
      <div class="process-step"><span class="idx">04</span><h4>Tesztelés és élesítés</h4><p>Minden eszközön és böngészőben ellenőrizzük.</p></div>
      <div class="process-step"><span class="idx">05</span><h4>Utánkövetés</h4><p>Figyeljük az eredményeket, és igény szerint továbbfejlesztjük.</p></div>
    </div>
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
    ("Mérés nélkül vakon repülsz.", "Bekötött mérés nélkül nem tudod, melyik hirdetésed hoz pénzt, és melyik viszi."),
    ("A sütisáv nem formalitás.", "Helyes beállítás nélkül jogi kockázatot vállalsz, és a mérési adataid is hiányosak lesznek."),
    ("Az oldalcsere elviheti a Google-helyezéseidet.", "Pontos átirányítások nélkül az évek alatt felépített láthatóság napok alatt eltűnhet."),
    ("A webshopoknak akadálymentesnek kell lenniük.", "Az EU akadálymentességi irányelve 2025 nyara óta a webshopok többségére kötelező."),
]) + """
  </div>
</section>

<section class="pad rule">
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
        <div class="faq-a"><p>Néhány alapinformációra a vállalkozásodról. A többit közösen kitaláljuk.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Készen állsz egy oldalra, amely ügyfelet hoz?</h2>
    <div class="ctas"><a href="../projekt-inditasa/" class="btn filled magnetic">INDÍTSUK EL A PROJEKTED</a></div>
  </div>
</section>
"""
