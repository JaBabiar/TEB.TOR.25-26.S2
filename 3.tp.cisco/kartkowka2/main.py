# ==========================================
# KARTKÓWKA - FUNKCJE LAMBDA (GRUPA 1)
# ==========================================
# Imię i nazwisko: .................................
# Klasa: ...........................................

# ZADANIE: Analiza asortymentu w sklepie komputerowym
# Poniżej znajduje się lista słowników reprezentujących produkty.
# Twoim zadaniem jest uzupełnienie brakującego kodu (oznaczonego jako "TUTAJ TWÓJ KOD")
# korzystając z funkcji anonimowych (lambda).

produkty = [
    {"nazwa": "Klawiatura mechaniczna", "cena": 350.0, "ocena": 4.8, "stan_magazynowy": 15},
    {"nazwa": "Myszka bezprzewodowa", "cena": 65.0, "ocena": 3.9, "stan_magazynowy": 120},
    {"nazwa": "Monitor 144Hz", "cena": 899.0, "ocena": 4.9, "stan_magazynowy": 5},
    {"nazwa": "Podkładka pod mysz", "cena": 25.0, "ocena": 4.2, "stan_magazynowy": 50},
    {"nazwa": "Kamera internetowa", "cena": 120.0, "ocena": 3.5, "stan_magazynowy": 0}
]

# ---------------------------------------------------------
# ZADANIE 1: Lambda + Skrócony warunek (if-else)
# ---------------------------------------------------------
# Napisz funkcję lambda, która przyjmuje jeden argument (wartość cena).
# Jeśli wartość jest większa lub równa 100, funkcja ma zwrócić tekst "Premium".
# W przeciwnym razie ma zwrócić tekst "Standard".
# Przypisz tę funkcję do zmiennej 'kategoria_cenowa'.

kategoria_cenowa = # TUTAJ TWÓJ KOD

# Możesz odkomentować poniższe linie, aby sprawdzić swój kod:
# print("--- ZADANIE 1 ---")
# print(kategoria_cenowa(150))  # Oczekiwany wynik: Premium
# print(kategoria_cenowa(40))   # Oczekiwany wynik: Standard


# ---------------------------------------------------------
# ZADANIE 2: Filtrowanie danych (filter + lambda)
# ---------------------------------------------------------
# Użyj funkcji wbudowanej filter() oraz wyrażenia lambda, aby z listy "produkty"
# wyciągnąć TYLKO te produkty, których "ocena" jest wyższa niż 4.0.
# Wynik przekonwertuj na listę i zapisz w zmiennej 'polecane_produkty'.

polecane_produkty = # TUTAJ TWÓJ KOD

# Możesz odkomentować poniższe linie, aby sprawdzić swój kod:
# print("\n--- ZADANIE 2 ---")
# for p in polecane_produkty:
#     print(p["nazwa"])  # Oczekiwany wynik: Klawiatura mechaniczna, Monitor 144Hz, Podkładka pod mysz


# ---------------------------------------------------------
# ZADANIE 3: Sortowanie z kluczem (sort/sorted + lambda)
# ---------------------------------------------------------
# Posortuj oryginalną listę "produkty" ROSNĄCO (od najmniejszej do największej)
# według wartości "stan_magazynowy". 
# Użyj metody .sort() i przekaż funkcję lambda do parametru 'key'.

# TUTAJ TWÓJ KOD

# Możesz odkomentować poniższe linie, aby sprawdzić swój kod:
# print("\n--- ZADANIE 3 ---")
# for p in produkty:
#      print(f"{p['nazwa']} - Ilość sztuk: {p['stan_magazynowy']}") 
# Oczekiwana kolejność: Kamera internetowa (0), Monitor 144Hz (5), Klawiatura mechaniczna (15), Podkładka pod mysz (50), Myszka bezprzewodowa (120)
