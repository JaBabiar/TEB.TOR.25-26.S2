class Gracz:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.ekwipunek = []

    def dodaj_punkty(self, punkty):
        if isinstance(punkty, str):
            raise TypeError("Zły Typ Danych")

        self.points += punkty

        if self.points < 0:
            raise ValueError("Punkty nie mogą być ujemne")

    def podnies_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)
    def wyrzuc_item(self, przedmiot):
        self.ekwipunek.remove(przedmiot)