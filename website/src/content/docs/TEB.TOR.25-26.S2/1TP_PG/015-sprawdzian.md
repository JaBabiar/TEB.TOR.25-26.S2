---
title: "Sprawdzian Praktyczny INF.03 - Front-End"
course: "TEB.TOR.25-26"
layout: ../layouts/ExamLayout.astro
---

# Zadanie Egzaminacyjne: Aplikacja "Kalkulator Usług IT"

## Instrukcja dla zdającego
Twoim zadaniem jest wykonanie aplikacji internetowej dla firmy informatycznej. Utwórz kod HTML, CSS oraz JavaScript. Pliki zapisz pod nazwami: `index.html`, `styl.css`, `skrypt.js` i połącz je w logiczną całość. 

Zadanie ma formę praktyczną i symuluje kwalifikację INF.03. Zadbaj o przejrzystość kodu oraz zgodność z wytycznymi technicznymi.

---

## Wytyczne do wykonania

### 1. Struktura i znaczniki HTML
- Zastosuj znaczniki semantyczne standardu HTML5.
- Struktura strony musi składać się z:
  - Nagłówka strony.
  - Kontenera głównego, a w nim:
    - Bloku lewego 
    - Bloku prawego.
  - Stopki.
- W bloku lewym utwórz formularz wyceny usług zawierający:
  - Etykietę o treści "Imię i nazwisko klienta:" z powiązanym polem tekstowym.
  - Etykietę o treści "Liczba stanowisk do konfiguracji:" z powiązanym polem liczbowym (`<input type="number">`).
  - Przycisk typu `<button>` lub `<input type="button">` z napisem "Oblicz koszt".
- W bloku prawym przygotuj wyodrębniony obszar (np. paragraf lub nagłówek z unikalnym identyfikatorem) przeznaczony do wyświetlenia wyniku działania skryptu.

### 2. Wygląd i kaskadowe arkusze stylów (CSS)
- Podepnij zewnętrzny arkusz `styl.css` do pliku HTML.
- **Kolorystyka witryny:**
  - Nagłówek oraz stopka muszą posiadać identyczny, jednolity kolor tła (np. ciemny odcień szarości).
  - Blok lewy oraz blok prawy muszą mieć przypisane dwa różne kolory tła, tak aby wyraźnie odcinały się od siebie nawzajem oraz od nagłówka i stopki.
- **Układ blokowy kontenera głównego:** Kontener główny musi automatycznie dopasowywać swoją wysokość do zawartości i poprawnie obejmować wszystkie elementy znajdujące się wewnątrz niego (nie może ulegać "zapadnięciu").
- **Wymiary i pozycjonowanie kolumn:**
  - Blok lewy musi mieć szerokość ustawioną na dokładnie `40%` oraz wysokość wynoszącą `450px`.
  - Blok prawy musi mieć szerokość ustawioną na dokładnie `60%` oraz wysokość wynoszącą `450px`.
  - Oba bloki (lewy i prawy) muszą bezwzględnie układać się obok siebie w jednej osi poziomej, tworząc stabilną strukturę dwukolumnową, która nie rozjeżdża się przy zmianie szerokości okna przeglądarki. Wybór metody pozycjonowania bloków należy do zdającego.
- **Marginesy wewnętrzne (Padding):** Zawartość formularza w lewym bloku oraz tekst wyniku w prawym bloku nie mogą bezpośrednio stykać się z krawędziami bocznymi swoich kontenerów. Zastosuj wewnętrzny odstęp o wielkości minimum `15px`.
- **Stopka:** Ustaw szerokość stopki na `100%`. Stopka musi zawsze wyświetlać się na samym dole strony, bezpośrednio pod spodem obu paneli bocznych — niedopuszczalne jest, aby kolumny nachodziły na stopkę lub aby stopka zasłaniała ich zawartość.

### 3. Logika i JavaScript
- Napisz funkcję, która zostanie wywołana po kliknięciu przycisku "Oblicz koszt".
- Pobierz wartości wpisane przez użytkownika w formularzu.
- Oprogramuj poniższą logikę:
  - Jeżeli pole liczby stanowisk jest puste lub wartość jest mniejsza niż 1, wyświetl pod formularzem komunikat o błędzie: *"Błąd: Wprowadź poprawną liczbę stanowisk!"*.
  - Jeśli dane są poprawne, pomnóż liczbę stanowisk przez bazową stawkę roboczogodziny (np. `150 zł`).
  - Wyświetl w przygotowanym obszarze (w bloku prawym) wynik wg wzoru: 
    *"Witaj [Imię i nazwisko], wyliczony koszt konfiguracji [Liczba] stanowisk wynosi: [Wynik] PLN."*

---

## Schemat punktacji i oceny

* **50%** (10 - 12 pkt) ➔ **Ocena: 2 (Dopuszczający)**
* **65%** (13 - 14 pkt) ➔ **Ocena: 3 (Dostateczny)**
* **75%** (15 - 17 pkt) ➔ **Ocena: 4 (Dobry)**
* **90%** (18 - 19 pkt) ➔ **Ocena: 5 (Bardzo dobry)**
* **100%** (20 pkt) ➔ **Ocena: 6 (Celujący)**