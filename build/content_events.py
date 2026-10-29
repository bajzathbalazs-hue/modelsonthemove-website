# -*- coding: utf-8 -*-
from shell import COOLTIX_EVENT_PRODUCT_ID, COOLTIX_WIDGET_URL

# Jegyértékesítés 2026.10.02-től Cooltix-on fut (korábban SevenRooms) — a
# gombok a Cooltix widget.js-t hívják (lásd shell.py COOLTIX_WIDGET_SCRIPT),
# nem közvetlen linkek. EVENT_TICKET_URL csak a JSON-LD structured datának kell.
EVENT_TICKET_URL = COOLTIX_WIDGET_URL
EVENT_SLUG = "dubai-style"

COOLTIX_TICKET_BTN = f'<button type="button" class="btn filled magnetic" data-cooltix-event-products=\'{COOLTIX_EVENT_PRODUCT_ID}\'>JEGYVÁSÁRLÁS</button>'
COOLTIX_TABLE_BTN = f'<button type="button" class="btn magnetic" data-cooltix-event-products=\'{COOLTIX_EVENT_PRODUCT_ID}\'>ASZTALFOGLALÁS</button>'

# ---- Instagram poszt-linkek a galéria csempékhez (kattintásra a valódi posztra/reelre visz) ----
IG_FEATURED = "https://www.instagram.com/p/DYm2IkFilaO/"
IG_FASHIONSHOW_REPORT = "https://www.instagram.com/p/DV13-0SCPjM/"
IG_POPOUT = "https://www.instagram.com/p/DVopDD_DTAr/"
IG_AFROHOUSE_ANNOUNCE = "https://www.instagram.com/p/DUgQUjGgjmC/"
IG_MOMLEROY_TEASER = "https://www.instagram.com/p/DUThgzQEhK4/"
IG_MYRAZS_RECAP = "https://www.instagram.com/p/DT8UZeBAgkQ/"
IG_AFTERPARTY_TICKETS = "https://www.instagram.com/p/DU8rIVhgjz3/"
IG_MYRAZS_TICKET_PROMO = "https://www.instagram.com/p/DXuTi24DD-C/"
IG_MYRAZS_FEATHER_MIRAGE = "https://www.instagram.com/p/DaNzhxwCTw9/"

# ---- korábbi események: egy kártya = egy esemény, kattintásra saját aloldal ----
PAST_EVENTS = [
    {
        "slug": "dubai-style",
        "title": "Models on the Move × VIBE — Dubai Style",
        "venue": "VIBE Budapest",
        "date_label": "2026.10.16.",
        "date_full": "2026. október 16., péntek",
        "time_label": None,
        "cover": "dubai-style-flyer.jpg",
        "teaser": "A divat világa találkozott a VIBE karakteres hangulatával — Fabios és Mandmil Afro House szettjei egy felejthetetlen estén.",
        "intro": [
            "2026. október 16-án a Models on the Move × VIBE Budapest — Dubai Style elhozta a dubai éjszakák stílusát és energiáját Budapestre.",
            "A divat világa találkozott a VIBE karakteres hangulatával: Fabios és Mandmil Afro House szettjei, táncosok és élő előadók emelték új szintre az éjszakát.",
            "Exkluzív italok, bottle service és snackek egész este — az Early Bird jegyek egy nap alatt elfogytak, a terem hajnalig tartó Afro House partyvá változott.",
        ],
        "facts": [
            ("DÁTUM", "2026. október 16., péntek"),
            ("IDŐPONT", "23:00–03:00"),
            ("HELYSZÍN", "VIBE Budapest"),
            ("DRESS CODE", "Elegáns party stílus"),
            ("KORHATÁR", "18+"),
        ],
        "lineup": [
            ("Fabios", "Afro House"),
            ("Mandmil", "Afro House"),
        ],
        "extras": ["Exkluzív italok", "Bottle service", "Early Bird jegyek 1 nap alatt elfogytak"],
        "gallery": ["vibe-jungle-lounge.jpg", "vibe-bartrio-final.jpg", "vibe-redroom-group.jpg", "vibe-table-group.jpg", "vibe-cellar-table.jpg"],
        "video": None,
    },
    {
        "slug": "myrazs-fashion-show",
        "title": "Myrázs Szülinapi Divatbemutató & After Party",
        "venue": "MOM Leroy Bistro",
        "date_label": "2026.01.09.",
        "date_full": "2026. január 9., péntek",
        "time_label": "18:00-tól",
        "cover": "ig-myrazs-recap.jpg",
        "teaser": "A Myrázs első kollekciójának bemutatója, majd After Party — ez indította el a rendszeres estéinket.",
        "intro": [
            "A Myrázs szülinapi divatbemutatója volt az első nagy MODELS ON THE MOVE party — a hatalmas érdeklődésre való tekintettel ez indította el a rendszeres estéink sorát.",
            "18:00–20:00 érkezés és vacsora, majd 20:00-tól a Myrázs bemutatta első kollekcióját, extra produkciókkal, tombolával és utána Myrázs After Partyval zárva az estét.",
        ],
        "facts": [
            ("DÁTUM", "2026. január 9., péntek"),
            ("IDŐPONT", "18:00-tól"),
            ("HELYSZÍN", "MOM Leroy Bistro"),
            ("LÉTSZÁM", "kb. 400 fő"),
        ],
        "lineup": [
            ("Myrázs", "Divatbemutató — első kollekció"),
            ("Nagy Nikol", "Extra produkció"),
            ("Gyulai Viktória", "Extra produkció"),
            ("Moani (Zsombor Dudás-Kass)", "DJ"),
        ],
        "extras": ["Tombola értékes nyereményekkel", "Myrázs After Party"],
        "gallery": ["ig-myrazs-recap.jpg"],
        "video": None,
    },
    {
        "slug": "afro-house-night",
        "title": "Afro House Night",
        "venue": "MOM Leroy Bistro",
        "date_label": "2026.02.27.",
        "date_full": "2026. február 27., péntek",
        "time_label": "19:00–03:00",
        "cover": "ig-afrohouse-announce.jpg",
        "teaser": "Vacsora, fashion show, majd hajnalig tartó Afro House party a MOM Leroy Bistróban.",
        "intro": [
            "Exkluzív vacsora, látványos fashion show, majd 22:30-tól hajnalig tartó Afro House party a MOM Leroy Bistróban.",
            "19:00 kapunyitás, 21:30 fashion show, 22:00 tombolahúzás, 22:30-tól Afro House party a POP OUT csapatával.",
        ],
        "facts": [
            ("DÁTUM", "2026. február 27., péntek"),
            ("IDŐPONT", "19:00–03:00"),
            ("HELYSZÍN", "MOM Leroy Bistro"),
            ("LÉTSZÁM", "forgóban nagyjából 500 fő"),
        ],
        "lineup": [
            ("Myrázs", "Fashion show"),
            ("Individual", "Fashion show"),
            ("POP OUT", "Afro House DJ-k"),
            ("Molnár Fábi", "DJ"),
            ("Moani", "DJ"),
        ],
        "extras": ["Welcome drink early bird jeggyel", "Tombola értékes nyereményekkel", "Dress code: Cool – Elegant"],
        "gallery": [],
        "video": None,
    },
    {
        "slug": "szezonnyito",
        "title": "Szezonnyitó — Day Time Party & Fashion Show",
        "venue": "MOM Leroy Bistro",
        "date_label": "2026.05.29.",
        "date_full": "2026. május 29., péntek",
        "time_label": "16:00–00:00",
        "cover": "leroy-szezonnyito.jpg",
        "teaser": "Két fashion show, élő DJ-k és napközbeni luxury hangulat a MOM Leroy teraszán.",
        "intro": [
            "A szezonnyitó estén a divat, a zene és a közösség találkozott a MOM Leroy Bistróban — napközbeni luxury experience-ként indult, és éjszakába nyúló partyvá alakult.",
            "Két fashion show, élő DJ-szettek, pop-up store és tombola tette emlékezetessé az estét, a teljesen megnyitott teraszon.",
        ],
        "facts": [
            ("DÁTUM", "2026. május 29., péntek"),
            ("IDŐPONT", "16:00–00:00"),
            ("HELYSZÍN", "MOM Leroy Bistro"),
            ("LÉTSZÁM", "kb. 300 fő"),
        ],
        "lineup": [
            ("Myrázs", "Fashion show"),
            ("In My Style", "Fashion show"),
            ("Szőke Rebeka (Sz_Becca)", "DJ"),
            ("Fabiosz x Soma", "DJ"),
        ],
        "extras": ["Pop-up store", "Tombola és meglepetések", "Teljes terasz élmény", "Food & drink experience"],
        "gallery": [],
        "video": {"src": "hero-myrazs.mp4", "poster": "hero-myrazs-poster.jpg"},
    },
]


