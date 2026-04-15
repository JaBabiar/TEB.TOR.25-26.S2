

# Kartkówka: Dynamiczne zarządzanie stylem elementu przez JavaScript

---

### Opis zadania

Stwórz aplikację webową składającą się z formularza oraz elementu podglądu (`div`). Użytkownik powinien móc wpisać parametry w formularzu, a po kliknięciu przycisku, styl elementu podglądu powinien zostać zaktualizowany zgodnie z wprowadzonymi danymi.

### Wymagania techniczne:

#### 1. Struktura HTML (3 pkt)

* Przygotuj kontener wizualny (np. `div` o id `preview-box`), który będzie stylizowany.
* Zbuduj formularz zawierający pola tekstowe lub numeryczne dla następujących właściwości:

    * Wysokość,
    * Szerokość,
    * Kolor tła,
    * Zaokrąglenie rogów (border-radius),
    * Treść napisu, który pojawi się wewnątrz elementu.
* **Dostępność (WCAG):** Każde pole formularza musi posiadać poprawnie przypisaną etykietę `<label>`.


#### 3. Logika JavaScript (7 pkt)

* Pobierz wszystkie niezbędne elementy z dokumentu DOM do zmiennych/stałych.
* Dodaj nasłuchiwanie zdarzenia 
* Wewnątrz funkcji obsługującej zdarzenie:
    * Pobierz aktualne wartości wpisane przez użytkownika.
    * Zastosuj pobrane wartości do elementu podglądu za pomocą właściwości `.style`.
    * Zaktualizuj tekst wewnątrz elementu (wykorzystaj `textContent` lub `innerText`).

---
