---

title: "Sprawdzian Praktyczny INF.03 - Front-End (Grupa A)"
course: "TEB.TOR.25-26"
layout: ../layouts/ExamLayout.astro

---
# Zadanie Egzaminacyjne: Aplikacja "Kalkulator Wsparcia IT"

## Instrukcja dla zdającego

Twoim zadaniem jest wykonanie aplikacji internetowej dla lokalnego serwisu komputerowego. Utwórz kod HTML, CSS oraz JavaScript. Pliki zapisz pod nazwami: `index.html`, `styl.css`, `skrypt.js` i połącz je w logiczną całość.

Zadanie ma formę praktyczną i symuluje kwalifikację INF.03. Zadbaj o przejrzystość kodu, dostępność oraz zgodność z wytycznymi technicznymi.

---

## Wytyczne do wykonania

### 1. Struktura i znaczniki HTML

* Zastosuj znaczniki semantyczne standardu HTML5.
* Struktura strony musi składać się z:
* Nagłówka strony.
* Kontenera głównego, a w nim:
* Bloku lewego.
* Bloku prawego.


* Stopki.


* W bloku lewym utwórz formularz wyceny usług zawierający:
* Etykietę o treści "Imię i nazwisko klienta:" z powiązanym polem tekstowym.
* Etykietę o treści "Liczba godzin wsparcia:" z powiązanym polem liczbowym (`<input type="number">`).
* Przycisk typu `<button>` lub `<input type="button">` z napisem "Oszacuj koszty".


* Zadbaj o dostępność cyfrową interfejsu: każda etykieta musi być prawidłowo powiązana ze swoim polem za pomocą atrybutów `for` oraz `id`, aby wspierać czytniki ekranowe.
* W bloku prawym przygotuj wyodrębniony obszar (np. paragraf lub nagłówek z unikalnym identyfikatorem) przeznaczony do wyświetlenia wyniku działania skryptu.

### 2. Wygląd i kaskadowe arkusze stylów (CSS)

* Podepnij zewnętrzny arkusz `styl.css` do pliku HTML.
* **Kolorystyka i dostępność:**
* Nagłówek oraz stopka muszą posiadać identyczny, jednolity kolor tła (np. granatowy lub ciemnoniebieski).
* Blok lewy oraz blok prawy muszą mieć przypisane dwa różne kolory tła. Zapewnij wysoki kontrast tekstu w stosunku do tła we wszystkich sekcjach, aby tekst był w pełni czytelny dla osób z wadami wzroku.


* **Układ blokowy kontenera głównego:** Kontener główny musi automatycznie dopasowywać swoją wysokość do zawartości i poprawnie obejmować wszystkie elementy znajdujące się wewnątrz niego.
* **Wymiary i pozycjonowanie kolumn:**
* Blok lewy musi mieć szerokość ustawioną na dokładnie **30%** oraz wysokość wynoszącą **500px**.
* Blok prawy musi mieć szerokość ustawioną na dokładnie **70%** oraz wysokość wynoszącą **500px**.
* Oba bloki muszą bezwzględnie układać się obok siebie w jednej osi poziomej, tworząc stabilną strukturę dwukolumnową, która nie ulega załamaniu przy zmianie rozmiaru okna. Do rozmieszczenia elementów wykorzystaj preferowaną technikę (np. Flexbox).


* **Marginesy wewnętrzne (Padding):** Zawartość w obu blokach bocznych musi posiadać wewnętrzny odstęp o wielkości minimum **20px**, aby tekst nie przylegał do krawędzi kontenera. Ponadto, przycisk formularza musi posiadać wyraźny styl dla stanu `:focus`.
* **Stopka:** Ustaw szerokość stopki na **100%**. Musi ona zawsze znajdować się pod panelami bocznymi, stanowiąc dolne zamknięcie witryny.

### 3. Logika i JavaScript

* Napisz funkcję, która zostanie wywołana po kliknięciu przycisku "Oszacuj koszty".
* Pobierz wartości wpisane przez użytkownika w formularzu.
* Oprogramuj poniższą logikę:
* Jeżeli pole liczby godzin jest puste lub wpisana wartość jest mniejsza niż 1, wyświetl pod formularzem komunikat o błędzie: *"Błąd: Wprowadź poprawną liczbę godzin roboczych!"*.
* Jeśli dane są poprawne, pomnóż podaną liczbę godzin przez stawkę serwisową wynoszącą **150 zł**.
* Wyświetl w przygotowanym obszarze (w bloku prawym) wynik wg wzoru:
*"Zleceniodawca: [Imię i nazwisko klienta], szacowany koszt za [Liczba] godzin wsparcia IT wynosi: [Wynik] PLN."*



---

## Schemat punktacji i oceny

* **od 50%** (10 - 12 pkt) ➔ **Ocena: 2 (Dopuszczający)**
* **od 65%** (13 - 14 pkt) ➔ **Ocena: 3 (Dostateczny)**
* **od 75%** (15 - 17 pkt) ➔ **Ocena: 4 (Dobry)**
* **od 90%** (18 - 19 pkt) ➔ **Ocena: 5 (Bardzo dobry)**
* **100%** (20 pkt) ➔ **Ocena: 6 (Celujący)**