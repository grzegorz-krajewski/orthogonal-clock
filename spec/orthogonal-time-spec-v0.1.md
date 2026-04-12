# Chronometria Ortogonalna
## Specyfikacja systemu czasu — wersja 0.1
### Wydanie robocze

## Spis treści
1. Wprowadzenie
2. Cel dokumentu
3. Zakres systemu
4. Rozdzielenie pojęć
5. Założenia ogólne
6. Terminologia podstawowa
7. Aksjomaty systemu
8. Pytania rozstrzygające przed wersją 0.2
9. Model formalny i definicje matematyczne
10. Własności podstawowe modelu
11. Przypadki graniczne, punkty szczególne i przykłady referencyjne
12. Relacja do czasu klasycznego
13. Notacja i format zapisu
14. Zgodność implementacji i wymagania referencyjne
15. Ograniczenia, pytania otwarte i roadmapa teorii
16. Status dokumentu, wersjonowanie i zasady publikacji
17. Plan dalszej rozbudowy dokumentu
18. Teza zamykająca wersję 0.1

## Status dokumentu
Niniejszy dokument jest roboczą specyfikacją wersji 0.1. Celem tego wydania jest formalne oddzielenie rdzenia matematycznego systemu od warstwy reprezentacji, wizualizacji i implementacji programistycznej oraz ustanowienie wspólnego języka dla dalszego rozwoju teorii i implementacji.

---

## 1. Wprowadzenie
Chronometria Ortogonalna jest propozycją alternatywnego systemu opisu czasu, w którym podstawową wielkością nie jest liniowy podział godziny na 60 minut, lecz relacja geometryczna między położeniami dwóch wskazań kątowych odpowiadających ruchowi godzinowemu i minutowemu.

W klasycznym modelu zegarowym czas jest odczytywany przez wartości przypisane arbitralnie do podziału tarczy. W Chronometrii Ortogonalnej odczyt wynika z relacji, napięcia i odchylenia geometrycznego względem stanu ortogonalnego. Oznacza to przejście od modelu indeksowego do modelu relacyjnego.

Chronometria Ortogonalna nie jest na tym etapie próbą zastąpienia czasu fizycznego, atomowego ani urzędowego. Jest formalnym systemem reprezentacji czasu opartym na geometrii oraz kandydatem na niezależny model chronometryczny.

Dokument ten ustanawia pierwszą spójną wersję języka, definicji i wymagań, które pozwalają traktować projekt nie jako samą intuicję, lecz jako rozwijający się system formalny.

## 2. Cel dokumentu
Celem niniejszej specyfikacji jest:

1. zdefiniowanie matematycznego rdzenia Chronometrii Ortogonalnej,
2. oddzielenie teorii czasu od mechanizmu jego wskazywania,
3. opisanie zasad konwersji z czasu bazowego do czasu ortogonalnego,
4. ustanowienie pojęć, jednostek, notacji i własności systemu,
5. przygotowanie podstaw pod implementacje referencyjne, narzędzia wizualne i przyszłe protokoły dystrybucji czasu ortogonalnego.

Dokument ma charakter fundacyjny: jego zadaniem nie jest wyczerpanie wszystkich pytań, lecz ustanowienie rdzenia wystarczająco ścisłego, by dalsze prace mogły rozwijać się bez utraty spójności pojęciowej.

## 3. Zakres systemu
Niniejsza specyfikacja obejmuje:
- definicje podstawowych pojęć,
- model geometryczny czasu ortogonalnego,
- sposób wyznaczania wartości czasu ortogonalnego,
- strukturę cykli i sfer,
- zasady notacji,
- relację systemu do klasycznego czasu zegarowego,
- ograniczenia modelu i pytania otwarte.

Specyfikacja nie obejmuje w tej wersji:
- protokołu sieciowego synchronizacji,
- standardu interoperacyjności z systemami operacyjnymi,
- formalnej standaryzacji międzynarodowej,
- mechanicznej konstrukcji urządzeń wskazujących.

## 4. Rozdzielenie pojęć
### 4.1. Chronometria Ortogonalna
Formalny system opisu czasu oparty na relacji geometrycznej między wskazaniami kątowymi.

### 4.2. Czas Ortogonalny
Konkretny stan czasu uzyskany przez zastosowanie reguł Chronometrii Ortogonalnej do chwili bazowej.

### 4.3. Zegar Ortogonalny
Dowolne urządzenie, program lub interfejs wizualny służący do prezentacji Czasu Ortogonalnego.

### 4.4. Implementacja referencyjna
Programowa realizacja algorytmu zgodnego z niniejszą specyfikacją.

## 5. Założenia ogólne
1. Czas ortogonalny jest funkcją chwili bazowej oraz jej reprezentacji kątowej.
2. Rdzeniem systemu jest relacja geometryczna, a nie arbitralny numer pozycji na podziałce.
3. Stanem odniesienia jest ortogonalność, rozumiana jako relacja kąta prostego między wskazaniami.
4. System dopuszcza warstwę interpretacyjną, ale nie może ona naruszać rdzenia matematycznego.
5. Reprezentacja wizualna systemu jest wtórna względem definicji formalnej.

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

## 8. Pytania rozstrzygające przed wersją 0.2
1. Czy chwila bazowa ma być definiowana względem UTC, Unix time czy lokalnego czasu cywilnego?
2. Czy sfera jest pojęciem czysto geometrycznym, czy częściowo interpretacyjnym?
3. Czy trend ma być własnością chwilową funkcji, czy tylko wynikiem porównania kolejnych próbek?
4. Czy system ma operować wyłącznie na modelu 12-godzinnym, czy ma mieć formalne rozszerzenie na czas ciągły?
5. Czy Centi jest jednostką formalną, czy jedynie konwencją zapisu?

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
- godzinę `h`,
- minutę `m`,
- sekundę `s`.

W przypadku gdy sekunda nie jest dostępna, przyjmuje się `s = 0`.

Dla modelu 12-godzinnego definiuje się godzinę zredukowaną:

`h12 = h mod 12`

### 9.3. Reprezentacja kątowa
#### 9.3.1. Kąt godzinowy
`H(T) = 30 * h12 + 0.5 * m + (1/120) * s`

#### 9.3.2. Kąt minutowy
`M(T) = 6 * m + 0.1 * s`

Oba kąty wyrażane są w stopniach.

### 9.4. Redukcja ortogonalna
Niech funkcja redukcji półobrotu będzie dana wzorem:

`R(x) = x mod 180`

Wtedy zredukowane kąty ortogonalne przyjmują postać:

`Hr(T) = R(H(T))`
`Mr(T) = R(M(T))`

### 9.5. Różnica kątowa
`D0(T) = |Hr(T) - Mr(T)|`

`D(T) = min(D0(T), 180 - D0(T))`

Wynika stąd, że:

`0 <= D(T) <= 90`

### 9.6. Odchylenie ortogonalne
`O(T) = |90 - D(T)|`

Zatem:

`0 <= O(T) <= 90`

### 9.7. Wartość czasu ortogonalnego
`Orth(T) = O(T)`

### 9.8. Rozbicie reprezentacyjne
`Orth_int(T) = floor(Orth(T))`

`Centi(T) = floor((Orth(T) - Orth_int(T)) * 100)`

Wersja 0.1 traktuje `Centi` jako element notacyjny reprezentacji liczby rzeczywistej, a nie jako niezależną jednostkę bazową systemu.

### 9.9. Cykl
`C(T) = h mod 12`

### 9.10. Sfera
W wersji 0.1 definiuje się sferę roboczą jako klasyfikację binarną zależną od położenia godzinowego względem osi strukturalnej systemu.

Dla uproszczonego modelu implementacyjnego:
- jeśli `3 <= h12 < 9`, to `S(T) = [-]`,
- w przeciwnym razie `S(T) = [+]`.

