## Część 1: Rozbudowana struktura HTML

Utwórz plik `index.html` z poprawną, semantyczną strukturą dokumentu HTML5.

Przygotuj główny kontener `main`, a w nim umieść **9 elementów** reprezentujących pozycje w bibliotece (np. Gry, ksiązki etc.). Każda pozycja musi być kompletną, niezależną sekcją i zawierać:

* **Nagłówek** Gry/Książki,
* **Autora/Wydawce** np. Adam Mickiewicz/CD Projekt,
* **Opis** ok. 15 losowych słów (najlepiej Lorem Ipsum)
* **Cenę** (wyraźnie wyróżnioną wizualnie) np. czerwony tekst i większa czcionka,

Wykorzystaj odpowiednie, czyste znaczniki semantyczne HTML5 (np. `article`, `section`). Zadbaj o pełną zgodność z wytycznymi dostępności cyfrowej WCAG – w szczególności pamiętaj o zachowaniu logicznej struktury i hierarchii nagłówków oraz zapewnieniu odpowiedniego kontrastu tekstu względem tła.

## Część 2: Domyślny wygląd (Desktop – ekrany powyżej 1024px)

W dołączonym pliku CSS stwórz style domyślne przeznaczone dla dużych ekranów:

* **Układ:** Główny kontener ma wyświetlać pozycje menu w układzie siatki  podzielonym na **3 równe kolumny** w rzędzie, z zachowaniem estetycznego odstępu między elementami.
* **Karta:** Każda pozycja delikatne, jednolite tło (np. `#fafafa`), wyraźne obramowanie dolne jako akcent kolorystyczny, zaokrąglone rogi  oraz wewnętrzny margines.
* **Kompozycja:** cena powinna znajdować się zawsze po prawej stronie na samym dole karty, niezależnie od długości opisu i liczby użytych słów.

## Część 3: Responsywność i elastyczność (Media Queries)

Na dole pliku CSS dopisz reguły modyfikujące układ. **Ważne:** Ogranicz zapytania z punktów 1, 2 i 3 wyłącznie do nośników typu ekranowego (`screen`).

1. **Dla laptopów / mniejszych ekranów (od 1025px do 1280px włącznie):**
* Zmień układ kontenera, aby pozycje menu automatycznie dopasowywały się i układały w **4 węższych kolumnach** .

2. **Dla tabletów w orientacji poziomej i pionowej (od 768px do 1024px włącznie):**
* Zmień układ kontenera, aby pozycje menu układały się w **2 kolumnach**.
* Spraw że opis .

3. **Dla smartfonów (do 767px włącznie):**
* Zmień układ kontenera, aby pozycje menu układały się w **1 kolumnie**.
* Powiększ rozmiar czcionki ceny o 25% oraz znacząco zwiększ przestrzeń klikalną wokół całej karty i jej elementów. Dodaj margines dolny o wartości minimum 24px między kartami.

4. **Dla wydruku (print):**
* Napisz osobną regułę docelową wyłącznie dla nośnika drukowanego (`print`).
* usuń tła dekoracyjne, obramowania oraz wszelkie cienie z pozycji menu.
* Wymuś całkowicie czarny kolor tekstu (`#000000`) na idealnie białym tle (`#ffffff`) oraz zmień krój czcionki na szeryfowy (np. Georgia lub Times New Roman), optymalizując w ten sposób czytelność tekstu na papierze oraz minimalizując zużycie tonera.
