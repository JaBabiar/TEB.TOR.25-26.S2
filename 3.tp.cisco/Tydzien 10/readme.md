# ==========================================
# POWTÓRKA PRZED KARTKÓWKĄ - FUNKCJE LAMBDA
# ==========================================

# ZADANIE: Analiza statystyk drużyny e-sportowej
# Poniżej znajduje się lista słowników reprezentujących graczy w drużynie. 
# Twoim zadaniem jest uzupełnienie brakującego kodu (oznaczonego jako "TUTAJ TWÓJ KOD")
# korzystając z funkcji anonimowych (lambda).

gracze = [
    {"nick": "neo", "kd_ratio": 1.2, "adr": 85.5, "hs_percent": 55},
    {"nick": "taz", "kd_ratio": 0.9, "adr": 60.2, "hs_percent": 45},
    {"nick": "snax", "kd_ratio": 1.5, "adr": 92.1, "hs_percent": 48},
    {"nick": "pasha", "kd_ratio": 1.1, "adr": 78.0, "hs_percent": 60},
    {"nick": "byali", "kd_ratio": 0.8, "adr": 55.4, "hs_percent": 30}
]

# ---------------------------------------------------------
# ETAP 1: Lambda + Skrócony warunek (if-else)
# ---------------------------------------------------------
# Napisz funkcję lambda, która przyjmuje jeden argument (wartość hs_percent).
# Jeśli wartość jest większa lub równa 50, funkcja ma zwrócić tekst "Wyborny strzelec".
# W przeciwnym razie ma zwrócić tekst "Zwykły gracz".
# Przypisz tę funkcję do zmiennej 'ocena_celnosci'.

ocena_celnosci = # TUTAJ TWÓJ KOD

# Odkomentuj poniższe linie, aby przetestować Etap 1:
# print("--- ETAP 1 ---")
# print(ocena_celnosci(55))  # Oczekiwany wynik: Wyborny strzelec
# print(ocena_celnosci(30))  # Oczekiwany wynik: Zwykły gracz


# ---------------------------------------------------------
# ETAP 2: Filtrowanie danych (filter + lambda)
# ---------------------------------------------------------
# Użyj funkcji wbudowanej filter() oraz wyrażenia lambda, aby z listy "gracze"
# wyciągnąć TYLKO tych graczy, których współczynnik "kd_ratio" jest większy niż 1.0.
# Wynik przekonwertuj na listę i zapisz w zmiennej 'gracze_na_plusie'.

gracze_na_plusie = # TUTAJ TWÓJ KOD

# Odkomentuj poniższe linie, aby przetestować Etap 2:
# print("\n--- ETAP 2 ---")
# for g in gracze_na_plusie:
#     print(g["nick"])  # Oczekiwany wynik: neo, snax, pasha


# ---------------------------------------------------------
# ETAP 3: Sortowanie z kluczem (sort/sorted + lambda)
# ---------------------------------------------------------
# Posortuj oryginalną listę "gracze" MALEJĄCO (od najwyższego do najniższego)
# według wartości "adr" (Average Damage per Round). 
# Użyj metody .sort() i przekaż funkcję lambda do parametru 'key'.

# TUTAJ TWÓJ KOD

# Odkomentuj poniższe linie, aby przetestować Etap 3:
# print("\n--- ETAP 3 ---")
# for g in gracze:
#     print(f"{g['nick']} - ADR: {g['adr']}") 
# Oczekiwana kolejność: snax (92.1), neo (85.5), pasha (78.0), taz (60.2), byali (55.4)