Definicja ta ma status przejściowy.

### 9.11. Trend
W wersji 0.1 rozróżnia się dwa typy trendu:

#### 9.11.1. Trend obserwacyjny
Dla dwóch kolejnych chwil obserwacji `T1` i `T2`, gdzie `T2 > T1`, definiuje się:
- trend rosnący, gdy `Orth(T2) > Orth(T1)`,
- trend malejący, gdy `Orth(T2) < Orth(T1)`,
- trend stały, gdy `Orth(T2) = Orth(T1)`.

#### 9.11.2. Trend lokalny
Trend lokalny jest własnością funkcji `Orth(T)` w otoczeniu chwili `T` i w przyszłych wersjach powinien być definiowany przez analizę przyrostu lub pochodnej względem czasu bazowego.

### 9.12. Pełny stan Czasu Ortogonalnego
`OT(T) = (S(T), C(T), Orth(T), Orth_int(T), Centi(T), Trend)`

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

## 11. Przypadki graniczne, punkty szczególne i przykłady referencyjne
### 11.1. Zakres analizy
Niniejszy rozdział opisuje szczególne klasy chwil bazowych, dla których model przyjmuje wartości skrajne, zerowe albo strukturalnie istotne.

### 11.2. Stan idealnej ortogonalności
Stan idealnej ortogonalności zachodzi wtedy i tylko wtedy, gdy:
`D(T) = 90`

co jest równoważne warunkowi:
`O(T) = 0`
oraz:
`Orth(T) = 0`

### 11.3. Stan maksymalnego oddalenia od ortogonalności
Stan maksymalnego oddalenia zachodzi wtedy, gdy:
`D(T) = 0`

co implikuje:
`O(T) = 90`
oraz:
`Orth(T) = 90`

### 11.4. Chwile klasyczne o szczególnym znaczeniu strukturalnym
#### 11.4.1. Chwila 12:00:00
- `h12 = 0`
- `H(T) = 0`
- `M(T) = 0`
- `Hr(T) = 0`
- `Mr(T) = 0`
- `D(T) = 0`
- `Orth(T) = 90`

#### 11.4.2. Chwila 6:00:00
- `h12 = 6`
- `H(T) = 180`
- `M(T) = 0`
- `Hr(T) = 0`
- `Mr(T) = 0`
- `D(T) = 0`
- `Orth(T) = 90`

#### 11.4.3. Chwila 3:00:00
- `h12 = 3`
- `H(T) = 90`
- `M(T) = 0`
- `Hr(T) = 90`
- `Mr(T) = 0`
- `D(T) = 90`
- `Orth(T) = 0`

#### 11.4.4. Chwila 9:00:00
- `h12 = 9`
- `H(T) = 270`
- `M(T) = 0`
- `Hr(T) = 90`
- `Mr(T) = 0`
- `D(T) = 90`
- `Orth(T) = 0`

### 11.5. Klasy równoważności podstawowej
Przykładowo:
- 12:00 i 6:00 należą do tej samej klasy maksymalnego oddalenia,
- 3:00 i 9:00 należą do tej samej klasy idealnej ortogonalności.

### 11.6. Zachowanie na granicy godzin i minut
Funkcje `H(T)` oraz `M(T)` są ciągłe względem czasu bazowego, jeśli `T` traktowane jest jako wielkość ciągła.

### 11.7. Punkty krytyczne
Punkty krytyczne modelu obejmują:
1. minima globalne: chwile, dla których `Orth(T) = 0`,
2. maksima globalne: chwile, dla których `Orth(T) = 90`,
3. punkty przejścia przez ortogonalność,
4. punkty przejścia przez pokrycie wskazań,
5. granice klasyfikacji sferycznej, jeśli sfera pozostaje definiowana przez segmentację godzinową.

### 11.8. Przykłady referencyjne
- `01:00:00 -> Orth(T)=60`
- `02:00:00 -> Orth(T)=30`
- `03:00:00 -> Orth(T)=0`
- `04:00:00 -> Orth(T)=30`
- `05:00:00 -> Orth(T)=60`
- `06:00:00 -> Orth(T)=90`

