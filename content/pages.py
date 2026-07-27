# -*- coding: utf-8 -*-
"""
Obsah podstránek služeb.

Texty, ceny i otázky vycházejí z původního webu rychly-zamecnik.cz — každá
stránka má vlastní, neopakující se obsah, aby si udržela pozice ve vyhledávání.
Klíč slovníku = URL segment, který web používal doteď (kvůli SEO neměnit).
"""

# Ceníkové položky sdílené mezi stránkami — jediné místo, kde se ceny udržují.
CENIK = {
    "otevirani-bytu": [
        ("Zabouchnuté dveře / bez bezpečnostních prvků", "od 290 Kč"),
        ("Zabouchnuté dveře / s bezpečnostním kováním", "od 490 Kč"),
        ("Zabouchnuté / bezpečnostní", "od 790 Kč"),
        ("Zabouchnuté / s vícebodovým zámkem", "od 990 Kč"),
        ("Zamčeno / obyčejné, bez bezp. prvků", "od 390 Kč"),
        ("Zamčeno / s bezpečnostním kováním", "od 890 Kč"),
        ("Zamčeno / kování R1, R3, OS1", "od 990 Kč"),
        ("Zamčeno / přídavný zámek", "od 890 Kč"),
        ("Zamčeno / zaseklý trezorový zámek", "od 1 190 Kč"),
        ("Zamčeno / prasklá střelka zámku", "od 790 Kč"),
        ("Zamčeno / dozický zámek", "od 790 Kč"),
        ("Zamčeno / schránkový, stolový, nábytkový zámek", "od 590 Kč"),
        ("Zamčeno / trezorový zámek", "od 1 990 Kč"),
        ("Otevření, oprava a servis trezoru", "dle typu"),
    ],
    "zamky": [
        ("Výměna zámku / obyčejné dveře bez kování", "od 290 Kč"),
        ("Výměna vložky bezpečnostního zámku", "od 390 Kč"),
        ("Výměna vložky / rozvorové zámky", "od 790 Kč"),
        ("Výměna zámku CR, Mottura, CISA", "od 1 090 Kč"),
        ("Oprava / zaseklá střelka nebo závora", "od 1 090 Kč"),
        ("Montáž / chytré zámky", "od 990 Kč"),
        ("Montáž kování R1, Richter apod.", "od 890 Kč"),
        ("Montáž zadlabacího zámku", "od 690 Kč"),
        ("Montáž elektromechanického zámku", "od 1 090 Kč"),
        ("Vyjmutí zlomeného klíče", "od 490 Kč"),
        ("Demontáž vložky bez klíče", "od 590 Kč"),
        ("Montáž bezpečnostní závory", "od 1 490 Kč"),
        ("Montáž přídavného zámku", "od 990 Kč"),
        ("Oprava dveří", "od 390 Kč"),
    ],
    # Tahle kategorie se na webu vysází přímo v index.html (čtvrtá záložka
    # ceníku), tady je proto, aby export do Frameru měl ceník kompletní.
    # Při změně upravit na obou místech.
    "ostatni": [
        ("Přepravné (dle vzdálenosti)", "490 Kč"),
        ("Doprava mimo Prahu", "+20 Kč / km"),
        ("Expresní výjezd, pohotovost", "300 Kč"),
        ("Sleva pro stálé zákazníky", "−50 %"),
        ("Sleva pro oběti trestných činů (vloupání apod.)", "−30 %"),
        ("Mimopracovní příplatek (17:00–7:00), víkend, svátek", "+100 %"),
        ("Spotřební materiál (vrtáky, frézy, kotouče)", "dle spotřeby"),
    ],
    "auta": [
        ("Otevření auta do r. v. 2002 (bez safe)", "od 590 Kč"),
        ("Otevření auta r. v. 2002 – 2007 (bez safe)", "od 990 Kč"),
        ("Otevření auta od r. v. 2007 (bez safe)", "od 1 290 Kč"),
        ("Trezorový typ zabezpečení do r. v. 2007", "od 1 490 Kč"),
        ("Trezorový typ zabezpečení r. v. 2008 – 2018", "od 1 690 Kč"),
        ("Výměna zámků", "od 990 Kč"),
        ("Výměna spínací skříňky", "od 1 990 Kč"),
        ("Demontáž zámku řazení (DEFEND LOCK apod.)", "od 2 490 Kč"),
    ],
}


