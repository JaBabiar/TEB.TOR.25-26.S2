# Podstawy JavaScript: Typy danych, Tablice, Pętle i DOM

## 1. Zmienne i Typy Danych

W JavaScript do deklarowania zmiennych używamy słowa kluczowego `let` (lub `const` dla stałych). W zmiennych możemy przechowywać różne typy informacji:

* **Tekst (String):** Wartości w cudzysłowach, np. `"string"`. Możemy pobierać z nich konkretne litery (np. `tekst[0]`) lub zmieniać wielkość liter za pomocą metod `.toLowerCase()` i `.toUpperCase()`.
* **Liczby (Number):** Cyfry całkowite i ułamkowe. Możemy wykonywać na nich standardowe operacje matematyczne (`+`, `-`, `*`) oraz korzystać z operatora reszty z dzielenia - modulo (`%`).
* **Wartości logiczne (Boolean):** Prawda (`true`) lub fałsz (`false`).
* **Konwersja:** Tekst zawierający cyfry (np. `"16"`) można zamienić na prawdziwą liczbę za pomocą `parseInt()` (dla liczb całkowitych) lub `parseFloat()` (dla ułamków).

## 2. Złożone typy danych: Tablice i Obiekty

* **Tablice (Listy):** Służą do przechowywania wielu wartości w jednej zmiennej (np. `[5, 6, "jajco", 2, 1]`).
  * Elementy pobieramy po ich indeksie (licząc od 0), np. `lista[0]`.
  * Długość tablicy sprawdzamy właściwością `.length`.
  * Przydatne metody: `.push()` (dodaje na koniec), `.pop()` (usuwa z końca), `.indexOf()` (szuka pozycji elementu), `.slice()` (kopiuje fragment) oraz `.splice()` (usuwa lub podmienia element w środku).
* **Obiekty:** Służą do opisywania rzeczy za pomocą właściwości (klucz: wartość). Do wartości odwołujemy się po kropce, np. `obiekt.imie`.

## 3. Logika i Manipulacja DOM

Za pomocą JavaScript możemy dynamicznie zmieniać to, co widzi użytkownik na stronie HTML.

* **Pobieranie elementów:** `document.getElementById('output')` pozwala "uchwycić" element HTML po jego identyfikatorze.
* **Instrukcje warunkowe (`if / else`):** Pozwalają wykonać różny kod w zależności od tego, czy dany warunek jest spełniony.
* **Pętle (`for`):** Służą do wielokrotnego powtarzania tego samego bloku kodu.
* **Modyfikacja HTML:** Właściwość `innerHTML` pozwala wstrzykiwać nowe znaczniki HTML do pobranego elementu, a `textContent` zwraca czysty tekst bez znaczników.

## 💡 Dobre praktyki i dostępność cyfrowa (WCAG)

* **Zrozumiałość dynamicznych zmian:** Kiedy wstrzykujesz treść na stronę za pomocą JS (tak jak w naszej pętli generującej liczby), czytniki ekranowe mogą nie zauważyć tej zmiany, chyba że zastosujesz odpowiednie atrybuty ARIA (np. `aria-live`).
* **Czytelność kodu:** Unikaj wstrzykiwania złożonego kodu HTML bezpośrednio przez `innerHTML` w postaci długich "sklejek" tekstu (konkatenacji). Łatwo tam o błąd (np. brak domknięcia cudzysłowu). W przyszłości warto korzystać z tzw. *Template Literals* (grawisów ` ` `).
* **Semantyka znacznika `<span>`:** Znacznik ten nie niesie ze sobą żadnego znaczenia. Jeśli używasz go tylko do pokolorowania elementu na czerwono, upewnij się, że informacja ta (np. o parzystości liczby) wynika również z kontekstu, a nie tylko z koloru (WCAG 1.4.1 Użycie koloru).
