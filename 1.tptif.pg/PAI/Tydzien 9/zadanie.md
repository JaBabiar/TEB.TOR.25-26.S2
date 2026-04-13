# 🧠 Zadanie: Generator przedmiotów (loot generator)

## 🎯 Cel zadania
Nauczysz się:
- używać funkcji (`function`)
- korzystać z pętli (`for`, `while`)
- losować dane (`Math.random`)
- pracować z tablicami

---

## 📦 Wprowadzenie

Tworzysz prosty generator przedmiotów do gry.

Każdy przedmiot składa się z:
- nazwy (np. Miecz, Łuk)
- rzadkości (np. Zwykły, Epicki)
- opcjonalnie: przedrostka (np. Ognisty, Lodowy)

---

## 📚 Przykładowe dane

Możesz użyć takich tablic:

```js
let przedmioty = ["Miecz", "Topór", "Łuk", "Sztylet"]

let rzadkosci = ["Zwykły", "Rzadki", "Epicki", "Legendarny"]

let przedrostki = ["Ognisty", "Lodowy", "Zatruty", "Święty"]
```

---

## 🟢 Część 1 – losowanie liczby (10 min)

### ✏️ Zadanie:

Napisz funkcję:

```js
function losujLiczbe(min, max)
```

która:

* zwraca losową liczbę całkowitą z zakresu `min`–`max`

---

## 🟡 Część 2 – losowanie elementu z tablicy (10 min)

### ✏️ Zadanie:

Napisz funkcję:

```js
function losujZTablicy(tablica)
```

która:

* losuje jeden element z podanej tablicy
* zwraca go

📌 Podpowiedź:
Użyj `.length`

---

## 🔵 Część 3 – generowanie przedmiotu (10 min)

### ✏️ Zadanie:

Napisz funkcję:

```js
function generujPrzedmiot()
```

która:

* losuje:

  * nazwę przedmiotu
  * rzadkość
  * przedrostek
* zwraca tekst w formacie:

```
[Przedrostek] [Nazwa] ([Rzadkość])
```

📌 Przykład:

```
Ognisty Miecz (Epicki)
Lodowy Łuk (Rzadki)
```

---

## 🔴 Część 4 – wiele przedmiotów (5–7 min)

### ✏️ Zadanie:

Napisz funkcję:

```js
function generujWiele(ile)
```

która:

* używa pętli (`for` lub `while`)
* generuje wiele przedmiotów
* wypisuje je w konsoli

📌 Przykład:

```
1: Ognisty Miecz (Epicki)
2: Sztylet (Zwykły)
3: Lodowy Topór (Legendarny)
```

---

## ⭐ Zadanie dodatkowe (dla chętnych)

1. Dodaj szansę na brak przedrostka (np. 50%)

   ```
   Miecz (Zwykły)
   ```

2. Dodaj „super rzadkość”:

   * np. 5% szans na „Mityczny”

3. Dodaj licznik ile wypadło przedmiotów każdej rzadkości

---

## 💡 Wskazówki

* indeksy tablic zaczynają się od `0`
* długość tablicy:

```js
tablica.length
```

* przydatne:

```js
Math.floor()
Math.random()
```

---

## 🚀 Cel końcowy

Program powinien:

* generować losowe przedmioty
* używać funkcji
* działać dla różnych danych
* być czytelny i poprawny

---

Powodzenia! 🎮

```

