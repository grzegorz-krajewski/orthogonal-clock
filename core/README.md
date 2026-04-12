# Core

Ten katalog zawiera referencyjny rdzeń obliczeniowy Chronometrii Ortogonalnej.

## Zasady
- brak zależności od UI,
- brak ukrytego pobierania czasu systemowego w funkcjach rdzenia,
- rozdzielenie modelu, konwersji, notacji i trendu,
- testy referencyjne jako pierwsza linia obrony zgodności.

## Moduły
- `model.py` — struktury danych
- `converter.py` — matematyka konwersji
- `notation.py` — formatowanie
- `trend.py` — trend obserwacyjny
- `sphere.py` — robocza definicja sfery
