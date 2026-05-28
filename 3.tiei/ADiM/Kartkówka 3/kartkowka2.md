# Zadanie praktyczne: Menu Pizzerii

**Cel:** Zbudowanie responsywnego układu pozycji w menu z wykorzystaniem zapytań medialnych i precyzyjnych przedziałów szerokości ekranu.

## Krok 1: Struktura HTML

Utwórz plik `index.html` z poprawną strukturą dokumentu. Pamiętaj o konfiguracji niezbędnej do prawidłowego skalowania strony na urządzeniach mobilnych.

Przygotuj główny kontener, a w nim umieść 6 elementów reprezentujących pojedyncze pozycje w menu (np. różne rodzaje pizzy). Każda z pozycji musi zawierać:

* Nagłówek z nazwą dania,
* Krótki opis składników.

Wykorzystaj odpowiednie znaczniki semantyczne. Zadbaj o dostępność cyfrową (m.in. logiczną strukturę nagłówków).

### Krok 2: Domyślny wygląd (Desktop)

W pliku CSS stwórz style domyślne dla dużych ekranów:

* Główny kontener ma wyświetlać pozycje menu w układzie siatki (Grid lub Flexbox) podzielonym na **3 równe kolumny**.
* Każda pozycja w menu powinna posiadać obramowanie, wewnętrzny margines (padding) oraz delikatny cień pod spodem.

### Krok 3: Responsywność

Na dole pliku CSS dopisz reguły modyfikujące układ. Ogranicz zapytania 1 i 2 wyłącznie do ekranów.

1. **Dla tabletów (przedział szerokości):**
Napisz regułę dla ekranów o szerokości od `768px` do `1024px` włącznie.

* Zmień układ kontenera, aby pozycje menu układały się w **2 kolumnach**.
* Zmień kolor tła pozycji na jasnoszary (`#f4f4f4`).

2. **Dla smartfonów:**
Napisz regułę dla ekranów o szerokości do `767px` włącznie.

* Zmień układ kontenera, aby pozycje menu układały się w **1 kolumnie** (każda zajmuje 100% szerokości dostępnego miejsca).
* Powiększ rozmiar czcionki nagłówków w pozycjach menu o 20%, aby ułatwić czytanie na małych wyświetlaczach.

3. **Dla wydruku:**
Napisz osobną regułę wyłącznie dla nośnika drukowanego.

* Usuń obramowanie i cienie z pozycji menu.
* Wymuś całkowicie czarny kolor tekstu na całkowicie białym tle.