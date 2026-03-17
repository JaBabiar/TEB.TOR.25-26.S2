# 📝 Notatka do kartkówki: Ścieżki, Semantyka i Tabele

## 1. Logika ścieżek w HTML

Ścieżki określają, gdzie znajduje się zasób (np. obrazek, plik CSS, inna strona), do którego chcemy się odwołać w atrybutach takich jak `href=""` (dla linków) lub `src=""` (dla multimediów).

### Ścieżki Absolutne (Bezwzględne)
Zawierają pełny adres URL. Używane głównie do linkowania zasobów zewnętrznych.
- **Przykład:** `<a href="https://tebesport.pl/">Strona główna</a>`
- **Przykład obrazka:** `<img src="https://placehold.co/300x400" alt="Placeholder">`

### Ścieżki Relatywne (Względne)
Określają lokalizację pliku względem pliku, w którym obecnie się znajdujemy. Używane do linkowania zasobów wewnątrz własnego projektu.
- `./` – oznacza "w tym samym folderze" (często można pominąć).
  - *Przykład:* `<link rel="stylesheet" href="./style.css">`
- `../` – oznacza "wyjdź folder wyżej" (do katalogu nadrzędnego). Można je łączyć!
  - *Przykład:* `<a href="../../../dokumenty/regulamin.pdf">Regulamin</a>` (cofa się o 3 foldery).
- `/` na samym początku – oznacza główny folder serwera (root).

### Inne ważne typy linków:
- **Zakotwiczenia (kotwice):** Przenoszą do konkretnego miejsca na *tej samej* stronie, używając atrybutu `id`.
  - *Przykład:* `<a href="#sekcja2">Przejdź do sekcji 2</a>` (wymaga elementu np. `<section id="sekcja2">`).
- **Linki specjalne:**
  - Telefon: `<a href="tel:+4899999999">Zadzwoń</a>`
  - E-mail: `<a href="mailto:test@test.com">Napisz maila</a>`

> [!TIP]
> **Pamiętaj o WCAG!**
> Obrazki ładowane przez `src` **muszą** mieć atrybut `alt` (nawet pusty `alt=""` jeśli obrazek jest tylko dekoracją), aby strona była dostępna dla czytników ekranu.

---

## 2. Semantyka HTML5

Semantyka to używanie odpowiednich tagów zgodnie z ich przeznaczeniem. Przeglądarka traktuje je jak zwykłe `<div>`, ale mają one ogromne znaczenie dla SEO (pozycjonowania) i **dostępności (WCAG)**, ponieważ definiują tzw. "landmarki" (punkty orientacyjne) dla czytników ekranu.

### Główne znaczniki strukturalne:
- `<header>` – Nagłówek strony lub sekcji (np. miejsce na logo, tytuł strony).
- `<nav>` – Nawigacja głównej strony (menu z linkami).
- `<main>` – Główna, unikalna treść dokumentu. Na stronie powinien być tylko jeden tag `<main>`.
- `<section>` – Tematyczna grupa treści, zazwyczaj z własnym nagłówkiem (np. h2, h3).
- `<article>` – Niezależny, samowystarczalny blok treści (np. post na blogu, news z aktualnościami).
- `<aside>` – Pasek boczny lub treść poboczna, powiązana z otoczeniem, ale nie kluczowa (np. reklamy, powiązane artykuły).
- `<footer>` – Stopka strony lub sekcji (np. prawa autorskie, autor, dolne menu).
- `<figure>` – Kontener dla treści pobocznych, najczęściej obrazków i ich podpisów (`<figcaption>`).
- `<h1>` do `<h6>` – Nagłówki hierarchiczne. `<h1>` powinien być użyty tylko raz na stronie (główny tytuł). Nie przeskakuj poziomów nagłówków (po h2 powinien być h3, nie h5).

> [!NOTE]
> **Poprawna struktura dokumentu:**
> ```html
> <body>
>   <header>
>     <nav> ... </nav>
>   </header>
>   <main>
>     <section>
>       <h2>Aktualności</h2>
>       <article> ... </article>
>     </section>
>     <aside> ... </aside>
>   </main>
>   <footer> ... </footer>
> </body>
> ```

---

## 3. Tabele danych w HTML

Tabele służą **wyłącznie do prezentacji danych tabelarycznych**, a nie do budowania układu strony (layoutu).

### Struktura HTML:
- `<table>` – Główny kontener tabeli.
- `<tr>` (Table Row) – Wiersz tabeli.
- `<th>` (Table Head) – Komórka nagłówkowa (domyślnie pogrubiona i wyśrodkowana).
- `<td>` (Table Data) – Standardowa komórka z danymi.

### Łączenie komórek (Atrybuty):
Atrybuty te dodajemy do `<th>` lub `<td>`, aby rozciągnąć komórkę na kilka wierszy lub kolumn:
- `colspan="x"` – Rozszerza komórkę na `x` **kolumn** (w poziomie).
  - *Przykład:* `<th colspan="4">Bundesliga</th>` (zajmuje szerokość 4 kolumn).
- `rowspan="x"` – Rozszerza komórkę na `x` **wierszy** (w pionie).

### Formatowanie CSS (Kluczowe dla tabel):
Domyślne tabele w HTML mają podwójne obramowanie i bywają nieczytelne.

