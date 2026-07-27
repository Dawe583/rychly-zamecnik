# -*- coding: utf-8 -*-
"""
Jazykové mutace — angličtina, ruština, ukrajinština.

Původní web měl mutace přes TranslatePress na /en/, /ru/ a /ua/. Zachováváme
stejné prefixy i stejné slugy podstránek, aby zůstaly funkční adresy, které
už jsou zaindexované.

Ceny se nepřekládají — čísla jsou stejná ve všech jazycích, mění se jen
popisky položek (viz CENIK_I18N).
"""

LANGS = {
    "en": {"name": "English", "short": "EN", "locale": "en_GB", "hreflang": "en"},
    "ru": {"name": "Русский", "short": "RU", "locale": "ru_RU", "hreflang": "ru"},
    "ua": {"name": "Українська", "short": "UA", "locale": "uk_UA", "hreflang": "uk"},
}

# --------------------------------------------------------------------------- #
# Rozhraní — navigace, tlačítka, patička
# --------------------------------------------------------------------------- #
UI = {
    "en": {
        "nav_services": "Services", "nav_why": "Why us", "nav_how": "How it works",
        "nav_prices": "Prices", "nav_area": "Coverage", "nav_reviews": "Reviews",
        "nav_blog": "Blog",
        "nonstop": "24/7 non-stop", "call_now": "Call now", "call": "Call",
        "show_prices": "See prices", "service_prices": "Service prices",
        "write_email": "Send an email", "home": "Home",
        "dispatch_live": "Our dispatcher is on the line right now",
        "footer_services": "Services", "footer_info": "Information", "footer_contact": "Contact",
        "footer_tagline": "Locksmith emergency service for Prague and the surrounding area. "
                          "Non-stop 24/7, 30 years of experience, two-year warranty on labour "
                          "and materials.",
        "footer_rights": "Locksmith Emergency Service Prague",
        "footer_note": "Prices shown on this site are indicative, starting from.",
        "privacy": "Privacy policy", "area": "Prague and surroundings",
        "cookie_settings": "Cookie settings",
        "terms": "Terms of service",
        "price_note": "Prices are indicative, starting from. We confirm the exact amount by "
                      "phone or on site <strong>before we start work</strong>. Seniors and "
                      "disability card holders are entitled to a discount.",
        "full_pricelist": "See the full price list",
        "more_services": "More services", "more_head": "What else we do",
        "faq_eyebrow": "FAQ", "faq_head": "The questions we get most",
        "faq_lead": "Didn't find your answer? Give us a ring — phone advice is free.",
        "why_eyebrow": "Why us", "prices_eyebrow": "Prices",
        "good_to_know": "Good to know",
        "cta_head": "Need help right now?",
        "cta_text": "Call us. Advice is free, we quote the price up front and a technician "
                    "sets off immediately — any day, any hour.",
        "cookie_head": "Cookies",
        "cookie_text": "This site uses only the cookies it needs to run. We collect statistics "
                       "only once you agree. More in our",
        "cookie_link": "privacy policy",
        "cookie_all": "Accept all", "cookie_min": "Necessary only",
        "lang_label": "Language",
    },
    "ru": {
        "nav_services": "Услуги", "nav_why": "Почему мы", "nav_how": "Как это происходит",
        "nav_prices": "Цены", "nav_area": "Где работаем", "nav_reviews": "Отзывы",
        "nav_blog": "Блог",
        "nonstop": "Круглосуточно 24/7", "call_now": "Позвонить", "call": "Звонок",
        "show_prices": "Посмотреть цены", "service_prices": "Цены на услугу",
        "write_email": "Написать письмо", "home": "Главная",
        "dispatch_live": "Диспетчер на линии прямо сейчас",
        "footer_services": "Услуги", "footer_info": "Информация", "footer_contact": "Контакты",
        "footer_tagline": "Аварийная служба слесаря для Праги и окрестностей. Круглосуточно "
                          "24/7, 30 лет опыта, два года гарантии на работу и материалы.",
        "footer_rights": "Аварийная служба слесаря, Прага",
        "footer_note": "Цены на сайте ориентировочные, «от».",
        "privacy": "Политика конфиденциальности", "area": "Прага и окрестности",
        "cookie_settings": "Настройки cookie",
        "terms": "Условия оказания услуг",
        "price_note": "Цены ориентировочные, «от». Точную сумму подтвердим по телефону или "
                      "на месте <strong>до начала работ</strong>. Пенсионеры и люди "
                      "с инвалидностью получают скидку.",
        "full_pricelist": "Смотреть полный прайс-лист",
        "more_services": "Другие услуги", "more_head": "Что мы ещё умеем",
        "faq_eyebrow": "Частые вопросы", "faq_head": "О чём спрашивают чаще всего",
        "faq_lead": "Не нашли ответ? Позвоните — консультация по телефону бесплатная.",
        "why_eyebrow": "Почему мы", "prices_eyebrow": "Цены",
        "good_to_know": "Полезно знать",
        "cta_head": "Нужна помощь прямо сейчас?",
        "cta_text": "Позвоните нам. Консультация бесплатна, цену называем заранее, "
                    "и мастер выезжает сразу — в любой день и в любое время.",
        "cookie_head": "Файлы cookie",
        "cookie_text": "Сайт использует только необходимые для работы файлы cookie. "
                       "Статистику собираем лишь с вашего согласия. Подробнее в",
        "cookie_link": "политике конфиденциальности",
        "cookie_all": "Принять всё", "cookie_min": "Только необходимые",
        "lang_label": "Язык",
    },
    "ua": {
        "nav_services": "Послуги", "nav_why": "Чому ми", "nav_how": "Як це відбувається",
        "nav_prices": "Ціни", "nav_area": "Де працюємо", "nav_reviews": "Відгуки",
        "nav_blog": "Блог",
        "nonstop": "Цілодобово 24/7", "call_now": "Зателефонувати", "call": "Дзвінок",
        "show_prices": "Переглянути ціни", "service_prices": "Ціни на послугу",
        "write_email": "Написати листа", "home": "Головна",
        "dispatch_live": "Диспетчер на лінії просто зараз",
        "footer_services": "Послуги", "footer_info": "Інформація", "footer_contact": "Контакти",
        "footer_tagline": "Аварійна слюсарна служба для Праги та околиць. Цілодобово 24/7, "
                          "30 років досвіду, два роки гарантії на роботу та матеріали.",
        "footer_rights": "Аварійна слюсарна служба, Прага",
        "footer_note": "Ціни на сайті орієнтовні, «від».",
        "privacy": "Політика конфіденційності", "area": "Прага та околиці",
        "cookie_settings": "Налаштування cookie",
        "terms": "Умови надання послуг",
        "price_note": "Ціни орієнтовні, «від». Точну суму підтвердимо телефоном або на місці "
                      "<strong>до початку робіт</strong>. Пенсіонери та люди з інвалідністю "
                      "мають право на знижку.",
        "full_pricelist": "Дивитися повний прайс-лист",
        "more_services": "Інші послуги", "more_head": "Що ми ще вміємо",
        "faq_eyebrow": "Часті запитання", "faq_head": "Про що питають найчастіше",
        "faq_lead": "Не знайшли відповіді? Зателефонуйте — консультація безкоштовна.",
        "why_eyebrow": "Чому ми", "prices_eyebrow": "Ціни",
        "good_to_know": "Корисно знати",
        "cta_head": "Потрібна допомога просто зараз?",
        "cta_text": "Зателефонуйте нам. Консультація безкоштовна, ціну називаємо наперед, "
                    "і майстер виїжджає одразу — будь-якого дня й будь-якої години.",
        "cookie_head": "Файли cookie",
        "cookie_text": "Сайт використовує лише необхідні для роботи файли cookie. "
                       "Статистику збираємо тільки за вашою згодою. Докладніше в",
        "cookie_link": "політиці конфіденційності",
        "cookie_all": "Прийняти все", "cookie_min": "Лише необхідні",
        "lang_label": "Мова",
    },
}


# --------------------------------------------------------------------------- #
# Ceníkové položky
# --------------------------------------------------------------------------- #
CENIK_I18N = {
    "en": {
        "otevirani-bytu": [
            ("Slammed door / no security fittings", "from 290 CZK"),
            ("Slammed door / with security fittings", "from 490 CZK"),
            ("Slammed / high-security", "from 790 CZK"),
            ("Slammed / multi-point lock", "from 990 CZK"),
            ("Locked / standard, no security fittings", "from 390 CZK"),
            ("Locked / with security fittings", "from 890 CZK"),
            ("Locked / R1, R3, OS1 fittings", "from 990 CZK"),
            ("Locked / additional lock", "from 890 CZK"),
            ("Locked / jammed safe lock", "from 1,190 CZK"),
            ("Locked / broken latch", "from 790 CZK"),
            ("Locked / lever lock", "from 790 CZK"),
            ("Locked / mailbox, desk or furniture lock", "from 590 CZK"),
            ("Locked / safe lock", "from 1,990 CZK"),
            ("Safe opening, repair and servicing", "by type"),
        ],
        "zamky": [
            ("Lock replacement / plain door, no fittings", "from 290 CZK"),
            ("Security lock cylinder replacement", "from 390 CZK"),
            ("Cylinder replacement / multi-bolt locks", "from 790 CZK"),
            ("Lock replacement CR, Mottura, CISA", "from 1,090 CZK"),
            ("Repair / jammed latch or bolt", "from 1,090 CZK"),
            ("Installation / smart locks", "from 990 CZK"),
            ("Installation of R1, Richter fittings", "from 890 CZK"),
            ("Mortise lock installation", "from 690 CZK"),
            ("Electromechanical lock installation", "from 1,090 CZK"),
            ("Broken key extraction", "from 490 CZK"),
            ("Cylinder removal without a key", "from 590 CZK"),
            ("Security bar installation", "from 1,490 CZK"),
            ("Additional lock installation", "from 990 CZK"),
            ("Door repair", "from 390 CZK"),
        ],
        "auta": [
            ("Car up to model year 2002 (no safe lock)", "from 590 CZK"),
            ("Car model year 2002–2007 (no safe lock)", "from 990 CZK"),
            ("Car from model year 2007 (no safe lock)", "from 1,290 CZK"),
            ("Safe-type security up to model year 2007", "from 1,490 CZK"),
            ("Safe-type security, model years 2008–2018", "from 1,690 CZK"),
            ("Lock replacement", "from 990 CZK"),
            ("Ignition switch replacement", "from 1,990 CZK"),
            ("Gear lock removal (DEFEND LOCK etc.)", "from 2,490 CZK"),
        ],
    },
    "ru": {
        "otevirani-bytu": [
            ("Захлопнулась дверь / без защитной фурнитуры", "от 290 крон"),
            ("Захлопнулась дверь / с защитной фурнитурой", "от 490 крон"),
            ("Захлопнулась / повышенной безопасности", "от 790 крон"),
            ("Захлопнулась / многозапорный замок", "от 990 крон"),
            ("Заперто / обычный, без защиты", "от 390 крон"),
            ("Заперто / с защитной фурнитурой", "от 890 крон"),
            ("Заперто / фурнитура R1, R3, OS1", "от 990 крон"),
            ("Заперто / дополнительный замок", "от 890 крон"),
            ("Заперто / заклинивший сейфовый замок", "от 1 190 крон"),
            ("Заперто / сломана защёлка", "от 790 крон"),
            ("Заперто / сувальдный замок", "от 790 крон"),
            ("Заперто / почтовый, столовый, мебельный замок", "от 590 крон"),
            ("Заперто / сейфовый замок", "от 1 990 крон"),
            ("Вскрытие, ремонт и обслуживание сейфа", "по типу"),
        ],
        "zamky": [
            ("Замена замка / обычная дверь без фурнитуры", "от 290 крон"),
            ("Замена цилиндра защитного замка", "от 390 крон"),
            ("Замена цилиндра / многозапорные замки", "от 790 крон"),
            ("Замена замка CR, Mottura, CISA", "от 1 090 крон"),
            ("Ремонт / заклинившая защёлка или ригель", "от 1 090 крон"),
            ("Установка / умные замки", "от 990 крон"),
            ("Установка фурнитуры R1, Richter и др.", "от 890 крон"),
            ("Установка врезного замка", "от 690 крон"),
            ("Установка электромеханического замка", "от 1 090 крон"),
            ("Извлечение сломанного ключа", "от 490 крон"),
            ("Демонтаж цилиндра без ключа", "от 590 крон"),
            ("Установка защитного засова", "от 1 490 крон"),
            ("Установка дополнительного замка", "от 990 крон"),
            ("Ремонт двери", "от 390 крон"),
        ],
        "auta": [
            ("Автомобиль до 2002 года (без сейфового замка)", "от 590 крон"),
            ("Автомобиль 2002–2007 (без сейфового замка)", "от 990 крон"),
            ("Автомобиль от 2007 года (без сейфового замка)", "от 1 290 крон"),
            ("Сейфовый тип защиты до 2007 года", "от 1 490 крон"),
            ("Сейфовый тип защиты 2008–2018", "от 1 690 крон"),
            ("Замена замков", "от 990 крон"),
            ("Замена замка зажигания", "от 1 990 крон"),
            ("Демонтаж замка КПП (DEFEND LOCK и др.)", "от 2 490 крон"),
        ],
    },
    "ua": {
        "otevirani-bytu": [
            ("Захряснули двері / без захисної фурнітури", "від 290 крон"),
            ("Захряснули двері / із захисною фурнітурою", "від 490 крон"),
            ("Захряснули / підвищеної безпеки", "від 790 крон"),
            ("Захряснули / багатозапорний замок", "від 990 крон"),
            ("Замкнено / звичайний, без захисту", "від 390 крон"),
            ("Замкнено / із захисною фурнітурою", "від 890 крон"),
            ("Замкнено / фурнітура R1, R3, OS1", "від 990 крон"),
            ("Замкнено / додатковий замок", "від 890 крон"),
            ("Замкнено / заклинив сейфовий замок", "від 1 190 крон"),
            ("Замкнено / зламана засувка", "від 790 крон"),
            ("Замкнено / сувальдний замок", "від 790 крон"),
            ("Замкнено / поштовий, столовий, меблевий замок", "від 590 крон"),
            ("Замкнено / сейфовий замок", "від 1 990 крон"),
            ("Відкриття, ремонт і обслуговування сейфа", "за типом"),
        ],
        "zamky": [
            ("Заміна замка / звичайні двері без фурнітури", "від 290 крон"),
            ("Заміна циліндра захисного замка", "від 390 крон"),
            ("Заміна циліндра / багатозапорні замки", "від 790 крон"),
            ("Заміна замка CR, Mottura, CISA", "від 1 090 крон"),
            ("Ремонт / заклинила засувка або ригель", "від 1 090 крон"),
            ("Встановлення / розумні замки", "від 990 крон"),
            ("Встановлення фурнітури R1, Richter тощо", "від 890 крон"),
            ("Встановлення врізного замка", "від 690 крон"),
            ("Встановлення електромеханічного замка", "від 1 090 крон"),
            ("Виймання зламаного ключа", "від 490 крон"),
            ("Демонтаж циліндра без ключа", "від 590 крон"),
            ("Встановлення захисного засува", "від 1 490 крон"),
            ("Встановлення додаткового замка", "від 990 крон"),
            ("Ремонт дверей", "від 390 крон"),
        ],
        "auta": [
            ("Автомобіль до 2002 року (без сейфового замка)", "від 590 крон"),
            ("Автомобіль 2002–2007 (без сейфового замка)", "від 990 крон"),
            ("Автомобіль від 2007 року (без сейфового замка)", "від 1 290 крон"),
            ("Сейфовий тип захисту до 2007 року", "від 1 490 крон"),
            ("Сейфовий тип захисту 2008–2018", "від 1 690 крон"),
            ("Заміна замків", "від 990 крон"),
            ("Заміна замка запалювання", "від 1 990 крон"),
            ("Демонтаж замка КПП (DEFEND LOCK тощо)", "від 2 490 крон"),
        ],
    },
}


