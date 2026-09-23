# -*- coding: utf-8 -*-
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import shell
from shell import page, breadcrumb, service_page, BASE_URL
from content_home import HOME_BODY
from content_services import SERVICES
from content_pages import MUNKAINK_BODY, ROLUNK_BODY, KAPCSOLAT_BODY, NOTFOUND_BODY
from content_events import EVENTS_BODY, REDIRECT_HTML, EVENT_DETAIL_BODY, EVENT_SLUG, EVENT_TICKET_URL, EVENT_TABLE_URL


def write(rel_path, content):
    full = os.path.join(SITE_ROOT, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel_path, len(content), "bytes")


def main():
    routes = []  # (path, priority, changefreq)

    # ---- shared external assets (cached across all pages) ----
    write("assets/site.css", shell.FULL_STYLE)
    js = shell.SCRIPT.strip()
    if js.startswith("<script>"):
        js = js[len("<script>"):]
    if js.endswith("</script>"):
        js = js[: -len("</script>")]
    write("assets/site.js", js.strip() + "\n")

    # ---- HOME ----
    home_html = page(
        title="Models on the Move — Modellek, influencerek, marketing és események, Budapest",
        description="Modellek és influencerek, teljes körű marketing, kreatív produkciók és események egyetlen összehangolt budapesti csapattól. Embereket, márkákat és élményeket kapcsolunk össze.",
        canonical_path="",
        body=HOME_BODY,
        depth=0,
        active="home",
    )
    write("index.html", home_html)
    routes.append(("", "1.0", "weekly"))

    # ---- SERVICE PAGES ----
    for svc in SERVICES:
        html = service_page(svc)
        write(f"{svc['slug']}/index.html", html)
        routes.append((svc["slug"] + "/", "0.9", "monthly"))

    # ---- MUNKAINK ----
    body = MUNKAINK_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Munkáink", None)], depth=1))
    html = page(
        title="Munkáink — Models on the Move referenciák",
        description="Weboldalak, marketingrendszerek, kampányok, tartalmak és események, amelyeket a Models on the Move összehangolt egészként valósított meg.",
        canonical_path="munkaink/",
        body=body,
        depth=1,
        active="works",
    )
    write("munkaink/index.html", html)
    routes.append(("munkaink/", "0.7", "monthly"))

    # ---- ROLUNK ----
    body = ROLUNK_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Rólunk", None)], depth=1))
    html = page(
        title="Rólunk — Models on the Move csapata",
        description="A Models on the Move Molnár Mira és Bajzáth Balázs közös projektje — két világ, modellek, marketing és események, egy közös vízió.",
        canonical_path="rolunk/",
        body=body,
        depth=1,
        active="about",
    )
    write("rolunk/index.html", html)
    routes.append(("rolunk/", "0.7", "monthly"))

    # ---- KAPCSOLAT ----
    body = KAPCSOLAT_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Kapcsolat", None)], depth=1))
    html = page(
        title="Kapcsolat — Ajánlatkérés | Models on the Move",
        description="Kérj ajánlatot modellközvetítésre, marketingre, rendezvényszervezésre vagy weboldalkészítésre. Mondd el, mit szeretnél elérni — beszéljük át személyesen.",
        canonical_path="kapcsolat/",
        body=body,
        depth=1,
        active="contact",
    )
    write("kapcsolat/index.html", html)
    routes.append(("kapcsolat/", "0.9", "monthly"))

    # ---- ESEMENYEK ----
    body = EVENTS_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Események", None)], depth=1))
    html = page(
        title="Események — Models on the Move Budapest",
        description="A Models on the Move aktuális és korábbi eseményei Budapesten — fotók, összefoglaló videók és a következő est részletei.",
        canonical_path="esemenyek/",
        body=body,
        depth=1,
        active="events",
    )
    write("esemenyek/index.html", html)
    routes.append(("esemenyek/", "0.8", "weekly"))

    # ---- ESEMENY DETAIL: Dubai Style (VIBE x MOTM, 2026.10.16.) ----
    event_jsonld = f"""
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Models on the Move × VIBE — Dubai Style",
  "startDate": "2026-10-16T23:00:00+02:00",
  "endDate": "2026-10-17T03:00:00+02:00",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {{
    "@type": "Place",
    "name": "VIBE Budapest",
    "address": {{"@type": "PostalAddress", "addressLocality": "Budapest", "addressCountry": "HU"}}
  }},
  "image": ["{BASE_URL}/assets/hero-champagne.jpg"],
  "description": "A Models on the Move x VIBE Budapest Dubai Style estje Fabios és Mandmil Afro House DJ-szettjeivel.",
  "performer": [
    {{"@type": "PerformingGroup", "name": "Fabios"}},
    {{"@type": "PerformingGroup", "name": "Mandmil"}}
  ],
  "organizer": {{"@type": "Organization", "name": "Models on the Move", "url": "{BASE_URL}/"}},
  "offers": [
    {{"@type": "Offer", "name": "Early Bird", "price": "4000", "priceCurrency": "HUF", "url": "{EVENT_TICKET_URL}", "availability": "https://schema.org/InStock"}},
    {{"@type": "Offer", "name": "Elővételes jegy", "price": "6000", "priceCurrency": "HUF", "url": "{EVENT_TICKET_URL}", "availability": "https://schema.org/InStock"}},
    {{"@type": "Offer", "name": "Helyszíni jegy", "price": "8000", "priceCurrency": "HUF", "url": "{EVENT_TICKET_URL}", "availability": "https://schema.org/InStock"}}
  ]
}}
</script>"""
    html = page(
        title="Models on the Move × VIBE — Dubai Style | 2026.10.16.",
        description="2026. október 16. — Models on the Move × VIBE Budapest, Dubai Style. Fabios és Mandmil Afro House szettjei, jegyek és asztalfoglalás.",
        canonical_path=f"esemenyek/{EVENT_SLUG}/",
        body=EVENT_DETAIL_BODY,
        depth=2,
        active="events",
        og_image="assets/hero-champagne.jpg",
        extra_jsonld=event_jsonld,
    )
    write(f"esemenyek/{EVENT_SLUG}/index.html", html)
    routes.append((f"esemenyek/{EVENT_SLUG}/", "0.9", "daily"))

    # old flat esemenyek.html -> redirect to esemenyek/
    write("esemenyek.html", REDIRECT_HTML.format(base=BASE_URL))

    # ---- 404 ----
    write("404.html", page(
        title="404 — Az oldal nem található | Models on the Move",
        description="A keresett oldal nem található.",
        canonical_path="404.html",
        body=NOTFOUND_BODY,
        depth=0,
        robots="noindex,follow",
    ))

    # ---- sitemap.xml ----
    urls = []
    for path, prio, freq in routes:
        loc = f"{BASE_URL}/{path}"
        urls.append(f"  <url>\n    <loc>{loc}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>")
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "\n".join(urls) + "\n</urlset>\n")
    write("sitemap.xml", sitemap)

    # ---- robots.txt ----
    robots = f"""User-agent: *
Allow: /
Disallow: /404.html

Sitemap: {BASE_URL}/sitemap.xml
"""
    write("robots.txt", robots)

    print(f"\nKész: {len(routes)} indexelhető route + 404 + sitemap + robots.")


if __name__ == "__main__":
    main()