### 11.9. Symetria pierwszego półcyklu
- 12:00 → 90
- 1:00 → 60
- 2:00 → 30
- 3:00 → 0
- 4:00 → 30
- 5:00 → 60
- 6:00 → 90

### 11.10. Znaczenie testowe przykładów referencyjnych
Każda implementacja zgodna z wersją 0.1 musi zwracać wartości zgodne z przykładami referencyjnymi dla chwil pełnogodzinnych opisanych w niniejszym rozdziale.

## 12. Relacja do czasu klasycznego
### 12.1. Charakter odwzorowania
Chronometria Ortogonalna nie zastępuje w wersji 0.1 klasycznego czasu cywilnego, lecz definiuje alternatywne odwzorowanie chwili bazowej do relacyjnej przestrzeni geometrycznej.

`F: T -> OT(T)`

W wersji podstawowej system jest więc funkcją wtórną względem czasu źródłowego, a nie autonomiczną skalą pierwotną.

### 12.2. Co system zachowuje
Chronometria Ortogonalna zachowuje następujące własności czasu klasycznego:
1. zależność od chwili bazowej,
2. ciągłość zmian przy ciągłym traktowaniu czasu wejściowego,
3. okresowość wynikającą z ruchu wskazań,
4. możliwość systematycznej konwersji z czasu klasycznego do czasu ortogonalnego,
5. deterministyczność odwzorowania przy ustalonym modelu wejścia.

### 12.3. Czego system nie zachowuje
Chronometria Ortogonalna nie zachowuje wszystkich własności klasycznego czasu zegarowego, w szczególności pełnej jednoznaczności odwrotnego odwzorowania i liniowego znaczenia minut jako podstawowej jednostki odczytu.

### 12.4. Jednoznaczność i niejednoznaczność
Mapowanie z czasu klasycznego do Czasu Ortogonalnego jest funkcją jednoznaczną, lecz mapowanie odwrotne nie jest jednoznaczne.

### 12.5. Relacja do minut i godzin
W Chronometrii Ortogonalnej godzina i minuta nie są odczytem końcowym, lecz parametrami pośrednimi używanymi do wyznaczenia położeń kątowych.

### 12.6. Relacja do czasu analogowego
Model analogowy należy traktować jako pierwszą realizację przestrzeni odniesienia, a nie jako jedyne możliwe ucieleśnienie systemu.

### 12.7. Relacja do czasu cyfrowego
System może być implementowany cyfrowo, ale nie jest systemem cyfrowym w sensie ontologicznym.

### 12.8. Relacja do UTC, czasu lokalnego i Unix time
UTC, czas lokalny oraz Unix time mogą pełnić rolę skali bazowej wejścia.

### 12.9. Relacja do odwracalności
Chronometria Ortogonalna jest bardziej systemem projekcji i klasyfikacji relacyjnej niż pełnym kodem odwracalnym chwili źródłowej.

### 12.10. Relacja do obiektywności
W obecnej postaci należy mówić przede wszystkim o obiektywności transformacyjnej lub geometrycznej, a nie o pełnej obiektywności infrastrukturalnej.

### 12.11. Status epistemiczny systemu
W wersji 0.1 najbardziej uzasadnione jest traktowanie jej jako formalnego systemu transformacji i reprezentacji, który dopiero w dalszym rozwoju może aspirować do statusu autonomicznej skali czasu.

### 12.12. Wniosek porównawczy
Czas klasyczny odpowiada przede wszystkim na pytanie: „która jest godzina według przyjętej skali podziału?”.
Czas Ortogonalny odpowiada przede wszystkim na pytanie: „jaki jest relacyjny stan geometryczny chwili w przestrzeni cyklicznej?”.

