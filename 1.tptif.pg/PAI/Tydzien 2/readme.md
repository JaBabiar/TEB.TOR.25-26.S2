# Podstawy Semantyki HTML i Wstęp do Flexboxa

## 1. Semantyczny HTML

Semantyka w HTML oznacza używanie tagów, które jasno opisują swoje przeznaczenie zarówno dla przeglądarki, jak i dla programisty. Zamiast budować całą stronę na bezimiennych blokach `<div>`, używamy znaczników strukturalnych. Ma to kolosalne znaczenie dla dostępności cyfrowej (WCAG), ponieważ pozwala czytnikom ekranowym poprawnie nawigować po stronie.

* `<header>` – określa nagłówek strony lub sekcji (często zawiera logo i nawigację).
* `<main>` – przechowuje główną, unikalną treść dokumentu. Na stronie powinien znajdować się tylko jeden taki tag.
* `<section>` – grupuje powiązaną ze sobą tematycznie treść.
* `<footer>` – definiuje stopkę dokumentu lub sekcji.

## 2. Podstawy układu z Flexbox

W tym tygodniu do układania elementów obok siebie wykorzystujemy podstawy Flexboxa.

* Aby elementy (np. sekcje) ustawiły się w jednym rzędzie zamiast jedna pod drugą, wystarczy na ich wspólnym rodzicu (np. `<main>`) nałożyć właściwość `display: flex;`.

## 3. Zarządzanie wielkością i klasami

Rozmiar elementów możemy kontrolować za pomocą jednostek stałych (jak piksele) oraz względnych (jak procenty).

* **Szerokość (Width):** Ustawienie `width: 33.3%;` sprawia, że element zajmie dokładnie jedną trzecią dostępnej szerokości swojego rodzica. Dzięki temu trzy takie same sekcje idealnie wypełnią całą szerokość kontenera `main` w jednym rzędzie.
* **Wysokość (Height):** Wysokość określamy zazwyczaj w pikselach, np. `height: 300px;` dla sekcji, czy `height: 100px;` dla nagłówka.
* **Klasy pomocnicze:** Używamy klas, aby nadpisywać standardowe style dla wybranych elementów. Klasa `.yellow-bg` zmienia domyślny czerwony kolor tła na żółty, a kolor tekstu na czerwony. Dzięki temu możemy łatwo tworzyć naprzemienne schematy kolorystyczne.
