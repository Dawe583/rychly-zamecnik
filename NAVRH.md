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
| Stats bar nad ohybem | 30 let / 887 recenzí / 4,8★ / 24-7 |
| Karty služeb | 6 služeb s cenou „od" přímo na kartě |
| Why choose us | 6 důvodů převzatých z původního webu |
| 3-step process | Zavoláte → Vyjíždíme → Otevřeme |
| Rotující recenze | všech 17 skutečných Google recenzí ve dvou pásech |
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
| `--accent` | `#35E62F` | Zesvětlená verze pro tmavé pozadí — **jen** CTA, čísla a ikony |
| `--bg` | `#0A0C0A` | Velmi tmavá šeď se stopou zelené, ne čerň |
| `--surface` | `#141814` | Karty |
| `--line` | `rgba(255,255,255,.09)` | Neutrální vlasové linky |
| `--star` | `#FFC531` | Hvězdičky hodnocení |

**Zelená je vzácná, ne všudypřítomná.** Původně tónovala i každý rámeček
a hover; tím přestala být akcentem. Teď drží linky neutrální a zelená
zbyla na volací tlačítka, ceny a ikony — tam, kde má něco znamenat.

Podklad není čerň. Čerň působí lacině, protože na ní nic nemá hloubku;
`#0A0C0A` dává kartám i clonám kam se posadit. Stejnou úvahu dělá Mugen
(`#141414`).

Kontrast ověřen výpočtem: text 17,9:1, tlumený text 6,4:1, akcent 11,7:1,
text na tlačítku 10,1:1 — všechno nad WCAG AA.

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

### Tvarosloví