def _event_card(ev, depth_prefix="../assets/", link_prefix="../esemenyek/"):
    return f"""      <a class="event-card glow-card" href="{link_prefix}{ev['slug']}/">
        <div class="plate photo grain" style="background-image:url('{depth_prefix}{ev['cover']}')"></div>
        <div class="event-card-body">
          <h3>{ev['title']}</h3>
          <div class="meta-line">{ev['venue']} · {ev['date_label']}</div>
          <p>{ev['teaser']}</p>
        </div>
      </a>"""


def _fact_rows(facts):
    return "\n".join(f'          <div><span>{k}</span><span>{v}</span></div>' for k, v in facts)


def _lineup_rows(lineup):
    if not lineup:
        return ""
    rows = "\n".join(
        f'          <div class="dj"><span class="name">{name}</span><span class="meta"><span class="genre">{role}</span></span></div>'
        for name, role in lineup
    )
    return f"""
        <div class="lineup" style="margin-top:40px;">
          <h4>KÖZREMŰKÖDŐK</h4>
{rows}
        </div>"""


def _extras_html(extras):
    if not extras:
        return ""
    tags = "".join(f'<span class="tag">{e}</span>' for e in extras)
    return f'\n        <div class="audience-row" style="margin-top:28px;">{tags}</div>'


def _gallery_html(ev):
    tiles = []
    if ev.get("video"):
        tiles.append(f"""      <div class="gtile wide glow-card">
        <video class="gtile-video" autoplay muted loop playsinline controls poster="../../assets/{ev['video']['poster']}">
          <source src="../../assets/{ev['video']['src']}" type="video/mp4">
        </video>
        <span class="gtile-badge">▶ VIDEÓ</span>
      </div>""")
    for i, img in enumerate(ev["gallery"]):
        wide = " wide" if i == 0 and not ev.get("video") else ""
        tiles.append(f"""      <div class="gtile{wide} glow-card"><div class="plate photo grain" style="background-image:url('../../assets/{img}')"></div></div>""")
    return "\n\n".join(tiles)


def past_event_detail_body(ev):
    intro_html = "\n        ".join(f"<p>{p}</p>" for p in ev["intro"])
    time_row = f'\n          <div><span>IDŐPONT</span><span>{ev["time_label"]}</span></div>' if ev.get("time_label") else ""
    gallery_section = ""
    if ev.get("video") or ev.get("gallery"):
        gallery_section = f"""
<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">GALÉRIA</span><h2>Ízelítő az estéből.</h2></div>
    <div class="gallery-grid rv-stagger">
{_gallery_html(ev)}
    </div>
  </div>
</section>"""
    return f"""
<section class="hero" style="min-height:56vh;">
  <div class="plate photo grain" style="background-image:url('../../assets/{ev['cover']}');background-position:center 28%;"></div>
  <a href="../" class="event-hero-back rv" style="position:absolute;top:110px;left:48px;z-index:3;">← ÖSSZES ESEMÉNY</a>
</section>

<section class="pad rule" style="padding-top:60px;padding-bottom:60px;">
  <div class="wrap">
    <div class="hero-kicker rv"><span class="dot"></span><span class="eyebrow">KORÁBBI ESTÉNK</span></div>
    <h1 class="rv" style="font-family:var(--sans);font-weight:800;text-transform:uppercase;font-size:clamp(30px,5.6vw,64px);line-height:1.02;letter-spacing:-.01em;margin-top:18px;max-width:900px;">{ev['title']}</h1>
    <div class="event-two-col rv" style="margin-top:44px;">
      <div>
        {intro_html}{_lineup_rows(ev['lineup'])}{_extras_html(ev['extras'])}
      </div>
      <div>
        <div class="event-facts">
{_fact_rows(ev['facts'])}{time_row}
        </div>
      </div>
    </div>
  </div>
</section>

{gallery_section}

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Szerveznél hasonló estét a márkádnak?</h2>
    <div class="ctas"><a href="../../projekt-inditasa/" class="btn filled magnetic">INDÍTSUK EL A PROJEKTED</a></div>
  </div>
</section>
"""


