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

## 11. Przypadki graniczne, punkty szczególne i przykłady referencyjne

### 11.1. Zakres analizy

Niniejszy rozdział opisuje szczególne klasy chwil bazowych, dla których model przyjmuje wartości skrajne, zerowe albo strukturalnie istotne.

Celem rozdziału jest:

* identyfikacja punktów idealnej ortogonalności,
* identyfikacja punktów maksymalnego oddalenia od ortogonalności,
* opisanie zachowania funkcji na granicach cyklu,
* ustanowienie przykładów referencyjnych do testów zgodności implementacji.

### 11.2. Stan idealnej ortogonalności

Stan idealnej ortogonalności zachodzi wtedy i tylko wtedy, gdy:

`D(T) = 90`

co jest równoważne warunkowi:

`O(T) = 0`

oraz:

`Orth(T) = 0`

Interpretacja:

* wskazania są względem siebie prostopadłe w przestrzeni zsymetryzowanej,
* układ osiąga stan zerowego odchylenia ortogonalnego,
* czas ortogonalny osiąga minimum globalne.

### 11.3. Stan maksymalnego oddalenia od ortogonalności

Stan maksymalnego oddalenia zachodzi wtedy, gdy:

`D(T) = 0`

co implikuje:

`O(T) = 90`

oraz:

`Orth(T) = 90`

Interpretacja:

* wskazania pokrywają się w przestrzeni zredukowanej lub tworzą relację równoważną zerowej różnicy,
* układ osiąga maksimum odchylenia względem ortogonalności.

### 11.4. Chwile klasyczne o szczególnym znaczeniu strukturalnym

Poniższe chwile klasyczne pełnią rolę punktów odniesienia dla analizy systemu.

#### 11.4.1. Chwila 12:00:00

Dla `h = 12`, `m = 0`, `s = 0`:

* `h12 = 0`
* `H(T) = 0`
* `M(T) = 0`
* `Hr(T) = 0`
* `Mr(T) = 0`
* `D(T) = 0`
* `Orth(T) = 90`

Chwila 12:00:00 jest punktem maksymalnego oddalenia od ortogonalności.

#### 11.4.2. Chwila 6:00:00

Dla `h = 6`, `m = 0`, `s = 0`:

* `h12 = 6`
* `H(T) = 180`
* `M(T) = 0`
* `Hr(T) = 0`
* `Mr(T) = 0`
* `D(T) = 0`
* `Orth(T) = 90`

Chwila 6:00:00 jest równoważna 12:00:00 w przestrzeni zredukowanej.

#### 11.4.3. Chwila 3:00:00

Dla `h = 3`, `m = 0`, `s = 0`:

* `h12 = 3`
* `H(T) = 90`
* `M(T) = 0`
* `Hr(T) = 90`
* `Mr(T) = 0`
* `D(T) = 90`
* `Orth(T) = 0`

Chwila 3:00:00 jest punktem idealnej ortogonalności.

#### 11.4.4. Chwila 9:00:00

Dla `h = 9`, `m = 0`, `s = 0`:

* `h12 = 9`
* `H(T) = 270`
* `M(T) = 0`
* `Hr(T) = 90`
* `Mr(T) = 0`
* `D(T) = 90`
* `Orth(T) = 0`

Chwila 9:00:00 jest równoważna 3:00:00 w przestrzeni zredukowanej.

### 11.5. Klasy równoważności podstawowej

Z uwagi na redukcję modulo 180 stopni oraz symetryzację różnicy, model podstawowy tworzy klasy równoważności chwil, które w czasie klasycznym są różne, ale w przestrzeni ortogonalnej mają tę samą wartość `Orth(T)`.

Przykładowo:

* 12:00 i 6:00 należą do tej samej klasy maksymalnego oddalenia,
* 3:00 i 9:00 należą do tej samej klasy idealnej ortogonalności.

Wynika stąd, że Chronometria Ortogonalna nie zachowuje pełnej jednoznaczności odwrotnego mapowania do czasu klasycznego.

