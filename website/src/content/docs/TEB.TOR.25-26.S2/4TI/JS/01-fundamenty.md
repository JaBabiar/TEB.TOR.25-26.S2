---
title: Fundamenty (Podstawy budowania)
description: Zmienne, typy danych i operatory w JavaScript - najważniejsze podstawy przed egzaminem INF.03.
sidebar:
  label: 1. Fundamenty
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