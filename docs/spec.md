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

## 13. Notacja i format zapisu

### 13.1. Cel notacji

Notacja Czasu Ortogonalnego służy do jednoznacznego przedstawiania stanu `OT(T)` w formie czytelnej dla człowieka oraz możliwej do przetwarzania maszynowego.

Dobra notacja powinna spełniać równocześnie cztery warunki:

1. zachowywać podstawowe składniki stanu ortogonalnego,
2. być zwięzła i możliwa do codziennego użycia,
3. nadawać się do serializacji w systemach informatycznych,
4. umożliwiać wersje skrócone i rozszerzone bez utraty spójności.

### 13.2. Składniki stanu notacyjnego

W wersji 0.1 pełny stan ortogonalny może zawierać następujące pola:

* `S` — Sfera,
* `C` — Cykl,
* `Orth` — pełna wartość czasu ortogonalnego,
* `Oi` — część całkowita `Orth`,
* `Ce` — część setna reprezentacji,
* `Tr` — Trend,
* `B` — opcjonalna informacja o chwili bazowej lub skali wejściowej.

### 13.3. Notacja pełna

Notacja pełna ma charakter opisowy i przeznaczona jest do dokumentacji, analizy, publikacji oraz interfejsów eksperckich.

Forma ogólna:

`OT[S=<sfera>; C=<cykl>; Orth=<wartość>; Oi=<część_całkowita>; Ce=<centi>; Tr=<trend>]`

Przykład:

`OT[S=+; C=3; Orth=0.00; Oi=0; Ce=00; Tr=↑]`

Notacja pełna może zostać rozszerzona o pole źródłowe:

`OT[S=+; C=3; Orth=0.00; Oi=0; Ce=00; Tr=↑; B=UTC:2026-04-12T03:00:00Z]`

### 13.4. Notacja standardowa użytkowa

Notacja standardowa użytkowa służy do codziennego prezentowania stanu czasu ortogonalnego człowiekowi.

Forma ogólna:

`[<sfera>] C<cykl> O<Oi>.<Ce> <trend>`

Przykład:

`[+] C3 O0.00 ↑`

lub:

`[-] C5 O60.00 ↓`

W tej formie:

* sfera pozostaje znakiem prefiksowym,
* cykl jest oznaczany literą `C`,
* wartość Orthos oznaczana jest literą `O`,
* trend pozostaje symbolem końcowym.

### 13.5. Notacja skrócona

Notacja skrócona przeznaczona jest dla interfejsów o ograniczonej przestrzeni, wizualizacji, tarcz i widgetów.

Forma ogólna:

`<sfera><cykl>:<Oi>.<Ce><trend>`

Przykład:

`+3:0.00↑`

lub:

`-5:60.00↓`

W notacji skróconej zakłada się znajomość kontekstu systemu przez użytkownika.

### 13.6. Notacja minimalistyczna

W szczególnych zastosowaniach dopuszcza się notację ograniczoną do samej wartości ortogonalnej:

`O<Oi>.<Ce>`

Przykład:

`O30.25`

Notacja minimalistyczna nie jest wystarczająca do pełnej identyfikacji stanu, ponieważ pomija Sferę, Cykl i Trend.

Może być stosowana wyłącznie tam, gdzie kontekst jest dostarczany innym kanałem.

### 13.7. Notacja maszynowa

Dla zastosowań informatycznych zaleca się zapis strukturalny.

Przykładowa reprezentacja JSON:

```json
{
  "system": "orthogonal-time",
  "version": "0.1",
  "sphere": "+",
  "cycle": 3,
  "orth": 0.0,
  "orth_int": 0,
  "centi": 0,
  "trend": "up",
  "base": {
    "scale": "UTC",
    "value": "2026-04-12T03:00:00Z"
  }
}
```

W przypadku braku źródła chwili bazowej pole `base` może zostać pominięte.

### 13.8. Trend w notacji

Dopuszcza się następujące symbole trendu:

* `↑` — trend rosnący,
* `↓` — trend malejący,
* `=` — trend stały,
* `?` — trend nieokreślony lub nieobliczony.

