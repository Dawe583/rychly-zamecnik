#!/usr/bin/env python3
"""
Vygeneruje jazykové mutace na /en/, /ru/ a /ua/.

Pro každý jazyk vzniká domovská stránka a šest podstránek služeb se stejnými
slugy jako česká verze — tedy /en/otevirani-dveri/ atd. Odpovídá to tomu,
jak adresy tvořil TranslatePress na původním webu.

Hlavička a patička se berou z index.html a přeloží se podle content/i18n.py.

Spuštění:  python3 build-i18n.py
"""

import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))

from buildlib import ARROW, ICO, PHONE_PATH, SITE, TEL, TEL_HUMAN, load_chrome  # noqa: E402
from content.i18n import CENIK_I18N, HOME, LANGS, LEGAL_I18N, SERVICES, UI  # noqa: E402
from content.pages import PAGES  # noqa: E402

LEGAL_SLUG = "zasady-ochrany-osobnich-udaju"

ICONS = {
    "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "coin": '<path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
    "users": ('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>'
              '<path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>'),
    "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8-6.2-3.3-6.2 3.3L7 14.2l-5-4.9 6.9-1L12 2z"/>',
}
TICK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M20 6 9 17l-5-5"/></svg>')
INFO = '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>'

# Recenze zůstávají v původním jazyce — jsou to citace skutečných lidí.
REVIEWS = [
    ("LK", "Lenka Kučerová", 5, "Spolehlivá a profesionální práce, velmi milé jednání, 100% doporučuji."),
    ("JG", "Jakub Grohol", 5, "Omylem zabouchnuté dveře a po zavolání okamžitý příjezd technika a do minuty jsme byli doma."),
    ("MD", "Michal Dzierža", 5, "Do 20 minut k nám dorazil a do 5 minut bylo vše vyřízeno. Naprostá spokojenost!"),
    ("PD", "Petr Dokoupil", 5, "Je smluvním technikem většiny pojišťoven, takže bylo vše hrazeno z pojištění domácnosti."),
    ("TV", "Tomáš Večerek", 5, "Přijel v co nejkratší době a rychlým a profesionálním přístupem rozsypaný zámek vyměnil."),
    ("LN", "Lili Nosková", 4, "Děkuji za otevření zabouchlých dveří. Hvězdička méně za zpoždění bez omluvy."),
    ("AK", "Adam Kučera", 5, "Dojezd technika byl 30 min od telefonátu. Velmi ochotný pán, poradil mi, jak řešit s pojišťovnou."),
    ("MJ", "Markéta Jirásková", 5, "Velice děkujeme za nedělní otevření zabouchnutých dveří. Rychlé a profesionální."),
    ("PP", "Pavel Poborský", 5, "Nouzové otevření zalomeného klíče proběhlo rychle i v sobotu. Přístup a jednání skvělé."),
    ("LM", "Linda Moore", 5, "Ztratila jsem klíče od bytu. Šikovný zámečník rychle přijel a hravě vše vyřešil."),
    ("TH", "Tom Hlavátý", 5, "Pán přijel obratem, krásná čistá práce bez poškození dveří! Doporučuji!"),
    ("ŠD", "Šárka Dytková", 5, "Doporučuji všemi deseti. Profesionální přístup, rychlost, dobrá domluva."),
]

DISTRICTS = [f"Praha {i}" for i in range(1, 23)]


# --------------------------------------------------------------------------- #
def langs_block(current: str, wide: bool) -> str:
    """Přepínač jazyků — odkazy míří na kořen dané mutace, čeština na /."""
    cls = "langs langs--wide" if wide else "langs"
    items = [("cs", "/", "Čeština" if wide else "CS", "cs")]
    for code, meta in LANGS.items():
        items.append((code, f"/{code}/", meta["name"] if wide else meta["short"],
                      meta["hreflang"]))
    links = []
    for code, href, label, hl in items:
        active = ' class="is-active" aria-current="true"' if code == current else ""
        links.append(f'    <a href="{href}" hreflang="{hl}"{active}>{label}</a>')
    return (f'<div class="{cls}" role="group" aria-label="{UI[current]["lang_label"]}">\n'
            + "\n".join(links) + "\n  </div>")


