---
title: Logika i Struktura Programu
description: Instrukcje warunkowe, pętle, tablice, funkcje i technika wczesnego powrotu (Guard Clause).
sidebar:
  label: 2. Logika i Struktura
---

## 🚦 Instrukcje Warunkowe (Podejmowanie decyzji)
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

### 🕹️ Konstrukcja `switch` (Wybór z wielu gotowych opcji)

Używamy jej, gdy sprawdzamy **jedną konkretną zmienną** i mamy przygotowaną listę gotowych przypadków (np. dni tygodnia, numer wybranej usługi u fryzjera, poziom trudności w grze). 

Działa to jak automat z napojami – wciskasz guzik numer 2 i dostajesz przypisany do niego napój.

:::caution[Ważne słowo na egzamin]
Słowo **`break`** (przerwij) to absolutna podstawa! Oznacza ono: *"Znalazłem to, czego szukałem, wykonaj kod i uciekaj stąd!"*. Jeśli go zapomnisz, program wykona wszystkie opcje poniżej!
:::

```javascript
let wybranaUsluga = 2;
let cenaDoZaplaty = 0;

switch (wybranaUsluga) {
    
    case 1:
        // Co robimy, gdy wybrano opcję 1
        cenaDoZaplaty = 50; 
        break; // Uciekamy!
        
    case 2:
        // Co robimy, gdy wybrano opcję 2
        cenaDoZaplaty = 100; 
        break; // Uciekamy!
        
    default:
        // "Wyjście awaryjne" – jeśli ktoś wpisał np. numer 99
        cenaDoZaplaty = 0; 
        console.log("Nie mamy takiej usługi!");
}
```

---

## 🔄 Pętle (Powtarzanie czynności)
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

## 📚 Tablice (Listy elementów)
Tablica to jedna zmienna, która trzyma wiele wartości naraz (np. listę ocen). Zaczynamy liczyć od **zera**!

```javascript
let oceny = [5, 4, 3, 5];

oceny[0]; // Wynik: 5 (pierwszy element)
oceny[2]; // Wynik: 3 (trzeci element)
```

- **`.push(wartość)`** – Dodaje nowy element na sam koniec tablicy.
- **`.length`** – Zwraca liczbę elementów w tablicy.

---

## ⚙️ Funkcje (Twoje własne maszyny)
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