W zapisie maszynowym zaleca się formy tekstowe:

* `up`,
* `down`,
* `steady`,
* `unknown`.

### 13.9. Sfera w notacji

W wersji 0.1 dopuszcza się dwa symbole Sfery:

* `+` dla sfery dodatniej,
* `-` dla sfery ujemnej.

W zapisie maszynowym dopuszcza się również formy rozwinięte:

* `positive`,
* `negative`.

Jeżeli w przyszłych wersjach system zostanie rozszerzony o dodatkowe klasy topologiczne, notacja musi zachować zgodność wsteczną dla podstawowych oznaczeń `+` i `-`.

### 13.10. Cykl w notacji

Cykl zapisuje się jako liczbę całkowitą z zakresu wynikającego z modelu podstawowego.

W wersji 0.1 dla modelu 12-godzinnego przyjmuje się:

`C(T) ∈ {0,1,2,3,4,5,6,7,8,9,10,11}`

Dopuszczalne są dwa warianty prezentacji:

* wariant techniczny: `0–11`,
* wariant użytkowy: `1–12` z jawnym określeniem reguły mapowania.

W dokumentacji specyfikacyjnej zaleca się pozostanie przy wariancie technicznym `0–11` dla uniknięcia niejednoznaczności.

### 13.11. Zasady zaokrąglania i prezentacji

Wartość `Orth(T)` jest wielkością rzeczywistą.

W prezentacji człowiekowi dopuszcza się:

* zapis z dwoma miejscami po przecinku,
* zapis z obcięciem do dwóch miejsc po przecinku,
* zapis z klasycznym zaokrągleniem do dwóch miejsc po przecinku,
* zapis z większą precyzją dla zastosowań analitycznych.

Każda implementacja musi jawnie deklarować używaną regułę prezentacji.

Dla testów zgodności zaleca się rozdzielenie:

* wartości obliczeniowej `Orth(T)`,
* wartości prezentacyjnej `Orth_display(T)`.

### 13.12. Zgodność notacyjna

Implementacja zgodna z wersją 0.1 powinna:

1. umożliwiać wygenerowanie co najmniej jednej notacji czytelnej dla człowieka,
2. umożliwiać wygenerowanie jednej reprezentacji maszynowej,
3. zachowywać spójność między `Orth`, `Oi` i `Ce`,
4. jednoznacznie oznaczać status trendu,
5. nie mieszać warstwy źródłowej z warstwą ortogonalną bez jawnych oznaczeń.

### 13.13. Rekomendacja domyślna

W wersji 0.1 jako domyślną notację użytkową rekomenduje się:

`[<sfera>] C<cykl> O<Oi>.<Ce> <trend>`

Przykład:

`[+] C3 O0.00 ↑`

Natomiast jako domyślną notację maszynową rekomenduje się strukturę JSON zawierającą co najmniej pola:

* `sphere`,
* `cycle`,
* `orth`,
* `orth_int`,
* `centi`,
* `trend`.

## 14. Zgodność implementacji i wymagania referencyjne

### 14.1. Cel rozdziału

Celem niniejszego rozdziału jest określenie minimalnych warunków, jakie musi spełnić implementacja Chronometrii Ortogonalnej, aby mogła zostać uznana za zgodną ze specyfikacją w wersji 0.1.

Zgodność implementacji oznacza zgodność z:

* definicjami matematycznymi,
* regułami notacji,
* wymaganiami dotyczącymi reprezentacji,
* przykładami referencyjnymi,
* zasadami jawnego deklarowania ograniczeń i przyjętych uproszczeń.

### 14.2. Klasy implementacji

W wersji 0.1 rozróżnia się następujące klasy implementacji:

#### 14.2.1. Implementacja obliczeniowa

Implementacja, która potrafi dla danej chwili bazowej obliczyć co najmniej wartość `Orth(T)` oraz jej podstawowe składniki.

#### 14.2.2. Implementacja prezentacyjna