# --------------------------------------------------------------------------- #
# Domovská stránka
# --------------------------------------------------------------------------- #
HOME = {
    "en": {
        "title": "Locksmith Prague — 24/7 emergency locksmith service",
        "desc": "Emergency locksmith in Prague, non-stop. Opening slammed doors, lock "
                "replacement, car and safe opening. On site within 30 minutes. "
                "4.8★ from 887 reviews.",
        "badge": "Open right now — non-stop, holidays included",
        "h1_a": "Locked out?", "h1_b": "We're with you in", "h1_em": "30 minutes",
        "sub": "Emergency locksmith service for Prague and the surrounding area. We open "
               "doors, cars and safes — fast, without a single scratch, at the lowest "
               "prices in Prague.",
        "chips": ["<b>4.8</b> from 887 reviews", "Non-stop <b>24 / 7</b>",
                  "On site <b>within 30 minutes</b>", "<b>2-year</b> warranty on labour",
                  "<b>50 %</b> off for regulars"],
        "ticker": ["Opening slammed doors", "Lock and cylinder replacement",
                   "Car opening without damage", "Safe opening and servicing",
                   "Door repair after a break-in", "Broken key extraction",
                   "Security bar installation", "Smart locks"],
        "stats": ["years of experience", "customer reviews",
                  "average Google rating", "emergency cover, no breaks"],
        "svc_eyebrow": "Our services",
        "svc_head": "There isn't a lock in Prague we can't handle",
        "svc_lead": "From slammed doors to safes and car ignition locks. We use only the "
                    "most modern tools — opening without damage, guaranteed.",
        "svc": [
            ("Door opening", "We open your door without a single scratch. Slammed or locked, "
             "with security fittings or a multi-point lock.", "from 290 CZK"),
            ("Lock replacement", "We fit and replace any locks and cylinders — every brand, "
             "type and security class, from standard to the very highest.", "from 290 CZK"),
            ("Car opening", "Masters of car locks. We guarantee opening without a scratch and "
             "without damage to the lock or bodywork.", "from 590 CZK"),
            ("Safe opening", "Forgotten the code or combination? Broken key or failed "
             "mechanism? Our locksmiths will handle it.", "from 1,190 CZK"),
            ("Repair after a break-in", "Break-ins happen in Prague. You need your peace of "
             "mind back as fast as possible — we're ready non-stop.", "from 390 CZK"),
            ("Emergency service", "Call any time — midnight, weekend or public holiday. "
             "Phone advice is free.", "call-out 300 CZK"),
        ],
        "why_head": "Six reasons people call us again",
        "why_lead": "Our goal is work done well and a satisfied customer — and our clients' "
                    "ratings speak for themselves.",
        "why": [
            ("Fair prices", "We keep prices low so clients stay happy. Seniors, disability "
             "card holders, regulars and crime victims are entitled to a discount."),
            ("Fast help", "We guarantee a fast arrival and high-quality work. We always give "
             "a two-year warranty on labour and materials."),
            ("Non-stop cover", "Your Prague locksmith is available round the clock. "
             "Professional, fast service in Prague and the surrounding area, 24/7."),
            ("Great ratings", "Our clients' ratings say it clearly — we're on the right track "
             "and still improving. 4.8 stars from 887 Google reviews."),
            ("Trained team", "Our locksmiths are trained professionals with many years of "
             "experience. The job gets done fast, well and without mistakes."),
            ("30 years of experience", "Long experience means work done properly. We serve "
             "thousands of customers across Prague every year."),
        ],
        "how_eyebrow": "How it works", "how_head": "Three steps and you're back inside",
        "how_lead": "No forms, no waiting for an email. One phone call is enough — "
                    "and the advice is free.",
        "steps": [
            ("Step 01", "You call", "We answer round the clock. Describe the situation and "
             "we'll estimate the price and arrival time straight away. Advice is free."),
            ("Step 02", "We set off", "A technician is on the way as fast as possible — "
             "typically within 20–30 minutes anywhere in Prague."),
            ("Step 03", "We open and repair", "We open without damage and confirm the price "
             "before starting. Two-year warranty on labour and materials."),
        ],
        "price_head": "We guarantee the lowest prices in Prague",
        "price_lead": "The price always depends on how complex the job is and can be agreed "
                      "individually — on site with the technician or by phone with the dispatcher.",
        "tabs": ["Homes and flats", "Lock repair and fitting", "Car opening", "Travel and discounts"],
        "extra": [
            ("Travel charge (by distance)", "490 CZK"),
            ("Travel outside Prague", "+20 CZK / km"),
            ("Express call-out, emergency", "300 CZK"),
            ("Discount for regular customers", "−50 %"),
            ("Discount for crime victims (break-ins etc.)", "−30 %"),
            ("Out-of-hours (17:00–07:00), weekends, holidays", "+100 %"),
            ("Consumables (drill bits, cutters, discs)", "as used"),
        ],
        "area_eyebrow": "Coverage", "area_head": "All of Prague 1–22 and nearby areas",
        "area_lead": "Our vans are spread across Prague, so the nearest technician comes to "
                     "you. We also travel outside Prague — that's +20 CZK per kilometre.",
        "area_btn": "Check availability by phone", "area_more": "+ surroundings",
        "rev_eyebrow": "Reviews", "rev_head": "What our customers say",
        "rev_lead": "Real Google ratings. We publish the critical ones too — that's how "
                    "we improve.",
        "rev_sum": "Overall rating based on <strong>887 reviews</strong>",
        "cta_head": "Standing outside and can't get in?",
        "cta_text": "Call us. Advice is free, we quote the price up front and a technician "
                    "sets off immediately — any day, any hour.",
    },
    "ru": {
        "title": "Слесарь Прага — аварийное вскрытие замков круглосуточно",
        "desc": "Аварийная служба слесаря в Праге, круглосуточно. Вскрытие захлопнувшихся "
                "дверей, замена замков, вскрытие авто и сейфов. Приезд за 30 минут. "
                "4,8★ из 887 отзывов.",
        "badge": "Работаем прямо сейчас — круглосуточно, и в праздники",
        "h1_a": "Захлопнулась дверь?", "h1_b": "Приедем за", "h1_em": "30 минут",
        "sub": "Аварийная служба слесаря для Праги и окрестностей. Откроем дверь, "
               "автомобиль и сейф — быстро, без единой царапины и по самым низким "
               "ценам в Праге.",
        "chips": ["<b>4,8</b> из 887 отзывов", "Круглосуточно <b>24 / 7</b>",
                  "Приезд <b>за 30 минут</b>", "<b>2 года</b> гарантии на работу",
                  "Скидка <b>50 %</b> постоянным клиентам"],
        "ticker": ["Вскрытие захлопнувшихся дверей", "Замена замков и цилиндров",
                   "Вскрытие авто без повреждений", "Вскрытие и сервис сейфов",
                   "Ремонт двери после взлома", "Извлечение сломанного ключа",
                   "Установка защитных засовов", "Умные замки"],
        "stats": ["лет опыта в отрасли", "оценок от клиентов",
                  "средняя оценка в Google", "работаем без перерыва"],
        "svc_eyebrow": "Наши услуги",
        "svc_head": "В Праге нет замка, с которым мы бы не справились",
        "svc_lead": "От захлопнувшихся дверей до сейфов и замков зажигания. Работаем только "
                    "самым современным инструментом — вскрытие без повреждений гарантируем.",
        "svc": [
            ("Вскрытие дверей", "Откроем дверь без единой царапины. Захлопнувшиеся и запертые, "
             "с защитной фурнитурой и многозапорным замком.", "от 290 крон"),
            ("Замена замков", "Устанавливаем и меняем любые замки и цилиндры — всех марок, "
             "типов и классов защиты, от стандартных до самых высоких.", "от 290 крон"),
            ("Вскрытие авто", "Мастера автомобильных замков. Гарантируем вскрытие без "
             "царапин и без повреждения замка или кузова.", "от 590 крон"),
            ("Вскрытие сейфов", "Забыли код или комбинацию? Сломался ключ или отказала "
             "механика? Наши слесари справятся.", "от 1 190 крон"),
            ("Ремонт после взлома", "Взломы в Праге случаются. Спокойствие нужно вернуть "
             "как можно быстрее — мы готовы круглосуточно.", "от 390 крон"),
            ("Аварийная служба", "Звоните в любое время — хоть в полночь, в выходной или "
             "в праздник. Консультация по телефону бесплатна.", "выезд 300 крон"),
        ],
        "why_head": "Шесть причин, почему нам звонят снова",
        "why_lead": "Наша цель — качественно выполненная работа и довольный клиент. "
                    "Оценки клиентов говорят сами за себя.",
        "why": [
            ("Доступные цены", "Держим цены низкими, чтобы клиенты оставались довольны. "
             "Пенсионеры, люди с инвалидностью, постоянные клиенты и жертвы преступлений "
             "получают скидку."),
            ("Быстрая помощь", "Гарантируем быстрый приезд и высокое качество работы. "
             "На работу и материалы всегда даём два года гарантии."),
            ("Круглосуточно", "Слесарь в Праге доступен вам круглосуточно. Профессиональные "
             "и быстрые услуги в Праге и окрестностях 24/7."),
            ("Высокие оценки", "Оценки клиентов говорят ясно — мы на верном пути и постоянно "
             "совершенствуемся. 4,8 звезды из 887 отзывов в Google."),
            ("Обученная команда", "Наши слесари — обученные профессионалы с многолетним "
             "опытом. Работу выполним быстро, качественно и без ошибок."),
            ("30 лет опыта", "Благодаря большому опыту работаем качественно. Ежегодно "
             "обслуживаем тысячи клиентов по всей Праге."),
        ],
        "how_eyebrow": "Как это происходит", "how_head": "Три шага — и вы дома",
        "how_lead": "Никаких форм и ожидания письма. Достаточно одного звонка — "
                    "консультация бесплатна.",
        "steps": [
            ("Шаг 01", "Вы звоните", "Отвечаем круглосуточно. Опишите ситуацию — сразу по "
             "телефону оценим цену и время приезда. Консультация бесплатна."),
            ("Шаг 02", "Мы выезжаем", "Мастер в пути в кратчайшее время — по Праге обычно "
             "за 20–30 минут после звонка."),
            ("Шаг 03", "Открываем и чиним", "Открываем без повреждений, цену подтверждаем "
             "до начала работ. На работу и материалы два года гарантии."),
        ],
        "price_head": "Гарантируем самые низкие цены в Праге",
        "price_lead": "Цена всегда зависит от сложности работы и обсуждается индивидуально — "
                      "на месте с мастером или по телефону с диспетчером.",
        "tabs": ["Квартиры и дома", "Ремонт и установка замков", "Вскрытие авто", "Выезд и скидки"],
        "extra": [
            ("Транспортные расходы (по расстоянию)", "490 крон"),
            ("Выезд за пределы Праги", "+20 крон / км"),
            ("Срочный выезд, аварийная служба", "300 крон"),
            ("Скидка постоянным клиентам", "−50 %"),
            ("Скидка жертвам преступлений (взлом и т. п.)", "−30 %"),
            ("Вне рабочего времени (17:00–07:00), выходные, праздники", "+100 %"),
            ("Расходные материалы (свёрла, фрезы, диски)", "по расходу"),
        ],
        "area_eyebrow": "Где работаем", "area_head": "Вся Прага 1–22 и ближайшие окрестности",
        "area_lead": "Наши машины распределены по всей Праге, поэтому к вам приедет ближайший "
                     "мастер. Выезжаем и за пределы Праги — тогда +20 крон за километр.",
        "area_btn": "Уточнить по телефону", "area_more": "+ окрестности",
        "rev_eyebrow": "Отзывы", "rev_head": "Что говорят наши клиенты",
        "rev_lead": "Настоящие отзывы из Google. Публикуем и критические — именно "
                    "благодаря им мы становимся лучше.",
        "rev_sum": "Общая оценка на основе <strong>887 отзывов</strong>",
        "cta_head": "Стоите перед дверью и не можете войти?",
        "cta_text": "Позвоните нам. Консультация бесплатна, цену называем заранее, "
                    "и мастер выезжает сразу — в любой день и в любое время.",
    },
    "ua": {
        "title": "Слюсар Прага — аварійне відкриття замків цілодобово",
        "desc": "Аварійна слюсарна служба в Празі, цілодобово. Відкриття захряслих дверей, "
                "заміна замків, відкриття авто та сейфів. Приїзд за 30 хвилин. "
                "4,8★ з 887 відгуків.",
        "badge": "Працюємо просто зараз — цілодобово, і у свята",
        "h1_a": "Захряснули двері?", "h1_b": "Приїдемо за", "h1_em": "30 хвилин",
        "sub": "Аварійна слюсарна служба для Праги та околиць. Відкриємо двері, автомобіль "
               "і сейф — швидко, без жодної подряпини та за найнижчими цінами в Празі.",
        "chips": ["<b>4,8</b> з 887 відгуків", "Цілодобово <b>24 / 7</b>",
                  "Приїзд <b>за 30 хвилин</b>", "<b>2 роки</b> гарантії на роботу",
                  "Знижка <b>50 %</b> постійним клієнтам"],
        "ticker": ["Відкриття захряслих дверей", "Заміна замків і циліндрів",
                   "Відкриття авто без пошкоджень", "Відкриття та сервіс сейфів",
                   "Ремонт дверей після зламу", "Виймання зламаного ключа",
                   "Встановлення захисних засувів", "Розумні замки"],
        "stats": ["років досвіду в галузі", "оцінок від клієнтів",
                  "середня оцінка в Google", "працюємо без перерви"],
        "svc_eyebrow": "Наші послуги",
        "svc_head": "У Празі немає замка, з яким ми б не впоралися",
        "svc_lead": "Від захряслих дверей до сейфів і замків запалювання. Працюємо лише "
                    "найсучаснішим інструментом — відкриття без пошкоджень гарантуємо.",
        "svc": [
            ("Відкриття дверей", "Відкриємо двері без жодної подряпини. Захряслі та замкнені, "
             "із захисною фурнітурою і багатозапорним замком.", "від 290 крон"),
            ("Заміна замків", "Встановлюємо й міняємо будь-які замки та циліндри — усіх марок, "
             "типів і класів безпеки, від стандартних до найвищих.", "від 290 крон"),
            ("Відкриття авто", "Майстри автомобільних замків. Гарантуємо відкриття без "
             "подряпин і без пошкодження замка чи кузова.", "від 590 крон"),
            ("Відкриття сейфів", "Забули код або комбінацію? Зламався ключ чи відмовила "
             "механіка? Наші слюсарі впораються.", "від 1 190 крон"),
            ("Ремонт після зламу", "Зломи в Празі трапляються. Спокій треба повернути "
             "якнайшвидше — ми готові цілодобово.", "від 390 крон"),
            ("Аварійна служба", "Телефонуйте будь-коли — хоч опівночі, у вихідний чи "
             "у свято. Консультація телефоном безкоштовна.", "виїзд 300 крон"),
        ],
        "why_head": "Шість причин, чому нам телефонують знову",
        "why_lead": "Наша мета — якісно виконана робота і задоволений клієнт. Оцінки "
                    "клієнтів говорять самі за себе.",
        "why": [
            ("Доступні ціни", "Тримаємо ціни низькими, щоб клієнти залишалися задоволені. "
             "Пенсіонери, люди з інвалідністю, постійні клієнти та жертви злочинів "
             "отримують знижку."),
            ("Швидка допомога", "Гарантуємо швидкий приїзд і високу якість роботи. "
             "На роботу й матеріали завжди даємо два роки гарантії."),
            ("Цілодобово", "Слюсар у Празі доступний вам цілодобово. Професійні та швидкі "
             "послуги в Празі й околицях 24/7."),
            ("Високі оцінки", "Оцінки клієнтів говорять ясно — ми на правильному шляху "
             "і постійно вдосконалюємось. 4,8 зірки з 887 відгуків у Google."),
            ("Навчена команда", "Наші слюсарі — навчені професіонали з багаторічним досвідом. "
             "Роботу виконаємо швидко, якісно й без помилок."),
            ("30 років досвіду", "Завдяки великому досвіду працюємо якісно. Щороку "
             "обслуговуємо тисячі клієнтів по всій Празі."),
        ],
        "how_eyebrow": "Як це відбувається", "how_head": "Три кроки — і ви вдома",
        "how_lead": "Жодних форм і очікування листа. Достатньо одного дзвінка — "
                    "консультація безкоштовна.",
        "steps": [
            ("Крок 01", "Ви телефонуєте", "Відповідаємо цілодобово. Опишіть ситуацію — одразу "
             "телефоном оцінимо ціну та час приїзду. Консультація безкоштовна."),
            ("Крок 02", "Ми виїжджаємо", "Майстер у дорозі якнайшвидше — Прагою зазвичай "
             "за 20–30 хвилин після дзвінка."),
            ("Крок 03", "Відкриваємо й ремонтуємо", "Відкриваємо без пошкоджень, ціну "
             "підтверджуємо до початку робіт. Два роки гарантії."),
        ],
        "price_head": "Гарантуємо найнижчі ціни в Празі",
        "price_lead": "Ціна завжди залежить від складності роботи й обговорюється "
                      "індивідуально — на місці з майстром або телефоном з диспетчером.",
        "tabs": ["Квартири та будинки", "Ремонт і встановлення замків", "Відкриття авто", "Виїзд і знижки"],
        "extra": [
            ("Транспортні витрати (за відстанню)", "490 крон"),
            ("Виїзд за межі Праги", "+20 крон / км"),
            ("Терміновий виїзд, аварійна служба", "300 крон"),
            ("Знижка постійним клієнтам", "−50 %"),
            ("Знижка жертвам злочинів (злам тощо)", "−30 %"),
            ("Поза робочим часом (17:00–07:00), вихідні, свята", "+100 %"),
            ("Витратні матеріали (свердла, фрези, диски)", "за витратою"),
        ],
        "area_eyebrow": "Де працюємо", "area_head": "Уся Прага 1–22 та найближчі околиці",
        "area_lead": "Наші машини розподілені по всій Празі, тож до вас приїде найближчий "
                     "майстер. Виїжджаємо й за межі Праги — тоді +20 крон за кілометр.",
        "area_btn": "Уточнити телефоном", "area_more": "+ околиці",
        "rev_eyebrow": "Відгуки", "rev_head": "Що кажуть наші клієнти",
        "rev_lead": "Справжні відгуки з Google. Публікуємо й критичні — саме завдяки "
                    "їм ми стаємо кращими.",
        "rev_sum": "Загальна оцінка на основі <strong>887 відгуків</strong>",
        "cta_head": "Стоїте перед дверима й не можете увійти?",
        "cta_text": "Зателефонуйте нам. Консультація безкоштовна, ціну називаємо наперед, "
                    "і майстер виїжджає одразу — будь-якого дня й будь-якої години.",
    },
}


# --------------------------------------------------------------------------- #
# Podstránky služeb
# --------------------------------------------------------------------------- #
SERVICES = {"en": {}, "ru": {}, "ua": {}}