PAGES = {
    # ------------------------------------------------------------------ #
    "otevirani-dveri": {
        "nav": "Otevírání dveří",
        "h1": "Nouzové otevírání dveří v Praze",
        "title": "Otevírání dveří Praha — nouzové otevření zabouchnutých dveří NONSTOP",
        "desc": "Zabouchli jste si dveře nebo ztratili klíče? Otevřeme bez poškození, "
                "technik u vás do 10–40 minut. Nonstop 24/7, od 290 Kč.",
        "img": "otevirani-dveri",
        "img_alt": "Zámečník otevírá zabouchnuté dveře bez poškození",
        "lead": "Zabouchli jste si dveře nebo ztratili klíče? Chápeme, že je to nepříjemná "
                "situace — a jsme tu pro vás nonstop, 24 hodin denně, 7 dní v týdnu.",
        "ticks": [
            "Technik dorazí <b>za 10–40 minut</b> kamkoliv po Praze",
            "Otevřeme <b>bez jediného škrábance</b> — zámek zůstane funkční",
            "Cenu řekneme <b>dopředu</b>, žádné skryté poplatky",
        ],
        "why_head": "Proč je Rychlý Zámečník správná volba pro otevírání dveří?",
        "why_lead": "V krizové chvíli není vhodné ztrácet čas. Proto jsme vám k dispozici "
                    "pro okamžitou pomoc 24/7, připraveni jednat ihned.",
        "why": [
            ("bolt", "Expresní příjezd",
             "Náš tým vyjíždí okamžitě a garantuje dojezd do 10–40 minut, ať jste "
             "kdekoliv v metropoli."),
            ("shield", "Šetrné otevírání",
             "Technici využívají pokročilé nástroje, aby otevřeli dveře bez jakéhokoliv "
             "poškození. Zámek bude i nadále fungovat tak, jak má."),
            ("coin", "Férové ceny",
             "Za nouzové otevření dveří garantujeme srozumitelnou a poctivou cenu, "
             "bez skrytých poplatků."),
        ],
        "prices": "otevirani-bytu",
        "prose_head": "Co nás dělá jedničkou v nouzovém otevírání dveří",
        "prose": [
            "Jsme specialisté na krizové situace, kde se počítá každá minuta. Kromě "
            "technických dovedností a rychlosti garantujeme i <strong>lidský a empatický "
            "přístup</strong>, který vám v nepříjemné chvíli uleví.",
            "V naší výbavě najdete pouze nejmodernější technologie pro nouzové otevírání. "
            "Díky tomu vyřešíme i ten nejtěžší případ rychle a vždy bez poškození vašeho zámku.",
            "Náš tým tvoří zkušení zámečníci, kteří pravidelně rozšiřují své znalosti a mají "
            "komplexní přehled o bezpečnostních systémech všech typů.",
        ],
        "faq": [
            ("Jak rychle přijede zámečník?",
             "Po Praze garantujeme dojezd v rozmezí 10–40 minut od telefonátu podle toho, "
             "kde se právě nachází nejbližší technik a jaká je dopravní situace. Přesnější "
             "odhad vám řekneme rovnou do telefonu."),
            ("Poškodíte mi dveře nebo zámek?",
             "V drtivé většině případů ne. Používáme nedestruktivní metody, po kterých zámek "
             "dál normálně funguje. Pokud by konkrétní zámek nedestruktivní otevření "
             "neumožňoval, řekneme vám to předem a domluvíme se na dalším postupu."),
            ("Kolik otevření dveří stojí?",
             "Zabouchnuté dveře bez bezpečnostních prvků otevřeme od 290 Kč, se bezpečnostním "
             "kováním od 490 Kč. Zamčené dveře začínají na 390 Kč. Konečná cena závisí na typu "
             "zámku a potvrdíme ji před zahájením práce."),
            ("Musím prokázat, že jde o můj byt?",
             "Ano. Před zásahem po vás budeme chtít doklad totožnosti a doložení vztahu "
             "k nemovitosti — například nájemní smlouvu, výpis z katastru nebo potvrzení "
             "od souseda či majitele. Je to ochrana vás i nás."),
            ("Jezdíte i v noci a o svátcích?",
             "Ano, dispečink bere telefon nepřetržitě, včetně nocí, víkendů i státních svátků. "
             "Mimo pracovní dobu (17:00–7:00), o víkendech a svátcích se účtuje příplatek."),
        ],
    },

    # ------------------------------------------------------------------ #
    "vymena-zamku": {
        "nav": "Výměna zámků",
        "h1": "Výměna zámků a bezpečnostních vložek v Praze",
        "title": "Výměna zámků Praha — montáž bezpečnostních vložek a kování",
        "desc": "Montáž a výměna zámků všech značek a bezpečnostních tříd — FAB, EVVA, "
                "MUL-T-LOCK, TOKOZ, ABUS. Poradenství zdarma, od 290 Kč.",
        "img": "vymena-zamku",
        "img_alt": "Montáž a výměna bezpečnostního zámku",
        "lead": "Výměna zámků je práce, kterou se v Praze zabýváme už celá léta. Postaráme se "
                "o montáž bezpečnostních vložek a zámků jakékoli značky, včetně systému "
                "generálního klíče.",
        "ticks": [
            "Do jakékoli části Prahy dorazíme <b>zhruba do 20 minut</b>",
            "Vložky <b>všech bezpečnostních tříd 1–5</b> od předních výrobců",
            "<b>Poradenství zdarma</b> — navrhneme řešení podle ceny i bezpečnosti",
        ],
        "why_head": "Proč je Rychlý Zámečník správná volba pro výměnu zámku?",
        "why_lead": "Zajistíme nejen rychlou a precizní výměnu zámku. Poskytneme i odborné "
                    "poradenství při výběru té nejlepší bezpečnostní vložky pro vaše dveře.",
        "why": [
            ("bolt", "Rychlost a kompletní vybavení",
             "Zámečníci přijíždějí plně připravení — vezou předem domluvený typ zámku a vložky "
             "i náhradní díly pro případ nečekaných komplikací."),
            ("clock", "Výměna zámku ihned",
             "Naléhavé bezpečnostní důvody si zaslouží rychlé řešení. Naše pohotovost je "
             "v plné akci 24/7 — neodkládejte svou ochranu."),
            ("users", "Poradenství na míru zdarma",
             "Projdeme s vámi všechny možnosti a vysvětlíme, co znamenají bezpečnostní třídy "
             "a proč je důležité správně kombinovat zámek s kováním."),
        ],
        "prices": "zamky",
        "prose_head": "Profesionální výměna bezpečnostního zámku",
        "prose": [
            "Pracujeme s <strong>certifikovanými bezpečnostními vložkami ve všech třídách "
            "(1–5)</strong> od předních světových výrobců, jako jsou FAB, EVVA, MUL-T-LOCK, "
            "RICHTER, TOKOZ nebo ABUS. Specializujeme se také na bezpečnostní zámky ATRA, "
            "MOTTURA a CISA.",
            "Pro mnoho zlodějů je samotná bezpečnostní vložka spíš výzvou než překážkou. "
            "Vždy proto doporučujeme přemýšlet společně s výměnou vložky i o "
            "<strong>bezpečnostním kování</strong>, které vložku chrání před vylomením, "
            "případně o bezpečnostní závoře proti vypáčení dveří.",
            "Všechny instalované produkty splňují evropské standardy kvality, bezpečnosti "
            "a životnosti. Naši technici mají potřebné certifikace a průběžně si prohlubují "
            "znalosti na pravidelných školeních.",
        ],
        "faq": [
            ("Jaký zámek si mám vybrat?",
             "Záleží na tom, co chráníte a jaké máte dveře. Bezpečnostní třídy jdou od 1 do 5 — "
             "pro běžný byt v panelovém domě obvykle stačí třída 3 v kombinaci s bezpečnostním "
             "kováním. Konzultaci vám dáme zdarma ještě před objednávkou."),
            ("Stačí vyměnit jen vložku, nebo celý zámek?",
             "Ve většině případů stačí vyměnit cylindrickou vložku — to je levnější a rychlejší. "
             "Celý zámek se mění, když je poškozený mechanismus, zasekne se střelka nebo "
             "přecházíte na jiný typ zabezpečení."),
            ("Máte vložky skladem, nebo se musí objednávat?",
             "Nejběžnější typy a varianty vozíme s sebou, takže výměnu obvykle zvládneme "
             "na jeden výjezd. Speciální nebo atypické vložky objednáváme — termín vám "
             "potvrdíme po telefonu."),
            ("Nastavíte mi systém generálního klíče?",
             "Ano. Systém generálního klíče — kdy jeden klíč otevírá více zámků a další klíče "
             "jen vybrané — navrhneme a nainstalujeme na míru. Hodí se do domů, kanceláří "
             "i provozoven."),
            ("Jakou dáváte záruku?",
             "Na odvedenou práci i použitý materiál dáváme dvouletou záruku."),
        ],
    },

    # ------------------------------------------------------------------ #
    "otevirani-aut": {
        "nav": "Otevírání aut",
        "h1": "Nouzové otevírání aut bez poškození",
        "title": "Otevírání aut Praha — nouzové otevření vozu bez poškození NONSTOP",
        "desc": "Zamklo se vám auto a klíče jsou uvnitř? Otevřeme bez rozbíjení skla "
                "a bez poškození laku či elektroniky. Nonstop 24/7, od 590 Kč.",
        "img": "otevirani-aut",
        "img_alt": "Nouzové otevírání auta bez klíče a bez poškození",
        "lead": "Zamklo se vám auto a klíče jsou uvnitř? Vybila se autobaterie? Zavřené dítě "
                "nebo běžící motor? Řešíme to — a bez rozbíjení skla.",
        "ticks": [
            "<b>Nebudete rozbíjet sklo</b> — otevíráme šetrnými metodami",
            "Zachováme <b>100% integritu laku, dveří i elektroniky</b>",
            "Dorazíme bleskově, pohotovost jede <b>24/7</b>",
        ],
        "why_head": "Proč je Rychlý Zámečník správná volba pro otevírání auta?",
        "why_lead": "V urgentních situacích s otevřením auta neexistuje kompromis. Naše "
                    "rychlost reakce a profesionální praxe jsou vaší zárukou.",
        "why": [
            ("bolt", "Rychlost příjezdu",
             "Díky optimální logistice a nepřetržité službě je certifikovaný zámečník "
             "u vašeho vozu během 10 až 40 minut od přijetí hovoru."),
            ("shield", "Otevření bez poškození",
             "Garantujeme šetrné metody, které zachovají integritu laku, dveří i citlivé "
             "elektroniky vozidla. Neřešíte žádné následné opravy."),
            ("clock", "Zámečník ihned",
             "Ať už zámečníka sháníte uprostřed noci, o víkendu nebo ve státní svátek, "
             "naše pohotovost je vždy připravena."),
        ],
        "prices": "auta",
        "prose_head": "Otevřeme i moderní vozy s trezorovým zabezpečením",
        "prose": [
            "Cena za otevření auta se odvíjí především od <strong>roku výroby a typu "
            "zabezpečení</strong>. Starší vozy do roku 2002 jsou nejjednodušší, novější "
            "modely s trezorovým typem zámku vyžadují speciální nástroje a víc času.",
            "Kromě samotného otevření řešíme i <strong>výměnu zámků, spínacích skříněk "
            "a demontáž zámků řazení</strong> typu DEFEND LOCK. Vše na místě, bez odtahu "
            "do servisu.",
            "Pokud je ve voze zavřené dítě nebo zvíře, řekněte to hned na začátku hovoru — "
            "takový výjezd řadíme na začátek fronty.",
        ],
        "faq": [
            ("Otevřete i novější auto s imobilizérem?",
             "Ano. Otevření vozu a imobilizér jsou dvě různé věci — dostaneme vás dovnitř, "
             "aniž bychom zasahovali do elektroniky. U vozů od roku 2007 a u trezorového typu "
             "zabezpečení je zásah náročnější, což se odráží v ceně."),
            ("Budete rozbíjet okno?",
             "Ne. Používáme nástroje, které otevřou vůz bez poškození skla, laku i těsnění. "
             "Rozbíjení skla je pro nás krajní řešení, ke kterému bychom sáhli jedině "
             "po vaší výslovné žádosti — třeba při ohrožení života."),
            ("Musím prokázat, že je auto moje?",
             "Ano, před otevřením budeme chtít doklad totožnosti a doklad k vozidlu — "
             "velký nebo malý technický průkaz, případně smlouvu. Bez toho vůz neotevřeme."),
            ("Co když mám klíče zamčené uvnitř a běží motor?",
             "Zavolejte hned a zmiňte to — je to naléhavá situace, kterou řešíme přednostně. "
             "Vůz otevřeme bez poškození, motor přitom může běžet dál."),
            ("Uděláte mi nový klíč, když jsem ten původní ztratil?",
             "Vůz otevřeme a umíme vyměnit zámky i spínací skříňku. Výrobu a naprogramování "
             "nového čipového klíče je ale u novějších vozů potřeba řešit u značkového "
             "servisu — poradíme vám po telefonu."),
        ],
    },

    # ------------------------------------------------------------------ #
    "otevirani-trezoru": {
        "nav": "Otevírání trezorů",
        "h1": "Otevření a servis trezorů",
        "title": "Otevírání trezorů Praha — nouzové otevření trezoru, servis a opravy",
        "desc": "Zapomněli jste kód nebo ztratili klíč od trezoru? Otevíráme elektronické "
                "i mechanické trezory od roku 1990 — SAFEMETAL, ROTTNER, KOVONA a další.",
        "img": "otevirani-trezoru",
        "img_alt": "Zámečník otevírá trezor",
        "lead": "Potřebujete se dostat do trezoru, ale chybí klíč nebo kód? Vybila se baterie? "
                "Jsme specialisté na nouzové otevírání trezorů s praxí od roku 1990.",
        "ticks": [
            "Otevíráme <b>elektronické i mechanické kódové trezory</b>",
            "Nejšetrnější metody — trezor půjde <b>dál bezpečně používat</b>",
            "I nutný malý zásah po sobě <b>profesionálně začistíme</b> speciálním tmelem",
        ],
        "why_head": "Proč je Rychlý Zámečník správná volba pro otevírání trezorů?",
        "why_lead": "Zajistíme nejen rychlé nouzové otevření. Poradíme i s výběrem "
                    "nejvhodnějšího trezorového zámku pro váš trezor.",
        "why": [
            ("bolt", "Bleskový příjezd",
             "Tým startuje ihned po zavolání a garantuje dojezd po celé metropoli "
             "v rozmezí 10 až 40 minut."),
            ("shield", "Nedestruktivní otevření",
             "Trezor otevíráme metodami, které zaručují nulové poškození. Mechanismus "
             "bude po zásahu plně funkční, jako předtím."),
            ("coin", "Férová cena bez šoků",
             "Otevření trezoru je samo o sobě dost stresující. Garantujeme transparentní "
             "cenu rovnou — žádná překvapení na faktuře."),
        ],
        "prices": "otevirani-bytu",
        "prose_head": "Se kterými trezory si poradíme",
        "prose": [
            "Otevíráme trezory značek <strong>SAFEMETAL, ROTTNER, KOVONA, T-SAFE, ASIST, "
            "BULDOK</strong> a mnoha dalších — mechanické klíčové, kódové i elektronické.",
            "Nejčastější důvody, proč nás volají: zapomenutý kód nebo kombinace, ztracený "
            "či zlomený klíč, <strong>vybitá baterie u elektronického zámku</strong> "
            "a porucha mechaniky.",
            "Kromě otevření zajišťujeme i opravu a kompletní servis trezorů včetně výměny "
            "trezorového zámku. Cena se určuje podle typu trezoru — proto ji vždy "
            "domlouváme individuálně.",
        ],
        "faq": [
            ("Otevřete trezor, aniž byste ho zničili?",
             "To je náš cíl a ve většině případů se to daří. Volíme nejšetrnější možnou "
             "metodu tak, aby trezor šel dál používat. Pokud je nutné navrtat, otvor "
             "po sobě profesionálně začistíme speciálním tmelem."),
            ("Zapomněl jsem kód. Jde s tím něco dělat?",
             "Ano, to je jeden z nejčastějších důvodů, proč nás volají. U elektronických "
             "i mechanických kódových trezorů máme postupy, jak se dovnitř dostat, "
             "a následně vám nastavíme nový kód."),
            ("Kolik otevření trezoru stojí?",
             "Cena se řídí typem trezoru a složitostí zásahu, proto ji uvádíme jako "
             "„dle typu“. Zaseklý trezorový zámek u dveří otevíráme od 1 190 Kč, "
             "zamčený trezorový zámek od 1 990 Kč. Konkrétní odhad dostanete po telefonu."),
            ("Vyměníte mi trezorový zámek?",
             "Ano, zajišťujeme opravy i kompletní servis trezorů včetně výměny zámku "
             "a poradíme s výběrem vhodného typu."),
            ("Co si mám připravit?",
             "Doklad totožnosti a doklad o tom, že trezor patří vám nebo vaší firmě — "
             "účtenku, fakturu, pojistnou smlouvu. U firemních trezorů potřebujeme "
             "souhlas oprávněné osoby."),
        ],
    },

    # ------------------------------------------------------------------ #
    "oprava-dveri": {
        "nav": "Oprava dveří",
        "h1": "Oprava dveří po vloupání",
        "title": "Oprava dveří po vloupání Praha — okamžitý výjezd a zabezpečení",
        "desc": "Vloupání je šok. Zajistíme rychlý návrat k bezpečí — opravíme dveře "
                "i zámky a navrhneme trvalé zabezpečení. Nonstop 24/7, od 390 Kč.",
        "img": "otevirani-zamku",
        "img_alt": "Oprava dveří a zámku po vloupání",
        "lead": "Vloupání je šok. My zajistíme rychlý návrat k bezpečí — přijedeme, dveře "
                "a zámky profesionálně opravíme a rovnou navrhneme, jak objekt zabezpečit "
                "do budoucna.",
        "ticks": [
            "<b>Okamžitý výjezd</b> — dveře a zámky opravíme na místě",
            "<b>Trvalé zabezpečení</b> — navrhneme řešení pro byt i provozovnu",
            "Sleva <b>30 %</b> pro oběti trestných činů",
        ],
        "why_head": "Proč je Rychlý Zámečník správná volba pro opravu dveří?",
        "why_lead": "V krizové chvíli je čas to nejdražší. Proto je zámečník k dispozici "
                    "nonstop, 24 hodin denně, 7 dní v týdnu.",
        "why": [
            ("bolt", "Příjezd do 30 minut",
             "Zámečníci jsou rozmístění po celé metropoli, aby byla rychlost maximální. "
             "U krizových zásahů garantujeme příjezd za 10–30 minut."),
            ("clock", "Volejte kdykoliv",
             "Jsme dostupní nepřetržitě — vaše jistota rychlé a profesionální pomoci "
             "v jakoukoli denní i noční dobu."),
            ("coin", "Férové ceny",
             "Vloupání je dostatečný stres. Žádné kličky, žádné skryté poplatky — "
             "náš slib transparentnosti platí bez výhrad."),
        ],
        "prices": "zamky",
        "prose_head": "Co dělat, když se k vám někdo vloupal",
        "prose": [
            "<strong>Nejdřív zavolejte policii</strong> a než dorazí, pokud možno nic "
            "nepřemisťujte — kvůli ohledání místa i kvůli pojišťovně. Vyfoťte si stav dveří "
            "a zámku, budete to potřebovat při hlášení pojistné události.",
            "Teprve potom volejte nás. Přijedeme, <strong>zprovozníme dveře a vyměníme "
            "poškozené zámky</strong>, abyste mohli byt bezpečně zamknout ještě týž den.",
            "Rovnou s vámi projdeme, kudy se pachatel dostal dovnitř, a navrhneme, co "
            "posílit — bezpečnostní vložku s kováním, přídavný zámek nebo závoru proti "
            "vypáčení. <strong>Obětem trestných činů dáváme slevu 30 %.</strong>",
        ],
        "faq": [
            ("Přijedete hned, nebo se objednává termín?",
             "Po vloupání jezdíme okamžitě — je to krizový zásah. Garantujeme příjezd "
             "za 10–30 minut od telefonátu."),
            ("Zaplatí to pojišťovna?",
             "Ve většině případů ano, pokud máte sjednané pojištění domácnosti. Vystavíme "
             "vám doklad s rozpisem prací a materiálu, který pojišťovně předložíte. "
             "Nafoťte si prosím stav dveří ještě před opravou."),
            ("Půjdou původní dveře opravit, nebo je potřeba nové?",
             "Záleží na rozsahu poškození. Často stačí opravit zárubeň, vyměnit zámek "
             "a kování. Pokud jsou dveře vylomené natolik, že už nejde zaručit bezpečnost, "
             "řekneme vám to na rovinu a doporučíme výměnu."),
            ("Poradíte, jak se bránit příště?",
             "Ano, je to součást zásahu. Projdeme s vámi, kudy se pachatel dostal dovnitř, "
             "a navrhneme konkrétní opatření — bezpečnostní vložku s kováním, přídavný "
             "zámek nebo bezpečnostní závoru."),
            ("Platí sleva pro oběti trestných činů automaticky?",
             "Uplatníme ji na místě — stačí říct, že jde o zásah po vloupání. Doporučujeme "
             "mít po ruce číslo jednací od policie."),
        ],
    },

    # ------------------------------------------------------------------ #
    "zamecnicka-pohotovost": {
        "nav": "Zámečnická pohotovost",
        "h1": "Zámečnická pohotovost Praha — nonstop 24/7",
        "title": "Zámečnická pohotovost Praha NONSTOP — zámečník 24 hodin denně",
        "desc": "Nejrychlejší zámečnická pohotovost v Praze za rozumné peníze. Otevírání "
                "dveří, aut i trezorů, výměna zámků. Nonstop 24/7, 30 let praxe.",
        "img": "vyjezd-den",
        "img_alt": "Vůz zámečnické pohotovosti Rychlý Zámečník na výjezdu",
        "lead": "Zámečnictví s dlouholetou historií. Kvalitní zámečnická pohotovost "
                "za rozumné peníze — kterýkoliv den, v kteroukoliv dobu.",
        "ticks": [
            "Otevírání <b>zabouchnutých i zamčených dveří</b> a nouzové otevírání zámků",
            "Otevírání <b>aut bez klíče</b>, aniž by došlo k jakémukoliv poškození",
            "Otevírání, oprava a <b>kompletní servis trezorů</b>",
            "Montáže a výměna <b>všech typů zámků</b>, vložek i bezpečnostního kování",
            "Montáže bezpečnostních <b>závor, přídavných zámků a zábran</b>",
            "Opravy dveří po vloupání a <b>návrhy zabezpečení objektu</b>",
        ],
        "why_head": "Kvalitní zámečník Praha, na kterého se spolehnete",
        "why_lead": "Ocitli jste se v situaci, kdy potřebujete rychlou pomoc zámečníka nebo "
                    "jen chcete s něčím poradit? Naše zámečnictví je tu pro vás 24 hodin denně.",
        "why": [
            ("clock", "Nonstop, opravdu",
             "Dispečink bere telefon ve dne v noci, o víkendech i o státních svátcích. "
             "Konzultace po telefonu je zdarma."),
            ("users", "Tisíce zákazníků ročně",
             "Zámečnictví poskytuje služby už dlouhá léta a ročně obslouží tisíce "
             "zákazníků — profesionální práci odvedeme bez chyb."),
            ("star", "Nejmodernější nářadí",
             "Abychom mohli zaručit nejvyšší kvalitu, používáme pro svou práci jen "
             "to nejmodernější nářadí a přístroje."),
        ],
        "prices": "otevirani-bytu",
        "prose_head": "Výměna zámku není všechno",
        "prose": [
            "Pro mnoho zlodějů je bezpečnostní vložka zámku <strong>výzvou, nikoliv "
            "překážkou</strong>. Vždy proto doporučujeme přemýšlet společně s výměnou vložky "
            "také o bezpečnostním kování, které vložku chrání před vylomením.",
            "Ani bezpečnostní kování s bezpečnostní vložkou neochrání byt či dům před zloději "
            "na 100 %. Můžete proto namontovat i <strong>bezpečnostní závoru</strong>, "
            "která ochrání dveře před vypáčením.",
            "Naši specialisté vám se vším poradí a pomohou tak, aby byl váš objekt co nejlépe "
            "chráněn. Samotná výměna vložky je důležitá, ale existuje i mnoho dalších "
            "možností, jak dům nebo byt zabezpečit lépe.",
        ],
        "faq": [
            ("Jste opravdu nonstop, i o svátcích?",
             "Ano. Dispečink bere telefon 24 hodin denně, 7 dní v týdnu, včetně víkendů "
             "a státních svátků. Mimo pracovní dobu (17:00–7:00), o víkendech a svátcích "
             "se účtuje příplatek."),
            ("Kolik si účtujete za výjezd?",
             "Přepravné je 490 Kč podle vzdálenosti, expresní výjezd 300 Kč. Mimo Prahu "
             "účtujeme +20 Kč za kilometr. Konzultace po telefonu je zdarma."),
            ("Dáváte nějaké slevy?",
             "Ano. Stálí zákazníci mají 50 %, oběti trestných činů 30 %. Slevu poskytujeme "
             "také seniorům a držitelům průkazu OZP."),
            ("Jak daleko jezdíte?",
             "Pokrýváme celou Prahu 1–22 a blízké okolí. Vyjíždíme i dál, doprava mimo "
             "Prahu se pak účtuje +20 Kč za kilometr."),
            ("Jakou máte praxi?",
             "V oboru se pohybujeme 30 let a ročně obsloužíme tisíce zákazníků. Na Google "
             "máme hodnocení 4,9 z 887 recenzí."),
        ],
    },
}
