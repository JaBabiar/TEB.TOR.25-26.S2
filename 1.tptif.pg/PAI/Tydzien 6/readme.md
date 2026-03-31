# Zdarzenia w czasie rzeczywistym i instrukcja Switch

## 1. Nasłuchiwanie zdarzeń (`addEventListener`)

Wcześniej nasze skrypty uruchamiały się zazwyczaj po kliknięciu przycisku. Dzięki metodzie `addEventListener()` możemy nasłuchiwać niemal wszystkiego, co użytkownik robi na stronie, w czasie rzeczywistym.

* Składnia: `element.addEventListener("nazwa_zdarzenia", funkcja_do_wykonania)`.
* **Zdarzenie `input`:** Uruchamia się za każdym razem, gdy wartość pola tekstowego lub liczbowego ulegnie zmianie (np. po wpisaniu każdej pojedynczej cyfry). Dzięki temu nasz kalkulator liczy na bieżąco, bez konieczności wciskania "Oblicz".
* **Zdarzenie `change`:** Uruchamia się, gdy wartość elementu zostanie ostatecznie zmieniona i zatwierdzona. W przypadku rozwijanej listy `<select>`, zdarzenie to odpala się w momencie wybrania nowej opcji `<option>`.

## 2. Rozwijane listy `<select>` i `<option>`

Pobieranie danych z listy rozwijanej jest bardzo proste.

* Kiedy użytkownik wybierze jedną z opcji (np. `<option value="usd">USD</option>`), wartość atrybutu `value` tej opcji staje się wartością całego elementu `<select>`.
* W naszym kodzie pobieramy ją po prostu odwołując się do `waluta.value`.

## 3. Instrukcja `switch`

Gdy mamy jedną zmienną, która może przyjmować wiele konkretnych wartości (np. "eur", "usd", "pln"), pisanie długiego łańcucha `if ... else if ... else if` staje się nieczytelne.

* Instrukcja `switch` przyjmuje zmienną i porównuje ją z różnymi przypadkami (`case`).
* Jeśli znajdzie pasujący przypadek, wykonuje przypisany do niego kod (np. ustawia odpowiedni `przelicznik`).
* **Bardzo ważne:** Pamiętaj o słowie kluczowym `break;` na końcu każdego przypadku! Jeśli go pominiesz, program nie zatrzyma się i "wpadnie" w kolejne przypadki, nadpisując Twój wynik.

## 💡 Dostępność cyfrowa (WCAG) - Gdzie podziały się etykiety?

Zwróć uwagę na plik `index.html`. Mamy tam dwa ważne elementy wejściowe: pole `<input>` oraz listę `<select>`.

* **Błąd:** Żaden z tych elementów nie posiada powiązanego znacznika `<label>`.
* Dla osoby widzącej napis "Przelicznik na Yuany" może być wystarczającą wskazówką. Jednak czytnik ekranowy, po wejściu w pole `<input>`, powie tylko "Pole edycji liczby", a po wejściu w `<select>` powie "Lista rozwijana". Użytkownik niewidomy nie dowie się, że w pierwszym polu ma wpisać kwotę, a w drugim wybrać walutę.
