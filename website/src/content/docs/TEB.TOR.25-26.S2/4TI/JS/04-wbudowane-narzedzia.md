---
title: Wbudowane Narzędzia (Ułatwiacze)
description: Praca z obiektami Date i Math oraz sterowanie czasem w JavaScript.
sidebar:
  label: 4. Narzędzia (Math, Date)
---

## 📅 Czas i Data (Obiekt `Date`)
Aby w ogóle zacząć pracować z czasem, musisz najpierw "spojrzeć na zegarek". Robimy to, tworząc nowy obiekt daty.

```javascript
// Zapisuje dokładny moment (rok, miesiąc, dzień, a nawet milisekundy), 
// w którym ten kod się uruchomił.
let dzisiaj = new Date(); 
```

Mając już zmienną `dzisiaj`, możemy z niej wyciągać konkretne informacje za pomocą wbudowanych funkcji (tzw. metod).

### 🗂️ Najważniejsze funkcje (Co możemy wyciągnąć?)

- **`getFullYear()`** – Zwraca pełny, 4-cyfrowy rok (np. `2026`).
:::caution[Uwaga]
Zawsze używaj `getFullYear()`, a nie przestarzałego `getYear()`!
:::
- **`getHours()`** – Zwraca aktualną godzinę (od 0 do 23).
- **`getMinutes()`** – Zwraca minuty (od 0 do 59).
- **`getSeconds()`** – Zwraca sekundy (od 0 do 59).

### 🚨 DWIE GŁÓWNE PUŁAPKI EGZAMINACYJNE!
Egzaminatorzy uwielbiają łapać uczniów na tych dwóch rzeczach:

**1. Pułapka Miesięcy (`getMonth`)**
W JavaScript miesiące są liczone tak samo jak tablice – **zaczynają się od zera!** Styczeń to `0`, Luty to `1`, a Grudzień to `11`.
- **Rozwiązanie:** Zawsze dodawaj jedynkę (`+ 1`), jeśli chcesz wyświetlić miesiąc człowiekowi na stronie.

```javascript
let prawidlowyMiesiac = dzisiaj.getMonth() + 1;
```

**2. Pułapka Dni (`getDate` vs `getDay`)**
Nazwy tych funkcji są bardzo podobne, ale robią zupełnie co innego:
- **`getDate()`** – Zwraca **dzień miesiąca** (np. 15. dzień miesiąca). Tego używasz w 99% przypadków!
- **`getDay()`** – Zwraca **dzień tygodnia** w formie liczby (0 to Niedziela, 1 to Poniedziałek).

---

### 💻 Gotowiec na egzamin: Wyświetlanie czytelnej daty
Częstym zadaniem jest wyświetlenie daty w formacie `DD.MM.RRRR` (np. 15.05.2026). Zobacz, jak złożyć to w całość, korzystając z naszego wcześniejszego doświadczenia. Zgodnie z dobrymi praktykami dostępności, warto zadbać, by tekst na stronie od razu generował się w czytelnej formie.

```javascript
function pokazAktualnaDate() {
    let czas = new Date();
    
    // 1. Pobieramy składniki
    let rok = czas.getFullYear();
    let miesiac = czas.getMonth() + 1; // Pamiętamy o pułapce!
    let dzien = czas.getDate();        // Dzień miesiąca
    
    // 2. Łączymy wszystko w jeden tekst (konkatenacja)
    let gotowaData = dzien + "." + miesiac + "." + rok;
    
    // 3. Wyświetlamy na stronie
    document.getElementById("pole-daty").innerHTML = gotowaData;
}
```

### 🧠 Zamiana numeru na nazwę miesiąca (Trik z Tablicą)
Pamiętasz pierwszą pułapkę egzaminacyjną z datami? Funkcja `getMonth()` liczy miesiące od zera (0 to Styczeń). To pozornie utrudnienie jest tak naprawdę naszą **największą zaletą**, ponieważ Tablice (listy elementów) w JavaScript **również liczy się od zera**!

Zamiast pisać 12 razy instrukcję warunkową `if` lub `switch`, tworzymy jedną listę wszystkich miesięcy po kolei.

**Krok po kroku:**
```javascript
function pokazPolskiMiesiac() {
    let czas = new Date();
    
    // 1. Pobieramy numer miesiąca (pamiętaj: Styczeń to 0, Luty to 1, itd.)
    let numerMiesiaca = czas.getMonth(); 

    // 2. Tworzymy tablicę ze wszystkimi nazwami. 
    // "Styczeń" ma pozycję 0, więc idealnie pasuje do wyniku z getMonth!
    const nazwy = [
        "stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", 
        "lipca", "sierpnia", "września", "października", "listopada", "grudnia"
    ];

    // 3. Wyciągamy z tablicy słowo, które znajduje się pod wylosowanym numerem
    let polskaNazwa = nazwy[numerMiesiaca];
    
    // 4. Pobieramy dzień i rok do pełnego zdania
    let dzien = czas.getDate();
    let rok = czas.getFullYear();

    // Gotowe zdanie: "Dzisiaj jest 15 maja 2026 roku."
    let wynik = "Dzisiaj jest " + dzien + " " + polskaNazwa + " " + rok + " roku.";
    
    document.getElementById("pole-daty").innerHTML = wynik;
}
```

