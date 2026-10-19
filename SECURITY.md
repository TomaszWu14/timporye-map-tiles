# Bezpieczeństwo

## Zgłaszanie podatności
Podatności zgłaszaj **prywatnie** — nie przez publiczne issue ani PR (repozytorium jest publiczne):
przez GitHub *Security → Report a vulnerability*
(https://github.com/TomaszWu14/timporye-map-tiles/security/advisories/new).

Podaj: SHA commita lub nazwę wydania, opis problemu, kroki odtworzenia i możliwy skutek.
Odpowiedź — najczęściej do 7 dni.

## Zakres
- Gałąź domyślna `main`: skrypt `make_tiles.py` i dokumentacja; wydania z kafelkami (`tiles.tar.gz`).
- Poza zakresem: aplikacja TIMPORYE (osobne repozytorium, własne `SECURITY.md`) oraz dane źródłowe NASA.

## Automatyczne kontrole (CI)
| Narzędzie | Co robi | Kiedy |
|---|---|---|
| **gitleaks** (przypięta wersja + sha256) | sekrety w historii gita | każdy PR (jego commity), push do `main`, co tydzień i ręcznie (cała historia) — `.github/workflows/security.yml` |
| **Dependabot** | aktualizacje akcji GitHub przypiętych do SHA | co tydzień — `.github/dependabot.yml` |
