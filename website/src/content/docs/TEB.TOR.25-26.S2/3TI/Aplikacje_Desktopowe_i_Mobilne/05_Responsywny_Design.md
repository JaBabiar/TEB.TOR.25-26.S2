---
title: Podstawy Responsywnego Designu
description: podstawowe informacje z przykładowym zadaniem
sidebar:
  label: 5. Responsywny Design
---

# Responsywność: @media screen and () - Teoria i Praktyka (INF.03)

## 📚 Notatka: Jak działa `@media screen and ()`?

Podstawowa reguła `@media` pozwala dostosować wygląd strony do wielkości ekranu. Kiedy jednak dodajemy słowa kluczowe `screen` oraz `and`, precyzujemy, na jakich dokładnie urządzeniach chcemy wymusić zmiany i jak te warunki ze sobą łączyć.

### 1. Typy nośników (Media Types)

- `all` (domyślnie) – style stosowane dla wszystkich urządzeń.
- `screen` – style stosowane **tylko** dla ekranów (monitory, tablety, telefony). Nie wpłyną np. na wydruk strony.
- `print` – style stosowane **tylko** podczas drukowania dokumentu (np. ukrywanie menu, czarno-białe tło dla oszczędności tuszu).

### 2. Słowo kluczowe `and`

Operator `and` (i) służy do łączenia typu nośnika z warunkiem (np. szerokością ekranu) lub do łączenia kilku precyzyjnych warunków ze sobą. Oba warunki muszą być spełnione, aby style wewnątrz bloku zadziałały.

**Przykład 1: Typ nośnika + Warunek**

```css
/* Zastosuj TYLKO na ekranach (nie na wydruku) i TYLKO gdy ekran ma maksymalnie 768px */
@media screen and (max-width: 768px) {
    .menu {
        display: block; /* np. menu pionowe na telefonach */
    }
}
```

**Przykład 2: Przedział szerokości (łączenie warunków)**

```css
/* Zastosuj TYLKO na ekranach o szerokości OD 768px DO 1024px (tzw. breakpoint dla tabletów) */
@media screen and (min-width: 768px) and (max-width: 1024px) {
    .container {
        width: 90%;
        grid-template-columns: 1fr 1fr;
    }
}
```

### ⚠️ Najczęstsze błędy na egzaminie

1. **Brak spacji po słowie `and`** – zapis `@media screen and(max-width: 600px)` jest składniowo niepoprawny i przeglądarka go zignoruje!
2. **Brak tagu Viewport** – niezależnie od poprawności CSS, bez `<meta name="viewport" content="width=device-width, initial-scale=1.0">` w pliku HTML strona nie dostosuje się na prawdziwym urządzeniu mobilnym.

---

## 💻 Zadanie praktyczne: Panel ogłoszeń

**Cel:** Zbudowanie responsywnej siatki ogłoszeń z wykorzystaniem typów nośników i precyzyjnych przedziałów szerokości ekranu.

### Krok 1: Struktura HTML

Stwórz plik `index.html` z główną sekcją `<main>`. Wewnątrz umieść 6 elementów `<article>` reprezentujących ogłoszenia. Każdy artykuł powinien zawierać nagłówek `<h3>` z dowolnym tytułem i krótki paragraf `<p>`. Pamiętaj o znaczniku Viewport w sekcji `<head>`.

### Krok 2: Domyślny wygląd (Desktop)

W pliku CSS stwórz style domyślne (dla dużych ekranów):

- Kontener `<main>` ma wykorzystywać siatkę `display: grid;` (lub Flexbox).
- Ogłoszenia (`<article>`) muszą układać się w **3 kolumnach** o równych szerokościach.
- Dodaj każdemu ogłoszeniu obramowanie, wewnętrzny margines (`padding`) i delikatny cień pod spodem.

### Krok 3: Dodanie `@media screen and ()`

Dopisz na dole pliku CSS odpowiednie reguły. Zwróć uwagę, by ograniczyć je wyłącznie do ekranów.

1. **Dla tabletów (wymagany przedział):**
   Napisz regułę, która zadziała **tylko na ekranach** o szerokości od `768px` do `1024px` włącznie.
   - Zmień układ `<main>`, aby ogłoszenia układały się w **2 kolumnach**.
   - Zmień kolor tła artykułów na jasnoszary (`#f4f4f4`).

2. **Dla smartfonów:**
   Napisz regułę, która zadziała **tylko na ekranach** o szerokości do `767px` włącznie.
   - Zmień układ `<main>`, aby ogłoszenia układały się w **1 kolumnie** (każde zajmuje 100% szerokości).
   - Powiększ rozmiar czcionki w nagłówkach `<h3>` o 20%, aby były bardziej czytelne na telefonie.

3. **Dla wydruku (Bonus punktowy):**
   Napisz osobną regułę wyłącznie dla nośnika drukowanego (`@media print`).
   - Usuń obramowanie i cienie z ogłoszeń (aby zaoszczędzić tusz drukarki).
   - Ustaw kolor tekstu na całkowicie czarny, a tło na całkowicie białe.

> **Wskazówka:** Konsekwentnie trzymaj wszystkie zapytania medialne na samym dole arkusza CSS, chroniąc zasady kaskadowości!
