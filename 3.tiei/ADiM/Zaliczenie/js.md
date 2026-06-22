# Zaliczenie JS
## Wytyczne dotyczące struktury HTML:
1. Plik należy zapisać pod nazwą `index.html`.
2. W sekcji `<body>` powinien znaleźć się kontener, a w nim:
    - Pole tekstowe na **Login**.
    - Pole tekstowe  na **Hasło**.
    - Przycisk z napisem „Zaloguj” wywołujący funkcję `weryfikuj()`.
    - Pola tekstowe muszą zawierać Etykiety zgodnie z WCAG
3. Pod formularzem powinien znajdować się blok `<span>` o identyfikatorze `wynik`.
## Wytyczne dotyczące skryptu JavaScript:
Skrypt powinien realizować następujące punkty:
1. Pobierać wartości z obu pól (login i hasło).
2. Sprawdzać, czy pola nie są puste. Jeśli brakuje danych:
    - Wypisać w konsoli: „Błąd: uzupełnij pola”.
    - Przerwać działanie funkcji.
3. Logika weryfikacji:
    - Jeśli login to **„admin”** ORAZ hasło to **„123”**:
        - Wypisać w `<span>`: „Witaj administratorze!”.
    - W przeciwnym razie:
        - Wypisać w `<span>`: „Błędny login lub hasło”.
