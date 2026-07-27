#!/usr/bin/env python3
"""
Vygeneruje podstránky služeb na původních URL (/otevirani-dveri/ atd.).

Hlavička, mobilní menu, patička a volací lišta se berou přímo z index.html,
takže existují na jednom místě a nemůžou se rozejít. Obsah stránek je
v content/pages.py.

Spuštění:  python3 build-pages.py
"""

import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))
from content.pages import CENIK, PAGES  # noqa: E402

TEL = "+420723965990"
TEL_HUMAN = "723 965 990"
SITE = "https://www.rychly-zamecnik.cz"

ICONS = {
    "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "coin": '<path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
    "users": ('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>'
              '<path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>'),
    "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8-6.2-3.3-6.2 3.3L7 14.2l-5-4.9 6.9-1L12 2z"/>',
}

ICO = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
       'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{}</svg>')

PHONE_PATH = ('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 '
              '19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 '
              '2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 '
              '2.81.7A2 2 0 0 1 22 16.92z"/>')
TICK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


# --------------------------------------------------------------------------- #
# Sdílené části vytažené z index.html
# --------------------------------------------------------------------------- #
def grab(pattern: str, source: str) -> str:
    m = re.search(pattern, source, re.S)
    if not m:
        raise SystemExit(f"build-pages: v index.html chybí blok {pattern!r}")
    return m.group(0)


def load_chrome() -> dict:
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    chrome = {
        "header": grab(r'<header class="header">.*?</header>', src),
        "mobilenav": grab(r'<nav class="mobile-nav".*?</nav>', src),
        "footer": grab(r'<footer class="footer">.*?</footer>', src),
        "callbar": grab(r'<div class="call-bar">.*?</div>\s*(?=<!-- Cookie)', src),
        "cookiebar": grab(r'<aside class="cookiebar".*?</aside>', src),
    }
    # Na podstránce musí kotvy mířit zpátky na domovskou stránku.
    for key, frag in chrome.items():
        frag = re.sub(r'href="#(?!top\b)', 'href="/#', frag)
        frag = frag.replace('href="#top"', 'href="/"')
        frag = frag.replace('src="assets/', 'src="/assets/')
        chrome[key] = frag
    return chrome


# --------------------------------------------------------------------------- #
# Skládání sekcí
# --------------------------------------------------------------------------- #
def price_rows(key: str) -> str:
    return "\n".join(
        '        <div class="price-row"><span class="price-row__name">{}</span>'
        '<span class="price-row__dots"></span>'
        '<span class="price-row__val">{}</span></div>'.format(html.escape(name), html.escape(val))
        for name, val in CENIK[key]
    )


def why_cards(items) -> str:
    return "\n".join(
        '        <div class="why" data-reveal data-tilt="4">\n'
        '          <div class="why__ico">{ico}</div>\n'
        '          <h3>{h}</h3>\n'
        '          <p>{p}</p>\n'
        '        </div>'.format(ico=ICO.format(ICONS[icon]), h=html.escape(head), p=html.escape(body))
        for icon, head, body in items
    )


def faq_items(items) -> str:
    return "\n".join(
        '        <details>\n'
        '          <summary>{q}</summary>\n'
        '          <div class="faq__a"><p>{a}</p></div>\n'
        '        </details>'.format(q=html.escape(q), a=html.escape(a))
        for q, a in items
    )


def more_links(current: str) -> str:
    out = []
    for slug, p in PAGES.items():
        if slug == current:
            continue
        out.append(
            '        <a class="more" href="/{slug}/" data-reveal>{nav}{arrow}</a>'.format(
                slug=slug, nav=html.escape(p["nav"]), arrow=ARROW)
        )
    return "\n".join(out)


