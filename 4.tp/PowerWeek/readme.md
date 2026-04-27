# 🚀 Tworzenie aplikacji w Python (PyQt6) – Przewodnik dla każdego

Wyobraź sobie, że tworzenie aplikacji to budowanie z klocków LEGO. **Qt Designer** to Twój zestaw klocków, a **Python** to instrukcja, która mówi, co te klocki mają robić.

---

## Podstawowe układy

### 1. Qt Designer – Projektujemy wygląd (To co widzisz)

Gdy otwierasz program (fman build of Qt Designer), wybierz na starcie **Main Window**. To jest Twoje puste płótno.

#### A. Gdzie co jest?

* **Lewa strona (Widget Box):** Tu są Twoje narzędzia (przyciski, pola tekstowe, napisy). Przeciągasz je na okno.
* **Prawa góra (Object Inspector):** Tu widzisz listę wszystkich klocków, które już są na oknie.
* **Prawa dół (Property Editor):** Tu zmieniasz kolory, nazwy, czcionki i wielkości.

#### B. Najważniejsze "Klocki" (Widgety):

1. **Label:** Zwykły napis (np. 
"Podaj imię:").
2. **Push Button:** Przycisk, który można kliknąć.
3. **Line Edit:** Jednolinijkowe pole, w którym użytkownik coś wpisuje.
4. **Check Box:** Pole "ptaszek" do zaznaczania opcji.

---

### 2. Layouty – Porządek w aplikacji

To jest moment, w którym większość osób się gubi. Jeśli po prostu rozrzucisz przyciski na oknie, po jego powiększeniu zostaną one w jednym miejscu, a reszta okna będzie pusta.

#### Jak zapanować nad chaosem?

1. **Metoda "Na Brudno":** Wrzuć wszystkie elementy (np. 3 przyciski) byle jak na okno.
2. **Grupowanie:** Zaznacz je wszystkie myszką. Kliknij **prawym przyciskiem** na jeden z nich -> **Lay Out** -> **Lay Out Horizontally** (obok siebie) lub **Vertically** (jeden pod drugim).
3. **Mocowanie do okna (KLUCZOWE):** Teraz Twój layout to jedna "paczka". Aby ta paczka wypełniała całe okno przy rozciąganiu:
    * Kliknij prawym przyciskiem na **puste, białe tło okna** (tam gdzie nie ma przycisków).
    * Wybierz **Lay Out** -> **Lay Out Vertically**.
    * **Gotowe!** Teraz wszystko "pływa" razem z oknem.

> **Pro Tip:** Jeśli chcesz, żeby przycisk był mniejszy i nie rozciągał się na całą stronę, użyj **Spacera** (niebieska sprężynka w przyborniku). Wrzuć go obok przycisku – on "wypchnie" przycisk w drugą stronę.

---

### 3. Nazewnictwo – Most do Pythona

Python nie wie, który przycisk jest który. Musisz mu to powiedzieć.

1. Kliknij na przycisk w Designerze.
2. W **Property Editor** (prawa dół) znajdź pole `objectName`.
3. Zmień `pushButton` na coś logicznego, np. `btn_oblicz`.
4. **Zasada:** Używaj przedrostków: `btn_` dla przycisków, `lbl_` dla napisów, `input_` dla pól tekstowych.

---

### 4. Kod Python – Ożywiamy aplikację

Zapisz swój projekt jako `widok.ui` w folderze z Twoim skryptem `.py`. Poniżej masz "szkielet", który kopiujesz do każdego zadania. Przeczytaj komentarze w kodzie – one tłumaczą, co się dzieje.

```python
import sys
from PyQt6 import QtWidgets, uic # Importujemy potrzebne narzędzia

class MojaApka(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. Łączymy kod z wyglądem z Designera
        uic.loadUi("widok.ui", self) 
        
        # 2. Mówimy przyciskowi, co ma robić po kliknięciu
        # self.NAZWA_Z_DESIGNERA.clicked.connect(self.moje_dzialanie)
        self.btn_oblicz.clicked.connect(self.oblicz)

    def oblicz(self):
        # 3. Pobieramy to, co użytkownik wpisał
        wpisany_tekst = self.input_dane.text()
        
        # 4. Robimy coś z tymi danymi (logika)
        try:
            liczba = int(wpisany_tekst)
            wynik = liczba * 2
            # 5. Wyświetlamy wynik w Labelce
            self.lbl_wynik.setText(f"Podwojona liczba to: {wynik}")
        except:
            # Okno z informacją o błędzie
            QtWidgets.QMessageBox.warning(self, "Błąd", "Wpisz poprawną liczbę!")

# --- Standardowe uruchomienie aplikacji (zawsze takie samo) ---
app = QtWidgets.QApplication(sys.argv)
okno = MojaApka()
okno.show()
app.exec()
```

---

### 5. Przykładowe zadanie: "Sprawdzacz Pełnoletności"

Spróbuj rozwiązać to zadanie, idąc tymi krokami:

1.  **Designer:**
    * Dodaj `Label` z napisem "Podaj wiek:".
    * Dodaj `Line Edit` i nazwij go (`objectName`) `input_wiek`.
    * Dodaj `Push Button` i nazwij go `btn_sprawdz`.
    * Dodaj kolejną `Label` na wynik i nazwij ją `lbl_status`.
    * Ustaw Layouty (np. wszystko w pionie i przypnij do okna).
    * **Zapisz jako `wiek.ui`.**

