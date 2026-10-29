# -*- coding: utf-8 -*-
# Projekt indítása — brief 4.10: többlépéses, elágazó űrlap.
#
# Felépítés: a teljes űrlap EGY <form data-netlify> elemben él (így a meglévő,
# megosztott motmHandleForm/Netlify Forms gépezet változtatás nélkül újrahasznosítható —
# honeypot, page_url/referrer_url, sikeres-küldés állapot). A lépések közötti
# navigációt, az elágazó logikát és a rejtett "subject" (KIEMELT/NORMÁL/
# JAVASLATOT KÉR) címkézést egy oldal-specifikus <script> végzi a lap alján.

def _chip_group(label, name, options, multi=True, extra_attrs=""):
    cls = "chips" if multi else "chips chips-single"
    chips = "\n".join(f'          <span class="chip-opt" data-value="{v}">{v}</span>' for v in options)
    return f"""      <div class="field"{extra_attrs}>
        <label>{label}</label>
        <div class="{cls}" data-field-name="{name}">
{chips}
        </div>
        <input type="hidden" name="{name}" value="">
      </div>"""


PROJEKT_BODY = """
%%BREADCRUMB%%
<section class="subhero" style="padding-bottom:40px;">
  <div class="wrap">
    <span class="eyebrow rv">PROJEKT INDÍTÁSA</span>
    <h1 class="rv">Mondd el, mit szeretnél. A többit mi intézzük.</h1>
    <p class="lead rv">Néhány egyszerű kérdés, nagyjából három perc. A válaszaid alapján személyre szabott javaslattal jelentkezünk.</p>
    <div class="audience-row rv" style="justify-content:center;margin-top:26px;">
      <span class="tag">Egy kapcsolattartó, aki végigviszi a projektedet</span>
      <span class="tag">Bevált csapat minden területre</span>
      <span class="tag">Átlátható lépések, mérhető eredmények</span>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MI TÖRTÉNIK A KÜLDÉS UTÁN</span></div>
    <ol class="sidebar-steps rv-stagger">
      <li>Egy munkanapon belül jelentkezünk.</li>
      <li>Rövid konzultáción pontosítjuk az igényeidet.</li>
      <li>Írásos javaslatot küldünk ütemezéssel.</li>
      <li>A jóváhagyásod után indulunk.</li>
    </ol>
  </div>
</section>

<section class="pad rule" style="padding-top:0;">
  <div class="wrap" style="max-width:720px;">

    <div class="pi-progress" style="margin-bottom:30px;">
      <div class="pi-progress-bar"><div class="pi-progress-fill" id="piProgressFill"></div></div>
      <p id="piProgressLabel" style="margin-top:10px;font-size:11px;letter-spacing:.08em;color:var(--ivory-dimmer);text-transform:uppercase;"></p>
    </div>

    <form class="form-panel" id="piForm" name="projekt-inditasa" data-netlify="true" data-netlify-honeypot="company_hp" data-motm-form data-msg-id="piMsg" data-event="projekt_inditasa_submit" novalidate>
      <input type="hidden" name="form-name" value="projekt-inditasa">
      <input type="hidden" name="page_url" value="">
      <input type="hidden" name="referrer_url" value="">
      <input type="hidden" name="subject" value="[NORMÁL] Új projektindítás">
      <div class="hp-field" aria-hidden="true"><label>Cégnév (ne töltsd ki)</label><input type="text" name="company_hp" tabindex="-1" autocomplete="off"></div>

      <!-- 1. LÉPÉS: KATEGÓRIA -->
      <div class="pi-step" data-step="kategoria">
""" + _chip_group("MIBEN SEGÍTHETÜNK? (TÖBB IS VÁLASZTHATÓ)", "kategoria", [
    "Arculat, weboldal vagy webshop",
    "Marketing, hirdetéskezelés vagy AI-megoldás",
    "Kampány és tartalomgyártás (fotó, videó)",
    "Influencer-együttműködés",
], multi=True) + """
        <div class="submit-row"><button type="button" class="btn filled magnetic pi-next">Tovább lépek</button></div>
      </div>

      <!-- ÁG: ARCULAT, WEBOLDAL VAGY WEBSHOP -->
      <div class="pi-step" data-step="arculat" hidden>
        <div class="sec-head" style="text-align:left;margin:0 0 26px;"><span class="eyebrow">ARCULAT, WEBOLDAL VAGY WEBSHOP</span></div>
""" + _chip_group("Mire van szükséged? (több is választható)", "oldal_tipus", ["Arculat (logó, színek, nyomdai anyagok)", "Bemutatkozó oldal", "Webshop", "Landing oldal", "Meglévő oldal megújítása"], multi=True) + """
""" + _chip_group("Van már arculatod (logó, színek, betűtípus)?", "arculat_keszenlet", ["Igen, kész", "Részben", "Nincs, ezt is kérném"], multi=False) + """
""" + _chip_group("Ki írja a szövegeket, és honnan lesznek a fotók?", "tartalom_igeny", ["Megvannak", "Kérem a szövegírást", "Kérem a fotózást is"], multi=True) + """
""" + _chip_group("Mire van szükséged az indításhoz?", "extra_igeny", ["Mérés és analitika", "Keresőoptimalizálás", "Jogi szövegek", "Domain és tárhely", "Folyamatos karbantartás"], multi=True) + """
      <div class="field" id="webshopExtra" hidden>
        <label for="webshop_termekszam">KÖRÜLBELÜL HÁNY TERMÉK LESZ?</label>
        <input id="webshop_termekszam" name="webshop_termekszam" type="text">
        <label class="check" style="margin-top:14px;"><input type="checkbox" name="webshop_fizetes" value="Igen"> Kérem a fizetés, a szállítás és a számlázás bekötését is.</label>
      </div>
      <div class="field"><label for="referencia_link">VAN OLYAN OLDAL, AMELY TETSZIK, ÉS MEGMUTATNÁD NEKÜNK? (NEM KÖTELEZŐ)</label><input id="referencia_link" name="referencia_link" type="text" placeholder="https://..."></div>
        <div class="submit-row"><button type="button" class="btn magnetic pi-back">Visszalépek</button><button type="button" class="btn filled magnetic pi-next">Tovább lépek</button></div>
      </div>

      <!-- ÁG: MARKETING, HIRDETÉSKEZELÉS VAGY AI -->
      <div class="pi-step" data-step="marketing" hidden>
        <div class="sec-head" style="text-align:left;margin:0 0 26px;"><span class="eyebrow">MARKETING, HIRDETÉSKEZELÉS VAGY AI</span></div>
""" + _chip_group("Mi a fő célod?", "marketing_cel", ["Több ajánlatkérés", "Több webshopos rendelés", "Márkaismertség", "Új piac vagy termék bevezetése", "Belső folyamatok gyorsítása AI-jal"], multi=False) + """
""" + _chip_group("Milyen csatornákon?", "csatornak", ["Google-keresés", "Google Ads", "Meta (Facebook, Instagram)", "TikTok", "YouTube", "E-mail"], multi=True) + """
""" + _chip_group("Fut most hirdetésed?", "fut_hirdetes", ["Igen, és jól megy", "Igen, de nem hoz eredményt", "Még nem"], multi=False) + """
""" + _chip_group("Milyen szintű segítség kell?", "segitseg_szint", ["Csak stratégia", "Stratégia és beállítás", "Teljes, folyamatos menedzsment"], multi=False) + """
      <div class="field" id="aiExtra" hidden>
""" + _chip_group("Mi érdekel?", "ai_erdeklodes", ["AI-oktatás a csapatnak", "Személyre szabott AI-asszisztens", "Automatizációk"], multi=False) + """
      </div>
        <div class="submit-row"><button type="button" class="btn magnetic pi-back">Visszalépek</button><button type="button" class="btn filled magnetic pi-next">Tovább lépek</button></div>
      </div>

      <!-- ÁG: KAMPÁNY VAGY TARTALOMGYÁRTÁS -->
      <div class="pi-step" data-step="kampany" hidden>
        <div class="sec-head" style="text-align:left;margin:0 0 26px;"><span class="eyebrow">KAMPÁNY VAGY TARTALOMGYÁRTÁS</span></div>
""" + _chip_group("Mit készítünk?", "mit_keszitunk", ["Reklámfilm", "Közösségi videók (Reels, TikTok)", "Hirdetési kreatívok", "Fotózás", "Eseményfilm"], multi=True) + """
""" + _chip_group("Mit intézzünk?", "mit_intezzunk", ["Koncepció és forgatókönyv", "Szereplők és modellek", "Helyszín", "Kellékek", "Luxusautó", "Operatőr és fotós", "Smink és stylist", "Vágás és utómunka"], multi=True) + """
      <div class="field"><label for="mennyiseg_platform">HÁNY DARAB ANYAG KELL, ÉS MELYIK PLATFORMRA?</label><input id="mennyiseg_platform" name="mennyiseg_platform" type="text"></div>
""" + _chip_group("Felhasználnád az anyagokat fizetett hirdetésben is?", "hirdetesben_hasznalna", ["Igen", "Nem", "Még nem tudom"], multi=False) + """
        <div class="submit-row"><button type="button" class="btn magnetic pi-back">Visszalépek</button><button type="button" class="btn filled magnetic pi-next">Tovább lépek</button></div>
      </div>

      <!-- ÁG: INFLUENCER-EGYÜTTMŰKÖDÉS -->
      <div class="pi-step" data-step="influencer" hidden>
        <div class="sec-head" style="text-align:left;margin:0 0 26px;"><span class="eyebrow">INFLUENCER-EGYÜTTMŰKÖDÉS</span></div>
""" + _chip_group("Milyen influencerprofil illik a márkádhoz?", "influencer_profil", ["Lifestyle", "Divat és szépség", "Sport és fitnesz", "Ismert arcok (tévé, szépségversenyek)"], multi=True) + """
""" + _chip_group("Milyen formában?", "egyuttmukodes_forma", ["Egyszeri megjelenés", "Havi, rendszeres együttműködés", "Eseményes megjelenés", "Termékcsere (barter)"], multi=False) + """
""" + _chip_group("Hogyan mérjük a sikert?", "siker_meres", ["Elérés", "Követőszám", "Weboldal-forgalom", "Eladás egyedi kóddal"], multi=True) + """
        <div class="submit-row"><button type="button" class="btn magnetic pi-back">Visszalépek</button><button type="button" class="btn filled magnetic pi-next">Tovább lépek</button></div>
      </div>

      <!-- KÖZÖS ZÁRÓ LÉPÉS -->
      <div class="pi-step" data-step="zaro" hidden>
        <div class="sec-head" style="text-align:left;margin:0 0 26px;"><span class="eyebrow">MÉG NÉHÁNY KÉRDÉS</span></div>
""" + _chip_group("Mikorra lenne rá szükséged?", "mikorra", ["1 hónapon belül", "1–3 hónap", "Nem sürgős"], multi=False) + """
      <div class="field" id="webKoltsegWrap" hidden>
""" + _chip_group("Mennyit szánnál a weboldal elkészítésére?", "weboldal_koltseg", ["200–400 ezer Ft", "400–600 ezer Ft", "600–800 ezer Ft", "800 ezer – 1,2 millió Ft", "1,2 millió Ft felett", "Még nem tudom, kérek javaslatot"], multi=False) + """
      </div>
      <div class="field" id="haviDijWrap" hidden>
""" + _chip_group("Mennyit szánnál havonta a mi díjunkra?", "havi_dij", ["100–200 ezer Ft / hó", "200–400 ezer Ft / hó", "400–700 ezer Ft / hó", "700 ezer – 1 millió Ft / hó", "1 millió Ft / hó felett", "Még nem tudom, kérek javaslatot"], multi=False) + """
        <p style="margin-top:10px;font-size:12px;color:var(--ivory-dimmer);">Ez a mi díjunk, a hirdetési költést külön kérdezzük. Csak irányszám, nem kötelezettségvállalás: segít abban, hogy a kereteidhez illő, reális javaslatot készítsünk.</p>
      </div>
      <div class="field" id="hirdetesKoltsegWrap" hidden>
""" + _chip_group("Mennyit költenél havonta hirdetésre?", "hirdetes_koltseg", ["100 ezer Ft alatt", "100–300 ezer Ft", "300–700 ezer Ft", "700 ezer Ft felett", "Még nem tudom"], multi=False) + """
        <p style="margin-top:10px;font-size:12px;color:var(--ivory-dimmer);">Ezt közvetlenül a Google-nek, a Metának vagy a TikToknak fizeted, nem nekünk.</p>
      </div>

      <div class="row2">
        <div class="field"><label for="pi-name">NÉV</label><input id="pi-name" name="name" type="text" required></div>
        <div class="field"><label for="pi-company">CÉGNÉV</label><input id="pi-company" name="company" type="text" required></div>
      </div>
      <div class="row2">
        <div class="field"><label for="pi-email">E-MAIL</label><input id="pi-email" name="email" type="email" required></div>
        <div class="field"><label for="pi-phone">TELEFONSZÁM</label><input id="pi-phone" name="phone" type="tel" required></div>
      </div>

      <div class="row2">
""" + _chip_group("Mikor kereshetünk? Napszak", "napszak", ["Délelőtt (9–12)", "Kora délután (12–15)", "Késő délután (15–18)"], multi=False) + """
""" + _chip_group("Csatorna", "csatorna", ["Telefonon", "E-mailben"], multi=False) + """
      </div>
      <p style="font-size:12px;color:var(--ivory-dimmer);margin-top:-10px;">Egy munkanapon belül jelentkezünk a megadott időpontban.</p>

""" + _chip_group("Hogyan hallottál rólunk?", "honnan_hallottal", ["Instagram", "TikTok", "Google", "Ajánlás", "Rendezvény", "Egyéb"], multi=False) + """

      <label class="check" style="margin-top:20px;"><input type="checkbox" name="consent" required> Elfogadom az Adatkezelési tájékoztatót.</label>

        <div class="submit-row"><button type="button" class="btn magnetic pi-back">Visszalépek</button><button type="submit" class="btn filled magnetic">Elküldöm a megkeresésem</button></div>
      </div>

      <div class="form-msg" id="piMsg"><h4>MEGKAPTUK. HAMAROSAN JELENTKEZÜNK.</h4><p>Egy munkanapon belül személyesen keresünk egy rövid konzultációval és az első javaslatunkkal.</p></div>
    </form>
  </div>
</section>

<script>
(function(){
  var form = document.getElementById('piForm');
  if(!form) return;
  var fill = document.getElementById('piProgressFill');
  var label = document.getElementById('piProgressLabel');
  var BRANCH_ORDER = ['arculat','marketing','kampany','influencer'];
  var BRANCH_LABEL = {
    'Arculat, weboldal vagy webshop':'arculat',
    'Marketing, hirdetéskezelés vagy AI-megoldás':'marketing',
    'Kampány és tartalomgyártás (fotó, videó)':'kampany',
    'Influencer-együttműködés':'influencer'
  };
  var queue = ['kategoria'];
  var idx = 0;

  function chipsValue(container){
    return Array.from(container.querySelectorAll('.chip-opt.on')).map(function(c){ return c.dataset.value; }).join(', ');
  }
  function syncHiddenFields(step){
    step.querySelectorAll('[data-field-name]').forEach(function(group){
      var hidden = group.parentElement.querySelector('input[type=hidden][name="'+group.dataset.fieldName+'"]');
      if(hidden) hidden.value = chipsValue(group);
    });
  }
  function stepEl(name){ return form.querySelector('.pi-step[data-step="'+name+'"]'); }

  function updateProgress(){
    var total = queue.length;
    var pct = Math.round(((idx+1)/total)*100);
    fill.style.width = pct + '%';
    label.textContent = (idx+1) + '. lépés / ' + total;
  }

  function showStep(i){
    queue.forEach(function(name){ stepEl(name).hidden = true; });
    stepEl(queue[i]).hidden = false;
    updateProgress();
    stepEl(queue[i]).scrollIntoView({behavior:'smooth', block:'start'});
  }

  function validateStep(step){
    var valid = true;
    step.querySelectorAll('[required]').forEach(function(el){
      var field = el.closest('.field') || el.closest('.check');
      var empty = el.type === 'checkbox' ? !el.checked : !el.value.trim();
      if(field) field.classList.toggle('error', empty);
      if(empty) valid = false;
    });
    return valid;
  }

  function buildQueueAfterKategoria(){
    var selected = Array.from(stepEl('kategoria').querySelectorAll('.chip-opt.on')).map(function(c){ return BRANCH_LABEL[c.dataset.value]; });
    queue = ['kategoria'];
    BRANCH_ORDER.forEach(function(b){ if(selected.indexOf(b) !== -1) queue.push(b); });
    queue.push('zaro');
    toggleConditionalFields(selected);
  }

  function toggleConditionalFields(selected){
    var webshopSelected = Array.from(stepEl('arculat') ? stepEl('arculat').querySelectorAll('.chip-opt.on') : []).some(function(c){ return c.dataset.value === 'Webshop'; });
    var webshopExtra = document.getElementById('webshopExtra');
    if(webshopExtra) webshopExtra.hidden = !webshopSelected;

    var webKoltsegWrap = document.getElementById('webKoltsegWrap');
    if(webKoltsegWrap) webKoltsegWrap.hidden = selected.indexOf('arculat') === -1;

    var haviDijWrap = document.getElementById('haviDijWrap');
    if(haviDijWrap) haviDijWrap.hidden = !(selected.indexOf('marketing') !== -1 || selected.indexOf('kampany') !== -1 || selected.indexOf('influencer') !== -1);

    var hirdetesKoltsegWrap = document.getElementById('hirdetesKoltsegWrap');
    if(hirdetesKoltsegWrap) hirdetesKoltsegWrap.hidden = selected.indexOf('marketing') === -1;
  }

  // AI-érdeklődés mező csak akkor, ha a "Belső folyamatok gyorsítása AI-jal" cél van kijelölve
  document.addEventListener('click', function(e){
    if(!e.target.classList.contains('chip-opt')) return;
    var marketingCelGroup = form.querySelector('[data-field-name="marketing_cel"]');
    if(marketingCelGroup && marketingCelGroup.contains(e.target)){
      setTimeout(function(){
        var aiOn = marketingCelGroup.querySelector('.chip-opt[data-value="Belső folyamatok gyorsítása AI-jal"]');
        var aiExtra = document.getElementById('aiExtra');
        if(aiExtra) aiExtra.hidden = !(aiOn && aiOn.classList.contains('on'));
      }, 0);
    }
    var oldalTipusGroup = form.querySelector('[data-field-name="oldal_tipus"]');
    if(oldalTipusGroup && oldalTipusGroup.contains(e.target)){
      setTimeout(function(){
        var webshopOn = oldalTipusGroup.querySelector('.chip-opt[data-value="Webshop"]');
        var webshopExtra = document.getElementById('webshopExtra');
        if(webshopExtra) webshopExtra.hidden = !(webshopOn && webshopOn.classList.contains('on'));
      }, 0);
    }
  });

  form.querySelectorAll('.pi-next').forEach(function(btn){
    btn.addEventListener('click', function(){
      var current = stepEl(queue[idx]);
      syncHiddenFields(current);
      if(!validateStep(current)) return;
      if(queue[idx] === 'kategoria'){
        var any = stepEl('kategoria').querySelector('.chip-opt.on');
        if(!any){ stepEl('kategoria').querySelector('.field').classList.add('error'); return; }
        buildQueueAfterKategoria();
      }
      idx++;
      showStep(idx);
    });
  });
  form.querySelectorAll('.pi-back').forEach(function(btn){
    btn.addEventListener('click', function(){
      if(idx === 0) return;
      idx--;
      showStep(idx);
    });
  });

  form.addEventListener('submit', function(){
    var last = stepEl(queue[queue.length-1]);
    syncHiddenFields(last);
    // [KIEMELT] / [NORMÁL] / [JAVASLATOT KÉR] belső rangsor a rejtett subject mezőben
    var webKoltseg = form.querySelector('input[name="weboldal_koltseg"]').value;
    var haviDij = form.querySelector('input[name="havi_dij"]').value;
    var subjectField = form.querySelector('input[name="subject"]');
    var tag = '[NORMÁL]';
    if(webKoltseg.indexOf('Még nem tudom') !== -1 || haviDij.indexOf('Még nem tudom') !== -1){
      tag = '[JAVASLATOT KÉR]';
    }
    // Pontos egyezés a [KIEMELT] sávokra — indexOf-alapú részszöveg-keresés
    // hamis pozitívot adott (pl. "400–600 ezer Ft" tartalmazza a "600"
    // részsztringet, holott az nem a kiemelt sáv).
    var webKiemelt = ['600–800 ezer Ft', '800 ezer – 1,2 millió Ft', '1,2 millió Ft felett'];
    var haviKiemelt = ['400–700 ezer Ft / hó', '700 ezer – 1 millió Ft / hó', '1 millió Ft / hó felett'];
    if(webKiemelt.indexOf(webKoltseg) !== -1 || haviKiemelt.indexOf(haviDij) !== -1){
      tag = '[KIEMELT]';
    }
    subjectField.value = tag + ' Új projektindítás';
  });

  showStep(0);
})();
</script>
"""
