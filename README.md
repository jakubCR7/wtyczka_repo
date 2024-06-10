## Informatyka Geodezyjna II
## Projekt 1 - Transformacje 
Program umożliwia implementację transformacji geodezyjnych zgodnie z potrzebami użytkownika.

## Wymagania do obsługi programu:
Program został stworzony z użyciem programu Python 3.11.5, zaimporotwana została biblioteka NumPy, pozwalająca na wykonywanie obliczeń numerycznych i naukowych. Program został napisany dla systemu operacyjnego Microsoft Windows 10 PRO i wyższych. Konieczna jest instalacja programu python.exe oraz biblioteki NumPy w konsoli.

## Funkcje programu:
**Użytkownik wybiera spośród dostępnych elipsoid:** <br>
GRS80<br>
WGRS84<br>
Krasowski <br>

**Użytkownik wybiera spośród dostępnych transformacji:** <br>
 1 = X, Y, Z --> phi, lam, h <br>
 2 = phi, lam, h --> X, Y, Z <br>
 3 = X, Y, Z --> neu <br>
 4 = BL --> X2000, Y2000 <br>
 5 = BL --> X92, Y92<br>
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
