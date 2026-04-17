class Komputer:
    def __init__(self, nazwa, peryferia):
        self.nazwa = nazwa
        self.peryferia = peryferia
        self.glosnosc = 100

    def zarzadzaj_dzwiekiem(self, zmiana):
        if (self.glosnosc + zmiana > 100):
            self.glosnosc = 100
            return self.glosnosc

        self.glosnosc += zmiana
        return self.glosnosc

    def podepnij_urzadzenie(self, dev):
        if (isinstance(dev, str)):
            self.peryferia += [dev]
        else:
            raise TypeError

    def odepnij_urzadzenie(self, dev):
        if (isinstance(dev, str)):
            self.peryferia.remove(dev)
        else:
            raise TypeError



