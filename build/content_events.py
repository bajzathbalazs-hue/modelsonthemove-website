# -*- coding: utf-8 -*-
from shell import COOLTIX_EVENT_PRODUCT_ID, COOLTIX_WIDGET_URL

# Jegyértékesítés: Cooltix widget (ld. shell.py COOLTIX_WIDGET_SCRIPT). A gomb
# a data-cooltix-event-products attribútumot hívja, nem közvetlen link.
EVENT_TICKET_URL = COOLTIX_WIDGET_URL

COOLTIX_TICKET_BTN = f'<button type="button" class="btn filled magnetic" data-cooltix-event-products=\'{COOLTIX_EVENT_PRODUCT_ID}\'>Jegyet veszek</button>'
COOLTIX_TABLE_BTN = f'<button type="button" class="btn magnetic" data-cooltix-event-products=\'{COOLTIX_EVENT_PRODUCT_ID}\'>VIP-asztalfoglalás</button>'

# ---- Főoldali/Események "következő esemény" kártya — csak akkor jelenik meg
# élesben teljes részletességgel, ha van ténylegesen meghirdetett esemény.
# Formátum: {"name": "...", "date_label": "2026. november 14., szombat",
#            "time_label": "23:00-tól", "venue_type": "prémium klub a belvárosban",
#            "mood": "Két-három mondat a témáról és a hangulatról.",
#            "dress_code": "Elegáns, all black.", "vip_table": True/False,
#            "countdown_iso": "2026-11-14T23:00:00+01:00"}
# A név/helyszín itt BELSŐ admin-célra van (pl. Cooltix-szinkron), a nyilvános
# oldal NEM jeleníti meg az esemény/helyszín NEVÉT — csak típus/hangulat szerint,
# anonimizáltan (brief 0. és 6.2 pont).
ACTIVE_EVENT = None

# ---- Korábbi események — anonimizált, név/helyszín nélküli leírások (brief
# 6.3). A képek megmaradnak (saját fotók, nem azonosítanak ügyfelet/helyszínt
# névvel), de a cím/helyszín/fellépő-nevek nem jelenhetnek meg. A pontos
# dátumok a brief 8. pontja szerint egyelőre nyitott kérdés — addig a
# "[ÉÉÉÉ. hónap NN.]" helyőrző marad, élesben rejtve (ld. shell.DEV_NOTE_STYLE),
# így a nyilvános oldalon egyelőre nincs dátum kiírva a kártyákon.
LATEST_EVENT = {
    "cover": "dubai-style-flyer.jpg",
    "teaser": "Egy este, amely a távoli éjszakák energiáját hozta Budapestre: élő DJ-szettek, különleges fények és hangulat, amely hajnalig tartó partyvá alakult.",
    "gallery": ["vibe-jungle-lounge.jpg", "vibe-bartrio-final.jpg", "vibe-redroom-group.jpg", "vibe-table-group.jpg", "vibe-cellar-table.jpg"],
    "video": None,
}

EARLIER_EVENTS = [
    {
        "cover": "ig-myrazs-recap.jpg",
        "teaser": "Divatbemutató és utána party — ez indította el a rendszeres estéink sorát.",
    },
    {
        "cover": "ig-afrohouse-announce.jpg",
        "teaser": "Exkluzív vacsora, fashion show, majd hajnalig tartó party.",
    },
    {
        "cover": "leroy-szezonnyito.jpg",
        "teaser": "Napközbeni luxusélmény a teraszon, két fashion show-val és élő DJ-szettekkel, amely éjszakába nyúló partyvá alakult.",
    },
]


def _event_card_anon(ev, depth_prefix="../assets/"):
    return f"""      <div class="event-card glow-card">
        <div class="plate photo grain" style="background-image:url('{depth_prefix}{ev['cover']}')"></div>
        <div class="event-card-body">
          <p class="dev-note">[ÉÉÉÉ. hónap NN.]</p>
          <p>{ev['teaser']}</p>
        </div>
      </div>"""