SERVICES["en"] = {
    "otevirani-dveri": {
        "nav": "Door opening",
        "h1": "Emergency door opening in Prague",
        "title": "Door opening Prague — emergency opening of slammed doors, 24/7",
        "desc": "Slammed your door or lost your keys? We open without damage, technician "
                "with you in 10–40 minutes. Non-stop 24/7, from 290 CZK.",
        "img": "otevirani-dveri", "img_alt": "Locksmith opening a slammed door",
        "lead": "Slammed your door or lost your keys? We know it's an unpleasant situation — "
                "and we're here for you non-stop, 24 hours a day, 7 days a week.",
        "ticks": ["A technician arrives <b>in 10–40 minutes</b> anywhere in Prague",
                  "We open <b>without a single scratch</b> — the lock keeps working",
                  "We quote the price <b>up front</b>, no hidden fees"],
        "why_head": "Why Rychlý Zámečník is the right call for door opening",
        "why_lead": "In a crisis there's no time to waste. That's why we're available for "
                    "immediate help 24/7, ready to act at once.",
        "why": [("bolt", "Express arrival",
                 "Our team sets off immediately and guarantees arrival within 10–40 minutes, "
                 "wherever you are in the city."),
                ("shield", "Gentle opening",
                 "Our technicians use advanced tools to open your door without any damage. "
                 "The lock will keep working exactly as it should."),
                ("coin", "Fair prices",
                 "For emergency door opening we guarantee a clear, honest price with no "
                 "hidden fees.")],
        "prices": "otevirani-bytu",
        "prose_head": "What makes us the first choice for emergency door opening",
        "prose": ["We specialise in crisis situations where every minute counts. Beyond "
                  "technical skill and speed, we guarantee a <strong>human, empathetic "
                  "approach</strong> that takes the edge off an unpleasant moment.",
                  "Our kit contains only the most modern technology for emergency opening. "
                  "That lets us solve even the hardest case quickly and always without "
                  "damaging your lock.",
                  "Our team is made up of experienced locksmiths who keep expanding their "
                  "knowledge and have a thorough grasp of security systems of every type."],
        "faq": [("How fast does the locksmith arrive?",
                 "Across Prague we guarantee arrival within 10–40 minutes of your call, "
                 "depending on where the nearest technician is and on traffic. We'll give "
                 "you a closer estimate on the phone."),
                ("Will you damage my door or lock?",
                 "In the vast majority of cases, no. We use non-destructive methods after "
                 "which the lock works normally. If a particular lock can't be opened that "
                 "way, we'll tell you beforehand and agree on how to proceed."),
                ("How much does door opening cost?",
                 "A slammed door without security fittings starts at 290 CZK, with security "
                 "fittings from 490 CZK. Locked doors start at 390 CZK. The final price "
                 "depends on the lock type and we confirm it before starting work."),
                ("Do I have to prove the flat is mine?",
                 "Yes. Before we start we'll ask for ID and proof of your relationship to "
                 "the property — a tenancy agreement, a land registry extract, or "
                 "confirmation from a neighbour or the owner. It protects you as much as us."),
                ("Do you come at night and on public holidays?",
                 "Yes, the dispatcher answers around the clock, including nights, weekends "
                 "and public holidays. Outside working hours (17:00–07:00), at weekends and "
                 "on holidays a surcharge applies.")],
    },
    "vymena-zamku": {
        "nav": "Lock replacement",
        "h1": "Lock and security cylinder replacement in Prague",
        "title": "Lock replacement Prague — security cylinders and fittings fitted",
        "desc": "Fitting and replacing locks of every brand and security class — FAB, EVVA, "
                "MUL-T-LOCK, TOKOZ, ABUS. Free advice, from 290 CZK.",
        "img": "vymena-zamku", "img_alt": "Fitting and replacing a security lock",
        "lead": "Replacing locks is work we've been doing in Prague for years. We'll fit "
                "security cylinders and locks of any brand, including a full master key system.",
        "ticks": ["We reach any part of Prague <b>in roughly 20 minutes</b>",
                  "Cylinders in <b>all security classes 1–5</b> from leading manufacturers",
                  "<b>Free advice</b> — we'll suggest a solution that fits your budget"],
        "why_head": "Why Rychlý Zámečník is the right call for lock replacement",
        "why_lead": "We don't just replace the lock quickly and precisely. We also advise "
                    "you on choosing the best security cylinder for your door.",
        "why": [("bolt", "Fast and fully equipped",
                 "Our locksmiths arrive fully prepared — carrying the agreed lock and "
                 "cylinder plus spare parts for unexpected complications."),
                ("clock", "Lock replaced right away",
                 "Urgent security reasons deserve a fast fix. Our emergency service runs "
                 "24/7 — don't put your protection off."),
                ("users", "Tailored advice, free",
                 "We'll walk you through the options and explain what the security classes "
                 "mean and why the lock has to be matched with the right fittings.")],
        "prices": "zamky",
        "prose_head": "Professional security lock replacement",
        "prose": ["We work with <strong>certified security cylinders in all classes (1–5)</strong> "
                  "from leading manufacturers such as FAB, EVVA, MUL-T-LOCK, RICHTER, TOKOZ "
                  "and ABUS. We also specialise in ATRA, MOTTURA and CISA security locks.",
                  "For many burglars a security cylinder on its own is a challenge rather "
                  "than an obstacle. That's why we always recommend thinking about "
                  "<strong>security fittings</strong> alongside the cylinder — they protect "
                  "it from being snapped — or a security bar against forcing.",
                  "Every product we install meets European standards for quality, safety and "
                  "durability. Our technicians hold the necessary certifications and keep "
                  "their knowledge current through regular training."],
        "faq": [("Which lock should I choose?",
                 "It depends on what you're protecting and what doors you have. Security "
                 "classes run from 1 to 5 — for a typical flat, class 3 combined with "
                 "security fittings is usually enough. The consultation is free."),
                ("Is replacing just the cylinder enough, or do I need a whole new lock?",
                 "In most cases replacing the cylinder is enough — it's cheaper and faster. "
                 "The whole lock gets replaced when the mechanism is damaged, the latch "
                 "jams, or you're moving to a different type of protection."),
                ("Do you carry cylinders in stock?",
                 "We carry the most common types and variants with us, so we usually manage "
                 "the replacement in a single visit. Special or non-standard cylinders are "
                 "ordered in — we'll confirm the timing by phone."),
                ("Can you set up a master key system?",
                 "Yes. We'll design and install a master key system — where one key opens "
                 "several locks and other keys only selected ones — tailored to you. It "
                 "suits houses, offices and business premises."),
                ("What warranty do you give?",
                 "We give a two-year warranty on the work done and on the materials used.")],
    },
    "otevirani-aut": {
        "nav": "Car opening",
        "h1": "Emergency car opening without damage",
        "title": "Car opening Prague — emergency vehicle opening without damage, 24/7",
        "desc": "Car locked with the keys inside? We open without breaking glass and without "
                "damaging paint or electronics. Non-stop 24/7, from 590 CZK.",
        "img": "otevirani-aut", "img_alt": "Emergency opening of a car without a key",
        "lead": "Car locked with the keys inside? Flat battery? A child or a running engine "
                "shut in? We deal with it — and without breaking any glass.",
        "ticks": ["<b>No broken glass</b> — we open using gentle methods",
                  "We preserve <b>100 % of the paint, doors and electronics</b>",
                  "We arrive fast, the emergency service runs <b>24/7</b>"],
        "why_head": "Why Rychlý Zámečník is the right call for car opening",
        "why_lead": "In urgent situations with a locked car there's no room for compromise. "
                    "Our reaction speed and professional practice are your guarantee.",
        "why": [("bolt", "Fast arrival",
                 "Thanks to smart logistics and round-the-clock service, a certified "
                 "locksmith is at your vehicle within 10 to 40 minutes of your call."),
                ("shield", "Opening without damage",
                 "We guarantee gentle methods that preserve the integrity of the paint, "
                 "doors and sensitive electronics. No follow-up repairs to deal with."),
                ("clock", "A locksmith right now",
                 "Whether you need a locksmith in the middle of the night, at the weekend "
                 "or on a public holiday, our emergency service is always ready.")],
        "prices": "auta",
        "prose_head": "We open modern vehicles with safe-type security too",
        "prose": ["The price for opening a car depends mainly on the <strong>model year and "
                  "type of security</strong>. Older vehicles up to 2002 are the simplest; "
                  "newer models with a safe-type lock need special tools and more time.",
                  "Besides the opening itself we handle <strong>lock replacement, ignition "
                  "switches and the removal of gear locks</strong> such as DEFEND LOCK. "
                  "All on the spot, with no tow to a garage.",
                  "If there's a child or an animal shut in the car, say so at the start of "
                  "the call — we move that kind of call-out to the front of the queue."],
        "faq": [("Can you open a newer car with an immobiliser?",
                 "Yes. Opening the vehicle and the immobiliser are two different things — we "
                 "get you inside without touching the electronics. Cars from 2007 onwards "
                 "and safe-type security take more work, which is reflected in the price."),
                ("Will you break a window?",
                 "No. We use tools that open the vehicle without damaging the glass, paint "
                 "or seals. Breaking glass is a last resort we'd only use at your explicit "
                 "request — for instance where life is at risk."),
                ("Do I have to prove the car is mine?",
                 "Yes, before opening we'll ask for ID and vehicle documents — the "
                 "registration certificate or a contract. We won't open the vehicle without it."),
                ("What if the keys are locked in and the engine is running?",
                 "Call straight away and mention it — it's an urgent situation we handle as "
                 "a priority. We'll open the car without damage; the engine can keep running."),
                ("Can you make a new key if I've lost mine?",
                 "We'll open the vehicle and we can replace the locks and the ignition "
                 "switch. Cutting and programming a new chipped key for newer vehicles has "
                 "to go through a main dealer — we'll advise you by phone.")],
    },
    "otevirani-trezoru": {
        "nav": "Safe opening",
        "h1": "Safe opening and servicing",
        "title": "Safe opening Prague — emergency safe opening, servicing and repairs",
        "desc": "Forgotten the code or lost the key to your safe? We've been opening "
                "electronic and mechanical safes since 1990 — SAFEMETAL, ROTTNER, KOVONA "
                "and more.",
        "img": "otevirani-trezoru", "img_alt": "Locksmith opening a safe",
        "lead": "Need to get into a safe but the key or code is missing? Battery dead? "
                "We specialise in emergency safe opening, with practice going back to 1990.",
        "ticks": ["We open <b>electronic and mechanical combination safes</b>",
                  "The gentlest methods — the safe stays <b>usable afterwards</b>",
                  "Even a necessary small intervention is <b>professionally filled</b>"],
        "why_head": "Why Rychlý Zámečník is the right call for safe opening",
        "why_lead": "We don't just open it fast. We'll also advise you on the most suitable "
                    "safe lock for your model.",
        "why": [("bolt", "Rapid arrival",
                 "The team sets off the moment you call and guarantees arrival anywhere in "
                 "the city within 10 to 40 minutes."),
                ("shield", "Non-destructive opening",
                 "We open safes using methods that guarantee zero damage. The mechanism "
                 "will be fully functional afterwards, exactly as before."),
                ("coin", "No shocks, just a fair price",
                 "Opening a safe is stressful enough. We guarantee a transparent, honest "
                 "price straight away — no surprises on the invoice.")],
        "prices": "otevirani-bytu",
        "prose_head": "The safes we can handle",
        "prose": ["We open safes from <strong>SAFEMETAL, ROTTNER, KOVONA, T-SAFE, ASIST, "
                  "BULDOK</strong> and many others — mechanical key safes, combination "
                  "safes and electronic ones.",
                  "The most common reasons people call: a forgotten code or combination, "
                  "a lost or broken key, a <strong>flat battery in an electronic lock</strong> "
                  "and mechanical failure.",
                  "Besides opening we handle repairs and full servicing of safes, including "
                  "replacing the safe lock. The price is set by the type of safe, which is "
                  "why we always agree it individually."],
        "faq": [("Can you open the safe without destroying it?",
                 "That's our aim and in most cases we manage it. We choose the gentlest "
                 "possible method so the safe stays usable. If drilling is unavoidable, we "
                 "professionally fill the hole afterwards with a special compound."),
                ("I've forgotten the code. Can anything be done?",
                 "Yes, it's one of the most common reasons people call us. For electronic "
                 "and mechanical combination safes alike we have ways in, and we'll set a "
                 "new code for you afterwards."),
                ("How much does opening a safe cost?",
                 "The price follows the type of safe and the complexity, which is why we "
                 "list it as 'by type'. A jammed safe lock on a door starts at 1,190 CZK, "
                 "a locked safe lock from 1,990 CZK. You'll get a concrete estimate by phone."),
                ("Can you replace the safe lock?",
                 "Yes, we handle repairs and complete servicing of safes including lock "
                 "replacement, and we'll advise on choosing a suitable type."),
                ("What should I have ready?",
                 "ID and proof that the safe belongs to you or your company — a receipt, "
                 "an invoice, an insurance policy. For company safes we need the consent "
                 "of an authorised person.")],
    },
    "oprava-dveri": {
        "nav": "Door repair",
        "h1": "Door repair after a break-in",
        "title": "Door repair after a break-in, Prague — immediate call-out and security",
        "desc": "A break-in is a shock. We'll get you back to safety fast — repairing doors "
                "and locks and proposing lasting security. Non-stop 24/7, from 390 CZK.",
        "img": "otevirani-zamku", "img_alt": "Repairing a door and lock after a break-in",
        "lead": "A break-in is a shock. We make sure you get back to safety fast — we come "
                "out, repair the doors and locks properly, and propose how to secure the "
                "place for the future.",
        "ticks": ["<b>Immediate call-out</b> — doors and locks repaired on the spot",
                  "<b>Lasting security</b> — a plan for your flat or business premises",
                  "<b>30 %</b> discount for victims of crime"],
        "why_head": "Why Rychlý Zámečník is the right call for door repair",
        "why_lead": "In a crisis, time is the most expensive thing there is. That's why a "
                    "locksmith is available to you non-stop, 24 hours a day, 7 days a week.",
        "why": [("bolt", "On site within 30 minutes",
                 "Our locksmiths are spread across the city to keep response times short. "
                 "For crisis call-outs we guarantee arrival in 10–30 minutes."),
                ("clock", "Call any time",
                 "We're reachable without a break — your certainty of fast, professional "
                 "help at any hour of the day or night."),
                ("coin", "Fair prices",
                 "A break-in is stress enough. No tricks, no hidden fees — our promise of "
                 "transparency holds without exception.")],
        "prices": "zamky",
        "prose_head": "What to do if someone has broken in",
        "prose": ["<strong>Call the police first</strong> and, if you can, move nothing "
                  "before they arrive — both for the investigation and for the insurer. "
                  "Photograph the state of the door and lock; you'll need it when reporting "
                  "the claim.",
                  "Only then call us. We'll come out, <strong>get the doors working and "
                  "replace the damaged locks</strong> so you can lock up safely the same day.",
                  "We'll go through how the intruder got in and suggest what to strengthen — "
                  "a security cylinder with fittings, an additional lock, or a bar against "
                  "forcing. <strong>Victims of crime get a 30 % discount.</strong>"],
        "faq": [("Do you come immediately or do I book a slot?",
                 "After a break-in we come out immediately — it's a crisis call-out. We "
                 "guarantee arrival within 10–30 minutes of your call."),
                ("Will the insurance cover it?",
                 "In most cases yes, if you have home contents insurance. We'll issue a "
                 "document itemising labour and materials for you to submit. Please "
                 "photograph the state of the door before the repair."),
                ("Can the original doors be repaired, or do I need new ones?",
                 "It depends on the extent of the damage. Often it's enough to repair the "
                 "frame and replace the lock and fittings. If the doors are forced badly "
                 "enough that safety can't be guaranteed, we'll say so plainly."),
                ("Will you advise on preventing it next time?",
                 "Yes, it's part of the job. We'll go through how the intruder got in and "
                 "propose concrete measures — a security cylinder with fittings, an "
                 "additional lock or a security bar."),
                ("Is the discount for crime victims automatic?",
                 "We apply it on site — just say it's a call-out after a break-in. We "
                 "recommend having the police reference number to hand.")],
    },
    "zamecnicka-pohotovost": {
        "nav": "Emergency service",
        "h1": "Locksmith emergency service Prague — non-stop 24/7",
        "title": "Locksmith emergency service Prague — a locksmith 24 hours a day",
        "desc": "The fastest locksmith emergency service in Prague at sensible prices. "
                "Opening doors, cars and safes, replacing locks. Non-stop 24/7, 30 years "
                "of experience.",
        "img": "vyjezd-den", "img_alt": "Emergency locksmith van on a call-out",
        "lead": "A locksmith business with a long history. Quality emergency cover at "
                "sensible prices — any day, at any hour.",
        "ticks": ["Opening <b>slammed and locked doors</b> and emergency lock opening",
                  "Opening <b>cars without a key</b>, with no damage whatsoever",
                  "Opening, repair and <b>full servicing of safes</b>",
                  "Fitting and replacing <b>all types of locks</b>, cylinders and fittings",
                  "Fitting security <b>bars, additional locks and barriers</b>",
                  "Door repairs after break-ins and <b>security proposals</b>"],
        "why_head": "A Prague locksmith you can rely on",
        "why_lead": "Found yourself needing fast help from a locksmith, or just want some "
                    "advice? Our locksmith service is here for you 24 hours a day.",
        "why": [("clock", "Non-stop, genuinely",
                 "The dispatcher answers day and night, at weekends and on public holidays. "
                 "Advice over the phone is free."),
                ("users", "Thousands of customers a year",
                 "We've been providing locksmith services for many years and serve thousands "
                 "of customers annually — professional work, without mistakes."),
                ("star", "The most modern tools",
                 "To guarantee the highest quality of service we use only the most modern "
                 "tools and equipment.")],
        "prices": "otevirani-bytu",
        "prose_head": "Replacing the lock isn't everything",
        "prose": ["For many burglars a security cylinder is <strong>a challenge, not an "
                  "obstacle</strong>. That's why we always recommend thinking about security "
                  "fittings alongside a cylinder replacement — they protect the cylinder "
                  "from being snapped.",
                  "Even security fittings with a security cylinder won't protect a flat or "
                  "house from burglars 100 %. You can therefore also fit a <strong>security "
                  "bar</strong>, which protects the door against being forced.",
                  "Our specialists will advise on everything and help make your property as "
                  "well protected as possible. Replacing the cylinder matters, but there are "
                  "many further ways to secure a house or flat better."],
        "faq": [("Are you really non-stop, holidays included?",
                 "Yes. The dispatcher answers 24 hours a day, 7 days a week, including "
                 "weekends and public holidays. Outside working hours (17:00–07:00), at "
                 "weekends and on holidays a surcharge applies."),
                ("What do you charge for the call-out?",
                 "The travel charge is 490 CZK depending on distance, an express call-out "
                 "300 CZK. Outside Prague we charge +20 CZK per kilometre. Advice over the "
                 "phone is free."),
                ("Do you offer any discounts?",
                 "Yes. Regular customers get 50 %, victims of crime 30 %. We also give a "
                 "discount to seniors and disability card holders."),
                ("How far do you travel?",
                 "We cover all of Prague 1–22 and the nearby area. We travel further too; "
                 "travel outside Prague is then charged at +20 CZK per kilometre."),
                ("How much experience do you have?",
                 "We've been in the trade for 30 years and serve thousands of customers a "
                 "year. On Google we have a rating of 4.8 from 887 reviews.")],
    },
}

