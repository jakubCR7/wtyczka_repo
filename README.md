## Informatyka Geodezyjna II
## Projekt 2 - Wtyczka do QGIS
Wtyczka umożliwia wyznaczanie różnic wysokości pomiędzy punktami oraz liczenie pól między punktami w hektarach, metrach kwadratowych lub arach.

### Wymagania do obsługi programu:
Do poprawnego działania wtyczki wymagany jest zainstalowany program QGiS. Folder z wtyczką musi być umieszczony w folderze plugins w plikach programu QGiS. 
Dodatkowo potrzebne są biblioteki:
qgis.PyQT, qgis.utils, qgis.core, PyQt5.QtWidgets, qgis.gui, PyQt5.QtCore

### Funkcje programu:
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

### Działanie wtyczki:
Wtyczka została stworzona w celu obliczenia różnicy wysokości między dwoma punktami oraz pola powierzchni
umieszczonej pomiędzy wybranymi punktami. Przed uruchomieniem wtyczki ważne jest załadowanie do QGIS-a
warstwy z odpowiednimi wartościami, tj. o geometrii punktowej, z atrybutem definiującym wysokość. Następnie
zainstalowana wtyczka "zaliczka, wtyka2" czytelnym interfejsem pozwala na wybór funkcji. Wynik wyświetla się w oknie wtyczki.

### Przykładowe użycie programu:
1. Użytkownik uruchamia program QGiS, w którym umieszcza warstwy z punktami na których chce wykonywać obliczenia.
2. Jeżeli folder z wtyczką został umieszczony poprawnie, wtyczka będzie się znajdować w panelu zarządzanie wtyczkami w zakładce zaintalowane wtyczki. Ze względu na to, że nasza wtyczka jest wtyczką eksperymentalną należy zaznaczyć, aby widoczne były również wtyczki eksperymentalne. Należy zaznaczyć okienko, aby wtyczka była gotowa do użycia.
3. Należy zaznaczyć punkty, na których przeprowadzone mają zostać obliczenia za pomocą narzędzia zaznaczanie.
4. z panelu wtyczki wybrać wtyczkę o nazwie **wtyka2**
5. W pierszym polu należy wybrać z listy warstwę na której znajdują się zaznaczone punkty, następnie wybrać funkcjonalność wysokość lub pole. <br> W przypadku wybrania pola należy zaznaczyć **jeden** z podanych checkbox'ów w zależności od jednostki w jakiej chce się uzyskać wynik.
6. Program zwróci wartość pola w odpowiedniej jednostce lub wartość różnicy wysokości (w zależności od wybranej funkcji) w okienku wtyczki.

### Błędy:
Obliczanie różnicy wysokości wymaga wyboru jedynie dwóch punktów. W przypadku wybrania ilości punktów 
większej od 2, zostanie wyświetlony komunikat **Różnica wysokosci: W celu obliczenia różnicy wysokosci wybierz 2 punkty.** <br>
Obliczanie pola powierzchni wymaga wyboru trzech i więcej punktów. W przypadku wybrania ilości punktów 
mniejszej od 3, zostanie wyświetlony komunikat **Pole powierzchni: W celu policzenia pola wybierz conajmniej 3 punkty.** <br>
W przypadku pracy w projekcie bez aktywnej warstwy zostanie wyświetlony komunikat **Nie wybrano aktywnej warstwy.** <br> 

### Autorzy programu:
Adam Buława <br>
Jakub Fajfer