def localize_chrome(chrome: dict, lang: str) -> dict:
    """Přeloží sdílené části a přesměruje odkazy do jazykové větve."""
    t = UI[lang]
    out = {}
    base = f"/{lang}"

    nav_map = [
        ("Služby", t["nav_services"]), ("Proč my", t["nav_why"]),
        ("Jak to probíhá", t["nav_how"]), ("Ceník", t["nav_prices"]),
        ("Kde jezdíme", t["nav_area"]), ("Recenze", t["nav_reviews"]),
        ("Blog", t["nav_blog"]),
    ]
    svc_map = [(PAGES[s]["nav"], SERVICES[lang][s]["nav"]) for s in PAGES]

    for key, frag in chrome.items():
        # Přepínač jazyků vyjmeme, ať ho přepis odkazů nerozbije — vrátíme
        # ho až nakonec, sestavený pro aktuální jazyk.
        wide = 'langs--wide' in frag
        had_langs = 'class="langs' in frag
        frag = re.sub(r'<div class="langs.*?</div>', "@@LANGS@@", frag, flags=re.S)

        # Blog je zatím jen česky — v mutacích na něj neodkazujeme, aby odkaz
        # nevedl na neexistující stránku.
        frag = re.sub(r'\s*<a href="/blogy-o-zamcich-a-zamecnictvich/"[^>]*>[^<]*</a>', "", frag)
        frag = re.sub(r'\s*<li><a href="/blogy-o-zamcich-a-zamecnictvich/">[^<]*</a></li>', "", frag)

        # Kotvy a odkazy do jazykové větve
        frag = frag.replace('href="/#', f'href="{base}/#')
        frag = re.sub(r'href="/([a-z][a-z0-9-]+)/"', rf'href="{base}/\1/"', frag)
        frag = frag.replace('href="/"', f'href="{base}/"')

        # Texty navigace a služeb
        for cs, tr in nav_map + svc_map:
            frag = re.sub(rf'>{re.escape(cs)}<', f'>{tr}<', frag)

        # Ostatní řetězce rozhraní
        frag = (frag
                .replace("Nonstop 24/7", t["nonstop"])
                .replace("Zavolat teď", t["call_now"])
                .replace(f'Zavolat {TEL_HUMAN}', f'{t["call_now"]} {TEL_HUMAN}')
                .replace("Hlavní navigace", t["lang_label"])
                .replace("Mobilní navigace", t["lang_label"])
                .replace("Otevřít menu", t["lang_label"])
                .replace(">Informace<", f'>{t["footer_info"]}<')
                .replace(">Kontakt<", f'>{t["footer_contact"]}<')
                .replace("Ochrana osobních údajů", t["privacy"])
                .replace("Praha a okolí", t["area"])
                .replace("Nonstop 24 / 7", t["nonstop"])
                .replace("© <span data-year>2026</span> Rychlý Zámečník — Zámečnická pohotovost Praha",
                         f'© <span data-year>2026</span> Rychlý Zámečník — {t["footer_rights"]}')
                .replace("Ceny uvedené na webu jsou orientační, „od“.", t["footer_note"])
                .replace("Zámečnická pohotovost pro Prahu a okolí. Nonstop 24/7, 30 let\n          zkušeností, dvouletá záruka na práci i materiál.", t["footer_tagline"])
                )
        # Patička — hlavička sloupce Služby
        frag = frag.replace("<h4>Služby</h4>", f'<h4>{t["footer_services"]}</h4>')

        # Cookie lišta
        frag = (frag
                .replace("Soubory cookie", t["cookie_head"])
                .replace("Přijmout vše", t["cookie_all"])
                .replace("Jen nezbytné", t["cookie_min"])
                .replace("zásadách ochrany osobních údajů", t["cookie_link"]))
        frag = re.sub(
            r"Web používá jen nezbytné cookies pro svůj provoz\.\s*Statistiky sbíráme,\s*"
            r"až když nám k tomu dáte souhlas\. Víc v",
            t["cookie_text"], frag)

        if had_langs:
            frag = frag.replace("@@LANGS@@", langs_block(lang, wide))
        out[key] = frag
    return out


