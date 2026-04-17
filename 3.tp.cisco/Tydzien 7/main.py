#Tradycyjna Funkcja
def dodaj(a,b):
    return  a+b
#lambda
#dodawanie = lambda a,b: a+b
dodawanie = (lambda a,b: a+b)(3,4)
print(dodawanie)
#Warunki w Lambda
czy_parzysta = lambda x: "Parzysta" if x%2==0 else "Nieparzysta"
##
goyslop = lambda x: "goyslop" if "67" in x else "Nie goyslop"
## Transformacje List
liczby = [1,2,3,4,5]
###Tradycyjne podejście
kwadraty_for = []
for n in liczby:
    kwadraty_for.append(n**2)
print(kwadraty_for)
### wersja Lambda
kwadraty_map = list(map(lambda  x: x**2 ,liczby))
print(kwadraty_map)
### Wersja super ultra skibid one piece
kwadraty = [x ** 2 for x in liczby]
print(kwadraty)
#Ostre Tebowanie
wiek_uczniow = [16,17,21,15,19,18,17]
pelnoletni_uczniowie = list(filter(lambda wiek: wiek >= 18, wiek_uczniow))
print(pelnoletni_uczniowie)
#Filtrowanie Słowników
produkty = [
    {"nazwa": "Mysz GM11" , "marka": "MSI", "cena": 89.99, "dostępny":True},
    {"nazwa": "Klawiatura Virgo GK30", "marka": "MSI" ,"cena":229.99, "dostępny":False},
    {"nazwa": "Redmi Buds 6.7" , "marka": "Xiaomi", "cena": 67, "dostępny":True},
    {"nazwa": "16GB Ram DDR5", "marka":"Xiao Long Bao", "cena": 2000, "dostępny":False},
    {"nazwa": "Mysz GM10" , "marka": "MSI", "cena": 30.99, "dostępny":False},
]
dostepne_produkty = list(filter(lambda p: p['dostępny'], produkty))
print(dostepne_produkty)
tanie_produkty = list(filter(lambda p: p['cena'] <=100,  produkty))
print(tanie_produkty)
#sortowanie
for p in sorted(dostepne_produkty, key=lambda p: (p['marka'], p['cena'])):
    print(f"{p['nazwa']} - Producent - {p['marka']}")