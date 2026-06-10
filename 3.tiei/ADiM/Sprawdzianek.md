# Sprawdzian praktyczny: Tworzenie responsywnego układu strony (Menu Pizzerii)

**Cel sprawdzianu:** Wykazanie się umiejętnością budowania złożonego, responsywnego układu elementów z wykorzystaniem zapytań medialnych (Media Queries), precyzyjnych przedziałów szerokości ekranu oraz zasad dostępności (WCAG).

## Część 1: Rozbudowana struktura HTML

Utwórz plik `index.html` z poprawną strukturą dokumentu. Pamiętaj o konfiguracji niezbędnej do prawidłowego skalowania strony na urządzeniach mobilnych.

Przygotuj główny kontener menu, a w nim umieść **8 elementów** reprezentujących pozycje w menu (np. różne rodzaje pizzy). Każda pozycja w menu musi być kompletną, niezależną sekcją i zawierać:

* **Nagłówek** z nazwą dania,
* **Krótki opis** składników,
* **Cenę** (wyróżnioną wizualnie),
* **Badge / Ekietę** (np. "Wege", "Ostra", "Bestseller") dla przynajmniej trzech wybranych pozycji.

Wykorzystaj odpowiednie, czyste znaczniki semantyczne HTML5. Zadbaj o zgodność z wytycznymi dostępności cyfrowej WCAG (m.in. poprzez zastosowanie poprawnej, logicznej hierarchii nagłówków).

## Część 2: Domyślny wygląd (Desktop – ekrany powyżej 1024px)

W dołączonym pliku CSS stwórz style domyślne dla dużych ekranów:

* **Układ:** Główny kontener ma wyświetlać pozycje menu w układzie siatki (Grid lub Flexbox) podzielonym na **4 równe kolumny** w jednym rzędzie.
* **Karta dania:** Każda pozycja w menu powinna posiadać widoczne obramowanie, zaokrąglone rogi (border-radius), wewnętrzny margines (padding) oraz delikatny cień (box-shadow).
* **Kompozycja:** Ekieta ("Wege"/"Ostra") musi być wypozycjonowana w prawym górnym rogu karty dania, a cena powinna znajdować się zawsze na samym dole karty, niezależnie od długości opisu.

## Część 3: Responsywność i elastyczność (Media Queries)

Na dole pliku CSS dopisz reguły modyfikujące układ. **Ważne:** Ogranicz zapytania z punktów 1, 2 i 3 wyłącznie do ekranów (`screen`).

1. **Dla laptopów / mniejszych ekranów (od 1025px do 1280px włącznie):**
* Zmień układ kontenera, aby pozycje menu układały się w **3 kolumnach**.


2. **Dla tabletów w orientacji poziomej i pionowej (od 768px do 1024px włącznie):**
* Zmień układ kontenera, aby pozycje menu układały się w **2 kolumnach**.
* Zmień kolor tła pozycji menu na jasnoszary (`#f4f4f4`), a kolor obramowania na nieco ciemniejszy.


3. **Dla smartfonów (do 767px włącznie):**
* Zmień układ kontenera, aby pozycje menu układały się w **1 kolumnie** (każda zajmuje 100% szerokości dostępnego miejsca).
* Powiększ rozmiar czcionki nagłówków w pozycjach menu o 20% oraz zwiększ przestrzeń klikalną (padding) wokół całej karty, aby ułatwić przeglądanie menu na małych wyświetlaczach dotykowych.


4. **Dla wydruku (print):**
* Napisz osobną regułę docelową wyłącznie dla nośnika drukowanego (`print`).
* Ukryj wszystkie etykiety (badg-e), usuń obramowanie, zaokrąglenia rogów oraz cienie z pozycji menu.
* Wymuś całkowicie czarny kolor tekstu na całkowicie białym tle, aby zoptymalizować zużycie tonera i czytelność na papierze.