### 11.6. Zachowanie na granicy godzin i minut

Funkcje `H(T)` oraz `M(T)` są ciągłe względem czasu bazowego, jeśli `T` traktowane jest jako wielkość ciągła.

W konsekwencji także:

* `Hr(T)` jest funkcją odcinkowo ciągłą,
* `Mr(T)` jest funkcją odcinkowo ciągłą,
* `D(T)` jest funkcją ciągłą,
* `O(T)` jest funkcją ciągłą,
* `Orth(T)` jest funkcją ciągłą.

Nieciągłości mogą pojawić się wyłącznie na poziomie reprezentacji dyskretnej, na przykład przy obcinaniu części ułamkowej do `Orth_int(T)` i `Centi(T)`.

### 11.7. Punkty krytyczne

Punkty krytyczne modelu obejmują:

1. minima globalne: chwile, dla których `Orth(T) = 0`,
2. maksima globalne: chwile, dla których `Orth(T) = 90`,
3. punkty przejścia przez ortogonalność,
4. punkty przejścia przez pokrycie wskazań,
5. granice klasyfikacji sferycznej, jeśli sfera pozostaje definiowana przez segmentację godzinową.

### 11.8. Przykłady referencyjne

Poniższe przykłady mają status referencyjny dla implementacji zgodnych z wersją 0.1 specyfikacji.

#### Przykład A — 01:00:00

* `h12 = 1`
* `H(T) = 30`
* `M(T) = 0`
* `Hr(T) = 30`
* `Mr(T) = 0`
* `D0(T) = 30`
* `D(T) = 30`
* `Orth(T) = 60`

#### Przykład B — 02:00:00

* `h12 = 2`
* `H(T) = 60`
* `M(T) = 0`
* `Hr(T) = 60`
* `Mr(T) = 0`
* `D0(T) = 60`
* `D(T) = 60`
* `Orth(T) = 30`

#### Przykład C — 03:00:00

* `h12 = 3`
* `H(T) = 90`
* `M(T) = 0`
* `Hr(T) = 90`
* `Mr(T) = 0`
* `D0(T) = 90`
* `D(T) = 90`
* `Orth(T) = 0`

#### Przykład D — 04:00:00

* `h12 = 4`
* `H(T) = 120`
* `M(T) = 0`
* `Hr(T) = 120`
* `Mr(T) = 0`
* `D0(T) = 120`
* `D(T) = 60`
* `Orth(T) = 30`

#### Przykład E — 05:00:00

* `h12 = 5`
* `H(T) = 150`
* `M(T) = 0`
* `Hr(T) = 150`
* `Mr(T) = 0`
* `D0(T) = 150`
* `D(T) = 30`
* `Orth(T) = 60`

#### Przykład F — 06:00:00

* `h12 = 6`
* `H(T) = 180`
* `M(T) = 0`
* `Hr(T) = 0`
* `Mr(T) = 0`
* `D0(T) = 0`
* `D(T) = 0`
* `Orth(T) = 90`

### 11.9. Symetria pierwszego półcyklu

Dla pełnych godzin od 12:00 do 6:00 model wykazuje następującą strukturę wartości:

* 12:00 → 90
* 1:00 → 60
* 2:00 → 30
* 3:00 → 0
* 4:00 → 30
* 5:00 → 60
* 6:00 → 90

Struktura ta ujawnia symetrię wokół punktu ortogonalnego 3:00 oraz maksimum w punktach zgodnych lub zredukowanie zgodnych.

### 11.10. Znaczenie testowe przykładów referencyjnych

Każda implementacja zgodna z wersją 0.1 musi zwracać wartości zgodne z przykładami referencyjnymi dla chwil pełnogodzinnych opisanych w niniejszym rozdziale, z uwzględnieniem przyjętej reguły zaokrąglania i reprezentacji części ułamkowej.

## 12. Relacja do czasu klasycznego

