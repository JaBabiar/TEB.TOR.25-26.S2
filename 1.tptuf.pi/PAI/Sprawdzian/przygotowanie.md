# Sprawdzian: Kalkulator przejazdu

W ramach zadania stwórz prostą aplikację webową do obliczania kosztów przejazdu. Rozwiązanie ma składać się z trzech plików: HTML, CSS i JS.

## 1. Struktura (HTML)
- Oprzyj dokument o tagi semantyczne: `header`, `main` oraz `footer`.
- Wewnątrz `main` utwórz dwie oddzielne sekcje, jedna z formularzem a druga z wypisanymi danymi w liście.
- Pamiętaj o wymogach WCAG – upewnij się, że każde pole w formularzu ma prawidłowo podpięty znacznik `label`.

## 2. Układ i wygląd (CSS)
- Użyj Flexboxa lub Grida, żeby sekcje w bloku `main` ustawiły się obok siebie w dwóch kolumnach.
- Kontener `main` ma mieć szerokość 1440px i być wyśrodkowany na stronie.
- Narzuć konkretny styl: sekcja z formularzem ma mieć jasnoszare tło, a sekcja z logami obramowanie (border: 1px solid black) na granicy z drugą sekcją. Dodaj podstawowe marginesy wewnętrzne 10px.

## 3. Działanie (JS)
- W pierwszej sekcji umieść formularz, który zbiera dwa parametry: imię klienta (tekst) i liczbę kilometrów (liczba).
- Po kliknięciu w przycisk zatrzymaj domyślne przeładowanie strony.
- W skrypcie ustaw na sztywno stawkę: 5 zł za 1 km.
- Oblicz koszt całkowity.
- W drugiej sekcji dopisz za pomocą skryptu wynik w postaci: `Klient [Imię]: [Liczba] km = [Koszt] zł`.
- Po wyświetleniu wyniku wyczyść oba pola formularza.