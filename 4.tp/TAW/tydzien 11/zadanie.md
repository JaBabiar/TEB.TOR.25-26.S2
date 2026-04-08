# Zadanie Praktyczne

## 🎯 Cel zadania

Stworzenie prostego notatnika, który zapisuje tekst w locie, pozwala na jego szybkie wyczyszczenie i odpowiednio zarządza stanem fokusu w przeglądarce.

## 📝 Wymagania i Instrukcje

Twój komponent powinien nazywać się `QuickNote`. Zaimplementuj w nim następujące elementy:

### 1. Zarządzanie Stanem (`useState`)

* Stwórz stan `noteText` przechowujący aktualnie wpisywany przez użytkownika tekst.
* Jako początkową wartość ustaw pusty ciąg znaków `""`.

### 2. Wykorzystanie Referencji (`useRef`)

* Utwórz referencję (np. `textareaRef`) i przypisz ją do elementu `<textarea>`. 
* Referencja posłuży do bezpośredniego manipulowania polem tekstowym (wymuszania tzw. fokusu), bez wywoływania ponownego renderowania całego komponentu.

### 3. Efekty Uboczne (`useEffect`)

* **Efekt 1 (Focus na start):** Napisz efekt, który uruchomi się **tylko raz** przy zamontowaniu komponentu. Użyj utworzonej referencji, aby automatycznie ustawić kursor wewnątrz pola tekstowego, tak by użytkownik mógł od razu zacząć pisać po wejściu na stronę.
* **Efekt 2 (Autozapis):** Napisz drugi efekt, który reaguje na **każdą zmianę** stanu `noteText`. Kiedy tekst się zmienia, efekt powinien zapisywać go do `localStorage` pod kluczem (np. `"saved_note"`). Zmiana tytułu karty w przeglądarce na "Zapisano zmiany!" na ułamek sekundy to fajny bonus.

### 4. Interfejs (UI) i Akcje

Zbuduj prosty interfejs składający się z:

1. **Pola tekstowego (`<textarea>`):** Powiązanego ze stanem `noteText`. Zadbaj tutaj o dobrą praktykę i zgodność z wytycznymi dostępności (WCAG) – pole musi posiadać wyraźny i połączony z nim tag `<label>` (używając atrybutu `htmlFor`), aby czytniki ekranu wiedziały, do czego służy to pole.
2. **Przycisku "Wyczyść":** Kliknięcie tego przycisku musi wykonać dwie akcje jednocześnie:
   * Wyzerować stan `noteText`.
   * Użyć referencji `textareaRef`, aby natychmiast przywrócić kursor do wyczyszczonego pola, pozwalając na płynne rozpoczęcie nowej notatki.
