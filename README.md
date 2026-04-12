# Orthogonal Clock / Chronometria Ortogonalna

Chronometria Ortogonalna to alternatywny system reprezentacji czasu, w którym podstawową wielkością nie jest arbitralny podział minutowy, lecz geometryczna relacja i odchylenie od ortogonalności w przestrzeni cyklicznej.

## Status projektu
Projekt znajduje się w fazie formowania rdzenia formalnego i implementacji referencyjnej.

Aktualnie repo rozdziela trzy warstwy:
- **spec/** — formalna specyfikacja systemu czasu,
- **core/** — referencyjny rdzeń obliczeniowy,
- **clock/** — warstwa prezentacji i interfejsów.

## Struktura repo
- `spec/orthogonal-time-spec-v0.1.md` — główna robocza specyfikacja systemu
- `core/orthogonal_time/` — logika obliczeniowa zgodna z wersją 0.1
- `core/tests/` — testy referencyjne i zgodności
- `clock/` — eksperymenty z zegarem i prezentacją
- `research/` — materiały badawcze i eksploracyjne
- `docs/` — dokumenty pomocnicze i publikacyjne

## Szybki start

```bash
cd core
python -m unittest discover -s tests -v
```

### Przykład użycia

```python
from orthogonal_time.converter import convert_hms
from orthogonal_time.notation import format_standard

state = convert_hms(hour=3, minute=0, second=0)
print(state.orth)              # 0.0
print(format_standard(state))  # [+] C3 O0.00 ?
```

## Założenia wersji 0.1
- rdzeń matematyczny jest określony,
- `Sphere` pozostaje częściowo robocza,
- `Trend` lokalny nie jest jeszcze formalnie domknięty,
- implementacja referencyjna rozdziela logikę obliczeniową od prezentacji.

## Roadmapa
1. domknięcie definicji Sfery,
2. formalizacja Trendu lokalnego,
3. rozszerzenie testów o chwile niepełnogodzinne,
4. demonstrator webowy klasyczny czas vs czas ortogonalny,
5. późniejsze eksperymenty z usługą czasu ortogonalnego.

## Licencja
Copyright (c) 2026 Grzegorz Krajewski. All Rights Reserved.
Wszelkie prawa zastrzeżone. Kod źródłowy oraz koncepcja matematyczna są prywatną własnością autora. Kopiowanie, rozpowszechnianie oraz wykorzystywanie bez zgody autora jest zabronione.