def price_rows(lang: str, key: str) -> str:
    return "\n".join(
        f'        <div class="price-row"><span class="price-row__name">{html.escape(n)}</span>'
        f'<span class="price-row__dots"></span>'
        f'<span class="price-row__val">{html.escape(v)}</span></div>'
        for n, v in CENIK_I18N[lang][key]
    )


def call_btn(lang: str, big=True) -> str:
    cls = "btn btn--lg btn--call" if big else "btn btn--call"
    return (f'<a class="{cls}" data-magnetic="0.25" href="tel:{TEL}">'
            f'{ICO.format(PHONE_PATH)} {TEL_HUMAN}</a>')


def doc(*, lang, slug, title, desc, img, head_extra, body, chrome) -> str:
    """HTML dokument s hreflang odkazy na všechny mutace."""
    canon = f"{SITE}/{lang}/{slug}/" if slug else f"{SITE}/{lang}/"
    alts = [f'<link rel="alternate" hreflang="cs" href="{SITE}/{slug + "/" if slug else ""}">']
    for code, meta in LANGS.items():
        alts.append(f'<link rel="alternate" hreflang="{meta["hreflang"]}" '
                    f'href="{SITE}/{code}/{slug + "/" if slug else ""}">')
    alts.append(f'<link rel="alternate" hreflang="x-default" '
                f'href="{SITE}/{slug + "/" if slug else ""}">')

    return f"""<!DOCTYPE html>
<html lang="{LANGS[lang]['hreflang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#060806">
<link rel="canonical" href="{canon}">
{chr(10).join(alts)}

<meta property="og:type" content="website">
<meta property="og:locale" content="{LANGS[lang]['locale']}">
<meta property="og:site_name" content="Rychlý Zámečník">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/{img}.webp">

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


# --------------------------------------------------------------------------- #
def render_home(lang: str, chrome: dict) -> str:
    h, t = HOME[lang], UI[lang]
    b = f"/{lang}"

    # Stejné ozdoby jako v české verzi: hvězdičky, tepající tečka, pak ikony
    chip_deco = [
        '<span class="stars">★★★★★</span> ',
        '<span class="dot"></span> ',
        f'<svg class="chip__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        f'{ICONS["bolt"]}</svg> ',
        f'<svg class="chip__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        f'{ICONS["shield"]}</svg> ',
        f'<svg class="chip__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        f'{ICONS["coin"]}</svg> ',
    ]
    chips = "\n".join(f'      <li class="chip">{chip_deco[i]}{c}</li>'
                      for i, c in enumerate(h["chips"]))
    ticker = "\n".join(f"      <span>{html.escape(x)}</span>" for x in h["ticker"])
    stats = "\n".join(
        f'      <div class="stat"><div class="stat__num"><span data-count="{n}">0</span>{suf}</div>'
        f'<div class="stat__label">{html.escape(lbl)}</div></div>'
        for (n, suf), lbl in zip([("30", "&nbsp;+"), ("887", "+"), ("4.9", "&nbsp;★"), ("24", "/7")],
                                 h["stats"]))

    svc = "\n".join(
        f"""      <article class="svc" data-reveal data-tilt="5">
        <div class="svc__media"><img src="/assets/img/{PAGES[slug]['img']}.webp" alt="{html.escape(name)}" loading="lazy"></div>
        <div class="svc__body">
          <h3><a class="svc__link" href="{b}/{slug}/">{html.escape(name)}</a></h3>
          <p>{html.escape(txt)}</p>
          <div class="svc__foot">
            <span class="svc__price"><b>{html.escape(price)}</b></span>
            <span class="svc__arrow" aria-hidden="true">{ARROW}</span>
          </div>
        </div>
      </article>"""
        for slug, (name, txt, price) in zip(PAGES, h["svc"]))

    why = "\n".join(
        f"""      <div class="why" data-reveal data-tilt="4">
        <div class="why__ico">{ICO.format(list(ICONS.values())[i])}</div>
        <h3>{html.escape(head)}</h3><p>{html.escape(txt)}</p>
      </div>""" for i, (head, txt) in enumerate(h["why"]))

    steps = "\n".join(
        f"""      <div class="step" data-reveal>
        <div class="step__n">{html.escape(n)}</div>
        <h3>{html.escape(head)}</h3><p>{html.escape(txt)}</p>
      </div>""" for n, head, txt in h["steps"])

    tabs = "\n".join(
        f'        <button class="tab" role="tab" id="tab-{i}" aria-controls="panel-{i}" '
        f'aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">'
        f'{html.escape(lbl)}</button>'
        for i, lbl in enumerate(h["tabs"]))

    panels = []
    for i, key in enumerate(["otevirani-bytu", "zamky", "auta"]):
        panels.append(f'      <div class="tab-panel" role="tabpanel" id="panel-{i}" '
                      f'aria-labelledby="tab-{i}"{"" if i == 0 else " hidden"}>\n'
                      f'{price_rows(lang, key)}\n      </div>')
    extra = "\n".join(
        f'        <div class="price-row"><span class="price-row__name">{html.escape(n)}</span>'
        f'<span class="price-row__dots"></span><span class="price-row__val">{html.escape(v)}</span></div>'
        for n, v in h["extra"])
    panels.append(f'      <div class="tab-panel" role="tabpanel" id="panel-3" '
                  f'aria-labelledby="tab-3" hidden>\n{extra}\n      </div>')

    districts = "\n".join(f"        <li>{d}</li>" for d in DISTRICTS)

    def rev_cards(items):
        return "\n".join(
            f"""          <article class="review">
            <div class="review__stars">{'★' * st}</div><p>{html.escape(txt)}</p>
            <div class="review__who"><span class="review__av">{ini}</span>
            <span><strong>{name}</strong><span>Google</span></span></div>
          </article>""" for ini, name, st, txt in items)

    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Locksmith",
        "name": "Rychlý Zámečník", "url": f"{SITE}/{lang}/", "telephone": TEL,
        "email": "info@rychly-zamecnik.cz", "priceRange": "290–2490 CZK",
        "areaServed": {"@type": "City", "name": "Praha"},
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59"},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9",
                            "reviewCount": "887", "bestRating": "5"},
    }, ensure_ascii=False, indent=2)

    body = f"""<main id="top">

