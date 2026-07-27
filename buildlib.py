# -*- coding: utf-8 -*-
"""
Sdílené díly pro generátory stránek.

Hlavička, mobilní menu, patička, volací lišta a cookie lišta se čtou přímo
z index.html — existují tedy na jednom místě a nemůžou se rozejít.
"""

import pathlib
import re

ROOT = pathlib.Path(__file__).parent

TEL = "+420723965990"
TEL_HUMAN = "723 965 990"
SITE = "https://www.rychly-zamecnik.cz"

ICO = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
       'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{}</svg>')

PHONE_PATH = ('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 '
              '19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 '
              '2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 '
              '2.81.7A2 2 0 0 1 22 16.92z"/>')

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')

CALL_BTN = (f'<a class="btn btn--lg btn--call" data-magnetic="0.25" href="tel:{TEL}">'
            f'{ICO.format(PHONE_PATH)}\n        {TEL_HUMAN}\n      </a>')


def grab(pattern: str, source: str, what: str) -> str:
    m = re.search(pattern, source, re.S)
    if not m:
        raise SystemExit(f"buildlib: v index.html chybí blok „{what}“")
    return m.group(0)


def load_chrome() -> dict:
    """Vytáhne sdílené části z index.html a přepíše cesty na absolutní."""
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    chrome = {
        "header": grab(r'<header class="header">.*?</header>', src, "hlavička"),
        "mobilenav": grab(r'<nav class="mobile-nav".*?</nav>', src, "mobilní menu"),
        "footer": grab(r'<footer class="footer">.*?</footer>', src, "patička"),
        "callbar": grab(r'<div class="call-bar">.*?</div>\s*(?=<!-- Cookie)', src, "volací lišta"),
        "cookiebar": grab(r'<aside class="cookiebar".*?</aside>', src, "cookie lišta"),
    }
    for key, frag in chrome.items():
        frag = re.sub(r'href="#(?!top\b)', 'href="/#', frag)
        frag = frag.replace('href="#top"', 'href="/"')
        frag = frag.replace('src="assets/', 'src="/assets/')
        chrome[key] = frag
    return chrome


def document(*, lang="cs", title, desc, canonical, og_image=None,
             head_extra="", body, chrome, og_type="website") -> str:
    """Obalí obsah stránky kompletním HTML dokumentem se sdíleným chrome."""
    img = og_image or f"{SITE}/assets/img/hero-van-night.webp"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#060806">
<link rel="canonical" href="{canonical}">

<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="cs_CZ">
<meta property="og:site_name" content="Rychlý Zámečník — Zámečnická pohotovost Praha">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{img}">

<link rel="icon" href="/assets/img/logo.webp">
<link rel="stylesheet" href="/assets/css/style.css">
{head_extra}
</head>

<body>
<div class="progress" aria-hidden="true"></div>

{chrome['header']}

{chrome['mobilenav']}

{body}

{chrome['footer']}

{chrome['callbar']}

{chrome['cookiebar']}

<script src="/assets/js/vendor/lenis.min.js"></script>
<script src="/assets/js/main.js"></script>
</body>
</html>
"""


def crumbs(*items) -> str:
    """items = (label, href|None) — poslední bez odkazu."""
    lis = []
    for label, href in items:
        inner = f'<a href="{href}">{label}</a>' if href else f'<span aria-current="page">{label}</span>'
        lis.append(f"        <li>{inner}</li>")
    return ('    <nav aria-label="Drobečková navigace">\n      <ol class="crumbs">\n'
            + "\n".join(lis) + "\n      </ol>\n    </nav>")


def cta_section(head, text) -> str:
    return f"""<section class="section section--tight">
  <div class="shell">
    <div class="cta-band" data-reveal>
      <div class="cta-band__media" data-parallax="0.12">
        <img src="/assets/img/tym-zamecniku.webp" alt="Tým zámečníků Rychlý Zámečník" loading="lazy">
      </div>
      <span class="badge-live"><span class="dot"></span> Nonstop 24/7, i o svátcích</span>
      <h2 data-split>{head}</h2>
      <p>{text}</p>
      <div class="hero__actions">
        {CALL_BTN}
        <a class="btn btn--lg btn--ghost" href="mailto:info@rychly-zamecnik.cz">Napsat e-mail</a>
      </div>
    </div>
  </div>
</section>"""
