### Witryna internetowa

Przygotowanie grafiki:
* Pliki `home.png` i `znak.png` należy przeskalować z zachowaniem proporcji do szerokości 80 px
* Plik `samochod.jpg` należy zapisać pod tą samą nazwą w formacie PNG z przezroczystym tłem

Cechy witryny:
* Składa się ze stron o nazwach `stacja.html` oraz `obliczenia.html` zapisanych w języku HTML 5. Obie strony różnią się jedynie blokiem lewym
* **Cechy wspólne dla obu stron:**
    * Jawnie zastosowany właściwy standard kodowania polskich znaków
    * Zadeklarowany język dla witryny: polski
    * Tytuł strony widoczny na karcie przeglądarki: „Stacja paliw"
    * Arkusz stylów w pliku o nazwie `styl2.css` prawidłowo połączony z kodem strony
    * Podział strony na bloki: blok banera, poniżej blok menu, poniżej blok lewy i prawy, na dole stopka. Podział zrealizowany za pomocą znaczników sekcji tak, aby po uruchomieniu w przeglądarce wygląd układu bloków był zgodny z obrazem 2
* **Zawartość bloku banera:** nagłówek pierwszego stopnia o treści „Całodobowa stacja paliw"
* **Zawartość bloku menu:**
    * Obraz `home.png`, który jest odnośnikiem do strony `stacja.html`
    * Obraz `znak.png`, który jest odnośnikiem do strony `obliczenia.html`
    * Odnośnik do pliku `kwerendy.txt` o treści: „Pobierz dokumenty"
* **Zawartość bloku prawego:** obraz `samochod.png` z tekstem alternatywnym „samochód"
* **Zawartość stopki:** akapit (paragraf) o treści: „Stronę opracował: ", oraz zawierający numer, którym został podpisany arkusz
* **Zawartość bloku lewego strony `stacja.html`:**
    * Nagłówek drugiego stopnia o treści „Godziny otwarcia stacji"
    * Tabela 3x3, której komórki są wypełnione zgodnie z obrazem 3

| Dzień | Od | Do |
| :--- | :--- | :--- |
| Pn - Sb | 6:00 | 24:00 |
| Nd | 7:00 | 24:00 |

* **Zawartość bloku lewego strony `obliczenia.html`:**
    * Nagłówek drugiego stopnia o treści „Orientacyjny koszt paliwa"
    * Pole edycyjne typu numerycznego, z napisem nad polem: „Rodzaj paliwa (1-benzyna, 2-olej napędowy):"
    * Pole edycyjne typu numerycznego z napisem nad polem: „Ile litrów?"
    * Przycisk o treści „OBLICZ"

### Styl CSS witryny internetowej

Cechy formatowania CSS, działające na obu stronach:
* Styl CSS zdefiniowany w całości w zewnętrznym pliku o nazwie `styl2.css`
* Domyślne formatowanie wszystkich selektorów: krój czcionki Cambria, wyrównanie tekstu do środka
* Wspólne dla bloku banera i stopki: kolor tła `rgb(120, 0, 46)`; biały kolor czcionki, marginesy wewnętrzne 5 px, rozmiar czcionki 150%
* Dla bloku menu: kolor tła `rgb(173, 20, 87)`; wyrównanie tekstu do lewej strony
* Dla bloku lewego: kolor tła `Snow`; kolor czcionki `OliveDrab`, szerokość 60%, wysokość 322 px, wyrównanie tekstu do lewej strony
* Dla bloku prawego: kolor tła `rgb(173, 20, 87)`; szerokość 40%, wysokość 322 px
* Dla obrazu z samochodem: marginesy zewnętrzne 40 px, wewnętrzne 10 px
* Gdy kursor myszy znajdzie się na samochodzie pojawia się obramowanie kropkowane o szerokości 1 px i kolorze `YellowGreen`
* Dla selektora odnośnika: marginesy wewnętrzne górny i dolny 0 px, lewy i prawy 50 px, kolor czcionki `YellowGreen`
* Dla selektora tabeli i komórki tabeli: obramowanie linią ciągłą o grubości 1 px i kolorze `OliveDrab`
* Dodatkowo dla selektora tabeli: szerokość 90%

Uwaga: style CSS dla odnośnika, tabeli i komórek tabeli należy zdefiniować wyłącznie przy pomocy selektora dla danego znacznika. Jest to uwarunkowane projektem późniejszej rozbudowy witryny.

### Skrypt

Wymagania dotyczące skryptu:
* Napisany w języku wykonywanym po stronie przeglądarki
* Skrypt uruchamia się po wciśnięciu przycisku OBLICZ na stronie `obliczenia.html`
* Skrypt pobiera wartości z obu pól edycyjnych
* Następnie oblicza koszt paliwa ze względu na rodzaj i liczbę litrów uwzględniając:
    * Gdy rodzaj paliwa jest równy 1 - koszt jednego litra paliwa wynosi 4 zł
    * Gdy rodzaj paliwa jest równy 2 - koszt jednego litra paliwa wynosi 3,5 zł
    * W każdym innym przypadku koszt paliwa wynosi 0 zł
* Następnie skrypt wyświetla wynik działania pod przyciskiem OBLICZ według wzoru: „koszt paliwa: `<wartość>` zł", gdzie `<wartość>` oznacza obliczony wcześniej koszt paliwa.