<section class="hero">
  <div class="hero__media" data-parallax="0.18">
    <img src="/assets/img/hero-van-night.webp" alt="Rychlý Zámečník" fetchpriority="high">
  </div>
  <div class="shell hero__inner">
    <span class="badge-live" data-reveal><span class="dot"></span> {html.escape(h['badge'])}</span>
    <h1 data-split>{html.escape(h['h1_a'])}<br>{html.escape(h['h1_b'])} <em>{html.escape(h['h1_em'])}</em>.</h1>
    <p class="hero__sub" data-reveal>{html.escape(h['sub'])}</p>
    <div class="hero__actions" data-reveal>
      {call_btn(lang)}
      <a class="btn btn--lg btn--ghost" href="#cenik">{html.escape(t['show_prices'])}</a>
    </div>
    <ul class="hero__trust" data-reveal>
{chips}
    </ul>
  </div>
</section>

<div class="marquee" aria-hidden="true">
  <div class="marquee__track" data-marquee>
    <div class="marquee__group">
{ticker}
    </div>
  </div>
</div>

<section class="section section--tight">
  <div class="shell">
    <div class="stats" data-reveal="scale">
{stats}
    </div>
  </div>
</section>

<section class="section" id="sluzby">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>{html.escape(h['svc_eyebrow'])}</span>
        <h2 class="h-sec" data-split>{html.escape(h['svc_head'])}</h2>
      </div>
      <p class="lead" data-reveal>{html.escape(h['svc_lead'])}</p>
    </div>
    <div class="svc-grid">
{svc}
    </div>
  </div>
