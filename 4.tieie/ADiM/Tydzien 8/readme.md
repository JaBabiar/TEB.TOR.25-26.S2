# Zajęcia: Piątek 27.03.2026

Na dzisiejszych zajęciach omówiliśmy dwa kluczowe zagadnienia w JavaScript: operacje na tablicach (listach) oraz interakcję ze stroną za pomocą zdarzeń (Events) i manipulacji modelem DOM.

---

## 1. Podstawowe Funkcje List (Tablic) w JS

W JavaScript do przechowywania wielu wartości w jednej zmiennej używamy tablic. Podczas zajęć pracowaliśmy na następującym przykładzie:

```javascript
let listaDanych = ["Valorant", "CS2", "Brawl Stars", "League of Legends", "Fortnite"];
```

Poniższa tabela przedstawia najważniejsze metody, które poznaliśmy:

| Funkcja | Opis | Przykład (na naszej liście) | Wynik działania |
| :--- | :--- | :--- | :--- |
| `length` | Właściwość (nie funkcja), która zwraca aktualną liczbę elementów w tablicy. | `listaDanych.length` | `5` |
| `.pop()` | Usuwa **ostatni** element z tablicy i zwraca jego wartość. | `listaDanych.pop()` | Zwraca `"Fortnite"`. W tablicy zostają 4 gry. |
| `.push()` | Dodaje nowy element na **koniec** tablicy. | `listaDanych.push("PUBG")` | Zwraca nową długość tablicy (np. `5`). |
| `.indexOf()` | Szuka elementu w tablicy i zwraca jego pozycję (indeks). Jeśli go nie ma, zwraca `-1`. | `listaDanych.indexOf("Brawl Stars")` | `2` (Pamiętaj: indeksy liczymy od 0!) |
| `.splice()` | Służy do usuwania (i dodawania) elementów w środku tablicy. Przyjmuje argumenty: `(indeks_startowy, liczba_elementów_do_usunięcia)`. | `listaDanych.splice(2, 1)` | Zwraca usunięty element `["Brawl Stars"]`. |
| `.slice()` | Kopiuje fragment tablicy i tworzy z niego nową. Obsługuje wartości ujemne (liczenie od końca tablicy). | `listaDanych.slice(-3, -1)` | Zwraca przedział (bez ostatniego elementu). |

### Zabezpieczenie przed błędami (Obsługa brakującego elementu)

Zanim spróbujemy usunąć element przez `.splice()`, warto sprawdzić, czy on w ogóle istnieje. Służy do tego instrukcja warunkowa `if`:

```javascript
let ie = listaDanych.indexOf("Brawl Stars");

if (ie < 0) {
    console.error("Brak słowa w słowniku!");
    // Można również użyć: throw new Error("Brak słowa w Słowniku");
} else {
    listaDanych.splice(ie, 1); // Usuwa tylko wtedy, gdy element istnieje
}
```

---

## 2. Manipulacja DOM i Zdarzenia (Events)

W drugiej części zajęć ożywiliśmy naszą stronę HTML. Nauczyliśmy się, jak nasłuchiwać działań użytkownika (np. kliknięć, ruchów myszką) i reagować na nie za pomocą JavaScriptu.

### Podpinanie elementów z HTML

Aby cokolwiek zmienić na stronie, najpierw musimy "złapać" ten element w JS za pomocą jego ID:

```javascript
let kolor = document.getElementById("kolor");
let div = document.getElementById("jakisDiv");
let btn = document.getElementById("btn");
let body = document.getElementById("canvas");
```

### Rodzaje użytych zdarzeń (Event Listeners)

#### A. Zmiana Koloru (`change`)

Pozwala na reakcję w momencie, gdy użytkownik wybierze nową wartość (np. z palety kolorów):

```javascript
kolor.addEventListener("change", function(event) {
    // Przypisanie wybranego koloru z inputa jako tło naszego Diva
    div.style.background = kolor.value;
});
```

#### B. Najechanie i opuszczenie myszką (`mouseenter` / `mouseleave`)

Dzięki modyfikacji `classList` możemy dynamicznie dodawać i usuwać style CSS.

```javascript
div.addEventListener("mouseenter", function() {
    div.classList.add("show-border"); // Dodaje ramkę
});

div.addEventListener("mouseleave", function() {
    div.classList.remove("show-border"); // Zabiera ramkę
});
```

#### C. Tryb Ciemny - Kliknięcie (`click`) i przełączanie klas (`toggle`)

Funkcja `.toggle()` jest bardzo użyteczna – jeśli element posiada daną klasę, to ją usuwa, a jeśli nie posiada – to ją dodaje. Dodatkowo dynamicznie zmieniamy napis na przycisku używając `textContent`.

```javascript
btn.addEventListener("click", function() {
    body.classList.toggle("darkmode");
    
    // Zmiana tekstu przycisku w zależności od aktualnego trybu
    if (btn.textContent == "tryb ciemny") {
        btn.textContent = "tryb jasny";
    } else {
        btn.textContent = "tryb ciemny";
    }
});
```
