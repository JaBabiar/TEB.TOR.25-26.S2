# Zadanie Praktyczne: Awaria w Sklepie Internetowym 🛒

## Wprowadzenie
Jesteście programistami w dużym sklepie internetowym. W systemie nastąpiła awaria i do koszyka wpadają produkty, których nie ma w magazynie, a niektóre ceny zapisały się jako tekst zamiast liczb! 

Waszym zadaniem jest uratować system przed całkowitym zawieszeniem, wyczyścić dane i napisać testy sprawdzające wprowadzone poprawki.

## Wytyczne do zadania

1. **Oczyszczanie (`filter`):** Użyjcie funkcji `filter` i wyrażenia `lambda`, aby stworzyć listę tylko tych produktów, które są aktualnie dostępne (`"dostepne": True`).
2. **Ekstrakcja cen (`map`):** Użyjcie funkcji `map` i wyrażenia `lambda`, aby z listy dostępnych produktów wyciągnąć same wartości przypisane do klucza `"cena"`.
3. **Bezpieczna kasa (`try...except`):** Napiszcie funkcję `podlicz_kase(lista_cen)`, która sumuje wszystkie ceny. Zabezpieczcie ją przed błędem `TypeError` (który wystąpi, gdy program spróbuje dodać liczbę do słowa "gratis"). W przypadku błędu funkcja powinna zwrócić komunikat: `"Błąd cennika: niepoprawny format danych"`.
4. **Testowanie (`unittest`):** Uzupełnijcie klasę testową, aby sprawdzić, czy funkcja poprawnie sumuje prawidłowe ceny i czy odpowiednio reaguje na błędne dane.

---

## Kod startowy dla ucznia

Poniższy kod skopiuj do swojego środowiska i uzupełnij brakujące fragmenty według wytycznych.

```python
import unittest

# Dane pobrane z zepsutego systemu sklepu
koszyk = [
    {"produkt": "Laptop", "cena": 3000, "dostepne": True},
    {"produkt": "Myszka", "cena": 100, "dostepne": False}, # Uwaga: Produkt niedostępny
    {"produkt": "Klawiatura", "cena": 200, "dostepne": True},
    {"produkt": "Kabel", "cena": 50, "dostepne": False},   # Uwaga: Produkt niedostępny
    {"produkt": "Podkładka", "cena": "gratis", "dostepne": True} # Uwaga: Błędny format ceny
]

# ZADANIE 1: Odfiltruj tylko dostępne produkty (użyj filter i lambda)
dostepne_produkty = # TUTAJ TWÓJ KOD

# ZADANIE 2: Wyciągnij same ceny z dostępnych produktów (użyj map i lambda)
ceny_do_zaplaty = # TUTAJ TWÓJ KOD

# ZADANIE 3: Napisz funkcję z użyciem try...except
def podlicz_kase(lista_cen):
    pass # TUTAJ TWÓJ KOD

# ZADANIE 4: Uzupełnij testy jednostkowe
class TestSklepu(unittest.TestCase):
    
    def test_podlicz_kase_poprawne(self):
        # Sprawdź, czy funkcja podlicz_kase([100, 200]) zwraca wartość 300
        pass

    def test_podlicz_kase_z_bledem(self):
        # Sprawdź, czy podlicz_kase([100, "gratis"]) zwraca "Błąd cennika: niepoprawny format danych"
        pass

if __name__ == '__main__':
    # Kod pomocniczy do weryfikacji przed testami:
    # print("Dostępne produkty:", list(dostepne_produkty))
    # print("Ceny do zapłaty:", list(ceny_do_zaplaty))
    
    # Uruchomienie testów
    unittest.main()