### 12.1. Charakter odwzorowania

Chronometria Ortogonalna nie zastępuje w wersji 0.1 klasycznego czasu cywilnego, lecz definiuje alternatywne odwzorowanie chwili bazowej do relacyjnej przestrzeni geometrycznej.

Odwzorowanie to ma postać:

`F: T -> OT(T)`

gdzie `T` jest chwilą bazową w przyjętej skali źródłowej, a `OT(T)` stanem Czasu Ortogonalnego.

W wersji podstawowej system jest więc funkcją wtórną względem czasu źródłowego, a nie autonomiczną skalą pierwotną.

### 12.2. Co system zachowuje

Chronometria Ortogonalna zachowuje następujące własności czasu klasycznego:

1. zależność od chwili bazowej,
2. ciągłość zmian przy ciągłym traktowaniu czasu wejściowego,
3. okresowość wynikającą z ruchu wskazań,
4. możliwość systematycznej konwersji z czasu klasycznego do czasu ortogonalnego,
5. deterministyczność odwzorowania przy ustalonym modelu wejścia.

Oznacza to, że dla każdej poprawnie zdefiniowanej chwili bazowej wynik czasu ortogonalnego jest jednoznacznie wyznaczony.

### 12.3. Czego system nie zachowuje

Chronometria Ortogonalna nie zachowuje wszystkich własności klasycznego czasu zegarowego.

W szczególności system nie zachowuje:

1. pełnej jednoznaczności odwrotnego odwzorowania,
2. liniowego znaczenia minut jako podstawowej jednostki odczytu,
3. pełnej rozróżnialności stanów różniących się o klasy równoważne w przestrzeni zredukowanej,
4. bezpośredniej zgodności z urzędowymi skalami czasu bez użycia chwili bazowej.

W konsekwencji Czas Ortogonalny nie jest w wersji 0.1 samowystarczalnym substytutem czasu cywilnego dla zastosowań administracyjnych, prawnych ani infrastrukturalnych.

### 12.4. Jednoznaczność i niejednoznaczność

Mapowanie z czasu klasycznego do Czasu Ortogonalnego jest funkcją jednoznaczną.

Dla ustalonej chwili bazowej `T` istnieje dokładnie jeden stan `OT(T)` zgodny ze specyfikacją.

Jednak mapowanie odwrotne nie jest jednoznaczne.

Istnieją różne chwile bazowe `T1` i `T2`, dla których:

`Orth(T1) = Orth(T2)`

oraz nawet:

`OT_partial(T1) = OT_partial(T2)`

gdzie `OT_partial` oznacza zapis nieuwzględniający pełnej informacji o źródle chwili bazowej.

Jest to konsekwencja:

* redukcji modulo 180 stopni,
* symetryzacji względem 90 stopni,
* okresowości ruchu wskazań,
* możliwego pomijania dodatkowych współrzędnych identyfikujących chwilę źródłową.

### 12.5. Relacja do minut i godzin

W klasycznym modelu godziny i minuty są jednostkami odczytu pierwotnego.

W Chronometrii Ortogonalnej godzina i minuta nie są odczytem końcowym, lecz parametrami pośrednimi używanymi do wyznaczenia położeń kątowych.

Oznacza to przejście:

* z modelu indeksowego do modelu relacyjnego,
* z modelu segmentowego do modelu geometrycznego,
* z modelu numeracji do modelu odchylenia i struktury.

### 12.6. Relacja do czasu analogowego

Chronometria Ortogonalna pozostaje silnie związana z geometrią tarczy analogowej, ponieważ jej podstawowy model wykorzystuje położenia odpowiadające wskazaniu godzinowemu i minutowemu.

Nie oznacza to jednak, że system musi być ograniczony do fizycznego zegara analogowego.

Model analogowy należy traktować jako pierwszą realizację przestrzeni odniesienia, a nie jako jedyne możliwe ucieleśnienie systemu.

