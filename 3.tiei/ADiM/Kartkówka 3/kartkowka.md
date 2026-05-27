# Zadanie praktyczne: Katalog Ofert Pracy

## Krok 1: Struktura HTML

Utwórz plik `index.html` z poprawną strukturą dokumentu. Pamiętaj o konfiguracji niezbędnej do prawidłowego skalowania strony na urządzeniach mobilnych.

Przygotuj główny kontener, a w nim umieść 6 elementów reprezentujących pojedyncze oferty pracy. Każda z ofert musi zawierać:

* Nagłówek z nazwą stanowiska,
* Krótki opis wymagań.

Wykorzystaj odpowiednie znaczniki semantyczne. Zadbaj o dostępność cyfrową (m.in. logiczną strukturę nagłówków).

## Krok 2: Domyślny wygląd (Desktop)

W pliku CSS stwórz style domyślne dla dużych ekranów:

* Główny kontener ma wyświetlać oferty w układzie siatki podzielonym na **3 równe kolumny**.
* Każda oferta pracy powinna posiadać obramowanie, wewnętrzny margines oraz delikatny cień pod spodem.

## Krok 3: Responsywność

Na dole pliku CSS dopisz reguły modyfikujące układ.

1. **Dla tabletów (przedział szerokości):**
Napisz regułę dla ekranów o szerokości od `768px` do `1024px` włącznie.

* Zmień układ kontenera, aby oferty układały się w **2 kolumnach**.
* Zmień kolor tła ofert na jasnoszary (`#f4f4f4`).

2. **Dla smartfonów:**
Napisz regułę dla ekranów o szerokości do `767px` włącznie.

* Zmień układ kontenera, aby oferty układały się w **1 kolumnie** (każda zajmuje 100% szerokości dostępnego miejsca).
* Powiększ rozmiar czcionki nagłówków w ofertach o 20%, aby ułatwić czytanie na małych wyświetlaczach.


3. **Dla wydruku:**
Napisz osobną regułę wyłącznie dla nośnika drukowanego.
* Usuń obramowanie i cienie z ofert.
* Wymuś całkowicie czarny kolor tekstu na całkowicie białym tle.