
# Chronometria Ortogonalna

## Specyfikacja systemu czasu — wersja 0.1 (szkic roboczy)

## Status dokumentu

Dokument roboczy. Celem tej wersji jest oddzielenie rdzenia matematycznego systemu od warstwy reprezentacji, wizualizacji i implementacji programistycznej.

---

## 1. Wprowadzenie

Chronometria Ortogonalna jest propozycją alternatywnego systemu opisu czasu, w którym podstawową wielkością nie jest liniowy podział godziny na 60 minut, lecz relacja geometryczna między położeniami dwóch wskazań kątowych odpowiadających ruchowi godzinowemu i minutowemu.

W klasycznym modelu zegarowym czas jest odczytywany przez wartości przypisane arbitralnie do podziału tarczy. W Chronometrii Ortogonalnej odczyt wynika z relacji, napięcia i odchylenia geometrycznego względem stanu ortogonalnego. Oznacza to przejście od modelu indeksowego do modelu relacyjnego.

Chronometria Ortogonalna nie jest na tym etapie próbą zastąpienia czasu fizycznego, atomowego ani urzędowego. Jest formalnym systemem reprezentacji czasu opartym na geometrii oraz kandydatem na niezależny model chronometryczny.

---

## 2. Cel dokumentu

Celem niniejszej specyfikacji jest:

1. zdefiniowanie matematycznego rdzenia Chronometrii Ortogonalnej,
2. oddzielenie teorii czasu od mechanizmu jego wskazywania,
3. opisanie zasad konwersji z czasu bazowego do czasu ortogonalnego,
4. ustanowienie pojęć, jednostek, notacji i własności systemu,
5. przygotowanie podstaw pod implementacje referencyjne, narzędzia wizualne i przyszłe protokoły dystrybucji czasu ortogonalnego.

---

## 3. Zakres systemu

Niniejsza specyfikacja obejmuje:

* definicje podstawowych pojęć,
* model geometryczny czasu ortogonalnego,
* sposób wyznaczania wartości czasu ortogonalnego,
* strukturę cykli i sfer,
* zasady notacji,
* relację systemu do klasycznego czasu zegarowego,
* ograniczenia modelu i pytania otwarte.

Specyfikacja nie obejmuje w tej wersji:

* protokołu sieciowego synchronizacji,
* standardu interoperacyjności z systemami operacyjnymi,
* formalnej standaryzacji międzynarodowej,
* mechanicznej konstrukcji urządzeń wskazujących.

---

## 4. Rozdzielenie pojęć

Dla zachowania ścisłości rozróżnia się następujące byty:

### 4.1. Chronometria Ortogonalna

Formalny system opisu czasu oparty na relacji geometrycznej między wskazaniami kątowymi.

### 4.2. Czas Ortogonalny

Konkretny stan czasu uzyskany przez zastosowanie reguł Chronometrii Ortogonalnej do chwili bazowej.

### 4.3. Zegar Ortogonalny

Dowolne urządzenie, program lub interfejs wizualny służący do prezentacji Czasu Ortogonalnego.

### 4.4. Implementacja referencyjna

Programowa realizacja algorytmu zgodnego z niniejszą specyfikacją.

---

## 5. Założenia ogólne

1. Czas ortogonalny jest funkcją chwili bazowej oraz jej reprezentacji kątowej.
2. Rdzeniem systemu jest relacja geometryczna, a nie arbitralny numer pozycji na podziałce.
3. Stanem odniesienia jest ortogonalność, rozumiana jako relacja kąta prostego między wskazaniami.
4. System dopuszcza warstwę interpretacyjną, ale nie może ona naruszać rdzenia matematycznego.
5. Reprezentacja wizualna systemu jest wtórna względem definicji formalnej.

---

## 6. Terminologia podstawowa

### 6.1. Chwila bazowa

Moment wejściowy pochodzący z przyjętej skali czasu źródłowego, na przykład UTC, czasu lokalnego lub znacznika Unix.

