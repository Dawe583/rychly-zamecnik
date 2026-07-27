# Návrh redesignu — rychly-zamecnik.cz

Návrh nového webu pro **Rychlý Zámečník — Zámečnická pohotovost Praha**.
Prototyp je funkční, ne obrázek: `index.html` je živá stránka, kterou lze
otevřít v prohlížeči a proklikat.

---

## 1. Zvolená šablona

**[Tradesman](https://www.framer.com/community/marketplace/templates/tradesman/)**
od Huehaus Studio — **zdarma**, Framer Community.
Živá ukázka: <https://tradesman.framer.website/>

### Proč právě tahle

Tradesman není obecná „business" šablona. Je postavená přesně na situaci,
ve které se zákazník zámečníka nachází — **stojí přede dveřmi, je ve stresu
a potřebuje rychle zavolat**. Struktura šablony tomu odpovídá:

| Sekce Tradesmanu | Co z ní je na novém webu |
|---|---|
| Sticky header s telefonem | Volací tlačítko viditelné pořád, na mobilu i spodní lišta |
| Hero s velkým titulkem + 2 CTA | „Zabouchlé dveře? Jsme u vás do 30 minut." |
| Stats bar nad ohybem | 30 let / 887 recenzí / 4,9★ / 24-7 |
| Karty služeb | 6 služeb s cenou „od" přímo na kartě |
| Why choose us | 6 důvodů převzatých z původního webu |
| 3-step process | Zavoláte → Vyjíždíme → Otevřeme |
| Rotující recenze | 14 skutečných Google recenzí ve dvou pásech |
| Location / hours | Mapa Prahy 1–22 + kontakty |

### Zvažované alternativy

| Šablona | Cena | Proč ne |
|---|---|---|
| [Handy](https://handymandy.framer.website/) | zdarma | Světlá, hravější — hodí se na hodinového manžela, ne na noční pohotovost |
| [Plumbing](https://plumbing-template.framer.website/) | zdarma | Silně vázaná na instalatérskou ikonografii, víc práce s přebarvením |
| [Electro](https://www.framer.com/community/marketplace/templates/electro/) | zdarma | Jednostránková, chybí prostor pro rozsáhlý ceník |

---

## 2. Vizuální směr — „Noční pohotovost"

Původní web je světlý, roztříštěný do mnoha podstránek a stavěný v Elementoru.
Nový směr staví na tom, co firma **už má** a co je vizuálně nejsilnější:
zelené polepené dodávky, noční Praha, neonové logo.

### Barvy

Odvozeno přímo z loga a firemních vozů — nic vymyšleného.

| Token | Hodnota | Použití |
|---|---|---|
| `--brand` | `#04A202` | Zelená vzorkovaná z loga |
| `--accent` | `#35E62F` | Zesvětlená verze pro tmavé pozadí — CTA, čísla, ikony |
| `--bg` | `#060806` | Téměř černá s nádechem zelené |
| `--surface` | `#121812` | Karty |
| `--star` | `#FFC531` | Hvězdičky hodnocení |

Kontrast textu na pozadí splňuje WCAG AA.

### Typografie

Systémový stack (Inter → San Francisco → Segoe UI). Žádné externí fonty:
web pak nemá jediný požadavek na cizí doménu, načte se rychleji a funguje
i pod přísnou CSP.

### Fotografie

Použité **beze změny z původního webu** — jsou dobré, jen byly špatně
naaranžované. Nejsilnější z nich, dodávka v noční Praze, dělá hero.

---

## 3. Co se oproti původnímu webu mění

### Struktura

Původní web má 9+ podstránek (`/sluzby/`, `/cenik/`, `/recenze/`,
`/otevirani-dveri/`, `/otevirani-aut/`, …). Zákazník v nouzi neproklikává
menu — potřebuje jedno číslo a jistotu, že mu někdo zvedne telefon.

Návrh je proto **jednostránkový** s kotvami. Podstránky pro jednotlivé služby
dává smysl zachovat kvůli SEO, ale jako doplněk, ne jako hlavní cestu.

### Konkrétní vylepšení

1. **Telefon je vidět vždy.** V hlavičce, v hero, v CTA pásu, v patičce
   a na mobilu ve fixní spodní liště, která najede po odscrollování.
2. **Ceník je použitelný.** 43 položek rozdělených do 4 záložek místo jedné
   dlouhé tabulky. Slevy a příplatky barevně odlišené.
3. **Ceny přímo u služeb.** Na každé kartě je „od X Kč" — návštěvník nemusí
   nikam chodit.
4. **Recenze působí věrohodně.** Včetně těch čtyřhvězdičkových. Nechal jsem
   i kritickou recenzi paní Noskové — weby, kde je 100 % pětihvězdiček,
   působí podezřele.
5. **Mapa pokrytí.** Zelená mapa pražských částí, kterou firma už má,
   nasazená přes `mix-blend-mode: screen` — na tmavém pozadí svítí.
6. **Strukturovaná data.** `LocalBusiness`/`Locksmith` JSON-LD s telefonem,
   otevírací dobou a hodnocením → hvězdičky ve výsledcích Google.

### Dynamika

Web se hýbe, ale nikde nepřekáží:

- Ken Burns na hero fotce + jemný parallax při scrollu
- Postupné odkrývání sekcí (`IntersectionObserver`, kaskádové zpoždění)
- Animovaná počítadla ve statistikách
- Dva běžící pásy recenzí proti sobě, po najetí myší se zastaví
- Pulzující kroužek kolem volacího tlačítka
- Ukazatel průběhu scrollu, zvýraznění aktivní položky v menu

Vše respektuje `prefers-reduced-motion` — komu se animace nelíbí nebo mu
dělá zle, tomu se vypnou.

---

## 4. Technický stav prototypu

| | |
|---|---|
| Velikost všech obrázků | **428 KB** (WebP, z původních 67 MB PNG) |
| Externí požadavky | **0** — žádné fonty, CDN ani trackery |
| Vodorovné přetečení | žádné (ověřeno na 390 px i 1440 px) |
| Chyby v konzoli | žádné |
| Závislosti | žádné, čistý HTML/CSS/JS |

Přístupnost: sémantické HTML, ARIA na záložkách ceníku (včetně ovládání
šipkami), viditelný focus, `aria-expanded` na mobilním menu, alt texty
u všech fotek.

---

## 5. Co ještě chybí / návrh dalších kroků

Prototyp je návrh vzhledu a struktury, ne hotový produkční web. Před nasazením
by bylo potřeba:

1. **Ověřit údaje** — 30 let praxe, „do 30 minut", počet recenzí 887 a
   hodnocení 4,9 jsem převzal z původního webu. Stojí za to potvrdit,
   že platí (u dojezdového času hlavně kvůli tomu, že je to slib).
2. **Doplnit povinné náležitosti** — GDPR / zásady cookies, obchodní podmínky.
   Původní web má cookie lištu, tady zatím není, protože prototyp nic nesbírá.
3. **Rozhodnout o realizaci.** Dvě cesty:
   - **Framer** — koupit/naklonovat Tradesman a přestavět v editoru.
     Klient si pak obsah edituje sám, hosting v ceně.
   - **Statický web** — to, co je v repozitáři teď. Rychlejší, levnější
     hosting, ale úpravy obsahu přes vývojáře.
4. **Zachovat SEO.** Původní web má vybudované pozice na „zámečník Praha".
   Při přechodu je nutné držet URL struktury podstránek nebo nastavit 301
   přesměrování, jinak firma přijde o organický provoz.
5. **Jazykové verze.** Původní web má EN / RU / UA přes TranslatePress.
   V návrhu zatím jen čeština.

---

## Zdroje

- Šablona: [Tradesman — Framer Community](https://www.framer.com/community/marketplace/templates/tradesman/)
- Obsah, ceník, recenze a fotografie: <https://www.rychly-zamecnik.cz/>