def _next_event_section():
    if ACTIVE_EVENT:
        ev = ACTIVE_EVENT
        vip_row = f'<p style="margin-top:14px;text-align:center;font-size:13px;color:var(--ivory-dim);">VIP-asztal is foglalható.</p>' if ev.get("vip_table") else ""
        dress_row = f"""
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">DRESS CODE</span></div>
    <div class="dresscode-box rv">{ev.get('dress_code', '')}</div>
  </div>
</section>""" if ev.get("dress_code") else ""
        return f"""
<section class="pad rule" id="kovetkezo" style="padding-top:60px;">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">A KÖVETKEZŐ ESEMÉNY</span>
      <h2>{ev['date_label']} · {ev.get('time_label','')} · Budapest, {ev['venue_type']}</h2>
      <p>{ev['mood']}</p>
    </div>
    <div class="ctas" style="margin-top:30px;justify-content:center;display:flex;gap:16px;flex-wrap:wrap;">
      {COOLTIX_TICKET_BTN}
      {COOLTIX_TABLE_BTN if ev.get('vip_table') else ''}
    </div>
    <p style="margin-top:18px;text-align:center;font-size:12.5px;color:var(--ivory-dimmer);">Jegy online és a helyszínen is vásárolható, amíg a készlet tart.</p>
    {vip_row}
  </div>
</section>
{dress_row}"""
    return """
<section class="pad rule" id="kovetkezo" style="padding-top:60px;">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">A KÖVETKEZŐ ESEMÉNY</span>
      <h2>Hamarosan jelentkezünk a részletekkel.</h2>
      <p>A következő esténk szervezés alatt áll. Iratkozz fel lent, és elsőként értesítünk, amint elérhető a jegyvásárlás.</p>
    </div>
    <p class="dev-note">[FEJLESZTŐI NÉZET — élesben rejtve. Ha lesz aktív esemény, töltsd ki az ACTIVE_EVENT szótárat content_events.py-ban, és ez a blokk a brief szerinti teljes sablonra vált: Esemény címe (belső, nem publikus) / Dátum · Kezdés · Budapest, a helyszín típusa / Két-három mondat a témáról és a hangulatról / Gomb: Jegyet veszek / "Jegy online és a helyszínen is vásárolható, amíg a készlet tart." / "VIP-asztal is foglalható." (csak ha elérhető) / Visszaszámláló az esemény kezdetéig.]</p>
  </div>
</section>"""


EVENTS_BODY = f"""
%%BREADCRUMB%%
<section class="gal-hero">
  <div class="wrap">
    <div class="rv">
      <span class="eyebrow">ESEMÉNYEK</span>
      <h1>Nem buli. Esemény.</h1>
      <p>Válogatott közönség, prémium helyszín, gondosan felépített este. Azoknak, akik nemcsak ott akarnak lenni, hanem emlékezni is szeretnének rá.</p>
    </div>
  </div>
</section>

{_next_event_section()}

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">MIRE SZÁMÍTHATSZ</span></div>
    <ul class="who-for rv-stagger">
      <li><b style="color:var(--ivory);">Válogatott vendégkör:</b> modellek, tartalomgyártók, vállalkozók és barátaik.</li>
      <li><b style="color:var(--ivory);">Tematikus este:</b> minden eseménynek saját világa van, a dekorációtól a zenéig.</li>
      <li><b style="color:var(--ivory);">Profi stáb:</b> fotósok és videósok rögzítik az estét, így a legjobb pillanataid megmaradnak.</li>
      <li><b style="color:var(--ivory);">Prémium élmény:</b> a belépéstől az utolsó zenéig.</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">GYAKORI KÉRDÉSEK</span></div>
    <div class="faq-list">
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Hány éves kortól lehet belépni?<span class="plus"></span></button>
        <div class="faq-a"><p>18 éves kortól, személyi igazolvánnyal.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Van dress code?<span class="plus"></span></button>
        <div class="faq-a"><p>Igen, az adott eseménynél mindig jelezzük.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Visszaváltható a jegy?<span class="plus"></span></button>
        <div class="faq-a"><p>A megvásárolt jegy nem váltható vissza, de más névre átíratható.</p></div>
      </div>
      <div class="faq-item" aria-expanded="false">
        <button type="button" class="faq-q">Hogyan értesülök a következő eseményről?<span class="plus"></span></button>
        <div class="faq-a"><p>Kövess minket Instagramon, vagy iratkozz fel a listánkra.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule" id="feliratkozas">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">LEGYÉL AZ ELSŐK KÖZÖTT</span>
      <p>Iratkozz fel, és még a nyilvános meghirdetés előtt értesítünk a következő eseményről.</p>
    </div>
    <div class="wrap rv" style="padding:0;max-width:480px;">
      <form class="form-panel" name="esemeny-feliratkozas" data-netlify="true" data-netlify-honeypot="company_website" data-motm-form data-msg-id="subscribeMsg" data-event="event_subscribe_submit" novalidate>
        <input type="hidden" name="form-name" value="esemeny-feliratkozas">
        <input type="hidden" name="page_url" value="">
        <input type="hidden" name="referrer_url" value="">
        <div class="hp-field" aria-hidden="true"><label>Cégnév (ne töltsd ki)</label><input type="text" name="company_website" tabindex="-1" autocomplete="off"></div>
        <div class="field"><label for="sub-name">NÉV</label><input id="sub-name" name="name" type="text" required></div>
        <div class="field"><label for="sub-email">E-MAIL</label><input id="sub-email" name="email" type="email" required></div>
        <label class="check"><input type="checkbox" name="consent" required> Elfogadom az Adatkezelési tájékoztatót.</label>
        <div class="submit-row">
          <button type="submit" class="btn filled magnetic">Feliratkozom</button>
        </div>
        <div class="form-msg" id="subscribeMsg"><h4>FELIRATKOZVA.</h4><p>Köszönjük. A következő eseményről elsőként értesítünk.</p></div>
      </form>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KORÁBBI ESTÉINK</span><h2>Nézd meg, mi történt eddig.</h2></div>
    <div style="text-align:center;"><a href="../korabbi-esemenyek/" class="btn magnetic">Megnézem a korábbi eseményeket →</a></div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Szeretnéd, hogy a márkád is megjelenjen az eseményeinken?</h2>
    <div class="ctas"><a href="../projekt-inditasa/" class="btn filled magnetic">Együttműködést szeretnék</a></div>
  </div>
</section>
"""