2. **Kod Python:**
    * Skopiuj szkielet powyżej.
    * W funkcji `oblicz` zmień logikę:

        ```python
        wiek = int(self.input_wiek.text())
        if wiek >= 18:
            self.lbl_status.setText("Jesteś dorosły")
        else:
            self.lbl_status.setText("Jesteś niepełnoletni")
        ```

---

### 6. Co jeśli nie działa? (Najczęstsze błędy)

* **Błąd: `FileNotFoundError`** – Plik `.ui` nie nazywa się tak samo jak w kodzie lub jest w innym folderze.
* **Błąd: `AttributeError: ... object has no attribute 'btn_cos'`** – Pomyliłeś nazwę w `objectName` w Designerze albo nie zapisałeś pliku (Ctrl+S).
* **Aplikacja się wyłącza bez błędu** – Zazwyczaj błąd jest w logice (np. próbujesz zamienić słowo "ABC" na liczbę). Używaj `try...except`.

Oto kompletna, skonsolidowana notatka dla Twoich uczniów. Jest przygotowana w formacie Markdown, gotowa do wrzucenia na GitHub, z zachowaniem Twoich wytycznych dotyczących struktury nagłówków.

---

## Interakcja z użytkownikiem i obsługa danych (Zapis/Odczyt)

### 1. Pobieranie wyborów użytkownika (Widgety wyboru)

W aplikacjach desktopowych rzadko tylko wpisujemy tekst. Częściej wybieramy gotowe opcje. Na egzaminie INF.04 musisz znać te trzy narzędzia:

* **QRadioButton (Przycisk opcji):** Używamy go, gdy użytkownik ma wybrać **tylko jedną** rzecz z listy (np. płeć: Kobieta lub Mężczyzna).
  * *W kodzie:* `self.radio_button.isChecked()` – zwraca `True`, jeśli zaznaczone.
* **QCheckBox (Pole wyboru):** Używamy go, gdy można zaznaczyć **wiele** opcji na raz (np. dodatki do pizzy).
  * *W kodzie:* `self.check_box.isChecked()` – zwraca `True`, jeśli "ptaszek" jest postawiony.
* **QComboBox (Lista rozwijana):** Pozwala oszczędzić miejsce. Użytkownik klika i wybiera jedną pozycję z listy.
  * *W kodzie:* `self.combo_box.currentText()` – zwraca tekst wybranej opcji.

> **Ważne (Layout):** Jeśli używasz `RadioButton`, zawsze grupuj je wewnątrz ramki **QGroupBox**. Dzięki temu system wie, że te konkretne kropki należą do jednego pytania.

### 2. Zapisywanie informacji do pliku tekstowego

Aby dane przetrwały zamknięcie aplikacji, zapisujemy je do pliku `.txt`. W Pythonie używamy do tego bezpiecznej konstrukcji `with open`.

* **Tryb 'a' (Append):** Dopisuje nową treść na końcu pliku (nie kasuje tego, co już tam było).
* **Tryb 'w' (Write):** Kasuje wszystko i zapisuje plik od nowa.

**Przykład zapisu:**

```python
with open("baza.txt", "a", encoding="utf-8") as plik:
    plik.write("Nowy wpis użytkownika\n") # \n oznacza nową linię
```

### 3. Odczyt i wyświetlanie bazy danych w aplikacji

Aby użytkownik widział, co zostało zapisane, używamy widgetu **QPlainTextEdit** (duże pole tekstowe).

1. W Designerze nazwij to pole np. `txt_podglad`.
2. Zaznacz mu opcję `readOnly`, aby użytkownik nie mógł tam nic wpisać ręcznie.
3. Użyj trybu **'r' (Read)**, aby pobrać dane z pliku:

```python
try:
    with open("baza.txt", "r", encoding="utf-8") as plik:
        wszystko = plik.read() # Czytamy cały plik
        self.txt_podglad.setPlainText(wszystko) # Wrzucamy do okienka
except FileNotFoundError:
    self.txt_podglad.setPlainText("Brak zapisanych danych.")
```

### 4. Kompletny wzorzec kodu (Szkielet egzaminacyjny)

Ten kod łączy wszystko: pobiera dane z pól, zapisuje je po kliknięciu i od razu odświeża widok na ekranie.

```python
import sys
from PyQt6 import QtWidgets, uic

class AplikacjaDanych(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("projekt.ui", self) # Załaduj swój plik z Designera
        
        # Podpinamy przyciski
        self.btn_zapisz.clicked.connect(self.akcja_zapisz)
        self.btn_odswiez.clicked.connect(self.wyswietl_liste)

    def akcja_zapisz(self):
        # 1. Pobieranie danych
        imie = self.input_imie.text()
        miasto = self.combo_miasto.currentText()
        
        # 2. Walidacja (czy pole nie jest puste)
        if imie == "":
            QtWidgets.QMessageBox.warning(self, "Błąd", "Podaj imię!")
            return

        # 3. Zapis do pliku
        with open("dane.txt", "a", encoding="utf-8") as f:
            f.write(f"Imię: {imie}, Miasto: {miasto}\n")
            
        QtWidgets.QMessageBox.information(self, "Sukces", "Zapisano pomyślnie!")
        self.input_imie.clear()
        self.wyswietl_liste() # Od razu pokazujemy zmiany

    def wyswietl_liste(self):
        try:
            with open("dane.txt", "r", encoding="utf-8") as f:
                self.txt_podglad.setPlainText(f.read())
        except FileNotFoundError:
            pass

app = QtWidgets.QApplication(sys.argv)
win = AplikacjaDanych()
win.show()
app.exec()
```