```css
table, td, th {
    border: 1px solid black; /* Dodanie obramowania */
    border-collapse: collapse; /* Kluczowe! Łączy podwójne linie w jedną ciągłą */
}

/* Scrollowanie tabeli (Responsywność) */
div.table-container {
    width: 400px; /* lub 100% */
    overflow-x: auto; /* Pozwala na scrollowanie tabeli na małych ekranach */
}
```
# 💻 Praktyczny Trening do Kartkówki: HTML & CSS



## 🛠️ Zadanie 1: (Semantyka)

Początkujący programista napisał strukturę strony używając wyłącznie tagów `<div>`. Twoim zadaniem jest **przepisanie tego kodu** z użyciem poprawnych, semantycznych znaczników HTML5 (`header`, `nav`, `main`, `section`, `article`, `aside`, `footer`).

**Zły kod do poprawy:**
```html
<div class="naglowek">
    <div class="menu">
        <a href="/">Strona główna</a>
    </div>
</div>

<div class="zawartosc-strony">
    <div class="aktualnosci">
        <div class="wpis-na-blogu">
            <h1>Nowy wpis</h1>
            <p>Treść wpisu...</p>
        </div>
    </div>
    
    <div class="pasek-boczny">
        <p>Reklama</p>
    </div>
</div>

<div class="stopka">
    <p>Copyright 2024</p>
</div>
```

> [!success]- Rozwiązanie: Sprawdź swój kod
> ```html
> <header>
>     <nav>
>         <a href="/">Strona główna</a>
>     </nav>
> </header>
> 
> <main>
>     <section> >         <article>
>             <h1>Nowy wpis</h1>
>             <p>Treść wpisu...</p>
>         </article>
>     </section>
>     
>     <aside>
>         <p>Reklama</p>
>     </aside>
> </main>
> 
> <footer>
>     <p>Copyright 2024</p>
> </footer>
> ```

---

## 🛠️ Zadanie 2: Labirynt folderów (Logika ścieżek)

Wyobraź sobie następującą strukturę plików i folderów w Twoim projekcie:
```text
projekt/
├── css/
│   └── style.css
├── img/
│   └── logo.png
├── podstrony/
│   └── oferta.html
└── index.html
```

**Polecenia:**
1. Jesteś w pliku **`index.html`**. Napisz kod podpinający arkusz stylów `style.css`.
2. Jesteś w pliku **`oferta.html`**. Napisz znacznik obrazka, który wyświetli `logo.png`.
3. Jesteś w pliku **`oferta.html`**. Napisz link, który przeniesie użytkownika z powrotem na stronę główną (`index.html`).

> [!success]- Rozwiązanie: Sprawdź swój kod
> **Ad 1.** (z `index.html` do folderu `css`):
> `<link rel="stylesheet" href="./css/style.css">` *(lub samo `css/style.css`)*
> 
> **Ad 2.** (Z `oferta.html` musisz najpierw wyjść wyżej `../`, a potem wejść do `img/`):
> `<img src="../img/logo.png" alt="Logo firmy">` *(Pamiętaj o alt!)*
> 
> **Ad 3.** (Z `oferta.html` musisz wyjść jeden poziom wyżej do `index.html`):
> `<a href="../index.html">Powrót do strony głównej</a>`

---

## 🛠️ Zadanie 3: Budowa tabeli (Dane i CSS)

Twoim zadaniem jest stworzenie kodu HTML oraz CSS dla tabeli przedstawiającej prosty plan lekcji. 

**Wymagania HTML:**
1. Tabela ma mieć główny nagłówek na samej górze z tekstem "Plan Lekcji", który rozciąga się na **3 kolumny**.
2. W drugim rzędzie mają być nagłówki kolumn: "Dzień", "Przedmiot", "Sala".
3. W trzecim rzędzie wpisz dowolne dane (np. "Poniedziałek", "Matematyka", "Sala 101").
4. Zabezpiecz tabelę przed "wylewaniem się" na telefonach (zawiń ją w odpowiedni kontener).

**Wymagania CSS:**
1. Dodaj czarne, pojedyncze obramowanie (`1px solid black`) dla tabeli i komórek.
2. Zastosuj właściwość, która sprawi, że linie obramowania nie będą podwójne.
3. Dodaj właściwość pozwalającą na scrollowanie na osi X dla kontenera tabeli.

> [!success]- Rozwiązanie: Sprawdź swój kod
> **Kod HTML:**
> ```html
> <div class="table-container">
>     <table>
>         <tr>
> 	         <th colspan="3">Plan Lekcji</th>
>         </tr>
>         <tr>
>             <th>Dzień</th>
>             <th>Przedmiot</th>
>             <th>Sala</th>
>         </tr>
>         <tr>
>             <td>Poniedziałek</td>
>             <td>Matematyka</td>
>             <td>Sala 101</td>
>         </tr>
>     </table>
> </div>
> ```
> 
> **Kod CSS:**
> ```css
> table, th, td {
>     border: 1px solid black;
>     border-collapse: collapse; /* Kluczowe! Łączy podwójne ramki w jedną */
> }
> 
> /* Opcjonalnie, dla czytelności: */
> td, th {
>     padding: 8px;
> }
> 
> /* Kontener zapobiegający psuciu layoutu na telefonach */
> .table-container {
>     width: 100%;
>     overflow-x: auto; 
> }
> ```

