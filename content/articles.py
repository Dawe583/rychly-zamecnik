# -*- coding: utf-8 -*-
"""
Obsah blogu a právních stránek.

Články jsou převzaté z původního webu rychly-zamecnik.cz, jen upravené
do struktury, kterou umí vysázet generátor. Datum publikace odpovídá
původnímu webu.

Formát bloku:
    ("p",  "odstavec")            běžný text (může obsahovat <strong>, <a>)
    ("h",  "mezinadpis")          h2 v článku
    ("ul", ["položka", ...])      odrážky
    ("ok", ["položka", ...])      odrážky s fajfkou
    ("no", ["položka", ...])      odrážky s křížkem
    ("q",  "citace")              vytažená citace
"""

ARTICLES = {
    # ------------------------------------------------------------------ #
    "nejcastejsi-triky-nepoctivych-zamecniku": {
        "title": "Nepoctiví zámečníci v Praze — triky, ceny a jak nenaletět",
        "meta_title": "Nepoctiví zámečníci v Praze — triky, ceny a jak nenaletět | Rychlý Zámečník",
        "desc": "Pozor na nepoctivé zámečníky v Praze. Odhalte jejich triky, zjistěte "
                "reálné ceny zámečníka a vyberte férového nonstop zámečníka.",
        "date": "2026-02-09",
        "date_h": "9. února 2026",
        "img": "otevirani-zamku",
        "img_alt": "Zámečník pracuje na bezpečnostním zámku",
        "perex": "Zabouchnuté dveře nebo ztracené klíče jsou stres. A přesně na tenhle "
                 "stres bohužel cílí nepoctiví zámečníci. Ukážeme vám nejčastější triky "
                 "a hlavně to, jak poznat férového nonstop zámečníka.",
        "tag": "Rady",
        "body": [
            ("h", "1. Podezřele nízká cena v inzerátu"),
            ("p", "„Otevření dveří od 499 Kč“ zní lákavě. Realita? Na místě se cena "
                  "vyšplhá klidně na <strong>5–10 tisíc Kč</strong>."),
            ("p", "Jak to dělají: nízká cena je jen „za příjezd“ a každá další operace "
                  "se účtuje zvlášť a draze."),
            ("ok", ["Vždy se ptejte na konečnou orientační cenu už po telefonu.",
                    "Seriózní zámečnická pohotovost cenu neskrývá."]),

            ("h", "2. Okamžité vrtání do zámku"),
            ("p", "Poctivý zámečník se vždy snaží o <strong>otevření bez poškození</strong>. "
                  "Nepoctivý často ani nezkusí šetrné metody a rovnou vrtá — což znamená "
                  "drahou výměnu zámku navíc."),
            ("ok", ["Zeptejte se rovnou: „Půjde to otevřít bez poškození?“",
                    "Když slyšíte „to jinak nejde“ hned po příjezdu, zbystřete."]),

            ("h", "3. Tlak na zbytečnou výměnu zámku"),
            ("q", "„Ten zámek je nebezpečný, musíme ho hned vyměnit.“"),
            ("p", "Častý trik hlavně v noci. Ve skutečnosti bývá zámek funkční "
                  "a výměna není nutná."),
            ("ok", ["Chtějte vysvětlení a konkrétní důvod.",
                    "Výměnu máte právo odmítnout."]),

            ("h", "4. Nejasná identita a žádný doklad"),
            ("p", "Typický scénář: žádné IČO, žádná firma, žádný doklad o zaplacení. "
                  "Nemáte se pak kam reklamovat a služba bývá extrémně předražená."),
            ("ok", ["Vybírejte ověřené zámečnictví.",
                    "Doklad o zaplacení je samozřejmost, ne laskavost."]),

            ("h", "5. Falešné „místní firmy“"),
            ("p", "Web tvrdí „Praha 1“, realita je dispečink mimo Prahu, dlouhý dojezd "
                  "a vysoké cestovní poplatky."),
            ("ok", ["Ověřte, jestli má firma reálnou působnost v Praze.",
                    "Čtěte recenze — ne jen pětihvězdičky bez textu."]),

            ("h", "Jak poznat poctivého zámečníka"),
            ("ok", ["Sdělí cenu předem po telefonu.",
                    "Přijede v rozumném čase.",
                    "Snaží se o otevření bez poškození.",
                    "Netlačí na zbytečné opravy.",
                    "Vystaví doklad o zaplacení."]),

            ("h", "Shrnutí"),
            ("no", ["Extrémně levné nabídky jsou riziko, ne výhra."]),
            ("ok", ["Cenu chtějte znát ještě před příjezdem.",
                    "Poctivý nonstop zámečník nemá co skrývat."]),
        ],
    },

    # ------------------------------------------------------------------ #
    "jak-odemknout-zamek-par-rad": {
        "title": "Jak odemknout zámek — praktické rady",
        "meta_title": "Jak odemknout zámek – praktické rady | Rychlý Zámečník",
        "desc": "Nevíte, jak odemknout zámek? Rychlý Zámečník radí, co můžete zkusit "
                "sami a kdy už je lepší zavolat zámečnickou pohotovost.",
        "date": "2026-01-09",
        "date_h": "9. ledna 2026",
        "img": "otevirani-dveri",
        "img_alt": "Ruce odemykající zámek dveří",
        "perex": "Zaseknutý klíč, zabouchnuté dveře nebo zámek, který odmítá spolupracovat. "
                 "Než začnete panikařit nebo zkoušet násilí, projděte si pár rad, jak "
                 "postupovat rozumně a bezpečně.",
        "tag": "Rady",
        "body": [
            ("h", "Rada č. 1: Netlačte na klíč silou"),
            ("p", "Pokud klíč v zámku drhne, netlačte na něj, nezkoušejte ho „lámat“ "
                  "a netočte jím násilím."),
            ("p", "Prasklý klíč v zámku znamená složitější otevírání a často i výměnu "
                  "celého zámku. Někdy pomůže jemné pohnutí klíčem nebo lehké přitlačení "
                  "dveří směrem k zárubni."),

            ("h", "Rada č. 2: Zkontrolujte, jestli nejde jen o zabouchnuté dveře"),
            ("p", "V mnoha případech nejde o zamčený zámek, ale pouze o zabouchnuté dveře. "
                  "To je dobrá zpráva — takové dveře jde často otevřít "
                  "<strong>bez poškození</strong>."),
            ("ok", ["Dveře nejsou zamčené na klíč.",
                    "Klíč není zlomený.",
                    "Zámek není poškozený."]),
            ("p", "Pokud platí všechno výše, je odborné otevření otázkou minut."),

            ("h", "Rada č. 3: Vyhněte se internetovým „zaručeným trikům“"),
            ("p", "Kreditní karta, šroubovák, drát nebo ramínko? Návody vypadají "
                  "jednoduše, ale v praxi končí spíš takhle:"),
            ("no", ["poškozenými dveřmi",
                    "zničeným zámkem",
                    "vyššími náklady na opravu"]),
            ("p", "To, co má vypadat jako rychlé řešení, se často změní v drahý problém."),

            ("h", "Kdy už volat zámečníka"),
            ("ul", ["Klíč nejde otočit.",
                    "Zámek je poškozený.",
                    "Klíč se zlomil.",
                    "Nechcete riskovat škody."]),
            ("p", "V těchhle případech je nejlepší volbou zámečnická pohotovost. Zkušený "
                  "nonstop zámečník zámek otevře šetrně, bez zbytečného poškození "
                  "a s cenou domluvenou dopředu."),
        ],
    },

    # ------------------------------------------------------------------ #
    "nejvtipnejsi-pribeh-nouzoveho-otevreni-auta-v-roce-2025": {
        "title": "Nejvtipnější nouzové otevření auta roku 2025",
        "meta_title": "Nejvtipnější nouzové otevření auta 2025 | Zámečník Praha 1",
        "desc": "Nouzové otevření auta Praha 1 — vtipný příběh z Václavského náměstí. "
                "Rychlý zámečník, otevření auta bez poškození, 24/7.",
        "date": "2025-12-28",
        "date_h": "28. prosince 2025",
        "img": "otevirani-aut",
        "img_alt": "Zámečník otevírá zamčené auto",
        "perex": "Jedna z nejkurióznějších situací roku se odehrála přímo v srdci Prahy "
                 "a ukázala, že nouzové otevření auta může být nejen rychlé, ale i "
                 "nečekaně zábavné.",
        "tag": "Ze života",
        "body": [
            ("h", "Zabouchnuté auto, turista a klobása v ruce"),
            ("p", "Bylo krátce po poledni, Václavák pulzoval životem a mezi turisty, "
                  "tramvajemi a pouličními umělci se objevil on — lehce zmatený zahraniční "
                  "návštěvník. V jedné ruce foťák, v druhé čerstvě zakoupená klobása. "
                  "Klíčky? Ty zůstaly uvnitř auta, které se s typickým „cvak“ právě zamklo."),
            ("p", "Zoufalství vystřídalo rychlé googlení: <strong>zámečník Praha 1 — "
                  "nouzové otevření auta</strong>."),

            ("h", "Zásah na pár minut"),
            ("p", "Zámečník dorazil během několika minut. Bez rozbíjení skla, bez poškození "
                  "zámku, jen se speciálním nářadím a klidem zkušeného odborníka. Když se "
                  "kolem auta začal shromažďovat hlouček lidí, turista nervózně poznamenal:"),
            ("q", "„Jestli to nepůjde, aspoň se rozdělíme o klobásu…“"),
            ("p", "To byla chyba. Smích publika byl tak hlasitý, že jeden z pouličních "
                  "hudebníků spontánně přidal dramatickou melodii. V ten moment zámečník "
                  "auto otevřel — elegantně, rychle a bez jediného škrábance. Potlesk. "
                  "Klobása zachráněna. Klíčky zpět v ruce majitele."),

            ("h", "Proč si ten příběh pamatujeme"),
            ("p", "Protože přesně vystihuje, jak má nouzové otevření auta v Praze vypadat:"),
            ("ok", ["rychlý příjezd, bez čekání",
                    "otevření auta bez poškození",
                    "profesionální a zároveň lidský přístup",
                    "situace vyřešená s úsměvem"]),

            ("h", "Poučení"),
            ("p", "Ať už jste turista nebo místní, zabouchnuté auto si nevybírá. Když se "
                  "to stane, nepropadejte panice, nezkoušejte páčit dveře sami a zavolejte "
                  "zámečníka, který má s nouzovým otevíráním aut zkušenosti."),
        ],
    },

    # ------------------------------------------------------------------ #
    "otevreni-trezoru-stodulky-neuveritelny-pribeh": {
        "title": "Otevření trezoru na Stodůlkách — neuvěřitelný příběh",
        "meta_title": "Otevření trezoru Stodůlky — neuvěřitelný příběh | Rychlý Zámečník",
        "desc": "Neuvěřitelný příběh otevření trezoru na Stodůlkách. Zámečník Praha 13, "
                "rychlý zásah, otevření trezoru bez poškození.",
        "date": "2025-12-29",
        "date_h": "29. prosince 2025",
        "img": "otevirani-trezoru",
        "img_alt": "Zámečník otevírá trezor",
        "perex": "Zapomenutý kód, vybitá baterie a trezor, který se roky neotevřel. "
                 "Zásah na Stodůlkách ukázal, proč se u trezorů vyplatí trpělivost "
                 "místo vrtačky.",
        "tag": "Ze života",
        "body": [
            ("h", "Trezor, který mlčel"),
            ("p", "Klient z Prahy 13 zdědil po rodičích starší trezor. Kód nikdo neznal, "
                  "klíč se za ta léta někam zatoulal a elektronika už dávno nejevila známky "
                  "života. První firma, kterou oslovil, navrhla rovnou navrtání."),

            ("h", "Proč vrtačka nebyla první volba"),
            ("p", "U trezorů platí jednoduché pravidlo: <strong>vrtat se dá vždycky, "
                  "ale zpátky už to nejde</strong>. Navrtaný trezor ztrácí certifikaci "
                  "i pojistnou hodnotu a oprava bývá dražší než samotné otevření."),
            ("ok", ["Nejdřív vyzkoušet nedestruktivní metody.",
                    "Zjistit typ zámku a výrobce.",
                    "Teprve pak zvažovat zásah do pláště."]),

            ("h", "Jak to dopadlo"),
            ("p", "Po výměně baterie v externím napájení a trpělivé práci s mechanikou "
                  "se trezor otevřel bez jediného otvoru. Uvnitř byly doklady, které "
                  "rodina hledala několik měsíců."),
            ("p", "Trezor je dodnes v provozu — jen s novým kódem, který si klient "
                  "tentokrát poznamenal."),

            ("h", "Co si z toho odnést"),
            ("ul", ["Kód k trezoru si uložte mimo trezor. Zní to samozřejmě, "
                    "ale je to nejčastější důvod našich výjezdů.",
                    "Baterie u elektronických zámků měňte preventivně.",
                    "Když někdo navrhne vrtání jako první krok, chtějte vysvětlení."]),
        ],
    },

    # ------------------------------------------------------------------ #
    "jak-otevrit-trezor-kaufland-praha-6": {
        "title": "Jak otevřít trezor — příběh z Kauflandu Praha 6",
        "meta_title": "Jak otevřít trezor — příběh z Kauflandu Praha 6 | Rychlý Zámečník",
        "desc": "Jak otevřít trezor, když selže technika? Příběh z Kauflandu Praha 6. "
                "Nouzové otevření trezoru, profesionální otevírání trezorů.",
        "date": "2025-12-30",
        "date_h": "30. prosince 2025",
        "img": "otevirani-trezoru",
        "img_alt": "Servis a otevírání trezoru",
        "perex": "Ne každý výjezd k trezoru je drama. Někdy je to spíš komedie — "
                 "hlavně když se řeší uprostřed provozu obchodního domu.",
        "tag": "Ze života",
        "body": [
            ("h", "Zavřeno v nejhorší možnou chvíli"),
            ("p", "Podvečer, plný obchod a trezor s denní tržbou, který se odmítl otevřít. "
                  "Elektronický zámek hlásil chybu, personál zkoušel kód pošesté a fronta "
                  "u pokladen mezitím rostla."),

            ("h", "První pravidlo: nezkoušet to donekonečna"),
            ("p", "Většina elektronických trezorových zámků má <strong>ochranu proti "
                  "opakovanému zadání</strong>. Po několika chybných pokusech se zámek "
                  "zablokuje na několik minut — a s každým dalším pokusem se prodleva "
                  "prodlužuje."),
            ("no", ["Zkoušet kód pořád dokola situaci jen zhorší."]),
            ("ok", ["Přestat, počkat a zavolat někoho, kdo trezor otevře odborně."]),

            ("h", "Jak zásah probíhal"),
            ("p", "Ukázalo se, že problém nebyl v kódu, ale ve vybité baterii — zámek měl "
                  "dost energie na rozsvícení displeje, ale ne na odjištění závory. "
                  "Externí napájení a trezor byl během chvíle otevřený."),

            ("h", "Co dělat, když se trezor nechce otevřít"),
            ("ul", ["Zkuste vyměnit baterie — je to nejčastější příčina.",
                    "Nezadávejte kód opakovaně, riskujete zablokování.",
                    "Nezkoušejte páčit ani vrtat, přijdete o certifikaci trezoru.",
                    "Zavolejte zámečníka se zkušeností s trezory."]),
        ],
    },
}


