# rychly-zamecnik.cz — návrh redesignu

Prototyp nového webu pro **Rychlý Zámečník — Zámečnická pohotovost Praha**
([rychly-zamecnik.cz](https://www.rychly-zamecnik.cz/)).

Struktura vychází ze šablony [Tradesman](https://www.framer.com/community/marketplace/templates/tradesman/)
(Framer Community, zdarma). Obsah, ceník, recenze i fotografie jsou převzaté
z původního webu.

**Kompletní návrh a zdůvodnění: [NAVRH.md](NAVRH.md)**

## Spuštění

Statické soubory, stačí je otevřít:

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

## Jednosouborová verze

Pro odeslání klientovi nebo náhled bez serveru — CSS, JS i obrázky
zabalené do jednoho HTML souboru:

```bash
python3 build-standalone.py
# → dist/rychly-zamecnik.html (~825 KB)
```

## Struktura

```
index.html              jednostránkový web
assets/css/style.css    styly (design tokens nahoře)
assets/js/main.js       interakce, bez závislostí
assets/img/             fotky z původního webu, převedené do WebP (428 KB)
build-standalone.py     sestavení jednosouborové verze
NAVRH.md                návrh — šablona, barvy, změny, další kroky
```

## Vlastnosti

- Bez závislostí a bez externích požadavků (žádné fonty z CDN ani trackery)
- Responzivní od 390 px výš, na mobilu fixní lišta s voláním
- Ceník ve 4 záložkách ovladatelných klávesnicí (ARIA tabs)
- JSON-LD `Locksmith` pro hvězdičky ve výsledcích vyhledávání
- Animace respektují `prefers-reduced-motion`