:::tip[Dlaczego to jest najlepsze rozwiązanie na egzamin?]
- Piszesz o wiele mniej kodu niż przy użyciu `switch`.
- Omijasz problem dodawania `+ 1` do miesiąca (bo indeks 0 w tablicy automatycznie wskazuje na pierwszy wyraz, czyli styczeń).
- Ten sam trik możesz zastosować do dni tygodnia! Z funkcji `getDay()` otrzymujesz cyfrę od 0 do 6, więc tworzysz po prostu tablicę: `["Niedziela", "Poniedziałek", "Wtorek", ...]` i gotowe!
:::

---

## 🧮 Zaawansowana Matematyka (Obiekt `Math`)
Czasami zwykłe dodawanie czy mnożenie to za mało. Na egzaminie często musisz wyliczyć, ile puszek farby trzeba kupić do pomalowania pokoju. Jeśli z obliczeń wyjdzie Ci `2.1` puszki, to w prawdziwym życiu musisz kupić **3 puszki**.

Zamiast pisać trudny kod, używamy wbudowanego obiektu `Math` (pisane zawsze z dużej litery!).

- **`Math.ceil(liczba)`** – (Z ang. _ceiling_ - sufit). **Zawsze zaokrągla w GÓRĘ**. To najważniejsza funkcja na egzaminie przy wyliczaniu materiałów (płytki, farba, panele).
```javascript
let wynik = 2.1;
let puszki = Math.ceil(wynik); // Wynik: 3
```

- **`Math.floor(liczba)`** – (Z ang. _floor_ - podłoga). **Zawsze zaokrągla w DÓŁ**, odcinając końcówkę.
```javascript
Math.floor(5.99); // Wynik: 5
```

- **`Math.round(liczba)`** – Standardowe zaokrąglanie, jak na lekcji matematyki (od 0.5 w górę).
```javascript
Math.round(4.4); // Wynik: 4
Math.round(4.5); // Wynik: 5
```

- **`Math.pow(podstawa, potęga)`** – Potęgowanie. Choć pamiętaj, że w nowym JS możesz też po prostu użyć dwóch gwiazdek (np. `5 ** 2`).

---

## ⏱️ Sterowanie czasem (`setTimeout` i `setInterval`)
Bardzo częstym zadaniem na egzaminie INF.03 jest stworzenie automatycznie zmieniającego się pokazu slajdów (karuzeli zdjęć) lub działającego zegara. Służą do tego dwie wbudowane funkcje, które "odmierzają czas".

:::caution[ZAPAMIĘTAJ]
W JavaScript czas zawsze podajemy w **milisekundach**.
1 sekunda = 1000 milisekund.
:::

### 💣 `setTimeout` (Bomba z opóźnionym zapłonem)
Uruchamia kod **tylko jeden raz**, po upływie zadanego czasu.

```javascript
function pokazKomunikat() {
    console.log("Minęły 3 sekundy!");
}

// Uruchom funkcję pokazKomunikat za 3000 milisekund (3 sekundy)
setTimeout(pokazKomunikat, 3000); 
```

### 🔁 `setInterval` (Bicie serca / Pętla w czasie)
Uruchamia kod **wielokrotnie**, w równych odstępach czasu. To właśnie ta funkcja napędza wszystkie automatyczne galerie zdjęć na stronach internetowych.

:::tip[Dobra praktyka WCAG]
Budując taki pokaz slajdów, niezwykle ważne jest, aby nie ustawiać czasu zmiany zdjęć na zbyt krótki. Karuzela zmieniająca obrazki co sekundę jest bardzo męcząca dla wzroku i łamie standardy dostępności. Ustawienie interwału na co najmniej 3000-5000 milisekund pozwala użytkownikom na spokojne zapoznanie się z treścią bez uczucia pośpiechu.
:::

```javascript
function zmienZdjecie() {
    // Tutaj znajdowałby się kod podmieniający źródło obrazka (src)
    console.log("Zmieniam zdjęcie na kolejne...");
}

// Uruchamiaj funkcję zmienZdjecie bez przerwy, co 4 sekundy
setInterval(zmienZdjecie, 4000);
```