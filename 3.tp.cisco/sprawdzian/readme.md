# Sprawdzian
## Projekt interfejsu i stylowanie (Qt Designer) - 15 pkt

Twoim zadaniem jest stworzenie pliku `ticket_generator.ui` za pomocą programu Qt Designer.

### 1. Wymagane elementy interfejsu (Widżety)

W oknie głównym muszą znaleźć się następujące elementy:

* **Nagłówek:** `QLabel` z tekstem "Nowe Zgłoszenie Serwisowe".
* **Pole na imię i nazwisko:** `QLineEdit` (z ustawionym *placeholder text*: "Wpisz imię i nazwisko").
* **Kategoria problemu:** `QComboBox` z trzema opcjami (np. "Sprzęt", "Oprogramowanie", "Sieć").
* **Opis problemu:** `QTextEdit` do wprowadzenia dłuższego opisu usterki.
* **Przycisk generowania:** `QPushButton` z tekstem "Generuj Zgłoszenie".
* **Pole na wynik:** `QTextBrowser` lub `QLabel` (tylko do odczytu), w którym wyświetli się podsumowanie.

### 2. Układ (Layouts)

* Aplikacja musi być responsywna. Zastosuj odpowiednio `QVBoxLayout` (dla ułożenia elementów jeden pod drugim) oraz opcjonalnie `QHBoxLayout` (np. jeśli chcesz umieścić etykiety obok pól tekstowych).

### 3. Stylowanie (QSS - Qt Style Sheets)

Aplikacja musi wyglądać nowocześnie i być czytelna dla każdego użytkownika. Dodaj arkusz stylów, który spełnia poniższe wymagania:

* Zmień kolor tła głównego okna (np. na jasnoszary lub ciemny motyw).
* **Wymóg dostępności (WCAG):** Zadbaj o wysoki kontrast pomiędzy tekstem a tłem we wszystkich elementach, szczególnie na przycisku głównym. Użyj czytelnej czcionki bezszeryfowej (np. Arial, Roboto) o odpowiedniej wielkości (min. 12px dla zwykłego tekstu, min. 16px dla nagłówka).
* Przycisk "Generuj Zgłoszenie" musi mieć inny kolor tła niż reszta interfejsu oraz posiadać zaokrąglone rogi (`border-radius`).

---

## Logika aplikacji (Python) - 15 pkt

Utwórz plik `main.py`. Skrypt musi ładować przygotowany interfejs graficzny i realizować opisaną niżej funkcjonalność.

### 1. Inicjalizacja i wczytanie UI

* Wczytaj plik `ticket_generator.ui` za pomocą modułu `uic` (lub przekonwertuj go na plik `.py` i zaimportuj).
* Uruchom główną pętlę zdarzeń aplikacji (`QApplication`).

### 2. Sygnały i Sloty

* Podłącz zdarzenie kliknięcia (`clicked`) przycisku "Generuj Zgłoszenie" do własnej metody/funkcji o nazwie np. `generate_ticket()`.

### 3. Logika i Walidacja

Wewnątrz funkcji generującej:

1. **Pobieranie danych:** Pobierz tekst z `QLineEdit` (imię i nazwisko), wybraną wartość z `QComboBox` (kategoria) oraz tekst z `QTextEdit` (opis).
2. **Walidacja:** Sprawdź, czy pole imię i nazwisko oraz opis nie są puste.
* *Jeśli są puste:* Wyświetl komunikat o błędzie (może to być `QMessageBox` lub czerwony tekst w oknie głównym).


3. **Generowanie wyniku:** Jeśli dane są poprawne, sformatuj je do czytelnego stringa (np. dodając stały prefix "TICKET-2026-X").
4. **Wyświetlanie:** Wypisz sformatowane zgłoszenie w dolnym polu wynikowym (`QTextBrowser`).
5. **Czyszczenie:** Po udanym wygenerowaniu zgłoszenia, wyczyść wpisane przez użytkownika dane w polach formularza.

---

## Kryteria oceniania (Maksymalnie 30 pkt)

**Interfejs (15 pkt):**

* [ ] Poprawne dodanie wszystkich widżetów (5 pkt)
* [ ] Zastosowanie layoutów - aplikacja poprawnie się skaluje (4 pkt)
* [ ] Stylowanie QSS zgodnie z wymogami (3 pkt)
* [ ] Zgodność stylów z wytycznymi wysokiego kontrastu / dostępności (3 pkt)

**Logika (15 pkt):**

* [ ] Prawidłowe załadowanie okna i uruchomienie aplikacji (3 pkt)
* [ ] Działające powiązanie przycisku z funkcją (sygnały i sloty) (3 pkt)
* [ ] Pobieranie danych z widżetów wejściowych (3 pkt)
* [ ] Implementacja walidacji i komunikatów o błędach (3 pkt)
* [ ] Formatowanie i wyświetlenie wyniku oraz czyszczenie pól formularza (3 pkt)

**Powodzenia!**