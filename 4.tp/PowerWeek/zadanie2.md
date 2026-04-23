Oto treść zadania przygotowana do zapisania w pliku `zadanie2.md`. Jest ono skonstruowane tak, aby uczeń mógł je wykonać w 20–30 minut, przechodząc przez wszystkie etapy: od projektu, przez logikę, aż po zapis i odczyt danych.

---

# 📝 Zadanie 2: System Rejestracji na Turniej E-sportowy
**Czas na wykonanie:** 20-30 minut  
**Temat:** Obsługa wyborów użytkownika (Radio, Combo, Checkbox) oraz praca z plikiem `.txt`.

---

## 3.1. Krok 1: Projekt w Qt Designer (ok. 10 min)

Stwórz interfejs aplikacji, który pozwoli zapisać zawodnika na turniej.

1.  **MainWindow:** Ustaw tytuł okna na "Rejestracja Turnieju".
2.  **Dane tekstowe:** Dodaj `Label` ("Nick:") oraz `Line Edit`. Nazwij go: `input_nick`.
3.  **Wybór gry (ComboBox):** Dodaj `Label` ("Wybierz grę:") oraz `Combo Box`. W edytorze elementów (kliknij dwa razy na Combo Box) dodaj: *League of Legends*, *Counter-Strike 2*, *Valorant*. Nazwij go: `combo_gra`.
4.  **Poziom (Radio Buttons):** Dodaj `Group Box` z tytułem "Poziom zaawansowania". W środku umieść dwa `Radio Button`: *Amator* oraz *Pro*. Nazwij je odpowiednio: `radio_amator` i `radio_pro`.
5.  **Dodatki (CheckBox):** Dodaj `Check Box` z tekstem "Własna myszka". Nazwij go: `check_mysz`.
6.  **Przyciski:** Dodaj dwa przyciski `Push Button`:
    * "Zapisz zawodnika" -> `btn_zapisz`
    * "Pokaż listę" -> `btn_lista`
7.  **Podgląd:** Dodaj `Plain Text Edit` na dole okna. Nazwij go: `txt_podglad` i zaznacz mu opcję `readOnly`.
8.  **Layout:** Zastosuj `Vertical Layout` na całym oknie, aby elementy równo się rozkładały.
9.  **Zapisz plik jako `turniej.ui`.**

---

## 3.2. Krok 2: Logika w Pythonie (ok. 15 min)

Twoim zadaniem jest ożywienie aplikacji. Wykorzystaj poniższy schemat.

```python
import sys
from PyQt6 import QtWidgets, uic

class TurniejApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("turniej.ui", self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TurniejApp()
    window.show()
    app.exec()
```

---

## 3.3. Checklista sukcesu (Sprawdź się!)

- [ ] Czy po kliknięciu "Zapisz" i ponownym kliknięciu "Pokaż listę" widzisz nowego gracza w polu na dole?
- [ ] Czy jeśli nie wpiszesz nicku, pojawia się ostrzeżenie?
- [ ] Czy po rozciągnięciu okna myszką, wszystkie pola również się powiększają (Layout)?
- [ ] Czy plik `gracze.txt` stworzył się w tym samym folderze co Twój kod?

---

**Podpowiedź dla szybkich:** Spróbuj zmienić kolor tła przycisku "Zapisz zawodnika" na zielony, korzystając z właściwości `styleSheet` w Designerze (`background-color: green; color: white;`).