SERVICES["ru"] = {
    "otevirani-dveri": {
        "nav": "Вскрытие дверей",
        "h1": "Аварийное вскрытие дверей в Праге",
        "title": "Вскрытие дверей Прага — аварийное вскрытие захлопнувшихся дверей 24/7",
        "desc": "Захлопнулась дверь или потеряли ключи? Вскроем без повреждений, мастер "
                "у вас за 10–40 минут. Круглосуточно 24/7, от 290 крон.",
        "img": "otevirani-dveri", "img_alt": "Слесарь вскрывает захлопнувшуюся дверь",
        "lead": "Захлопнулась дверь или потеряли ключи? Понимаем, что ситуация неприятная — "
                "и мы рядом круглосуточно, 24 часа в сутки, 7 дней в неделю.",
        "ticks": ["Мастер приедет <b>за 10–40 минут</b> в любую точку Праги",
                  "Вскроем <b>без единой царапины</b> — замок останется рабочим",
                  "Цену назовём <b>заранее</b>, без скрытых платежей"],
        "why_head": "Почему Rychlý Zámečník — правильный выбор для вскрытия дверей",
        "why_lead": "В критическую минуту терять время нельзя. Поэтому мы готовы помочь "
                    "немедленно, 24/7.",
        "why": [("bolt", "Срочный приезд",
                 "Наша команда выезжает сразу и гарантирует приезд за 10–40 минут, где бы "
                 "вы ни находились в городе."),
                ("shield", "Бережное вскрытие",
                 "Мастера используют современный инструмент, чтобы вскрыть дверь без "
                 "повреждений. Замок продолжит работать как прежде."),
                ("coin", "Честные цены",
                 "За аварийное вскрытие двери гарантируем понятную и честную цену "
                 "без скрытых платежей.")],
        "prices": "otevirani-bytu",
        "prose_head": "Что делает нас первым выбором при аварийном вскрытии",
        "prose": ["Мы специализируемся на кризисных ситуациях, где важна каждая минута. "
                  "Кроме технических навыков и скорости гарантируем <strong>человечный "
                  "и участливый подход</strong>, который облегчит неприятный момент.",
                  "В нашем оснащении только самые современные технологии аварийного "
                  "вскрытия. Благодаря этому решаем даже самый сложный случай быстро "
                  "и всегда без повреждения замка.",
                  "Наша команда — опытные слесари, которые постоянно расширяют знания "
                  "и хорошо разбираются в системах безопасности всех типов."],
        "faq": [("Как быстро приедет слесарь?",
                 "По Праге гарантируем приезд за 10–40 минут после звонка — в зависимости "
                 "от того, где сейчас ближайший мастер и какова дорожная обстановка. Более "
                 "точную оценку назовём сразу по телефону."),
                ("Повредите ли вы дверь или замок?",
                 "В подавляющем большинстве случаев нет. Мы применяем неразрушающие методы, "
                 "после которых замок работает нормально. Если конкретный замок так вскрыть "
                 "нельзя, скажем об этом заранее и договоримся о дальнейших действиях."),
                ("Сколько стоит вскрытие двери?",
                 "Захлопнувшуюся дверь без защитной фурнитуры вскроем от 290 крон, "
                 "с защитной фурнитурой — от 490 крон. Запертые двери — от 390 крон. "
                 "Итоговая цена зависит от типа замка и подтверждается до начала работ."),
                ("Нужно ли доказывать, что квартира моя?",
                 "Да. До начала работ мы попросим удостоверение личности и документ, "
                 "подтверждающий ваше отношение к жилью — договор аренды, выписку из "
                 "кадастра или подтверждение от соседа либо владельца. Это защита и для вас."),
                ("Работаете ли ночью и в праздники?",
                 "Да, диспетчер принимает звонки круглосуточно, включая ночи, выходные "
                 "и государственные праздники. Вне рабочего времени (17:00–07:00), "
                 "в выходные и праздники действует наценка.")],
    },
    "vymena-zamku": {
        "nav": "Замена замков",
        "h1": "Замена замков и защитных цилиндров в Праге",
        "title": "Замена замков Прага — установка защитных цилиндров и фурнитуры",
        "desc": "Установка и замена замков всех марок и классов защиты — FAB, EVVA, "
                "MUL-T-LOCK, TOKOZ, ABUS. Консультация бесплатно, от 290 крон.",
        "img": "vymena-zamku", "img_alt": "Установка и замена защитного замка",
        "lead": "Заменой замков в Праге мы занимаемся уже много лет. Установим защитные "
                "цилиндры и замки любой марки, включая систему единого ключа.",
        "ticks": ["В любую часть Праги доберёмся <b>примерно за 20 минут</b>",
                  "Цилиндры <b>всех классов защиты 1–5</b> от ведущих производителей",
                  "<b>Консультация бесплатно</b> — подберём решение по цене и защите"],
        "why_head": "Почему Rychlý Zámečník — правильный выбор для замены замка",
        "why_lead": "Мы не только быстро и аккуратно заменим замок. Ещё и подскажем, какой "
                    "защитный цилиндр лучше подойдёт вашей двери.",
        "why": [("bolt", "Скорость и полное оснащение",
                 "Слесари приезжают полностью готовыми — везут не только оговорённый тип "
                 "замка и цилиндра, но и запасные части на случай осложнений."),
                ("clock", "Замена замка сразу",
                 "Срочные соображения безопасности заслуживают быстрого решения. Наша "
                 "аварийная служба работает 24/7 — не откладывайте свою защиту."),
                ("users", "Индивидуальная консультация бесплатно",
                 "Разберём с вами все варианты и объясним, что означают классы защиты "
                 "и почему важно правильно сочетать замок с фурнитурой.")],
        "prices": "zamky",
        "prose_head": "Профессиональная замена защитного замка",
        "prose": ["Работаем с <strong>сертифицированными защитными цилиндрами всех классов "
                  "(1–5)</strong> от ведущих мировых производителей: FAB, EVVA, MUL-T-LOCK, "
                  "RICHTER, TOKOZ, ABUS. Специализируемся также на замках ATRA, MOTTURA и CISA.",
                  "Для многих взломщиков сам по себе защитный цилиндр — скорее вызов, чем "
                  "препятствие. Поэтому вместе с заменой цилиндра всегда рекомендуем подумать "
                  "и о <strong>защитной фурнитуре</strong>, которая бережёт цилиндр от "
                  "выламывания, либо о защитном засове против отжима.",
                  "Все устанавливаемые изделия отвечают европейским стандартам качества, "
                  "безопасности и долговечности. У наших мастеров есть нужные сертификаты, "
                  "и они регулярно проходят обучение."],
        "faq": [("Какой замок выбрать?",
                 "Зависит от того, что вы защищаете и какие у вас двери. Классы защиты — "
                 "от 1 до 5; для обычной квартиры обычно достаточно класса 3 в сочетании "
                 "с защитной фурнитурой. Консультацию дадим бесплатно."),
                ("Достаточно заменить только цилиндр или нужен весь замок?",
                 "В большинстве случаев достаточно заменить цилиндр — это дешевле и быстрее. "
                 "Весь замок меняют, когда повреждён механизм, заклинила защёлка или вы "
                 "переходите на другой тип защиты."),
                ("Цилиндры есть в наличии?",
                 "Самые распространённые типы возим с собой, поэтому замену обычно делаем "
                 "за один выезд. Специальные или нестандартные цилиндры заказываем — сроки "
                 "подтвердим по телефону."),
                ("Настроите систему единого ключа?",
                 "Да. Систему единого ключа — когда один ключ открывает несколько замков, "
                 "а остальные только выбранные — спроектируем и установим под ваши задачи. "
                 "Подходит для домов, офисов и коммерческих помещений."),
                ("Какую даёте гарантию?",
                 "На выполненную работу и использованные материалы даём два года гарантии.")],
    },
    "otevirani-aut": {
        "nav": "Вскрытие авто",
        "h1": "Аварийное вскрытие автомобиля без повреждений",
        "title": "Вскрытие авто Прага — аварийное вскрытие автомобиля без повреждений 24/7",
        "desc": "Автомобиль заперт, а ключи внутри? Вскроем без разбивания стекла и без "
                "повреждения краски и электроники. Круглосуточно 24/7, от 590 крон.",
        "img": "otevirani-aut", "img_alt": "Аварийное вскрытие автомобиля без ключа",
        "lead": "Автомобиль заперт, а ключи внутри? Села аккумуляторная батарея? Закрыт "
                "ребёнок или работает двигатель? Решаем — и без разбивания стекла.",
        "ticks": ["<b>Стекло разбивать не будем</b> — вскрываем бережными методами",
                  "Сохраним <b>краску, двери и электронику на 100 %</b>",
                  "Приедем быстро, служба работает <b>24/7</b>"],
        "why_head": "Почему Rychlý Zámečník — правильный выбор для вскрытия авто",
        "why_lead": "В срочных ситуациях с запертым автомобилем компромиссов не бывает. "
                    "Наша скорость реакции и практический опыт — ваша гарантия.",
        "why": [("bolt", "Скорость приезда",
                 "Благодаря продуманной логистике и круглосуточной работе сертифицированный "
                 "мастер будет у вашего автомобиля за 10–40 минут после звонка."),
                ("shield", "Вскрытие без повреждений",
                 "Гарантируем бережные методы, сохраняющие целостность краски, дверей "
                 "и чувствительной электроники. Никаких последующих ремонтов."),
                ("clock", "Слесарь сейчас же",
                 "Нужен ли мастер посреди ночи, в выходной или в праздник — наша аварийная "
                 "служба всегда готова.")],
        "prices": "auta",
        "prose_head": "Вскрываем и современные авто с сейфовой защитой",
        "prose": ["Цена вскрытия автомобиля зависит прежде всего от <strong>года выпуска "
                  "и типа защиты</strong>. Машины до 2002 года самые простые, более новые "
                  "модели с сейфовым типом замка требуют специального инструмента и времени.",
                  "Кроме самого вскрытия занимаемся <strong>заменой замков, замков зажигания "
                  "и демонтажем замков КПП</strong> типа DEFEND LOCK. Всё на месте, без "
                  "эвакуации в сервис.",
                  "Если в машине заперт ребёнок или животное, скажите об этом сразу в начале "
                  "разговора — такой выезд ставим в начало очереди."],
        "faq": [("Вскроете ли более новую машину с иммобилайзером?",
                 "Да. Вскрытие автомобиля и иммобилайзер — разные вещи: мы откроем салон, "
                 "не вмешиваясь в электронику. У машин от 2007 года и с сейфовым типом "
                 "защиты работа сложнее, что отражается на цене."),
                ("Будете разбивать стекло?",
                 "Нет. Мы используем инструмент, который открывает автомобиль без "
                 "повреждения стекла, краски и уплотнителей. Разбивание стекла — крайняя "
                 "мера, к которой мы прибегли бы только по вашей прямой просьбе, например "
                 "при угрозе жизни."),
                ("Нужно ли доказывать, что машина моя?",
                 "Да, перед вскрытием попросим удостоверение личности и документ на "
                 "автомобиль — техпаспорт или договор. Без этого машину не откроем."),
                ("Что если ключи внутри, а двигатель работает?",
                 "Позвоните сразу и скажите об этом — это срочная ситуация, которую мы "
                 "решаем в приоритете. Автомобиль вскроем без повреждений, двигатель может "
                 "продолжать работать."),
                ("Сделаете новый ключ, если старый потерян?",
                 "Автомобиль вскроем, можем заменить замки и замок зажигания. Изготовление "
                 "и программирование нового чип-ключа у новых машин нужно решать "
                 "у официального сервиса — подскажем по телефону.")],
    },
    "otevirani-trezoru": {
        "nav": "Вскрытие сейфов",
        "h1": "Вскрытие и обслуживание сейфов",
        "title": "Вскрытие сейфов Прага — аварийное вскрытие сейфа, сервис и ремонт",
        "desc": "Забыли код или потеряли ключ от сейфа? Вскрываем электронные и механические "
                "сейфы с 1990 года — SAFEMETAL, ROTTNER, KOVONA и другие.",
        "img": "otevirani-trezoru", "img_alt": "Слесарь вскрывает сейф",
        "lead": "Нужно попасть в сейф, но нет ключа или кода? Села батарейка? Мы специалисты "
                "по аварийному вскрытию сейфов с опытом с 1990 года.",
        "ticks": ["Вскрываем <b>электронные и механические кодовые сейфы</b>",
                  "Самые бережные методы — сейфом можно <b>пользоваться дальше</b>",
                  "Даже необходимое небольшое вмешательство <b>профессионально заделаем</b>"],
        "why_head": "Почему Rychlý Zámečník — правильный выбор для вскрытия сейфов",
        "why_lead": "Мы не только быстро вскроем. Ещё и подскажем, какой сейфовый замок "
                    "подойдёт вашему сейфу лучше всего.",
        "why": [("bolt", "Молниеносный приезд",
                 "Команда выезжает сразу после звонка и гарантирует приезд по всему городу "
                 "в пределах 10–40 минут."),
                ("shield", "Неразрушающее вскрытие",
                 "Сейф вскрываем методами, гарантирующими нулевые повреждения. Механизм "
                 "после работы останется полностью исправным."),
                ("coin", "Без сюрпризов, честная цена",
                 "Вскрытие сейфа само по себе достаточно нервное. Поэтому гарантируем "
                 "прозрачную цену сразу — никаких «сюрпризов» в счёте.")],
        "prices": "otevirani-bytu",
        "prose_head": "С какими сейфами мы работаем",
        "prose": ["Вскрываем сейфы марок <strong>SAFEMETAL, ROTTNER, KOVONA, T-SAFE, ASIST, "
                  "BULDOK</strong> и многих других — механические ключевые, кодовые "
                  "и электронные.",
                  "Самые частые причины обращений: забытый код или комбинация, потерянный "
                  "или сломанный ключ, <strong>севшая батарейка электронного замка</strong> "
                  "и неисправность механики.",
                  "Кроме вскрытия обеспечиваем ремонт и полное обслуживание сейфов, включая "
                  "замену сейфового замка. Цена определяется типом сейфа, поэтому её всегда "
                  "обсуждаем индивидуально."],
        "faq": [("Вскроете сейф, не уничтожив его?",
                 "Это наша цель, и в большинстве случаев это удаётся. Выбираем самый "
                 "бережный метод, чтобы сейфом можно было пользоваться дальше. Если "
                 "сверление неизбежно, отверстие профессионально заделаем специальным "
                 "составом."),
                ("Я забыл код. Что-то можно сделать?",
                 "Да, это одна из самых частых причин обращений. И для электронных, и для "
                 "механических кодовых сейфов у нас есть способы попасть внутрь, после чего "
                 "настроим вам новый код."),
                ("Сколько стоит вскрытие сейфа?",
                 "Цена зависит от типа сейфа и сложности, поэтому указывается как «по типу». "
                 "Заклинивший сейфовый замок в двери вскрываем от 1 190 крон, запертый "
                 "сейфовый замок — от 1 990 крон. Конкретную оценку дадим по телефону."),
                ("Замените сейфовый замок?",
                 "Да, выполняем ремонт и полное обслуживание сейфов, включая замену замка, "
                 "и поможем выбрать подходящий тип."),
                ("Что нужно подготовить?",
                 "Удостоверение личности и документ о том, что сейф принадлежит вам или "
                 "вашей компании — чек, счёт, страховой договор. Для корпоративных сейфов "
                 "нужно согласие уполномоченного лица.")],
    },
    "oprava-dveri": {
        "nav": "Ремонт дверей",
        "h1": "Ремонт двери после взлома",
        "title": "Ремонт двери после взлома, Прага — немедленный выезд и защита",
        "desc": "Взлом — это шок. Быстро вернём вас к безопасности: отремонтируем двери "
                "и замки и предложим надёжную защиту. Круглосуточно 24/7, от 390 крон.",
        "img": "otevirani-zamku", "img_alt": "Ремонт двери и замка после взлома",
        "lead": "Взлом — это шок. Мы обеспечим быстрое возвращение к безопасности: приедем, "
                "профессионально отремонтируем двери и замки и сразу предложим, как защитить "
                "жильё на будущее.",
        "ticks": ["<b>Немедленный выезд</b> — двери и замки отремонтируем на месте",
                  "<b>Надёжная защита</b> — предложим решение для квартиры и помещения",
                  "Скидка <b>30 %</b> жертвам преступлений"],
        "why_head": "Почему Rychlý Zámečník — правильный выбор для ремонта дверей",
        "why_lead": "В критическую минуту время дороже всего. Поэтому слесарь доступен вам "
                    "круглосуточно, 24 часа в сутки, 7 дней в неделю.",
        "why": [("bolt", "Приезд за 30 минут",
                 "Наши слесари распределены по всему городу, чтобы скорость была "
                 "максимальной. При кризисных выездах гарантируем приезд за 10–30 минут."),
                ("clock", "Звоните в любое время",
                 "Мы доступны непрерывно — ваша уверенность в быстрой и профессиональной "
                 "помощи в любое время дня и ночи."),
                ("coin", "Честные цены",
                 "Взлом — уже достаточный стресс. Никаких уловок и скрытых платежей: наше "
                 "обещание прозрачности действует без исключений.")],
        "prices": "zamky",
        "prose_head": "Что делать, если к вам проникли",
        "prose": ["<strong>Сначала вызовите полицию</strong> и по возможности ничего не "
                  "перемещайте до её приезда — и ради осмотра места, и ради страховой. "
                  "Сфотографируйте состояние двери и замка, это понадобится при заявлении "
                  "о страховом случае.",
                  "Только потом звоните нам. Приедем, <strong>приведём двери в рабочее "
                  "состояние и заменим повреждённые замки</strong>, чтобы вы могли безопасно "
                  "запереть жильё в тот же день.",
                  "Сразу разберём, каким путём проник злоумышленник, и предложим, что "
                  "усилить — защитный цилиндр с фурнитурой, дополнительный замок или засов "
                  "против отжима. <strong>Жертвам преступлений даём скидку 30 %.</strong>"],
        "faq": [("Приедете сразу или нужно записываться?",
                 "После взлома выезжаем немедленно — это кризисный вызов. Гарантируем "
                 "приезд за 10–30 минут после звонка."),
                ("Оплатит ли это страховая?",
                 "В большинстве случаев да, если у вас оформлено страхование жилья. Выдадим "
                 "документ с перечнем работ и материалов для страховой. Пожалуйста, "
                 "сфотографируйте состояние двери до ремонта."),
                ("Можно ли отремонтировать исходные двери или нужны новые?",
                 "Зависит от масштаба повреждений. Часто достаточно отремонтировать коробку, "
                 "заменить замок и фурнитуру. Если двери выломаны настолько, что "
                 "безопасность гарантировать нельзя, скажем прямо."),
                ("Подскажете, как защититься в следующий раз?",
                 "Да, это часть работы. Разберём, каким путём проник злоумышленник, "
                 "и предложим конкретные меры — защитный цилиндр с фурнитурой, "
                 "дополнительный замок или защитный засов."),
                ("Скидка жертвам преступлений действует автоматически?",
                 "Применим её на месте — достаточно сказать, что это выезд после взлома. "
                 "Желательно иметь под рукой номер дела из полиции.")],
    },
    "zamecnicka-pohotovost": {
        "nav": "Аварийная служба",
        "h1": "Аварийная служба слесаря в Праге — круглосуточно 24/7",
        "title": "Аварийная служба слесаря Прага — слесарь 24 часа в сутки",
        "desc": "Самая быстрая аварийная служба слесаря в Праге за разумные деньги. "
                "Вскрытие дверей, авто и сейфов, замена замков. Круглосуточно 24/7, "
                "30 лет опыта.",
        "img": "vyjezd-den", "img_alt": "Машина аварийной слесарной службы на выезде",
        "lead": "Слесарная мастерская с давней историей. Качественная аварийная служба "
                "за разумные деньги — в любой день и в любое время.",
        "ticks": ["Вскрытие <b>захлопнувшихся и запертых дверей</b> и аварийное вскрытие замков",
                  "Вскрытие <b>авто без ключа</b>, без каких-либо повреждений",
                  "Вскрытие, ремонт и <b>полное обслуживание сейфов</b>",
                  "Установка и замена <b>всех типов замков</b>, цилиндров и фурнитуры",
                  "Установка защитных <b>засовов, дополнительных замков и решёток</b>",
                  "Ремонт дверей после взлома и <b>проекты защиты объекта</b>"],
        "why_head": "Качественный слесарь в Праге, на которого можно положиться",
        "why_lead": "Оказались в ситуации, когда нужна быстрая помощь слесаря, или просто "
                    "хотите совета? Наша мастерская работает для вас 24 часа в сутки.",
        "why": [("clock", "Круглосуточно, по-настоящему",
                 "Диспетчер принимает звонки днём и ночью, в выходные и государственные "
                 "праздники. Консультация по телефону бесплатна."),
                ("users", "Тысячи клиентов в год",
                 "Мастерская работает уже много лет и ежегодно обслуживает тысячи клиентов — "
                 "профессиональная работа без ошибок."),
                ("star", "Самый современный инструмент",
                 "Чтобы гарантировать наивысшее качество услуг, используем только самый "
                 "современный инструмент и оборудование.")],
        "prices": "otevirani-bytu",
        "prose_head": "Замена замка — это ещё не всё",
        "prose": ["Для многих взломщиков защитный цилиндр — <strong>вызов, а не "
                  "препятствие</strong>. Поэтому вместе с заменой цилиндра всегда советуем "
                  "подумать и о защитной фурнитуре, которая бережёт цилиндр от выламывания.",
                  "Даже защитная фурнитура вместе с защитным цилиндром не защитит квартиру "
                  "или дом от воров на 100 %. Поэтому можно установить и <strong>защитный "
                  "засов</strong>, который убережёт дверь от отжима.",
                  "Наши специалисты всё подскажут и помогут защитить объект наилучшим "
                  "образом. Сама замена цилиндра важна, но есть и множество других способов "
                  "лучше обезопасить дом или квартиру."],
        "faq": [("Вы действительно работаете круглосуточно, и в праздники?",
                 "Да. Диспетчер принимает звонки 24 часа в сутки, 7 дней в неделю, включая "
                 "выходные и государственные праздники. Вне рабочего времени (17:00–07:00), "
                 "в выходные и праздники действует наценка."),
                ("Сколько стоит выезд?",
                 "Транспортные расходы — 490 крон в зависимости от расстояния, срочный "
                 "выезд — 300 крон. За пределами Праги +20 крон за километр. Консультация "
                 "по телефону бесплатна."),
                ("Есть ли скидки?",
                 "Да. Постоянным клиентам — 50 %, жертвам преступлений — 30 %. Скидку также "
                 "даём пенсионерам и людям с инвалидностью."),
                ("Как далеко вы выезжаете?",
                 "Покрываем всю Прагу 1–22 и ближайшие окрестности. Выезжаем и дальше, "
                 "тогда дорога за пределами Праги стоит +20 крон за километр."),
                ("Какой у вас опыт?",
                 "В отрасли мы 30 лет и ежегодно обслуживаем тысячи клиентов. В Google "
                 "у нас оценка 4,8 из 887 отзывов.")],
    },
}

