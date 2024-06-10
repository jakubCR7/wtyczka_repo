## Informatyka Geodezyjna II
## Projekt 2 - Wtyczka do QGIS
Wtyczka umożliwia wyznaczanie różnic wysokości pomiędzy punktami oraz liczenie pól między punktami w hektarach, mekrach kwadratowych lub arach

## Wymagania do obsługi programu:
Do poprawnego działania wtyczki wymagany jest zainstalowany program QGiS. Folder z wtyczką musi być umieszczony w folderze plugins w plikach programu QGiS. 
Dodatkowo potrzebne są biblioteki:
qgis.PyQT, qgis.utils, qgis.core, PyQt5.QtWidgets, qgis.gui, PyQt5.QtCore

## Funkcje programu:
Opracowanie danych z poziomu wtyczki po wgraniu do projektu QGIS.

**Liczenie różnicy wysokości pomiędzy wybranymi punktami z aktywnej warstwy:** <br>
W celu obliczenia różnicy wysokośći między punktami należy wybrać dokładnie dwa punkty znajdujące się na tej samej warstwie.
Ważne, aby w tabeli atrybutów znajdowała się kolumna z danymi "wysokosc", w której znajdują się wysokości puntków.
Wtyczka odejmuje wysokość punktu początkowego od punktu końcowego, co może dać wynik dodatni lub ujemny, na tej podstawie 
można stwierdzić, czy nastąpił spadek czy wzrost wysokości. Wynik podany jest w metrach z dokładnością do centymetra.
 <br>
 <br>
**Liczenie pola powierzchni pomiędzy zaznaczonymi punktami** <br>
W celu obliczenia pola powierzchni między punktami użytkownik wybiera minimum trzy punkty leżące na tej samej warstwie. 
Na podstawie współrzędnych wybranych punktów program obliczy pole powierzchni pomiędzy nimi, przy użyciu metody Gaussa.
Użytkownik może wybrać, w jakich jednostkach wyświetli się otrzymany wynik. Wybór pomiędzy m2, ha, ar, z dokładnością do trzech miejsc po przecinku.

### Działanie programu:
Uruchamiając program Python wymagane jest również podanie nazwy pliku ze współrzędnymi wraz z jego rozszerzeniem. Następnie, zgodnie z instrukcjami programu należy wybrać elipsoidę. Następnie, poprzez wpisanie liczby od 1 do 5, dokonujemy wyboru transformacji. Załączony plik z danymi musi być zgodny z wybraną transformacją tj. dla transformacji **1, 3** plik z danymi powinien zawierać współrzędne ortokartezjańskie, a dla transformacji **2, 4, 5** współrzędne geodezyjne. W przeciwnym wypadku uzyskane wyniki nie będą poprawne. Opcje, spośród których dokonujemy wyboru są podane powyżej w punkcje **Funkcje programu**. W przypadku wybrania opcji **3** program poprosi użytkownika o podanie współrzędnych środka układu NEU.

### Przykładowe użycie programu:
1. Użytkownik uruchamia konsolę CMD (wiersz poleceń) w folderze, w którym znajduje się program.<br>
**cd C:\Users\admin\Desktop\Program1**
2. Program uruchamia się poprzez wpisanie poleceń **python**, po spacji nazwa programu **Program1.txt**, oraz po spacji nazwa pliku z danymi, np. **wsp_int.txt** i po spacji żądaną nazwę pliku z danymi wyjściowymi, np. **dane_wyjsciowe.txt**.
3. Wymagania wobec pliku z danymi:
   - nagłówek może być dowolny
   - separatorem danych jest przecinek ','
   - dane muszą być różne od 0, inaczej program nie będzie działał
   - przykładowy wygląd pliku: <br>
   ----- X ----- Y ----- Z ----- <br>
   1009.9999,1008.8889,107.777
 4. Wybór elipsoidy poprzez wpisanie w konsolę, według poleceń na ekranie np. **grs80**
 5. Wybór transformacji poprzez wpisanie w konsolę odpowiedniej cyfry, według poleceń na ekranie, np. X,Y,Z-->neu **1**

Przy zastosowaniu prawidłowej ścieżki i odpowiednich poleceń program powinien się uruchomić, następnie wyświetlić komunikat:<br>
**program zapisał plik o nazwie "dane_wyjsciowe.txt" ze współrzędnymi geodezyjnymi w bierzącym folderze**
#### Przykładowe użycie pliku:
Aby program zadziałał, dane w pliku muszą spełniać wyżej przedstawione wymogi, można zweryfikować za pomocą przykładowych plików umieszczonych na stronie.<br>

Dane wejściowe:'wsp_inp.txt'<br>
Pod nagłówkiem dane zapisane są w trzech kolumnach, pierwsza to współrzędne X, druga to współrzędne Y, a trzecia to wysokość Z, wszystkie wartości podane w metrach.<br>

Dane wyjściowe:<br>
W pliku wyjściowym dane są rozłożone tak, jak w pliku wejściowym.

### Błędy programu:
1. W przypadku pliku o odpowiedniej strukturze, jednak z błędnymi danymi (np. phi lam h zamiast XYZ) program nie wyrzuci błędu, tylko nieprawidłowe wartości
2. W przypadku transformacji **4, 5** przy elipsoidzie Krassowskiego program poda błędne wartości jednak wcześniej wyświetli stosowną informację na ekranie.
3. W przypadku transformacji **3** (X, Y, Z --> neu), przy podaniu punktu o współrzędnych tych samych co początek układu NEU program zwraca tylko jedną współrzędną.
### Autorzy programu:
Adam Buława <br>
Jakub Fajfer
