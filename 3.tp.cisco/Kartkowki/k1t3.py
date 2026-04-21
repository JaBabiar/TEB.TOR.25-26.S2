# =====================================================================
# KARTKÓWKA: Podstawy Pythona (Listy, Słowniki, Klasy i Obiekty) - POPRAWA
# Maksymalna liczba punktów: 20
# Imię i nazwisko: ....................................................
# =====================================================================

# ---------------------------------------------------------------------
# ZADANIE 1: Listy i logika (7 punktów)
# ---------------------------------------------------------------------
# Poniżej zdefiniowano listę początkową. Nie zmieniaj tej linijki.
liczby = [14, 7, 25, 4, 18]

# a) (2 pkt) Dodaj do powyższej listy liczbę 12, a następnie 
#    posortuj całą listę malejąco (od największej do najmniejszej).
# Miejsce na Twój kod:



# b) (2 pkt) Wypisz z listy wyłącznie te liczby, które są MNIEJSZE od 15.
# Miejsce na Twój kod:



# c) (2 pkt) Oblicz i wypisz sumę wszystkich elementów 
#    obecnych na liście.
# Miejsce na Twój kod:



# d) (1 pkt) Sprawdź, czy liczba 7 znajduje się na liście, 
#    i wypisz na ekran odpowiedni komunikat informujący o wyniku.
# Miejsce na Twój kod:




# ---------------------------------------------------------------------
# ZADANIE 2: Słowniki (5 punktów)
# ---------------------------------------------------------------------
# Poniżej zdefiniowano początkowy słownik. Nie zmieniaj tej linijki.
ksiazka = {
    'tytul': "Hobbit",
    'strony': 250
}

# a) (1 pkt) Zmień wartość przypisaną do klucza 'strony' na 310.
# Miejsce na Twój kod:



# b) (2 pkt) Dodaj do słownika informację o autorze (klucz 'autor') 
#    z przypisaną wartością "Tolkien".
# Miejsce na Twój kod:



# c) (2 pkt) Pobierz i wypisz na ekran wszystkie PARY (zarówno klucz, 
#    jak i wartość) występujące w słowniku (np. używając metody items()).
# Miejsce na Twój kod:




# ---------------------------------------------------------------------
# ZADANIE 3: Klasy i Obiekty (8 punktów)
# ---------------------------------------------------------------------
# Poniżej przygotowano szkielety klas. Twoim zadaniem jest ich uzupełnienie
# poprzez zastąpienie słowa kluczowego 'pass' odpowiednim kodem.

class Zwierze:
    # a) (2 pkt) Uzupełnij konstruktor tak, aby przypisywał do obiektu 
    #    atrybuty 'imie' oraz 'energia'. 'energia' musi mieć 
    #    wartość domyślną równą 100.
    def __init__(self, imie, energia=100):
        pass

    # b) (2 pkt) Uzupełnij metodę tak, aby zmniejszała 'energia' obiektu 
    #    o wartość 'zmeczenie', a następnie wypisywała komunikat 
    #    o aktualnym stanie energii zwierzęcia.
    def mecz_sie(self, zmeczenie):
        pass


class Pies(Zwierze):
    # c) (2 pkt) Uzupełnij konstruktor klasy Pies. Wykorzystaj mechanizm 
    #    dziedziczenia, aby zainicjować 'imie' i 'energia' z klasy bazowej. 
    #    Następnie utwórz nowy atrybut 'rasa' (z wartością domyślną "Mieszaniec").
    def __init__(self, imie, energia=100, rasa="Mieszaniec"):
        pass


# d) (2 pkt) Utwórz obiekt klasy Pies o imieniu "Burek" 
#    (resztę parametrów pozostaw domyślną). Następnie spraw, aby ten 
#    obiekt stracił 40 punktów energii, wywołując odpowiednią metodę.
# Miejsce na Twój kod: