class Postac:
    def __init__(self,imie,hp):
        self.imie = imie 
        self.hp = hp 
        self.max_hp = hp
    
    def otrzymaj_obrazenia(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0 
        return self.hp
    
    def status(self):
        return f"{self.imie}: {round(self.hp,2)} / {self.max_hp}"