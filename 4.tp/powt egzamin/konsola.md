## Część I. Aplikacja konsolowa

Zaprogramuj klasę o nazwie `Wyszukiwanie` implementującą logikę algorytmu wyszukiwania elementu w zbiorze z wykorzystaniem tzw. wartownika.

**Założenia do programu:**

* Wykonywany w konsoli

* Zastosowany obiektowy język programowania zgodny z zainstalowanym na stanowisku egzaminacyjnym: Python

* Zastosowane znaczące, angielskie lub polskie nazewnictwo zmiennych i funkcji

* Zapisany czytelnie, z zachowaniem zasad czystego formatowania kodu

**Klasa `Wyszukiwanie` powinna zawierać:**

* Pole prywatne przechowujące wygenerowaną listę 10 liczb całkowitych.

**Konstruktor bezargumentowy:**

* Losuje 10 liczb pseudolosowych z zakresu od 1 do 100.

* Przypisuje wylosowane liczby do pola prywatnego przechowującego listę.

* **Metoda prywatna** `dodaj_wartownika`, przyjmująca jeden argument (szukaną wartość):
* Dodaje przekazaną w argumencie wartość na sam koniec listy jako jej 11. element.
* Metoda nie zwraca żadnej wartości.

* **Metoda ogólnodostępna** `szukaj_elementu`, przyjmująca jeden argument (szukaną wartość):
* Wywołuje metodę prywatną `dodaj_wartownika` przekazując jej szukaną wartość.
* Realizuje algorytm wyszukiwania z wartownikiem za pomocą pętli `while`.
* Przed zakończeniem działania usuwa dodanego wcześniej wartownika z listy (przywracając jej rozmiar do 10 elementów).
* Zwraca liczbę całkowitą: indeks pierwszego wystąpienia szukanej wartości lub `-1`, jeśli szukana wartość nie wystąpiła w oryginalnej, 10-elementowej liście.

**Sprawdź działanie klasy w programie głównym:**

* Należy utworzyć obiekt klasy `Wyszukiwanie`.
* Wypisać na ekranie wszystkie elementy wylosowanej listy oddzielone przecinkami.
* Pobrać od użytkownika z klawiatury wartość do wyszukania.

* Wywołać metodę `szukaj_elementu` i wyświetlić w konsoli czytelną informację o wyniku (indeks znalezionego elementu lub informację o jego braku).

**Wymagania dotyczące dokumentacji kodu:**

* W kodzie źródłowym za pomocą komentarza utwórz nagłówek dla metody `szukaj_elementu` według poniższego wzoru. W miejscu `<nawiasów>` należy podać odpowiednie opisy, a w miejscu autor podać numer zdającego.

```text
****************************************************
nazwa funkcji: <nazwa>
opis funkcji: <krótki opis co robi funkcja>
parametry: <nazwa i opis parametru>
zwracany typ i opis: <nazwa typu i opis co jest zwracane>
autor: <numer zdającego>
****************************************************

```

---

## Notatka
Skopiuj poniższy blok kodu i wklej go bezpośrednio do pliku np. `README.md` lub `Zadanie_Wartownik.md` w swoim repozytorium na GitHubie.

### Rozwiązywanie Aplikacji Konsolowych na egzaminie INF.04 (Python)

Na egzaminie zawodowym INF.04 zadanie z aplikacji konsolowej zawsze opiera się na **programowaniu obiektowym (OOP)**. Komisja (CKE) wymaga rygorystycznego trzymania się poleceń, hermetyzacji (pola prywatne) oraz odpowiedniego dokumentowania kodu.

Poniżej znajdziesz przewodnik krok po kroku, jak rozwiązać typowe zadanie na przykładzie algorytmu wyszukiwania z wartownikiem.

### Krok 1: Importy i struktura klasy

Zawsze zaczynamy od zaimportowania potrzebnych modułów i zdefiniowania szkieletu klasy. Zwróć uwagę na wymóg tworzenia pól prywatnych. W Pythonie pole prywatne oznaczamy **dwoma podkreśleniami** (np. `__tablica`).

