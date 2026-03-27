#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KARTA PRACY UCZNIA - Funkcje lambda
INF.04 | Imię i nazwisko: ___________________
"""

# ===== ZADANIE 1: Podstawy =====
# Napisz funkcję lambda, która:
# a) mnoży liczbę przez 3
# a) sprawdza, czy liczba jest dodatnia
# c) zwraca pierwszy znak ciągu tekstowego

pomnoz_przez_3 = lambda x: ...  # TODO
czy_dodatnia = lambda x: ...    # TODO
pierwszy_znak = lambda txt: ... # TODO

# Testy (odkomentuj po rozwiązaniu):
# print(pomnoz_przez_3(5))        # oczekiwane: 15
# print(czy_dodatnia(-3))         # oczekiwane: False
# print(pierwszy_znak("Python"))  # oczekiwane: 'P'


# ===== ZADANIE 2: map() z lambda =====
ceny_netto = [100, 250, 89, 499, 1200]

# Dodaj 23% VAT do każdej ceny za pomocą map() + lambda
ceny_brutto = list(map(lambda cena: ..., ceny_netto))  # TODO

print(f"Ceny brutto: {[round(c, 2) for c in ceny_brutto]}")


# ===== ZADANIE 3: filter() z lambda =====
oceny = [2, 3, 4, 5, 2, 3, 5, 4, 6, 1]

# Zostaw tylko oceny pozytywne (>= 3)
oceny_pozytywne = list(filter(lambda ocena: ..., oceny))  # TODO

print(f"Oceny pozytywne: {oceny_pozytywne}")


# ===== ZADANIE 4: sorted() z lambda - WYZWANIE =====
pracownicy = [
    {'nazwisko': 'Kowalski', 'dzial': 'IT', 'wynagrodzenie': 5500},
    {'nazwisko': 'Nowak', 'dzial': 'HR', 'wynagrodzenie': 4200},
    {'nazwisko': 'Wiśniewski', 'dzial': 'IT', 'wynagrodzenie': 6100},
    {'nazwisko': 'Wójcik', 'dzial': 'Sprzedaż', 'wynagrodzenie': 4800},
]

# Posortuj pracowników po dziale, a w ramach działu po wynagrodzeniu (malejąco)
posortowani = sorted(pracownicy, key=lambda p: ...)  # TODO

print("\nPracownicy posortowani:")
for prac in posortowani:
    print(f"  {prac['nazwisko']:15} | {prac['dzial']:10} | {prac['wynagrodzenie']} zł")


# ===== ZADANIE 5 (opcjonalne): Mini-projekt =====
"""
Stwórz system filtracji produktów:
- Lista słowników z produktami (nazwa, kategoria, cena, ocena)
- Użyj filter() + lambda, aby wyświetlić:
  a) produkty z kategorii "elektronika"
  b) produkty z oceną >= 4.0
  c) produkty tanie (< 200 zł) I z dobrą oceną (>= 4.0)
"""

# TODO: Twój kod tutaj
