#!/usr/bin/env python3
"""
Sestaví jednosouborovou verzi webu (dist/rychly-zamecnik.html).

CSS a JS se vloží inline, obrázky se zakódují jako data: URI. Výsledek je jeden
HTML soubor bez jakýchkoliv externích požadavků — vhodný pro náhled, sdílení
klientovi nebo publikaci pod přísnou CSP.
"""

import base64
import mimetypes
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
DIST = ROOT / "dist"


def data_uri(rel_path: str) -> str:
    path = ROOT / rel_path
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def build() -> pathlib.Path:
    html = (ROOT / "index.html").read_text(encoding="utf-8")

    # 1) Inline stylesheet
    css = (ROOT / "assets/css/style.css").read_text(encoding="utf-8")
    html = html.replace(
        '<link rel="stylesheet" href="assets/css/style.css">',
        f"<style>\n{css}\n</style>",
    )

    # 2) Inline script
    js = (ROOT / "assets/js/main.js").read_text(encoding="utf-8")
    html = html.replace(
        '<script src="assets/js/main.js"></script>',
        f"<script>\n{js}\n</script>",
    )

    # 3) Obrázky -> data: URI (src=, href= i og:image content=)
    def repl(match: "re.Match[str]") -> str:
        attr, rel = match.group(1), match.group(2)
        return f'{attr}="{data_uri(rel)}"'

    html = re.sub(r'(src|href|content)="(assets/img/[^"]+)"', repl, html)

    # 4) Jednosouborová verze je jen domovská stránka — odkazy na podstránky
    #    by vedly do prázdna, tak je svedeme na kotvu se službami.
    html = re.sub(r'href="/[a-z-]+/"', 'href="#sluzby"', html)

    DIST.mkdir(exist_ok=True)
    out = DIST / "rychly-zamecnik.html"
    out.write_text(html, encoding="utf-8")
    return out


if __name__ == "__main__":
    out = build()
    print(f"{out}  —  {out.stat().st_size / 1024:.0f} KB")
