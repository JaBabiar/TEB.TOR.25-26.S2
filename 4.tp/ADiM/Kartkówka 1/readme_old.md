# Karkówka UnitTest

## Plik 1: `aplikacja.py`

```python
# =====================================================================
# PLIK: aplikacja.py
# Ten plik zawiera kod źródłowy do przetestowania. 
# Znajduje się tu tylko jedna klasa.
# NIE ZMIENIAJ KODU W TYM PLIKU!
# =====================================================================

class Zamowienie:
    """Klasa reprezentująca zamówienie w sklepie internetowym."""
    
    def __init__(self, numer):
        self.numer = numer
        self.status = "Nowe"
        self.suma = 0

    def dodaj_produkt(self, cena):
        """Dodaje cenę produktu do sumy zamówienia. Cena musi być dodatnia."""
        if cena <= 0:
            raise ValueError("Cena produktu musi być większa od zera!")
        self.suma += cena

    def oplac(self):
        """Zmienia status zamówienia na opłacone."""
        self.status = "Opłacone"

    def gotowe_do_wysylki(self):
        """Zwraca prawdę, jeśli zamówienie zostało opłacone."""
        return self.status == "Opłacone"
```

---

## Plik 2: `test_kartkowka.py`

```python
# =====================================================================
# KARTKÓWKA: Testowanie jednostkowe w Pythonie (biblioteka unittest)
# Maksymalna liczba punktów: 20
# Imię i nazwisko: ....................................................
# =====================================================================

import unittest

# Importujemy NASZĄ JEDYNĄ KLASĘ z pliku aplikacja.py do przetestowania
from aplikacja import Zamowienie

# ---------------------------------------------------------------------
# ZADANIE 1: Podstawy tworzenia testów i asercje (7 punktów)
# ---------------------------------------------------------------------

# a) (2 pkt) Utwórz klasę testową o nazwie TestPodstawowyZamowienia, która
#    dziedziczy po odpowiedniej klasie z biblioteki unittest.
# b) (2 pkt) Wewnątrz klasy napisz metodę testową. Utwórz w niej obiekt 
#    Zamowienie(100), wywołaj na nim metodę dodaj_produkt(50), a następnie 
#    sprawdź, czy jego atrybut 'suma' wynosi dokładnie 50.
# c) (2 pkt) Wewnątrz klasy napisz drugą metodę testową. Utwórz nowe zamówienie,
#    a następnie sprawdź, czy metoda gotowe_do_wysylki() zwraca fałsz.
# Miejsce na Twój kod:







# d) (1 pkt) Zapisz instrukcję warunkową, która uruchamia wszystkie 
#    testy, jeśli ten plik jest uruchamiany bezpośrednio.
# Miejsce na Twój kod:




# ---------------------------------------------------------------------
# ZADANIE 2: Przydatne metody asercji i błędy (5 punktów)
# ---------------------------------------------------------------------

class TestZaawansowanyZamowienia(unittest.TestCase):
    
    # a) (2 pkt) Uzupełnij poniższy test. Sprawdź odpowiednią asercją, czy 
    #    atrybut 'status' w obiekcie z jest typu tekstowego (str).
    def test_typu_statusu(self):
        z = Zamowienie(200)
        # <-- Tutaj dodaj asercję sprawdzającą typ zmiennej

    # b) (3 pkt) Napisz test, który sprawdzi, czy wywołanie z.dodaj_produkt(-10) 
    #    poprawnie zgłasza błąd ValueError (niedozwolona ujemna cena).
    def test_ujemnej_ceny(self):
        z = Zamowienie(200)
        pass  # <-- Zastąp słowo 'pass' swoim kodem


# ---------------------------------------------------------------------
# ZADANIE 3: Przygotowanie środowiska - metoda setUp (8 punktów)
# ---------------------------------------------------------------------

class TestProcesuZamowienia(unittest.TestCase):
    
    # a) (3 pkt) Uzupełnij specjalną metodę, która wykonuje się automatycznie 
    #    przed KAŻDYM testem. Wewnątrz niej utwórz nowy obiekt 
    #    klasy Zamowienie(300) i przypisz go do atrybutu (self.moje_zamowienie).
    def setUp(self):
        pass

    # b) (3 pkt) Napisz test sprawdzający, czy po utworzeniu zamówienia 
    #    (self.moje_zamowienie) jego początkowa 'suma' wynosi 0. 
    def test_poczatkowa_suma(self):
        pass

    # c) (2 pkt) Napisz test sprawdzający proces opłacania.
    #    Wywołaj metodę oplac() na self.moje_zamowienie, a następnie 
    #    sprawdź, czy metoda gotowe_do_wysylki() zwraca prawdę.
    def test_oplacenia_zamowienia(self):
        pass
```
