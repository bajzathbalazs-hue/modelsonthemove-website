# -*- coding: utf-8 -*-
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import shell
from shell import page, breadcrumb, BASE_URL
from content_home import HOME_BODY
from content_pages import ROLUNK_BODY, KAPCSOLAT_BODY, NOTFOUND_BODY
from content_events import EVENTS_BODY, KORABBI_ESEMENYEK_BODY
from content_arculat import ARCULAT_BODY
from content_marketing_ai import MARKETING_AI_BODY
from content_influencer import INFLUENCER_BODY
from content_tartalomgyartas import TARTALOMGYARTAS_BODY
from content_projekt import PROJEKT_BODY


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
        title="Models on the Move — Prémium események, arculat és marketing | Budapest",
        description="Prémium eseményeket szervezünk, és ugyanezzel az igényességgel építjük fel a vállalkozásod arculatát, weboldalát és online jelenlétét. Marketing és influencer-együttműködés.",
        canonical_path="",
        body=HOME_BODY,
        depth=0,
        active="home",
    )
    write("index.html", home_html)
    routes.append(("", "1.0", "weekly"))

    # ---- ESEMÉNYEK ----
    body = EVENTS_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Események", None)], depth=1))
    html = page(
        title="Események — Models on the Move Budapest",
        description="A Models on the Move következő estje: válogatott vendégkör, prémium helyszín, VIP-asztalok.",
        canonical_path="esemenyek/",
        body=body,
        depth=1,
        active="events",
    )
    write("esemenyek/index.html", html)
    routes.append(("esemenyek/", "0.9", "weekly"))

    # ---- KORÁBBI ESEMÉNYEK (összefoglaló oldal) ----
    body = KORABBI_ESEMENYEK_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Események", "esemenyek/"), ("Korábbi események", None)], depth=1))
    html = page(
        title="Korábbi események — Models on the Move Budapest",
        description="Galéria és eredmények a Models on the Move korábbi estjeiről.",
        canonical_path="korabbi-esemenyek/",
        body=body,
        depth=1,
        active="events",
    )
    write("korabbi-esemenyek/index.html", html)
    routes.append(("korabbi-esemenyek/", "0.7", "monthly"))

    # NOTE: 2026.10.29 óta a korábbi, név/helyszín-szerinti esemény-aloldalak
    # (pl. /esemenyek/dubai-style/) megszűntek — a végleges brief 10-oldalas
    # oldaltérképében nincs helyük, és ügyfél-/helyszín-/eseménynevet nem
    # tartalmazhatnak (0. pont). A korábbi tartalom anonimizált, összevont
    # formában a /korabbi-esemenyek/ oldalon él tovább. A régi URL-ek a
    # _redirects fájlban 301-gyel idekerülnek.

    # ---- ARCULAT ÉS WEBFEJLESZTÉS ----
    body = ARCULAT_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Arculat és webfejlesztés", None)], depth=1))
    html = page(
        title="Arculat és webfejlesztés — Models on the Move",
        description="Logótól a weboldalig: márkaarculat, weboldal, webshop tervezése és fejlesztése, prémium kivitelben.",
        canonical_path="arculat-es-webfejlesztes/",
        body=body,
        depth=1,
        active="arculat",
    )
    write("arculat-es-webfejlesztes/index.html", html)
    routes.append(("arculat-es-webfejlesztes/", "0.9", "monthly"))

    # ---- MARKETING ÉS AI ----
    body = MARKETING_AI_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Marketing és AI", None)], depth=1))
    html = page(
        title="Marketing és AI — Models on the Move",
        description="Marketing, amelyből bevétel lesz. SEO, Google Ads, Meta- és TikTok-hirdetések, közösségi média, AI és automatizáció cégeknek.",
        canonical_path="marketing-es-ai/",
        body=body,
        depth=1,
        active="marketing",
    )
    write("marketing-es-ai/index.html", html)
    routes.append(("marketing-es-ai/", "0.9", "monthly"))

    # ---- INFLUENCER-EGYÜTTMŰKÖDÉS ----
    body = INFLUENCER_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Influencer-együttműködés", None)], depth=1))
    html = page(
        title="Influencer-együttműködés — Models on the Move",
        description="Állandó influencerhálózatunkkal hiteles megjelenést építünk, a kiválasztástól a mérhető eredményig.",
        canonical_path="influencer-egyuttmukodes/",
        body=body,
        depth=1,
        active="influencer",
    )
    write("influencer-egyuttmukodes/index.html", html)
    routes.append(("influencer-egyuttmukodes/", "0.9", "monthly"))

    # ---- TARTALOMGYÁRTÁS ----
    body = TARTALOMGYARTAS_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Tartalomgyártás", None)], depth=1))
    html = page(
        title="Tartalomgyártás — Models on the Move",
        description="Reklámfilm, közösségi videók, fotózás és eseményfilm — teljes gyártásszervezéssel, egy kapcsolattartóval.",
        canonical_path="tartalomgyartas/",
        body=body,
        depth=1,
        active="tartalom",
    )
    write("tartalomgyartas/index.html", html)
    routes.append(("tartalomgyartas/", "0.8", "monthly"))

    # ---- ROLUNK ----
    body = ROLUNK_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Rólunk", None)], depth=1))
    html = page(
        title="Rólunk — Models on the Move csapata",
        description="Bajzáth Balázs és Molnár Míra, a Models on the Move alapítói — stratégia, weboldal, marketing, tartalom és influencerkapcsolatok egy kézben.",
        canonical_path="rolunk/",
        body=body,
        depth=1,
        active="about",
    )
    write("rolunk/index.html", html)
    routes.append(("rolunk/", "0.6", "monthly"))

    # ---- KAPCSOLAT ----
    body = KAPCSOLAT_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Kapcsolat", None)], depth=1))
    html = page(
        title="Kapcsolat | Models on the Move",
        description="Írj nekünk — egy munkanapon belül válaszolunk.",
        canonical_path="kapcsolat/",
        body=body,
        depth=1,
        active="contact",
    )
    write("kapcsolat/index.html", html)
    routes.append(("kapcsolat/", "0.8", "monthly"))

    # ---- PROJEKT INDÍTÁSA ----
    body = PROJEKT_BODY.replace("%%BREADCRUMB%%", breadcrumb([("Projekt indítása", None)], depth=1))
    html = page(
        title="Projekt indítása — Models on the Move",
        description="Mondd el, mit szeretnél. A többit mi intézzük — néhány kérdés, és személyre szabott javaslattal jelentkezünk.",
        canonical_path="projekt-inditasa/",
        body=body,
        depth=1,
        active="",
    )
    write("projekt-inditasa/index.html", html)
    routes.append(("projekt-inditasa/", "0.9", "monthly"))

    # NOTE: intentionally NOT writing a physical esemenyek.html file here.
    # On Netlify, a static esemenyek.html sitting next to the esemenyek/ directory
    # makes Netlify's pretty-URL resolution treat esemenyek.html as canonical and
    # 301-redirect esemenyek/ -> esemenyek, whose content then meta-refreshes back
    # to esemenyek/ — an infinite redirect loop (broke hard in Safari). The legacy
    # /esemenyek.html bookmark is instead handled by the _redirects rule below.

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

    # ---- CNAME (GitHub Pages custom domain) ----
    domain = BASE_URL.replace("https://", "").replace("http://", "").rstrip("/")
    write("CNAME", domain + "\n")

    # ---- _redirects (Netlify) ----
    # 2026.10.29: a site teljes IA-átépítése (10-oldalas sitemap). A régi
    # szolgáltatás-oldalak URL-jei 301-gyel a legközelebbi új oldalra mutatnak,
    # hogy a meglévő linkek/keresőbeli helyezés ne vesszen el.
    redirects = """/esemenyek.html  /esemenyek/  301
/modellugynokseg/*  /influencer-egyuttmukodes/  301
/influencer-marketing/*  /influencer-egyuttmukodes/  301
/marketing-ugynokseg/*  /marketing-es-ai/  301
/rendezvenyszervezes/*  /esemenyek/  301
/reklamfilm-keszites/*  /tartalomgyartas/  301
/weboldal-keszites/*  /arculat-es-webfejlesztes/  301
/kozossegi-media-kezeles/*  /marketing-es-ai/  301
/munkaink/*  /  301
/esemenyek/dubai-style/*  /korabbi-esemenyek/  301
/esemenyek/myrazs-fashion-show/*  /korabbi-esemenyek/  301
/esemenyek/afro-house-night/*  /korabbi-esemenyek/  301
/esemenyek/szezonnyito/*  /korabbi-esemenyek/  301
"""
    write("_redirects", redirects)

    print(f"\nKész: {len(routes)} indexelhető route + 404 + sitemap + robots + CNAME + _redirects ({domain}).")


if __name__ == "__main__":
    main()
