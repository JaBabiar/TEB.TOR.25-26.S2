# Zadanie Desktopowa

## Część II. Aplikacja desktopowa

Za pomocą dostępnego na stanowisku egzaminacyjnym środowiska programistycznego i narzędzia do projektowania interfejsów (np. QtDesigner) wykonaj aplikację desktopową realizującą funkcję kalkulatora kosztów podróży.

**Opis wyglądu aplikacji w stanie początkowym:**

1. **Tytuł okna:** „Kalkulator podróży. Wykonał: ” a po nim wstawiony numer zdającego.
2. **Tło okna:** Kolor jasnoszary (np. `#F0F0F0`).
3. **Kontrolki na formularzu (zastosuj czytelny układ, np. siatkę lub układ pionowy):**

* Etykieta z tekstem: „Podaj dystans w kilometrach:” oraz pole tekstowe umożliwiające wpisanie wartości.
* Etykieta z tekstem: „Podaj średnie spalanie (l/100km):” oraz pole tekstowe umożliwiające wpisanie wartości.
* Etykieta z tekstem: „Cena paliwa za litr:” oraz suwak (Slider) ułożony poziomo.
* Suwak powinien mieć minimalną wartość 4, a maksymalną 10 (odpowiadające kwocie w złotych). Wartość początkowa to 6.
* Z prawej strony suwaka etykieta wyświetlająca aktualną wartość suwaka (początkowo „6 zł”).
* Przycisk z napisem „OBLICZ KOSZT” o zielonym kolorze tła.
* Na dole okna duża etykieta przeznaczona na wynik, z pogrubioną czcionką, domyślnie pusta.



**Działanie aplikacji:**

1. Zmiana położenia suwaka powoduje natychmiastową zmianę wartości na etykiecie obok suwaka (np. po przesunięciu na wartość 7, etykieta zmienia tekst na „7 zł”).
2. Po wciśnięciu przycisku „OBLICZ KOSZT” aplikacja:

* Pobiera wartości z obu pól tekstowych oraz aktualną wartość suwaka.
* Oblicza całkowity koszt podróży według wzoru: `(dystans / 100) * spalanie * cena`.
* Wyświetla wynik na dolnej etykiecie w formacie: „Koszt podróży wyniesie: [wynik] zł”.


3. Aplikacja powinna być zabezpieczona przed wprowadzeniem błędnych danych. Jeśli w polach tekstowych nie ma liczb, po wciśnięciu przycisku na dolnej etykiecie powinien pojawić się komunikat o błędzie (np. „Błąd: Wprowadź poprawne dane liczbowe”).

Aplikacja powinna być zapisana czytelnie, z zasadami czystego formatowania kodu, należy stosować znaczące nazwy zmiennych i funkcji, również dla elementów interfejsu użytkownika w pliku projektowym.

Kod aplikacji przygotuj do nagrania na płytę. W folderze `desktopowa` powinno znaleźć się archiwum całego projektu o nazwie `desktopowa.zip`, skopiowane z projektu pliki źródłowe (w tym wygenerowany lub zapisany plik interfejsu `.ui`) oraz logika aplikacji.

---

## Szablon aplikacji desktopowej PyQt5 / QtDesigner (INF.04)

Poniżej znajduje się kod startowy, który potrafi załadować plik `.ui` stworzony w QtDesignerze. Waszym zadaniem jest uzupełnienie logiki w miejscach oznaczonych jako `TODO`.

### Krok 1: Projekt w QtDesigner

1. Otwórz QtDesigner i stwórz formularz `Main Window` lub `Widget`.
2. Dodaj z przybornika potrzebne elementy: `QLabel`, `QLineEdit`, `QSlider`, `QPushButton`.
3. **Ważne:** Zmień nazwy obiektów w prawym panelu (`Object Inspector`) na logiczne! Zamiast `lineEdit_2` nazwij go np. `input_spalanie`. Zamiast `pushButton` nazwij go `btn_oblicz`.
4. Ustaw odpowiednie wartości domyślne dla suwaka (min, max, value) w panelu właściwości (`Property Editor`).
5. Zapisz plik jako `interfejs.ui` w tym samym folderze co Twój skrypt Pythona.

## Krok 2: Uzupełnienie logiki w Pythonie

Skopiuj poniższy szablon i uzupełnij brakujące fragmenty kodu.

```python
import sys
from PyQt5 import QtWidgets, uic

class KalkulatorPodrozy(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. Ładowanie pliku z interfejsem
        uic.loadUi("interfejs.ui", self)
        
        # 2. Ustawienie tytułu okna (wymóg CKE)
        self.setWindowTitle("Kalkulator podróży. Wykonał: 00000000000")
        
        # -------------------------------------------------------------
        # TODO: 3. Podpinanie sygnałów do slotów (metod)
        # -------------------------------------------------------------
        # Podepnij kliknięcie przycisku obliczania:
        # self.nazwa_przycisku.clicked.connect(self.oblicz_koszt)
        
        
        # Podepnij przesuwanie suwaka. 
        # Podstawowym sygnałem do wykorzystania jest 'valueChanged':
        # self.nazwa_suwaka.valueChanged.connect(self.aktualizuj_suwak)
        

    # -----------------------------------------
    # Metody obsługujące zdarzenia (Sloty)
    # -----------------------------------------
    def aktualizuj_suwak(self):
        # TODO: Pobierz wartość z suwaka za pomocą metody .value()
        # TODO: Ustaw pobraną wartość jako tekst w odpowiedniej etykiecie (.setText())
        pass

    def oblicz_koszt(self):
        try:
            # TODO: Pobierz tekst z pól wprowadzania za pomocą .text()
            # TODO: Zrzutuj pobrany tekst na typ zmiennoprzecinkowy (float)
            # TODO: Pobierz wartość z suwaka (.value())
            
            # TODO: Oblicz wynik używając wzoru z zadania
            
            # TODO: Wyświetl wynik na dolnej etykiecie (.setText())
            pass
            
        except ValueError:
            # Obsługa błędu, gdy użytkownik wpisze tekst zamiast liczb
            # TODO: Wyświetl komunikat o błędzie na dolnej etykiecie
            pass

# ==========================================
# URUCHOMIENIE APLIKACJI
# ==========================================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    okno = KalkulatorPodrozy()
    okno.show()
    sys.exit(app.exec_())

```

## Przydatne ściągawki i sygnały

* **Sygnały dla QSlidera:** Głównym sygnałem, który reaguje na każdą zmianę wartości, jest `valueChanged`. Możecie jednak dodatkowo wykorzystać (i sprawdzić jak działają) inne sygnały, np.:
* `sliderMoved` - emitowany tylko podczas fizycznego przeciągania suwaka myszą.
* `sliderReleased` - emitowany dopiero po puszczeniu przycisku myszy.
* `sliderPressed` - emitowany w momencie kliknięcia na suwak.


* **Pobieranie tekstu z pola (QLineEdit):** `zmienna = self.nazwa_pola.text()`
* **Pobieranie liczby z suwaka (QSlider):** `zmienna = self.nazwa_suwaka.value()`
* **Ustawianie tekstu w etykiecie (QLabel):** `self.nazwa_etykiety.setText("Mój tekst")`
* **Rzutowanie tekstu na liczbę:** `liczba = float("5.5")`
