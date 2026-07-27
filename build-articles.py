#!/usr/bin/env python3
"""
Vygeneruje blog (rozcestník + články) a právní stránky.

Blog zůstává na původní adrese /blogy-o-zamcich-a-zamecnictvich/, články
na svých původních URL — kvůli zachování pozic ve vyhledávání.

Spuštění:  python3 build-articles.py
"""

import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))

from buildlib import ROOT as _R, SITE, crumbs, cta_section, document, load_chrome  # noqa: E402
from content.articles import ARTICLES, LEGAL  # noqa: E402

BLOG_SLUG = "blogy-o-zamcich-a-zamecnictvich"


# --------------------------------------------------------------------------- #
def blocks(items) -> str:
    """Vysází obsahové bloky článku."""
    out = []
    for kind, val in items:
        if kind == "p":
            out.append(f"      <p>{val}</p>")
        elif kind == "h":
            out.append(f'      <h2 data-reveal>{html.escape(val)}</h2>')
        elif kind == "q":
            out.append(f'      <blockquote data-reveal>{html.escape(val)}</blockquote>')
        elif kind in ("ul", "ok", "no"):
            cls = {"ul": "list", "ok": "list list--ok", "no": "list list--no"}[kind]
            lis = "\n".join(f"        <li>{v}</li>" for v in val)
            out.append(f'      <ul class="{cls}" data-reveal>\n{lis}\n      </ul>')
    return "\n".join(out)


def article_ld(slug: str, a: dict) -> str:
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BlogPosting",
                "headline": a["title"],
                "description": a["desc"],
                "datePublished": a["date"],
                "image": f"{SITE}/assets/img/{a['img']}.webp",
                "mainEntityOfPage": f"{SITE}/{slug}/",
                "author": {"@type": "Organization", "name": "Rychlý Zámečník"},
                "publisher": {
                    "@type": "Organization",
                    "name": "Rychlý Zámečník",
                    "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/img/logo.webp"},
                },
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Úvod", "item": f"{SITE}/"},
                    {"@type": "ListItem", "position": 2, "name": "Blog",
                     "item": f"{SITE}/{BLOG_SLUG}/"},
                    {"@type": "ListItem", "position": 3, "name": a["title"],
                     "item": f"{SITE}/{slug}/"},
                ],
            },
        ],
    }
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>")


# --------------------------------------------------------------------------- #
def render_article(slug: str, a: dict, chrome: dict) -> str:
    body = f"""<main id="top">

<article>
<section class="page-hero page-hero--article">
  <div class="page-hero__media" data-parallax="0.14">
    <img src="/assets/img/{a['img']}.webp" alt="{html.escape(a['img_alt'])}" fetchpriority="high">
  </div>

  <div class="shell">
{crumbs(("Úvod", "/"), ("Blog", f"/{BLOG_SLUG}/"), (html.escape(a['title']), None))}

    <p class="article__meta">
      <span class="tag">{html.escape(a['tag'])}</span>
      <time datetime="{a['date']}">{a['date_h']}</time>
    </p>

    <h1 data-split>{html.escape(a['title'])}</h1>
    <p class="page-hero__lead">{html.escape(a['perex'])}</p>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="article">
{blocks(a['body'])}
    </div>
  </div>
</section>
</article>

{cta_section("Potřebujete zámečníka teď hned?",
             "Konzultace po telefonu je zdarma. Cenu řekneme dopředu a technik "
             "vyjíždí okamžitě — nonstop, i o svátcích.")}

<section class="section section--tight">
  <div class="shell">
    <div class="sec-head">
      <div>
        <span class="eyebrow" data-reveal>Další články</span>
        <h2 class="h-sec" data-split>Mohlo by vás zajímat</h2>
      </div>
    </div>
    <div class="more-grid">
{other_links(slug)}
    </div>
  </div>
</section>

</main>"""

    return document(
        title=html.escape(a["meta_title"]),
        desc=html.escape(a["desc"]),
        canonical=f"{SITE}/{slug}/",
        og_image=f"{SITE}/assets/img/{a['img']}.webp",
        og_type="article",
        head_extra=article_ld(slug, a),
        body=body,
        chrome=chrome,
    )


