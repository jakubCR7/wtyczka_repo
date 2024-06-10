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
1. Użytkownik uruchamia program QGiS, w którym umieszcza warstwy z punktami na których chce wykonywać obliczenia.
2. Jeżeli folder z wtyczką został umieszczony poprawnie, wtyczka będzie się znajdować w panelu zarządzanie wtyczkami w zakładce zaintalowane wtyczki. Ze względu na to, że nasza wtyczka jest wtyczką eksperymentalną należy zaznaczyć, aby widoczne były również wtyczki eksperymentalne. Należy zaznaczyć okienko, aby wtyczka była gotowa do użycia.
3. Należy zaznaczyć punkty, na których przeprowadzone mają zostać obliczenia za pomocą narzędzia zaznaczanie.
4. z panelu wtyczki wybrać wtyczkę o nazwie **wtyka2**
5. W pierszym polu należy wybrać z listy warstwę na której znajdują się zaznaczone punkty, następnie wybrać funkcjonalność wysokość lub pole. <br> W przypadku wybrania pola należy zaznaczyć **jeden** z podanych checkbox'ów w zależności od jednostki w jakiej chce się uzyskać wynik.
6. Program zwróci wartość pola w odpowiedniej jednostce lub wartość różnicy wysokości (w zależności od wybranej funkcji) w okienku wtyczki.

### Błędy programu:
1. W przypadku pliku o odpowiedniej strukturze, jednak z błędnymi danymi (np. phi lam h zamiast XYZ) program nie wyrzuci błędu, tylko nieprawidłowe wartości
2. W przypadku transformacji **4, 5** przy elipsoidzie Krassowskiego program poda błędne wartości jednak wcześniej wyświetli stosowną informację na ekranie.
3. W przypadku transformacji **3** (X, Y, Z --> neu), przy podaniu punktu o współrzędnych tych samych co początek układu NEU program zwraca tylko jedną współrzędną.
### Autorzy programu:
Adam Buława <br>
Jakub Fajfer
