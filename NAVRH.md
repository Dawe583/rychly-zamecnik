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

Dvojice písem, obě proměnná a hostovaná lokálně — žádné CDN:

| Role | Písmo | Proč |
|---|---|---|
| Nadpisy, čísla, tlačítka | **Oswald** 400–700 | Kondenzovaný grotesk. Industriální, naléhavý — tón, kterým mluví dopravní značení a dílenské cedule, ne webová šablona. Úzké písmo navíc unese větší stupeň, takže titulek může být opravdu velký. |
| Běžný text | **Golos Text** 400–700 | Čistý text grotesk s **nativní cyrilicí** od Paratype — u RU a UA mutací je to znát. |
| Hvězdičky hodnocení | **Noto Sans Symbols 2** (jen ★ a ☆) | Ani jedno z hlavních písem znak ★ nemá. Bez tohohle 0,7kB subsetu by spadl na systémové písmo a hodnocení by v každém prohlížeči vypadalo jinak. |

Obě hlavní písma jsou subsetovaná na latinku, latin extended a cyrilici —
dohromady **92 kB**. Licence OFL, přiložené v `assets/fonts/`.

Záměrně se vyhýbáme Interu, Space Grotesku a Poppins. Nejsou špatné, ale
jsou to výchozí volby, které dnes web okamžitě zařadí mezi generické.

### Fotografie a video

Fotky jsou použité **beze změny z původního webu** — jsou dobré, jen byly
špatně naaranžované.

V heru běží **video smyčka sestavená z těch samých fotek**: čtyři záběry
(noční dodávka u Hradu, tým, otevírání dveří, otevírání auta) s pomalým
nájezdem a prolínáním, 11,6 s, bezešvě navazuje. Není to koupený stock ani
nic vymyšleného — je to jejich vlastní materiál rozhýbaný ve `build-video.py`.

Video je ztmavené (`brightness .58`) a hero má silnější clonu zleva, aby
titulek držel kontrast i nad nejsvětlejším záběrem smyčky.

---

## 3. Co se oproti původnímu webu mění

### Struktura

Původní web má 9+ podstránek (`/sluzby/`, `/cenik/`, `/recenze/`,
`/otevirani-dveri/`, `/otevirani-aut/`, …). Zákazník v nouzi neproklikává
menu — potřebuje jedno číslo a jistotu, že mu někdo zvedne telefon.

Domovská stránka je proto **jednostránková** s kotvami: hero, služby, proč my,
postup, ceník, mapa, recenze. To je hlavní cesta pro člověka, který stojí
přede dveřmi.

**Podstránky služeb zůstávají** — na původních URL a s vlastním obsahem.
Neslouží pro nouzového návštěvníka, ale pro vyhledávače a pro toho, kdo si
službu vybírá v klidu:

| URL | Obsah |
|---|---|
| `/otevirani-dveri/` | Nouzové otevírání dveří |
| `/vymena-zamku/` | Výměna zámků a vložek |
| `/otevirani-aut/` | Otevírání aut |
| `/otevirani-trezoru/` | Otevírání a servis trezorů |
| `/oprava-dveri/` | Oprava dveří po vloupání |
| `/zamecnicka-pohotovost/` | Pohotovost nonstop |

Každá má vlastní, neopakující se text, ceník jen pro danou službu, pět
otázek a odpovědí a strukturovaná data `Service` + `BreadcrumbList` +
`FAQPage`. Karty služeb na úvodu na ně odkazují, stejně jako patička.

Blog zůstal na `/blogy-o-zamcich-a-zamecnictvich/` i s pěti články na jejich
původních adresách. Přibyly zásady ochrany osobních údajů a jazykové mutace
na `/en/`, `/ru/` a `/ua/` — úvod, šest služeb a zásady, každá se správným
`hreflang` a `canonical`.

Mapa přesměrování pro `/sluzby/`, `/cenik/` a `/recenze/` je
v [REDIRECTS.md](REDIRECTS.md).

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

Plynulý scroll obstarává **[Lenis](https://github.com/darkroomengineering/lenis)**
(MIT), vendorovaný v repozitáři — žádné CDN. Všechny efekty běží v jediné
rAF smyčce, kterou Lenis pohání, takže se scroll listenery nepřebíjejí:

- Nadpisy se rozpadají na slova a naskakují zdola s kaskádou
- Odkrývání sekcí v šesti variantách (fade, scale, zleva, zprava, blur, maska)
- Parallax na hero fotce i na CTA pásu
- 3D naklopení karet s leskem, který sleduje kurzor
- Magnetická volací tlačítka, světelná stopa kurzoru
- Běžící pásy reagují na rychlost scrollu — zrychlí a lehce se zkosí
- Hlavička se schová při scrollu dolů a vyjede při scrollu nahoru
- Animovaná počítadla, jemné zrno přes celou stránku
- Ukazatel průběhu scrollu, zvýraznění aktivní položky v menu
- Ambientní zelené světlo, které se pod sekcemi rozsvítí a pomalu driftuje
- Linka pod nadpisem sekce se dokresluje zleva doprava
- Ceníkové řádky najíždějí zleva po jednom
- Vlnka po kliknutí na tlačítko, kdekoliv na webu
- Prstenec kolem mobilního volacího tlačítka ukazuje průběh scrollu
- Ukazatel scrollování pod heroem s běžící linkou, po odscrollování zmizí

**Nic z toho se nevypíná podle zařízení.** Efekty stojí na Pointer Events,
takže naklopení karet, magnetická tlačítka i světelná stopa reagují na prst
stejně jako na kurzor — na mobilu naskočí při doteku a po zvednutí prstu se
vrátí. Plynulý scroll běží i na dotyku (`syncTouch`), ověřeno skutečnými
touch událostmi.

Jedinou výjimkou je systémové nastavení `prefers-reduced-motion`. To ale není
omezení zařízení, ale výslovná volba člověka, kterému rychlý pohyb na obrazovce
dělá fyzicky zle. V tom režimu se Lenis vůbec nespustí, nadpisy se nerozdělují
a obsah je rovnou viditelný. Pokud má běžet i tam, je to jedna podmínka v
`assets/js/main.js`.

---

## 4. Technický stav prototypu

| | |
|---|---|
| Počet stránek | **38** (14 českých, 8 × EN / RU / UA) |
| Velikost všech obrázků | **428 KB** (WebP, z původních 67 MB PNG) |
| Písma | **92 kB** (2 proměnná, subsetovaná) + 0,7 kB hvězdičky |
| Hero video | **1,1 MB** VP8/WebM, 11,6 s smyčka |
| Externí požadavky | **0** — žádné fonty, CDN ani trackery |
| Vodorovné přetečení | žádné (ověřeno na 360, 390, 820, 1180 a 1440 px) |
| Chyby v konzoli | žádné (proklikáno crawlerem přes všech 38 stránek) |
| Závislosti | jediná — Lenis (13 KB, MIT), vendorovaný v repozitáři |

**Hero video je jen WebM.** ffmpeg dostupný v tomhle prostředí neumí H.264,
takže MP4 varianta chybí — starší Safari a iOS pod 14.5 uvidí místo videa
plakát, což je přesně původní statické hero. Doplnit MP4 je jeden příkaz,
až bude po ruce plný ffmpeg; generátor snímků je v `build-video.py`.

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
2. **Nechat právně zkontrolovat zásady ochrany osobních údajů.** Text je
   připravený jako podklad ve všech čtyřech jazycích, ale odpovědnost za jeho
   znění musí převzít někdo, kdo ji unese. Obchodní podmínky zatím chybí.
3. **Rozhodnout o realizaci.** Dvě cesty:
   - **Framer** — koupit/naklonovat Tradesman a přestavět v editoru.
     Klient si pak obsah edituje sám, hosting v ceně.
   - **Statický web** — to, co je v repozitáři teď. Rychlejší, levnější
     hosting, ale úpravy obsahu přes vývojáře.
4. **Nechat překlady zkontrolovat rodilým mluvčím.** Mutace EN / RU / UA
   jsou kompletní a konzistentní, ale u textů, které mají prodávat, se
   korektura vyplatí.
5. **Cookie lišta zatím nic nespouští.** Ukládá volbu do `localStorage`,
   ale žádná analytika na ni napojená není — až se nasadí, musí se
   spouštět právě podle téhle volby.
6. **Blog je jen česky.** V jazykových mutacích na něj proto neodkazujeme.
   Až vzniknou překlady článků, stačí odkaz vrátit do navigace.

---

## Zdroje

- Šablona: [Tradesman — Framer Community](https://www.framer.com/community/marketplace/templates/tradesman/)
- Obsah, ceník, recenze a fotografie: <https://www.rychly-zamecnik.cz/>
