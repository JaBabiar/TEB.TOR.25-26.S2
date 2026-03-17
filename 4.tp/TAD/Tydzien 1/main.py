# Stwórz klase pytanie która zawiera wartości
# - tresc / odpowiedzi / odpowiedz poprawna
# oraz metody
# odpowiedz
# Quiz który zawiera wartości
# Punkty / Lista Pytan / Imie I nazwisko /Wynik


class Quiz:
    def __init__(self, nazwa):
        self.punkty = 0
        self.max_punkty = 0
        self.nazwa = nazwa
        self.lista_pytan = []
    def getResult(self):
        return self.punkty
    def getQ(self, i):
        return self.lista_pytan[i-1]
    def addQ(self, p):
        self.lista_pytan.append(p)


class Pytanie:
    def __init__(self, tresc, odp, correct):
        self.tresc = tresc
        self.odp = odp
        self.correct = correct

    def getAnswer(self):
        print("Podaj Odpowiedz: ")
        user_input = input()
        if int(user_input) == self.correct:
            print("Poprawne")
        else:
            print("Zle")

def main():
    quiz = Quiz("test")
    quiz.addQ(Pytanie("Ile dni jest w 2025? ", ["365", "366"], 1))
    print(quiz.getQ(1).tresc)
    quiz.getQ(1).getAnswer()
    return 0

main()