Implementacja, która potrafi zaprezentować stan czasu ortogonalnego człowiekowi, lecz może korzystać z zewnętrznego silnika obliczeniowego.

#### 14.2.3. Implementacja referencyjna

Implementacja, która realizuje pełny rdzeń matematyczny, wspiera rekomendowaną notację i przechodzi zestaw testów referencyjnych określonych w tej specyfikacji.

#### 14.2.4. Implementacja eksperymentalna

Implementacja rozszerzająca model podstawowy o dodatkowe elementy interpretacyjne, wizualne lub protokołowe, które nie są jeszcze częścią wersji 0.1.

### 14.3. Wymagania minimalne dla zgodności obliczeniowej

Aby implementacja była zgodna obliczeniowo z wersją 0.1, musi:

1. przyjmować chwilę bazową `T` lub dane pozwalające ją jednoznacznie wyznaczyć,
2. obliczać `H(T)` zgodnie z definicją specyfikacji,
3. obliczać `M(T)` zgodnie z definicją specyfikacji,
4. stosować redukcję `R(x) = x mod 180`,
5. obliczać `D0(T)` jako bezwzględną różnicę zredukowanych kątów,
6. obliczać `D(T) = min(D0(T), 180 - D0(T))`,
7. obliczać `O(T) = |90 - D(T)|`,
8. zwracać `Orth(T)` jako wartość równą `O(T)`.

Brak któregokolwiek z powyższych elementów uniemożliwia uznanie implementacji za zgodną z rdzeniem matematycznym systemu.

### 14.4. Wymagania minimalne dla zgodności reprezentacyjnej

Aby implementacja była zgodna reprezentacyjnie z wersją 0.1, musi:

1. zwracać co najmniej jedną notację czytelną dla człowieka albo strukturę maszynową,
2. zachowywać spójność pomiędzy `Orth(T)`, `Orth_int(T)` i `Centi(T)`,
3. jawnie oznaczać zastosowaną regułę zaokrąglania lub obcinania,
4. nie prezentować trendu jako wartości pewnej, jeśli nie został on obliczony,
5. nie mieszać chwili bazowej z czasem ortogonalnym bez jawnego rozróżnienia pól.

### 14.5. Wymagania minimalne dla zgodności referencyjnej

Implementacja referencyjna powinna dodatkowo:

1. wspierać notację rekomendowaną `[<sfera>] C<cykl> O<Oi>.<Ce> <trend>`,
2. wspierać reprezentację maszynową z polami określonymi w rozdziale 13,
3. przechodzić zestaw przykładów referencyjnych z rozdziału 11,
4. deklarować przyjętą skalę chwili bazowej,
5. deklarować, czy sekundy są uwzględniane,
6. deklarować sposób wyznaczania Sfery,
7. deklarować sposób wyznaczania Trendu.

### 14.6. Wymagania dotyczące chwili bazowej

Każda implementacja musi jawnie określić, z jakiej skali wejściowej korzysta.

Dopuszczalne są między innymi:

* lokalny czas cywilny,
* UTC,
* Unix time,
* własna skala wejściowa pod warunkiem, że można ją jednoznacznie przekształcić do `h`, `m`, `s`.

Implementacja nie może ukrywać tej decyzji, ponieważ wybór skali wejściowej wpływa na interpretację wyniku.

### 14.7. Wymagania dotyczące precyzji

Implementacja musi rozróżniać:

* precyzję obliczeniową,
* precyzję prezentacyjną.

Zaleca się, aby wewnętrzne obliczenia były prowadzone z większą dokładnością niż końcowa prezentacja.

Obcięcie lub zaokrąglenie do dwóch miejsc po przecinku nie może zmieniać logiki obliczeniowej rdzenia systemu.

### 14.8. Status Sfery i Trendu

W wersji 0.1:

* Sfera ma status częściowo przejściowy,
* Trend ma status częściowo zależny od sposobu obserwacji.

Dlatego implementacja może być zgodna z rdzeniem matematycznym nawet wtedy, gdy:

* nie udostępnia Sfery,
* oznacza Trend jako `unknown`,
* korzysta z roboczej definicji Sfery i obserwacyjnej definicji Trendu.

Jednak implementacja nie może przedstawiać tych elementów jako ostatecznie domkniętych, jeśli korzysta z wersji roboczych.

### 14.9. Testy referencyjne minimalne

Każda implementacja zgodna z wersją 0.1 powinna poprawnie odtwarzać co najmniej następujące przypadki:

1. `12:00:00 -> Orth = 90`
2. `03:00:00 -> Orth = 0`
3. `06:00:00 -> Orth = 90`
4. `09:00:00 -> Orth = 0`
5. `01:00:00 -> Orth = 60`
6. `02:00:00 -> Orth = 30`
7. `04:00:00 -> Orth = 30`
8. `05:00:00 -> Orth = 60`

Zaleca się również rozszerzenie testów o wartości z sekundami i o chwile niepełnogodzinne.

### 14.10. Niezgodności krytyczne

Za niezgodność krytyczną uznaje się między innymi:

1. brak redukcji do 180 stopni,
2. użycie niewłaściwej definicji różnicy kątowej,
3. użycie wartości innej niż `|90 - D(T)|` jako podstawy `Orth(T)`,
4. niespójność między wynikiem liczbowym a jego reprezentacją tekstową,
5. przypisywanie pełnej zgodności wersji 0.1 przy pominięciu wymogów matematycznych.

### 14.11. Niezgodności dopuszczalne warunkowo

Dopuszczalne warunkowo są różnice dotyczące:

* formatu wyświetlania,
* kolejności pól w reprezentacji maszynowej,
* obecności lub braku pola `base`,
* wyboru dokładności prezentacyjnej,
* sposobu oznaczania trendu, o ile jest on jasno zadeklarowany.

### 14.12. Deklaracja zgodności

Implementacja, która chce powoływać się na zgodność z wersją 0.1, powinna zawierać deklarację w rodzaju:

`This implementation conforms to Orthogonal Time Specification v0.1 in its computational core.`

lub w wersji rozszerzonej:

`This implementation conforms to Orthogonal Time Specification v0.1 in its computational and representational layers, with experimental handling of sphere and trend.`

W dokumentacji polskiej dopuszcza się odpowiedniki:

`Ta implementacja jest zgodna z wersją 0.1 Specyfikacji Czasu Ortogonalnego w warstwie obliczeniowej.`

oraz:

`Ta implementacja jest zgodna z wersją 0.1 Specyfikacji Czasu Ortogonalnego w warstwie obliczeniowej i reprezentacyjnej, z eksperymentalną obsługą Sfery i Trendu.`

### 14.13. Rekomendacja dla implementacji wzorcowej

Implementacja wzorcowa powinna:

* przyjmować chwilę bazową jako jawny argument,
* nie opierać obliczeń wyłącznie na stanie globalnym programu,
* rozdzielać funkcje obliczeniowe od prezentacyjnych,
* udostępniać testy jednostkowe dla przypadków referencyjnych,
* pozwalać na rozszerzenie o kolejne wersje specyfikacji bez łamania zgodności wstecznej.

## 15. Ograniczenia, pytania otwarte i roadmapa teorii

### 15.1. Rola niniejszego rozdziału

Celem niniejszego rozdziału jest jawne wskazanie ograniczeń wersji 0.1, zidentyfikowanie pytań, które pozostają nierozstrzygnięte, oraz wyznaczenie kierunków rozwoju Chronometrii Ortogonalnej.

Jawne wskazywanie ograniczeń nie osłabia systemu. Przeciwnie — zwiększa jego wiarygodność, ponieważ odróżnia elementy domknięte formalnie od elementów eksploracyjnych.

### 15.2. Ograniczenie źródłowe

W wersji 0.1 Chronometria Ortogonalna nie definiuje własnej niezależnej skali czasu absolutnego.

System wymaga chwili bazowej pochodzącej z innego źródła, takiego jak:

* UTC,
* czas lokalny,
* Unix time,
* równoważna skala wejściowa.