# ---- főoldali hero "felúszó eseménykártya" — csak akkor jelenik meg, ha van
# ténylegesen aktív/meghirdetett következő esemény. Ha van, töltsd ki:
# ACTIVE_EVENT = {"name": "Esemény neve", "date_label": "2026. november 14., szombat", "venue": "Helyszín"}
ACTIVE_EVENT = None

# ---- /esemenyek/ — a brief 4.2 szerint: szöveg még nem végleges ("később
# érkezik"), ezért itt csak a tervezett szerkezet épül fel helyőrző szöveggel.
# Tervezett elemek: következő esemény (dátum, helyszín típusa anonim módon,
# hangulat), jegyvásárlás gomb, VIP-asztalfoglalás (csak ha az adott bulin
# elérhető), dress code, GYIK. Helyszín/influencer NEVE nem jelenhet meg —
# csak típus/hangulat szerinti, anonimizált leírás.
EVENTS_BODY = f"""
%%BREADCRUMB%%
<section class="gal-hero">
  <div class="wrap">
    <div class="rv">
      <span class="eyebrow">ESEMÉNYEK</span>
      <h1>Esték, amelyekről még hetekig beszélnek.</h1>
      <p>Válogatott közönség, prémium budapesti helyszín, VIP-asztalok — [a következő esemény hangulatának rövid leírása következik ide, helyszín- és névmegjelölés nélkül].</p>
    </div>
  </div>
</section>

<section class="pad rule" id="kovetkezo" style="padding-top:60px;">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KÖVETKEZŐ ESEMÉNYÜNK</span><h2>[Esemény jellege] · [dátum]</h2>
      <p>[Rövid, hangulati leírás a következő estéről — helyszín típusa, de nem neve; dress code; mire számíthatsz.]</p>
    </div>
    <div class="ctas" style="margin-top:30px;justify-content:center;display:flex;gap:16px;flex-wrap:wrap;">
      <a href="#" class="btn filled magnetic">JEGYVÁSÁRLÁS</a>
      <a href="../projekt-inditasa/" class="btn magnetic">VIP-ASZTALFOGLALÁS</a>
    </div>
    <p style="margin-top:18px;text-align:center;font-size:12.5px;color:var(--ivory-dimmer);">A VIP-asztalfoglalás csak akkor jelenik meg, ha az adott estén elérhető.</p>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">GYAKORI KÉRDÉSEK</span><h2>Amit az esténkről érdemes tudni.</h2>
      <p>[Helyőrző — a végleges kérdés-válasz lista a részletes szöveg megérkezésével kerül ide: dress code, korhatár, jegytípusok, VIP-asztal.]</p>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">KORÁBBI ESTÉINK</span><h2>Nézd meg, mi történt eddig.</h2></div>
    <div style="text-align:center;"><a href="../korabbi-esemenyek/" class="btn magnetic">KORÁBBI ESEMÉNYEK →</a></div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Szerveznél hasonló estét a márkádnak?</h2>
    <div class="ctas"><a href="../projekt-inditasa/" class="btn filled magnetic">INDÍTSUK EL A PROJEKTED</a></div>
  </div>
</section>
"""

# ---- /korabbi-esemenyek/ — a brief 4.3 szerint: szöveg később érkezik,
# tervezett szerkezet: galéria, eseményfilm, eredmények. Az eseményekre név
# nélkül hivatkozunk ("legutóbbi eseményünk"), helyszínnév nélkül.
# A kártyák egyelőre a meglévő esemény-aloldalakra mutatnak (ott még a régi,
# nem anonimizált részletek — ez külön átnézendő, lásd a végső összefoglalót).
KORABBI_ESEMENYEK_BODY = f"""
%%BREADCRUMB%%
<section class="gal-hero">
  <div class="wrap">
    <div class="rv">
      <span class="eyebrow">KORÁBBI ESEMÉNYEK</span>
      <h1>Egy pillantás arra, ami már megtörtént.</h1>
      <p>Galéria és eredmények a korábbi estjeinkről — [a végleges bevezető szöveg később érkezik].</p>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="event-cards-row rv-stagger">
{chr(10).join(_event_card(ev) for ev in PAST_EVENTS)}
    </div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Szerveznél hasonló estét a márkádnak?</h2>
    <div class="ctas"><a href="../projekt-inditasa/" class="btn filled magnetic">INDÍTSUK EL A PROJEKTED</a></div>
  </div>
</section>
"""