SERVICES["ua"] = {
    "otevirani-dveri": {
        "nav": "Відкриття дверей",
        "h1": "Аварійне відкриття дверей у Празі",
        "title": "Відкриття дверей Прага — аварійне відкриття захряслих дверей 24/7",
        "desc": "Захряснули двері або загубили ключі? Відкриємо без пошкоджень, майстер "
                "у вас за 10–40 хвилин. Цілодобово 24/7, від 290 крон.",
        "img": "otevirani-dveri", "img_alt": "Слюсар відкриває захряслі двері",
        "lead": "Захряснули двері або загубили ключі? Розуміємо, що ситуація неприємна — "
                "і ми поруч цілодобово, 24 години на добу, 7 днів на тиждень.",
        "ticks": ["Майстер приїде <b>за 10–40 хвилин</b> у будь-яку точку Праги",
                  "Відкриємо <b>без жодної подряпини</b> — замок залишиться робочим",
                  "Ціну назвемо <b>наперед</b>, без прихованих платежів"],
        "why_head": "Чому Rychlý Zámečník — правильний вибір для відкриття дверей",
        "why_lead": "У критичну хвилину втрачати час не можна. Тому ми готові допомогти "
                    "негайно, 24/7.",
        "why": [("bolt", "Терміновий приїзд",
                 "Наша команда виїжджає одразу й гарантує приїзд за 10–40 хвилин, де б "
                 "ви не були в місті."),
                ("shield", "Дбайливе відкриття",
                 "Майстри використовують сучасний інструмент, щоб відкрити двері без "
                 "пошкоджень. Замок працюватиме далі так, як має."),
                ("coin", "Чесні ціни",
                 "За аварійне відкриття дверей гарантуємо зрозумілу й чесну ціну "
                 "без прихованих платежів.")],
        "prices": "otevirani-bytu",
        "prose_head": "Що робить нас першим вибором при аварійному відкритті",
        "prose": ["Ми спеціалізуємось на кризових ситуаціях, де важлива кожна хвилина. "
                  "Крім технічних навичок і швидкості гарантуємо <strong>людяний "
                  "і чуйний підхід</strong>, який полегшить неприємну мить.",
                  "У нашому оснащенні лише найсучасніші технології аварійного відкриття. "
                  "Завдяки цьому вирішуємо навіть найскладніший випадок швидко й завжди "
                  "без пошкодження замка.",
                  "Наша команда — досвідчені слюсарі, які постійно розширюють знання "
                  "й добре знаються на системах безпеки всіх типів."],
        "faq": [("Як швидко приїде слюсар?",
                 "Прагою гарантуємо приїзд за 10–40 хвилин після дзвінка — залежно від "
                 "того, де зараз найближчий майстер і яка дорожня ситуація. Точнішу "
                 "оцінку назвемо одразу телефоном."),
                ("Чи пошкодите двері або замок?",
                 "У переважній більшості випадків ні. Ми застосовуємо неруйнівні методи, "
                 "після яких замок працює нормально. Якщо конкретний замок так відкрити "
                 "не можна, скажемо про це заздалегідь і домовимось про подальші дії."),
                ("Скільки коштує відкриття дверей?",
                 "Захряслі двері без захисної фурнітури відкриємо від 290 крон, "
                 "із захисною фурнітурою — від 490 крон. Замкнені двері — від 390 крон. "
                 "Підсумкова ціна залежить від типу замка й підтверджується до початку робіт."),
                ("Чи треба доводити, що квартира моя?",
                 "Так. До початку робіт попросимо документ, що посвідчує особу, і документ, "
                 "який підтверджує ваше відношення до житла — договір оренди, витяг "
                 "з кадастру або підтвердження від сусіда чи власника. Це захист і для вас."),
                ("Чи працюєте вночі та у свята?",
                 "Так, диспетчер приймає дзвінки цілодобово, включно з ночами, вихідними "
                 "та державними святами. Поза робочим часом (17:00–07:00), у вихідні "
                 "та свята діє націнка.")],
    },
    "vymena-zamku": {
        "nav": "Заміна замків",
        "h1": "Заміна замків і захисних циліндрів у Празі",
        "title": "Заміна замків Прага — встановлення захисних циліндрів і фурнітури",
        "desc": "Встановлення та заміна замків усіх марок і класів захисту — FAB, EVVA, "
                "MUL-T-LOCK, TOKOZ, ABUS. Консультація безкоштовно, від 290 крон.",
        "img": "vymena-zamku", "img_alt": "Встановлення та заміна захисного замка",
        "lead": "Заміною замків у Празі ми займаємось уже багато років. Встановимо захисні "
                "циліндри та замки будь-якої марки, включно із системою єдиного ключа.",
        "ticks": ["У будь-яку частину Праги дістанемось <b>приблизно за 20 хвилин</b>",
                  "Циліндри <b>всіх класів захисту 1–5</b> від провідних виробників",
                  "<b>Консультація безкоштовно</b> — підберемо рішення за ціною та захистом"],
        "why_head": "Чому Rychlý Zámečník — правильний вибір для заміни замка",
        "why_lead": "Ми не лише швидко й акуратно замінимо замок. Ще й підкажемо, який "
                    "захисний циліндр краще підійде вашим дверям.",
        "why": [("bolt", "Швидкість і повне оснащення",
                 "Слюсарі приїжджають повністю готовими — везуть не тільки обумовлений тип "
                 "замка й циліндра, а й запасні частини на випадок ускладнень."),
                ("clock", "Заміна замка одразу",
                 "Термінові міркування безпеки заслуговують на швидке рішення. Наша "
                 "аварійна служба працює 24/7 — не відкладайте свій захист."),
                ("users", "Індивідуальна консультація безкоштовно",
                 "Розберемо з вами всі варіанти й пояснимо, що означають класи захисту "
                 "та чому важливо правильно поєднувати замок із фурнітурою.")],
        "prices": "zamky",
        "prose_head": "Професійна заміна захисного замка",
        "prose": ["Працюємо із <strong>сертифікованими захисними циліндрами всіх класів "
                  "(1–5)</strong> від провідних світових виробників: FAB, EVVA, MUL-T-LOCK, "
                  "RICHTER, TOKOZ, ABUS. Спеціалізуємось також на замках ATRA, MOTTURA і CISA.",
                  "Для багатьох зловмисників сам собою захисний циліндр — радше виклик, ніж "
                  "перешкода. Тому разом із заміною циліндра завжди радимо подумати "
                  "й про <strong>захисну фурнітуру</strong>, яка береже циліндр від "
                  "виламування, або про захисний засув проти віджиму.",
                  "Усі встановлювані вироби відповідають європейським стандартам якості, "
                  "безпеки та довговічності. Наші майстри мають потрібні сертифікати "
                  "й регулярно проходять навчання."],
        "faq": [("Який замок обрати?",
                 "Залежить від того, що ви захищаєте та які у вас двері. Класи захисту — "
                 "від 1 до 5; для звичайної квартири зазвичай достатньо класу 3 в поєднанні "
                 "із захисною фурнітурою. Консультацію дамо безкоштовно."),
                ("Достатньо замінити лише циліндр чи потрібен весь замок?",
                 "У більшості випадків достатньо замінити циліндр — це дешевше і швидше. "
                 "Весь замок міняють, коли пошкоджений механізм, заклинила засувка або ви "
                 "переходите на інший тип захисту."),
                ("Чи є циліндри в наявності?",
                 "Найпоширеніші типи возимо із собою, тож заміну зазвичай робимо за один "
                 "виїзд. Спеціальні або нестандартні циліндри замовляємо — терміни "
                 "підтвердимо телефоном."),
                ("Чи налаштуєте систему єдиного ключа?",
                 "Так. Систему єдиного ключа — коли один ключ відкриває кілька замків, "
                 "а решта лише вибрані — спроєктуємо та встановимо під ваші задачі. "
                 "Підходить для будинків, офісів і комерційних приміщень."),
                ("Яку даєте гарантію?",
                 "На виконану роботу та використані матеріали даємо два роки гарантії.")],
    },
    "otevirani-aut": {
        "nav": "Відкриття авто",
        "h1": "Аварійне відкриття автомобіля без пошкоджень",
        "title": "Відкриття авто Прага — аварійне відкриття автомобіля без пошкоджень 24/7",
        "desc": "Автомобіль замкнено, а ключі всередині? Відкриємо без розбивання скла "
                "й без пошкодження фарби та електроніки. Цілодобово 24/7, від 590 крон.",
        "img": "otevirani-aut", "img_alt": "Аварійне відкриття автомобіля без ключа",
        "lead": "Автомобіль замкнено, а ключі всередині? Сів акумулятор? Зачинена дитина "
                "чи працює двигун? Вирішуємо — і без розбивання скла.",
        "ticks": ["<b>Скло розбивати не будемо</b> — відкриваємо дбайливими методами",
                  "Збережемо <b>фарбу, двері та електроніку на 100 %</b>",
                  "Приїдемо швидко, служба працює <b>24/7</b>"],
        "why_head": "Чому Rychlý Zámečník — правильний вибір для відкриття авто",
        "why_lead": "У термінових ситуаціях із замкненим автомобілем компромісів не буває. "
                    "Наша швидкість реакції та практичний досвід — ваша гарантія.",
        "why": [("bolt", "Швидкість приїзду",
                 "Завдяки продуманій логістиці та цілодобовій роботі сертифікований майстер "
                 "буде біля вашого автомобіля за 10–40 хвилин після дзвінка."),
                ("shield", "Відкриття без пошкоджень",
                 "Гарантуємо дбайливі методи, що зберігають цілісність фарби, дверей "
                 "і чутливої електроніки. Жодних подальших ремонтів."),
                ("clock", "Слюсар негайно",
                 "Чи потрібен майстер серед ночі, у вихідний або у свято — наша аварійна "
                 "служба завжди готова.")],
        "prices": "auta",
        "prose_head": "Відкриваємо й сучасні авто із сейфовим захистом",
        "prose": ["Ціна відкриття автомобіля залежить насамперед від <strong>року випуску "
                  "та типу захисту</strong>. Машини до 2002 року найпростіші, новіші моделі "
                  "із сейфовим типом замка потребують спеціального інструменту й часу.",
                  "Крім самого відкриття займаємось <strong>заміною замків, замків "
                  "запалювання та демонтажем замків КПП</strong> типу DEFEND LOCK. Усе на "
                  "місці, без евакуації до сервісу.",
                  "Якщо в машині зачинена дитина або тварина, скажіть про це одразу на "
                  "початку розмови — такий виїзд ставимо на початок черги."],
        "faq": [("Чи відкриєте новіше авто з іммобілайзером?",
                 "Так. Відкриття автомобіля та іммобілайзер — різні речі: ми відкриємо "
                 "салон, не втручаючись в електроніку. У машин від 2007 року та із сейфовим "
                 "типом захисту робота складніша, що відображається на ціні."),
                ("Чи будете розбивати скло?",
                 "Ні. Ми використовуємо інструмент, який відкриває автомобіль без "
                 "пошкодження скла, фарби та ущільнювачів. Розбивання скла — крайній захід, "
                 "до якого вдалися б лише на ваше пряме прохання, наприклад при загрозі життю."),
                ("Чи треба доводити, що машина моя?",
                 "Так, перед відкриттям попросимо документ, що посвідчує особу, і документ "
                 "на автомобіль — техпаспорт або договір. Без цього машину не відкриємо."),
                ("Що робити, якщо ключі всередині, а двигун працює?",
                 "Зателефонуйте одразу й скажіть про це — це термінова ситуація, яку "
                 "вирішуємо в пріоритеті. Автомобіль відкриємо без пошкоджень, двигун може "
                 "працювати далі."),
                ("Чи зробите новий ключ, якщо старий загублено?",
                 "Автомобіль відкриємо, можемо замінити замки та замок запалювання. "
                 "Виготовлення й програмування нового чип-ключа в новіших авто треба "
                 "вирішувати в офіційному сервісі — підкажемо телефоном.")],
    },
    "otevirani-trezoru": {
        "nav": "Відкриття сейфів",
        "h1": "Відкриття та обслуговування сейфів",
        "title": "Відкриття сейфів Прага — аварійне відкриття сейфа, сервіс і ремонт",
        "desc": "Забули код або загубили ключ від сейфа? Відкриваємо електронні та механічні "
                "сейфи з 1990 року — SAFEMETAL, ROTTNER, KOVONA та інші.",
        "img": "otevirani-trezoru", "img_alt": "Слюсар відкриває сейф",
        "lead": "Потрібно потрапити в сейф, але немає ключа чи коду? Сіла батарейка? Ми "
                "фахівці з аварійного відкриття сейфів із досвідом від 1990 року.",
        "ticks": ["Відкриваємо <b>електронні та механічні кодові сейфи</b>",
                  "Найдбайливіші методи — сейфом можна <b>користуватися далі</b>",
                  "Навіть потрібне невелике втручання <b>професійно заробимо</b>"],
        "why_head": "Чому Rychlý Zámečník — правильний вибір для відкриття сейфів",
        "why_lead": "Ми не лише швидко відкриємо. Ще й підкажемо, який сейфовий замок "
                    "найкраще підійде вашому сейфу.",
        "why": [("bolt", "Блискавичний приїзд",
                 "Команда виїжджає одразу після дзвінка й гарантує приїзд по всьому місту "
                 "в межах 10–40 хвилин."),
                ("shield", "Неруйнівне відкриття",
                 "Сейф відкриваємо методами, що гарантують нульові пошкодження. Механізм "
                 "після роботи залишиться повністю справним."),
                ("coin", "Без сюрпризів, чесна ціна",
                 "Відкриття сейфа саме собою достатньо нервове. Тому гарантуємо прозору "
                 "ціну одразу — жодних «сюрпризів» у рахунку.")],
        "prices": "otevirani-bytu",
        "prose_head": "З якими сейфами ми працюємо",
        "prose": ["Відкриваємо сейфи марок <strong>SAFEMETAL, ROTTNER, KOVONA, T-SAFE, "
                  "ASIST, BULDOK</strong> та багатьох інших — механічні ключові, кодові "
                  "й електронні.",
                  "Найчастіші причини звернень: забутий код або комбінація, загублений чи "
                  "зламаний ключ, <strong>сіла батарейка електронного замка</strong> "
                  "та несправність механіки.",
                  "Крім відкриття забезпечуємо ремонт і повне обслуговування сейфів, включно "
                  "із заміною сейфового замка. Ціна визначається типом сейфа, тому її завжди "
                  "обговорюємо індивідуально."],
        "faq": [("Чи відкриєте сейф, не знищивши його?",
                 "Це наша мета, і в більшості випадків це вдається. Обираємо найдбайливіший "
                 "метод, щоб сейфом можна було користуватися далі. Якщо свердління "
                 "неминуче, отвір професійно заробимо спеціальним складом."),
                ("Я забув код. Чи можна щось зробити?",
                 "Так, це одна з найчастіших причин звернень. І для електронних, і для "
                 "механічних кодових сейфів у нас є способи потрапити всередину, після чого "
                 "налаштуємо вам новий код."),
                ("Скільки коштує відкриття сейфа?",
                 "Ціна залежить від типу сейфа та складності, тому вказується як «за типом». "
                 "Заклинілий сейфовий замок у дверях відкриваємо від 1 190 крон, замкнений "
                 "сейфовий замок — від 1 990 крон. Конкретну оцінку дамо телефоном."),
                ("Чи заміните сейфовий замок?",
                 "Так, виконуємо ремонт і повне обслуговування сейфів, включно із заміною "
                 "замка, і допоможемо обрати відповідний тип."),
                ("Що треба підготувати?",
                 "Документ, що посвідчує особу, і документ про те, що сейф належить вам або "
                 "вашій компанії — чек, рахунок, страховий договір. Для корпоративних сейфів "
                 "потрібна згода уповноваженої особи.")],
    },
    "oprava-dveri": {
        "nav": "Ремонт дверей",
        "h1": "Ремонт дверей після зламу",
        "title": "Ремонт дверей після зламу, Прага — негайний виїзд і захист",
        "desc": "Злам — це шок. Швидко повернемо вас до безпеки: відремонтуємо двері "
                "та замки й запропонуємо надійний захист. Цілодобово 24/7, від 390 крон.",
        "img": "otevirani-zamku", "img_alt": "Ремонт дверей і замка після зламу",
        "lead": "Злам — це шок. Ми забезпечимо швидке повернення до безпеки: приїдемо, "
                "професійно відремонтуємо двері та замки й одразу запропонуємо, як "
                "захистити житло на майбутнє.",
        "ticks": ["<b>Негайний виїзд</b> — двері та замки відремонтуємо на місці",
                  "<b>Надійний захист</b> — запропонуємо рішення для квартири й приміщення",
                  "Знижка <b>30 %</b> жертвам злочинів"],
        "why_head": "Чому Rychlý Zámečník — правильний вибір для ремонту дверей",
        "why_lead": "У критичну хвилину час дорожчий за все. Тому слюсар доступний вам "
                    "цілодобово, 24 години на добу, 7 днів на тиждень.",
        "why": [("bolt", "Приїзд за 30 хвилин",
                 "Наші слюсарі розподілені по всьому місту, щоб швидкість була максимальною. "
                 "При кризових виїздах гарантуємо приїзд за 10–30 хвилин."),
                ("clock", "Телефонуйте будь-коли",
                 "Ми доступні безперервно — ваша впевненість у швидкій і професійній "
                 "допомозі будь-якої пори дня й ночі."),
                ("coin", "Чесні ціни",
                 "Злам — уже достатній стрес. Жодних хитрощів і прихованих платежів: наша "
                 "обіцянка прозорості діє без винятків.")],
        "prices": "zamky",
        "prose_head": "Що робити, якщо до вас проникли",
        "prose": ["<strong>Спершу викличте поліцію</strong> і за можливості нічого не "
                  "переміщуйте до її приїзду — і заради огляду місця, і заради страхової. "
                  "Сфотографуйте стан дверей і замка, це знадобиться при заяві про "
                  "страховий випадок.",
                  "Тільки потім телефонуйте нам. Приїдемо, <strong>приведемо двері до "
                  "робочого стану й замінимо пошкоджені замки</strong>, щоб ви могли "
                  "безпечно замкнути житло того самого дня.",
                  "Одразу розберемо, яким шляхом проник зловмисник, і запропонуємо, що "
                  "посилити — захисний циліндр із фурнітурою, додатковий замок або засув "
                  "проти віджиму. <strong>Жертвам злочинів даємо знижку 30 %.</strong>"],
        "faq": [("Приїдете одразу чи треба записуватись?",
                 "Після зламу виїжджаємо негайно — це кризовий виклик. Гарантуємо приїзд "
                 "за 10–30 хвилин після дзвінка."),
                ("Чи оплатить це страхова?",
                 "У більшості випадків так, якщо у вас оформлене страхування житла. Видамо "
                 "документ із переліком робіт і матеріалів для страхової. Будь ласка, "
                 "сфотографуйте стан дверей до ремонту."),
                ("Чи можна відремонтувати початкові двері, чи потрібні нові?",
                 "Залежить від масштабу пошкоджень. Часто достатньо відремонтувати коробку, "
                 "замінити замок і фурнітуру. Якщо двері виламані настільки, що безпеку "
                 "гарантувати не можна, скажемо прямо."),
                ("Чи підкажете, як захиститися наступного разу?",
                 "Так, це частина роботи. Розберемо, яким шляхом проник зловмисник, "
                 "і запропонуємо конкретні заходи — захисний циліндр із фурнітурою, "
                 "додатковий замок або захисний засув."),
                ("Чи діє знижка жертвам злочинів автоматично?",
                 "Застосуємо її на місці — достатньо сказати, що це виїзд після зламу. "
                 "Бажано мати під рукою номер справи з поліції.")],
    },
    "zamecnicka-pohotovost": {
        "nav": "Аварійна служба",
        "h1": "Аварійна слюсарна служба в Празі — цілодобово 24/7",
        "title": "Аварійна слюсарна служба Прага — слюсар 24 години на добу",
        "desc": "Найшвидша аварійна слюсарна служба в Празі за розумні гроші. Відкриття "
                "дверей, авто та сейфів, заміна замків. Цілодобово 24/7, 30 років досвіду.",
        "img": "vyjezd-den", "img_alt": "Машина аварійної слюсарної служби на виїзді",
        "lead": "Слюсарна майстерня з давньою історією. Якісна аварійна служба за розумні "
                "гроші — будь-якого дня й будь-якої години.",
        "ticks": ["Відкриття <b>захряслих і замкнених дверей</b> та аварійне відкриття замків",
                  "Відкриття <b>авто без ключа</b>, без жодних пошкоджень",
                  "Відкриття, ремонт і <b>повне обслуговування сейфів</b>",
                  "Встановлення та заміна <b>всіх типів замків</b>, циліндрів і фурнітури",
                  "Встановлення захисних <b>засувів, додаткових замків і ґрат</b>",
                  "Ремонт дверей після зламу та <b>проєкти захисту об'єкта</b>"],
        "why_head": "Якісний слюсар у Празі, на якого можна покластися",
        "why_lead": "Опинилися в ситуації, коли потрібна швидка допомога слюсаря, чи просто "
                    "хочете поради? Наша майстерня працює для вас 24 години на добу.",
        "why": [("clock", "Цілодобово, по-справжньому",
                 "Диспетчер приймає дзвінки вдень і вночі, у вихідні та державні свята. "
                 "Консультація телефоном безкоштовна."),
                ("users", "Тисячі клієнтів на рік",
                 "Майстерня працює вже багато років і щороку обслуговує тисячі клієнтів — "
                 "професійна робота без помилок."),
                ("star", "Найсучасніший інструмент",
                 "Щоб гарантувати найвищу якість послуг, використовуємо лише найсучасніший "
                 "інструмент і обладнання.")],
        "prices": "otevirani-bytu",
        "prose_head": "Заміна замка — це ще не все",
        "prose": ["Для багатьох зловмисників захисний циліндр — <strong>виклик, а не "
                  "перешкода</strong>. Тому разом із заміною циліндра завжди радимо подумати "
                  "й про захисну фурнітуру, яка береже циліндр від виламування.",
                  "Навіть захисна фурнітура разом із захисним циліндром не захистить "
                  "квартиру чи будинок від злодіїв на 100 %. Тому можна встановити й "
                  "<strong>захисний засув</strong>, який убереже двері від віджиму.",
                  "Наші фахівці все підкажуть і допоможуть захистити об'єкт якнайкраще. "
                  "Сама заміна циліндра важлива, але є й багато інших способів краще "
                  "убезпечити будинок або квартиру."],
        "faq": [("Ви справді працюєте цілодобово, і у свята?",
                 "Так. Диспетчер приймає дзвінки 24 години на добу, 7 днів на тиждень, "
                 "включно з вихідними та державними святами. Поза робочим часом "
                 "(17:00–07:00), у вихідні та свята діє націнка."),
                ("Скільки коштує виїзд?",
                 "Транспортні витрати — 490 крон залежно від відстані, терміновий виїзд — "
                 "300 крон. За межами Праги +20 крон за кілометр. Консультація телефоном "
                 "безкоштовна."),
                ("Чи є знижки?",
                 "Так. Постійним клієнтам — 50 %, жертвам злочинів — 30 %. Знижку також "
                 "даємо пенсіонерам і людям з інвалідністю."),
                ("Як далеко ви виїжджаєте?",
                 "Покриваємо всю Прагу 1–22 та найближчі околиці. Виїжджаємо й далі, тоді "
                 "дорога за межами Праги коштує +20 крон за кілометр."),
                ("Який у вас досвід?",
                 "У галузі ми 30 років і щороку обслуговуємо тисячі клієнтів. У Google "
                 "у нас оцінка 4,8 з 887 відгуків.")],
    },
}


