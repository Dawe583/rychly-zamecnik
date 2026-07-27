# rychly-zamecnik.cz — návrh redesignu

Prototyp nového webu pro **Rychlý Zámečník — Zámečnická pohotovost Praha**
([rychly-zamecnik.cz](https://www.rychly-zamecnik.cz/)).

Struktura vychází ze šablony [Tradesman](https://www.framer.com/community/marketplace/templates/tradesman/)
(Framer Community, zdarma). Obsah, ceník, recenze i fotografie jsou převzaté
z původního webu.

**Kompletní návrh a zdůvodnění: [NAVRH.md](NAVRH.md)**

## Spuštění

Statické soubory. Kvůli odkazům typu `/otevirani-dveri/` je potřeba
server, ne otevření souboru z disku:

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

## Sestavení

```bash
python3 build-pages.py       # podstránky služeb z content/pages.py
python3 build-articles.py    # blog, články a zásady ochrany údajů
python3 build-i18n.py        # jazykové mutace /en/, /ru/, /ua/
python3 build-sitemap.py     # sitemap.xml
python3 build-standalone.py  # dist/rychly-zamecnik.html — vše v jednom souboru
```

Podstránky jsou vygenerované a zároveň zakomitované, takže web funguje
i bez spuštění buildu. Po úpravě `index.html` nebo `content/pages.py`
spusťte `build-pages.py` znovu — hlavička a patička se berou přímo
z `index.html`, aby nevznikly dvě verze.

## Struktura

```
index.html                    domovská stránka
<sluzba>/index.html           6 podstránek služeb (generované)
blogy-.../index.html          blog + 5 článků (generované)
zasady-.../index.html         zásady ochrany osobních údajů
obchodni-podminky/index.html  obchodní podmínky
404.html                      stránka nenalezena (noindex)
en|ru|ua/                     jazykové mutace (generované)
content/pages.py              obsah podstránek — texty, ceny, FAQ
content/articles.py           články a právní stránky
content/i18n.py               překlady rozhraní i obsahu
assets/css/style.css          styly (design tokens nahoře)
assets/js/main.js             interakce a animace
assets/js/vendor/lenis.min.js Lenis — plynulý scroll (MIT)
assets/fonts/                 Oswald + Golos Text (OFL, subsetované)
assets/video/hero-loop.webm   video smyčka do hera (generovaná)
assets/img/                   fotky z původního webu ve WebP (428 KB)
buildlib.py                   sdílené díly generátorů
build-pages.py                generátor podstránek služeb
build-articles.py             generátor blogu a právních stránek
build-i18n.py                 generátor jazykových mutací
build-video.py                sestaví hero video z fotek
build-framer-export.py        vysype obsah pro přenos do Frameru
build-sitemap.py              generátor sitemap.xml
build-standalone.py           jednosouborová verze pro sdílení
framer-export/                obsah k vložení do Frameru (generované)
NAVRH.md                      návrh — šablona, barvy, změny, další kroky
REDIRECTS.md                  mapa 301 přesměrování pro zachování SEO
FRAMER.md                     srovnání Framer šablon s cenami + podklady
```

## Stránky

| URL | Obsah |
|---|---|
| `/` | Hero, služby, proč my, postup, ceník, mapa, recenze |
| `/otevirani-dveri/` | Nouzové otevírání dveří |
| `/vymena-zamku/` | Výměna zámků a vložek |
| `/otevirani-aut/` | Otevírání aut |
| `/otevirani-trezoru/` | Otevírání a servis trezorů |
| `/oprava-dveri/` | Oprava dveří po vloupání |
| `/zamecnicka-pohotovost/` | Pohotovost nonstop |
| `/blogy-o-zamcich-a-zamecnictvich/` | Blog + 5 článků na původních URL |
| `/zasady-ochrany-osobnich-udaju/` | Zásady ochrany osobních údajů |
| `/obchodni-podminky/` | Obchodní podmínky |
| `/en/`, `/ru/`, `/ua/` | Jazykové mutace — úvod, 6 služeb, zásady |

Celkem **38 stránek**. Všechny drží **původní URL**, aby se nepřišlo
o pozice ve vyhledávání — podrobnosti v [REDIRECTS.md](REDIRECTS.md).

## Vlastnosti

- Plynulý scroll přes [Lenis](https://github.com/darkroomengineering/lenis) (MIT,
  vendorovaný — žádné CDN)
- Žádné externí požadavky: písma lokální, nulové trackery
- Typografie: **Oswald** (nadpisy) + **Golos Text** (text), obě proměnná
  a subsetovaná na latinku i cyrilici — dohromady 92 kB
- Hero video sestavené z vlastních fotek klienta (11,6 s bezešvá smyčka)
- Responzivní od 360 px výš, na mobilu fixní lišta s voláním
- Ceník ve 4 záložkách ovladatelných klávesnicí (ARIA tabs)
- FAQ přes nativní `<details>` — funguje i bez JavaScriptu
- Strukturovaná data: `Locksmith` na úvodu, `Service` + `BreadcrumbList`
  + `FAQPage` na podstránkách
- Animace: nadpisy po slovech, parallax, 3D naklopení karet, magnetická
  tlačítka, světelná stopa kurzoru, běžící pásy reagující na rychlost scrollu
- **Všechny efekty běží na každém zařízení** — myš, dotyk i pero. Stojí
  na Pointer Events, takže naklopení i lesk reagují na prst stejně jako
  na kurzor; plynulý scroll jede i na dotyku (`syncTouch`)
- Vše respektuje `prefers-reduced-motion` — Lenis se pak vůbec nespustí
- Cookie lišta s volbou „jen nezbytné“, volba se pamatuje
