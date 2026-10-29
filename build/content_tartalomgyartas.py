# -*- coding: utf-8 -*-
# Tartalomgyártás — végleges brief 6.7, betűre pontosan.

def _notice(items):
    rows = "\n".join(
        f'      <p style="margin-top:18px;"><b style="color:var(--bronze-bright);">{lead}</b> {rest}</p>'
        for lead, rest in items
    )
    return f'<div class="wrap" style="max-width:720px;">{rows}\n    </div>'


TARTALOMGYARTAS_BODY = """
%%BREADCRUMB%%
<section class="subhero">
  <div class="wrap">
    <span class="eyebrow rv">TARTALOMGYÁRTÁS</span>
    <h1 class="rv">Képek és videók, amelyeknél nem görgetnek tovább.</h1>
    <p class="lead rv">Reklámfilmtől a TikTok-videóig mindent elkészítünk, az ötlettől a kész, publikálható anyagig. Neked csak jóvá kell hagynod.</p>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KINEK AJÁNLJUK</span></div>
    <ul class="who-for rv-stagger">
      <li><b style="color:var(--ivory);">Márkáknak,</b> amelyeknek folyamatosan friss közösségi tartalom kell.</li>
      <li><b style="color:var(--ivory);">Cégeknek,</b> amelyek reklámfilmet vagy bemutatkozó videót szeretnének.</li>
      <li><b style="color:var(--ivory);">Webshopoknak,</b> amelyeknek termékfotó és hirdetési kreatív kell.</li>
      <li><b style="color:var(--ivory);">Rendezvényszervezőknek,</b> akik eseményfilmmel adnák el a következő estét.</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MIT KÉSZÍTÜNK</span></div>
    <div class="process-grid rv-stagger">
      <div class="process-step"><h4>Reklámfilm és márkavideó</h4><p>A márkád története néhány erős percben.</p></div>
      <div class="process-step"><h4>Közösségi videók</h4><p>Reels, TikTok és Shorts formátumban, a platformok ritmusára vágva.</p></div>
      <div class="process-step"><h4>Hirdetési kreatívok</h4><p>Több változatban, teszteléshez.</p></div>
      <div class="process-step"><h4>Fotózás</h4><p>Termék-, portré-, divat- és lifestyle-fotók.</p></div>
      <div class="process-step"><h4>Eseményfilm</h4><p>A rendezvényed hangulata, amely a következő eseményt is eladja.</p></div>
      <div class="process-step"><h4>Autós és prémium tartalom</h4><p>Látványos helyszíneken, luxusautókkal.</p></div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MINDENT MEGSZERVEZÜNK</span></div>
    <ul class="bullet-list" style="margin:0 auto;">
      <li>Koncepció, forgatókönyv és képes forgatási terv (storyboard)</li>
      <li>Szereplők, modellek és influencerek</li>
      <li>Helyszínkeresés és engedélyek</li>
      <li>Kellékek, ruhák és luxusautó</li>
      <li>Profi felszerelésű operatőr és fotós, világítással</li>
      <li>Smink és stylist</li>
      <li>Vágás, színkorrekció, hang és feliratozás</li>
      <li>Jogtiszta zene</li>
      <li>Egy gyártásvezető, aki a teljes folyamatot összefogja</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MIT KAPSZ A VÉGÉN</span></div>
    <ul class="bullet-list" style="margin:0 auto;">
      <li>Kész anyagok minden platform méretében (álló, fekvő, négyzetes)</li>
      <li>Rövid és hosszú változatok, hirdetésre optimalizált vágások</li>
      <li>Felirat, mert a közösségi videók jelentős részét hang nélkül nézik</li>
      <li>Rendezett felhasználási jogok a saját oldaladhoz és a hirdetéseidhez</li>
      <li>Szerkesztett fájlok átadása rendezett mappaszerkezetben</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">HOGYAN DOLGOZUNK</span></div>
    <div class="phase-table-wrap rv">
      <table class="phase-table">
        <tr><th>Fázis</th><th>Mit csinálunk</th><th>Mit kapsz</th><th>Jóváhagyás</th></tr>
        <tr><td>1. Brief</td><td>Megbeszéljük a célt és a megjelenési helyeket.</td><td>Írásos brief</td><td class="check">✓</td></tr>
        <tr><td>2. Koncepció</td><td>Ötletet, forgatókönyvet és látványtervet készítünk.</td><td>Koncepció és storyboard</td><td class="check">✓</td></tr>
        <tr><td>3. Előkészítés</td><td>Megszervezünk mindent és mindenkit.</td><td>Forgatási ütemterv</td><td class="check">–</td></tr>
        <tr><td>4. Forgatás</td><td>Végig ott vagyunk, neked nem kell mindenre figyelned.</td><td>–</td><td class="check">–</td></tr>
        <tr><td>5. Utómunka</td><td>Vágás, színezés, hang, felirat.</td><td>Első változat, egy javítási körrel</td><td class="check">✓</td></tr>
        <tr><td>6. Átadás</td><td>Minden formátumban, publikálásra készen.</td><td>Végleges anyagok</td><td class="check">–</td></tr>
      </table>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">EGYÜTTMŰKÖDÉSI FORMÁK</span></div>
    <ul class="bullet-list" style="margin:0 auto;">
      <li><b style="color:var(--ivory);">Egyszeri gyártás:</b> egy film, egy fotózás vagy egy kampány anyagai.</li>
      <li><b style="color:var(--ivory);">Havi tartalomcsomag:</b> rendszeres forgatási nap, amelyből egy havi tartalom jön ki.</li>
      <li><b style="color:var(--ivory);">Eseményrögzítés:</b> fotó és film a rendezvényedről.</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">AMIRE A LEGTÖBBEN NEM GONDOLNAK</span></div>
""" + _notice([
    ("Az első három másodperc dönt.", "Ha a videó eleje nem ragadja meg a nézőt, a többit már senki sem látja. Ezért minden videót az elejétől tervezünk."),
    ("Egy forgatás, sokféle anyag.", "Jó tervezéssel egyetlen forgatási napból egy havi tartalom is kijöhet."),
    ("A felhasználási jogot előre kell rendezni.", "Szereplők, zene és helyszín esetén is, különben a kész anyag nem használható hirdetésben."),
]) + """
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KINEK NEM AJÁNLJUK</span></div>
    <div class="who-not rv">
      <p>Akkor valószínűleg nem mi vagyunk a jó választás, ha forgatókönyv és előkészítés nélkül, azonnal szeretnél forgatni.</p>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">GYAKORI KÉRDÉSEK</span></div>
    <div class="faq-list">
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Mennyi idő alatt készül el?<span class="plus"></span></button>
        <div class="faq-a"><p>Egy közösségi videócsomag általában 1–2 hét, egy reklámfilm 3–6 hét alatt.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Hány javítási kör van?<span class="plus"></span></button>
        <div class="faq-a"><p>Egy javítási kör benne van, továbbiak egyeztetés szerint.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Kié lesznek az anyagok?<span class="plus"></span></button>
        <div class="faq-a"><p>A tiéd, a megállapodásban rögzített felhasználási joggal.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">EZ IS ÉRDEKELHET</span></div>
    <div class="cross-links rv-stagger">
      <a class="cross-link" href="../influencer-egyuttmukodes/"><span class="k">Influencer-együttműködés</span><p>Arcok, akik eljuttatják a tartalmadat a közönséghez.</p></a>
      <a class="cross-link" href="../marketing-es-ai/"><span class="k">Marketing és AI</span><p>Hirdetés, amely tovább dolgoztatja az anyagaidat.</p></a>
    </div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Mutassuk meg a márkádat úgy, ahogy megérdemli.</h2>
    <div class="ctas"><a href="../projekt-inditasa/" class="btn filled magnetic">Elindítom a projektem</a></div>
  </div>
</section>
"""
