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

## 9. Model formalny i definicje matematyczne

### 9.1. Chwila bazowa

Niech chwila bazowa będzie oznaczona przez symbol `T`.

Chwila bazowa jest elementem przyjętej skali czasu źródłowego i stanowi wejście do procesu konwersji do Czasu Ortogonalnego.

W wersji 0.1 specyfikacja dopuszcza trzy klasy chwil bazowych:

1. czas lokalny cywilny,
2. czas uniwersalny skoordynowany (UTC),
3. znacznik czasu typu Unix.

Wewnętrzny model Chronometrii Ortogonalnej nie zależy od nazwy skali wejściowej, lecz od możliwości jednoznacznego przekształcenia chwili bazowej do reprezentacji kątowej.

### 9.2. Składowe chwili bazowej

Dla potrzeb podstawowego modelu przyjmuje się, że chwila bazowa `T` może zostać rozpisana na:

* godzinę `h`,
* minutę `m`,
* sekundę `s`.

W przypadku gdy sekunda nie jest dostępna, przyjmuje się `s = 0`.

Dla modelu 12-godzinnego definiuje się godzinę zredukowaną:

`h12 = h mod 12`

### 9.3. Reprezentacja kątowa

Chronometria Ortogonalna operuje na dwóch kątach pochodnych:

#### 9.3.1. Kąt godzinowy

Kąt godzinowy `H(T)` jest funkcją chwili bazowej i wyraża położenie wskazania godzinowego:

`H(T) = 30 * h12 + 0.5 * m + (1/120) * s`

#### 9.3.2. Kąt minutowy

Kąt minutowy `M(T)` jest funkcją chwili bazowej i wyraża położenie wskazania minutowego:

`M(T) = 6 * m + 0.1 * s`

Oba kąty wyrażane są w stopniach.

### 9.4. Redukcja ortogonalna

Niech funkcja redukcji półobrotu będzie dana wzorem:

`R(x) = x mod 180`

Wtedy zredukowane kąty ortogonalne przyjmują postać:

`Hr(T) = R(H(T))`

`Mr(T) = R(M(T))`

Redukcja do 180 stopni usuwa równoważności pełnego obrotu nieistotne z punktu widzenia relacji ortogonalnej.

### 9.5. Różnica kątowa

Definiuje się pierwotną różnicę kątową jako:

`D0(T) = |Hr(T) - Mr(T)|`

Ponieważ relacja ortogonalna jest symetryczna względem 90 stopni, definiuje się różnicę zsymetryzowaną:

`D(T) = min(D0(T), 180 - D0(T))`

Wynika stąd, że:

`0 <= D(T) <= 90`

### 9.6. Odchylenie ortogonalne

Definiuje się odchylenie ortogonalne `O(T)` jako odległość różnicy zsymetryzowanej od stanu idealnej ortogonalności:

`O(T) = |90 - D(T)|`

Zatem:

`0 <= O(T) <= 90`

Wartość `O(T) = 0` oznacza idealny stan ortogonalny.

Wartość `O(T) = 90` oznacza maksymalne oddalenie od ortogonalności w obrębie przestrzeni zsymetryzowanej.

### 9.7. Wartość czasu ortogonalnego

Podstawową skalarną wartością Czasu Ortogonalnego jest funkcja:

`Orth(T) = O(T)`

W wersji podstawowej `Orth(T)` jest wielkością rzeczywistą wyrażoną w stopniach ortogonalnych.

### 9.8. Rozbicie reprezentacyjne

Dla potrzeb zapisu i odczytu definiuje się:

`Orth_int(T) = floor(Orth(T))`

`Centi(T) = floor((Orth(T) - Orth_int(T)) * 100)`

gdzie:

* `Orth_int(T)` oznacza część całkowitą jednostki Orthos,
* `Centi(T)` oznacza dwucyfrową część setną reprezentacji.

Wersja 0.1 traktuje `Centi` jako element notacyjny reprezentacji liczby rzeczywistej, a nie jako niezależną jednostkę bazową systemu.

### 9.9. Cykl

Dla chwili bazowej `T` definiuje się cykl podstawowy:

`C(T) = h mod 12`

Wartość `C(T)` identyfikuje położenie chwili w strukturze 12-godzinnej.

W kolejnych wersjach specyfikacji zostanie rozstrzygnięte, czy Cykl ma być wyłącznie etykietą fazową, czy składnikiem formalnego indeksu czasu ortogonalnego.

### 9.10. Sfera

W wersji 0.1 definiuje się sferę roboczą jako klasyfikację binarną zależną od położenia godzinowego względem osi strukturalnej systemu.

Dla uproszczonego modelu implementacyjnego:

* jeśli `3 <= h12 < 9`, to `S(T) = [-]`,
* w przeciwnym razie `S(T) = [+]`.

Definicja ta ma status przejściowy.

W kolejnych wersjach zostanie zastąpiona definicją w pełni geometryczną, niezależną od prostego warunku godzinowego.

### 9.11. Trend

Trend opisuje kierunek zmiany wartości czasu ortogonalnego.

W wersji 0.1 rozróżnia się dwa typy trendu:

#### 9.11.1. Trend obserwacyjny

Dla dwóch kolejnych chwil obserwacji `T1` i `T2`, gdzie `T2 > T1`, definiuje się:

* trend rosnący, gdy `Orth(T2) > Orth(T1)`,
* trend malejący, gdy `Orth(T2) < Orth(T1)`,
* trend stały, gdy `Orth(T2) = Orth(T1)`.

#### 9.11.2. Trend lokalny

Trend lokalny jest własnością funkcji `Orth(T)` w otoczeniu chwili `T` i w przyszłych wersjach powinien być definiowany przez analizę przyrostu lub pochodnej względem czasu bazowego.

### 9.12. Pełny stan Czasu Ortogonalnego

Pełny stan czasu ortogonalnego dla chwili `T` może być zapisany jako uporządkowana struktura:

`OT(T) = (S(T), C(T), Orth(T), Orth_int(T), Centi(T), Trend)`

W zależności od zastosowania dopuszcza się zapis pełny lub skrócony.

## 10. Własności podstawowe modelu

### 10.1. Ograniczoność

Funkcja `Orth(T)` jest ograniczona i przyjmuje wartości z przedziału domkniętego `[0, 90]`.

### 10.2. Okresowość

Model podstawowy jest okresowy względem struktury 12-godzinnej wynikającej z ruchu wskazania godzinowego.

### 10.3. Symetria

Redukcja do przestrzeni 180 stopni oraz symetryzacja różnicy kątowej sprawiają, że model identyfikuje klasy stanów równoważnych względem półobrotu.

### 10.4. Centralność ortogonalności

Stan ortogonalny pełni funkcję punktu odniesienia, wobec którego definiowana jest wartość czasu ortogonalnego.

### 10.5. Wielowartościowość odwrotna

Nie gwarantuje się, że odwzorowanie z czasu klasycznego do czasu ortogonalnego jest odwracalne w sposób jednoznaczny.

Różne chwile bazowe mogą prowadzić do tej samej wartości `Orth(T)`.

## 11. Plan dalszej rozbudowy dokumentu

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
