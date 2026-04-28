# Kartkówka INF.03 - Obsługa danych (Grupa 1)

## 1. Struktura HTML

W pliku `index.html` przygotuj strukturę, używając wyłącznie skrótu Emmet:
`(label+input)*2+button`

**Wymagania:**

* **Pierwsza para:** Etykieta "Nazwa produktu" oraz pole tekstowe.
* **Druga para:** Etykieta "Cena netto" oraz pole typu liczbowego.
* **Przycisk:** Napis "Oblicz".
* **Dostępność:** Połącz etykiety z polami za pomocą atrybutów `id` oraz `for` (zgodnie z WCAG).
* **Uwaga:** Nie używaj znacznika `<form>`.

## 2. Skrypt JavaScript

Napisz skrypt, który po kliknięciu przycisku:

1. Pobierze wartości z obu pól do zmiennych.
2. **Sprawdzi (walidacja):** czy nazwa produktu nie jest pusta oraz czy cena jest liczbą większą od zera.
3. **Wypisze w konsoli:**
    * Jeśli dane są poprawne: `Produkt: [Nazwa], Cena brutto (23%): [Cena * 1.23]`.
    * Jeśli dane są błędne: `Błąd danych!`.

---

## System oceniania

| Wynik procentowy | Ocena |
| :--- | :--- |
| 0% – 49% | 1 (niedostateczny) |
| 50% – 59% | 2 (dopuszczający) |
| 60% – 74% | 3 (dostateczny) |
| 75% – 89% | 4 (dobry) |
| 90% – 100% | 5 (bardzo dobry) |
