# timporye-map-tiles

Kafelki mapy 2D (Blue Marble) dla aplikacji TIMPORYE — ostrzejszy obraz przy przybliżeniu.

- **Źródło:** NASA Visible Earth — *Blue Marble: Next Generation w/ Topography and Bathymetry*,
  grudzień 2004, `world.topo.bathy.200412.3x21600x10800.jpg`
  (https://visibleearth.nasa.gov/images/73909/december-blue-marble-next-generation-w-topography-and-bathymetry).
- **Autor:** Reto Stöckli, NASA Earth Observatory (dane: NASA GSFC).
- **Licencja:** domena publiczna (materiały NASA). Nie sugerujemy poparcia NASA, nie używamy logo NASA.

## Zawartość wydania

`tiles.tar.gz` → `tiles/<z>/<y>_<x>.webp`, kafelek 1024 px, projekcja equirectangular (lon −180…180):

| z | rozdzielczość | kafelki |
|---|---------------|---------|
| 1 | 8192 × 4096   | 8 × 4   |
| 2 | 16384 × 8192  | 16 × 8  |

Poziom 0 (4096 × 2048) jest w repo aplikacji. Odtworzenie: `python make_tiles.py <źródło.jpg> out/`
(Pillow, WebP q72).

## Bezpieczeństwo

CI (`.github/workflows/security.yml`) skanuje historię gita na sekrety narzędziem gitleaks (każdy PR,
push do `main`, co tydzień); Dependabot aktualizuje akcje GitHub. Podatności zgłaszaj prywatnie —
zob. [SECURITY.md](SECURITY.md).