W dalszym rozwoju możliwe jest uogólnienie systemu do abstrakcyjnej przestrzeni fazowej, niezależnej od klasycznej tarczy zegarowej.

### 12.7. Relacja do czasu cyfrowego

Czas cyfrowy zapisuje chwilę przez parę liczb lub ciąg liczb dyskretnych.

Chronometria Ortogonalna nie korzysta z takiej reprezentacji jako formy pierwotnej odczytu. Zamiast tego przekształca dane liczbowe do relacji kątowych, a następnie do wartości ortogonalnej.

Z tego względu system może być implementowany cyfrowo, ale nie jest systemem cyfrowym w sensie ontologicznym.

### 12.8. Relacja do UTC, czasu lokalnego i Unix time

UTC, czas lokalny oraz Unix time mogą pełnić rolę skali bazowej wejścia.

Chronometria Ortogonalna nie konkuruje z nimi bezpośrednio w warstwie źródłowej, ponieważ nie definiuje w wersji 0.1 własnego niezależnego mechanizmu wyznaczania chwili absolutnej.

Zamiast tego system działa jako formalna transformacja chwili bazowej do postaci ortogonalnej.

W praktyce oznacza to, że:

* UTC może służyć jako neutralna skala wejściowa,
* czas lokalny może służyć jako skala użytkowa,
* Unix time może służyć jako skala implementacyjna.

### 12.9. Relacja do odwracalności

W systemie klasycznym zapis godziny i minuty zazwyczaj pozwala wprost odtworzyć stan czasu w danym formacie.

W Chronometrii Ortogonalnej wartość `Orth(T)` sama w sobie nie wystarcza do jednoznacznego odtworzenia chwili bazowej.

Nawet rozszerzony zapis z Cyklem i Sferą może nie być wystarczający, jeśli nie zawiera dodatkowego kontekstu źródłowego.

Wynika stąd fundamentalna cecha systemu:

Chronometria Ortogonalna jest bardziej systemem projekcji i klasyfikacji relacyjnej niż pełnym kodem odwracalnym chwili źródłowej.

### 12.10. Relacja do obiektywności

W klasycznym sensie infrastrukturalnym obiektywność czasu oznacza zgodność ze wspólną, stabilną i synchronizowalną skalą odniesienia, taką jak UTC.

Chronometria Ortogonalna nie spełnia jeszcze w wersji 0.1 tego kryterium jako niezależny system infrastrukturalny.

Może jednak rościć sobie prawo do obiektywności w sensie formalnym i geometrycznym, o ile:

1. reguły transformacji są ścisłe,
2. wynik nie zależy od subiektywnej interpretacji obserwatora,
3. każda chwila bazowa daje deterministyczny wynik,
4. system jest spójny matematycznie.

Dlatego w obecnej postaci należy mówić przede wszystkim o obiektywności transformacyjnej lub geometrycznej, a nie o pełnej obiektywności infrastrukturalnej.

### 12.11. Status epistemiczny systemu

Chronometria Ortogonalna może być rozumiana równocześnie jako:

* formalny system transformacji czasu,
* alternatywna reprezentacja chwili,
* model relacyjny czasu zegarowego,
* propozycja nowej chronometrii.

W wersji 0.1 najbardziej uzasadnione jest traktowanie jej jako formalnego systemu transformacji i reprezentacji, który dopiero w dalszym rozwoju może aspirować do statusu autonomicznej skali czasu.

### 12.12. Wniosek porównawczy

Czas klasyczny odpowiada przede wszystkim na pytanie: „która jest godzina według przyjętej skali podziału?”.

Czas Ortogonalny odpowiada przede wszystkim na pytanie: „jaki jest relacyjny stan geometryczny chwili w przestrzeni cyklicznej?”.

Oba systemy opisują tę samą chwilę bazową, lecz czynią to za pomocą odmiennych zasad organizacji informacji.

## 13. Plan dalszej rozbudowy dokumentu

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
