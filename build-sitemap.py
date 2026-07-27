#!/usr/bin/env python3
"""Vygeneruje sitemap.xml ze seznamu stránek v content/pages.py."""

import datetime
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))
from content.pages import PAGES  # noqa: E402

SITE = "https://www.rychly-zamecnik.cz"


def build() -> pathlib.Path:
    today = datetime.date.today().isoformat()
    urls = [(f"{SITE}/", "1.0")] + [(f"{SITE}/{slug}/", "0.8") for slug in PAGES]

    body = "\n".join(
        f"  <url>\n"
        f"    <loc>{loc}</loc>\n"
        f"    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n"
        f"    <priority>{prio}</priority>\n"
        f"  </url>"
        for loc, prio in urls
    )

    out = ROOT / "sitemap.xml"
    out.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n"
        "</urlset>\n",
        encoding="utf-8",
    )
    return out


if __name__ == "__main__":
    out = build()
    print(f"{out.name} — {len(PAGES) + 1} URL")
