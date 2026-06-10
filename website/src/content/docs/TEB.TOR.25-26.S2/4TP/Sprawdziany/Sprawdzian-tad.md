---
title: "Zadanie Praktyczne: Aplikacja Desktopowa w PyQt6 + Qt Designer (INF.04)"
description: "Zadanie praktyczne sprawdzające umiejętności projektowania interfejsów za pomocą narzędzia Qt Designer oraz łączenia ich z logiką w języku Python (PyQt6)."
pubDate: 2026-06-10
category: "Sprawdziany"
tags: ["python", "pyqt6", "qt-designer", "inf-04", "desktop"]
---

# Zadanie Praktyczne: Prosta Aplikacja Desktopowa z Qt Designer (INF.04)

## Opis zadania
Zostałeś poproszony o przygotowanie prostej aplikacji "Generator Powitań", która ma sprawdzić Twoje umiejętności tworzenia interfejsów graficznych z wykorzystaniem narzędzia **Qt Designer** oraz podpinania do nich logiki w języku Python (framework PyQt6).

Zadanie składa się z dwóch etapów: zaprojektowania widoku oraz napisania skryptu.

---

## Wytyczne do realizacji

### Część 1: Projektowanie Interfejsu (Qt Designer)
1. **Inicjalizacja projektu:** Otwórz program Qt Designer i utwórz nowy formularz oparty na szablonie **Widget** (lub **Main Window**). Ustaw tytuł okna (właściwość `windowTitle`) na: "Powitanie".
2. **Dodawanie widżetów:** Przeciągnij z przybornika i upuść na formularz następujące elementy:
   * **Pole tekstowe (`QLineEdit`)** – nadaj mu sensowną nazwę obiektu (właściwość `objectName`), np. `inputName`. Będzie służyć do wpisania imienia.
   * **Przycisk (`QPushButton`)** – zmień jego tekst na "Przywitaj się" i nadaj `objectName` np. `btnGreet`.
   * **Etykieta tekstowa (`QLabel`)** – ustaw jej początkowy tekst na "Tu pojawi się powitanie..." i nadaj `objectName` np. `labelResult`.
3. **Układ Elementów (Layout):** Zaznacz główne tło okna (kliknij w puste miejsce) i zastosuj na nim **pionowy menedżer układu** (Vertical Layout - skrót `Ctrl+1` lub z paska narzędzi). Elementy powinny ułożyć się równo jeden pod drugim i responsywnie reagować na zmianę rozmiaru okna.
4. **Dostępność i nawigacja klawiaturą:** Przejdź w tryb edycji kolejności tabulacji (*Edit Tab Order*) na górnym pasku. Upewnij się, że nawigacja klawiszem `Tab` przebiega logicznie – najpierw pole tekstowe, a następnie przycisk.
5. Zapisz projekt jako plik o nazwie **`interfejs.ui`**.

### Część 2: Konwersja i Kodowanie (Python)
1. **Konwersja pliku:** Wykorzystaj narzędzie `pyuic6` w terminalu, aby wygenerować kod Pythona z pliku `.ui`. Przykładowe polecenie:
   `pyuic6 -x interfejs.ui -o ui_interfejs.py`
2. **Plik główny aplikacji:** Utwórz plik `main.py`. Zaimportuj w nim niezbędne moduły z `PyQt6.QtWidgets` oraz wygenerowaną klasę interfejsu z pliku `ui_interfejs.py`.
3. **Logika i Sygnały:** * Utwórz główną klasę aplikacji dziedziczącą po `QWidget` (lub `QMainWindow`), w której zainicjujesz wygenerowany interfejs (metoda `setupUi`).
   * Napisz metodę `generuj_powitanie(self)`. Wewnątrz niej odczytaj tekst z pola `QLineEdit` (metoda `.text()`), a następnie ustaw nowy tekst na etykiecie `QLabel` (metoda `.setText()`) w formacie: *"Witaj, [Wpisane_Imię]!"*.
   * W konstruktorze klasy głównej połącz akcję kliknięcia przycisku (sygnał `.clicked`) ze stworzoną metodą za pomocą `.connect()`.
4. **Uruchomienie:** Na końcu pliku `main.py` utwórz instancję `QApplication`, wyświetl okno (`.show()`) i uruchom pętlę zdarzeń (`.exec()`).

---

## Kryteria Oceniania (Checklista)
- [ ] Poprawnie wygenerowano plik `interfejs.ui` z poziomu narzędzia Qt Designer.
- [ ] Zastosowano Layout pionowy (Vertical Layout) do ułożenia widżetów.
- [ ] Zmieniono domyślne nazwy obiektów (`objectName`) na własne, znaczące (np. `inputName`, `btnGreet`).
- [ ] Zadbano o logiczną kolejność tabulacji (Tab Order) elementów interaktywnych.
- [ ] Skonwertowano plik `.ui` do pliku `.py` za pomocą polecenia `pyuic6`.
- [ ] W osobnym pliku (np. `main.py`) poprawnie zaimportowano wygenerowany interfejs.
- [ ] Poprawnie połączono sygnał przycisku ze slotem: `self.ui.btnGreet.clicked.connect(self.generuj_powitanie)`.
- [ ] Użyto metody `.text()`, aby pobrać dane i `.setText()`, aby zmienić zawartość QLabel.
- [ ] Aplikacja uruchamia się bez błędów w konsoli.