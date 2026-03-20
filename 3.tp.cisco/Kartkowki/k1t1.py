# =====================================================================
# KARTKÓWKA: Podstawy Pythona (Listy, Słowniki, Klasy i Obiekty)
# Maksymalna liczba punktów: 20
# Imię i nazwisko: ....................................................
# =====================================================================

# ---------------------------------------------------------------------
# ZADANIE 1: Listy i logika (7 punktów)
# ---------------------------------------------------------------------
# Poniżej zdefiniowano listę początkową. Nie zmieniaj tej linijki.
liczby = [15, 2, 8, 21, 5]

# a) (2 pkt) Dodaj do powyższej listy liczbę 10, a następnie 
#    posortuj całą listę rosnąco.
# Miejsce na Twój kod:



# b) (2 pkt) Wypisz z listy wyłącznie te liczby, które są parzyste.
# Miejsce na Twój kod:



# c) (2 pkt) Oblicz i wypisz średnią arytmetyczną wszystkich 
#    elementów obecnych na liście.
# Miejsce na Twój kod:



# d) (1 pkt) Sprawdź, czy liczba 8 znajduje się na liście, 
#    i wypisz na ekran odpowiedni komunikat informujący o wyniku.
# Miejsce na Twój kod:




# ---------------------------------------------------------------------
# ZADANIE 2: Słowniki (5 punktów)
# ---------------------------------------------------------------------
# Poniżej zdefiniowano początkowy słownik. Nie zmieniaj tej linijki.
gra = {
    'tytul': "Wiedźmin",
    'ocena': 8
}

# a) (1 pkt) Zmień wartość przypisaną do klucza 'ocena' na 10.
# Miejsce na Twój kod:



# b) (2 pkt) Dodaj do słownika informację o roku wydania (klucz 'rok_wydania') 
#    z przypisaną wartością 2015.
# Miejsce na Twój kod:



# c) (2 pkt) Pobierz i wypisz na ekran wszystkie same klucze 
#    występujące w słowniku.
# Miejsce na Twój kod:




# ---------------------------------------------------------------------
# ZADANIE 3: Klasy i Obiekty (8 punktów)
# ---------------------------------------------------------------------
# Poniżej przygotowano szkielety klas. Twoim zadaniem jest ich uzupełnienie
# poprzez zastąpienie słowa kluczowego 'pass' odpowiednim kodem.

class Postac:
    # a) (2 pkt) Uzupełnij konstruktor tak, aby przypisywał do obiektu 
    #    atrybuty 'imie' oraz 'punkty_zycia'. 'punkty_zycia' muszą mieć 
    #    wartość domyślną równą 100.
    def __init__(self, imie, punkty_zycia=100):
        pass

    # b) (2 pkt) Uzupełnij metodę tak, aby zmniejszała 'punkty_zycia' obiektu 
    #    o wartość 'obrazenia', a następnie wypisywała komunikat 
    #    o aktualnym stanie życia postaci.
    def otrzymaj_obrazenia(self, obrazenia):
        pass


class Mag(Postac):
    # c) (2 pkt) Uzupełnij konstruktor klasy Mag. Wykorzystaj mechanizm 
    #    dziedziczenia, aby zainicjować 'imie' i 'punkty_zycia' z klasy bazowej. 
    #    Następnie utwórz nowy atrybut 'mana' (z wartością domyślną 50).
    def __init__(self, imie, punkty_zycia=100, mana=50):
        pass


# d) (2 pkt) Utwórz obiekt klasy Mag o imieniu "Gandalf" 
#    (resztę parametrów pozostaw domyślną). Następnie zadaj temu 
#    obiektowi 20 punktów obrażeń, wywołując odpowiednią metodę.
# Miejsce na Twój kod: