# Zadanie Praktyczne: Prosta Aplikacja Desktopowa w PyQt6 (INF.04)

## Opis zadania
Zostałeś poproszony o przygotowanie prostej aplikacji "Generator Powitań", która ma sprawdzić Twoje podstawowe umiejętności tworzenia interfejsów graficznych z użyciem frameworka PyQt6.

Napisz skrypt w języku Python, który zrealizuje poniższe wytyczne.

---

## Wytyczne do realizacji

### 1. Inicjalizacja Aplikacji i Okna
* Zaimportuj niezbędne moduły z `PyQt6.QtWidgets` oraz `sys`.
* Utwórz obiekt głównej aplikacji (`QApplication`).
* Utwórz klasę własnego okna dziedziczącą po `QWidget` (lub `QMainWindow`).
* W konstruktorze okna ustaw jego tytuł na: "Powitanie".

### 2. Budowa Interfejsu (Widżety)
W głównym oknie aplikacji umieść trzy elementy:
1.  **Pole tekstowe (`QLineEdit`)** – posłuży użytkownikowi do wpisania swojego imienia.
2.  **Przycisk (`QPushButton`)** – z widocznym napisem "Przywitaj się".
3.  **Etykieta tekstowa (`QLabel`)** – początkowo zawierająca tekst "Tu pojawi się powitanie...". Będzie służyć do wyświetlenia wyniku.

### 3. Układ Elementów (Layout)
* Zamiast pozycjonowania ręcznego, użyj menedżera układu pionowego (**`QVBoxLayout`**).
* Dodaj utworzone wcześniej pole tekstowe, przycisk i etykietę do tego układu, tak aby wyświetlały się równo jedno pod drugim.
* Przypisz utworzony układ do głównego okna (metoda `setLayout()`).

### 4. Logika i Zdarzenia (Sygnały i Sloty)
* Napisz metodę/funkcję (tzw. slot), np. o nazwie `generuj_powitanie`.
* Wewnątrz tej funkcji odczytaj tekst z pola wprowadzania, korzystając z metody **`.text()`**.
* Następnie zmień tekst w etykiecie wynikowej za pomocą metody **`.setText()`** tak, aby wyświetlała format: *"Witaj, [Wpisane_Imię]!"*.
* Połącz akcję kliknięcia przycisku (sygnał **`.clicked`**) z nową metodą używając **`.connect()`**.

### 5. Uruchomienie aplikacji
* Poza definicją klasy wyświetl okno za pomocą metody **`.show()`**.
* Uruchom główną pętlę zdarzeń aplikacji za pomocą **`.exec()`** (w starszych wersjach `.exec_()`).

---

## Kryteria Oceniania (Checklista)
- [ ] Utworzono obiekt `QApplication(sys.argv)`.
- [ ] Zbudowano interfejs w oparciu o `QWidget` lub `QMainWindow`.
- [ ] Dodano pole jednowierszowe używając klasy `QLineEdit`.
- [ ] Użyto `QVBoxLayout` do uporządkowania elementów w pionie.
- [ ] Poprawnie połączono sygnał przycisku ze slotem: `przycisk.clicked.connect(funkcja)`.
- [ ] Użyto metody `.text()`, aby pobrać dane z QLineEdit.
- [ ] Użyto metody `.setText()`, aby zmienić zawartość QLabel.
- [ ] Na końcu pliku uruchomiono pętlę `app.exec()`.

---

## Miejsce na Twój kod:

```python
# Tutaj wklej swoje rozwiązanie