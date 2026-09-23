# Models on the Move — weboldal

Statikus, több oldalas weboldal (nincs build-eszköz futásidőben — az oldalak egy Python
generátorral készülnek, majd sima HTML/CSS/JS fájlként kerülnek ki, amit bármilyen
statikus hosting kiszolgálhat, jelenleg GitHub Pages).

Élő oldal: https://bajzathbalazs-hue.github.io/modelsonthemove-website/

## Hogyan működik ez a rendszer

A látható `.html` fájlok (pl. `index.html`, `modellugynokseg/index.html`) **generáltak** —
ne szerkeszd őket közvetlenül, mert a következő build felülírja őket. A tényleges forrás
a `build/` mappában van:

- `build/shell.py` — közös fejléc/navigáció/lábléc/JS-keret, SEO meta-generátor, a
  `service_page()` sablon a 7 szolgáltatásoldalhoz
- `build/shared_style.css`, `build/ext_style.css` — a teljes design-rendszer (a kettő
  együtt egyetlen `assets/site.css` fájlba kerül buildeléskor)
- `build/legal_modals.html` — Impresszum / Adatkezelés / ÁSZF (bilingual HU/EN belül)
- `build/content_home.py`, `build/content_services.py`, `build/content_pages.py`,
  `build/content_events.py` — az egyes oldalak tényleges szövege/tartalma
- `build/build.py` — összeállítja és kiírja az összes oldalt, a `sitemap.xml`-t és a
  `robots.txt`-t

### Build futtatása

```bash
cd build
python3 build.py
```

Ez felülírja a repo gyökerében (és almappáiban) lévő összes generált `index.html`
fájlt, valamint az `assets/site.css` / `assets/site.js` fájlokat.

### Helyi előnézet

```bash
python3 -m http.server 8080
```

majd nyisd meg a `http://localhost:8080/` címet.

## Konfigurációs pontok (élesítés előtt ellenőrizendő)

Minden oldal `<script src="assets/site.js">`-t tölt be, ami az elején egy
`window.MOTM_CONFIG` objektumot definiál. Az alábbiakat kell kitölteni éles indításkor:

| Kulcs | Jelenlegi érték | Teendő |
|---|---|---|
| `formEndpoint` | üres string | Amíg üres, az űrlapok (üzleti ajánlatkérő, modelljelentkezés) **nem** állítják, hogy sikeresen elküldték az adatot — egy tájékoztató üzenetet mutatnak helyette. Állítsd be egy valódi form-fogadó endpoint URL-jére (pl. saját szerverless függvény), hogy éles beküldés induljon. |
| `analytics.ga4MeasurementId` | üres | Google Analytics 4 mérési azonosító |
| `analytics.googleSearchConsole` | üres | Search Console verifikációs kód |
| `analytics.metaPixelId` | üres | Meta Pixel azonosító |
| `analytics.googleAdsConversionId` | üres | Google Ads konverziókövetési azonosító |

Ezek a `build/shell.py`-ban a `SCRIPT` konstansban vannak — módosítás után futtasd
újra a buildet.

### Domain-csere

A `build/shell.py` tetején egyetlen konstans (`BASE_URL`) állítja be a canonical
URL-eket, az Open Graph tageket és a sitemap domainjét. Saját domain (pl.
`https://modelsonthemove.hu`) beállásakor **ezt az egy sort** kell átírni, majd
újra buildelni és publikálni — nincs más helyen hardcode-olva.

GitHub Pages nem támogat szerveroldali 301-es átirányítást egy domain-váltásnál;
DNS-átállás esetén a GitHub Pages saját "custom domain" beállítását és a
CNAME rekordot kell használni, a régi `github.io` cím pedig automatikusan
átirányít az új domainre, ha a "Custom domain" mezőben be van állítva.

## Hiányzó / jóváhagyásra váró tartalmak

- **Tárhelyszolgáltató adatai** az Impresszumban (`build/legal_modals.html`) —
  placeholder marad, amíg nincs végleges hosting.
- **Alapítói fotók** (Molnár Mira, Bajzáth Balázs) — a Rólunk és a főoldal jelenleg
  absztrakt színes plate-et használ fotó helyett, mert nincs jóváhagyott, valódi
  portréfotó. Csere: `content_home.py` és `content_pages.py` `.founder .plate`
  elemei.
- **Munkáink esettanulmányok** (Midas Property Management, BTK Kft.) — jelenleg
  monogramos absztrakt placeholder kártyák valódi projektfotó helyett, mert nincs
  jóváhagyott képanyag ezekhez a referenciákhoz.
- **Instagram / TikTok linkek** a fejlécben és a láblécben — jelenleg `#` placeholder,
  amíg nincs megadva a tényleges márka-fiók URL-je.
- **Form-beküldési endpoint** — lásd fentebb.

## Régi URL-ek

A korábbi `esemenyek.html` (lapos, nem clean-URL formátum) meta-refresh
átirányítással mutat az új `esemenyek/` route-ra, hogy a korábban megosztott
linkek ne törjenek el.
