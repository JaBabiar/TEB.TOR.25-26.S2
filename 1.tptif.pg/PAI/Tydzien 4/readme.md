# Model Pudełkowy, Float i Clearfix

## 1. Opływanie elementów (Float)

Właściwość `float` pozwala na ustawienie elementu po lewej lub prawej stronie jego kontenera, pozwalając innym elementom (zazwyczaj tekstowi) opływać go dookoła.

* W naszym układzie używamy `float: left;` dla lewej sekcji (`.l`) oraz prawej sekcji (`.p`). Dzięki temu obie sekcje ustawiają się obok siebie w jednym rzędzie, o ile ich łączna szerokość nie przekracza 100%.
* Podobny zabieg zastosowano dla małych bloków `<div>` wewnątrz lewej sekcji – dzięki `float: left;` układają się one w rzędy tworząc siatkę (np. galerię).

## 2. Problem "zapadającego się" rodzica i Clearfix

Gdy wszystkie elementy wewnątrz kontenera "pływają" (mają nadany `float`), kontener ten zachowuje się tak, jakby był pusty – jego wysokość spada do zera. Nazywamy to "zapadaniem się rodzica".

* Aby temu zapobiec, na rodzicu (np. znaczniku `<main>` oraz sekcji `.l`) stosujemy regułę `display: flow-root;`.
* Tworzy to nowy kontekst formatowania bloków, wymuszając na rodzicu uwzględnienie w swojej wysokości wszystkich "pływających" dzieci.

## 3. Model Pudełkowy i `box-sizing`

Domyślnie w CSS szerokość elementu (`width`) dotyczy tylko jego zawartości. Jeśli dodamy do niego wewnętrzny odstęp (`padding`) lub obramowanie (`border`), element powiększy swoje rzeczywiste wymiary.

* Prawa sekcja ma szerokość `30%` oraz `padding: 10px 20px;`. Domyślnie zajęłaby więc 30% + 40px, co rozbiłoby nasz układ (70% + >30% > 100%), wyrzucając sekcję do nowej linii.
* Rozwiązaniem jest dodanie `box-sizing: border-box;`. Sprawia to, że przeglądarka wlicza `padding` i `border` w zadeklarowaną szerokość (30%), "wciskając" odstępy do środka elementu.

## 💡 Dostępność cyfrowa (WCAG) a stałe wysokości

Zwróć uwagę na regułę `height: 500px;` przypisaną do elementu `<main>`.

* **Ostrzeżenie:** Ustalanie sztywnych wysokości dla kontenerów z tekstem (jak w sekcji `.p`) może naruszać kryterium WCAG 1.4.4 (Zmiana rozmiaru tekstu).
* Jeśli użytkownik niedowidzący powiększy tekst w przeglądarce o 200%, tekst ten może wylać się poza sztywne ramy 500px i stać się nieczytelny. Lepszą praktyką jest używanie `min-height: 500px;`, co pozwala kontenerowi rosnąć wraz z zawartością.
