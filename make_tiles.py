"""Tnie NASA Blue Marble (equirectangular 21600x10800, lon -180..180) na piramidę kafelków WebP.

Układ: tiles/<z>/<y>_<x>.webp, kafelek TILE px. Poziom z ma szerokość BASE * 2**z
(z=1: 8192x4096 → 8x4 kafelki, z=2: 16384x8192 → 16x8). Poziom 0 to istniejący
earth-blue-marble-4k.webp w TIMPORYE (nie generujemy go tutaj).

Użycie: python make_tiles.py world.topo.bathy.200412.3x21600x10800.jpg out/
"""
import pathlib
import sys

from PIL import Image

Image.MAX_IMAGE_PIXELS = None
TILE = 1024
BASE = 4096
LEVELS = (1, 2)
QUALITY = 72


def main(src: str, out: str) -> None:
    img = Image.open(src).convert("RGB")
    for z in LEVELS:
        w = BASE * 2 ** z
        level = img.resize((w, w // 2), Image.LANCZOS)
        for y in range(level.height // TILE):
            for x in range(w // TILE):
                path = pathlib.Path(out, "tiles", str(z), f"{y}_{x}.webp")
                path.parent.mkdir(parents=True, exist_ok=True)
                level.crop((x * TILE, y * TILE, (x + 1) * TILE, (y + 1) * TILE)) \
                    .save(path, "WEBP", quality=QUALITY, method=6)
        print(f"z={z}: {w}x{w // 2}, {(w // TILE) * (w // 2 // TILE)} kafelków")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
