## Spis Treści 
### 🧱 Część 1: Fundamenty (Podstawy budowania) 
* [1. Zmienne (Pudełka na dane)](#dzial-1) 
* [2. Typy Danych i Operatory](#dzial-2) 
### 🧠 Część 2: Logika i Struktura Programu 
* [3. Instrukcje Warunkowe (Podejmowanie decyzji)](#dzial-3) 
* [4. Pętle (Powtarzanie czynności)](#dzial-4)
* [5. Tablice (Listy elementów)](#dzial-5) 
* [6. Funkcje (Twoje własne maszyny)](#dzial-6) 
* [9. Guard Clause (Klauzula Strażnicza / Wczesny powrót)](#dzial-9)  
### 🌐 Część 3: Interakcja ze Stroną (HTML i DOM) 
* [7. Praca z HTML (DOM) – Najważniejsze na INF.03!](#dzial-7) 
* [8. Zdarzenia (Events) – Jak strona reaguje na użytkownika](#dzial-8) 
* [14. Pola wyboru (Checkboxy i Radio) – .checked](#dzial-14) 
* [13. Nowoczesna zmiana wyglądu (classList)](#dzial-13) 
### 🛠️ Część 4: Wbudowane Narzędzia (Ułatwiacze) 
* [10. Czas i Data (Obiekt Date)](#dzial-10) 
* [11. Zaawansowana Matematyka (Obiekt Math)](#dzial-11) 
* [12. Sterowanie czasem (setTimeout i setInterval)](#dzial-12) 
### 🐛 Część 5: Rozwiązywanie Problemów 
* [15. Szukanie błędów (Ratunek na egzaminie: console.log)](#dzial-15) 
* ---
## 📦<a id="dzial-1"></a>1. Zmienne (Pudełka na dane)
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
## 🧩<a id="dzial-2"></a> 2. Typy Danych i Operatory
Na egzaminie pracujesz głównie na trzech rodzajach informacji.
### 📝 Tekst (String)

Wszystko, co jest w cudzysłowach `""` lub apostrofach `''`.

> ⚠️ **ZAPAMIĘTAJ:** Dane wpisane przez użytkownika na stronie (z pola `input`) to **zawsze tekst**, nawet jeśli wpisze tam cyfrę!
- **Łączenie tekstów (`+`):**
```javascript
"5" + "5" // Wynik: "55" (Skleił teksty, nie dodał matematycznie!)
```
- **`.length`** – Liczy, ile znaków ma tekst (przydatne przy sprawdzaniu długości hasła).
    JavaScript
```javascript
"Egzamin".length; // Wynik: 7
```
- **Wielkość liter:**
```javascript
"Polska".toLowerCase(); // Wynik: "polska" (małe litery)
"Polska".toUpperCase(); // Wynik: "POLSKA" (DUŻE LITERY)
```
### 🔢 Liczba (Number)

> 🛑 **BŁĄD EGZAMINACYJNY:** W ułamkach **zawsze używamy kropki**, a nie przecinka (pisz `3.14`, nigdy `3,14`).
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

---
## 🚦<a id="dzial-3"></a>3. Instrukcje Warunkowe (Podejmowanie decyzji)
Program musi wiedzieć, co zrobić w zależności od sytuacji.
### Konstrukcja `if / else` (Jeśli / W przeciwnym razie)
```javascript
let wiek = 18;

if (wiek >= 18) {
// Co ma się stać, jeśli warunek to PRAWDA
	console.log("Jesteś pełnoletni");
} else {
// Co ma się stać, jeśli warunek to FAŁSZ
	console.log("Jesteś niepełnoletni");
}
```

### Konstrukcja `switch` (Wybór z wielu opcji)
Przydatna, gdy sprawdzasz jedną zmienną pod kątem wielu konkretnych wartości (np. wybór usługi u fryzjera).
```javascript
let usluga = 2;

switch (usluga) {
    case 1:
        cena = 50; // Jeśli usluga to 1
        break;     // Zatrzymaj sprawdzanie!
    case 2:
        cena = 100; // Jeśli usluga to 2
        break;
    default:
        cena = 0;   // W każdym innym przypadku
}
```

---
## 🔄<a id="dzial-4"></a> 4. Pętle (Powtarzanie czynności)
Zamiast pisać ten sam kod 100 razy, używamy pętli.
### Pętla `for`
Najczęściej używana. Składa się z 3 części: (start; warunek działania; krok).
```javascript
// Wypisze w konsoli liczby od 1 do 5
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
```

---
## 📚<a id="dzial-5"></a> 5. Tablice (Listy elementów)
Tablica to jedna zmienna, która trzyma wiele wartości naraz (np. listę ocen). Zaczynamy liczyć od **zera**!
``` javascript
let oceny = [5, 4, 3, 5];

oceny[0]; // Wynik: 5 (pierwszy element)
oceny[2]; // Wynik: 3 (trzeci element)
```
- **`.push(wartość)`** – Dodaje nowy element na sam koniec tablicy.
- **`.length`** – Zwraca liczbę elementów w tablicy.
---
## ⚙️<a id="dzial-6"></a> 6. Funkcje (Twoje własne maszyny)
Funkcja to blok kodu, który coś robi, ale uruchamia się dopiero wtedy, kiedy go **wywołasz** (np. po kliknięciu przycisku).
```javascript
// Budujemy funkcję
function powitanie(imie) {
    let wynik = "Cześć " + imie;
    return wynik; // "Zwróć" wynik na zewnątrz
}

// Uruchamiamy funkcję
powitanie("Jan"); // Wynik: "Cześć Jan"
```

---
## 🌐<a id="dzial-7"></a> 7. Praca z HTML (DOM) – Najważniejsze na INF.03!
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
- **`.value`** – Odczytuje to, co użytkownik wpisał w pole tekstowe (input). **Pamiętaj o konwersji na liczbę!**
```javascript
let wpisanaWartosc = parseInt(document.getElementById("liczba1").value);
```
### 🎨 KROK 3: Zmiana wyglądu (Stylów CSS) z poziomu JS
Zamiast pisać myślniki (jak w CSS: `background-color`), w JavaScript łączymy słowa i piszemy drugie z dużej litery (tzw. camelCase: `backgroundColor`).
```javascript
poleWyniku.style.backgroundColor = "red"; // Zmienia tło na czerwone
poleWyniku.style.fontSize = "20px";       // Zmienia wielkość czcionki
```

## 🖱️<a id="dzial-8"></a> 8. Zdarzenia (Events) – Jak strona reaguje na użytkownika

Zdarzenia to sygnały, które przeglądarka wysyła, gdy coś się dzieje na stronie (ktoś kliknął, wpisał tekst, najechał myszką). Nasz kod JavaScript może tych sygnałów **nasłuchiwać** i na nie reagować.
### 🌟 Część 1: Najważniejsze Zdarzenia (Lista Przebojów)
Oto zdarzenia, które najczęściej pojawiają się na egzaminach i w codziennej pracy:
**Zdarzenia Myszy:**
- `click` – Pojedyncze kliknięcie (najpopularniejsze).
- `dblclick` – Podwójne kliknięcie.
- `mouseenter` / `mouseleave` – Nowocześniejsze wersje `mouseover` i `mouseout`. Reagują, gdy kursor "wchodzi" na element i z niego "schodzi".
**Zdarzenia Klawiatury (Ważne dla dostępności - WCAG!):**
- `keydown` – Użytkownik wciska klawisz (np. przydatne do zrobienia sterowania w prostej grze).
- `keyup` – Użytkownik puszcza klawisz (często używane do sprawdzania hasła na żywo, zaraz po wpisaniu literki).
**Zdarzenia Formularzy:**
- `focus` – Użytkownik wszedł w pole tekstowe (np. kliknął w nie, żeby zacząć pisać).
- `blur` – Użytkownik wyszedł z pola tekstowego.
- `input` – Reaguje na **każdą** zmianę w polu tekstowym w czasie rzeczywistym (lepsze niż `keyup` dla formularzy).
- `change` – Reaguje na zmianę, ale dopiero po zatwierdzeniu (np. po wybraniu innej opcji z rozwijanej listy `<select>`).
### 🎧 Część 2: Nowoczesne podejście – `addEventListener`
Do tej pory używaliśmy zdarzeń dopisywanych bezpośrednio w HTML (np. `<button onclick="oblicz()">`).

W nowoczesnym programowaniu stosujemy **`addEventListener`** (czyli "Dodaj Nasłuchiwacza Zdarzeń"). To profesjonalny standard.
**Dlaczego to jest lepsze?**
1. **Porządek:** Oddzielamy wygląd (HTML) od logiki (JavaScript). Plik HTML jest czysty, nie ma w nim kodu JS.
2. **Więcej możliwości:** Możemy podpiąć kilka różnych funkcji pod jedno kliknięcie.

**Jak to wygląda w praktyce?**
Schemat jest zawsze taki sam: `Kto ma słuchać . addEventListener ( "jakie zdarzenie" , jakaFunkcja )`
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
### 🚨 Część 3: Pułapka Egzaminacyjna! `submit` vs `click` w formularzach
To jest miejsce, w którym najwięcej osób traci punkty na egzaminie. Formularze (`<form>`) rządzą się swoimi prawami.

Wyobraź sobie, że masz formularz z przyciskiem `<button type="submit">Wyślij</button>`.
#### ❌ Złe podejście: Nasłuchiwanie na `click` (na przycisku)

Jeśli założysz nasłuchiwacz `click` na samym przycisku, sprawdzisz tylko, czy ktoś kliknął myszką.

- **Problem:** Jeśli użytkownik wpisze dane i wciśnie klawisz **Enter** na klawiaturze (co jest naturalne i wymagane przez standardy dostępności WCAG), Twój kod na kliknięcie w ogóle się nie uruchomi!
#### ✅ Dobre podejście: Nasłuchiwanie na `submit` (na całym formularzu)
Zdarzenie `submit` przypinamy do **całego tagu `<form>`**, a nie do przycisku.

Dzięki temu reagujemy na sam fakt wysyłania formularza – nieważne, czy ktoś kliknął przycisk myszką, czy wcisnął "Enter".

**Najważniejsza rzecz przy zdarzeniu `submit`:**

Domyślnie, gdy wyślesz formularz, przeglądarka odświeża całą stronę. W zadaniach z JavaScriptu **nie chcemy tego**, bo stracimy nasze obliczenia! Musimy to zablokować za pomocą magicznego zaklęcia: **`event.preventDefault()`** (czyli "zapobiegnij domyślnemu zachowaniu").

**Zobaczmy to na przykładzie (łączymy `submit` ):**

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

## 🛡️<a id="dzial-9"></a> 9. Guard Clause (Klauzula Strażnicza / Wczesny powrót)

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

### 🧠 Dlaczego na egzaminie to absolutny strzał w dziesiątkę?
- **Brak zagubionych nawiasów:** W podejściu Guard Clause nawiasy się nie nawarstwiają. Znacznie trudniej o głupi błąd składniowy, przez który skrypt nie chce działać.
- **Czytelność:** Twój mózg nie musi analizować skomplikowanych gałęzi `if/else`. Czytasz kod linijka po linijce, z góry na dół. Zmniejsza to obciążenie poznawcze, co idealnie wpisuje się w standardy budowania zrozumiałych, dostępnych systemów (zarówno dla twórcy, jak i innych programistów).
- **Skupienie na głównej logice:** Od razu widać, gdzie kończy się sprawdzanie błędów, a gdzie zaczyna się właściwe obliczanie zadania egzaminacyjnego.
### 🔑 Zrozumienie wykrzyknika (`!`)

W Guard Clause wykrzyknik to Twój najlepszy przyjaciel. W języku JavaScript pusty tekst `""`, liczba `0`, a także wartości `null` i `undefined` są traktowane jako "fałszywe" (falsy).

Zatem zapis:

```javascript
if (!wartosc) { return; }
```

Działa jak uniwersalna pułapka. Oznacza: _"Jeśli zmienna 'wartosc' jest pusta, ma zero, albo w ogóle jej nie zdefiniowano – natychmiast przerwij"_. To najkrótszy i najszybszy sposób na zabezpieczenie pola w formularzu przed złośliwym lub zapominalskim użytkownikiem.
## 📅<a id="dzial-10"></a> 10. Czas i Data (Obiekt `Date`)

Aby w ogóle zacząć pracować z czasem, musisz najpierw "spojrzeć na zegarek". Robimy to, tworząc nowy obiekt daty.
```javascript
// Zapisuje dokładny moment (rok, miesiąc, dzień, a nawet milisekundy), 
// w którym ten kod się uruchomił.
let dzisiaj = new Date(); 
```

Mając już zmienną `dzisiaj`, możemy z niej wyciągać konkretne informacje za pomocą wbudowanych funkcji (tzw. metod).
### 🗂️ Najważniejsze funkcje (Co możemy wyciągnąć?)
- **`getFullYear()`** – Zwraca pełny, 4-cyfrowy rok (np. `2026`).
    > ⚠️ **Uwaga:** Zawsze używaj `getFullYear()`, a nie przestarzałego `getYear()`!
- **`getHours()`** – Zwraca aktualną godzinę (od 0 do 23).
- **`getMinutes()`** – Zwraca minuty (od 0 do 59).
- **`getSeconds()`** – Zwraca sekundy (od 0 do 59).
### 🚨 DWIE GŁÓWNE PUŁAPKI EGZAMINACYJNE!
Egzaminatorzy uwielbiają łapać uczniów na tych dwóch rzeczach:
**1. Pułapka Miesięcy (`getMonth`)**
W JavaScript miesiące są liczone tak samo jak tablice – **zaczynają się od zera!**
Styczeń to `0`, Luty to `1`, a Grudzień to `11`.
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

Częstym zadaniem jest wyświetlenie daty w formacie `DD.MM.RRRR` (np. 15.05.2026). Zobacz, jak złożyć to w całość, korzystając z naszego wcześniejszego doświadczenia.

Zgodnie z dobrymi praktykami dostępności, warto zadbać, by tekst na stronie od razu generował się w czytelnej formie.
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
### Zamiana numeru na nazwę miesiąca (Trik z Tablicą)
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

**Dlaczego to jest najlepsze rozwiązanie na egzamin?**
- Piszesz o wiele mniej kodu niż przy użyciu `switch`.
- Omijasz problem dodawania `+ 1` do miesiąca (bo indeks 0 w tablicy automatycznie wskazuje na pierwszy wyraz, czyli styczeń).
- Ten sam trik możesz zastosować do dni tygodnia! Z funkcji `getDay()` otrzymujesz cyfrę od 0 do 6, więc tworzysz po prostu tablicę: `["Niedziela", "Poniedziałek", "Wtorek", ...]` i gotowe!
## 🧮<a id="dzial-11"></a> 11. Zaawansowana Matematyka (Obiekt `Math`)

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
- **`Math.pow(podstawa, potęga)`** – Potęgowanie. Choć pamiętaj, że w nowym JS możesz też po prostu użyć dwóch gwiazdek (np. `5 2`).
## ⏱️<a id="dzial-12"></a> 12. Sterowanie czasem (`setTimeout` i `setInterval`)

Bardzo częstym zadaniem na egzaminie INF.03 jest stworzenie automatycznie zmieniającego się pokazu slajdów (karuzeli zdjęć) lub działającego zegara. Służą do tego dwie wbudowane funkcje, które "odmierzają czas".

> ⚠️ **ZAPAMIĘTAJ:** W JavaScript czas zawsze podajemy w **milisekundach**.
> 
> 1 sekunda = 1000 milisekund.
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

Budując taki pokaz slajdów, niezwykle ważne jest, aby nie ustawiać czasu zmiany zdjęć na zbyt krótki. Karuzela zmieniająca obrazki co sekundę jest bardzo męcząca dla wzroku i łamie standardy dostępności WCAG. Ustawienie interwału na co najmniej 3000-5000 milisekund pozwala użytkownikom na spokojne zapoznanie się z treścią bez uczucia pośpiechu.
```javascript
function zmienZdjecie() {
    // Tutaj znajdowałby się kod podmieniający źródło obrazka (src)
    console.log("Zmieniam zdjęcie na kolejne...");
}

// Uruchamiaj funkcję zmienZdjecie bez przerwy, co 4 sekundy
setInterval(zmienZdjecie, 4000);
```

## 👗<a id="dzial-13"></a> 13. Nowoczesna zmiana wyglądu (`classList`)

### 🎨 KROK 1: Przygotowanie "ubrania" w CSS

Najpierw w pliku ze stylami tworzymy gotową klasę. Zadbajmy od razu o dobry kontrast (jasnożółty tekst na czarnym tle), co jest świetną praktyką ułatwiającą czytanie!

```css
/* Plik CSS */
.wysoki-kontrast {
    background-color: #000000;
    color: #ffff00;
    font-size: 24px;
}
```
### ⚙️ KROK 2: Przebieranie elementu w JavaScript
Kiedy mamy pobrany element z HTML, możemy użyć na nim właściwości `classList` oraz jednej z trzech superprzydatnych funkcji:
- **`.add("nazwa")`** – Dodaje klasę (zakłada ubranie).
- **`.remove("nazwa")`** – Usuwa klasę (zdejmuje ubranie).
- **`.toggle("nazwa")`** – **Przełącznik!** To absolutny hit na egzaminie. Działa jak włącznik światła. Jeśli element NIE MA klasy, to ją doda. Jeśli ją MA, to ją zdejmie.

> ⚠️ **Ważne:** W nawiasach wpisujemy samą nazwę klasy, **BEZ kropki na początku!**
### 💻 Gotowiec na egzamin: Przycisk zmiany motywu

Poniżej bardzo popularne zadanie – przycisk, który po kliknięciu zmienia całą stronę w tryb przyjazny dla osób niedowidzących, a po ponownym kliknięciu wraca do normalnego wyglądu. Z użyciem `toggle` to banalnie proste!
```javascript
function zmienMotyw() {
    // 1. Łapiemy całe ciało strony (tag <body>)
    const strona = document.getElementById("cialo-strony");

    // 2. Używamy przełącznika! 
    // Jedna linijka kodu załatwia nam sprawdzanie, czy klasa już tam jest.
    strona.classList.toggle("wysoki-kontrast");
}
```
**Dlaczego warto to stosować na INF.03?**
1. Kod JS jest krótki i czysty.
2. Wygląd (CSS) i działanie (JS) są od siebie oddzielone.
3. Zrobienie trybu "Dark Mode" lub "Wysoki Kontrast" zajmuje dosłownie jedną linijkę, a bardzo często pojawia się w arkuszach egzaminacyjnych.
Jako **Dział 14** idealnie sprawdzi się temat, na którym "wykłada się" mnóstwo osób na egzaminie, czyli **obsługa Checkboxów i Radio buttonów** (pól wyboru).

Wcześniej uczyliśmy się, że żeby pobrać tekst z pola wpisywania, używamy `.value`. Jednak na egzaminie w niemal każdym zadaniu jest jakiś "haczyk" w postaci ptaszka do zaznaczenia (np. _"Dolicz 50 zł, jeśli użytkownik zaznaczył opcję 'Wniesienie mebli'"_).

Tutaj `.value` nie zadziała w sposób, jakiego oczekujesz. Musimy użyć innej, bardzo prostej właściwości.
## ☑️<a id="dzial-14"></a> 14. Pola wyboru (Checkboxy i Radio) – `.checked`
Kiedy masz do czynienia z kwadratowym okienkiem do zaznaczania (Checkbox) lub okrągłym polem wyboru (Radio), nie interesuje Cię to, co jest w nim napisane. Interesuje Cię tylko jedno: **Czy jest zaznaczone, czy nie?**

Do sprawdzania tego używamy właściwości **`.checked`** (z ang. _zaznaczony_).

Zwraca ona nam tylko dwie odpowiedzi, które już świetnie znasz (Wartości logiczne z działu 2):
- **`true`** (Prawda) – pole jest zaznaczone.
- **`false`** (Fałsz) – pole jest puste.
### 💡 KROK 1: Jak to zapisać?
Zamiast pisać długie sprawdzanie typu `if (pole.checked === true)`, w JavaScript możemy to skrócić. Sama nazwa zmiennej wewnątrz nawiasów `if` wystarczy!
```javascript
const opcjaDostawy = document.getElementById("dostawa");

// Czytamy to jako: "Jeśli opcjaDostawy jest zaznaczona..."
if (opcjaDostawy.checked) {
    console.log("Doliczam koszty dostawy!");
} else {
    console.log("Odbiór osobisty - za darmo.");
}
```

### 💻 Gotowiec na egzamin: Obliczanie ceny z dodatkiem
Połączmy teraz naszą wiedzę o wczesnym powrocie (Guard Clause), matematyce i checkboxach. To absolutny klasyk z arkuszy egzaminacyjnych (np. rezerwacja sali weselnej z opcją poprawin).
```javascript
function obliczKosztyWesela() {
    // 1. Pobieramy liczbę gości
    let goscie = document.getElementById("pole-goscie").value;
    let wynik = document.getElementById("wynik");

    // 🛑 STRAŻNIK: Sprawdzamy błędy (wczesny powrót)
    if (!goscie || isNaN(goscie)) {
        wynik.innerHTML = "Błąd: Wpisz poprawną liczbę gości!";
        return; 
    }

    // 2. Skoro nie ma błędów, zamieniamy tekst na liczbę i liczymy bazową cenę
    let liczbaGosci = parseInt(goscie);
    let cenaCalkowita = liczbaGosci * 100; // 100 zł za talerzyk

    // 3. Sprawdzamy CHECKBOX z poprawinami
    const poprawiny = document.getElementById("pole-poprawiny");
    
    // Jeśli checkbox jest ZAZNACZONY, doliczamy opłatę
    if (poprawiny.checked) {
        cenaCalkowita = cenaCalkowita + 2000; // Dodajemy 2000 zł za salę na drugi dzień
    }

    // 4. Wyświetlamy ostateczny wynik na stronie
    wynik.innerHTML = "Całkowity koszt wesela to: " + cenaCalkowita + " zł";
}
```

**Dlaczego o tym pamiętać?**

Wielu zdających próbuje pobrać `.value` z checkboxa, co prowadzi do błędów w obliczeniach (często zwraca po prostu słowo "on"). Użycie `.checked` gwarantuje poprawną, matematyczną logikę i daje pewne punkty na egzaminie!
