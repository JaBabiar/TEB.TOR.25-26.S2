# Zadanie Praktyczne: Kalkulator Statystyk Gracza (PyQt6 + Qt Designer)

## Opis zadania

Twoim zadaniem jest zaprojektowanie i oprogramowanie okienkowej aplikacji typu "Kalkulator Statystyk", która wylicza współczynnik K/D (Kills/Deaths) dla graczy turniejowych. Aplikacja musi składać się z dwóch plików: widoku stworzonego w programie Qt Designer (`.ui`) oraz logiki napisanej w języku Python (`.py`).

---

## Cześć 1: Projektowanie Interfejsu (Qt Designer)

Utwórz plik `kalkulator.ui` (oparty na `QMainWindow` lub `QWidget`). Interfejs musi być zorganizowany i estetyczny. Wykorzystaj odpowiednie Layouty (np. `QVBoxLayout` i `QHBoxLayout`), aby formularz się skalował.

W oknie muszą znaleźć się następujące elementy:

1. **Pole tekstowe (`QLineEdit`)** – do wpisania pseudonimu (nicku) gracza.
2. **Lista rozwijana (`QComboBox`)** – do wyboru głównej gry (dodaj w Designerze minimum trzy opcje, np.: *Counter-Strike 2*, *Deadlock*, *Minecraft*).
3. **Dwa pola liczbowe (`QSpinBox`)** – jedno dla liczby likwidacji (Kills), drugie dla liczby zgonów (Deaths). Ustaw ich maksymalną wartość na 9999.
4. **Pole wyboru (`QCheckBox`)** – z tekstem "Konto Prime / VIP".
5. **Przycisk (`QPushButton`)** – z tekstem "Generuj Raport".
6. **Etykieta tekstowa (`QLabel`)** – do wyświetlenia ostatecznego wyniku. Ustaw jej domyślny tekst na: *"Czekam na dane..."*.

*Pamiętaj, aby w Qt Designerze nadać kontrolkom sensowne nazwy (np. `input_nick`, `box_gra`, `spin_kills`, `btn_generuj`), aby łatwo było się do nich odwołać w Pythonie!*

---

## Część 2: Logika Aplikacji (Python)

Utwórz plik `main.py` i zrealizuj poniższe wytyczne:

1. **Inicjalizacja:** Załaduj wygenerowany plik `kalkulator.ui` za pomocą metody `uic.loadUi()`.
2. **Sygnał i Slot:** Podepnij zdarzenie kliknięcia przycisku do nowej metody np. `oblicz_statystyki`.
3. **Pobieranie danych:** Wewnątrz metody pobierz:
* Tekst z `QLineEdit` (użyj `.text()`).
* Aktualnie wybraną grę z `QComboBox` (użyj `.currentText()`).
* Wartości liczbowe ze `QSpinBox` (użyj `.value()`).
* Stan zaznaczenia `QCheckBox` (użyj `.isChecked()` - zwraca `True` lub `False`).


4. **Logika i Matematyka:**
* Oblicz współczynnik K/D (Kills podzielone przez Deaths).
* **Ważne:** Zabezpiecz program przed błędem dzielenia przez zero! Jeśli użytkownik zostawi liczbę zgonów na `0`, współczynnik K/D powinien wynosić po prostu tyle, co liczba zabójstw (lub wypisz błąd używając `QMessageBox`).
* Jeśli `QCheckBox` jest zaznaczony, dodaj do raportu informację o statusie VIP.


5. **Wyświetlanie Wyniku:** Użyj f-stringów, aby sformatować wynik i wyświetlić go w `QLabel`. Współczynnik K/D powinien być zaokrąglony do dwóch miejsc po przecinku (np. `1.25`).

**Przykładowy format wyniku:**

> "Gracz: Ninja | Gra: Counter-Strike 2
> Status VIP: TAK
> Współczynnik K/D: 1.45"

---

## Kryteria Oceniania (Checklista)

* [ ] Plik `.ui` został poprawnie załadowany przez `uic.loadUi()`.
* [ ] Zastosowano Layouty w Qt Designerze (elementy nie są ułożone absolutnie).
* [ ] Poprawnie pobrano dane z różnych typów kontrolek (`.text()`, `.value()`, `.currentText()`, `.isChecked()`).
* [ ] Zabezpieczono program przed crashem spowodowanym dzieleniem przez zero (`ZeroDivisionError`).
* [ ] Współczynnik K/D wylicza się poprawnie matematycznie i jest zaokrąglony do maksymalnie 2 miejsc po przecinku.
* [ ] Zastosowano f-stringi do sformatowania końcowego raportu.
* [ ] Do obsługi zdarzenia przycisku poprawnie użyto `clicked.connect()`.

