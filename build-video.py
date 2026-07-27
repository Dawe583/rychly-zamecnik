#!/usr/bin/env python3
"""
Sestaví hero video z fotek klienta.

Čtyři záběry z `assets/img/` dostanou pomalý nájezd (Ken Burns) a prolnou se
do sebe. Poslední záběr se prolíná zpátky do prvního, takže smyčka nikde
neškubne. Žádný stock, žádná generovaná grafika — jen jejich vlastní fotky
rozhýbané.

Vyžaduje ffmpeg s libvpx. ffmpeg dodávaný s Playwrightem umí jen VP8/WebM
a jako vstup přijímá pouze MJPEG přes rouru, proto ta oklika s JPEGy.

Spuštění:  python3 build-video.py
"""

import io
import pathlib
import subprocess

from PIL import Image

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "assets/img"
OUT = ROOT / "assets/video/hero-loop.webm"

FFMPEG = "/opt/pw-browsers/ffmpeg-1011/ffmpeg-linux"

W, H, FPS = 1280, 720, 24
STEP = 2.9      # jak dlouho je záběr sám na plátně
FADE = 0.9      # délka prolnutí do dalšího záběru

# (soubor, zoom od, zoom do, posun středu x/y jako podíl rozměru)
SHOTS = [
    ("hero-van-night.webp", 1.00, 1.13, (-0.02, 0.01)),
    ("tym-zamecniku.webp", 1.13, 1.00, (0.02, -0.01)),
    ("otevirani-dveri.webp", 1.00, 1.12, (0.00, -0.02)),
    ("otevirani-aut.webp", 1.12, 1.00, (-0.02, 0.00)),
]

N = len(SHOTS)
TOTAL = N * STEP
FRAMES = int(TOTAL * FPS)
SPAN = STEP + FADE          # celá doba, po kterou je záběr vidět


def load_sources():
    """Zvětší fotky tak, aby i při maximálním zoomu zůstaly ostré."""
    out = []
    for name, *_ in SHOTS:
        im = Image.open(SRC / name).convert("RGB")
        s = max(W * 1.3 / im.width, H * 1.3 / im.height)
        out.append(im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS))
    return out


def ken_burns(base, i, p):
    """Výřez ze záběru i v postupu p (0–1)."""
    p = max(0.0, min(1.0, p))
    _, z0, z1, (dx, dy) = SHOTS[i]
    e = p * p * (3 - 2 * p)          # smoothstep — pohyb nikde neškubne
    z = z0 + (z1 - z0) * e
    im = base[i]
    cw, ch = W / z, H / z
    cx = im.width / 2 + dx * im.width * (e - 0.5)
    cy = im.height / 2 + dy * im.height * (e - 0.5)
    left = max(0, min(im.width - cw, cx - cw / 2))
    top = max(0, min(im.height - ch, cy - ch / 2))
    return im.crop((round(left), round(top), round(left + cw), round(top + ch))) \
             .resize((W, H), Image.LANCZOS)


def build() -> pathlib.Path:
    base = load_sources()
    OUT.parent.mkdir(parents=True, exist_ok=True)

    ff = subprocess.Popen([
        FFMPEG, "-hide_banner", "-loglevel", "error", "-y",
        "-f", "image2pipe", "-vcodec", "mjpeg", "-r", str(FPS), "-i", "pipe:0",
        "-c:v", "libvpx", "-b:v", "780k", "-crf", "33", "-qmin", "10", "-qmax", "44",
        "-auto-alt-ref", "0", "-g", "48", "-deadline", "good", "-cpu-used", "2",
        "-an", "-pix_fmt", "yuv420p", str(OUT),
    ], stdin=subprocess.PIPE)

    for f in range(FRAMES):
        t = f / FPS
        slot = int(t // STEP)
        i = slot % N
        local = t - slot * STEP

        frame = ken_burns(base, i, local / SPAN)
        if local < FADE:
            # dojíždí předchozí záběr — ten pokračuje ve svém pohybu
            prev = (i - 1) % N
            frame = Image.blend(ken_burns(base, prev, (local + STEP) / SPAN),
                                frame, local / FADE)

        buf = io.BytesIO()
        frame.save(buf, "JPEG", quality=93, subsampling=0)
        ff.stdin.write(buf.getvalue())

    ff.stdin.close()
    if ff.wait() != 0:
        raise SystemExit("build-video: ffmpeg skončil s chybou")
    return OUT


if __name__ == "__main__":
    out = build()
    print(f"{out.relative_to(ROOT)}  {out.stat().st_size / 1024:.0f} KB  ({TOTAL:.1f} s)")
