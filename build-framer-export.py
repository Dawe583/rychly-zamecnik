#!/usr/bin/env python3
"""
Vysype všechen obsah do podoby, která se dá rovnou vkládat do Frameru.

Framer se plní ručně, takže cílem není strojový import, ale co nejmenší tření
při copy-paste: jeden soubor na stránku, ceník v CSV pro tabulkové komponenty,
překlady vedle sebe pro snadné přepínání jazyků.

Spuštění:  python3 build-framer-export.py
"""

import csv
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "framer-export"
sys.path.insert(0, str(ROOT))

from content.articles import ARTICLES, LEGAL  # noqa: E402
from content.i18n import (ARTICLES_I18N, BLOG_I18N, CENIK_I18N, HOME,  # noqa: E402
                          LANGS, LEGAL_I18N, SERVICES, UI)
from content.pages import CENIK, PAGES  # noqa: E402

KATEGORIE = {
    "otevirani-bytu": "Otevírání bytů a domů",
    "zamky": "Opravy a montáže zámků",
    "auta": "Otevírání aut",
    "ostatni": "Cestovné, slevy a příplatky",
}


def strip_tags(s: str) -> str:
    """Framer nechce HTML — tučné se v editoru nastaví ručně.

    Entity je potřeba rozkódovat, ne jen odstranit značky: do textu se
    jinak dostane „&bdquo;“ místo uvozovky a v editoru by se to muselo
    přepisovat ručně na každé stránce.
    """
    return html.unescape(re.sub(r"<[^>]+>", "", s))


# --------------------------------------------------------------------------- #
def export_cenik():
    """Ceník do CSV — nejrychlejší cesta do tabulkové komponenty."""
    path = OUT / "cenik.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["Kategorie", "Položka", "Cena"])
        for key, rows in CENIK.items():
            for name, price in rows:
                w.writerow([KATEGORIE.get(key, key), name, price])
    rows = sum(len(v) for v in CENIK.values())

    # Totéž pro jazykové mutace. Cestovné a slevy jsou v překladech uložené
    # zvlášť (HOME[lang]["extra"]), tak je sem doplníme, ať je ceník úplný.
    for lang in LANGS:
        p = OUT / f"cenik-{lang}.csv"
        with p.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["Category", "Item", "Price"])
            # Názvy kategorií vzít z přeložených záložek ceníku, ne z českých
            tabs = HOME[lang]["tabs"]
            poradi = {"otevirani-bytu": 0, "zamky": 1, "auta": 2}
            for key, items in CENIK_I18N[lang].items():
                for name, price in items:
                    w.writerow([tabs[poradi[key]], name, price])
            for name, price in HOME[lang]["extra"]:
                w.writerow([tabs[3], name, price])
    return rows


def export_sluzby():
    """Jedna stránka služby = jeden soubor, v pořadí, v jakém se skládá."""
    for slug, p in PAGES.items():
        lines = [
            f"# {p['h1']}", "",
            "## SEO", "",
            f"- **Title:** {p['title']}",
            f"- **Description:** {p['desc']}",
            f"- **URL:** /{slug}/",
            f"- **Fotka:** assets/img/{p['img']}.webp", "",
            "## Hero", "",
            p["lead"], "",
            "**Odrážky:**", "",
        ]
        lines += [f"- {strip_tags(t)}" for t in p["ticks"]]
        lines += ["", f"## {p['why_head']}", "", p["why_lead"], ""]
        for _, head, body in p["why"]:
            lines += [f"### {head}", "", body, ""]
        lines += [f"## Ceník — {KATEGORIE.get(p['prices'], p['prices'])}", "",
                  "Viz `cenik.csv`, kategorie výše.", "",
                  f"## {p['prose_head']}", ""]
        lines += [strip_tags(x) + "\n" for x in p["prose"]]
        lines += ["## Časté dotazy", ""]
        for q, a in p["faq"]:
            lines += [f"**{q}**", "", a, ""]
        (OUT / f"sluzba-{slug}.md").write_text("\n".join(lines), encoding="utf-8")
    return len(PAGES)