</section>

<section class="section" id="proc-my">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>{html.escape(t['why_eyebrow'])}</span>
        <h2 class="h-sec" data-split>{html.escape(h['why_head'])}</h2>
      </div>
      <p class="lead" data-reveal>{html.escape(h['why_lead'])}</p>
    </div>
    <div class="why-grid">
{why}
    </div>
  </div>
</section>

<section class="section" id="postup">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>{html.escape(h['how_eyebrow'])}</span>
        <h2 class="h-sec" data-split>{html.escape(h['how_head'])}</h2>
      </div>
      <p class="lead" data-reveal>{html.escape(h['how_lead'])}</p>
    </div>
    <div class="steps">
{steps}
    </div>
  </div>
</section>

<section class="section" id="cenik">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>{html.escape(t['prices_eyebrow'])}</span>
        <h2 class="h-sec" data-split>{html.escape(h['price_head'])}</h2>
      </div>
      <p class="lead" data-reveal>{html.escape(h['price_lead'])}</p>
    </div>
    <div class="pricing" data-reveal>
      <div class="tabs" role="tablist" aria-label="{html.escape(t['prices_eyebrow'])}">
{tabs}
      </div>
{chr(10).join(panels)}
      <p class="pricing__note">{ICO.format(INFO)}<span>{t['price_note']}</span></p>
    </div>
  </div>
</section>

<section class="section" id="pokryti">
  <div class="shell">
    <div class="coverage">
      <div>
        <span class="eyebrow" data-reveal>{html.escape(h['area_eyebrow'])}</span>
        <h2 class="h-sec" data-split>{html.escape(h['area_head'])}</h2>
        <p class="lead" data-reveal>{html.escape(h['area_lead'])}</p>
        <ul class="districts" data-reveal="left">
{districts}
          <li>{html.escape(h['area_more'])}</li>
        </ul>
        <div class="hero__actions" data-reveal>
          <a class="btn btn--call" data-magnetic="0.25" href="tel:{TEL}">{html.escape(h['area_btn'])}</a>
        </div>
      </div>
      <div class="coverage__map" data-reveal="right">
        <img src="/assets/img/mapa-prahy.webp" alt="Praha 1–22" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section" id="recenze">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>{html.escape(h['rev_eyebrow'])}</span>
        <h2 class="h-sec" data-split>{html.escape(h['rev_head'])}</h2>
      </div>
      <p class="lead" data-reveal>{html.escape(h['rev_lead'])}</p>
    </div>
    <div class="gsum" data-reveal>
      <div class="gsum__score">4,9</div>
      <div class="gsum__meta"><span class="stars">★★★★★</span><span>{h['rev_sum']}</span></div>
    </div>
  </div>
  <div class="rev-marquee">
    <div class="rev-track" data-marquee>
      <div class="rev-group">
{rev_cards(REVIEWS[:6])}
      </div>
    </div>
  </div>
  <div class="rev-marquee">
    <div class="rev-track rev-track--rev" data-marquee>
      <div class="rev-group">
{rev_cards(REVIEWS[6:])}
      </div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="shell">
    <div class="cta-band" data-reveal>
      <div class="cta-band__media" data-parallax="0.12">
        <img src="/assets/img/tym-zamecniku.webp" alt="Rychlý Zámečník" loading="lazy">
      </div>
      <span class="badge-live"><span class="dot"></span> {html.escape(t['dispatch_live'])}</span>
      <h2 data-split>{html.escape(h['cta_head'])}</h2>
      <p>{html.escape(h['cta_text'])}</p>
      <div class="hero__actions">
        {call_btn(lang)}
        <a class="btn btn--lg btn--ghost" href="mailto:info@rychly-zamecnik.cz">{html.escape(t['write_email'])}</a>
      </div>
    </div>
  </div>
</section>

