---
title: Podstawy Responsywnego Designu
description: podstawowe informacje z przykładowym zadaniem
sidebar:
  label: 6. Materialy JS
---

## 📦 Zmienne (Pudełka na dane)
Zmienne to po prostu pojemniki, w których trzymamy informacje.

- **`let` (zmienna)** – Używaj do wartości, które **będą się zmieniać** (np. wynik w grze, cena po rabacie).

```javascript
let punkty = 0;
punkty = 10; // Zmieniamy wartość na 10 - wszystko działa!
```

- **`const` (stała)** – Używaj do wartości, które **nigdy się nie zmienią** (np. pobrany element HTML, stawka podatku).

```javascript
const przycisk = document.getElementById("btn");
// przycisk = 5; // 🛑 BŁĄD! Program przestanie działać.
```

---

## 🧩 Typy Danych i Operatory
Na egzaminie pracujesz głównie na trzech rodzajach informacji.

### 📝 Tekst (String)

Wszystko, co jest w cudzysłowach `""` lub apostrofach `''`.

:::caution[ZAPAMIĘTAJ]
Dane wpisane przez użytkownika na stronie (z pola `input`) to **zawsze tekst**, nawet jeśli wpisze tam cyfrę!
:::

- **Łączenie tekstów (`+`):**

```javascript
"5" + "5" // Wynik: "55" (Skleił teksty, nie dodał matematycznie!)
```

- **`.length`** – Liczy, ile znaków ma tekst (przydatne przy sprawdzaniu długości hasła).

```javascript
"Egzamin".length; // Wynik: 7
```

- **Wielkość liter:**

```javascript
"Polska".toLowerCase(); // Wynik: "polska" (małe litery)
"Polska".toUpperCase(); // Wynik: "POLSKA" (DUŻE LITERY)
```

### 🔢 Liczba (Number)

:::danger[BŁĄD EGZAMINACYJNY]
W ułamkach **zawsze używamy kropki**, a nie przecinka (pisz `3.14`, nigdy `3,14`).
:::

- **Matematyka:** `+` (dodawanie), `-` (odejmowanie), `*` (mnożenie), `/` (dzielenie).
- **`%` (Modulo)** – Reszta z dzielenia. Super do sprawdzania, czy liczba jest parzysta.

```javascript
10 % 2; // Wynik: 0 (liczba jest parzysta)
11 % 2; // Wynik: 1 (liczba jest nieparzysta)
```

- **Zmiana tekstu w liczbę (Bardzo ważne na egzaminie!):**
    - `parseInt(tekst)` – Zwraca liczbę całkowitą (odcina ułamki).
    - `parseFloat(tekst)` – Zwraca liczbę z ułamkiem.

```javascript
parseInt("15px"); // Wynik: 15
parseFloat("15.99"); // Wynik: 15.99
```

### ⚖️ Wartość Logiczna (Boolean)
Odpowiada tylko: **Prawda (`true`)** albo **Fałsz (`false`)**.

- `===` (Identyczne) – Sprawdza, czy wartości są **dokładnie takie same**. Używaj tego zamiast `==`.

```javascript
5 === 5;   // Wynik: true
5 === "5"; // Wynik: false (liczba to nie to samo co tekst!)
```

- `!==` (Różne) – Sprawdza, czy wartości się różnią.
- **Łączenie warunków:**
    - `&&` (ORAZ) – Oba warunki muszą być spełnione.
    - `||` (LUB) – Wystarczy, że jeden warunek jest spełniony.
  

## 🚦 Instrukcje Warunkowe (Podejmowanie decyzji)

## 🛡️ Guard Clause (Klauzula Strażnicza / Wczesny powrót)

**Guard Clause** to technika pisania kodu, w której błędy i niechciane sytuacje odrzucamy na samej górze funkcji. Jeśli "strażnik" wykryje problem, natychmiast wyrzuca nas z funkcji za pomocą słowa `return`.

Wyobraź sobie bramkarza w klubie. Zamiast zapraszać Cię do środka, prowadzić na parkiet i dopiero tam sprawdzać, czy masz bilet, sprawdza go na samym wejściu. Brak biletu? Od razu wracasz do domu (`return`).

### ❌ Jak wygląda kod BEZ Guard Clause (Piramida Zagłady)

Tradycyjne pisanie kodu często prowadzi do tworzenia tzw. "piramidy". Główny kod przesuwa się coraz bardziej w prawo, co jest bardzo trudne do czytania i łatwo zgubić zamykający nawias klamrowy `}`.

```javascript
function obliczZnizke(wiek) {
    let wynik = "";
    
    // Sprawdzamy, czy w ogóle podano wiek
    if (wiek !== "") {
        // Sprawdzamy, czy wpisano liczbę
        if (!isNaN(wiek)) {
            // GŁÓWNY KOD
            wynik = "Przyznano zniżkę na podstawie wieku: " + wiek;
        } else {
            wynik = "Błąd: To nie jest liczba!";
        }
    } else {
        wynik = "Błąd: Pole jest puste!";
    }
    
    return wynik;
}
```

### ✅ Jak wygląda kod Z Guard Clause (Płaski i czytelny)

Tutaj stosujemy podejście odwrócone. Szukamy błędów, a do odwracania warunków używamy wykrzyknika `!`. Znak `!` oznacza zaprzeczenie (np. `!wiek` czytamy jako "jeśli NIE MA wieku").

```javascript
function obliczZnizke(wiek) {
    
    // 🛑 STRAŻNIK 1: Czy pole jest puste?
    if (!wiek) {
        return "Błąd: Pole jest puste!"; // Od razu przerywamy funkcję
    }

    // 🛑 STRAŻNIK 2: Czy to NIE jest liczba?
    if (isNaN(wiek)) {
        return "Błąd: To nie jest liczba!"; // Znowu przerywamy
    }

    // ✅ GŁÓWNY KOD: Skoro żaden strażnik nas nie wyrzucił,
    // to znaczy, że wszystko jest w 100% poprawne.
    // Piszemy główny kod na samym dole, bez żadnych zagnieżdżeń!
    
    return "Przyznano zniżkę na podstawie wieku: " + wiek;
}
```

Każdy program musi wiedzieć, co zrobić w zależności od sytuacji. Wyobraź to sobie jako **bramkarza w klubie** lub **kasjera w kinie**, który zadaje pytanie i na podstawie odpowiedzi podejmuje decyzję.

### ⚖️ Konstrukcja `if / else` (Jeśli / W przeciwnym razie)

To najprostszy sposób podejmowania decyzji. Mamy tylko dwie drogi: Prawda albo Fałsz.

```javascript
let wiek = 18;

if (wiek >= 18) {
    
    // ✅ Droga 1: Co ma się stać, jeśli warunek to PRAWDA
    console.log("Wchodzisz, jesteś pełnoletni!");

} else {
    
    // ❌ Droga 2: W przeciwnym razie (jeśli to FAŁSZ)
    console.log("Stop, jesteś niepełnoletni!");

}
```

### 🔀 Konstrukcja `else if` (A jeśli jednak...)

Czasami dwie opcje to za mało. Chcemy sprawdzić kilka rzeczy po kolei. Używamy do tego `else if`. 
Program sprawdza warunki z góry na dół. **Zatrzyma się od razu, gdy znajdzie pierwszą pasującą Prawdę.**

```javascript
let punkty = 85;

if (punkty >= 90) {
    // Pierwsze sprawdzenie
    console.log("Dostajesz ocenę: 5");

} else if (punkty >= 75) {
    // Jeśli pierwsze to fałsz, sprawdź to
    console.log("Dostajesz ocenę: 4");

} else {
    // Jeśli nic wcześniej nie pasowało (wyjście awaryjne)
    console.log("Dostajesz ocenę: 2");
}
```

### 🔑 Zrozumienie wykrzyknika (`!`)

W Guard Clause wykrzyknik to Twój najlepszy przyjaciel. W języku JavaScript pusty tekst `""`, liczba `0`, a także wartości `null` i `undefined` są traktowane jako "fałszywe" (falsy).

Zatem zapis:

```javascript
if (!wartosc) { return; }
```

Działa jak uniwersalna pułapka. Oznacza: _"Jeśli zmienna 'wartosc' jest pusta, ma zero, albo w ogóle jej nie zdefiniowano – natychmiast przerwij"_. To najkrótszy i najszybszy sposób na zabezpieczenie pola w formularzu przed złośliwym lub zapominalskim użytkownikiem.

## 🌐 Praca z HTML (DOM) – Najważniejsze na INF.03!
To jest klucz do zdania egzaminu. Musisz umieć połączyć kod JavaScript z elementami na stronie internetowej (HTML).

### 📥 KROK 1: Pobieranie elementów z HTML
Używamy do tego identyfikatorów (`id`), które są przypisane do tagów w HTML.

```javascript
// Szuka w HTML elementu z id="wynik" i zapisuje go w zmiennej
const poleWyniku = document.getElementById("wynik");
```

### ✍️ KROK 2: Zmiana tego, co widać na stronie
- **`.innerHTML`** – Zmienia tekst pomiędzy tagami (np. wewnątrz akapitu `<p>TUTAJ</p>`).

```javascript
poleWyniku.innerHTML = "Twój wynik to 100!";
```

- **`.value`** – Odczytuje to, co użytkownik wpisał w pole tekstowe (input).

:::caution[ZAPAMIĘTAJ]
Dane wpisane przez użytkownika na stronie (z pola `input`) to **zawsze tekst**, nawet jeśli wpisze tam cyfrę! Pamiętaj o konwersji na liczbę, jeśli pobierasz wartość do obliczeń matematycznych.
:::

```javascript
let wpisanaWartosc = parseInt(document.getElementById("liczba1").value);
```

### 🎧 Nowoczesne podejście – `addEventListener`

Do tej pory używaliśmy zdarzeń dopisywanych bezpośrednio w HTML (np. `<button onclick="oblicz()">`). W nowoczesnym programowaniu stosujemy **`addEventListener`** (czyli "Dodaj Nasłuchiwacza Zdarzeń"). To profesjonalny standard.

**Dlaczego to jest lepsze?**

1. **Porządek:** Oddzielamy wygląd (HTML) od logiki (JavaScript). Plik HTML jest czysty, nie ma w nim kodu JS.
2. **Więcej możliwości:** Możemy podpiąć kilka różnych funkcji pod jedno kliknięcie.

**Jak to wygląda w praktyce?**
Schemat jest zawsze taki sam: `Kto ma słuchać.addEventListener("jakie zdarzenie", jakaFunkcja)`

```javascript
// 1. Znajdujemy przycisk w HTML
const mojPrzycisk = document.getElementById("btn-oblicz");

// 2. Tworzymy funkcję, która ma się wykonać
function pokazWynik() {
    console.log("Przycisk został kliknięty!");
}

// 3. Dodajemy nasłuchiwacza do przycisku
mojPrzycisk.addEventListener("click", pokazWynik); 
// UWAGA: podajemy nazwę zdarzenia BEZ "on" (piszemy "click", a nie "onclick")!
```

### 🚨 Pułapka Egzaminacyjna! `submit` vs `click` w formularzach

To jest miejsce, w którym najwięcej osób traci punkty na egzaminie. Formularze (`<form>`) rządzą się swoimi prawami. Wyobraź sobie, że masz formularz z przyciskiem `<button type="submit">Wyślij</button>`.

#### ❌ Złe podejście: Nasłuchiwanie na `click` (na przycisku)

Jeśli założysz nasłuchiwacz `click` na samym przycisku, sprawdzisz tylko, czy ktoś kliknął myszką.

- **Problem:** Jeśli użytkownik wpisze dane i wciśnie klawisz **Enter** na klawiaturze (co jest naturalne i wymagane przez standardy dostępności WCAG), Twój kod na kliknięcie w ogóle się nie uruchomi!

#### ✅ Dobre podejście: Nasłuchiwanie na `submit` (na całym formularzu)

Zdarzenie `submit` przypinamy do **całego tagu `<form>`**, a nie do przycisku. Dzięki temu reagujemy na sam fakt wysyłania formularza – nieważne, czy ktoś kliknął przycisk myszką, czy wcisnął "Enter".

:::danger[NAJWAŻNIEJSZA RZECZ PRZY SUBMIT]
Domyślnie, gdy wyślesz formularz, przeglądarka odświeża całą stronę. W zadaniach z JavaScriptu **nie chcemy tego**, bo stracimy nasze obliczenia! Musimy to zablokować za pomocą magicznego zaklęcia: **`event.preventDefault()`** (czyli "zapobiegnij domyślnemu zachowaniu").
:::

**Zobaczmy to na przykładzie (łączymy submit i Guard Clause):**

```javascript
// Łapiemy CAŁY formularz (nie sam przycisk!)
const formularz = document.getElementById("moj-formularz");

// Zauważ parametr 'event' (lub 'e') w nawiasie funkcji!
formularz.addEventListener("submit", function(event) {
    
    // 🛑 1. MAGIA: Blokujemy odświeżanie strony!
    event.preventDefault(); 

    // Pobieramy wpisane imię
    let imie = document.getElementById("pole-imie").value;

    // 🛑 2. STRAŻNIK (Wczesny powrót)
    if (!imie) {
        console.log("Błąd: Musisz podać imię!");
        return; // Przerywamy działanie
    }

    // ✅ 3. Jeśli dotarliśmy tutaj, formularz jest wypełniony poprawnie
    console.log("Formularz wysłany pomyślnie. Cześć " + imie + "!");
});
```
