# 🧠 NOTATKA: Jak zdać kartkówkę z `unittest`

Programowanie testów to nie jest pisanie nowych, skomplikowanych algorytmów. To po prostu mechaniczne sprawdzanie, czy napisany już kod działa zgodnie z założeniami. Piszesz kod, który używa twojego kodu i patrzy, czy zmienne mają odpowiednie wartości. Koniec magii.

[Tu masz PLIKI](https://github.com/JaBabiar/TEB.TOR.25-26.S2/tree/main/3.tp.cisco/Tydzien%204%20(unittest))
[Tu masz Kartkowka](https://github.com/JaBabiar/TEB.TOR.25-26.S2/blob/main/3.tp.cisco/Kartkowki/k2t1_unittest.md)
Masz do dyspozycji przykłady z plików `edziennik_test.py` oraz `Gracz_test.py`. Poniżej znajdziesz wyjaśnienie, jak przenieść z nich gotowe schematy do swojej kartkówki (`Postac_test.py`).

## ⚙️ Krok 1: Zrozum `setUp` (Fabryka obiektów)

Zanim zaczniesz cokolwiek testować, musisz stworzyć obiekt. Metoda `setUp` uruchamia się **przed każdym pojedynczym testem**. Gwarantuje to, że każdy test odpala się na "czystym" obiekcie, z nienaruszonymi zmiennymi.

**Jak to wygląda w kodzie przykładowym (`Gracz_test.py`):**
```python
def setUp(self):
    self.g = Gracz("Tester") # Tworzymy instancję klasy Gracz i przypisujemy do self.g
```

**Co musisz zrobić w ZADANIU 1:**
Musisz stworzyć instancję klasy `Postac`, podać jej argument `"Wojownik"` i zapisać to w atrybucie klasy testowej (z `self`), żeby inne testy miały do tego dostęp.
```python
def setUp(self):
    self.p = Postac("Wojownik")
```
## 🔍 Krok 2: Asercje (Narzędzia sędziego)
W każdym teście musisz wywołać jakąś metodę ze swojego obiektu (np. dodać coś do listy, odjąć wartość), a następnie użyć **asercji**, żeby sprawdzić, czy stan obiektu się zmienił.
Oto jedyne 4 narzędzia, których potrzebujesz na tę kartkówkę:

| **Kod asercji**                 | **Do czego służy?**                                                                            | **Przykład z gotowych plików**                                                   |
| ------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `self.assertEqual(a, b)`        | Sprawdza, czy zmienna `a` ma dokładnie taką samą wartość jak `b`.                              | `self.assertEqual(self.g.points, 10)`                                            |
| `self.assertIn(a, b)`           | Sprawdza, czy element `a` znajduje się wewnątrz listy/kolekcji `b`.                            | `self.assertIn("Miecz", self.g.ekwipunek)`                                       |
| `self.assertNotIn(a, b)`        | Sprawdza, czy elementu `a` **na pewno nie ma** w liście `b`.                                   | `self.assertNotIn("Jan K", self.k.uczniowie)`                                    |
| `with self.assertRaises(Błąd):` | Sprawdza, czy po wykonaniu błędnego kodu program wyrzuci konkretny wyjątek (np. `ValueError`). | `with self.assertRaises(ValueError):`<br><br>  <br><br>`self.g.dodaj_punkty(-5)` |

## 🚀 Krok 3: Rozwiązanie kartkówki (Podstawianie schematów)
Każdy test składa się z dwóch faz: **Akcja** (wywołanie metody na `self.p`) i **Weryfikacja** (asercja z `self.assert...`). Wzoruj się 1:1 na załączonych przykładach.
### ZADANIE 2: `test_otrzymaj_obrazenia`
- **Logika:** Wywołujesz metodę ucinającą HP, a potem używasz `assertEqual`, żeby sprawdzić, czy z początkowych 100 HP zostało 80.
- **Rozwiązanie:**
```python
def test_otrzymaj_obrazenia(self):
    self.p.otrzymaj_obrazenia(20)          # Akcja
    self.assertEqual(self.p.zdrowie, 80)   # Weryfikacja
```

### ZADANIE 3: `test_dodaj_do_plecaka`

- **Logika:** Wrzucasz stringa na listę (do plecaka) używając odpowiedniej metody, a potem sprawdzasz przez `assertIn`, czy ten string na niej jest.
- **Rozwiązanie:**
```python
def test_dodaj_do_plecaka(self):
    self.p.dodaj_do_plecaka("Mikstura")       # Akcja
    self.assertIn("Mikstura", self.p.plecak)  # Weryfikacja
```

### ZADANIE 4: `test_usun_z_plecaka`
- **Logika:** Dodajesz coś na listę, usuwasz z listy, a na koniec żądasz przez `assertNotIn` potwierdzenia, że element zniknął. Wzoruj się na `usun_ucznia`.
- **Rozwiązanie:**
```python
def test_usun_z_plecaka(self):
    self.p.dodaj_do_plecaka("Klucz")          # Akcja 1 (przygotowanie)
    self.p.usun_z_plecaka("Klucz")            # Akcja 2 (usunięcie)
    self.assertNotIn("Klucz", self.p.plecak)  # Weryfikacja
```

### ZADANIE 5: `test_bledy_obrazen`

- **Logika:** Jeśli klasa główna celowo rzuca błędem (wyjątkiem) przy nieprawidłowych danych (ujemne obrażenia to błąd `ValueError` według pliku `Postac.py`), musisz to obsłużyć. Używasz bloku `with`.
- **Rozwiązanie:**
```python
def test_bledy_obrazen(self):
    with self.assertRaises(ValueError):       # Deklaracja oczekiwanego błędu
        self.p.otrzymaj_obrazenia(-10)        # Kod, który celowo ten błąd wywołuje
```

_(Ważne: Kod wewnątrz bloku `with` musi być wcięty o jeden poziom!)_

## Całe Rozwiązanie 

```python 

import unittest
from Postac import Postac

class TestPostaci(unittest.TestCase):
    
    def setUp(self):
        # ZADANIE 1 (4 pkt): 
        # Utwórz obiekt klasy Postac o imieniu "Wojownik".
        # Przypisz ten obiekt do zmiennej self.p
        self.p = Postac("Wojownik")

    def test_otrzymaj_obrazenia(self):
        # ZADANIE 2 (4 pkt): 
        # Krok 1: Użyj metody otrzymaj_obrazenia na self.p, aby zadać 20 obrażeń.
        # Krok 2: Sprawdź czy self.p.zdrowie wynosi teraz 80.
        self.p.otrzymaj_obrazenia(20)
        self.assertEqual(self.p.zdrowie, 80)

    def test_dodaj_do_plecaka(self):
        # ZADANIE 3 (4 pkt): 
        # Krok 1: Użyj metody dodaj_do_plecaka, aby dodać "Mikstura" do plecaka self.p.
        # Krok 2: Sprawdź czy "Mikstura" znajduje się w self.p.plecak.
        self.p.dodaj_do_plecaka("Mikstura")
        self.assertIn("Mikstura", self.p.plecak)

    def test_usun_z_plecaka(self):
        # ZADANIE 4 (4 pkt): 
        # Krok 1: Najpierw dodaj "Klucz" do plecaka (użyj dodaj_do_plecaka).
        # Krok 2: Następnie usuń "Klucz" z plecaka (użyj usun_z_plecaka).
        # Krok 3: Sprawdź czy "Klucz" zniknął z self.p.plecak.
        self.p.dodaj_do_plecaka("Klucz")
        self.p.usun_z_plecaka("Klucz")
        self.assertNotIn("Klucz", self.p.plecak)
        
    def test_bledy_obrazen(self):
        # ZADANIE 5 (4 pkt): 
        # Sprawdź sprawdź czy funckja podnosi błąd wartości
        # Wewnątrz tego bloku spróbuj zadać ujemne obrażenia, np. self.p.otrzymaj_obrazenia(-10)
        with self.assertRaises(ValueError):
            self.p.otrzymaj_obrazenia(-10)

```