def other_links(current: str) -> str:
    from buildlib import ARROW
    out = []
    for slug, a in ARTICLES.items():
        if slug == current:
            continue
        out.append(f'        <a class="more" href="/{slug}/" data-reveal>'
                   f'{html.escape(a["title"])}{ARROW}</a>')
    return "\n".join(out[:4])


# --------------------------------------------------------------------------- #
def render_blog_index(chrome: dict) -> str:
    cards = []
    for slug, a in sorted(ARTICLES.items(), key=lambda kv: kv[1]["date"], reverse=True):
        cards.append(f"""      <article class="post" data-reveal data-tilt="4">
        <div class="post__media" data-reveal="clip">
          <img src="/assets/img/{a['img']}.webp" alt="{html.escape(a['img_alt'])}" loading="lazy">
        </div>
        <div class="post__body">
          <p class="article__meta">
            <span class="tag">{html.escape(a['tag'])}</span>
            <time datetime="{a['date']}">{a['date_h']}</time>
          </p>
          <h2><a class="post__link" href="/{slug}/">{html.escape(a['title'])}</a></h2>
          <p>{html.escape(a['perex'])}</p>
        </div>
      </article>""")

    body = f"""<main id="top">

<section class="page-hero">
  <div class="page-hero__media" data-parallax="0.14">
    <img src="/assets/img/vyjezd-den.webp" alt="Vůz zámečnické pohotovosti" fetchpriority="high">
  </div>
  <div class="shell">
{crumbs(("Úvod", "/"), ("Blog", None))}
    <h1 data-split>Blog o zámcích a zámečnictví</h1>
    <p class="page-hero__lead">
      Rady, na co si dát pozor, a příběhy z výjezdů. Píšeme o tom, co
      opravdu potkáváme u zákazníků.
    </p>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="post-grid">
{chr(10).join(cards)}
    </div>
  </div>
</section>

{cta_section("Řešíte zámek právě teď?",
             "Nečtěte a volejte. Konzultace je zdarma a technik vyjíždí okamžitě.")}

</main>"""

    return document(
        title="Blog o zámcích a zámečnictví | Rychlý Zámečník",
        desc="Rady o zámcích, bezpečnosti a příběhy z výjezdů zámečnické pohotovosti "
             "v Praze. Jak nenaletět nepoctivým zámečníkům a co dělat, když se zabouchnou dveře.",
        canonical=f"{SITE}/{BLOG_SLUG}/",
        body=body,
        chrome=chrome,
    )


# --------------------------------------------------------------------------- #
def render_legal(slug: str, p: dict, chrome: dict) -> str:
    body = f"""<main id="top">

<section class="page-hero page-hero--plain">
  <div class="shell">
{crumbs(("Úvod", "/"), (html.escape(p['title']), None))}
    <h1 data-split>{html.escape(p['title'])}</h1>
    <p class="page-hero__lead">{html.escape(p['intro'])}</p>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="article">
{blocks(p['body'])}

      <p class="pricing__note" style="border:1px solid var(--line);border-radius:var(--radius);margin-top:34px">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
        <span>{html.escape(p['note'])}</span>
      </p>
    </div>
  </div>
</section>

</main>"""

    return document(
        title=html.escape(p["meta_title"]),
        desc=html.escape(p["desc"]),
        canonical=f"{SITE}/{slug}/",
        body=body,
        chrome=chrome,
    )


# --------------------------------------------------------------------------- #
def main() -> None:
    chrome = load_chrome()

    d = ROOT / BLOG_SLUG
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(render_blog_index(chrome), encoding="utf-8")
    print(f"  {BLOG_SLUG}/index.html")

    for slug, a in ARTICLES.items():
        d = ROOT / slug
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(render_article(slug, a, chrome), encoding="utf-8")
        print(f"  {slug}/index.html")

    for slug, p in LEGAL.items():
        d = ROOT / slug
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(render_legal(slug, p, chrome), encoding="utf-8")
        print(f"  {slug}/index.html")

    print(f"Hotovo — blog, {len(ARTICLES)} článků, {len(LEGAL)} právní stránka.")


if __name__ == "__main__":
    main()
