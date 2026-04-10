# Przygotowanie do INF 0.3

## Zmienne, Typy danych i Operatory

### Deklaracje zmiennych

- `let` (zmienna) - Używamy do wartości które mogą się zmieniać w trakcie działania programu (np. Wynik)

```js
let punkty = 0;
punkty = 10; // Wszystko w porządku, zmieniamy wartość
```

- `const` (stała) - Wartość przypisana raz, każda próba jej zmiany wyrzuci błąd, używamy do elementów które na pewno się nie zmienią (np. Pobrany element HTML)

```js
const stawkaVAT = 0.23;
const przycisk = document.getElementById("btn");
// stawkaVAT = 0.08; // BŁĄD KRYTYCZNY! Skrypt przestanie działać.
```

### Typy Danych

W języku JavaScript (i na egzaminie INF.03) pracujemy głównie na trzech podstawowych typach danych. Każdy z nich ma swoje unikalne właściwości, operatory i wbudowane funkcje.

#### Tekst (String)

Wszystko, co znajduje się w cudzysłowach `""`, apostrofach `''` lub backtickach `` ` ``. 
> **Ważne:** Pamiętaj, że dane pobierane z HTML (np. `document.getElementById('input').value`) są **zawsze** traktowane przez JS jako tekst!

**Podstawowe operacje:**

- **Łączenie (Konkatenacja):** Używamy znaku `+`.

    ```javascript
    "Ala" + " " + "ma kota" // Wynik: "Ala ma kota"
    "5" + "5" // Wynik: "55" (Złączył teksty, nie dodał liczb!)
    ```

- **Pobieranie konkretnego znaku:** Używamy nawiasów kwadratowych `[]` (liczymy od zera!).

    ```javascript
    let haslo = "Okon";
    haslo[0]; // Wynik: "O"
    haslo[2]; // Wynik: "o"
    ```

**Przydatne właściwości i funkcje (Metody):**

- `.length` – Zwraca długość tekstu (liczbę znaków). Bardzo ważne przy walidacji haseł!
 
    ```javascript
    "Egzamin".length; // Wynik: 7
    ```

- `.toLowerCase()` / `.toUpperCase()` – Zmienia wielkość liter. Przydatne, gdy chcemy porównać to, co wpisał użytkownik, ignorując 
wielkość liter.

    ```javascript
    "Polska".toLowerCase(); // Wynik: "polska"
    "Polska".toUpperCase(); // Wynik: "POLSKA"
    ```

- `.substring(od, do)` – Wycina fragment tekstu.

    ```javascript
    "Warszawa".substring(0, 4); // Wynik: "Wars" (wycina znaki od indeksu 0 do 3)
    ```

---

#### Liczba (Number)

Obejmuje zarówno liczby całkowite, jak i ułamkowe.
> **Błąd egzaminacyjny:** W ułamkach w programowaniu **zawsze używamy kropki**, a nie przecinka (np. `3.14`, nigdy `3,14`)!

**Podstawowe operacje (Matematyka):**

- `+`, `-`, `*`, `/` – Standardowe dodawanie, odejmowanie, mnożenie, dzielenie.
- `%` (Modulo) – Reszta z dzielenia. Klasyk egzaminacyjny do sprawdzania, czy liczba jest parzysta.

    ```javascript
    10 % 2; // Wynik: 0 (liczba parzysta)
    11 % 2; // Wynik: 1 (liczba nieparzysta)
    ```

- `**` (Potęgowanie) – Zastępuje starsze `Math.pow()`.

    ```javascript
    3 ** 2; // Wynik: 9
    ```

**Przydatne funkcje i konwersja:**

- `parseInt(tekst)` – Zamienia tekst na liczbę całkowitą (odcina ułamki i litery na końcu). **Używaj tego zawsze do pobierania liczb z formularza!**

    ```javascript
    parseInt("15"); // Wynik: 15
    parseInt("15.99"); // Wynik: 15 (ucięło ułamek)
    parseInt("15px"); // Wynik: 15 (ucięło tekst)
    ```

- `parseFloat(tekst)` – Zamienia tekst na liczbę zmiennoprzecinkową (zachowuje ułamki).

    ```javascript
    parseFloat("15.99"); // Wynik: 15.99
    ```

- `.toFixed(miejsca)` – Zaokrągla liczbę do podanej ilości miejsc po przecinku (przydatne przy wyświetlaniu cen!). Zwraca wynik jako tekst.

    ```javascript
    let cena = 10.5678;
    cena.toFixed(2); // Wynik: "10.57"
    ```

---

#### Wartość logiczna (Boolean)

Najprostszy typ danych. Przyjmuje tylko dwie wartości: `true` (prawda) lub `false` (fałsz). Jest to wynik każdego porównania i fundament instrukcji warunkowych (If/Else).

**Podstawowe operacje (Operatory Porównania):**

- `>` (większe), `<` (mniejsze), `>=` (większe lub równe), `<=` (mniejsze lub równe).
- `==` (Równe) – Sprawdza, czy wartości są takie same (ignoruje typ danych).

    ```javascript
    5 == "5"; // Wynik: true (JS sam zamienił tekst na liczbę do porównania)
    ```

- `===` (Identyczne) – **Zalecane na egzaminie.** Sprawdza, czy wartości ORAZ typy danych są takie same.

    ```javascript
    5 === "5"; // Wynik: false (Liczba to nie to samo co Tekst)
    ```

- `!=` (Różne) oraz `!==` (Absolutnie różne).

**Podstawowe operacje (Operatory Logiczne):**
Pozwalają łączyć wiele warunków w jeden.

- `&&` (Logiczne ORAZ / AND) – Oba warunki muszą być prawdziwe.

    ```javascript
    (wiek >= 18) && (kartaRowerowa == true)
    ```

- `||` (Logiczne LUB / OR) – Wystarczy, że jeden warunek jest prawdziwy.

    ```javascript
    (dzien == "Sobota") || (dzien == "Niedziela")
    ```

- `!` (Logiczne NIE / NOT) – Odwraca wartość.

    ```javascript
    !true // Wynik: false
    ```
