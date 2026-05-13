# Sigiemka karkówka

## Zadanie 1 - Statystyki gracza (3 pkt)

### Stwórz komponent PlayerKills, który:

* wyświetla aktualną liczbę punktów/fragów oraz przyciski "+1" i "-1"
* używa `useState` do przechowywania aktualnego wyniku
* używa `useRef` do zapisania poprzedniego wyniku i wyświetlenia go pod spodem ("Poprzedni wynik: X")
* używa `useEffect`, aby aktualizować referencję przy każdej zmianie stanu punktów

## Zadanie 2 - Wyszukiwarka zawodników z auto-focusem (3 pkt)

### Stwórz komponent PlayerSearchBox, który:

* ma pole input na wpisanie nicku powiązane ze stanem (`useState`)
* dba o dostępność (WCAG) poprzez prawidłowe powiązanie pola input z etykietą `<label>`
* automatycznie ustawia kursor (focus) w polu po załadowaniu widoku (`useRef` + `useEffect`)
* po naciśnięciu klawisza Enter wypisuje wpisany nick w konsoli i czyści input
* wyświetla aktualną liczbę znaków wpisanego nicku poniżej pola

## Zadanie 3 - Pobieranie profilu z API (4 pkt)

### Stwórz komponent PlayerProfileLoader, który:

* po załadowaniu pobiera dane zawodnika z `[https://jsonplaceholder.typicode.com/users/3](https://jsonplaceholder.typicode.com/users/3)`
* zapisuje pobrany wynik w stanie (`useState`)
* wyświetla status ładowania ("Wczytywanie..."), błąd lub nazwę gracza w zależności od stanu zapytania
* używa funkcji czyszczącej (cleanup function) w `useEffect`, aby bezpiecznie obsłużyć odmontowanie komponentu w trakcie pobierania danych

Oto najprostsza możliwa wersja zadania z `useEffect`, która nie wymaga znajomości asynchroniczności, timerów, API ani zdarzeń okna. Klasycznym i najłatwiejszym przykładem na zrozumienie "efektu ubocznego" jest zmiana tytułu zakładki w przeglądarce.

## Zadanie 3 (ALT) - Aktualizacja tytułu strony (4 pkt)

### Stwórz komponent TabTitleChanger, który:

* wyświetla aktualną liczbę punktów oraz przycisk "Dodaj punkt"
* używa `useState` do przechowywania liczby punktów (zaczynając od 0)
* używa `useEffect`, aby za każdym razem, gdy zmieni się liczba punktów, zaktualizować tytuł zakładki w przeglądarce (wykorzystując do tego `document.title`)
* nowy tytuł karty powinien brzmieć np.: "Zdobyte punkty: X" (gdzie X to aktualny stan)