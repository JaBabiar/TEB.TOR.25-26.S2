# Karkówka dzis? 

## Plik 1: `aplikacja.py`

```python
# =====================================================================
# PLIK: aplikacja.py (GRUPA E)
# Ten plik zawiera kod źródłowy do przetestowania. 
# Znajduje się tu tylko jedna klasa.
# NIE ZMIENIAJ KODU W TYM PLIKU!
# =====================================================================

class Rezerwacja:
    """Klasa reprezentująca rezerwację hotelową."""
    
    def __init__(self, nazwisko):
        self.nazwisko = nazwisko
        self.ilosc_dni = 0
        self.zaplacono = False

    def dodaj_dni(self, liczba_dni):
        """Zwiększa czas trwania rezerwacji. Liczba dni musi być dodatnia."""
        if liczba_dni <= 0:
            raise ValueError("Liczba dni musi być większa od zera!")
        self.ilosc_dni += liczba_dni

    def potwierdz_wplate(self):
        """Oznacza rezerwację jako opłaconą."""
        self.zaplacono = True

    def czy_wazna(self):
        """Zwraca prawdę, jeśli rezerwacja trwa minimum 1 dzień i jest opłacona."""
        return self.ilosc_dni > 0 and self.zaplacono
```

---

## Plik 2: `test_kartkowka.py`

```python
# =====================================================================
# KARTKÓWKA: Testowanie jednostkowe w Pythonie (biblioteka unittest)
# Maksymalna liczba punktów: 20
# GRUPA: E
# Imię i nazwisko: ....................................................
# =====================================================================

import unittest

# Importujemy NASZĄ JEDYNĄ KLASĘ z pliku aplikacja.py do przetestowania
from aplikacja import Rezerwacja

# ---------------------------------------------------------------------
# ZADANIE 1: Podstawy tworzenia testów i asercje (7 punktów)
# ---------------------------------------------------------------------

# a) (2 pkt) Utwórz klasę testową o nazwie TestPodstawowyRezerwacji, która
#    dziedziczy po odpowiedniej klasie z biblioteki unittest.
# b) (2 pkt) Wewnątrz klasy napisz metodę testową. Utwórz w niej obiekt 
#    Rezerwacja("Kowalski"), wywołaj na nim metodę dodaj_dni(5), a następnie 
#    sprawdź, czy jego atrybut 'ilosc_dni' wynosi dokładnie 5.
# c) (2 pkt) Wewnątrz klasy napisz drugą metodę testową. Utwórz nową rezerwację,
#    a następnie sprawdź, czy metoda czy_wazna() zwraca fałsz.
# Miejsce na Twój kod:







# d) (1 pkt) Zapisz instrukcję warunkową, która uruchamia wszystkie 
#    testy, jeśli ten plik jest uruchamiany bezpośrednio.
# Miejsce na Twój kod:




# ---------------------------------------------------------------------
# ZADANIE 2: Przydatne metody asercji i błędy (5 punktów)
# ---------------------------------------------------------------------

class TestZaawansowanyRezerwacji(unittest.TestCase):
    
    # a) (2 pkt) Uzupełnij poniższy test. Sprawdź odpowiednią asercją, czy 
    #    atrybut 'nazwisko' w obiekcie r jest typu tekstowego (str).
    def test_typu_nazwiska(self):
        r = Rezerwacja("Nowak")
        # <-- Tutaj dodaj asercję sprawdzającą typ zmiennej

    # b) (3 pkt) Napisz test, który sprawdzi, czy wywołanie r.dodaj_dni(-2) 
    #    poprawnie zgłasza błąd ValueError (niedozwolona ujemna liczba dni).
    def test_ujemnej_liczby_dni(self):
        r = Rezerwacja("Nowak")
        pass  # <-- Zastąp słowo 'pass' swoim kodem


# ---------------------------------------------------------------------
# ZADANIE 3: Przygotowanie środowiska - metoda setUp (8 punktów)
# ---------------------------------------------------------------------

class TestProcesuRezerwacji(unittest.TestCase):
    
    # a) (3 pkt) Uzupełnij specjalną metodę, która wykonuje się automatycznie 
    #    przed KAŻDYM testem. Wewnątrz niej utwórz nowy obiekt 
    #    klasy Rezerwacja("Malinowski") i przypisz go do atrybutu (self.moja_rezerwacja).
    def setUp(self):
        pass

    # b) (3 pkt) Napisz test sprawdzający, czy po utworzeniu rezerwacji 
    #    (self.moja_rezerwacja) jej atrybut 'zaplacono' ma wartość Fałsz. 
    def test_poczatkowy_status_platnosci(self):
        pass

    # c) (2 pkt) Napisz test sprawdzający proces aktywacji rezerwacji.
    #    Wywołaj metodę potwierdz_wplate(), a także dodaj 3 dni (dodaj_dni(3)) 
    #    na obiekcie self.moja_rezerwacja. Następnie sprawdź, czy 
    #    metoda czy_wazna() zwraca prawdę.
    def test_waznosci_rezerwacji(self):
        pass
```