KORABBI_ESEMENYEK_BODY = f"""
%%BREADCRUMB%%
<section class="gal-hero">
  <div class="wrap">
    <div class="rv">
      <span class="eyebrow">KORÁBBI ESEMÉNYEK</span>
      <h1>Esték, amelyekről még mindig beszélnek.</h1>
      <p>Négy esemény, eseményenként 200–300 vendég, és egy közösség, amely minden alkalommal tovább nő.</p>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="stat-row rv-stagger" style="margin-top:0;">
      <div><b>4</b><span>ESEMÉNY</span></div>
      <div><b>200–300</b><span>VENDÉG ESEMÉNYENKÉNT</span></div>
      <div><b>332 ezer</b><span>MEGTEKINTÉS EGYETLEN KAMPÁNYBAN</span></div>
      <div><b>87,6%</b><span>ÚJ KÖZÖNSÉG</span></div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">LEGUTÓBBI ESEMÉNYÜNK</span>
      <p class="dev-note">[ÉÉÉÉ. hónap NN.]</p>
      <p>{LATEST_EVENT['teaser']}</p>
      <p style="margin-top:14px;"><b style="color:var(--bronze-bright);">Eredmények a kampányidőszakban:</b> 332 ezer megtekintés · 81 ezer egyedi néző · 135 ezer sztori-, 107 ezer poszt- és 87 ezer Reels-megtekintés</p>
    </div>
    <div class="gallery-grid rv-stagger" style="margin-top:40px;">
{chr(10).join(f'''      <div class="gtile glow-card"><div class="plate photo grain" style="background-image:url('../assets/{img}')"></div></div>''' for img in LATEST_EVENT['gallery'])}
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KORÁBBI ESEMÉNYEINK</span></div>
    <div class="event-cards-row rv-stagger">
{chr(10).join(_event_card_anon(ev) for ev in EARLIER_EVENTS)}
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KEZDETEK</span>
      <p>Divatbemutatókkal indultunk, ma már saját eseménysorozatunk van, és egy közösség, amely minden alkalommal visszatér.</p>
    </div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Eseményeinken a márkád valós, prémium közönség előtt jelenhet meg, a karszalagtól a fotófalig.</h2>
    <div class="ctas"><a href="../influencer-egyuttmukodes/" class="btn filled magnetic">Együttműködést szeretnék</a></div>
  </div>
</section>

<section class="pad rule" style="padding-top:60px;">
  <div class="wrap rv" style="text-align:center;">
    <h2 style="font-family:var(--serif);font-size:clamp(26px,4vw,40px);margin-bottom:28px;">Ott leszel a következőn?</h2>
    <a href="../esemenyek/" class="btn filled magnetic">Megnézem a következő eseményt</a>
  </div>
</section>
"""
