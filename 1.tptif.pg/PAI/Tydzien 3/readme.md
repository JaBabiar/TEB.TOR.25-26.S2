# Metody Display oraz Układ Bloków

## 1. Właściwość Float (Opływanie)

Historycznie `float` był używany do tworzenia całych układów stron. Dziś służy głównie do tego, do czego został stworzony: opływania obrazków przez tekst.

* `float: left;` / `float: right;` – sprawia, że element jest "wyjmowany" ze standardowego przepływu i dosuwany do lewej lub prawej krawędzi.
* **Clearfix:** Kiedy rodzic zawiera tylko elementy opływające, "zapada się". Zastosowanie `display: flow-root` na kontenerze rozwiązuje ten problem, tworząc nowy kontekst formatowania.

## 2. Flexbox (Układ Jednowymiarowy)

Flexbox służy do układania elementów w jednym rzędzie lub jednej kolumnie.

* Włączenie flexboxa następuje poprzez przypisanie kontenerowi `display: flex;`.
* **Główna oś (justify-content):** Służy do rozmieszczania elementów w poziomie (domyślnie). Popularne wartości to `center`, `space-between`, `space-evenly`, `space-around`.
* **Oś poprzeczna (align-items / align-content):** Wyrównuje elementy w pionie (np. `align-content: center;`).
* **Właściwości dzieci:** `flex-shrink: 1;` sprawia, że element może się kurczyć, gdy brakuje miejsca. Zabezpiecza się to często za pomocą `min-width`.

## 3. CSS Grid (Układ Dwuwymiarowy)

Najpotężniejsze narzędzie do tworzenia całych struktur (siatek) opartych na wierszach i kolumnach. Uruchamiamy go za pomocą `display: grid;`.

* **Definiowanie siatki:**
  * `grid-template-columns: 15% repeat(2, 1fr);` – tworzy 3 kolumny: pierwsza na 15% szerokości, a dwie kolejne dzielą się po równo pozostałą przestrzenią (jednostka `fr` - fraction).
  * `grid-template-rows: 300px 100px;` – ustala wysokość kolejnych wierszy.
* **Umiejscawianie elementów:** Właściwość `grid-area: row-start / col-start / row-end / col-end;` pozwala na precyzyjne rozciąganie bloków na siatce (np. `grid-area: 1 / 1 / 3 / 1;` zajmuje 2 wiersze w pierwszej kolumnie).

## 💡 Dobre praktyki i dostępność cyfrowa

Podczas tworzenia układów z wykorzystaniem Flexbox i Grid, **wizualna kolejność elementów nie powinna różnić się od ich rzeczywistej kolejności w kodzie HTML**.

* Zmiana kolejności za pomocą CSS nie wpływa na to, jak stronę czytają czytniki ekranowe
* Zawsze zaczynaj od poprawnej struktury i używaj znaczników semantycznych (`<header>`, `<section>`, `<footer>`), a dopiero potem modyfikuj ich ułożenie w CSS
