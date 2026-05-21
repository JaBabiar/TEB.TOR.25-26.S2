import random


class Wyszukiwanie:
    def __init__(self):
        self.__tablica = []
        for i in range(10):
            self.__tablica.append(random.randint(1,100))

    def __dodaj_wartownika(self, wartownik):
        self.__tablica.append(wartownik)

    def szukaj_elementu(self,wartosc):
        self.__dodaj_wartownika(wartosc)

        i = 0
        while self.__tablica[i] != wartosc:
            i += 1
        self.__tablica.pop()

        if i == 10:
            return -1
        else:
            return i
    def get_tablica(self):
        return self.__tablica

## Krok 4 z notatek
if __name__ == "__main__":
    # 1. Utworzenie obiektu
    app = Wyszukiwanie()

    wylosowane = app.get_tablica()
    print("Wylosowana tablica:", ", ".join(map(str, wylosowane)))

    szukana_liczba = int(input("Podaj liczbę do wyszukania: "))

    # 3. Wywołanie metody i wynik
    indeks = app.szukaj_elementu(szukana_liczba)

    if indeks != -1:
        print(f"Znaleziono element pod indeksem: {indeks}")
    else:
        print("Szukanej liczby nie ma w wylosowanej tablicy.")
