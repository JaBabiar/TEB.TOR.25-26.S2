# =====================================================================
# KARTKÓWKA: Podstawy Pythona (Listy, Słowniki, Klasy i Obiekty)
# Maksymalna liczba punktów: 20
# Imię i nazwisko: ....................................................
# =====================================================================

# ---------------------------------------------------------------------
# ZADANIE 1: Listy i logika (7 punktów)
# ---------------------------------------------------------------------
# Poniżej zdefiniowano listę początkową. Nie zmieniaj tej linijki.
liczby = [9, 22, 3, 16, 8]

# a) (2 pkt) Dodaj do powyższej listy liczbę 11, a następnie 
#    posortuj całą listę rosnąco.
# Miejsce na Twój kod:



# b) (2 pkt) Wypisz z listy wyłącznie te liczby, które są NIEPARZYSTE.
# Miejsce na Twój kod:



# c) (2 pkt) Oblicz i wypisz średnią arytmetyczną wszystkich 
#    elementów obecnych na liście.
# Miejsce na Twój kod:



# d) (1 pkt) Sprawdź, czy liczba 3 znajduje się na liście, 
#    i wypisz na ekran odpowiedni komunikat informujący o wyniku.
# Miejsce na Twój kod:




# ---------------------------------------------------------------------
# ZADANIE 2: Słowniki (5 punktów)
# ---------------------------------------------------------------------
# Poniżej zdefiniowano początkowy słownik. Nie zmieniaj tej linijki.
film = {
    'tytul': "Matrix",
    'ocena': 7
}

# a) (1 pkt) Zmień wartość przypisaną do klucza 'ocena' na 9.
# Miejsce na Twój kod:



# b) (2 pkt) Dodaj do słownika informację o roku wydania (klucz 'rok_wydania') 
#    z przypisaną wartością 1999.
# Miejsce na Twój kod:



# c) (2 pkt) Pobierz i wypisz na ekran wszystkie same WARTOŚCI 
#    występujące w słowniku.
# Miejsce na Twój kod:




# ---------------------------------------------------------------------
# ZADANIE 3: Klasy i Obiekty (8 punktów)
# ---------------------------------------------------------------------
# Poniżej przygotowano szkielety klas. Twoim zadaniem jest ich uzupełnienie
# poprzez zastąpienie słowa kluczowego 'pass' odpowiednim kodem.

class Pojazd:
    # a) (2 pkt) Uzupełnij konstruktor tak, aby przypisywał do obiektu 
    #    atrybuty 'marka' oraz 'paliwo'. 'paliwo' musi mieć 
    #    wartość domyślną równą 100.
    def __init__(self, marka, paliwo):
        pass

    # b) (2 pkt) Uzupełnij metodę tak, aby zmniejszała 'paliwo' obiektu 
    #    o wartość 'zuzycie', a następnie wypisywała komunikat 
    #    o aktualnym stanie paliwa pojazdu.
    def zuzyj_paliwo(self, zuzycie):
        pass


class Samochod(Pojazd):
    # c) (2 pkt) Uzupełnij konstruktor klasy Samochod. Wykorzystaj mechanizm 
    #    dziedziczenia, aby zainicjować 'marka' i 'paliwo' z klasy bazowej. 
    #    Następnie utwórz nowy atrybut 'przebieg' (z wartością domyślną 0).
    def __init__(self, marka, paliwo=100, przebieg=0):
        pass


# d) (2 pkt) Utwórz obiekt klasy Samochod o marce "Ford" 
#    (resztę parametrów pozostaw domyślną). Następnie spraw, aby ten 
#    obiekt zużył 30 jednostek paliwa, wywołując odpowiednią metodę.
# Miejsce na Twój kod:
