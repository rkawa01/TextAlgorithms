Zadanie polega na implementacji dwóch algorytmów kompresji:

statycznego algorytmu Huffmana (2 p)
dynamicznego algorytmu Huffmana (3 p)
Dla każdego z algorytmów należy wykonać następujące zadania:

Opracować format pliku przechowującego dane. Zwróć uwagę na dwie kwestie:
Liczba bitów wynikowego pliku nie musi być podzielna przez 8, ale z dysku zawsze odczytujemy pełne bajty, dlatego ważne jest, aby jakoś rozwiązać ten problem. W przeciwnym razie po dekompresji można uzyskać nadmiarowe dane.
Plik wynikowy musi być binarny, tzn. rozwiązanie nie może zakładać, że w pliku tym zapisywane są 0 i 1 jako znaki ASCII.
Zaimplementować algorytm kompresji i dekompresji danych dla tego formatu pliku.
Zmierzyć współczynnik kompresji (wyrażone w procentach: 1 - plik_skompresowany / plik_nieskompresowany) dla plików o rozmiarach: 1kB, 10kB, 100kB, 1MB, o różnej zawartości:
wybrany przez Ciebie plik tekstowy z projektu Gutenberg,
wybrany przez Ciebie plik z kodem źródłowym jądra Linuksa,
plik ze znakami losowanymi z rozkładu jednostajnego - należy uwzględnić wszystkie 256 wartości, a nie tylko znaki drukowalne.
W sumie w punkcie 3 należy przeprowadzić analizę dla łącznie 12 plików (4 rozmiary x 3 typy plików).
Zmierzyć czas kompresji i dekompresji dla plików z punktu 3.
Zadanie dla chętnych:
Zaimplementować dowolny algorytm ze zmiennym blokiem kompresji, który uzyska lepszy współczynnik kompresji na większości (czyli min. dla 7 plików) danych wejściowych, niż algorytmy Huffmana  (+2 punkty).