# --------------------------------------------------------------------------- #
# Zásady ochrany osobních údajů v jazykových mutacích
# --------------------------------------------------------------------------- #
PRIVACY_I18N = {
    "en": {
        "title": "Privacy policy",
        "meta_title": "Privacy policy | Rychlý Zámečník",
        "desc": "How we handle personal data and cookies on rychly-zamecnik.cz.",
        "intro": "This policy describes what data we process about you, why we do it and "
                 "what rights you have towards us.",
        "body": [
            ("h", "Who the controller is"),
            ("p", "The controller of personal data is <strong>Rychlý Zámečník</strong>, "
                  "company ID 075 25 711, e-mail "
                  "<a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>, "
                  "telephone <a href=\"tel:+420723965990\">+420 723 965 990</a>."),
            ("h", "What data we process"),
            ("ul", ["<strong>Call-out details</strong> — name, phone number and the address "
                    "of the job. Without them we cannot come to you.",
                    "<strong>E-mail correspondence</strong> — if you write to us, we process "
                    "the content of your message and your e-mail address.",
                    "<strong>Technical data</strong> — if you give consent, we collect "
                    "anonymised traffic statistics."]),
            ("h", "Why we process it"),
            ("ul", ["To carry out the service you ordered (performance of a contract).",
                    "To meet legal obligations — mainly issuing and archiving tax documents.",
                    "To improve the website (only on the basis of your consent)."]),
            ("h", "How long we keep it"),
            ("p", "Call-out details are kept for as long as needed to complete the job and "
                  "then for the statutory period for archiving tax documents. Traffic "
                  "statistics are kept for a maximum of 14 months."),
            ("h", "Who we share it with"),
            ("p", "We do not pass personal data to third parties except where required by "
                  "law, or where it is necessary to complete the job — for example to an "
                  "insurer if the work is covered by your home insurance."),
            ("h", "Cookies"),
            ("p", "By default the site uses only <strong>necessary cookies</strong>, without "
                  "which it would not work. These do not require consent. Analytics cookies "
                  "are only deployed once you have given consent in the cookie bar."),
            ("p", "You can withdraw consent at any time — the <strong>Cookie settings</strong> "
                  "link in the footer reopens the bar and overwrites your choice."),
            ("h", "Your rights"),
            ("ul", ["The right of access to your data.",
                    "The right to have inaccurate data corrected.",
                    "The right to erasure where there is no legal ground for processing.",
                    "The right to restrict processing and the right to object.",
                    "The right to data portability.",
                    "The right to lodge a complaint with the Office for Personal Data "
                    "Protection."]),
            ("p", "You can exercise them by e-mail at "
                  "<a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>."),
        ],
        "note": "This document is provided as a starting point. Before the site goes live, "
                "have it reviewed by someone who can take responsibility for its wording.",
    },
    "ru": {
        "title": "Политика конфиденциальности",
        "meta_title": "Политика конфиденциальности | Rychlý Zámečník",
        "desc": "Как мы обращаемся с персональными данными и файлами cookie "
                "на сайте rychly-zamecnik.cz.",
        "intro": "Эта политика описывает, какие данные о вас мы обрабатываем, зачем это "
                 "делаем и какие права вы имеете по отношению к нам.",
        "body": [
            ("h", "Кто является администратором"),
            ("p", "Администратор персональных данных — <strong>Rychlý Zámečník</strong>, "
                  "IČO 075 25 711, e-mail "
                  "<a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>, "
                  "телефон <a href=\"tel:+420723965990\">+420 723 965 990</a>."),
            ("h", "Какие данные мы обрабатываем"),
            ("ul", ["<strong>Данные заявки</strong> — имя, телефон, адрес места работы. "
                    "Без них мы не сможем приехать.",
                    "<strong>Данные из переписки</strong> — если вы нам напишете, "
                    "мы обрабатываем содержание сообщения и ваш адрес электронной почты.",
                    "<strong>Технические данные</strong> — при наличии вашего согласия "
                    "собираем анонимизированную статистику посещаемости."]),
            ("h", "Зачем мы их обрабатываем"),
            ("ul", ["Чтобы выполнить заказанную услугу (исполнение договора).",
                    "Чтобы выполнить требования закона — прежде всего выставление "
                    "и хранение налоговых документов.",
                    "Чтобы улучшать сайт (только на основании вашего согласия)."]),
            ("h", "Как долго мы их храним"),
            ("p", "Данные заявки храним в течение времени, необходимого для выполнения "
                  "заказа, и затем в течение установленного законом срока хранения "
                  "налоговых документов. Статистика посещаемости хранится не более "
                  "14 месяцев."),
            ("h", "Кому мы их передаём"),
            ("p", "Персональные данные не передаём третьим лицам, за исключением случаев, "
                  "предусмотренных законом, или когда это необходимо для выполнения заказа — "
                  "например страховой компании, если работы оплачиваются из страхования жилья."),
            ("h", "Файлы cookie"),
            ("p", "По умолчанию сайт использует только <strong>необходимые файлы "
                  "cookie</strong>, без которых он не работал бы. Они не требуют согласия. "
                  "Аналитические cookie подключаем только после того, как вы дадите согласие "
                  "в баннере."),
            ("p", "Согласие можно отозвать в любой момент — ссылка <strong>Настройки cookie</strong> "
                  "в подвале сайта снова откроет баннер и перезапишет ваш выбор."),
            ("h", "Ваши права"),
            ("ul", ["Право на доступ к своим данным.",
                    "Право на исправление неточных данных.",
                    "Право на удаление, если для обработки нет законного основания.",
                    "Право на ограничение обработки и право на возражение.",
                    "Право на переносимость данных.",
                    "Право подать жалобу в Управление по защите персональных данных."]),
            ("p", "Реализовать их можно по электронной почте "
                  "<a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>."),
        ],
        "note": "Этот документ подготовлен как основа. Перед запуском сайта его следует дать "
                "на проверку тому, кто может нести ответственность за его формулировки.",
    },
    "ua": {
        "title": "Політика конфіденційності",
        "meta_title": "Політика конфіденційності | Rychlý Zámečník",
        "desc": "Як ми поводимося з персональними даними та файлами cookie "
                "на сайті rychly-zamecnik.cz.",
        "intro": "Ця політика описує, які дані про вас ми обробляємо, навіщо це робимо "
                 "та які права ви маєте щодо нас.",
        "body": [
            ("h", "Хто є розпорядником"),
            ("p", "Розпорядник персональних даних — <strong>Rychlý Zámečník</strong>, "
                  "IČO 075 25 711, e-mail "
                  "<a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>, "
                  "телефон <a href=\"tel:+420723965990\">+420 723 965 990</a>."),
            ("h", "Які дані ми обробляємо"),
            ("ul", ["<strong>Дані заявки</strong> — ім'я, телефон, адреса місця роботи. "
                    "Без них ми не зможемо приїхати.",
                    "<strong>Дані з листування</strong> — якщо ви нам напишете, ми обробляємо "
                    "зміст повідомлення та вашу адресу електронної пошти.",
                    "<strong>Технічні дані</strong> — за наявності вашої згоди збираємо "
                    "анонімізовану статистику відвідуваності."]),
            ("h", "Навіщо ми їх обробляємо"),
            ("ul", ["Щоб виконати замовлену послугу (виконання договору).",
                    "Щоб виконати вимоги закону — насамперед виставлення та зберігання "
                    "податкових документів.",
                    "Щоб покращувати сайт (лише на підставі вашої згоди)."]),
            ("h", "Як довго ми їх зберігаємо"),
            ("p", "Дані заявки зберігаємо протягом часу, потрібного для виконання "
                  "замовлення, і далі протягом установленого законом строку зберігання "
                  "податкових документів. Статистика відвідуваності зберігається не більше "
                  "14 місяців."),
            ("h", "Кому ми їх передаємо"),
            ("p", "Персональні дані не передаємо третім особам, окрім випадків, передбачених "
                  "законом, або коли це потрібно для виконання замовлення — наприклад "
                  "страховій компанії, якщо роботи оплачуються зі страхування житла."),
            ("h", "Файли cookie"),
            ("p", "За замовчуванням сайт використовує лише <strong>необхідні файли "
                  "cookie</strong>, без яких він не працював би. Вони не потребують згоди. "
                  "Аналітичні cookie підключаємо лише після того, як ви дасте згоду "
                  "в банері."),
            ("p", "Згоду можна відкликати будь-коли — посилання <strong>Налаштування cookie</strong> "
                  "у підвалі сайту знову відкриє банер і перезапише ваш вибір."),
            ("h", "Ваші права"),
            ("ul", ["Право на доступ до своїх даних.",
                    "Право на виправлення неточних даних.",
                    "Право на видалення, якщо для обробки немає законної підстави.",
                    "Право на обмеження обробки та право заперечувати.",
                    "Право на перенесення даних.",
                    "Право подати скаргу до Управління із захисту персональних даних."]),
            ("p", "Реалізувати їх можна електронною поштою "
                  "<a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>."),
        ],
        "note": "Цей документ підготовлено як основу. Перед запуском сайту його варто дати "
                "на перевірку тому, хто може нести відповідальність за його формулювання.",
    },
}


# --------------------------------------------------------------------------- #
# Obchodní podmínky v jazykových mutacích
# --------------------------------------------------------------------------- #
TERMS_I18N = {
    "en": {
        "title": "Terms of service",
        "meta_title": "Terms of service | Rychlý Zámečník",
        "desc": "Terms for our locksmith services — how an order is made, how the price "
                "is set, warranty, complaints and withdrawal from the contract.",
        "intro": "So that it is clear where we stand from the start. What we agree on "
                 "the phone holds — this document just writes it down.",
        "body": [
            ("h", "Who provides the services"),
            ("p", "Services are provided by <strong>Rychlý Zámečník</strong>, company ID "
                  "075 25 711, e-mail "
                  "<a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>, "
                  "telephone <a href=\"tel:+420723965990\">+420 723 965 990</a> "
                  "(the &bdquo;<strong>contractor</strong>&ldquo;)."),

            ("h", "What these terms cover"),
            ("p", "They apply to locksmith work carried out at the customer's location — "
                  "emergency opening of doors, cars and safes, replacement and repair of "
                  "locks and cylinders, door repairs and security work."),

            ("h", "How an order is made"),
            ("p", "An order is placed by phone or e-mail. Before the call-out the contractor "
                  "states an <strong>indicative price</strong> and an approximate arrival "
                  "time. The contract is concluded the moment the customer confirms the "
                  "call-out."),
            ("p", "Prices shown on this website are indicative, in the &bdquo;from&ldquo; "
                  "format. The final price depends on the type of lock, the extent of the "
                  "damage and the material used."),

            ("h", "The price and its confirmation"),
            ("ul", ["The technician assesses the job on site and states the "
                    "<strong>final price before any work begins</strong>.",
                    "Work starts only after the customer approves that price.",
                    "If it turns out during the job that more work is needed, the "
                    "technician stops and agrees a new price."]),
            ("p", "The customer is not obliged to order the work if the stated price does "
                  "not suit them. In that case only the call-out fee per the price list "
                  "is payable."),

            ("h", "Call-out fee and surcharges"),
            ("p", "A call-out fee per the price list is added to the price of the work. "
                  "Surcharges for night hours, weekends and public holidays are listed in "
                  "the price list and the technician points them out when confirming the "
                  "price. Discounts for seniors and disability card holders apply on "
                  "presentation of the document."),

            ("h", "Proof of entitlement"),
            ("p", "Before a door, vehicle or safe is opened, the customer must "
                  "<strong>prove they are entitled to have it opened</strong> — by an ID "
                  "document showing the address, a tenancy agreement, a vehicle "
                  "registration certificate or other credible means."),
            ("p", "Without that proof the technician will not carry out the work. This is "
                  "not a formality — it protects the owner as much as the contractor. The "
                  "call-out fee remains payable in such a case."),

            ("h", "Payment"),
            ("p", "Payment is due once the work is finished, in cash or by bank transfer. "
                  "A receipt is issued for every job. On request the contractor will issue "
                  "an invoice to a company or documentation for an insurer."),

            ("h", "Warranty"),
            ("p", "The contractor provides a <strong>24-month</strong> warranty on the work "
                  "carried out and the material supplied, from the date of handover. The "
                  "warranty does not cover defects caused by normal wear, forced damage, "
                  "unqualified interference by a third party or improper use."),

            ("h", "Complaints"),
            ("p", "Make a complaint by phone or e-mail, ideally with a description of the "
                  "defect and a photograph. The contractor will settle it "
                  "<strong>within 30 days at the latest</strong> unless a longer period is "
                  "agreed with the customer."),
            ("p", "If the complaint is justified, the contractor removes the defect free of "
                  "charge. Where that is not possible, they provide a reasonable discount "
                  "or refund the amount paid."),

            ("h", "Withdrawal from the contract"),
            ("p", "For contracts concluded at a distance or off business premises, a consumer "
                  "has the right to withdraw within 14 days. For an <strong>urgent repair the "
                  "consumer has expressly requested</strong>, that right lapses on performance "
                  "of the service under the Czech Civil Code — which is the typical case with "
                  "emergency opening."),
            ("p", "An order can be cancelled free of charge until the technician has set off. "
                  "Once they are on the way, the call-out fee is payable."),

            ("h", "Liability for damage"),
            ("p", "The contractor is liable for damage demonstrably caused while carrying out "
                  "the work. With emergency opening, <strong>damage to the lock may be "
                  "unavoidable</strong> — the technician points this out in advance and agrees "
                  "both the procedure and the price of any replacement."),

            ("h", "Dispute resolution"),
            ("p", "Disputes are settled primarily by agreement. A consumer has the right to "
                  "out-of-court resolution before the <strong>Czech Trade Inspection "
                  "Authority</strong> (<a href=\"https://adr.coi.cz\" rel=\"noopener\">adr.coi.cz</a>)."),

            ("h", "Effective date"),
            ("p", "These terms are effective from 1 January 2026. Orders already placed are "
                  "governed by the wording effective at the time of the order."),
        ],
        "note": "This document is prepared as a starting point, not as finished legal text. "
                "Before the website starts using it, have it checked by someone who can take "
                "responsibility for its wording — especially the periods, warranty and "
                "withdrawal.",
    },

    "ru": {
        "title": "Условия оказания услуг",
        "meta_title": "Условия оказания услуг | Rychlý Zámečník",
        "desc": "Условия оказания слесарных услуг — как оформляется заказ, как "
                "определяется цена, гарантия, рекламации и отказ от договора.",
        "intro": "Чтобы заранее было понятно, на чём мы договорились. Что обсудим по "
                 "телефону, то и действует — этот документ лишь фиксирует это письменно.",
        "body": [
            ("h", "Кто оказывает услуги"),
            ("p", "Услуги оказывает <strong>Rychlý Zámečník</strong>, ИНН 075 25 711, "
                  "эл. почта "
                  "<a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>, "
                  "телефон <a href=\"tel:+420723965990\">+420 723 965 990</a> "
                  "(далее «<strong>исполнитель</strong>»)."),

            ("h", "К чему относятся условия"),
            ("p", "Они распространяются на слесарные работы, выполняемые на месте у "
                  "заказчика, — аварийное вскрытие дверей, автомобилей и сейфов, замену "
                  "и ремонт замков и личинок, ремонт дверей и работы по безопасности."),

            ("h", "Как оформляется заказ"),
            ("p", "Заказ оформляется по телефону или электронной почте. Перед выездом "
                  "исполнитель сообщает <strong>ориентировочную цену</strong> и примерное "
                  "время прибытия. Договор считается заключённым в момент, когда заказчик "
                  "подтверждает выезд."),
            ("p", "Цены на сайте ориентировочные, в формате «от». Итоговая цена зависит "
                  "от типа замка, степени повреждения и использованных материалов."),

            ("h", "Цена и её подтверждение"),
            ("ul", ["Техник на месте оценивает объём работ и сообщает "
                    "<strong>итоговую цену ещё до начала работ</strong>.",
                    "Работы начинаются только после согласования этой цены заказчиком.",
                    "Если в ходе работ выяснится, что нужно сделать больше, техник "
                    "приостанавливает работу и согласовывает цену заново."]),
            ("p", "Заказчик не обязан заказывать работу, если названная цена его не "
                  "устраивает. В этом случае оплачивается только выезд по прайс-листу."),

            ("h", "Выезд и надбавки"),
            ("p", "К стоимости работ добавляется плата за выезд по прайс-листу. Надбавки "
                  "за ночные часы, выходные и праздничные дни указаны в прайс-листе, и "
                  "техник сообщает о них при подтверждении цены. Скидки пенсионерам и "
                  "людям с инвалидностью предоставляются по предъявлении документа."),

            ("h", "Подтверждение права на вскрытие"),
            ("p", "Перед вскрытием двери, автомобиля или сейфа заказчик обязан "
                  "<strong>подтвердить своё право на это</strong> — документом, "
                  "удостоверяющим личность с указанием адреса, договором найма, "
                  "техническим паспортом на автомобиль или иным убедительным способом."),
            ("p", "Без такого подтверждения техник работу не выполнит. Это не формальность — "
                  "так защищён и владелец, и исполнитель. Выезд в таком случае оплачивается."),

            ("h", "Оплата"),
            ("p", "Оплата производится после завершения работ, наличными или переводом. "
                  "На каждый заказ выдаётся документ. По запросу исполнитель выставит "
                  "счёт на компанию или подготовит документы для страховой."),

            ("h", "Гарантия"),
            ("p", "На выполненные работы и поставленные материалы исполнитель предоставляет "
                  "гарантию <strong>24 месяца</strong> со дня передачи. Гарантия не "
                  "распространяется на дефекты, вызванные обычным износом, механическим "
                  "повреждением, неквалифицированным вмешательством третьих лиц или "
                  "ненадлежащей эксплуатацией."),

            ("h", "Рекламации"),
            ("p", "Рекламацию направьте по телефону или электронной почте, желательно с "
                  "описанием дефекта и фотографией. Исполнитель рассмотрит её "
                  "<strong>не позднее 30 дней</strong> с момента обращения, если с "
                  "заказчиком не согласован более длительный срок."),
            ("p", "Если рекламация обоснована, исполнитель устраняет дефект бесплатно. "
                  "Если это невозможно, предоставляется соразмерная скидка или "
                  "возвращается уплаченная сумма."),

            ("h", "Отказ от договора"),
            ("p", "При договорах, заключённых дистанционно или вне торговых помещений, "
                  "потребитель вправе отказаться в течение 14 дней. При "
                  "<strong>неотложном ремонте, о котором он сам прямо попросил</strong>, "
                  "это право по Гражданскому кодексу ЧР прекращается с выполнением "
                  "услуги — что типично для аварийного вскрытия."),
            ("p", "Заказ можно бесплатно отменить, пока техник не выехал. Если он уже в "
                  "пути, оплачивается выезд."),

            ("h", "Ответственность за ущерб"),
            ("p", "Исполнитель отвечает за ущерб, доказуемо причинённый при выполнении "
                  "работ. При аварийном вскрытии <strong>повреждение замка может быть "
                  "неизбежным</strong> — техник предупреждает об этом заранее и "
                  "согласовывает порядок действий и стоимость возможной замены."),

            ("h", "Разрешение споров"),
            ("p", "Споры решаются прежде всего соглашением сторон. Потребитель вправе "
                  "обратиться за внесудебным разрешением спора в <strong>Чешскую торговую "
                  "инспекцию</strong> (<a href=\"https://adr.coi.cz\" rel=\"noopener\">adr.coi.cz</a>)."),

            ("h", "Вступление в силу"),
            ("p", "Условия действуют с 1 января 2026 года. К уже оформленным заказам "
                  "применяется редакция, действовавшая на момент заказа."),
        ],
        "note": "Этот документ подготовлен как основа, а не как готовый юридический текст. "
                "Прежде чем сайт начнёт его использовать, дайте его на проверку тому, кто "
                "может нести ответственность за формулировки — прежде всего сроки, гарантию "
                "и отказ от договора.",
    },

    "ua": {
        "title": "Умови надання послуг",
        "meta_title": "Умови надання послуг | Rychlý Zámečník",
        "desc": "Умови надання слюсарних послуг — як оформлюється замовлення, як "
                "визначається ціна, гарантія, рекламації та відмова від договору.",
        "intro": "Щоб заздалегідь було зрозуміло, про що ми домовилися. Що обговоримо "
                 "телефоном, те й діє — цей документ лише фіксує це письмово.",
        "body": [
            ("h", "Хто надає послуги"),
            ("p", "Послуги надає <strong>Rychlý Zámečník</strong>, ІПН 075 25 711, "
                  "ел. пошта "
                  "<a href=\"mailto:info@rychly-zamecnik.cz\">info@rychly-zamecnik.cz</a>, "
                  "телефон <a href=\"tel:+420723965990\">+420 723 965 990</a> "
                  "(далі «<strong>виконавець</strong>»)."),

            ("h", "Чого стосуються умови"),
            ("p", "Вони поширюються на слюсарні роботи, що виконуються на місці в "
                  "замовника, — аварійне відкриття дверей, автомобілів і сейфів, заміну "
                  "та ремонт замків і личинок, ремонт дверей і роботи із безпеки."),

            ("h", "Як оформлюється замовлення"),
            ("p", "Замовлення оформлюється телефоном або електронною поштою. Перед виїздом "
                  "виконавець повідомляє <strong>орієнтовну ціну</strong> та приблизний час "
                  "прибуття. Договір вважається укладеним у момент, коли замовник "
                  "підтверджує виїзд."),
            ("p", "Ціни на сайті орієнтовні, у форматі «від». Підсумкова ціна залежить від "
                  "типу замка, ступеня пошкодження та використаних матеріалів."),

            ("h", "Ціна та її підтвердження"),
            ("ul", ["Технік на місці оцінює обсяг робіт і повідомляє "
                    "<strong>підсумкову ціну ще до початку робіт</strong>.",
                    "Роботи починаються лише після погодження цієї ціни замовником.",
                    "Якщо під час робіт з'ясується, що потрібно зробити більше, технік "
                    "припиняє роботу й погоджує ціну заново."]),
            ("p", "Замовник не зобов'язаний замовляти роботу, якщо названа ціна його не "
                  "влаштовує. У такому разі оплачується лише виїзд згідно з прайс-листом."),

            ("h", "Виїзд і надбавки"),
            ("p", "До вартості робіт додається плата за виїзд згідно з прайс-листом. "
                  "Надбавки за нічні години, вихідні та святкові дні вказані в прайс-листі, "
                  "і технік повідомляє про них під час підтвердження ціни. Знижки "
                  "пенсіонерам і людям з інвалідністю надаються після пред'явлення документа."),

            ("h", "Підтвердження права на відкриття"),
            ("p", "Перед відкриттям дверей, автомобіля чи сейфа замовник зобов'язаний "
                  "<strong>підтвердити своє право на це</strong> — документом, що посвідчує "
                  "особу із зазначенням адреси, договором найму, технічним паспортом на "
                  "автомобіль або іншим переконливим способом."),
            ("p", "Без такого підтвердження технік роботу не виконає. Це не формальність — "
                  "так захищено і власника, і виконавця. Виїзд у такому разі оплачується."),

            ("h", "Оплата"),
            ("p", "Оплата здійснюється після завершення робіт, готівкою або переказом. "
                  "На кожне замовлення видається документ. За запитом виконавець виставить "
                  "рахунок на компанію або підготує документи для страхової."),

            ("h", "Гарантія"),
            ("p", "На виконані роботи та поставлені матеріали виконавець надає гарантію "
                  "<strong>24 місяці</strong> від дня передання. Гарантія не поширюється на "
                  "дефекти, спричинені звичайним зношенням, механічним пошкодженням, "
                  "некваліфікованим втручанням третіх осіб або неналежною експлуатацією."),

            ("h", "Рекламації"),
            ("p", "Рекламацію надішліть телефоном або електронною поштою, бажано з описом "
                  "дефекту та фотографією. Виконавець розгляне її <strong>не пізніше ніж "
                  "за 30 днів</strong> від моменту звернення, якщо із замовником не "
                  "погоджено довший строк."),
            ("p", "Якщо рекламація обґрунтована, виконавець усуває дефект безкоштовно. "
                  "Якщо це неможливо, надається співмірна знижка або повертається "
                  "сплачена сума."),

            ("h", "Відмова від договору"),
            ("p", "За договорами, укладеними дистанційно або поза торговельними "
                  "приміщеннями, споживач має право відмовитися протягом 14 днів. За "
                  "<strong>невідкладного ремонту, про який він сам прямо попросив</strong>, "
                  "це право згідно з Цивільним кодексом ЧР припиняється з виконанням "
                  "послуги — що є типовим для аварійного відкриття."),
            ("p", "Замовлення можна безкоштовно скасувати, доки технік не виїхав. Якщо він "
                  "уже в дорозі, оплачується виїзд."),

            ("h", "Відповідальність за шкоду"),
            ("p", "Виконавець відповідає за шкоду, доказово завдану під час виконання робіт. "
                  "За аварійного відкриття <strong>пошкодження замка може бути "
                  "неминучим</strong> — технік попереджає про це заздалегідь і погоджує "
                  "як порядок дій, так і вартість можливої заміни."),

            ("h", "Вирішення спорів"),
            ("p", "Спори вирішуються насамперед за домовленістю. Споживач має право на "
                  "позасудове вирішення спору в <strong>Чеській торговій інспекції</strong> "
                  "(<a href=\"https://adr.coi.cz\" rel=\"noopener\">adr.coi.cz</a>)."),

            ("h", "Набрання чинності"),
            ("p", "Умови діють з 1 січня 2026 року. До вже оформлених замовлень "
                  "застосовується редакція, що діяла на момент замовлення."),
        ],
        "note": "Цей документ підготовлено як основу, а не як готовий юридичний текст. "
                "Перш ніж сайт почне його використовувати, дайте його на перевірку тому, "
                "хто може нести відповідальність за формулювання — насамперед строки, "
                "гарантію та відмову від договору.",
    },
}


