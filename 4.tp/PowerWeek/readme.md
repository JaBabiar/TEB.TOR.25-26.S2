To jest rozbudowany podręcznik "krok po kroku", napisany prostym językiem dla Twoich uczniów. Możesz to wkleić do pliku `README.md` na GitHubie lub do dokumentu w chmurze. 

---

# 🚀 Tworzenie aplikacji w Python (PyQt6) – Przewodnik dla każdego
### Cel: Zaliczenie egzaminu INF.04 (nawet jeśli nie planujesz zostać programistą)

Wyobraź sobie, że tworzenie aplikacji to budowanie z klocków LEGO. **Qt Designer** to Twój zestaw klocków, a **Python** to instrukcja, która mówi, co te klocki mają robić.

---

## 1. Qt Designer – Projektujemy wygląd (To co widzisz)

Gdy otwierasz program (fman build of Qt Designer), wybierz na starcie **Main Window**. To jest Twoje puste płótno.

### A. Gdzie co jest?
* **Lewa strona (Widget Box):** Tu są Twoje narzędzia (przyciski, pola tekstowe, napisy). Przeciągasz je na okno.
* **Prawa góra (Object Inspector):** Tu widzisz listę wszystkich klocków, które już są na oknie.
* **Prawa dół (Property Editor):** Tu zmieniasz kolory, nazwy, czcionki i wielkości.

### B. Najważniejsze "Klocki" (Widgety):
1.  **Label:** Zwykły napis (np. "Podaj imię:").
2.  **Push Button:** Przycisk, który można kliknąć.
3.  **Line Edit:** Jednolinijkowe pole, w którym użytkownik coś wpisuje.
4.  **Check Box:** Pole "ptaszek" do zaznaczania opcji.



---

## 2. Layouty – Porządek w aplikacji

To jest moment, w którym większość osób się gubi. Jeśli po prostu rozrzucisz przyciski na oknie, po jego powiększeniu zostaną one w jednym miejscu, a reszta okna będzie pusta.

### Jak zapanować nad chaosem?
1.  **Metoda "Na Brudno":** Wrzuć wszystkie elementy (np. 3 przyciski) byle jak na okno.
2.  **Grupowanie:** Zaznacz je wszystkie myszką. Kliknij **prawym przyciskiem** na jeden z nich -> **Lay Out** -> **Lay Out Horizontally** (obok siebie) lub **Vertically** (jeden pod drugim).
3.  **Mocowanie do okna (KLUCZOWE):** Teraz Twój layout to jedna "paczka". Aby ta paczka wypełniała całe okno przy rozciąganiu:
    * Kliknij prawym przyciskiem na **puste, białe tło okna** (tam gdzie nie ma przycisków).
    * Wybierz **Lay Out** -> **Lay Out Vertically**.
    * **Gotowe!** Teraz wszystko "pływa" razem z oknem.

> **Pro Tip:** Jeśli chcesz, żeby przycisk był mniejszy i nie rozciągał się na całą stronę, użyj **Spacera** (niebieska sprężynka w przyborniku). Wrzuć go obok przycisku – on "wypchnie" przycisk w drugą stronę.



---

## 3. Nazewnictwo – Most do Pythona

Python nie wie, który przycisk jest który. Musisz mu to powiedzieć.
1.  Kliknij na przycisk w Designerze.
2.  W **Property Editor** (prawa dół) znajdź pole `objectName`.
3.  Zmień `pushButton` na coś logicznego, np. `btn_oblicz`.
4.  **Zasada:** Używaj przedrostków: `btn_` dla przycisków, `lbl_` dla napisów, `input_` dla pól tekstowych.

---

## 4. Kod Python – Ożywiamy aplikację

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

## 5. Przykładowe zadanie: "Sprawdzacz Pełnoletności"

Spróbuj rozwiązać to zadanie, idąc tymi krokami:

1.  **Designer:**
    * Dodaj `Label` z napisem "Podaj wiek:".
    * Dodaj `Line Edit` i nazwij go (`objectName`) `input_wiek`.
    * Dodaj `Push Button` i nazwij go `btn_sprawdz`.
    * Dodaj kolejną `Label` na wynik i nazwij ją `lbl_status`.
    * Ustaw Layouty (np. wszystko w pionie i przypnij do okna).
    * **Zapisz jako `wiek.ui`.**

2.  **Kod Python:**
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

## 6. Co jeśli nie działa? (Najczęstsze błędy)

* **Błąd: `FileNotFoundError`** – Plik `.ui` nie nazywa się tak samo jak w kodzie lub jest w innym folderze.
* **Błąd: `AttributeError: ... object has no attribute 'btn_cos'`** – Pomyliłeś nazwę w `objectName` w Designerze albo nie zapisałeś pliku (Ctrl+S).
* **Aplikacja się wyłącza bez błędu** – Zazwyczaj błąd jest w logice (np. próbujesz zamienić słowo "ABC" na liczbę). Używaj `try...except`.

