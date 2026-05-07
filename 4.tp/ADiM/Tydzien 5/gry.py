class mainClass():
    def __init__(self, lista_danych, kwota):
        self.lista = lista_danych
        self.kwota = kwota
        
    def dodaj_do_listy(self, item):
        self.lista.append(item)
        
    def usun_z_listy(self, item):
        self.lista.remove(item)
        
    def dodaj_saldo(self, kwota):
        if  isinstance(kwota,str):
            raise TypeError
        if kwota <= 0:
            raise ValueError
        
        self.kwota += kwota