# Právní stránky podle slugu — česká verze je v content/articles.py
LEGAL_I18N = {
    "zasady-ochrany-osobnich-udaju": PRIVACY_I18N,
    "obchodni-podminky": TERMS_I18N,
}


# --------------------------------------------------------------------------- #
# Blog — rozcestník a články v jazykových mutacích
#
# Datum a obrázek se berou z české verze v content/articles.py, překládá se
# jen text. date_h je tu zvlášť, protože formát data se jazyk od jazyka liší.
# --------------------------------------------------------------------------- #
BLOG_I18N = {
    "en": {
        "title": "Blog about locks and locksmithing",
        "meta_title": "Blog about locks and locksmithing | Rychlý Zámečník",
        "desc": "Advice on locks and security, and stories from call-outs by a locksmith "
                "emergency service in Prague. How not to fall for dishonest locksmiths and "
                "what to do when a door slams shut.",
        "lead": "Advice on what to watch out for, and stories from call-outs. We write "
                "about what we actually run into at customers' homes.",
        "cta_head": "Dealing with a lock right now?",
        "cta_text": "Don't read — call. The consultation is free and a technician sets off "
                    "immediately.",
        "more_head": "You might also like",
        "more_eyebrow": "More articles",
    },
    "ru": {
        "title": "Блог о замках и слесарном деле",
        "meta_title": "Блог о замках и слесарном деле | Rychlý Zámečník",
        "desc": "Советы о замках и безопасности, истории с выездов аварийной слесарной "
                "службы в Праге. Как не попасться недобросовестным слесарям и что делать, "
                "когда захлопнулась дверь.",
        "lead": "Советы, на что обратить внимание, и истории с выездов. Пишем о том, "
                "с чем действительно сталкиваемся у клиентов.",
        "cta_head": "Решаете проблему с замком прямо сейчас?",
        "cta_text": "Не читайте — звоните. Консультация бесплатна, и техник выезжает "
                    "немедленно.",
        "more_head": "Возможно, вас заинтересует",
        "more_eyebrow": "Другие статьи",
    },
    "ua": {
        "title": "Блог про замки та слюсарну справу",
        "meta_title": "Блог про замки та слюсарну справу | Rychlý Zámečník",
        "desc": "Поради про замки та безпеку, історії з виїздів аварійної слюсарної "
                "служби в Празі. Як не натрапити на недобросовісних слюсарів і що робити, "
                "коли зачинилися двері.",
        "lead": "Поради, на що звернути увагу, та історії з виїздів. Пишемо про те, "
                "з чим справді стикаємося у клієнтів.",
        "cta_head": "Вирішуєте проблему із замком просто зараз?",
        "cta_text": "Не читайте — телефонуйте. Консультація безкоштовна, і технік виїжджає "
                    "негайно.",
        "more_head": "Можливо, вас зацікавить",
        "more_eyebrow": "Інші статті",
    },
}


ARTICLES_I18N = {"en": {}, "ru": {}, "ua": {}}

ARTICLES_I18N["en"] = {
    "nejcastejsi-triky-nepoctivych-zamecniku": {
        "title": "Dishonest locksmiths in Prague — the tricks, the prices, how not to fall for it",
        "meta_title": "Dishonest locksmiths in Prague — tricks and prices | Rychlý Zámečník",
        "desc": "Watch out for dishonest locksmiths in Prague. Spot their tricks, learn "
                "the real prices and pick a fair 24/7 locksmith.",
        "date_h": "9 February 2026",
        "img_alt": "A locksmith working on a security lock",
        "perex": "A slammed door or lost keys are stressful. And that stress is exactly "
                 "what dishonest locksmiths target. We'll show you the most common tricks "
                 "and, above all, how to recognise a fair 24/7 locksmith.",
        "tag": "Advice",
        "body": [
            ("h", "1. A suspiciously low price in the ad"),
            ("p", "&bdquo;Door opening from CZK 499&ldquo; sounds tempting. The reality? "
                  "On site the price easily climbs to <strong>CZK 5,000–10,000</strong>."),
            ("p", "How they do it: the low price is only &bdquo;for turning up&ldquo; and "
                  "every further step is billed separately, and steeply."),
            ("ok", ["Always ask for the final indicative price on the phone.",
                    "A serious locksmith service does not hide the price."]),

            ("h", "2. Drilling the lock straight away"),
            ("p", "An honest locksmith always tries to open <strong>without damage</strong>. "
                  "A dishonest one often doesn't even attempt the gentle methods and drills "
                  "immediately — which means an expensive lock replacement on top."),
            ("ok", ["Ask outright: &bdquo;Can it be opened without damage?&ldquo;",
                    "If you hear &bdquo;there's no other way&ldquo; the moment they arrive, "
                    "be on your guard."]),

            ("h", "3. Pressure for an unnecessary lock replacement"),
            ("q", "&bdquo;That lock is dangerous, we have to replace it right away.&ldquo;"),
            ("p", "A common trick, especially at night. In reality the lock is usually "
                  "working fine and no replacement is needed."),
            ("ok", ["Ask for an explanation and a specific reason.",
                    "You have every right to refuse the replacement."]),

            ("h", "4. Unclear identity and no receipt"),
            ("p", "The typical scenario: no company ID, no company, no proof of payment. "
                  "You then have nowhere to complain and the service tends to be wildly "
                  "overpriced."),
            ("ok", ["Choose an established locksmith business.",
                    "A receipt is a matter of course, not a favour."]),

            ("h", "5. Fake &bdquo;local firms&ldquo;"),
            ("p", "The website claims &bdquo;Prague 1&ldquo;, the reality is a call centre "
                  "outside Prague, a long journey and high travel charges."),
            ("ok", ["Check whether the firm really operates in Prague.",
                    "Read the reviews — not just five-star ones with no text."]),

            ("h", "How to recognise an honest locksmith"),
            ("ok", ["They give you the price in advance, on the phone.",
                    "They arrive within a reasonable time.",
                    "They try to open without damage.",
                    "They don't push unnecessary repairs.",
                    "They issue a receipt."]),

            ("h", "In short"),
            ("no", ["Extremely cheap offers are a risk, not a bargain."]),
            ("ok", ["Insist on knowing the price before they set off.",
                    "An honest 24/7 locksmith has nothing to hide."]),
        ],
    },

    "jak-odemknout-zamek-par-rad": {
        "title": "How to unlock a lock — practical advice",
        "meta_title": "How to unlock a lock — practical advice | Rychlý Zámečník",
        "desc": "Not sure how to unlock a lock? Rychlý Zámečník explains what you can try "
                "yourself and when it is better to call an emergency locksmith.",
        "date_h": "9 January 2026",
        "img_alt": "Hands unlocking a door lock",
        "perex": "A jammed key, a slammed door or a lock that refuses to cooperate. "
                 "Before you panic or resort to force, go through a few tips on how to "
                 "proceed sensibly and safely.",
        "tag": "Advice",
        "body": [
            ("h", "Tip 1: Don't force the key"),
            ("p", "If the key is catching in the lock, don't force it, don't try to "
                  "&bdquo;break it free&ldquo; and don't turn it violently."),
            ("p", "A snapped key in the lock means a more complicated opening and often "
                  "a replacement of the whole lock. Sometimes a gentle wiggle of the key "
                  "or a light push of the door towards the frame is all it takes."),

            ("h", "Tip 2: Check whether the door has merely slammed shut"),
            ("p", "In many cases the lock isn't locked at all — the door has simply "
                  "slammed shut. That's good news: such a door can often be opened "
                  "<strong>without any damage</strong>."),
            ("ok", ["The door isn't locked with a key.",
                    "The key isn't broken.",
                    "The lock isn't damaged."]),
            ("p", "If all of the above holds, a professional opening is a matter of minutes."),

            ("h", "Tip 3: Avoid the &bdquo;guaranteed tricks&ldquo; from the internet"),
            ("p", "A credit card, a screwdriver, a wire or a coat hanger? The tutorials "
                  "look simple, but in practice they tend to end like this:"),
            ("no", ["a damaged door",
                    "a ruined lock",
                    "higher repair costs"]),
            ("p", "What is meant to be a quick fix often turns into an expensive problem."),

            ("h", "When to call a locksmith"),
            ("ul", ["The key won't turn.",
                    "The lock is damaged.",
                    "The key has snapped.",
                    "You don't want to risk the damage."]),
            ("p", "In these cases an emergency locksmith is the best choice. An experienced "
                  "24/7 locksmith will open the lock gently, without needless damage and "
                  "at a price agreed in advance."),
        ],
    },

    "nejvtipnejsi-pribeh-nouzoveho-otevreni-auta-v-roce-2025": {
        "title": "The funniest emergency car opening of 2025",
        "meta_title": "The funniest emergency car opening of 2025 | Locksmith Prague 1",
        "desc": "Emergency car opening in Prague 1 — a funny story from Wenceslas Square. "
                "A fast locksmith, opening a car without damage, 24/7.",
        "date_h": "28 December 2025",
        "img_alt": "A locksmith opening a locked car",
        "perex": "One of the most curious situations of the year played out right in the "
                 "heart of Prague and showed that an emergency car opening can be not only "
                 "fast, but unexpectedly entertaining too.",
        "tag": "From the field",
        "body": [
            ("h", "A locked car, a tourist and a sausage in hand"),
            ("p", "It was shortly after noon, Wenceslas Square was pulsing with life, and "
                  "among the tourists, trams and street performers there he was — a slightly "
                  "bewildered foreign visitor. A camera in one hand, a freshly bought sausage "
                  "in the other. The keys? They stayed inside the car, which had just locked "
                  "itself with that characteristic <em>click</em>."),
            ("p", "Despair gave way to some frantic googling: <strong>locksmith Prague 1 — "
                  "emergency car opening</strong>."),

            ("h", "A job that took minutes"),
            ("p", "The locksmith arrived within a few minutes. No smashed glass, no damage "
                  "to the lock, just specialist tools and the calm of an experienced "
                  "professional. As a small crowd began to gather around the car, the "
                  "tourist remarked nervously:"),
            ("q", "&bdquo;If it doesn't work, at least we can share the sausage…&ldquo;"),
            ("p", "That was a mistake. The audience laughed so loudly that one of the street "
                  "musicians spontaneously added a dramatic melody. At that very moment the "
                  "locksmith opened the car — elegantly, quickly and without a single "
                  "scratch. Applause. The sausage saved. The keys back in their owner's hand."),

            ("h", "Why we remember that one"),
            ("p", "Because it captures exactly what an emergency car opening in Prague "
                  "should look like:"),
            ("ok", ["a quick arrival, no waiting",
                    "opening the car without damage",
                    "professional and human at the same time",
                    "the situation solved with a smile"]),

            ("h", "The takeaway"),
            ("p", "Whether you're a tourist or a local, a locked car doesn't discriminate. "
                  "When it happens, don't panic, don't try to lever the door yourself, and "
                  "call a locksmith who has experience with emergency car openings."),
        ],
    },

    "otevreni-trezoru-stodulky-neuveritelny-pribeh": {
        "title": "Opening a safe in Stodůlky — an unbelievable story",
        "meta_title": "Opening a safe in Stodůlky — an unbelievable story | Rychlý Zámečník",
        "desc": "The unbelievable story of opening a safe in Stodůlky. Locksmith Prague 13, "
                "a fast job, opening a safe without damage.",
        "date_h": "29 December 2025",
        "img_alt": "A locksmith opening a safe",
        "perex": "A forgotten code, a dead battery and a safe that hadn't been opened in "
                 "years. The job in Stodůlky showed why patience beats a drill when it "
                 "comes to safes.",
        "tag": "From the field",
        "body": [
            ("h", "The safe that stayed silent"),
            ("p", "A client from Prague 13 inherited an older safe from his parents. Nobody "
                  "knew the code, the key had wandered off somewhere over the years and the "
                  "electronics had long shown no sign of life. The first company he "
                  "approached proposed drilling it straight out."),

            ("h", "Why the drill wasn't the first choice"),
            ("p", "With safes there's a simple rule: <strong>you can always drill, but you "
                  "can't undo it</strong>. A drilled safe loses its certification and its "
                  "insurance value, and the repair tends to cost more than the opening itself."),
            ("ok", ["Try the non-destructive methods first.",
                    "Identify the lock type and the manufacturer.",
                    "Only then consider going through the shell."]),

            ("h", "How it turned out"),
            ("p", "After replacing the battery in the external power supply and some patient "
                  "work with the mechanism, the safe opened without a single hole. Inside "
                  "were the documents the family had been looking for for months."),
            ("p", "The safe is still in service today — just with a new code, which the "
                  "client wrote down this time."),

            ("h", "What to take from it"),
            ("ul", ["Keep the code to your safe somewhere outside the safe. It sounds "
                    "obvious, but it's the most common reason for our call-outs.",
                    "Replace the batteries in electronic locks as a precaution.",
                    "If someone proposes drilling as the first step, ask for an explanation."]),
        ],
    },

    "jak-otevrit-trezor-kaufland-praha-6": {
        "title": "How to open a safe — a story from Kaufland in Prague 6",
        "meta_title": "How to open a safe — a story from Kaufland Prague 6 | Rychlý Zámečník",
        "desc": "How do you open a safe when the technology fails? A story from Kaufland "
                "in Prague 6. Emergency safe opening, professional safe work.",
        "date_h": "30 December 2025",
        "img_alt": "Servicing and opening a safe",
        "perex": "Not every safe call-out is a drama. Sometimes it's more of a comedy — "
                 "especially when it plays out in the middle of a busy department store.",
        "tag": "From the field",
        "body": [
            ("h", "Locked at the worst possible moment"),
            ("p", "Early evening, a full shop and a safe holding the day's takings that "
                  "refused to open. The electronic lock was reporting an error, the staff "
                  "were trying the code for the sixth time and the queue at the tills kept "
                  "growing."),

            ("h", "First rule: don't keep trying forever"),
            ("p", "Most electronic safe locks have <strong>protection against repeated "
                  "entry</strong>. After several wrong attempts the lock blocks itself for "
                  "a few minutes — and with every further attempt the delay gets longer."),
            ("no", ["Trying the code over and over only makes things worse."]),
            ("ok", ["Stop, wait, and call someone who can open the safe properly."]),

            ("h", "How the job went"),
            ("p", "It turned out the problem wasn't the code but a flat battery — the lock "
                  "had enough power to light up the display, but not to release the bolt. "
                  "An external power supply, and the safe was open in moments."),

            ("h", "What to do when a safe won't open"),
            ("ul", ["Try replacing the batteries — it's the most common cause.",
                    "Don't enter the code repeatedly, you risk locking it out.",
                    "Don't try to lever or drill it, you'll lose the safe's certification.",
                    "Call a locksmith with experience of safes."]),
        ],
    },
}

