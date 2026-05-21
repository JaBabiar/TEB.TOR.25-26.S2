# Kartkówka: Projektowanie GUI w Qt Designer

## Wymagania techniczne (Qt Designer)

1. **Główne okno:** Stwórz projekt oparty na szablonie `QMainWindow` lub `QWidget`.
2. **Układy (Layouts):**
   * Całość powinna być zamknięta w głównym układzie pionowym (`Vertical Layout`).
   * Formularz wprowadzania danych (Marka, Model, Rok produkcji) musi używać układu formularza (`Form Layout`).
   * Przyciski na dole muszą być ułożone obok siebie za pomocą układu poziomego (`Horizontal Layout`) i wyrównane do lewej strony okna (wykorzystaj do tego `Horizontal Spacer` wstawiony po prawej stronie przycisków).
3. **Widżety:**
   * Tytuł: `Label` (zwiększ czcionkę, ustaw pogrubienie i wyśrodkowanie tekstu).
   * Pola wprowadzania tekstu: `Line Edit`.
   * Pole na rok produkcji: `Spin Box` (ustaw domyślną wartość w okienku właściwości na 2015).
   * Przyciski: `Push Button`.
4. **Nazewnictwo obiektów (objectName):**
   * Zmień właściwość `objectName` dla przycisku "Dodaj" na: `btn_add`.
   * Zmień właściwość `objectName` dla przycisku "Wyczyść" na: `btn_clear`.
5. **Zapis:** Zapisz swój projekt jako plik o nazwie `pojazd.ui`.

## Zadanie końcowe: Import do Pythona

Gdy Twój interfejs jest już gotowy i zapisany, utwórz plik `app.py` w tym samym folderze co Twój plik `pojazd.ui`. 
Użyj poniższego kodu, aby wczytać i wyświetlić zaprojektowany interfejs:

```python
import sys
from PyQt6 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Wczytywanie pliku interfejsu
        uic.loadUi("pojazd.ui", self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



