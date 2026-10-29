# -*- coding: utf-8 -*-
# Influencer-együttműködés — végleges brief 6.6, betűre pontosan.
from shell import MODEL_APPLICATION_FORM

def _notice(items):
    rows = "\n".join(
        f'      <p style="margin-top:18px;"><b style="color:var(--bronze-bright);">{lead}</b> {rest}</p>'
        for lead, rest in items
    )
    return f'<div class="wrap" style="max-width:720px;">{rows}\n    </div>'


INFLUENCER_BODY = """
%%BREADCRUMB%%
<section class="subhero">
  <div class="wrap">
    <span class="eyebrow rv">INFLUENCER-EGYÜTTMŰKÖDÉS</span>
    <h1 class="rv">A márkád ott, ahol a figyelem van.</h1>
    <p class="lead rv">Állandó influencerhálózatunkkal hiteles, valódi közönséghez szóló megjelenést építünk, a kiválasztástól a mérhető eredményig.</p>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="stat-row rv-stagger" style="margin-top:0;">
      <div><b>16</b><span>ÁLLANDÓ INFLUENCERPARTNER</span></div>
      <div><b>≈790 000</b><span>INSTAGRAM-KÖVETŐ</span></div>
      <div><b>332 000</b><span>MEGTEKINTÉS EGYETLEN KAMPÁNYBAN</span></div>
      <div><b>87,6%</b><span>ÚJ KÖZÖNSÉG</span></div>
    </div>
    <p style="margin-top:22px;text-align:center;font-size:11.5px;color:var(--ivory-dimmer);">Partnereink Instagram-követőinek összesített száma, 2026. október. Az összeg átfedéseket tartalmazhat.</p>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KINEK AJÁNLJUK</span></div>
    <ul class="who-for rv-stagger">
      <li><b style="color:var(--ivory);">Prémium márkáknak,</b> amelyek hiteles arcokkal szeretnének megjelenni.</li>
      <li><b style="color:var(--ivory);">Új márkáknak és termékeknek,</b> amelyeknek gyorsan kell ismertséget szerezniük.</li>
      <li><b style="color:var(--ivory);">Szolgáltatóknak és kereskedőknek,</b> akik mérhető forgalmat várnak a megjelenésből.</li>
      <li><b style="color:var(--ivory);">Rendezvényszervezőknek,</b> akiknek közönség kell.</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">HÁLÓZATUNK</span>
      <p>Szépségkirálynők, olimpikonok, divatmodellek, tévéből ismert arcok, fitnesz- és lifestyle-tartalomgyártók. Mindegyikükkel rendszeresen dolgozunk, ezért gyorsan, megbízhatóan és kedvező feltételekkel tudunk együttműködést indítani.</p>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MIT KAPSZ, TÉTELESEN</span></div>
    <div class="subgroup">
      <h4>Adat és stratégia</h4>
      <ul class="bullet-list">
        <li>Közönségelemzés: kik követik valójában az influencert (kor, nem, helyszín, aktivitás)</li>
        <li>Friss statisztikák bekérése minden kiválasztott partnertől</li>
        <li>Kampánystratégia és célok rögzítése</li>
        <li>Éves influencerterv, ha hosszú távon gondolkodsz</li>
      </ul>
    </div>
    <div class="subgroup">
      <h4>Kreatív és gyártás</h4>
      <ul class="bullet-list">
        <li>Koncepció és forgatókönyv</li>
        <li>Kiválasztás (casting) a hálózatunkból vagy azon kívül</li>
        <li>Teljes gyártásszervezés: helyszín, kellékek, stáb</li>
        <li>Állandó operatőr és vágó</li>
      </ul>
    </div>
    <div class="subgroup">
      <h4>Kampánykezelés</h4>
      <ul class="bullet-list">
        <li>Írásos megállapodás a partnerekkel, rögzített feltételekkel</li>
        <li>Tartalmak előzetes jóváhagyása a megjelenés előtt</li>
        <li>Jogszerű reklámjelölés minden megjelenésnél</li>
        <li>Egy kapcsolattartó, aki végig koordinálja a projektet</li>
      </ul>
    </div>
    <div class="subgroup">
      <h4>Terjesztés és hirdetés</h4>
      <ul class="bullet-list">
        <li>A tartalmak felhasználási jogának rendezése a saját hirdetéseidhez</li>
        <li>Partnerhirdetés az influencer fiókjáról, ha ezt választod</li>
        <li>A legjobban teljesítő anyagok kiválasztása ráhirdetésre</li>
      </ul>
    </div>
    <div class="subgroup" style="margin-bottom:0;">
      <h4>Mérés</h4>
      <ul class="bullet-list">
        <li>Egyedi követőlinkek és kedvezménykódok</li>
        <li>Záró riport elérésről, követőszámról, weboldal-forgalomról és eladásokról</li>
      </ul>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">HOGYAN DOLGOZUNK</span></div>
    <div class="process-grid rv-stagger">
      <div class="process-step"><span class="idx">01</span><h4>Célmeghatározás</h4><p>Mit szeretnél elérni, és kiket.</p></div>
      <div class="process-step"><span class="idx">02</span><h4>Kiválasztás</h4><p>A hálózatunkból olyan influencereket ajánlunk, akiknek a közönsége illik a márkádhoz. Ha van saját kiszemelted, őt is megkeressük.</p></div>
      <div class="process-step"><span class="idx">03</span><h4>Koncepció</h4><p>Kidolgozzuk a tartalom ötletét és üzenetét, és jóváhagyásra elküldjük.</p></div>
      <div class="process-step"><span class="idx">04</span><h4>Gyártás</h4><p>Megszervezzük a forgatást vagy a fotózást.</p></div>
      <div class="process-step"><span class="idx">05</span><h4>Jóváhagyás</h4><p>A kész tartalmat a megjelenés előtt megmutatjuk neked.</p></div>
      <div class="process-step"><span class="idx">06</span><h4>Megjelenés</h4><p>A tartalom az influencer saját oldalán fut, organikusan.</p></div>
      <div class="process-step"><span class="idx">07</span><h4>Ráhirdetés igény szerint</h4><p>A legjobb anyagokat a saját hirdetéseidben is felhasználhatod.</p></div>
      <div class="process-step"><span class="idx">08</span><h4>Mérés és riport</h4><p>Pontosan látod, hány látogatót és vásárlót hozott az együttműködés.</p></div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">EGYÜTTMŰKÖDÉSI FORMÁK</span></div>
    <ul class="bullet-list" style="margin:0 auto;">
      <li><b style="color:var(--ivory);">Egyszeri megjelenés:</b> egy termék, egy esemény vagy egy bejelentés</li>
      <li><b style="color:var(--ivory);">Havi együttműködés:</b> rendszeres jelenlét, amely bizalmat épít</li>
      <li><b style="color:var(--ivory);">Eseményes megjelenés:</b> a márkád a rendezvényeinken, valós közönség előtt</li>
      <li><b style="color:var(--ivory);">Termékcsere (barter):</b> a termékedért vagy szolgáltatásodért cserébe</li>
      <li><b style="color:var(--ivory);">Teljes kampány:</b> több influencerrel, egységes koncepcióval</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">EREDMÉNYEK</span>
      <p>Legutóbbi eseményünk kampányidőszakában 332 ezer megtekintést értünk el, 81 ezer egyedi nézővel, és a nézők 87,6%-a új közönség volt.</p>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">AMIRE A LEGTÖBBEN NEM GONDOLNAK</span></div>
""" + _notice([
    ("A követőszám nem minden.", "Egy kisebb, de elkötelezett közönség gyakran több vásárlót hoz, mint egy nagy, de passzív. Ezért mi a valós adatokat nézzük, nem csak a számot."),
    ("A reklámjelölés barternél is kötelező.", "A Gazdasági Versenyhivatal iránymutatása szerint a jelölésnek (például #reklám) a szöveg elején kell állnia, és elmaradásáért a hirdető is felelősségre vonható. Mi ezt minden megjelenésnél ellenőrizzük."),
    ("Felhasználási jog nélkül nem hirdethetsz vele.", "Ha egy jól sikerült videót a saját hirdetésedben is használni szeretnél, ezt előre írásban kell rögzíteni. Mi ezt az elejétől rendezzük."),
    ("Egy videó élettartama néhány nap.", "Az organikus megtekintések jellemzően egy héten belül kifutnak, ezért érdemes a legjobb anyagokat hirdetéssel tovább dolgoztatni."),
]) + """
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KINEK NEM AJÁNLJUK</span></div>
    <div class="who-not rv">
      <p>Akkor valószínűleg nem mi vagyunk a jó választás, ha garantált megtekintésszámot vársz, vagy reklámjelölés nélküli megjelenést szeretnél.</p>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">GYAKORI KÉRDÉSEK</span></div>
    <div class="faq-list">
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Kiválaszthatom, ki jelenjen meg?<span class="plus"></span></button>
        <div class="faq-a"><p>Igen. Javaslatot teszünk, de a végső döntés a tiéd.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Láthatom a tartalmat megjelenés előtt?<span class="plus"></span></button>
        <div class="faq-a"><p>Igen, minden tartalmat jóváhagyásra elküldünk.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Garantáltok megtekintésszámot?<span class="plus"></span></button>
        <div class="faq-a"><p>Nem, mert az organikus elérés a platformok működésétől függ. Azt viszont garantáljuk, hogy minden eredményt pontosan mérünk és átláthatóan riportolunk.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Mennyi idő alatt indulhat egy kampány?<span class="plus"></span></button>
        <div class="faq-a"><p>Néhány héten belül.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">EZ IS ÉRDEKELHET</span></div>
    <div class="cross-links rv-stagger">
      <a class="cross-link" href="../tartalomgyartas/"><span class="k">Tartalomgyártás</span><p>Profi gyártás minden megjelenéshez.</p></a>
      <a class="cross-link" href="../esemenyek/"><span class="k">Események</span><p>A márkád a rendezvényeinken.</p></a>
    </div>
  </div>
</section>
""" + MODEL_APPLICATION_FORM + """

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Találjuk meg a márkádhoz illő arcokat.</h2>
    <div class="ctas"><a href="../projekt-inditasa/" class="btn filled magnetic">Együttműködést szeretnék</a></div>
    <p style="margin-top:22px;font-size:11px;color:var(--ivory-dimmer);">Forrás a reklámjelöléshez: Világgazdaság (vg.hu), 2026. április, a GVH iránymutatásáról.</p>
  </div>
</section>
"""