def export_domovska():
    lines = ["# Domovská stránka", "", "## Hero", "",
             "**Titulek:** Zabouchlé dveře? Jsme u vás do 30 minut.", "",
             "**Podtitulek:** Zámečnická pohotovost pro Prahu a okolí. Otevřeme vám "
             "dveře, auto i trezor — rychle, bez jediného škrábance a za nejnižší "
             "ceny v Praze.", "",
             "**Tlačítka:** 723 965 990 (tel:+420723965990) · Zobrazit ceník", "",
             "**Odznaky:** 4,8 z 887 recenzí · Nonstop 24/7 · Příjezd do 30 minut · "
             "2 roky záruka · Sleva 50 % pro stálé zákazníky", "",
             "**Video:** assets/video/hero-loop.webm (plakát: hero-van-night.webp)", "",
             "## Statistiky", "",
             "- 30 let zkušeností v oboru",
             "- 887+ hodnocení od zákazníků",
             "- 4,8 ★ průměrné hodnocení Google",
             "- 24/7 pohotovost bez přestávky", "",
             "## Služby", ""]
    for slug, p in PAGES.items():
        lines += [f"- **{p['nav']}** → /{slug}/ — {p['desc'][:90]}…"]
    lines += ["", "## Kontakt", "",
              "- Telefon: 723 965 990 (+420723965990)",
              "- E-mail: info@rychly-zamecnik.cz",
              "- IČO: 075 25 711",
              "- Působnost: Praha 1–22 a okolí", "",
              "## Podklady", "",
              "- Ceník: `cenik.csv`",
              "- Podstránky služeb: `sluzba-*.md`",
              "- Články: `clanek-*.md`",
              "- Překlady: `preklady-*.md`"]
    (OUT / "domovska.md").write_text("\n".join(lines), encoding="utf-8")


def md_blocks(body) -> list:
    """Obsahové bloky do Markdownu — stejný formát pro články i právní texty."""
    lines = []
    for kind, val in body:
        if kind == "h":
            lines += [f"## {strip_tags(val)}", ""]
        elif kind == "p":
            lines += [strip_tags(val), ""]
        elif kind == "q":
            lines += [f"> {strip_tags(val)}", ""]
        elif kind in ("ul", "ok", "no"):
            mark = {"ul": "-", "ok": "- ✓", "no": "- ✗"}[kind]
            lines += [f"{mark} {strip_tags(v)}" for v in val] + [""]
    return lines


def clanek_md(a: dict, url: str, date_h: str, img: str) -> str:
    lines = [f"# {a['title']}", "",
             f"- **Title:** {a['meta_title']}",
             f"- **Description:** {a['desc']}",
             f"- **URL:** {url}",
             f"- **Datum:** {date_h}",
             f"- **Rubrika:** {a['tag']}",
             f"- **Fotka:** assets/img/{img}.webp", "",
             f"**Perex:** {a['perex']}", ""]
    return "\n".join(lines + md_blocks(a["body"]))


def pravni_md(p: dict, url: str) -> str:
    lines = [f"# {p['title']}", "", f"- **URL:** {url}", "", p["intro"], ""]
    lines += md_blocks(p["body"])
    lines += ["---", "", p["note"]]
    return "\n".join(lines)


def export_clanky():
    for slug, a in ARTICLES.items():
        (OUT / f"clanek-{slug}.md").write_text(
            clanek_md(a, f"/{slug}/", a["date_h"], a["img"]), encoding="utf-8")

    for slug, p in LEGAL.items():
        (OUT / f"pravni-{slug}.md").write_text(
            pravni_md(p, f"/{slug}/"), encoding="utf-8")
    return len(ARTICLES) + len(LEGAL)


def export_clanky_i18n():
    """Články a právní texty v mutacích — jeden soubor na stránku, jako u češtiny."""
    n = 0
    for lang in LANGS:
        for slug, a in ARTICLES_I18N[lang].items():
            cs = ARTICLES[slug]      # datum a fotka jsou společné s českou verzí
            (OUT / f"clanek-{lang}-{slug}.md").write_text(
                clanek_md(a, f"/{lang}/{slug}/", a["date_h"], cs["img"]), encoding="utf-8")
            n += 1
        for slug, langs in LEGAL_I18N.items():
            (OUT / f"pravni-{lang}-{slug}.md").write_text(
                pravni_md(langs[lang], f"/{lang}/{slug}/"), encoding="utf-8")
            n += 1
    return n


