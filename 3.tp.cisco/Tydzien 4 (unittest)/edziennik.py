

class edziennik:

    def __init__(self, klasa, uczniowie, wychowawca):
        self.klasa = klasa
        self.uczniowie = uczniowie
        self.wychowawca = wychowawca

    def nowy_uczen(self, uczen):
        self.uczniowie.append(uczen)
        return

    def usun_ucznia(self,uczen):
        self.uczniowie.remove(uczen)
