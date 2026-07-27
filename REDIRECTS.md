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

## Nedořešeno

Žádné. Blog i jazykové mutace jsou součástí návrhu a drží původní adresy:

| URL | Stav |
|---|---|
| `/blogy-o-zamcich-a-zamecnictvich/` | zachováno, včetně všech pěti článků |
| `/en/`, `/ru/`, `/ua/` | zachováno — úvod, šest služeb a zásady |

Jedinou výjimkou jsou podstránky služeb v jazykových mutacích: pokud
TranslatePress používal jiné slugy než české, je potřeba je dohledat
v Search Console a přesměrovat na `/{jazyk}/{český-slug}/`.

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