def json_ld(slug: str, p: dict) -> str:
    faq = ",\n".join(
        '    {{"@type":"Question","name":{q},'
        '"acceptedAnswer":{{"@type":"Answer","text":{a}}}}}'.format(
            q=jstr(q), a=jstr(a))
        for q, a in p["faq"]
    )
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Service",
      "name": {jstr(p['h1'])},
      "description": {jstr(p['desc'])},
      "serviceType": {jstr(p['nav'])},
      "areaServed": {{ "@type": "City", "name": "Praha" }},
      "provider": {{
        "@type": "Locksmith",
        "name": "Rychlý Zámečník — Zámečnická pohotovost Praha",
        "telephone": "{TEL}",
        "email": "info@rychly-zamecnik.cz",
        "url": "{SITE}/"
      }}
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Úvod", "item": "{SITE}/" }},
        {{ "@type": "ListItem", "position": 2, "name": {jstr(p['nav'])}, "item": "{SITE}/{slug}/" }}
      ]
    }},
    {{
      "@type": "FAQPage",
      "mainEntity": [
{faq}
      ]
    }}
  ]
}}
</script>"""


def jstr(s: str) -> str:
    """Bezpečný JSON řetězec (obsah je český text s uvozovkami a diakritikou)."""
    import json
    return json.dumps(s, ensure_ascii=False)


# --------------------------------------------------------------------------- #
def render(slug: str, p: dict, chrome: dict) -> str:
    ticks = "\n".join(
        f'          <li>{TICK}<span>{t}</span></li>' for t in p["ticks"]
    )
    prose = "\n".join(f"        <p>{x}</p>" for x in p["prose"])

    return f"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p['title'])}</title>
<meta name="description" content="{html.escape(p['desc'])}">
<meta name="theme-color" content="#060806">
<link rel="canonical" href="{SITE}/{slug}/">

<meta property="og:type" content="article">
<meta property="og:locale" content="cs_CZ">
<meta property="og:site_name" content="Rychlý Zámečník — Zámečnická pohotovost Praha">
<meta property="og:title" content="{html.escape(p['title'])}">
<meta property="og:description" content="{html.escape(p['desc'])}">
<meta property="og:url" content="{SITE}/{slug}/">
<meta property="og:image" content="{SITE}/assets/img/{p['img']}.webp">

<link rel="icon" href="/assets/img/logo.webp">
<link rel="stylesheet" href="/assets/css/style.css">

{json_ld(slug, p)}
</head>

<body>
<div class="progress" aria-hidden="true"></div>

{chrome['header']}

{chrome['mobilenav']}

<main id="top">

<!-- ======================= HERO PODSTRÁNKY ======================= -->
<section class="page-hero">
  <div class="page-hero__media" data-parallax="0.14">
    <img src="/assets/img/{p['img']}.webp" alt="{html.escape(p['img_alt'])}" fetchpriority="high">
  </div>

  <div class="shell">
    <nav aria-label="Drobečková navigace">
      <ol class="crumbs">
        <li><a href="/">Úvod</a></li>
        <li><a href="/#sluzby">Služby</a></li>
        <li><span aria-current="page">{html.escape(p['nav'])}</span></li>
      </ol>
    </nav>

    <span class="badge-live"><span class="dot"></span> Dispečink je právě teď na příjmu</span>

    <h1>{html.escape(p['h1'])}</h1>
    <p class="page-hero__lead">{html.escape(p['lead'])}</p>

    <ul class="ticks">
{ticks}
    </ul>

    <div class="hero__actions">
      <a class="btn btn--lg btn--call" data-magnetic="0.25" href="tel:{TEL}">
        {ICO.format(PHONE_PATH)}
        {TEL_HUMAN}
      </a>
      <a class="btn btn--lg btn--ghost" href="#cenik-sluzby">Ceník služby</a>
    </div>
  </div>
</section>

<!-- ======================= PROČ MY ======================= -->
<section class="section">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>Proč my</span>
        <h2 class="h-sec" data-split>{html.escape(p['why_head'])}</h2>
      </div>
      <p class="lead" data-reveal>{html.escape(p['why_lead'])}</p>
    </div>

    <div class="why-grid">
{why_cards(p['why'])}
    </div>
  </div>
</section>

<!-- ======================= CENÍK SLUŽBY ======================= -->
<section class="section" id="cenik-sluzby">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>Ceník</span>
        <h2 class="h-sec" data-split>Orientační ceny — {html.escape(p['nav'].lower())}</h2>
      </div>
      <p class="lead" data-reveal>
        Ceny jsou transparentní a all-inclusive. V ceně je doprava certifikovaného
        technika i záruka na práci a materiál.
      </p>
    </div>

    <div class="pricing" data-reveal>
      <div class="tab-panel">
{price_rows(p['prices'])}
      </div>
      <p class="pricing__note">
        {ICO.format('<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>')}
        <span>Ceny jsou orientační, „od“. Přesnou částku potvrdíme po telefonu nebo na místě
        <strong>před zahájením práce</strong>. Senioři a držitelé OZP mají nárok na slevu.
        <a href="/#cenik" style="color:var(--accent)">Zobrazit kompletní ceník</a>.</span>
      </p>
    </div>
  </div>
</section>

<!-- ======================= TEXT ======================= -->
<section class="section">
  <div class="shell">
    <span class="eyebrow" data-reveal>Dobré vědět</span>
    <h2 class="h-sec" data-split>{html.escape(p['prose_head'])}</h2>
    <div class="prose" style="margin-top:26px" data-reveal>
{prose}
    </div>
  </div>
</section>

<!-- ======================= FAQ ======================= -->
<section class="section">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>Časté dotazy</span>
        <h2 class="h-sec" data-split>Na co se ptáte nejčastěji</h2>
      </div>
      <p class="lead" data-reveal>
        Nenašli jste odpověď? Zavolejte — konzultace po telefonu je zdarma.
      </p>
    </div>

    <div class="faq" data-reveal>
{faq_items(p['faq'])}
    </div>
  </div>
</section>

<!-- ======================= DALŠÍ SLUŽBY ======================= -->
<section class="section">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>Další služby</span>
        <h2 class="h-sec" data-split>Co ještě umíme</h2>
      </div>
    </div>
    <div class="more-grid">
{more_links(slug)}
    </div>
  </div>
</section>

<!-- ======================= CTA ======================= -->
<section class="section section--tight">
  <div class="shell">
    <div class="cta-band" data-reveal>
      <div class="cta-band__media" data-parallax="0.12">
        <img src="/assets/img/tym-zamecniku.webp" alt="Tým zámečníků Rychlý Zámečník" loading="lazy">
      </div>
      <span class="badge-live"><span class="dot"></span> Nonstop 24/7, i o svátcích</span>
      <h2>Potřebujete pomoct hned?</h2>
      <p>
        Zavolejte nám. Konzultace je zdarma, cenu řekneme dopředu a technik
        vyjíždí okamžitě.
      </p>
      <div class="hero__actions">
        <a class="btn btn--lg btn--call" data-magnetic="0.25" href="tel:{TEL}">
          {ICO.format(PHONE_PATH)}
          {TEL_HUMAN}
        </a>
        <a class="btn btn--lg btn--ghost" href="mailto:info@rychly-zamecnik.cz">Napsat e-mail</a>
      </div>
    </div>
  </div>
</section>

</main>

{chrome['footer']}

{chrome['callbar']}

{chrome['cookiebar']}

<script src="/assets/js/vendor/lenis.min.js"></script>
<script src="/assets/js/main.js"></script>
</body>
</html>
"""


def main() -> None:
    chrome = load_chrome()
    for slug, p in PAGES.items():
        d = ROOT / slug
        d.mkdir(exist_ok=True)
        out = d / "index.html"
        out.write_text(render(slug, p, chrome), encoding="utf-8")
        print(f"  {slug}/index.html  ({out.stat().st_size / 1024:.0f} KB)")
    print(f"Hotovo — {len(PAGES)} podstránek.")


if __name__ == "__main__":
    main()