LEGAL = {
    "zasady-ochrany-osobnich-udaju": {
        "title": "Zásady ochrany osobních údajů",
        "meta_title": "Zásady ochrany osobních údajů | Rychlý Zámečník",
        "desc": "Jak nakládáme s osobními údaji a soubory cookie na webu "
                "rychly-zamecnik.cz.",
        "intro": "Tyhle zásady popisují, jaké údaje o vás zpracováváme, proč to děláme "
                 "a jaká práva vůči nám máte.",
        "body": [
            ("h", "Kdo je správce"),
            ("p", "Správcem osobních údajů je <strong>Rychlý Zámečník</strong>, "
                  "IČO 075 25 711, e-mail "
                  "<a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>, "
                  "telefon <a href=\"tel:+420723965990\">723 965 990</a>."),

            ("h", "Jaké údaje zpracováváme"),
            ("ul", ["<strong>Údaje z objednávky zásahu</strong> — jméno, telefon, adresa "
                    "místa zásahu. Bez nich k vám nemůžeme přijet.",
                    "<strong>Údaje z e-mailové komunikace</strong> — pokud nám napíšete, "
                    "zpracováváme obsah zprávy a vaši e-mailovou adresu.",
                    "<strong>Technické údaje</strong> — pokud udělíte souhlas, sbíráme "
                    "anonymizované statistiky návštěvnosti."]),

            ("h", "Proč je zpracováváme"),
            ("ul", ["Abychom mohli provést objednanou službu (plnění smlouvy).",
                    "Abychom splnili zákonné povinnosti — hlavně vystavení "
                    "a archivaci daňových dokladů.",
                    "Abychom web zlepšovali (jen na základě vašeho souhlasu)."]),

            ("h", "Jak dlouho je uchováváme"),
            ("p", "Údaje z objednávky uchováváme po dobu nutnou k vyřízení zakázky "
                  "a následně po zákonnou dobu pro archivaci daňových dokladů. "
                  "Statistiky návštěvnosti se uchovávají nejvýše 14 měsíců."),

            ("h", "Komu je předáváme"),
            ("p", "Osobní údaje nepředáváme třetím stranám s výjimkou případů, kdy to "
                  "ukládá zákon, nebo kdy je to nutné pro vyřízení zakázky — například "
                  "pojišťovně, pokud zásah hradí z pojištění domácnosti."),

            ("h", "Soubory cookie"),
            ("p", "Web ve výchozím stavu používá pouze <strong>nezbytné cookies</strong>, "
                  "bez kterých by nefungoval. Ty nevyžadují souhlas. Analytické cookies "
                  "nasazujeme až poté, co nám k tomu dáte souhlas v cookie liště."),
            ("p", "Souhlas můžete kdykoliv odvolat — v patičce webu je odkaz "
                  "<strong>Nastavení cookies</strong>, který lištu otevře znovu "
                  "a volbu přepíše."),

            ("h", "Vaše práva"),
            ("ul", ["Právo na přístup ke svým údajům.",
                    "Právo na opravu nepřesných údajů.",
                    "Právo na výmaz, pokud pro zpracování není zákonný důvod.",
                    "Právo na omezení zpracování a právo vznést námitku.",
                    "Právo na přenositelnost údajů.",
                    "Právo podat stížnost u Úřadu pro ochranu osobních údajů."]),
            ("p", "Uplatnit je můžete e-mailem na "
                  "<a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>."),
        ],
        "note": "Tento dokument je připravený jako podklad. Před spuštěním webu ho nechte "
                "zkontrolovat někým, kdo za jeho znění může nést odpovědnost.",
    },

    "obchodni-podminky": {
        "title": "Obchodní podmínky",
        "meta_title": "Obchodní podmínky | Rychlý Zámečník",
        "desc": "Podmínky poskytování zámečnických služeb — jak vzniká objednávka, "
                "jak se určuje cena, záruka, reklamace a odstoupení od smlouvy.",
        "intro": "Aby bylo předem jasné, na čem jsme. Co si domluvíme po telefonu, "
                 "to platí — tenhle dokument to jen sepisuje.",
        "body": [
            ("h", "Kdo služby poskytuje"),
            ("p", "Služby poskytuje <strong>Rychlý Zámečník</strong>, IČO 075 25 711, "
                  "e-mail <a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>, "
                  "telefon <a href=\"tel:+420723965990\">723 965 990</a> "
                  "(dále „<strong>zhotovitel</strong>“)."),

            ("h", "Čeho se podmínky týkají"),
            ("p", "Vztahují se na zámečnické práce prováděné na místě u zákazníka — "
                  "nouzové otevírání dveří, aut a trezorů, výměnu a opravu zámků "
                  "a vložek, opravy dveří a zabezpečení."),

            ("h", "Jak vzniká objednávka"),
            ("p", "Objednávka vzniká telefonicky nebo e-mailem. Zhotovitel před výjezdem "
                  "sdělí <strong>orientační cenu</strong> a přibližnou dobu příjezdu. "
                  "Smlouva je uzavřena okamžikem, kdy zákazník výjezd potvrdí."),
            ("p", "Ceny uvedené na webu jsou orientační, ve formátu „od“. Konečná cena "
                  "závisí na typu zámku, rozsahu poškození a použitém materiálu."),

            ("h", "Cena a její potvrzení"),
            ("ok", ["Technik na místě posoudí rozsah práce a sdělí <strong>konečnou cenu "
                    "ještě před zahájením prací</strong>.",
                    "Teprve po odsouhlasení ceny zákazníkem se začíná pracovat.",
                    "Pokud se během práce ukáže, že je potřeba udělat víc, technik "
                    "práci přeruší a domluví se na ceně znovu."]),
            ("p", "Zákazník není povinen práci objednat, pokud mu sdělená cena nevyhovuje. "
                  "V takovém případě hradí pouze cestovné podle ceníku."),

            ("h", "Cestovné a příplatky"),
            ("p", "K ceně práce se připočítává cestovné podle ceníku. Příplatky za noční "
                  "hodiny, víkendy a svátky jsou uvedené v ceníku a technik na ně upozorní "
                  "při potvrzení ceny. Slevy pro seniory a držitele průkazu ZTP se "
                  "uplatňují po předložení dokladu."),

            ("h", "Prokázání oprávněnosti zásahu"),
            ("p", "Před otevřením dveří, vozidla nebo trezoru je zákazník povinen "
                  "<strong>prokázat, že je k zásahu oprávněn</strong> — dokladem "
                  "totožnosti s adresou, nájemní smlouvou, velkým technickým průkazem "
                  "nebo jiným věrohodným způsobem."),
            ("p", "Bez tohoto doložení technik zásah neprovede. Není to formalita — "
                  "chrání to majitele i zhotovitele. Cestovné se v takovém případě hradí."),

            ("h", "Platba"),
            ("p", "Platí se po dokončení práce, v hotovosti nebo převodem. Ke každé "
                  "zakázce zhotovitel vystaví doklad. Na požádání vystaví fakturu "
                  "na firmu nebo podklad pro pojišťovnu."),

            ("h", "Záruka"),
            ("p", "Na provedenou práci i dodaný materiál poskytuje zhotovitel záruku "
                  "<strong>24 měsíců</strong> ode dne předání. Záruka se nevztahuje na "
                  "vady způsobené běžným opotřebením, násilným poškozením, neodbornými "
                  "zásahy třetí osoby nebo nevhodným užíváním."),

            ("h", "Reklamace"),
            ("p", "Reklamaci uplatněte telefonicky nebo e-mailem, ideálně s popisem vady "
                  "a fotografií. Zhotovitel ji vyřídí <strong>nejpozději do 30 dnů</strong> "
                  "od uplatnění, pokud se se zákazníkem nedohodne na delší lhůtě."),
            ("p", "Je-li reklamace oprávněná, zhotovitel vadu bezplatně odstraní. Není-li "
                  "to možné, poskytne přiměřenou slevu nebo vrátí zaplacenou částku."),

            ("h", "Odstoupení od smlouvy"),
            ("p", "Spotřebitel má u smluv uzavřených na dálku nebo mimo obchodní prostory "
                  "právo odstoupit do 14 dnů. U <strong>neodkladné opravy, o kterou sám "
                  "výslovně požádal</strong>, toto právo podle občanského zákoníku zaniká "
                  "provedením služby — což je u nouzového otevírání typický případ."),
            ("p", "Objednávku lze bezplatně zrušit, dokud technik nevyjel. Pokud už je "
                  "na cestě, hradí se cestovné."),

            ("h", "Odpovědnost za škodu"),
            ("p", "Zhotovitel odpovídá za škodu, kterou při provádění prací prokazatelně "
                  "způsobil. U nouzového otevírání může být <strong>poškození zámku "
                  "nevyhnutelné</strong> — technik na to upozorní předem a domluví se "
                  "na postupu i na ceně případné výměny."),

            ("h", "Řešení sporů"),
            ("p", "Spory se řeší především dohodou. Spotřebitel má právo na mimosoudní "
                  "řešení sporu u <strong>České obchodní inspekce</strong> "
                  "(<a href=\"https://adr.coi.cz\" rel=\"noopener\">adr.coi.cz</a>)."),

            ("h", "Účinnost"),
            ("p", "Podmínky jsou účinné od 1. 1. 2026. Pro už uzavřené objednávky platí "
                  "znění účinné v době objednávky."),
        ],
        "note": "Tento dokument je připravený jako podklad, ne jako hotový právní text. "
                "Než ho web začne používat, nechte ho zkontrolovat někým, kdo za jeho "
                "znění může nést odpovědnost — hlavně lhůty, záruku a odstoupení.",
    },
}