</main>"""

    return doc(lang=lang, slug="", title=h["title"], desc=h["desc"], img="hero-van-night",
               head_extra=f'<script type="application/ld+json">\n{ld}\n</script>',
               body=body, chrome=chrome)


# --------------------------------------------------------------------------- #
def render_service(lang: str, slug: str, chrome: dict) -> str:
    p, t = SERVICES[lang][slug], UI[lang]
    b = f"/{lang}"

    ticks = "\n".join(f"          <li>{TICK}<span>{x}</span></li>" for x in p["ticks"])
    why = "\n".join(
        f"""        <div class="why" data-reveal data-tilt="4">
          <div class="why__ico">{ICO.format(ICONS[ic])}</div>
          <h3>{html.escape(hd)}</h3><p>{html.escape(tx)}</p>
        </div>""" for ic, hd, tx in p["why"])
    prose = "\n".join(f"        <p>{x}</p>" for x in p["prose"])
    faq = "\n".join(
        f'        <details><summary>{html.escape(q)}</summary>'
        f'<div class="faq__a"><p>{html.escape(a)}</p></div></details>'
        for q, a in p["faq"])
    more = "\n".join(
        f'        <a class="more" href="{b}/{s}/" data-reveal>'
        f'{html.escape(SERVICES[lang][s]["nav"])}{ARROW}</a>'
        for s in PAGES if s != slug)

    ld = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Service", "name": p["h1"], "description": p["desc"],
             "serviceType": p["nav"], "areaServed": {"@type": "City", "name": "Praha"},
             "provider": {"@type": "Locksmith", "name": "Rychlý Zámečník",
                          "telephone": TEL, "url": f"{SITE}/{lang}/"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": t["home"], "item": f"{SITE}/{lang}/"},
                {"@type": "ListItem", "position": 2, "name": p["nav"],
                 "item": f"{SITE}/{lang}/{slug}/"}]},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
        ]}, ensure_ascii=False, indent=2)

    body = f"""<main id="top">

<section class="page-hero">
  <div class="page-hero__media" data-parallax="0.14">
    <img src="/assets/img/{p['img']}.webp" alt="{html.escape(p['img_alt'])}" fetchpriority="high">
  </div>
  <div class="shell">
    <nav aria-label="{html.escape(t['home'])}">
      <ol class="crumbs">
        <li><a href="{b}/">{html.escape(t['home'])}</a></li>
        <li><a href="{b}/#sluzby">{html.escape(t['footer_services'])}</a></li>
        <li><span aria-current="page">{html.escape(p['nav'])}</span></li>
      </ol>
    </nav>
    <span class="badge-live"><span class="dot"></span> {html.escape(t['dispatch_live'])}</span>
    <h1 data-split>{html.escape(p['h1'])}</h1>
    <p class="page-hero__lead">{html.escape(p['lead'])}</p>
    <ul class="ticks">
{ticks}
    </ul>
    <div class="hero__actions">
      {call_btn(lang)}
      <a class="btn btn--lg btn--ghost" href="#cenik-sluzby">{html.escape(t['service_prices'])}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>{html.escape(t['why_eyebrow'])}</span>
        <h2 class="h-sec" data-split>{html.escape(p['why_head'])}</h2>
      </div>
      <p class="lead" data-reveal>{html.escape(p['why_lead'])}</p>
    </div>
    <div class="why-grid">
{why}
    </div>
  </div>
</section>

