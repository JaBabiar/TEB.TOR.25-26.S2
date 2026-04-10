"""
Docstring for 3.tp.cisco.Tydzien 6.main

Funkcje map oraz filter
"""


testowaLista = ("jedne", "dwa", "tri")

print(list(map(lambda x: "numer: "+x, testowaLista)))

## Filter - produkty w przedziale cenowym 
sprzet = msi_sprzet = {
    "MSI Vigor GK30": {"typ": "klawiatura", "cena": 180},
    "MSI Vigor GK50 Low Profile": {"typ": "klawiatura", "cena": 350},
    "MSI Vigor GK50 Elite": {"typ": "klawiatura", "cena": 420},
    "MSI Clutch GM08": {"typ": "mysz", "cena": 70},
    "MSI Clutch GM11": {"typ": "mysz", "cena": 90},
    "MSI Clutch GM20 Elite": {"typ": "mysz", "cena": 150},
    "MSI Immerse GH20": {"typ": "słuchawki", "cena": 120},
    "MSI Immerse GH30 V2": {"typ": "słuchawki", "cena": 115},
    "MSI Agility GD20": {"typ": "podkładka", "cena": 45},
    "MSI Agility GD60": {"typ": "podkładka", "cena": 150}
}
minimalna = input("Podaj Cene minimalną: ")
maksymalna = input("Podaj Cene Maksymalną: ")

