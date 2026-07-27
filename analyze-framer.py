#!/usr/bin/env python3
"""
Vytáhne design systém z Framer šablony.

Framer neumí export do HTML/CSS a jeho DOM je nepoužitelný — generované
třídy typu `framer-1oe98bp`, stovky inline stylů a markup zduplikovaný pro
každý breakpoint. Kopírovat se z toho nedá nic.

Použitelná je ale ta část, kterou Framer inlinuje do `<style>`: barevné
tokeny, `@font-face` a rozměry. Z nich se dá přečíst, jaká rozhodnutí
autor šablony udělal — a to je jediné, co má z koupené šablony smysl
přenášet ručně.

Spuštění:  python3 analyze-framer.py https://homemaster.framer.website/
"""

import collections
import re
import sys
import urllib.request

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")


def fetch(url: str) -> str:
    # Framer bez věrohodné hlavičky spojení rovnou resetuje.
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace")


def top(pattern: str, css: str, n: int = 14) -> str:
    c = collections.Counter(re.findall(pattern, css))
    return ", ".join(f"{v}px ({n_})" for v, n_ in c.most_common(n)) or "—"


def main(url: str) -> None:
    page = fetch(url)
    css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", page, re.S))
    print(f"{url}\n{len(page) / 1024:.0f} kB HTML, {len(css) / 1024:.0f} kB inline CSS\n")

    print("## Barevné tokeny")
    seen = []
    for _, val in re.findall(r"(--token-[0-9a-fA-F-]+)\s*:\s*([^;}]+)", css):
        v = val.strip()
        if re.fullmatch(r"#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)", v) and v not in seen:
            seen.append(v)
    print("   " + ", ".join(seen) if seen else "   —")

    print("\n## Písma")
    fams = collections.Counter()
    for face in re.findall(r"@font-face\s*\{(.*?)\}", css, re.S):
        m = re.search(r"font-family:\s*([^;]+);", face)
        w = re.search(r"font-weight:\s*([^;]+);", face)
        if m:
            fams[f"{m.group(1).strip().strip(chr(34) + chr(39))} {w.group(1).strip() if w else ''}"] += 1
    for k, n in fams.most_common(12):
        print(f"   {k}  ({n}×)")

    for label, pat in [("Stupně písma", r"font-size:\s*([0-9.]+)px"),
                       ("Rádiusy", r"border-radius:\s*([0-9.]+)px"),
                       ("Mezery (gap)", r"gap:\s*([0-9.]+)px"),
                       ("Odsazení", r"padding:\s*([0-9.]+)px")]:
        print(f"\n## {label}\n   {top(pat, css)}")

    heads = []
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", page, flags=re.S)
    for m in re.finditer(r"<(h[1-3])[^>]*>(.*?)</\1>", body, re.S):
        t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(2))).strip()
        if t and len(t) < 110 and t not in heads:
            heads.append(t)
    print(f"\n## Nadpisy ({len(heads)})")
    for h in heads[:25]:
        print(f"   {h}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__.strip().splitlines()[-1])
    main(sys.argv[1])
