"""
Docstring for 3.tp.cisco.Tydzien 6.main

Funkcje map oraz filter
"""


testowaLista = ("jedne", "dwa", "tri")

print(list(map(lambda x: "numer: "+x, testowaLista)))

## Filter - produkty w przedziale cenowym 
msi_sprzet = [
    {"nazwa": "MSI Vigor GK30", "typ": "klawiatura", "cena": 180},
    {"nazwa": "MSI Vigor GK50 Low Profile", "typ": "klawiatura", "cena": 350},
    {"nazwa": "MSI Vigor GK50 Elite", "typ": "klawiatura", "cena": 420},
    {"nazwa": "MSI Clutch GM08", "typ": "mysz", "cena": 70},
    {"nazwa": "MSI Clutch GM11", "typ": "mysz", "cena": 90},
    {"nazwa": "MSI Clutch GM20 Elite", "typ": "mysz", "cena": 150},
    {"nazwa": "MSI Immerse GH20", "typ": "słuchawki", "cena": 120},
    {"nazwa": "MSI Immerse GH30 V2", "typ": "słuchawki", "cena": 115},
    {"nazwa": "MSI Agility GD20", "typ": "podkładka", "cena": 45},
    {"nazwa": "MSI Agility GD60", "typ": "podkładka", "cena": 150}
]
#minimalna = input("Podaj Cene minimalną: ")
#maksymalna = input("Podaj Cene Maksymalną: ")
#filtrowana = list(filter(lambda x: int(minimalna) <= x["cena"] <= int(maksymalna), msi_sprzet ))
#print(filtrowana)

## bloki try... except
def podziel_pizze(osoby, kawałki=8):
    try:
        wynik = kawałki / osoby
        return f"Każda osobo ma {wynik} kawałki"
    except ZeroDivisionError:
        return "Nie dziel przez 0"
    except TypeError:
        return "Zły typ danych >////<"

print(podziel_pizze(4))
print(podziel_pizze(0))
print(podziel_pizze("dwie"))