## 13. Notacja i format zapisu
### 13.1. Cel notacji
Notacja Czasu Ortogonalnego służy do jednoznacznego przedstawiania stanu `OT(T)` w formie czytelnej dla człowieka oraz możliwej do przetwarzania maszynowego.

### 13.2. Składniki stanu notacyjnego
- `S` — Sfera,
- `C` — Cykl,
- `Orth` — pełna wartość czasu ortogonalnego,
- `Oi` — część całkowita `Orth`,
- `Ce` — część setna reprezentacji,
- `Tr` — Trend,
- `B` — opcjonalna informacja o chwili bazowej lub skali wejściowej.

### 13.3. Notacja pełna
`OT[S=<sfera>; C=<cykl>; Orth=<wartość>; Oi=<część_całkowita>; Ce=<centi>; Tr=<trend>]`

Przykład:
`OT[S=+; C=3; Orth=0.00; Oi=0; Ce=00; Tr=↑]`

### 13.4. Notacja standardowa użytkowa
`[<sfera>] C<cykl> O<Oi>.<Ce> <trend>`

Przykład:
`[+] C3 O0.00 ↑`

### 13.5. Notacja skrócona
`<sfera><cykl>:<Oi>.<Ce><trend>`

Przykład:
`+3:0.00↑`

### 13.6. Notacja minimalistyczna
`O<Oi>.<Ce>`

Przykład:
`O30.25`

### 13.7. Notacja maszynowa
Zalecany jest zapis strukturalny JSON z polami:
- `sphere`
- `cycle`
- `orth`
- `orth_int`
- `centi`
- `trend`
- opcjonalnie `base`

### 13.8. Trend w notacji
- `↑` — trend rosnący,
- `↓` — trend malejący,
- `=` — trend stały,
- `?` — trend nieokreślony lub nieobliczony.

### 13.9. Sfera w notacji
- `+` dla sfery dodatniej,
- `-` dla sfery ujemnej.

### 13.10. Cykl w notacji
W dokumentacji specyfikacyjnej zaleca się wariant techniczny `0–11`.

### 13.11. Zasady zaokrąglania i prezentacji
Implementacja musi jawnie deklarować używaną regułę prezentacji.

### 13.12. Zgodność notacyjna
Implementacja zgodna z wersją 0.1 powinna:
1. umożliwiać wygenerowanie co najmniej jednej notacji czytelnej dla człowieka,
2. umożliwiać wygenerowanie jednej reprezentacji maszynowej,
3. zachowywać spójność między `Orth`, `Oi` i `Ce`,
4. jednoznacznie oznaczać status trendu,
5. nie mieszać warstwy źródłowej z warstwą ortogonalną bez jawnych oznaczeń.

### 13.13. Rekomendacja domyślna
Domyślna notacja użytkowa:
`[<sfera>] C<cykl> O<Oi>.<Ce> <trend>`

## 14. Zgodność implementacji i wymagania referencyjne
### 14.1. Cel rozdziału
Celem niniejszego rozdziału jest określenie minimalnych warunków, jakie musi spełnić implementacja Chronometrii Ortogonalnej, aby mogła zostać uznana za zgodną ze specyfikacją w wersji 0.1.

### 14.2. Klasy implementacji
- implementacja obliczeniowa,
- implementacja prezentacyjna,
- implementacja referencyjna,
- implementacja eksperymentalna.

### 14.3. Wymagania minimalne dla zgodności obliczeniowej
Implementacja musi:
1. przyjmować chwilę bazową `T` lub dane pozwalające ją jednoznacznie wyznaczyć,
2. obliczać `H(T)` zgodnie z definicją specyfikacji,
3. obliczać `M(T)` zgodnie z definicją specyfikacji,
4. stosować redukcję `R(x) = x mod 180`,
5. obliczać `D0(T)` jako bezwzględną różnicę zredukowanych kątów,
6. obliczać `D(T) = min(D0(T), 180 - D0(T))`,
7. obliczać `O(T) = |90 - D(T)|`,
8. zwracać `Orth(T)` jako wartość równą `O(T)`.

### 14.4. Wymagania minimalne dla zgodności reprezentacyjnej
Implementacja musi:
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
Implementacja musi jawnie określić, z jakiej skali wejściowej korzysta.

### 14.7. Wymagania dotyczące precyzji
Implementacja musi rozróżniać precyzję obliczeniową i prezentacyjną.

### 14.8. Status Sfery i Trendu
W wersji 0.1 implementacja może być zgodna z rdzeniem matematycznym nawet wtedy, gdy:
- nie udostępnia Sfery,
- oznacza Trend jako `unknown`,
- korzysta z roboczej definicji Sfery i obserwacyjnej definicji Trendu.

### 14.9. Testy referencyjne minimalne
Każda implementacja zgodna z wersją 0.1 powinna poprawnie odtwarzać co najmniej:
1. `12:00:00 -> Orth = 90`
2. `03:00:00 -> Orth = 0`
3. `06:00:00 -> Orth = 90`
4. `09:00:00 -> Orth = 0`
5. `01:00:00 -> Orth = 60`
6. `02:00:00 -> Orth = 30`
7. `04:00:00 -> Orth = 30`
8. `05:00:00 -> Orth = 60`

### 14.10. Niezgodności krytyczne
Za niezgodność krytyczną uznaje się między innymi:
1. brak redukcji do 180 stopni,
2. użycie niewłaściwej definicji różnicy kątowej,
3. użycie wartości innej niż `|90 - D(T)|` jako podstawy `Orth(T)`,
4. niespójność między wynikiem liczbowym a jego reprezentacją tekstową,
5. przypisywanie pełnej zgodności wersji 0.1 przy pominięciu wymogów matematycznych.

### 14.11. Niezgodności dopuszczalne warunkowo
Dopuszczalne warunkowo są różnice dotyczące:
- formatu wyświetlania,
- kolejności pól w reprezentacji maszynowej,
- obecności lub braku pola `base`,
- wyboru dokładności prezentacyjnej,
- sposobu oznaczania trendu.

### 14.12. Deklaracja zgodności
`This implementation conforms to Orthogonal Time Specification v0.1 in its computational core.`

### 14.13. Rekomendacja dla implementacji wzorcowej
Implementacja wzorcowa powinna:
- przyjmować chwilę bazową jako jawny argument,
- nie opierać obliczeń wyłącznie na stanie globalnym programu,
- rozdzielać funkcje obliczeniowe od prezentacyjnych,
- udostępniać testy jednostkowe dla przypadków referencyjnych,
- pozwalać na rozszerzenie o kolejne wersje specyfikacji bez łamania zgodności wstecznej.

## 15. Ograniczenia, pytania otwarte i roadmapa teorii
### 15.1. Rola niniejszego rozdziału
Celem niniejszego rozdziału jest jawne wskazanie ograniczeń wersji 0.1, zidentyfikowanie pytań, które pozostają nierozstrzygnięte, oraz wyznaczenie kierunków rozwoju Chronometrii Ortogonalnej.

### 15.2. Ograniczenie źródłowe
W wersji 0.1 Chronometria Ortogonalna nie definiuje własnej niezależnej skali czasu absolutnego.

### 15.3. Ograniczenie odwracalności
Chronometria Ortogonalna nie jest jeszcze pełnym kodem chwili, lecz projekcją relacyjną chwili.

### 15.4. Ograniczenie modelu tarczowego
Model podstawowy wyrasta z geometrii klasycznej tarczy analogowej.

### 15.5. Ograniczenie definicji Sfery
W wersji 0.1 Sfera posiada status przejściowy.

### 15.6. Ograniczenie definicji Trendu
Wersja 0.1 nie domyka formalnie Trendu lokalnego.

### 15.7. Ograniczenie ontologiczne
Dokument celowo pozostawia częściowo otwartą kwestię, czy system jest reprezentacją, nową klasą czasu czy kandydatem na autonomiczną skalę.

### 15.8. Ograniczenie infrastrukturalne
Wersja 0.1 nie definiuje protokołu synchronizacji, dystrybucji ani interoperacyjności z istniejącymi standardami czasu.

### 15.9. Ograniczenie semantyczne
Nie zostało jeszcze ostatecznie ustalone, czy `Orthos`, `Centi`, `Cykl` i `Sfera` są wyłącznie operacyjne, częściowo ontologiczne czy w pełni aksjomatyczne.

### 15.10. Pytania otwarte — rdzeń matematyczny
1. Czy model powinien zostać uogólniony z tarczy 12-godzinnej do abstrakcyjnej przestrzeni fazowej?
2. Czy istnieje głębsza definicja Sfery wynikająca bezpośrednio z topologii układu?
3. Czy Trend lokalny można zdefiniować przez pochodną funkcji `Orth(T)`?
4. Czy możliwe jest wprowadzenie dodatkowych współrzędnych zwiększających odwracalność systemu?
5. Czy istnieje kanoniczny zapis pełnego stanu ortogonalnego zachowujący więcej informacji źródłowej?

### 15.11. Pytania otwarte — rdzeń ontologiczny
1. Czy stan ortogonalny jest tylko użyteczną miarą relacji, czy nową podstawową kategorią czasu?
2. Czy Chronometria Ortogonalna opisuje czas, czy raczej strukturę jego reprezentacji?
3. Czy oś 3–9 ma znaczenie konieczne, czy tylko konwencyjne?
4. Czy system odkrywa relację obecną w czasie, czy tworzy nowy porządek interpretacyjny?
5. Czy relacyjność i ortogonalność mogą zostać uznane za bardziej fundamentalne niż podział minutowy?

### 15.12. Pytania otwarte — warstwa praktyczna
1. Jaka forma interfejsu najlepiej ujawnia logikę systemu?
2. Czy użytkownik powinien widzieć jednocześnie czas klasyczny i ortogonalny?
3. Czy możliwe jest stworzenie serwera czasu ortogonalnego bez pełnego protokołu infrastrukturalnego?
4. Jak powinno wyglądać API czasu ortogonalnego?
5. Czy projekt powinien rozwijać się najpierw jako biblioteka, demonstrator czy manifest naukowy?

### 15.13. Roadmapa wersji 0.2
- doprecyzowanie definicji Sfery,
- rozdzielenie Trendu obserwacyjnego i analitycznego,
- rozszerzenie zestawu przypadków referencyjnych,
- dopracowanie formalnej relacji między Cyklem a pełnym stanem czasu,
- ustalenie kanonicznej reprezentacji maszynowej.

### 15.14. Roadmapa wersji 0.5
- budowa biblioteki referencyjnej niezależnej od UI,
- pełny zestaw testów zgodności,
- stabilna notacja użytkowa i maszynowa,
- demonstrator pokazujący równoległe działanie czasu klasycznego i ortogonalnego,
- pierwszy dokument o możliwości dystrybucji czasu ortogonalnego w sieci.

### 15.15. Roadmapa wersji 1.0
Wersja 1.0 powinna zostać osiągnięta dopiero wtedy, gdy:
1. rdzeń matematyczny będzie formalnie domknięty,
2. status Sfery i Trendu zostanie jednoznacznie określony,
3. notacja będzie stabilna,
4. implementacja referencyjna będzie publicznie dostępna,
5. zestaw testów zgodności będzie kompletny,
6. system będzie posiadał jasną deklarację swojego statusu ontologicznego i praktycznego.

### 15.16. Wniosek rozwojowy
Chronometria Ortogonalna w wersji 0.1 jest systemem o silnym rdzeniu koncepcyjnym i rosnącym stopniu formalizacji, ale nie jest jeszcze teorią domkniętą.

## 16. Status dokumentu, wersjonowanie i zasady publikacji
### 16.1. Status dokumentu
Niniejszy dokument ma status roboczej specyfikacji systemu Chronometrii Ortogonalnej w wersji 0.1.

### 16.2. Charakter normatywny i informacyjny
Rozróżnia się treści normatywne i informacyjne.

### 16.3. Zasady interpretacji zapisów
- `musi` — wymaganie bezwzględne,
- `powinno` — wymaganie silnie zalecane,
- `może` — zachowanie dopuszczalne opcjonalnie,
- `nie może` — zachowanie niedopuszczalne.

### 16.4. Zasady wersjonowania
- `0.x` — etap eksploracyjny i formacyjny,
- `1.0` — pierwsza wersja formalnie domknięta,
- `1.x` — wersje zgodne wstecznie,
- `2.0` — zmiana niezgodna wstecznie w rdzeniu systemu.

### 16.5. Zasady zmian między wersjami
Każda nowa wersja dokumentu powinna jawnie określać:
1. co dodano,
2. co doprecyzowano,
3. co zmieniło status,
4. co utraciło ważność,
5. czy zmiana narusza zgodność wsteczną.

### 16.6. Zgodność wsteczna
Należy dążyć do zachowania zgodności wstecznej rdzenia matematycznego, podstawowej notacji użytkowej, reprezentacji maszynowej pól podstawowych i przykładów referencyjnych.

### 16.7. Zasady publikacji implementacji
Implementacje publiczne odwołujące się do Chronometrii Ortogonalnej powinny wskazywać wersję specyfikacji i jawnie deklarować własne rozszerzenia.

### 16.8. Zasady cytowania dokumentu
`Chronometria Ortogonalna — Specyfikacja systemu czasu, wersja 0.1`

### 16.9. Zasady publikacji przyszłych standardów pochodnych
Dokumenty takie jak API, protokół dystrybucji czy standard zegara ortogonalnego powinny być publikowane jako dokumenty podrzędne wobec niniejszej specyfikacji rdzeniowej.

### 16.10. Kierunek publikacji projektu
Projekt powinien rozwijać się równolegle jako:
1. dokument specyfikacyjny,
2. implementacja referencyjna,
3. demonstrator.

### 16.11. Kryterium przejścia z wersji roboczej do stabilnej
Dokument może zostać uznany za stabilny dopiero wtedy, gdy:
1. definicja Sfery zostanie domknięta,
2. Trend lokalny zostanie określony formalnie,
3. przypadki referencyjne obejmą pełniejszy zakres czasu wejściowego,
4. implementacja referencyjna przejdzie jawnie opublikowany zestaw testów,
5. status ontologiczny systemu zostanie określony precyzyjniej.

### 16.12. Wniosek końcowy
Wersja 0.1 stanowi pierwszy poważny krok w kierunku przekształcenia Chronometrii Ortogonalnej z autorskiej idei w system możliwy do formalnego opisu, implementacji i dalszej weryfikacji.

## 17. Plan dalszej rozbudowy dokumentu
W kolejnych wersjach dokument może zostać rozszerzony o:
- formalny aneks z dowodami i własnościami funkcji,
- tablice konwersji dla wybranych przedziałów czasu,
- pełny zestaw testów zgodności,
- aneks terminologiczny polsko-angielski,
- rozdział o architekturze biblioteki referencyjnej,
- rozdział o protokołach publikacji i dystrybucji czasu ortogonalnego.

## 18. Teza zamykająca wersję 0.1
Chronometria Ortogonalna proponuje relacyjno-geometryczne ujęcie czasu, w którym kluczową rolę odgrywa nie arbitralna numeracja podziałki, lecz odchylenie od stanu ortogonalnego w przestrzeni cyklicznej.

Wersja 0.1 nie kończy tej teorii, lecz ustanawia jej pierwszy formalny język.

Jeżeli kolejne wersje zachowają ścisłość rdzenia matematycznego, klarowność notacji i uczciwe rozróżnienie między teorią a interpretacją, Chronometria Ortogonalna może rozwinąć się z autorskiej idei w rozpoznawalny, implementowalny i dyskutowalny system chronometryczny.
