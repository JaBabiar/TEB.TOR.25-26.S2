---
title: "Sprawdzian: Aplikacja Internetowa (Front-end)"
description: "Zadanie praktyczne przygotowujące do egzaminu zawodowego (Część II: Aplikacja Web). Implementacja formularza w React/Angular z użyciem Bootstrapa i zachowaniem zasad WCAG."
pubDate: 2026-06-10
category: "Sprawdziany"
tags: ["react", "angular", "bootstrap", "egzamin-zawodowy", "wcag"]
---

## Opis zadania

Wykonaj aplikację internetową typu front-end obsługującą formularz, wykorzystując dostępny na stanowisku egzaminacyjnym framework **Angular** lub bibliotekę **React.js**. Do zdefiniowania stylu oraz układu formularza zastosuj bibliotekę **Bootstrap**.

Aplikacja ma na celu zbieranie informacji o grach komputerowych i poprawną walidację oraz logowanie danych przy użyciu zdarzeń. 

> ### ⚠️ Ważna informacja dla zdającego
> Zadanie nie zawiera załączonych zrzutów ekranu wizualizacji interfejsu. Całość układu, powiązań elementów oraz dostępności cyfrowej należy wykonać precyzyjnie na podstawie poniższych założeń oraz wytycznych projektowych (w tym standardów WCAG).

---

## Założenia aplikacji

### 1. Struktura i komponenty
- Aplikacja składa się z **jednego, głównego komponentu formularza**.
- Interfejs formularza musi zawierać następujące elementy:
  - Pole edycyjne (tekstowe) wraz z etykietą o treści: **„Tytuł gry”**
  - Listę rozwijalną (`<select>`) wraz z etykietą o treści: **„Gatunek”**
  - Przycisk zatwierdzający o treści: **„Zapisz”**

### 2. Elementy listy rozwijalnej
Lista rozwijalna „Gatunek” musi definiować dokładnie 5 opcji wyboru (znaczniki `<option>`):
1. Opcja pusta (domyślna, zachęcająca do wyboru)
2. **FPS** – o wartości (`value`) równej `1`
3. **RPG** – o wartości (`value`) równej `2`
4. **Strategia** – o wartości (`value`) równej `3`
5. **MOBA** – o wartości (`value`) równej `4`

### 3. Stan początkowy i działanie aplikacji
- W stanie początkowym (bezpośrednio po uruchomieniu i załadowaniu strony) aplikacja wyświetla puste pole tekstowe oraz wybraną domyślną (pustą) opcję na liście rozwijalnej.
- Po kliknięciu przycisku **„Zapisz”** generowane jest zdarzenie, które pobiera dane z formularza.
- Aplikacja **nie może przeładowywać strony** przy zatwierdzaniu formularza (należy zablokować domyślną akcję `submit`).
- Dane pobrane z formularza muszą zostać wypisane w konsoli przeglądarki dokładnie w następującym formacie tekstowym:
  `tytul: [wartość_pola_tytuł]; gatunek: [wartość_pola_gatunek]`

*(Gdzie w miejscu nawiasów kwadratowych mają znaleźć się rzeczywiste dane wprowadzone lub wybrane przez użytkownika, np. `tytul: Gothic; gatunek: 2`)*.

---

## Wygląd, stylizacja i dostępność (WCAG)

1. **Formatowanie strony:** Cała strona (element `body`) musi posiadać zdefiniowany w lokalnym arkuszu stylów wewnętrzny margines: `body { padding: 20px; }`.
2. **Bootstrap:** Elementy formularza (pole tekstowe, lista rozwijalna, przycisk) muszą zostać w pełni ostylowane klasami biblioteki Bootstrap w celu zapewnienia nowoczesnego i czytelnego wyglądu (np. `form-control`, `form-select`, `btn`, `btn-primary`, `mb-3` itp.).
3. **Dostępność (WCAG):** Formularz musi spełniać podstawowe kryteria dostępności:
* Każde pole formularza musi być jednoznacznie i poprawnie powiązane z odpowiadającą mu etykietą (`<label>`) przy użyciu identyfikatorów (atrybuty `id` w polu oraz `for`/`htmlFor` w etykiecie).
* Elementy interaktywne (pole tekstowe, select, przycisk) muszą posiadać wyraźny i widoczny wskaźnik skupienia (*focus border*) podczas nawigacji za pomocą klawiatury (klawisz `Tab`).