```python
import random

class Wyszukiwanie:
    def __init__(self):
        # Generowanie 10 losowych liczb z zakresu 1-100 za pomocą list comprehension
        self.__tablica = [random.randint(1, 100) for _ in range(10)]

```

### Krok 2: Metody prywatne i algorytm

Metody prywatne w Pythonie również poprzedzamy dwoma podkreśleniami (np. `__dodaj_wartownika`). Wyszukiwanie z wartownikiem polega na dopisaniu szukanego elementu na koniec listy – dzięki temu nie musimy w pętli `while` sprawdzać, czy wyszliśmy poza zakres tablicy (bo szukany element na pewno tam jest).

```python
    def __dodaj_wartownika(self, wartosc):
        # Dopisanie wartownika na koniec listy
        self.__tablica.append(wartosc)

    def szukaj_elementu(self, wartosc):
        # 1. Dodajemy wartownika korzystając z metody prywatnej
        self.__dodaj_wartownika(wartosc)
        
        # 2. Algorytm wyszukiwania
        i = 0
        while self.__tablica[i] != wartosc:
            i += 1
            
        # 3. Sprzątanie: usuwamy wartownika z końca listy
        self.__tablica.pop()
        
        # 4. Sprawdzamy czy znaleziony element to był nasz wartownik (indeks 10)
        # Jeśli tak, to znaczy że elementu nie było w pierwotnej tablicy
        if i == 10:
            return -1
        else:
            return i

```

### Krok 3: Dokumentacja kodu (Wymóg CKE)

W arkuszach często pojawia się wymóg udokumentowania konkretnej funkcji/metody według podanego wzoru. Komentarz ten musi znaleźć się dokładnie nad funkcją. Brak tego elementu to gwarantowana strata punktów.

```python
    # ****************************************************
    # nazwa funkcji: szukaj_elementu
    # opis funkcji: Wyszukuje przekazaną wartość w liście używając algorytmu z wartownikiem
    # parametry: wartosc - liczba całkowita, której szukamy w liście
    # zwracany typ i opis: int - indeks pierwszego wystąpienia elementu lub -1 w przypadku braku
    # autor: 00000000000
    # ****************************************************
    def szukaj_elementu(self, wartosc):
        # ... kod metody ...

```

### Krok 4: Program główny (Testowanie)

Instrukcje "Sprawdź działanie klasy w programie głównym" oznaczają, że musisz utworzyć obiekt, pobrać dane od użytkownika i wywołać metody. Zawsze zabezpieczaj uruchomienie programu instrukcją `if __name__ == "__main__":`. Pamiętaj też o rzutowaniu wejścia na typ `int`!

```python
if __name__ == "__main__":
    # 1. Utworzenie obiektu
    app = Wyszukiwanie()
    
    # Python pozwala na dobieranie się do pól prywatnych przez "name mangling", 
    # ale do podglądu dla celów testowych użyjemy wbudowanego __dict__ 
    # lub po prostu wypiszemy to z wnętrza obiektu. Wzorcowo powinniśmy 
    # mieć getter (metodę zwracającą tablicę), więc załóżmy dodanie metody wyswietl().
    
    # Poniżej trick na wypisanie prywatnego pola w celach egzaminacyjnych, 
    # bez dopisywania dodatkowych metod (których nie było w poleceniu):
    wylosowane = app._Wyszukiwanie__tablica 
    print("Wylosowana tablica:", ", ".join(map(str, wylosowane)))
    
    # 2. Pobranie danych
    # Pamiętaj o int()! input() zawsze zwraca string (tekst).
    szukana_liczba = int(input("Podaj liczbę do wyszukania: "))
    
    # 3. Wywołanie metody i wynik
    indeks = app.szukaj_elementu(szukana_liczba)
    
    if indeks != -1:
        print(f"Znaleziono element pod indeksem: {indeks}")
    else:
        print("Szukanej liczby nie ma w wylosowanej tablicy.")

```

> **Pro Tip:** Podczas rozwiązywania na egzaminie: zawsze czytaj ze zrozumieniem nazwy klas i metod. CKE odejmuje punkty za "niezgodność nazw z założeniami". Jeśli kazali nazwać metodę `dodaj_wartownika`, nie nazywaj jej `dodajWartownika` czy `add_sentinel`.
