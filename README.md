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
python3 build-sitemap.py     # sitemap.xml
python3 build-standalone.py  # dist/rychly-zamecnik.html — vše v jednom souboru
```

Podstránky jsou vygenerované a zároveň zakomitované, takže web funguje
i bez spuštění buildu. Po úpravě `index.html` nebo `content/pages.py`
spusťte `build-pages.py` znovu — hlavička a patička se berou přímo
z `index.html`, aby nevznikly dvě verze.

## Struktura

```
index.html                  domovská stránka
<sluzba>/index.html         6 podstránek na původních URL (generované)
content/pages.py            obsah podstránek — texty, ceny, FAQ
assets/css/style.css        styly (design tokens nahoře)
assets/js/main.js           interakce, bez závislostí
assets/img/                 fotky z původního webu ve WebP (428 KB)
build-pages.py              generátor podstránek
build-sitemap.py            generátor sitemap.xml
build-standalone.py         jednosouborová verze pro sdílení
NAVRH.md                    návrh — šablona, barvy, změny, další kroky
REDIRECTS.md                mapa 301 přesměrování pro zachování SEO
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

Všechny podstránky drží **původní URL**, aby se nepřišlo o pozice
ve vyhledávání — podrobnosti v [REDIRECTS.md](REDIRECTS.md).

## Vlastnosti

- Bez závislostí a bez externích požadavků (žádné fonty z CDN ani trackery)
- Responzivní od 360 px výš, na mobilu fixní lišta s voláním
- Ceník ve 4 záložkách ovladatelných klávesnicí (ARIA tabs)
- FAQ přes nativní `<details>` — funguje i bez JavaScriptu
- Strukturovaná data: `Locksmith` na úvodu, `Service` + `BreadcrumbList`
  + `FAQPage` na podstránkách
- Animace respektují `prefers-reduced-motion`
