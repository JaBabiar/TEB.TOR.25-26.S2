##
# Stwórz klase Szkoła zaweirające nazwe szkoły, miasto, klasy
# Stwórz klase Klasa która będzie zawierała Nazwe klasy, Uczniów profil i wychowawce
# Stwórz klase uczeń która będzie zawierała imie, nazwisko oraz będzie rozszeniem klasy Klasa
##

import json

def load_data():
    try:
        with open("./klasy.json", "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading settings: {e}")
        return {}

dane_klas = load_data()



class Szkola:
    def __init__(self, nazwa_szkoly, miasto):
        self.nazwa = nazwa_szkoly
        self.miasto = miasto
        self.klasy = []

    def dodaj_klase(self, k):
        self.klasy.append(k)
    def policz_uczniow(self):
        suma = 0
        for klasa in self.klasy:
            suma += klasa.policz_uczniow()
        return suma

class Klasa:
    def __init__(self, nazwa_klasy, kierunek):
        self.nazwa_klasy = nazwa_klasy
        self.kierunek = kierunek
        self.uczniowie = []
    def policz_uczniow(self):
        return len(self.uczniowie)

    def dodaj_ucznia(self, u):
            self.uczniowie.append(u)

    def dane_uczniow(self):
        dane = []

        for uczen in self.uczniowie:
            nazwa = f"{uczen.imie} {uczen.nazwisko}"
            dane.append(nazwa)
        return dane

class Uczen:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


szkola = Szkola(dane_klas['nazwa_szkoly'], dane_klas['miasto'])

for klasa in dane_klas['klasy']:
    obiektKlasy = Klasa(klasa['symbol'], klasa['profil'])
    szkola.dodaj_klase(obiektKlasy)
    for uczen in klasa['uczniowie']:
        u = Uczen(uczen["imie"], uczen['nazwisko'])
        obiektKlasy.dodaj_ucznia(u)

print(szkola.policz_uczniow())
##
# Dodaj Funkcje która wyświetla wszystkich uczniów w danej klasie
# Dodaj Funkcje która podaje ilość uczniów w klasie (Jako funkcje klasy)
# Dodaj Funkcje która podaje ilość uczniów w szkole (Jako Funkcje klasy)
# https://github.com/JaBabiar/4TP/tree/main/sem2/powt