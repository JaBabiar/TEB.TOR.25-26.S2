# CZĘŚĆ 1: LISTY
# 1. Utwórz listę zawierającą pięć dowolnych imion.
nazwaListy = ["Adam", "Bartek", "Czarek", "Marek", "Jarek"]
# 2. Wyświetl trzeci element tej listy (pamiętaj o indeksowaniu od zera!).
print(nazwaListy[2])
# 3. Dodaj na koniec listy swoje imię.
nazwaListy.append("Adrian")
# 4. Usuń drugi element z listy.
nazwaListy.pop(1)
# 5. Odwróć kolejność elementów w liście i wyświetl wynik.
nazwaListy.reverse()
# 6. Utwórz nową listę zawierającą tylko imiona zaczynające się na literę "A" (lub inną wybraną).
imieNaA = []
for imie in nazwaListy:
    if imie.startswith("A"):
        imieNaA.append(imie)
print(imieNaA)
# 7. Połącz dwie listy: jedną z imionami, a drugą z nazwiskami – tak aby powstała lista par (np. ["Jan", "Kowalski"]).
imiona = ["Anna", "Piotr", "Kasia", "Marek", "Julia"]
nazwiska = ["Kowalski", "Nowak", "Wiśniewski", "Wójcik", "Kamińska"]
imieNazwisko = []
for para in zip(imiona, nazwiska):
    imieNazwisko.append(list(para))
print(imieNazwisko)


# CZĘŚĆ 2: SŁOWNIKI
# 1. Utwórz słownik reprezentujący ucznia: klucze to "imię", "nazwisko", "klasa", a wartości – przykładowe dane.
# 2. Dodaj do słownika nowy klucz "oceny" z wartością będącą listą liczb (np. [5, 4, 6, 3]).
# 3. Wyświetl tylko listę ocen ucznia.
# 4. Oblicz i wyświetl średnią ocen ucznia.
# 5. Utwórz słownik klas, w którym każda klasa (np. "3A", "3B") ma swój własny słownik z danymi uczniów:
#    np. {"3A": {"uczniowie": [{"imię": "Ziutek", "oceny": [5, 6]}, ...], "wychowawca": "Pan Nowak"}}
klasy = {
    "3TP": {
        "uczniowie": [
            {"imie": "Ziutek", "oceny": [5,6]},
            {"imie": "Ziutek", "oceny": [2,4]},
        ],
        "wychowawca": "Jan Nowak"
    },
    "4TP": {
        "uczniowie": [
            {"imie": "Ziutek", "oceny": [5, 6]},
            {"imie": "Ziutek", "oceny": [2, 4]},
        ],
        "wychowawca": "Jan Wanok"
    }

}
# 6. Dodaj nowego ucznia do jednej z klas.
nowy_uczen = {"imie": "kotolga", "oceny": [4,3]}
klasy["3TP"]["uczniowie"].append(nowy_uczen)
# 7. Znajdź ucznia z najwyższą średnią ocen w danej klasie i wyświetl jego imię.
def najlepszy_uczen(nazwa_klasy):
    uczniowie = klasy[nazwa_klasy]["uczniowie"]
    # wybieramy ucznia z najwyższą średnią
    najlepszy = max(uczniowie, key=lambda u: sum(u["oceny"]) / len(u["oceny"]))
    najgorszy = min(uczniowie, key=lambda u: sum(u["oceny"])/ len(u["oceny"]))
    return najlepszy["imie"]

print(najlepszy_uczen("3TP"))
