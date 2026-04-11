# Projekt: Zegar Systemu 3-9 (Chronometria Ortogonalna)

## 💡 Opis Koncepcji
Autorski system organizacji i odczytu czasu bazujący na geometrii wskazówek klasycznego zegara. Projekt odrzuca tradycyjny podział godziny na 60 równych minut na rzecz badania napięcia geometrycznego między wskazówkami.

### Główne Założenia:
* **Wskazówka minutowa** działa jako linia przechodząca przez całą tarczę (średnica).
* **Osią bazową (horyzontem)** systemu są godziny `3:00` i `9:00`. Dzielą one dobę na sferę górną (dzień/szczyt) oraz dolną (noc/odpoczynek).

---

## ⏳ Jak odczytywać czas w Systemie 3-9?

Zapis czasu w tym systemie składa się z trzech elementów, np.: **`[+] Cykl: 3 | Ortos: 0.06`**

1. **Sfera `[+]` lub `[-]`** - Określa, czy czas znajduje się w górnej sferze dobowej (nad linią 3-9), czy w dolnej (pod linią 3-9).
2. **Cykl** - Odpowiednik tradycyjnej godziny (od 0 do 11). Stanowi fundament, na którym opiera się układ.
3. **Ortos** - Nowa jednostka określająca minuty. Jest to **stopień odchylenia od prostopadłości** linii minutowej względem wskazówki godzinowej (od wartości `0` do `90`). 
   * Wartość `0` (Moment Ortos) to stan idealnej harmonii i prostopadłości (krzyż prosty).

---

## 📁 Zawartość Repozytorium
* `skala.txt` - Dowód matematyczny z wykazem 22 momentów pełnej prostopadłości w cyklu 12-godzinnym.
* `zegar.py` - Kod źródłowy w języku Python. W pełni funkcjonalny symulator graficzny odliczający czas w Cyklach i Ortosach.

## ⚖️ Prawa Autorskie
Copyright (c) 2026. Wszelkie prawa zastrzeżone. Kod źródłowy oraz koncepcja matematyczna są prywatną własnością autora tego repozytorium. Kopiowanie, rozpowszechnianie oraz wykorzystywanie bez zgody autora jest zabronione.