Świetny pomysł. Aplikacje okienkowe domyślnie korzystają z szarego motywu systemu, co dla aplikacji "gamingowej" jest trochę nudne. Wprowadzenie stylizowania to też doskonały pretekst, żeby przypomnieć im wiedzę z kwalifikacji INF.03, ponieważ w PyQt6 używa się **QSS (Qt Style Sheets)**, które działają niemal w 100% tak samo jak CSS na stronach internetowych.

Możesz dokleić poniższą sekcję na sam koniec pliku z zadaniem.

---

Pewnie, zmuszenie ich do samodzielnego przypomnienia sobie składni to świetny manewr pedagogiczny – idealnie połączy to, co pamiętają z INF.03, z nowym środowiskiem.

Oto wersja instrukcji "Zadania Premium", która tłumaczy proces i stawia przed nimi konkretne cele wizualne, ale nie podaje gotowego kodu do skopiowania na tacy.

---

## Część 3 (Zadanie Premium): Stylowanie Interfejsu (QSS)

Prawdziwa aplikacja e-sportowa nie może być szara! Biblioteka PyQt obsługuje mechanizm **Qt Style Sheets (QSS)**, który działa niemal identycznie jak kaskadowe arkusze stylów (CSS), które znasz z tworzenia stron internetowych (kwalifikacja INF.03).

Twoim zadaniem jest zmiana wyglądu aplikacji na nowoczesny, gamingowy "Dark Mode" bezpośrednio w programie Qt Designer.

**Jak narzędziowo podejść do zadania:**

1. W Qt Designerze w oknie "Object Inspector" (po prawej stronie) kliknij **prawym przyciskiem myszy** na najwyższy element w hierarchii (np. `MainWindow` lub `centralwidget`).
2. Z menu kontekstowego wybierz opcję **"Change styleSheet..."**. Otworzy się edytor tekstowy, w którym będziesz pisać swoje style. Efekty zobaczysz od razu po kliknięciu "Apply" lub "OK".
3. Składnia jest taka sama jak w CSS: najpierw podajesz nazwę klasy widżetu (np. `QPushButton`, `QLineEdit`, `QLabel`), a następnie w nawiasach klamrowych `{ }` wypisujesz właściwości.

**Twoje cele do samodzielnego zakodowania:**

* **Baza:** Zmień kolor tła głównego okna na ciemnoszary lub granatowy. Zastanów się, jakiej właściwości używasz w CSS do określania koloru tła.
* **Czytelność:** Ponieważ tło jest teraz ciemne, standardowe czarne napisy znikną. Zmień kolor czcionki dla wszystkich etykiet (`QLabel`) oraz pola wyboru (`QCheckBox`) na jasny (np. biały lub pastelowy). Możesz też nieznacznie powiększyć rozmiar tekstu.
* **Nowoczesny Przycisk:** Skup się na przycisku (`QPushButton`). Nadaj mu wyrazisty, gamingowy kolor tła (np. jaskrawy zielony, niebieski lub fioletowy). Pogrub czcionkę. Dodaj wewnętrzne marginesy (aby tekst "oddychał" i nie przyklejał się do krawędzi) oraz lekko zaokrąglij jego rogi.
* **Interaktywność (Hover):** Zadbaj o doświadczenie użytkownika. Zastosuj odpowiednią pseudoklasę, aby po najechaniu kursorem na przycisk, zmieniał on delikatnie swój odcień na jaśniejszy.
* **Pola danych:** Zmodyfikuj pola wejściowe (`QLineEdit`, `QSpinBox`, `QComboBox`). Nadaj im tło, które odetnie je od reszty okna (np. nieco jaśniejszy odcień szarości niż tło główne), zmień kolor wpisywanego tekstu na jasny i dodaj cienkie, subtelne obramowanie.

*Wskazówka: Jeśli nie pamiętasz dokładnych nazw właściwości, przypomnij sobie, jak w HTML/CSS robiłeś zaokrąglenia, marginesy wewnętrzne czy zmieniałeś kolor tekstu. W QSS te komendy nazywają się i działają dokładnie tak samo!*