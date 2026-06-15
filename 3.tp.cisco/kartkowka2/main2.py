# ==========================================
# KARTKÓWKA - FUNKCJE LAMBDA (GRUPA B)
# ==========================================
# Imię i nazwisko: .................................
# Klasa: ...........................................

# ZADANIE: Analiza asortymentu w księgarni internetowej
# Poniżej znajduje się lista słowników reprezentujących książki.
# Twoim zadaniem jest uzupełnienie brakującego kodu (oznaczonego jako "TUTAJ TWÓJ KOD")
# korzystając z funkcji anonimowych (lambda).

ksiazki = [
    {"tytul": "Wiedźmin", "cena": 49.99, "liczba_stron": 320, "w_magazynie": 45},
    {"tytul": "Encyklopedia PWN", "cena": 180.0, "liczba_stron": 950, "w_magazynie": 3},
    {"tytul": "Poradnik Python", "cena": 85.0, "liczba_stron": 210, "w_magazynie": 12},
    {"tytul": "Krótki komiks", "cena": 15.50, "liczba_stron": 48, "w_magazynie": 80},
    {"tytul": "Mały Książę", "cena": 29.90, "liczba_stron": 96, "w_magazynie": 0}
]

# ---------------------------------------------------------
# ZADANIE 1: Lambda + Skrócony warunek (if-else)
# ---------------------------------------------------------
# Napisz funkcję lambda, która przyjmuje jeden argument (wartość liczba_stron).
# Jeśli wartość jest większa lub równa 200, funkcja ma zwrócić tekst "Gruba".
# W przeciwnym razie ma zwrócić tekst "Cienka".
# Przypisz tę funkcję do zmiennej 'objetosc_ksiazki'.

objetosc_ksiazki = # TUTAJ TWÓJ KOD

# Możesz odkomentować poniższe linie, aby sprawdzić swój kod:
# print("--- ZADANIE 1 ---")
# print(objetosc_ksiazki(350))  # Oczekiwany wynik: Gruba
# print(objetosc_ksiazki(120))  # Oczekiwany wynik: Cienka


# ---------------------------------------------------------
# ZADANIE 2: Filtrowanie danych (filter + lambda)
# ---------------------------------------------------------
# Użyj funkcji wbudowanej filter() oraz wyrażenia lambda, aby z listy "ksiazki"
# wyciągnąć TYLKO te pozycje, których "cena" jest niższa niż 50.0 złotych.
# Wynik przekonwertuj na listę i zapisz w zmiennej 'tanie_ksiazki'.

tanie_ksiazki = # TUTAJ TWÓJ KOD

# Możesz odkomentować poniższe linie, aby sprawdzić swój kod:
# print("\n--- ZADANIE 2 ---")
# for k in tanie_ksiazki:
#     print(k["tytul"])  # Oczekiwany wynik: Wiedźmin, Krótki komiks, Mały Książę


# ---------------------------------------------------------
# ZADANIE 3: Sortowanie z kluczem (sort/sorted + lambda)
# ---------------------------------------------------------
# Posortuj oryginalną listę "ksiazki" ROSNĄCO (od najmniejszej do największej)
# według wartości "w_magazynie". 
# Użyj metody .sort() i przekaż funkcję lambda do parametru 'key'.

# TUTAJ TWÓJ KOD

# Możesz odkomentować poniższe linie, aby sprawdzić swój kod:
# print("\n--- ZADANIE 3 ---")
# for k in ksiazki:
#      print(f"{k['tytul']} - Dostępnośc: {k['w_magazynie']} szt.") 
# Oczekiwana kolejność: Mały Książę (0), Encyklopedia PWN (3), Poradnik Python (12), Wiedźmin (45), Krótki komiks (80)