ARTICLES_I18N["ru"] = {
    "nejcastejsi-triky-nepoctivych-zamecniku": {
        "title": "Недобросовестные слесари в Праге — уловки, цены и как не попасться",
        "meta_title": "Недобросовестные слесари в Праге — уловки и цены | Rychlý Zámečník",
        "desc": "Осторожно с недобросовестными слесарями в Праге. Разберитесь в их уловках, "
                "узнайте реальные цены и выберите честную круглосуточную службу.",
        "date_h": "9 февраля 2026",
        "img_alt": "Слесарь работает с замком повышенной безопасности",
        "perex": "Захлопнутая дверь или потерянные ключи — это стресс. И именно на этот "
                 "стресс, к сожалению, рассчитывают недобросовестные слесари. Покажем самые "
                 "частые уловки и главное — как распознать честную круглосуточную службу.",
        "tag": "Советы",
        "body": [
            ("h", "1. Подозрительно низкая цена в объявлении"),
            ("p", "«Вскрытие двери от 499 крон» звучит заманчиво. Реальность? На месте цена "
                  "легко доходит до <strong>5–10 тысяч крон</strong>."),
            ("p", "Как это делается: низкая цена — только «за выезд», а каждая следующая "
                  "операция считается отдельно и дорого."),
            ("ok", ["Всегда спрашивайте итоговую ориентировочную цену уже по телефону.",
                    "Серьёзная слесарная служба цену не скрывает."]),

            ("h", "2. Немедленное сверление замка"),
            ("p", "Честный слесарь всегда пытается вскрыть <strong>без повреждений</strong>. "
                  "Недобросовестный часто даже не пробует щадящие методы и сразу сверлит — "
                  "а это ещё и дорогая замена замка."),
            ("ok", ["Спросите прямо: «Получится вскрыть без повреждений?»",
                    "Если сразу по приезде слышите «иначе никак» — насторожитесь."]),

            ("h", "3. Давление на ненужную замену замка"),
            ("q", "«Этот замок опасен, его нужно немедленно заменить.»"),
            ("p", "Частая уловка, особенно ночью. На деле замок обычно исправен "
                  "и замена не нужна."),
            ("ok", ["Требуйте объяснения и конкретной причины.",
                    "Вы вправе отказаться от замены."]),

            ("h", "4. Неясная личность и отсутствие документа"),
            ("p", "Типичный сценарий: нет ИНН, нет фирмы, нет документа об оплате. "
                  "Обратиться с претензией потом некуда, а услуга оказывается крайне "
                  "завышенной по цене."),
            ("ok", ["Выбирайте проверенную слесарную компанию.",
                    "Документ об оплате — это норма, а не одолжение."]),

            ("h", "5. Поддельные «местные фирмы»"),
            ("p", "На сайте написано «Прага 1», а на деле это диспетчерская за пределами "
                  "Праги, долгая дорога и высокая плата за выезд."),
            ("ok", ["Проверьте, действительно ли фирма работает в Праге.",
                    "Читайте отзывы — не только пятизвёздочные без текста."]),

            ("h", "Как распознать честного слесаря"),
            ("ok", ["Называет цену заранее по телефону.",
                    "Приезжает в разумный срок.",
                    "Старается вскрыть без повреждений.",
                    "Не навязывает ненужный ремонт.",
                    "Выдаёт документ об оплате."]),

            ("h", "Коротко"),
            ("no", ["Крайне дешёвые предложения — это риск, а не выгода."]),
            ("ok", ["Цену узнавайте ещё до выезда.",
                    "Честной круглосуточной службе нечего скрывать."]),
        ],
    },

    "jak-odemknout-zamek-par-rad": {
        "title": "Как открыть замок — практические советы",
        "meta_title": "Как открыть замок — практические советы | Rychlý Zámečník",
        "desc": "Не знаете, как открыть замок? Rychlý Zámečník подсказывает, что можно "
                "попробовать самому и когда лучше вызвать аварийную слесарную службу.",
        "date_h": "9 января 2026",
        "img_alt": "Руки открывают дверной замок",
        "perex": "Заклинивший ключ, захлопнутая дверь или замок, который отказывается "
                 "работать. Прежде чем паниковать или применять силу, прочитайте несколько "
                 "советов, как действовать разумно и безопасно.",
        "tag": "Советы",
        "body": [
            ("h", "Совет 1: не давите на ключ силой"),
            ("p", "Если ключ в замке идёт туго, не давите на него, не пытайтесь «сломить» "
                  "сопротивление и не проворачивайте с силой."),
            ("p", "Сломанный ключ в замке означает более сложное вскрытие и часто замену "
                  "всего замка. Иногда достаточно слегка пошевелить ключом или чуть "
                  "прижать дверь к косяку."),

            ("h", "Совет 2: проверьте, не просто ли захлопнулась дверь"),
            ("p", "Во многих случаях замок вовсе не заперт — дверь просто захлопнулась. "
                  "Это хорошая новость: такую дверь часто можно открыть "
                  "<strong>без повреждений</strong>."),
            ("ok", ["Дверь не заперта на ключ.",
                    "Ключ не сломан.",
                    "Замок не повреждён."]),
            ("p", "Если всё перечисленное верно, профессиональное вскрытие — вопрос минут."),

            ("h", "Совет 3: избегайте «гарантированных приёмов» из интернета"),
            ("p", "Банковская карта, отвёртка, проволока или вешалка? Инструкции выглядят "
                  "просто, но на практике всё чаще заканчивается так:"),
            ("no", ["повреждённая дверь",
                    "испорченный замок",
                    "более высокие расходы на ремонт"]),
            ("p", "То, что должно было стать быстрым решением, нередко превращается "
                  "в дорогую проблему."),

            ("h", "Когда пора звонить слесарю"),
            ("ul", ["Ключ не поворачивается.",
                    "Замок повреждён.",
                    "Ключ сломался.",
                    "Вы не хотите рисковать повреждениями."]),
            ("p", "В этих случаях лучший выбор — аварийная слесарная служба. Опытный "
                  "круглосуточный слесарь вскроет замок аккуратно, без лишних повреждений "
                  "и по цене, согласованной заранее."),
        ],
    },

    "nejvtipnejsi-pribeh-nouzoveho-otevreni-auta-v-roce-2025": {
        "title": "Самое смешное аварийное вскрытие автомобиля 2025 года",
        "meta_title": "Самое смешное вскрытие автомобиля 2025 | Слесарь Прага 1",
        "desc": "Аварийное вскрытие автомобиля в Праге 1 — забавная история с Вацлавской "
                "площади. Быстрый слесарь, вскрытие без повреждений, 24/7.",
        "date_h": "28 декабря 2025",
        "img_alt": "Слесарь вскрывает запертый автомобиль",
        "perex": "Одна из самых курьёзных ситуаций года произошла прямо в сердце Праги "
                 "и показала, что аварийное вскрытие автомобиля бывает не только быстрым, "
                 "но и неожиданно забавным.",
        "tag": "Из практики",
        "body": [
            ("h", "Запертая машина, турист и колбаска в руке"),
            ("p", "Было чуть за полдень, Вацлавская площадь бурлила жизнью, и среди "
                  "туристов, трамваев и уличных артистов появился он — слегка растерянный "
                  "иностранный гость. В одной руке фотоаппарат, в другой — только что "
                  "купленная колбаска. Ключи? Они остались внутри машины, которая с "
                  "характерным <em>щелчком</em> как раз заперлась."),
            ("p", "На смену отчаянию пришёл быстрый поиск: <strong>слесарь Прага 1 — "
                  "аварийное вскрытие автомобиля</strong>."),

            ("h", "Работа на пару минут"),
            ("p", "Слесарь приехал за считаные минуты. Без разбитого стекла, без "
                  "повреждения замка — только специальный инструмент и спокойствие "
                  "опытного мастера. Когда вокруг машины стала собираться небольшая "
                  "толпа, турист нервно заметил:"),
            ("q", "«Если не получится, хотя бы разделим колбаску…»"),
            ("p", "Это было ошибкой. Публика рассмеялась так громко, что один из уличных "
                  "музыкантов спонтанно добавил драматическую мелодию. Именно в этот момент "
                  "слесарь открыл машину — изящно, быстро и без единой царапины. "
                  "Аплодисменты. Колбаска спасена. Ключи снова в руках владельца."),

            ("h", "Почему мы помним эту историю"),
            ("p", "Потому что она точно показывает, каким должно быть аварийное вскрытие "
                  "автомобиля в Праге:"),
            ("ok", ["быстрый приезд, без ожидания",
                    "вскрытие автомобиля без повреждений",
                    "профессионально и по-человечески одновременно",
                    "ситуация решена с улыбкой"]),

            ("h", "Вывод"),
            ("p", "Турист вы или местный — запертая машина не выбирает. Если это случилось, "
                  "не паникуйте, не пытайтесь отжать дверь самостоятельно и позвоните "
                  "слесарю, у которого есть опыт аварийного вскрытия автомобилей."),
        ],
    },

    "otevreni-trezoru-stodulky-neuveritelny-pribeh": {
        "title": "Вскрытие сейфа в Стодулках — невероятная история",
        "meta_title": "Вскрытие сейфа в Стодулках — невероятная история | Rychlý Zámečník",
        "desc": "Невероятная история вскрытия сейфа в Стодулках. Слесарь Прага 13, "
                "быстрый выезд, вскрытие сейфа без повреждений.",
        "date_h": "29 декабря 2025",
        "img_alt": "Слесарь вскрывает сейф",
        "perex": "Забытый код, севшая батарейка и сейф, который не открывали годами. "
                 "Выезд в Стодулки показал, почему с сейфами терпение выгоднее дрели.",
        "tag": "Из практики",
        "body": [
            ("h", "Сейф, который молчал"),
            ("p", "Клиент из Праги 13 унаследовал от родителей старый сейф. Кода никто "
                  "не знал, ключ за эти годы куда-то затерялся, а электроника давно "
                  "не подавала признаков жизни. Первая фирма, к которой он обратился, "
                  "сразу предложила сверлить."),

            ("h", "Почему дрель не была первым выбором"),
            ("p", "С сейфами действует простое правило: <strong>просверлить можно всегда, "
                  "а вот обратно уже никак</strong>. Просверленный сейф теряет сертификацию "
                  "и страховую ценность, а ремонт обычно дороже самого вскрытия."),
            ("ok", ["Сначала испробовать неразрушающие методы.",
                    "Определить тип замка и производителя.",
                    "И только потом рассматривать вмешательство в корпус."]),

            ("h", "Чем всё закончилось"),
            ("p", "После замены батарейки во внешнем питании и терпеливой работы "
                  "с механикой сейф открылся без единого отверстия. Внутри лежали "
                  "документы, которые семья искала несколько месяцев."),
            ("p", "Сейф работает до сих пор — только с новым кодом, который клиент "
                  "на этот раз записал."),

            ("h", "Что стоит запомнить"),
            ("ul", ["Код от сейфа храните вне сейфа. Звучит очевидно, но это самая "
                    "частая причина наших выездов.",
                    "Батарейки в электронных замках меняйте профилактически.",
                    "Если кто-то предлагает сверление первым шагом — требуйте объяснений."]),
        ],
    },

    "jak-otevrit-trezor-kaufland-praha-6": {
        "title": "Как вскрыть сейф — история из Kaufland в Праге 6",
        "meta_title": "Как вскрыть сейф — история из Kaufland Прага 6 | Rychlý Zámečník",
        "desc": "Как вскрыть сейф, когда техника подводит? История из Kaufland в Праге 6. "
                "Аварийное вскрытие сейфа, профессиональная работа с сейфами.",
        "date_h": "30 декабря 2025",
        "img_alt": "Обслуживание и вскрытие сейфа",
        "perex": "Не каждый выезд к сейфу — драма. Иногда это скорее комедия, особенно "
                 "когда всё происходит посреди работы торгового центра.",
        "tag": "Из практики",
        "body": [
            ("h", "Заперто в самый неподходящий момент"),
            ("p", "Ранний вечер, полный магазин и сейф с дневной выручкой, который "
                  "отказался открываться. Электронный замок сообщал об ошибке, персонал "
                  "вводил код в шестой раз, а очередь на кассах тем временем росла."),

            ("h", "Первое правило: не пробовать до бесконечности"),
            ("p", "У большинства электронных сейфовых замков есть <strong>защита "
                  "от повторного ввода</strong>. После нескольких неверных попыток замок "
                  "блокируется на несколько минут — и с каждой следующей попыткой пауза "
                  "становится длиннее."),
            ("no", ["Вводить код снова и снова — только хуже."]),
            ("ok", ["Остановиться, подождать и вызвать того, кто вскроет сейф профессионально."]),

            ("h", "Как прошёл выезд"),
            ("p", "Выяснилось, что дело было не в коде, а в севшей батарейке — энергии "
                  "хватало на подсветку дисплея, но не на отпирание ригеля. Внешнее "
                  "питание — и сейф открылся за считаные мгновения."),

            ("h", "Что делать, если сейф не открывается"),
            ("ul", ["Попробуйте заменить батарейки — это самая частая причина.",
                    "Не вводите код многократно, рискуете заблокировать замок.",
                    "Не пытайтесь отжать или просверлить — потеряете сертификацию сейфа.",
                    "Вызовите слесаря с опытом работы с сейфами."]),
        ],
    },
}

ARTICLES_I18N["ua"] = {
    "nejcastejsi-triky-nepoctivych-zamecniku": {
        "title": "Недобросовісні слюсарі у Празі — хитрощі, ціни і як не натрапити",
        "meta_title": "Недобросовісні слюсарі у Празі — хитрощі та ціни | Rychlý Zámečník",
        "desc": "Обережно з недобросовісними слюсарями у Празі. Розберіться в їхніх "
                "хитрощах, дізнайтеся реальні ціни та оберіть чесну цілодобову службу.",
        "date_h": "9 лютого 2026",
        "img_alt": "Слюсар працює із замком підвищеної безпеки",
        "perex": "Зачинені двері чи загублені ключі — це стрес. І саме на цей стрес, "
                 "на жаль, розраховують недобросовісні слюсарі. Покажемо найчастіші "
                 "хитрощі й головне — як розпізнати чесну цілодобову службу.",
        "tag": "Поради",
        "body": [
            ("h", "1. Підозріло низька ціна в оголошенні"),
            ("p", "«Відкриття дверей від 499 крон» звучить привабливо. Реальність? "
                  "На місці ціна легко сягає <strong>5–10 тисяч крон</strong>."),
            ("p", "Як це роблять: низька ціна — лише «за виїзд», а кожна наступна операція "
                  "рахується окремо й дорого."),
            ("ok", ["Завжди питайте підсумкову орієнтовну ціну ще телефоном.",
                    "Серйозна слюсарна служба ціну не приховує."]),

            ("h", "2. Негайне свердління замка"),
            ("p", "Чесний слюсар завжди намагається відкрити <strong>без пошкоджень</strong>. "
                  "Недобросовісний часто навіть не пробує щадні методи й одразу свердлить — "
                  "а це ще й дорога заміна замка."),
            ("ok", ["Запитайте прямо: «Чи вдасться відкрити без пошкоджень?»",
                    "Якщо одразу після приїзду чуєте «інакше ніяк» — насторожіться."]),

            ("h", "3. Тиск на непотрібну заміну замка"),
            ("q", "«Цей замок небезпечний, його треба негайно замінити.»"),
            ("p", "Часта хитрість, особливо вночі. Насправді замок зазвичай справний "
                  "і заміна не потрібна."),
            ("ok", ["Вимагайте пояснення та конкретної причини.",
                    "Ви маєте право відмовитися від заміни."]),

            ("h", "4. Незрозуміла особа й жодного документа"),
            ("p", "Типовий сценарій: немає ІПН, немає фірми, немає документа про оплату. "
                  "Звернутися з претензією потім нікуди, а послуга виявляється вкрай "
                  "завищеною за ціною."),
            ("ok", ["Обирайте перевірену слюсарну компанію.",
                    "Документ про оплату — це норма, а не послуга."]),

            ("h", "5. Фальшиві «місцеві фірми»"),
            ("p", "На сайті написано «Прага 1», а насправді це диспетчерська за межами "
                  "Праги, довга дорога та висока плата за виїзд."),
            ("ok", ["Перевірте, чи справді фірма працює у Празі.",
                    "Читайте відгуки — не лише п'ятизіркові без тексту."]),

            ("h", "Як розпізнати чесного слюсаря"),
            ("ok", ["Називає ціну заздалегідь телефоном.",
                    "Приїжджає в розумний строк.",
                    "Намагається відкрити без пошкоджень.",
                    "Не нав'язує непотрібний ремонт.",
                    "Видає документ про оплату."]),

            ("h", "Коротко"),
            ("no", ["Украй дешеві пропозиції — це ризик, а не вигода."]),
            ("ok", ["Ціну з'ясовуйте ще до виїзду.",
                    "Чесній цілодобовій службі нема чого приховувати."]),
        ],
    },

    "jak-odemknout-zamek-par-rad": {
        "title": "Як відкрити замок — практичні поради",
        "meta_title": "Як відкрити замок — практичні поради | Rychlý Zámečník",
        "desc": "Не знаєте, як відкрити замок? Rychlý Zámečník підказує, що можна "
                "спробувати самому і коли краще викликати аварійну слюсарну службу.",
        "date_h": "9 січня 2026",
        "img_alt": "Руки відкривають дверний замок",
        "perex": "Заклинений ключ, зачинені двері або замок, який відмовляється працювати. "
                 "Перш ніж панікувати чи застосовувати силу, прочитайте кілька порад, "
                 "як діяти розумно й безпечно.",
        "tag": "Поради",
        "body": [
            ("h", "Порада 1: не тисніть на ключ силою"),
            ("p", "Якщо ключ у замку йде туго, не тисніть на нього, не намагайтеся "
                  "«зламати» опір і не прокручуйте із силою."),
            ("p", "Зламаний ключ у замку означає складніше відкриття і часто заміну "
                  "всього замка. Іноді достатньо злегка поворушити ключем або трохи "
                  "притиснути двері до одвірка."),

            ("h", "Порада 2: перевірте, чи не просто зачинилися двері"),
            ("p", "У багатьох випадках замок узагалі не замкнений — двері просто "
                  "зачинилися. Це добра новина: такі двері часто можна відкрити "
                  "<strong>без пошкоджень</strong>."),
            ("ok", ["Двері не замкнені на ключ.",
                    "Ключ не зламаний.",
                    "Замок не пошкоджений."]),
            ("p", "Якщо все перелічене справджується, професійне відкриття — питання хвилин."),

            ("h", "Порада 3: уникайте «гарантованих прийомів» з інтернету"),
            ("p", "Банківська картка, викрутка, дріт чи вішак? Інструкції виглядають "
                  "просто, але на практиці все частіше закінчується так:"),
            ("no", ["пошкоджені двері",
                    "зіпсований замок",
                    "вищі витрати на ремонт"]),
            ("p", "Те, що мало стати швидким рішенням, нерідко перетворюється "
                  "на дорогу проблему."),

            ("h", "Коли час телефонувати слюсарю"),
            ("ul", ["Ключ не повертається.",
                    "Замок пошкоджений.",
                    "Ключ зламався.",
                    "Ви не хочете ризикувати пошкодженнями."]),
            ("p", "У цих випадках найкращий вибір — аварійна слюсарна служба. Досвідчений "
                  "цілодобовий слюсар відкриє замок акуратно, без зайвих пошкоджень "
                  "і за ціною, погодженою заздалегідь."),
        ],
    },

    "nejvtipnejsi-pribeh-nouzoveho-otevreni-auta-v-roce-2025": {
        "title": "Найкумедніше аварійне відкриття автомобіля 2025 року",
        "meta_title": "Найкумедніше відкриття автомобіля 2025 | Слюсар Прага 1",
        "desc": "Аварійне відкриття автомобіля у Празі 1 — кумедна історія з Вацлавської "
                "площі. Швидкий слюсар, відкриття без пошкоджень, 24/7.",
        "date_h": "28 грудня 2025",
        "img_alt": "Слюсар відкриває замкнений автомобіль",
        "perex": "Одна з найкурйозніших ситуацій року сталася просто в серці Праги "
                 "й показала, що аварійне відкриття автомобіля буває не лише швидким, "
                 "а й несподівано кумедним.",
        "tag": "З практики",
        "body": [
            ("h", "Замкнене авто, турист і ковбаска в руці"),
            ("p", "Був початок дня, Вацлавська площа вирувала життям, і серед туристів, "
                  "трамваїв та вуличних артистів з'явився він — трохи розгублений "
                  "іноземний гість. В одній руці фотоапарат, у другій — щойно куплена "
                  "ковбаска. Ключі? Вони залишилися всередині авта, яке з характерним "
                  "<em>клацанням</em> саме замкнулося."),
            ("p", "На зміну відчаю прийшов швидкий пошук: <strong>слюсар Прага 1 — "
                  "аварійне відкриття автомобіля</strong>."),

            ("h", "Робота на кілька хвилин"),
            ("p", "Слюсар приїхав за лічені хвилини. Без розбитого скла, без пошкодження "
                  "замка — лише спеціальний інструмент і спокій досвідченого майстра. "
                  "Коли навколо авта почав збиратися невеликий натовп, турист нервово "
                  "зауважив:"),
            ("q", "«Якщо не вийде, хоча б поділимо ковбаску…»"),
            ("p", "Це була помилка. Публіка засміялася так голосно, що один з вуличних "
                  "музикантів спонтанно додав драматичну мелодію. Саме цієї миті слюсар "
                  "відкрив авто — елегантно, швидко й без жодної подряпини. Оплески. "
                  "Ковбаска врятована. Ключі знову в руках власника."),

            ("h", "Чому ми пам'ятаємо цю історію"),
            ("p", "Бо вона точно показує, яким має бути аварійне відкриття автомобіля "
                  "у Празі:"),
            ("ok", ["швидкий приїзд, без очікування",
                    "відкриття автомобіля без пошкоджень",
                    "професійно й по-людськи водночас",
                    "ситуація вирішена з усмішкою"]),

            ("h", "Висновок"),
            ("p", "Турист ви чи місцевий — замкнене авто не обирає. Якщо це сталося, "
                  "не панікуйте, не намагайтеся віджати двері самотужки й зателефонуйте "
                  "слюсарю, який має досвід аварійного відкриття автомобілів."),
        ],
    },

    "otevreni-trezoru-stodulky-neuveritelny-pribeh": {
        "title": "Відкриття сейфа у Стодулках — неймовірна історія",
        "meta_title": "Відкриття сейфа у Стодулках — неймовірна історія | Rychlý Zámečník",
        "desc": "Неймовірна історія відкриття сейфа у Стодулках. Слюсар Прага 13, "
                "швидкий виїзд, відкриття сейфа без пошкоджень.",
        "date_h": "29 грудня 2025",
        "img_alt": "Слюсар відкриває сейф",
        "perex": "Забутий код, сіла батарейка і сейф, який не відкривали роками. "
                 "Виїзд у Стодулки показав, чому із сейфами терпіння вигідніше за дриль.",
        "tag": "З практики",
        "body": [
            ("h", "Сейф, який мовчав"),
            ("p", "Клієнт із Праги 13 успадкував від батьків старий сейф. Коду ніхто "
                  "не знав, ключ за ці роки кудись подівся, а електроніка давно "
                  "не подавала ознак життя. Перша фірма, до якої він звернувся, одразу "
                  "запропонувала свердлити."),

            ("h", "Чому дриль не була першим вибором"),
            ("p", "Із сейфами діє просте правило: <strong>просвердлити можна завжди, "
                  "а от назад уже ніяк</strong>. Просвердлений сейф втрачає сертифікацію "
                  "і страхову вартість, а ремонт зазвичай дорожчий за саме відкриття."),
            ("ok", ["Спершу випробувати неруйнівні методи.",
                    "Визначити тип замка та виробника.",
                    "І лише потім розглядати втручання в корпус."]),

            ("h", "Чим усе закінчилося"),
            ("p", "Після заміни батарейки в зовнішньому живленні та терплячої роботи "
                  "з механікою сейф відкрився без жодного отвору. Усередині лежали "
                  "документи, які родина шукала кілька місяців."),
            ("p", "Сейф працює й досі — тільки з новим кодом, який клієнт цього разу "
                  "записав."),

            ("h", "Що варто запам'ятати"),
            ("ul", ["Код від сейфа зберігайте поза сейфом. Звучить очевидно, але це "
                    "найчастіша причина наших виїздів.",
                    "Батарейки в електронних замках міняйте профілактично.",
                    "Якщо хтось пропонує свердління першим кроком — вимагайте пояснень."]),
        ],
    },

    "jak-otevrit-trezor-kaufland-praha-6": {
        "title": "Як відкрити сейф — історія з Kaufland у Празі 6",
        "meta_title": "Як відкрити сейф — історія з Kaufland Прага 6 | Rychlý Zámečník",
        "desc": "Як відкрити сейф, коли техніка підводить? Історія з Kaufland у Празі 6. "
                "Аварійне відкриття сейфа, професійна робота із сейфами.",
        "date_h": "30 грудня 2025",
        "img_alt": "Обслуговування та відкриття сейфа",
        "perex": "Не кожен виїзд до сейфа — драма. Іноді це радше комедія, особливо "
                 "коли все відбувається посеред роботи торгового центру.",
        "tag": "З практики",
        "body": [
            ("h", "Замкнено в найгірший можливий момент"),
            ("p", "Ранній вечір, повний магазин і сейф із денною виручкою, який "
                  "відмовився відкриватися. Електронний замок повідомляв про помилку, "
                  "персонал уводив код ушосте, а черга на касах тим часом росла."),

            ("h", "Перше правило: не пробувати до безкінечності"),
            ("p", "У більшості електронних сейфових замків є <strong>захист від "
                  "повторного введення</strong>. Після кількох хибних спроб замок "
                  "блокується на кілька хвилин — і з кожною наступною спробою пауза "
                  "стає довшою."),
            ("no", ["Уводити код знову і знову — лише гірше."]),
            ("ok", ["Зупинитися, зачекати й викликати того, хто відкриє сейф професійно."]),

            ("h", "Як минув виїзд"),
            ("p", "З'ясувалося, що річ була не в коді, а в сілій батарейці — енергії "
                  "вистачало на підсвічування дисплея, але не на відмикання ригеля. "
                  "Зовнішнє живлення — і сейф відкрився за лічені миті."),

            ("h", "Що робити, якщо сейф не відкривається"),
            ("ul", ["Спробуйте замінити батарейки — це найчастіша причина.",
                    "Не вводьте код багаторазово, ризикуєте заблокувати замок.",
                    "Не намагайтеся віджати чи просвердлити — втратите сертифікацію сейфа.",
                    "Викличте слюсаря з досвідом роботи із сейфами."]),
        ],
    },
}