<section class="section" id="cenik-sluzby">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>{html.escape(t['prices_eyebrow'])}</span>
        <h2 class="h-sec" data-split>{html.escape(t['service_prices'])} — {html.escape(p['nav'].lower())}</h2>
      </div>
    </div>
    <div class="pricing" data-reveal>
      <div class="tab-panel">
{price_rows(lang, p['prices'])}
      </div>
      <p class="pricing__note">{ICO.format(INFO)}<span>{t['price_note']}
        <a href="{b}/#cenik" style="color:var(--accent)">{html.escape(t['full_pricelist'])}</a>.</span></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <span class="eyebrow" data-reveal>{html.escape(t['good_to_know'])}</span>
    <h2 class="h-sec" data-split>{html.escape(p['prose_head'])}</h2>
    <div class="prose" style="margin-top:26px" data-reveal>
{prose}
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>{html.escape(t['faq_eyebrow'])}</span>
        <h2 class="h-sec" data-split>{html.escape(t['faq_head'])}</h2>
      </div>
      <p class="lead" data-reveal>{html.escape(t['faq_lead'])}</p>
    </div>
    <div class="faq" data-reveal>
{faq}
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>{html.escape(t['more_services'])}</span>
        <h2 class="h-sec" data-split>{html.escape(t['more_head'])}</h2>
      </div>
    </div>
    <div class="more-grid">
{more}
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="shell">
    <div class="cta-band" data-reveal>
      <div class="cta-band__media" data-parallax="0.12">
        <img src="/assets/img/tym-zamecniku.webp" alt="Rychlý Zámečník" loading="lazy">
      </div>
      <span class="badge-live"><span class="dot"></span> {html.escape(t['nonstop'])}</span>
      <h2 data-split>{html.escape(t['cta_head'])}</h2>
      <p>{html.escape(t['cta_text'])}</p>
      <div class="hero__actions">
        {call_btn(lang)}
        <a class="btn btn--lg btn--ghost" href="mailto:info@rychly-zamecnik.cz">{html.escape(t['write_email'])}</a>
      </div>
    </div>
  </div>
</section>

</main>"""

    return doc(lang=lang, slug=slug, title=p["title"], desc=p["desc"], img=p["img"],
               head_extra=f'<script type="application/ld+json">\n{ld}\n</script>',
               body=body, chrome=chrome)


# --------------------------------------------------------------------------- #
def render_legal(lang: str, chrome: dict) -> str:
    p, t = LEGAL_I18N[lang], UI[lang]
    b = f"/{lang}"

    out = []
    for kind, val in p["body"]:
        if kind == "p":
            out.append(f"      <p>{val}</p>")
        elif kind == "h":
            out.append(f'      <h2 data-reveal>{html.escape(val)}</h2>')
        elif kind == "ul":
            lis = "\n".join(f"        <li>{v}</li>" for v in val)
            out.append(f'      <ul class="list" data-reveal>\n{lis}\n      </ul>')

    body = f"""<main id="top">

<section class="page-hero page-hero--plain">
  <div class="shell">
    <nav aria-label="{html.escape(t['home'])}">
      <ol class="crumbs">
        <li><a href="{b}/">{html.escape(t['home'])}</a></li>
        <li><span aria-current="page">{html.escape(p['title'])}</span></li>
      </ol>
    </nav>
    <h1 data-split>{html.escape(p['title'])}</h1>
    <p class="page-hero__lead">{html.escape(p['intro'])}</p>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="article">
{chr(10).join(out)}

      <p class="pricing__note" style="border:1px solid var(--line);border-radius:var(--radius);margin-top:34px">
        {ICO.format(INFO)}<span>{html.escape(p['note'])}</span>
      </p>
    </div>
  </div>
</section>

</main>"""

    return doc(lang=lang, slug=LEGAL_SLUG, title=p["meta_title"], desc=p["desc"],
               img="hero-van-night", head_extra="", body=body, chrome=chrome)


def main() -> None:
    base_chrome = load_chrome()
    total = 0
    for lang in LANGS:
        chrome = localize_chrome(base_chrome, lang)
        d = ROOT / lang
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(render_home(lang, chrome), encoding="utf-8")
        total += 1
        for slug in PAGES:
            sd = d / slug
            sd.mkdir(parents=True, exist_ok=True)
            (sd / "index.html").write_text(render_service(lang, slug, chrome), encoding="utf-8")
            total += 1
        ld = d / LEGAL_SLUG
        ld.mkdir(parents=True, exist_ok=True)
        (ld / "index.html").write_text(render_legal(lang, chrome), encoding="utf-8")
        total += 1
        print(f"  /{lang}/ — domovská + {len(PAGES)} podstránek + zásady")
    print(f"Hotovo — {total} stránek ve {len(LANGS)} jazycích.")


if __name__ == "__main__":
    main()