def export_preklady():
    """Překlady po jazycích — rozhraní i obsah pohromadě."""
    for lang, meta in LANGS.items():
        t, h = UI[lang], HOME[lang]
        lines = [f"# Překlady — {meta['name']} (/{lang}/)", "", "## Rozhraní", ""]
        lines += [f"- **{k}:** {v}" for k, v in t.items()]
        lines += ["", "## Domovská stránka", "",
                  f"- **Title:** {h['title']}",
                  f"- **Description:** {h['desc']}",
                  f"- **Titulek:** {h['h1_a']} {h['h1_b']} {h['h1_em']}",
                  f"- **Podtitulek:** {h['sub']}", "",
                  "**Odznaky:**", ""]
        lines += [f"- {strip_tags(c)}" for c in h["chips"]]
        lines += ["", "**Služby na úvodu:**", ""]
        for name, txt, price in h["svc"]:
            lines += [f"- **{name}** ({price}) — {txt}"]
        lines += ["", "**Proč my:**", ""]
        for head, txt in h["why"]:
            lines += [f"- **{head}** — {txt}"]
        lines += ["", "**Jak to probíhá:**", ""]
        for n, head, txt in h["steps"]:
            lines += [f"- **{n} {head}** — {txt}"]
        lines += ["", "## Podstránky služeb", ""]
        for slug, p in SERVICES[lang].items():
            lines += [f"### /{lang}/{slug}/", "",
                      f"- **Title:** {p['title']}",
                      f"- **H1:** {p['h1']}",
                      f"- **Perex:** {p['lead']}", "",
                      "**Časté dotazy:**", ""]
            for q, a in p["faq"]:
                lines += [f"- **{q}** — {a}"]
            lines += [""]
        (OUT / f"preklady-{lang}.md").write_text("\n".join(lines), encoding="utf-8")
    return len(LANGS)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    polozek = export_cenik()
    sluzeb = export_sluzby()
    export_domovska()
    clanku = export_clanky()
    prekladu = export_clanky_i18n()
    jazyku = export_preklady()

    (OUT / "README.md").write_text(
        "# Obsah pro Framer\n\n"
        "Vygenerováno `build-framer-export.py` z `content/`. Needituj ručně —\n"
        "zdroj je v `content/`, tohle je jen výstup pro copy-paste do Frameru.\n\n"
        "| Soubor | Co v něm je |\n|---|---|\n"
        "| `domovska.md` | Domovská stránka — hero, statistiky, kontakty |\n"
        "| `sluzba-*.md` | 6 podstránek služeb včetně FAQ |\n"
        "| `clanek-*.md` | 5 článků na blog |\n"
        "| `clanek-{en,ru,ua}-*.md` | Tytéž články v mutacích |\n"
        "| `pravni-*.md` | Zásady ochrany osobních údajů, obchodní podmínky |\n"
        "| `pravni-{en,ru,ua}-*.md` | Právní texty v mutacích |\n"
        "| `cenik.csv` | 43 ceníkových položek (oddělovač `;`, UTF-8 BOM) |\n"
        "| `cenik-{en,ru,ua}.csv` | Ceník v jazykových mutacích |\n"
        "| `preklady-*.md` | Kompletní překlady do EN, RU a UA |\n\n"
        "Obrázky a video zůstávají v `assets/` — do Frameru se nahrávají přímo.\n\n"
        "Výběr šablony a srovnání cen je ve [FRAMER.md](../FRAMER.md).\n",
        encoding="utf-8")

    print(f"  cenik.csv                  {polozek} položek")
    print(f"  sluzba-*.md                {sluzeb} služeb")
    print(f"  clanek-*.md, pravni-*.md   {clanku} textů česky")
    print(f"  tytéž v mutacích           {prekladu} textů")
    print(f"  preklady-*.md              {jazyku} jazyky")
    print(f"Hotovo — {len(list(OUT.iterdir()))} souborů v framer-export/")


if __name__ == "__main__":
    main()
