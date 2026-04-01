class Postac:
    def __init__(self, imie, hp, zloto=0, poziom=1):
        self.imie = imie
        self.hp = hp
        self.max_hp = hp
        self.zloto = zloto
        self.poziom = poziom
    
    def otrzymaj_obrazenia(self, ile):
        if self.hp <= 0:
            return "Postać nie żyje!"
        self.hp -= ile
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def ulecz(self, ile):
        if self.hp <= 0:
            return "Nie można uleczyć!"
        self.hp += ile
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        return self.hp
    
    def zbierz_zloto(self, ile):
        self.zloto += ile
        return self.zloto
    
    def get_status(self):
        return f"{self.imie} | HP: {self.hp}/{self.max_hp} | Złoto: {self.zloto} | Lvl: {self.poziom}"