Rádiusy jsou sevřené — `10px` na karty, `14px` na velké bloky. Původních
18/26 px působilo měkce a šablonovitě. [Offset](https://offset.framer.website/)
používá na celém webu jedinou hodnotu 12 px, [Mugen](https://mugen.framer.website/)
tři (10/16/24); v obou případech je to znát.

Z hero titulku zmizela neonová záře za zeleným textem. Ve stupni přes 100 px
z ní byl hranatý flek a celý nadpis kvůli ní četl lacině.

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
původních adresách. Přibyly zásady ochrany osobních údajů, obchodní podmínky
a jazykové mutace na `/en/`, `/ru/` a `/ua/` — úvod, šest služeb, obě právní
stránky a celý blog včetně článků, každá se správným `hreflang` a `canonical`.

Články mají ve všech čtyřech jazycích stejné slugy. Je to schválně: adresy
už mají v Google historii a překládat je znamená zahodit ji kvůli kosmetice.

Mapa přesměrování pro `/sluzby/`, `/cenik/` a `/recenze/` je
v [REDIRECTS.md](REDIRECTS.md).

### Konkrétní vylepšení

1. **Telefon je vidět vždy.** V hlavičce, v hero, v CTA pásu, v patičce
   a na mobilu ve fixní spodní liště, která najede po odscrollování.
2. **Ceník je použitelný.** 43 položek rozdělených do 4 záložek místo jedné
   dlouhé tabulky. Slevy a příplatky barevně odlišené.
3. **Ceny přímo u služeb.** Na každé kartě je „od X Kč" — návštěvník nemusí
   nikam chodit.
4. **Recenze působí věrohodně.** Je jich všech **17** z původního webu, ve
   stejném pořadí a plném znění — včetně tříhvězdičkové („byl nepříjemný,
   zřejmě měl špatný den") a čtyřhvězdičkové paní Noskové. Weby, kde je
   100 % pětihvězdiček, působí podezřele; a hlavně by výběr jen těch
   nejlepších byl zkreslení. Dvě recenze jsou anglicky, tak jak je lidi
   napsali — mají `lang="en"`, aby je předčítač nečetl česky.
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
- Běžící pásy a recenze jedou rovnoměrně — scroll na ně nemá žádný vliv
- Hlavička se schová při scrollu dolů a vyjede při scrollu nahoru
- Animovaná počítadla, jemné zrno přes celou stránku
- Ukazatel průběhu scrollu, zvýraznění aktivní položky v menu
- Ambientní zelené světlo, které se pod sekcemi rozsvítí a pomalu driftuje
- Linka pod nadpisem sekce se dokresluje zleva doprava
- Ceníkové řádky najíždějí zleva po jednom, i po přepnutí kategorie
- Vlnka po kliknutí na tlačítko, kdekoliv na webu
- Prstenec kolem mobilního volacího tlačítka ukazuje průběh scrollu
- Ukazatel scrollování pod heroem s běžící linkou, po odscrollování zmizí

**Nic z toho se nevypíná podle zařízení.** Efekty stojí na Pointer Events,
takže naklopení karet, magnetická tlačítka i světelná stopa reagují na prst
stejně jako na kurzor — na mobilu naskočí při doteku a po zvednutí prstu se
vrátí. Plynulý scroll běží i na dotyku (`syncTouch`), ověřeno skutečnými
touch událostmi.

**A žádná výjimka nezbyla ani u `prefers-reduced-motion`.** Dřív se v tom
režimu Lenis nespustil a efekty se vypnuly; teď běží všechno stejně jako
jinde. Ověřeno v prohlížeči ve čtyřech režimech — desktop, omezený pohyb,
dotykový mobil s omezeným pohybem a mobil bez omezení — celkem 28 kontrol:
Lenis jede, nadpisy se dělí na slova, sekce se odkrývají, pásy se pohybují,
přechody nejsou zkrácené a hero video se nepotlačuje.

Za tu volbu ale stojí vědět, komu se sahá pod ruce: `prefers-reduced-motion`
si zapíná člověk, kterému rychlý pohyb na obrazovce dělá fyzicky zle —
závrať, migrénu, nevolnost. U webu, kam lidi chodí ve stresu se zabouchnutými
dveřmi, to není úplně teoretická skupina. Vrátit se to dá na jednom místě:
`reduced` v `assets/js/main.js` zpátky na `motionQuery.matches` a k tomu
obnovit blok v CSS (popsáno na jeho místě v `style.css`). Obojí musí jít
ruku v ruce — samotný CSS by pohyb zastavil jen zčásti, protože parallax
a běžící pásy dopočítává JavaScript.

---

## 4. Technický stav prototypu

| | |
|---|---|
| Počet stránek | **60** (15 českých, 15 × EN / RU / UA) + stránka 404 |
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

Přístupnost: sémantické HTML, ARIA na záložkách ceníku (klik, šipky dokola,
Home a End — ověřeno v prohlížeči ve všech čtyřech jazycích), viditelný
focus, `aria-expanded` na mobilním menu, alt texty u všech fotek.

---

## 5. Co ještě chybí / návrh dalších kroků

Prototyp je návrh vzhledu a struktury, ne hotový produkční web. Před nasazením
by bylo potřeba:

1. **Zbývá ověřit počet recenzí.** Zbytek je proti původnímu webu
   zkontrolovaný položku po položce (27. 7. 2026):

   | Údaj | Stav |
   |---|---|
   | Ceník, 43 položek | **sedí** — všechny ceny shodné, opravené jen překlepy |
   | 30 let praxe | **potvrzeno** — nadpis na úvodní stránce |
   | „do 30 minut" | **potvrzeno** — `/oprava-dveri/`; jinde slibují 10–40 min |
   | Hodnocení | **opraveno na 4,8** — viz níž |
   | Recenze | **doplněno na 17** — všechny z `/recenze/` |
   | Počet 887 | **nejasné** — viz níž |

   Hodnocení bylo v repu 4,9, ale původní web má ve strukturovaných datech
   `ratingValue: 4.8`. Průměr ze sedmnácti skutečně zveřejněných recenzí
   vychází 4,824 — obojí ukazuje na 4,8, takže je teď všude 4,8.

   **Počet recenzí si původní web protiřečí sám:** stránka `/recenze/` hlásí
   „na základě 887 recenzí", ale jeho vlastní strukturovaná data na
   podstránkách služeb uvádějí `reviewCount: 85`. Drží se tu viditelných
   887, protože strukturovaná data musí odpovídat tomu, co je na stránce
   vidět. Který údaj platí, se pozná jen z jejich profilu na Googlu —
   tohle je jediná věc, kterou nešlo ověřit zvenčí.
2. **Nechat právně zkontrolovat zásady ochrany osobních údajů a obchodní
   podmínky.** Oba texty jsou připravené jako podklad ve všech čtyřech
   jazycích, ale odpovědnost za jejich znění musí převzít někdo, kdo ji unese
   — u podmínek hlavně lhůty, záruku a odstoupení od smlouvy.

   Obchodní podmínky stojí na tom, jak firma podle původního webu opravdu
   pracuje: cena se potvrzuje na místě před zahájením prací, dvouletá záruka,
   cestovné při odmítnutí. Je v nich i klauzule o **prokázání oprávněnosti
   zásahu** — u zámečníka to není formalita, ale to hlavní, co odděluje
   řemeslo od vloupání.
3. **Rozhodnout o realizaci.** Dvě cesty:
   - **Framer** — koupit/naklonovat Tradesman a přestavět v editoru.
     Klient si pak obsah edituje sám, hosting v ceně.
   - **Statický web** — to, co je v repozitáři teď. Rychlejší, levnější
     hosting, ale úpravy obsahu přes vývojáře.
4. **Nechat překlady zkontrolovat rodilým mluvčím.** Mutace EN / RU / UA
   jsou kompletní a konzistentní, ale u textů, které mají prodávat, se
   korektura vyplatí.
5. **Analytika zatím žádná není.** Cookie lišta na ni ale už je připravená —
   drží volbu a pouští k ní ostatní přes `window.rzConsent`:

   ```js
   rzConsent.onGrant(function () { /* až tady zavést měřicí kód */ });
   ```

   Callback se spustí teprve po kliknutí na „Přijmout vše"; po „Jen nezbytné"
   se nespustí vůbec. Vracejícímu se návštěvníkovi se spustí rovnou při
   načtení. Volbu jde kdykoliv změnit odkazem „Nastavení cookies" v patičce —
   to GDPR vyžaduje, souhlas musí jít odvolat stejně snadno, jako se dával.
   Kromě `onGrant` se při každé změně posílá událost `rz:consent`.

   **Žádný měřicí skript se nesmí načíst mimo tohle.** Sledovací kód vložený
   napevno do stránky by souhlas obešel bez ohledu na to, co lišta ukazuje.
6. **Korektura blogu v mutacích.** Platí totéž co u bodu 4 — články jsou
   přeložené kompletně a konzistentně, ale u textů, které mají prodávat,
   se rodilý mluvčí vyplatí. Ceny v článcích jsou uvedené v korunách
   i v cizojazyčných verzích; to je záměr, zákazník platí v Praze.

---

## Zdroje

- Šablona: [Tradesman — Framer Community](https://www.framer.com/community/marketplace/templates/tradesman/)
- Obsah, ceník, recenze a fotografie: <https://www.rychly-zamecnik.cz/>
