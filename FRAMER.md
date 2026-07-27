# Přechod do Frameru — výběr šablony a podklady

Tenhle dokument je pro případ, že web nemá zůstat statický v tomhle repozitáři,
ale má žít ve Frameru, kde si ho klient edituje sám.

**Framer šablona se do repozitáře naimportovat nedá.** Je to projekt uvnitř
Frameru — kupuje se licence a remixuje se v jeho editoru. Export do HTML/CSS
neexistuje. Volba je tedy „buď — anebo", ne „obojí".

---

## 1. Srovnání šablon

Ceny ověřené 27. 7. 2026 přímo z Framer Marketplace (jednorázová licence
na jeden web).

| Šablona | Cena | Určení | Hodí se? |
|---|---|---|---|
| **[HomeMaster](https://www.framer.com/marketplace/templates/homemaster/)** | **49 USD** | Lokální služby — instalatéři, elektrikáři, **zámečníci**, HVAC | ★★★★★ Nejbližší oboru. Má vše, co web potřebuje: ceníkové tabulky, sekce služeb, recenze, oblasti pokrytí. |
| **[Plubar](https://www.framer.com/marketplace/templates/plubar/)** | 49 USD | Instalatéři a domácí služby | ★★★★ Struktura sedí, ale ikonografie je silně instalatérská — víc práce s předěláním. |
| **[Elek](https://www.framer.com/marketplace/templates/elek/)** | 29 USD | Elektrikáři, řemesla | ★★★ Nejlevnější, ale jednodušší. Na 43 ceníkových položek je krátká. |
| **[Mugen](https://www.framer.com/marketplace/templates/mugen/)** | 129 USD | Tmavé prémiové portfolio / agentura | ★★ Vypadá nejdráž, ale je to portfolio. Ceník ani nouzové CTA neřeší. |
| **[Offset](https://www.framer.com/marketplace/templates/offset/)** | 149 USD | Kinematické portfolio | ★★ Nejkrásnější typografie z celého výběru, ale pro zámečnickou pohotovost je to špatný nástroj. |
| **[Tradesman](https://www.framer.com/community/marketplace/templates/tradesman/)** | **zdarma** | Řemesla, nouzové výjezdy | ★★★★ Podle téhle je postavená struktura současného webu. Zdarma, ale vizuálně nejjednodušší. |

### Doporučení

**HomeMaster za 49 USD.** Je to jediná šablona ze seznamu, která přímo počítá
se zámečníky, a hlavně má připravené **ceníkové tabulky** — což je u tohohle
webu ta nejpracnější část (43 položek ve čtyřech kategoriích). U Mugenu nebo
Offsetu by se ceník musel stavět od nuly.

Mugen a Offset jsou hezčí, ale jsou to portfolia pro kreativce. Zámečnická
pohotovost potřebuje telefon nad ohybem a ceník, ne case studies.

### Na co si dát pozor

- **Licence je na jeden web.** Pokud by měly jazykové mutace běžet jako
  samostatné projekty, je potřeba licencí víc — ověřit před nákupem.
- **Framer si účtuje hosting** zvlášť (od ~5 USD/měsíc za vlastní doménu).
  Statická verze v tomhle repozitáři se dá hostovat zdarma.
- **Vícejazyčnost** má Framer nativně, ale v placeném tarifu. Původní web
  na to používal TranslatePress.
- **Rychlost.** Současná statická verze má 0 externích požadavků a všechna
  písma lokálně. Framer tahá vlastní runtime — bude pomalejší.

---

## 2. Co se ze šablony dá vytáhnout

Šablona je koupená, ale **čistý kód z Frameru nevypadne**. Ověřeno na
`homemaster.framer.website`: 265 generovaných tříd typu `framer-1oe98bp`,
540 inline stylů, žádný externí stylesheet (CSS je celé v `<style>`),
11 skriptů a markup zduplikovaný pro každý breakpoint přes
`class="ssr-variant hidden-17ig7g5"`.

Stáhnout ten DOM a nalepit ho do repozitáře by znamenalo vyměnit dnešní
čitelný kód za nečitelný. Užitečné na koupené šabloně proto není HTML,
ale **rozhodnutí, která jsou v ní udělaná**.

### Design systém HomeMasteru

Vytažené z inlinovaného CSS — `python3 analyze-framer.py <url>` to zopakuje
nad libovolnou Framer šablonou. Pozor: čísla jsou z prezentační stránky
šablony, ne z jejích šesti ukázkových homepage — ty jsou dostupné až po
přihlášení do Frameru.

| | HomeMaster | Web teď |
|---|---|---|
| Podklad | `#fff` — světlá | `#0A0C0A` — tmavá |
| Text | `#0d0d0d` | `#F2F5F2` |
| Hlavní barva | `#113d3c` tmavě zelená | `#04A202` z loga |
| Akcenty | `#00509d`, `#3ab449`, `#f3752b`, `#fdc500`, `#ff3722` | jen zelená |
| Písmo | Inter (400–900) + Satoshi | Oswald + Golos Text |
| Rádiusy | 8 / 16 / 24 px | 10 / 14 px |
| Stupně písma | 12–60 px | 13–120 px |
| Odsazení sekcí | 60–150 px | 72–140 px |

### Doporučení: vzít strukturu, ne vzhled

FRAMER.md doporučil HomeMaster kvůli **ceníkovým tabulkám a sekcím pro
lokální služby**, ne kvůli tomu, jak vypadá. To rozdělení má smysl držet:

- **Vzít:** anatomii ceníku, mřížku služeb, sekci oblastí pokrytí,
  rozvržení recenzí, strukturu 21 stránek (6 homepage + 15 vnitřních),
  Figma soubor jako podklad pro rozkreslení.
- **Nechat:** tmavý podklad, zelenou z loga a dodávek, Oswald s Golosem,
  sevřené rádiusy.

Důvod je v [NAVRH.md](NAVRH.md): tmavý směr není libovůle, ale odvozený
z toho, co firma **už má** — zelené polepené dodávky a noční výjezdy.
HomeMaster je světlá multioborová šablona pro instalatéry i úklid; Inter
je navíc přesně to výchozí písmo, kterému se návrh záměrně vyhýbal.

Překlopit web do vzhledu šablony jde, ale je to obrat o 180 stupňů —
ne dodělání. Proto to čeká na rozhodnutí, ne na commit.

---

## 3. Co je připravené k nasazení

Všechen obsah je hotový a strukturovaný. Do Frameru se přenáší ručně
(copy-paste), ale nic není potřeba psát znovu.

### Texty a struktura

| Kde | Co obsahuje |
|---|---|
| `content/pages.py` | 6 služeb — nadpisy, perexy, odrážky, 3 důvody „proč my", texty a **5 otázek a odpovědí ke každé službě** (30 celkem) |
| `content/pages.py` → `CENIK` | **43 ceníkových položek** ve 4 kategoriích |
| `content/articles.py` | 5 článků na blog + zásady ochrany osobních údajů a obchodní podmínky |
| `content/i18n.py` | Kompletní překlady do **EN, RU a UA** — rozhraní, obsah služeb, FAQ, popisky ceníku, obě právní stránky i celý blog |
| `index.html` | Domovská stránka — hero, statistiky, 6 služeb, 6 důvodů, 3 kroky, ceník, mapa pokrytí, 14 recenzí |

Pro pohodlný přenos je vedle toho v `framer-export/` totéž vysypané do
Markdownu a CSV — **43 souborů, jeden na stránku** včetně všech mutací.
Viz `python3 build-framer-export.py`.

### Obrazové podklady

| Soubor | Použití |
|---|---|
| `assets/img/*.webp` | 10 fotek z původního webu, převedených do WebP (428 kB celkem) |
| `assets/video/hero-loop.webm` | 11,6s smyčka do hera, sestavená z jejich fotek |
| `assets/img/mapa-prahy.webp` | Mapa pražských částí |
| `assets/img/logo.webp` | Logo |

### Co se do Frameru nepřenese samo

- **Strukturovaná data** (`Locksmith`, `Service`, `FAQPage`, `BreadcrumbList`) —
  ve Frameru se vkládají přes custom code v nastavení stránky. Hotový JSON-LD
  je v generátorech `build-pages.py` a `build-articles.py`.
- **301 přesměrování** — viz [REDIRECTS.md](REDIRECTS.md). Framer je umí
  nastavit v Site Settings → Redirects.
- **Písma.** Oswald i Golos Text jsou na Google Fonts, Framer je nabízí
  nativně. Hvězdičkový subset odpadá, Framer si poradí sám.

---

## 4. Rozhodnutí, které je potřeba udělat

| | Statický web (teď v repu) | Framer |
|---|---|---|
| Cena | 0 | 49 USD licence + hosting od ~5 USD/měs. |
| Edituje obsah | vývojář | **klient sám** |
| Rychlost | 0 externích požadavků | Framer runtime |
| Jazykové mutace | hotové, 45 stránek | placený tarif, nutno přeložit znovu |
| Blog | hotový, 5 článků ve 4 jazycích | CMS ve Frameru, obsah přenést |
| Stav | **hotovo, 60 stránek** | zhruba 2–3 dny práce |

Statická verze je hotová a funguje. Framer dává smysl jedině tehdy, pokud
je pro klienta zásadní, aby si obsah spravoval sám — což u firmy, která
mění ceník párkrát do roka, nemusí vyvážit 2–3 dny práce navíc a ztrátu
jazykových mutací.
