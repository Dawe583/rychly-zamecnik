# Přesměrování při přechodu na nový web

Původní web má vybudované pozice na „zámečník Praha" a příbuzné dotazy.
Aby se při nasazení neztratily, musí **každá URL, která dnes existuje,
buď dál fungovat, nebo mít 301 přesměrování** na nejbližší odpovídající
stránku.

## Zachované URL (beze změny)

Tyhle adresy zůstávají stejné, jen s novým obsahem — nic se nepřesměrovává:

| URL | Stav |
|---|---|
| `/` | zachováno |
| `/otevirani-dveri/` | zachováno |
| `/vymena-zamku/` | zachováno |
| `/otevirani-aut/` | zachováno |
| `/otevirani-trezoru/` | zachováno |
| `/oprava-dveri/` | zachováno |
| `/zamecnicka-pohotovost/` | zachováno |

## URL k přesměrování

Obsah těchto stránek je nově součástí domovské stránky:

| Původní URL | Cíl | Kód |
|---|---|---|
| `/sluzby/` | `/#sluzby` | 301 |
| `/cenik/` | `/#cenik` | 301 |
| `/recenze/` | `/#recenze` | 301 |

## Nedořešeno — vyžaduje rozhodnutí

| Původní URL | Poznámka |
|---|---|
| `/blogy-o-zamcich-a-zamecnictvich/` | Blog není součástí návrhu. Buď ho zachovat beze změny, nebo obsah převzít — **nepřesměrovávat naslepo na `/`**, přišlo by se o long-tail dotazy. |
| `/en/`, `/ru/`, `/ua/` | Jazykové mutace (TranslatePress). Návrh je zatím jen česky — do doby, než vzniknou, musí staré verze zůstat funkční. |

## Konfigurace

### Apache (`.htaccess`)

```apache
RewriteEngine On
RewriteRule ^sluzby/?$   /#sluzby  [R=301,L]
RewriteRule ^cenik/?$    /#cenik   [R=301,L]
RewriteRule ^recenze/?$  /#recenze [R=301,L]
```

### Nginx

```nginx
location = /sluzby/  { return 301 /#sluzby; }
location = /cenik/   { return 301 /#cenik; }
location = /recenze/ { return 301 /#recenze; }
```

### Netlify / Vercel (`_redirects`)

```
/sluzby/   /#sluzby   301
/cenik/    /#cenik    301
/recenze/  /#recenze  301
```

## Po nasazení zkontrolovat

1. Odeslat `sitemap.xml` v Google Search Console.
2. V Search Console projít **Pokrytí** — hlídat nárůst 404.
3. Ověřit strukturovaná data testerem bohatých výsledků
   (na podstránkách je `Service`, `BreadcrumbList` a `FAQPage`).
4. Sledovat pozice na „zámečník Praha", „otevírání dveří Praha",
   „zámečnická pohotovost" — propad po nasazení je signál chybějícího
   přesměrování.
