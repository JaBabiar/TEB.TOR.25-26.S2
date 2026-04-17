
# KARTKÓWKA PRAKTYCZNA: Testy Jednostkowe (unittest)

## 📋 INSTRUKCJA WYKONANIA ZADANIA

Aby rozpocząć pracę, wykonaj poniższe kroki:

1. **Stwórz dwa nowe pliki** w swoim edytorze kodu (np. w PyCharm, VS Code lub Thonny).
2. **Skopiuj i wklej** do nich odpowiednie kody, które znajdziesz poniżej.
3. Twoim zadaniem jest **uzupełnić tylko plik testowy** zgodnie z instrukcjami podanymi w komentarzach.
4. Za każde poprawnie wykonane zadanie otrzymasz **4 punkty**.

---

## 📄 PLIK 1: Kod główny programu (NIE EDYTUJ TEGO PLIKU)

Stwórz plik o nazwie **`Postac.py`** i wklej do niego poniższy kod. Służy on tylko do tego, abyś mógł sprawdzić, jak działają metody postaci.

```python
class Postac:
    def __init__(self, imie):
        self.imie = imie
        self.zdrowie = 100
        self.plecak = []

    def otrzymaj_obrazenia(self, obrazenia):
        if not isinstance(obrazenia, int):
            raise TypeError("Obrażenia muszą być liczbą!")
            
        if obrazenia < 0:
            raise ValueError("Obrażenia nie mogą być ujemne!")
            
        self.zdrowie -= obrazenia
        
        if self.zdrowie < 0:
            self.zdrowie = 0

    def dodaj_do_plecaka(self, przedmiot):
        self.plecak.append(przedmiot)

    def usun_z_plecaka(self, przedmiot):
        if przedmiot in self.plecak:
            self.plecak.remove(przedmiot)
```

---

## 🛠️ PLIK 2: Twoje zadania (TUTAJ PRACUJESZ)

Stwórz plik o nazwie **`Postac_test.py`** i wklej do niego poniższy kod.
**Zastąp słowo `pass` odpowiednim kodem.** Czytaj uważnie kroki w komentarzach.

```python
import unittest
from Postac import Postac

class TestPostaci(unittest.TestCase):
    
    def setUp(self):
        # ZADANIE 1 (4 pkt): 
        # Utwórz obiekt klasy Postac o imieniu "Wojownik".
        # Przypisz ten obiekt do zmiennej self.p
        pass

    def test_otrzymaj_obrazenia(self):
        # ZADANIE 2 (4 pkt): 
        # Krok 1: Użyj metody otrzymaj_obrazenia na self.p, aby zadać 20 obrażeń.
        # Krok 2: Sprawdź czy self.p.zdrowie wynosi teraz 80.
        pass

    def test_dodaj_do_plecaka(self):
        # ZADANIE 3 (4 pkt): 
        # Krok 1: Użyj metody dodaj_do_plecaka, aby dodać "Mikstura" do plecaka self.p.
        # Krok 2: Sprawdź czy "Mikstura" znajduje się w self.p.plecak.
        pass

    def test_usun_z_plecaka(self):
        # ZADANIE 4 (4 pkt): 
        # Krok 1: Najpierw dodaj "Klucz" do plecaka (użyj dodaj_do_plecaka).
        # Krok 2: Następnie usuń "Klucz" z plecaka (użyj usun_z_plecaka).
        # Krok 3: Sprawdź czy "Klucz" zniknął z self.p.plecak.
        pass
        
    def test_bledy_obrazen(self):
        # ZADANIE 5 (4 pkt): 
        # Sprawdź sprawdź czy funckja podnosi błąd wartości
        # Wewnątrz tego bloku spróbuj zadać ujemne obrażenia, np. self.p.otrzymaj_obrazenia(-10)
        pass

if __name__ == '__main__':
    unittest.main()
```

---

## 📊 SKALA OCENIANIA

### (Maksymalna liczba punktów do zdobycia: 20)

| Procent | Punkty | Ocena |
| :--- | :--- | :--- |
| **0% - 49%** | 0 - 9 pkt | **1** (Niedostateczny) |
| **50%** | 10 - 11 pkt | **2** (Dopuszczający) |
| **60%** | 12 - 14 pkt | **3** (Dostateczny) |
| **75%** | 15 - 17 pkt | **4** (Dobry) |
| **90%+** | 18 - 20 pkt | **5** (Bardzo dobry) |
