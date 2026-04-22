# 📝 Zadanie Treningowe: "Kalkulator Kosztów Paliwa"

**Czas na wykonanie:** 30 minut  
**Cel:** Stworzenie aplikacji, która obliczy koszt przejazdu na podstawie wpisanych danych.

---

## Część 1: Qt Designer (10-15 minut)

Twoim zadaniem jest przygotowanie okna aplikacji, które wygląda estetycznie i reaguje na zmianę rozmiaru.

1. **Stwórz nowe okno typu `Main Window`.**
2. **Dodaj następujące elementy (Widgety):**
    * `Label` z tekstem: "Dystans do przejechania (km):"
    * `Line Edit` (miejsce na wpisanie km) -> zmień `objectName` na: **input_dystans**
    * `Label` z tekstem: "Cena paliwa za litr (PLN):"
    * `Line Edit` (miejsce na cenę) -> zmień `objectName` na: **input_cena**
    * `Push Button` z tekstem: "Oblicz koszt" -> zmień `objectName` na: **btn_oblicz**
    * `Label` (miejsce na wynik) -> zmień `objectName` na: **lbl_wynik** (usuń z niej domyślny tekst "TextLabel", niech będzie pusta).
3. **Ustaw Layouty:**
    * Zaznacz wszystkie elementy i ustaw je w pionie (`Lay Out Vertically`).
    * Kliknij na tło okna i ustaw layout główny (`Lay Out Vertically`), aby aplikacja wypełniała okno.
4. **Dodatki (Dostępność):**
    * Kliknij na `MainWindow` i w Property Editorze ustaw `minimumSize` na **300 x 200**.
5. **Zapisz plik jako `kalkulator.ui` w folderze ze swoim skryptem Python.**

---

## Część 2: Python (10-15 minut)

Ożyw aplikację. Wykorzystaj poniższy wzór. Twoim zadaniem jest uzupełnienie funkcji `oblicz`.

**Wzór do uzupełnienia:**

```python
import sys
from PyQt6 import QtWidgets, uic

class KalkulatorPaliwa(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("kalkulator.ui", self)
        
        # Podpięcie przycisku
        self.btn_oblicz.clicked.connect(self.oblicz)

    def oblicz(self):
        try:
            # 1. Pobierz dane z pól tekstowych (pamiętaj o zamianie na float!)
            dystans = float(self.input_dystans.text())
            cena = float(self.input_cena.text())
            
            # 2. Załóżmy średnie spalanie 8 litrów na 100 km
            spalanie = 8.0
            
            # 3. Oblicz koszt: (dystans / 100) * spalanie * cena
            koszt = (dystans / 100) * spalanie * cena
            
            # 4. Wyświetl wynik w lbl_wynik
            self.lbl_wynik.setText(f"Koszt podróży to: {koszt:.2f} PLN")
            
        except ValueError:
            # Wyświetl błąd jeśli ktoś wpisze litery zamiast liczb
            QtWidgets.QMessageBox.critical(self, "Błąd", "Wprowadź poprawne liczby!")

app = QtWidgets.QApplication(sys.argv)
okno = KalkulatorPaliwa()
okno.show()
app.exec()
```

---

## Kryteria sukcesu (Checklista dla ucznia):

1. [ ] Czy plik `.ui` ma taką samą nazwę jak w kodzie?
2. [ ] Czy nazwy `objectName` w Designerze są identyczne jak te w kodzie Pythona?
3. [ ] Czy po rozciągnięciu okna przyciski i pola tekstowe również się rozszerzają?
4. [ ] Czy po wpisaniu tekstu zamiast liczb aplikacja pokazuje okno z błędem zamiast się wyłączyć?
5. [ ] Czy wynik wyświetla się z dokładnością do dwóch miejsc po przecinku (np. `15.50 PLN`)?