Oznacza to, że obecna wersja jest systemem transformacji i reprezentacji, a nie jeszcze autonomicznym źródłem czasu infrastrukturalnego.

### 15.3. Ograniczenie odwracalności

Wartość `Orth(T)` oraz nawet rozszerzony stan ortogonalny nie gwarantują pełnej odwracalności do unikalnej chwili bazowej.

Jest to konsekwencja samej konstrukcji systemu:

* redukcji modulo 180 stopni,
* symetryzacji względem 90 stopni,
* okresowości ruchu wskazań,
* częściowej utraty informacji przy przejściu do reprezentacji relacyjnej.

W praktyce oznacza to, że Chronometria Ortogonalna nie jest jeszcze pełnym kodem chwili, lecz projekcją relacyjną chwili.

### 15.4. Ograniczenie modelu tarczowego

Model podstawowy wyrasta z geometrii klasycznej tarczy analogowej.

Jest to siła systemu, ponieważ dostarcza intuicyjnego modelu odniesienia, ale jednocześnie ograniczenie, ponieważ:

* wiąże system z reprezentacją historycznie ukształtowaną,
* może utrudniać rozszerzenie na systemy niezależne od modelu zegara wskazówkowego,
* pozostawia pytanie, czy relacja ortogonalna jest cechą samego czasu, czy wybranego sposobu jego geometryzacji.

### 15.5. Ograniczenie definicji Sfery

W wersji 0.1 Sfera posiada status przejściowy.

Jej obecna definicja zależy od segmentacji godzinowej i nie została jeszcze wyprowadzona wyłącznie z pełnego modelu geometrycznego.

W związku z tym:

* Sfera jest częścią użyteczną notacji,
* Sfera nie jest jeszcze elementem ostatecznie domkniętym matematycznie,
* przyszłe wersje muszą rozstrzygnąć, czy Sfera wynika z topologii modelu, z osi odniesienia, czy z dodatkowej warstwy interpretacyjnej.

### 15.6. Ograniczenie definicji Trendu

W wersji 0.1 Trend posiada podwójny status:

* jako trend obserwacyjny może być liczony między kolejnymi próbkami,
* jako trend lokalny nie został jeszcze w pełni zdefiniowany analitycznie.

Oznacza to, że Trend nie jest jeszcze całkowicie niezależną własnością chwili, lecz częściowo zależy od sposobu próbkowania i obserwacji.

### 15.7. Ograniczenie ontologiczne

Wersja 0.1 nie rozstrzyga jeszcze jednoznacznie, czy Chronometria Ortogonalna ma być rozumiana jako:

* alternatywna reprezentacja istniejącego czasu,
* nowa klasa czasu relacyjnego,
* teoria pomocnicza do reinterpretacji czasu zegarowego,
* kandydat na autonomiczną skalę chronometryczną.

Dokument celowo pozostawia tę kwestię częściowo otwartą, aby nie nadawać systemowi statusu szerszego, niż uzasadnia aktualny poziom formalizacji.

### 15.8. Ograniczenie infrastrukturalne

Wersja 0.1 nie definiuje:

* protokołu synchronizacji sieciowej,
* mechanizmu dystrybucji czasu ortogonalnego,
* formatu interoperacyjności z systemami operacyjnymi,
* warstwy zgodności z istniejącymi protokołami czasu.

Dlatego system nie może być jeszcze traktowany jako zamiennik infrastrukturalny dla UTC, NTP ani pokrewnych standardów.

### 15.9. Ograniczenie semantyczne

W wersji 0.1 nie zostało jeszcze ostatecznie ustalone, czy jednostki takie jak `Orthos`, `Centi`, `Cykl` i `Sfera` mają charakter:

* wyłącznie operacyjny,
* częściowo ontologiczny,
* w pełni formalno-aksjomatyczny.

W szczególności `Centi` jest obecnie traktowane jako element reprezentacji liczby, a nie jako niezależna jednostka fundamentalna systemu.

### 15.10. Pytania otwarte — rdzeń matematyczny

Do najważniejszych pytań otwartych w warstwie matematycznej należą:

1. Czy model powinien zostać uogólniony z tarczy 12-godzinnej do abstrakcyjnej przestrzeni fazowej?
2. Czy istnieje głębsza definicja Sfery wynikająca bezpośrednio z topologii układu?
3. Czy Trend lokalny można zdefiniować przez pochodną funkcji `Orth(T)` względem chwili bazowej?
4. Czy możliwe jest wprowadzenie dodatkowych współrzędnych pozwalających zwiększyć odwracalność systemu?
5. Czy istnieje kanoniczny zapis pełnego stanu ortogonalnego zachowujący więcej informacji źródłowej bez utraty elegancji notacyjnej?

### 15.11. Pytania otwarte — rdzeń ontologiczny

Do najważniejszych pytań ontologicznych należą:

1. Czy stan ortogonalny jest tylko użyteczną miarą relacji, czy powinien być traktowany jako nowa podstawowa kategoria czasu?
2. Czy Chronometria Ortogonalna opisuje czas, czy raczej strukturę jego reprezentacji?
3. Czy oś 3–9 ma znaczenie konieczne, czy tylko konwencyjne?
4. Czy system odkrywa relację obecną w czasie, czy tworzy nowy porządek interpretacyjny nakładany na czas klasyczny?
5. Czy relacyjność i ortogonalność mogą zostać uznane za bardziej fundamentalne niż tradycyjny podział minutowy?

### 15.12. Pytania otwarte — warstwa praktyczna

Do najważniejszych pytań praktycznych należą:

1. Jaka forma interfejsu najlepiej ujawnia logikę systemu użytkownikowi?
2. Czy użytkownik powinien widzieć jednocześnie czas klasyczny i ortogonalny?
3. Czy możliwe jest stworzenie serwera czasu ortogonalnego bez przedwczesnego wchodzenia w pełny protokół infrastrukturalny?
4. Jak powinno wyglądać API czasu ortogonalnego?
5. Czy projekt powinien rozwijać się najpierw jako biblioteka, demonstrator czy manifest naukowy?

### 15.13. Roadmapa wersji 0.2

Wersja 0.2 powinna dążyć do:

* doprecyzowania definicji Sfery,
* rozdzielenia Trendu obserwacyjnego i analitycznego,
* rozszerzenia zestawu przypadków referencyjnych,
* dopracowania formalnej relacji między Cyklem a pełnym stanem czasu,
* ustalenia kanonicznej reprezentacji maszynowej.

### 15.14. Roadmapa wersji 0.5

Wersja 0.5 powinna dążyć do:

* budowy biblioteki referencyjnej niezależnej od UI,
* pełnego zestawu testów zgodności,
* stabilnej notacji użytkowej i maszynowej,
* demonstratora pokazującego równoległe działanie czasu klasycznego i ortogonalnego,
* pierwszego dokumentu opisującego możliwość dystrybucji czasu ortogonalnego w sieci.

### 15.15. Roadmapa wersji 1.0

Wersja 1.0 powinna zostać osiągnięta dopiero wtedy, gdy spełnione zostaną łącznie następujące warunki:

1. rdzeń matematyczny będzie formalnie domknięty,
2. status Sfery i Trendu zostanie jednoznacznie określony,
3. notacja będzie stabilna,
4. implementacja referencyjna będzie publicznie dostępna,
5. zestaw testów zgodności będzie kompletny,
6. system będzie posiadał jasną deklarację swojego statusu ontologicznego i praktycznego.

### 15.16. Wniosek rozwojowy

Chronometria Ortogonalna w wersji 0.1 jest systemem o silnym rdzeniu koncepcyjnym i rosnącym stopniu formalizacji, ale nie jest jeszcze teorią domkniętą.

Jej siłą jest spójny pomysł relacyjno-geometryczny.

Jej najważniejszym zadaniem rozwojowym jest przejście od trafnej idei i działającego modelu do formalnie zamkniętej, niezależnej i interoperacyjnej chronometrii.

## 16. Plan dalszej rozbudowy dokumentu

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