### 6.2. Reprezentacja kątowa

Przekształcenie chwili bazowej do dwóch położeń kątowych: godzinowego i minutowego.

### 6.3. Kąt godzinowy

Kąt odpowiadający położeniu wskazania godzinowego dla danej chwili bazowej.

### 6.4. Kąt minutowy

Kąt odpowiadający położeniu wskazania minutowego dla danej chwili bazowej.

### 6.5. Przestrzeń zredukowana

Przestrzeń kątowa po redukcji modulo 180 stopni, służąca do analizy relacji ortogonalnej.

### 6.6. Różnica kątowa

Bezwzględna różnica między zredukowanymi położeniami kątowymi.

### 6.7. Odchylenie ortogonalne

Miara oddalenia od relacji idealnej ortogonalności, wyrażona względem 90 stopni.

### 6.8. Orthos

Podstawowa wielkość czasu ortogonalnego będąca wartością wyprowadzoną z odchylenia ortogonalnego.

### 6.9. Centi

Część ułamkowa reprezentacji czasu ortogonalnego, wyrażona w setnych jednostki Orthos.

### 6.10. Trend

Kierunek lokalnej zmiany wartości czasu ortogonalnego pomiędzy kolejnymi stanami obserwacji albo jako własność funkcji w danym otoczeniu.

### 6.11. Cykl

Jednostka okresowości systemu związana z pełnym obiegiem struktury odniesienia.

### 6.12. Sfera

Warstwa klasyfikacji topologicznej lub strukturalnej czasu ortogonalnego, związana z położeniem względem osi odniesienia.

---

## 7. Aksjomaty systemu

### Aksjomat 1. Relacyjność

Czas ortogonalny jest określany przez relację geometryczną między dwoma wskazaniami kątowymi, a nie przez ich niezależne wartości indeksowe.

### Aksjomat 2. Symetryzacja

Dla celów analizy ortogonalnej przestrzeń relacji ulega redukcji do przestrzeni symetrycznej względem 180 stopni.

### Aksjomat 3. Uprzywilejowanie ortogonalności

Stan ortogonalny stanowi centralny punkt odniesienia systemu i wyznacza podstawową miarę odchylenia.

### Aksjomat 4. Dwuwarstwowość

System składa się z warstwy matematycznej i warstwy reprezentacyjnej. Warstwa reprezentacyjna nie definiuje systemu, lecz go ujawnia.

### Aksjomat 5. Okresowość

Czas ortogonalny jest osadzony w strukturze okresowej, której własności wynikają z geometrii ruchu wskazań.

---

## 8. Pytania rozstrzygające przed wersją 0.2

1. Czy chwila bazowa ma być definiowana względem UTC, Unix time czy lokalnego czasu cywilnego?
2. Czy sfera jest pojęciem czysto geometrycznym, czy częściowo interpretacyjnym?
3. Czy trend ma być własnością chwilową funkcji, czy tylko wynikiem porównania kolejnych próbek?
4. Czy system ma operować wyłącznie na modelu 12-godzinnym, czy ma mieć formalne rozszerzenie na czas ciągły?
5. Czy Centi jest jednostką formalną, czy jedynie konwencją zapisu?

---

## 9. Plan dalszej rozbudowy dokumentu

W kolejnych wersjach dokument zostanie rozszerzony o:

* formalne definicje matematyczne i wzory,
* analizę własności funkcji czasu ortogonalnego,
* klasy graniczne i punkty osobliwe,
* system notacji pełnej i skróconej,
* zgodność implementacji,
* przykłady konwersji,
* aneksy obliczeniowe.

---

## 10. Teza robocza

Chronometria Ortogonalna traktuje czas nie jako arbitralnie indeksowaną sekwencję jednostek, lecz jako stan relacyjny wynikający z geometrii współobecnych ruchów w przestrzeni cyklicznej.
