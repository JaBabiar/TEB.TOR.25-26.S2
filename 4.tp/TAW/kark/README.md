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