# Sprawdzian praktyczny: Tworzenie responsywnego układu strony (Menu Burgerowni) – Grupa 2

**Cel sprawdzianu:** Wykazanie się umiejętnością budowania złożonego, responsywnego układu elementów z wykorzystaniem zapytań medialnych (Media Queries), precyzyjnych przedziałów szerokości ekranu oraz zasad dostępności cyfrowej (WCAG).

## Część 1: Rozbudowana struktura HTML

Utwórz plik `index.html` z poprawną, semantyczną strukturą dokumentu HTML5. Pamiętaj o dodaniu i skonfigurowaniu znacznika `meta` viewport, który jest niezbędny do prawidłowego skalowania i renderowania strony na urządzeniach mobilnych.

Przygotuj główny kontener menu, a w nim umieść **9 elementów** reprezentujących pozycje w menu (np. różne rodzaje burgerów lub zestawów). Każda pozycja w menu musi być kompletną, niezależną sekcją i zawierać:

* **Nagłówek** z nazwą dania,
* **Krótki opis** składników wraz z informacją o gramaturze,
* **Cenę** (wyraźnie wyróżnioną wizualnie),
* **Badge / Etykietę** (np. "Vegan", "Keto", "Nowość", "Szef Poleca") dla przynajmniej trzech wybranych pozycji.

Wykorzystaj odpowiednie, czyste znaczniki semantyczne HTML5 (np. `article`, `section`). Zadbaj o pełną zgodność z wytycznymi dostępności cyfrowej WCAG – w szczególności pamiętaj o zachowaniu logicznej struktury i hierarchii nagłówków oraz zapewnieniu odpowiedniego kontrastu tekstu względem tła.

## Część 2: Domyślny wygląd (Desktop – ekrany powyżej 1024px)

W dołączonym pliku CSS stwórz style domyślne przeznaczone dla dużych ekranów:

* **Układ:** Główny kontener ma wyświetlać pozycje menu w układzie siatki (Grid lub Flexbox) podzielonym na **3 równe kolumny** w rzędzie, z zachowaniem estetycznego odstępu (gap) między elementami.
* **Karta dania:** Każda pozycja w menu powinna posiadać delikatne, jednolite tło (np. `#fafafa`), wyraźne obramowanie górne (`border-top`) jako akcent kolorystyczny, zaokrąglone dolne rogi (border-radius) oraz wewnętrzny margines (padding).
* **Kompozycja:** Etykieta ("Vegan"/"Nowość") musi być wypozycjonowana w lewym górnym rogu karty dania, natomiast cena powinna znajdować się zawsze po prawej stronie na samym dole karty, niezależnie od długości opisu i liczby użytych słów.

## Część 3: Responsywność i elastyczność (Media Queries)

Na dole pliku CSS dopisz reguły modyfikujące układ. **Ważne:** Ogranicz zapytania z punktów 1, 2 i 3 wyłącznie do nośników typu ekranowego (`screen`).

1. **Dla laptopów / mniejszych ekranów (od 1025px do 1280px włącznie):**
* Zmień układ kontenera, aby pozycje menu automatycznie dopasowywały się i układały w **4 węższych kolumnach** (w celu przetestowania elastyczności komponentów).

2. **Dla tabletów w orientacji poziomej i pionowej (od 768px do 1024px włącznie):**
* Zmień układ kontenera, aby pozycje menu układały się w **2 kolumnach**.
* Zmień kolor tła pozycji menu na bardzo jasny odcień pastelowej zieleni lub beżu (np. `#f0f4f1`), a górne obramowanie karty na ciemniejszy, bardziej kontrastowy kolor.

3. **Dla smartfonów (do 767px włącznie):**
* Zmień układ kontenera, aby pozycje menu układały się w **1 kolumnie** (każda karta zajmuje 100% szerokości dostępnego obszaru roboczego).
* Powiększ rozmiar czcionki ceny o 25% oraz znacząco zwiększ przestrzeń klikalną (padding) wokół całej karty i jej elementów. Dodaj margines dolny (margin-bottom) o wartości minimum 24px między kartami, aby spełnić kryteria WCAG dotyczące minimalnego rozmiaru celów dotykowych (Target Size) na małych ekranach.

4. **Dla wydruku (print):**
* Napisz osobną regułę docelową wyłącznie dla nośnika drukowanego (`print`).
* Ukryj wszystkie etykiety (badge), usuń tła dekoracyjne, obramowania oraz wszelkie cienie z pozycji menu.
* Wymuś całkowicie czarny kolor tekstu (`#000000`) na idealnie białym tle (`#ffffff`) oraz zmień krój czcionki na szeryfowy (np. Georgia lub Times New Roman), optymalizując w ten sposób czytelność tekstu na papierze oraz minimalizując zużycie tonera.
