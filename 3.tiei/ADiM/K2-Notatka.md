# 📚 Notatka do kartkówki: CSS – Zaokrąglenia, wielkości i cienie bloków

Ta notatka zawiera najważniejsze informacje, właściwości i przykłady, które musisz znać na kartkówkę.

---

## 1. Zaokrąglenia rogów (`border-radius`)

Właściwość `border-radius` służy do zaokrąglania rogów elementów HTML (np. przycisków, obrazków, kontenerów `<div>`).

### Podstawowe użycie:
```css
.box {
  border-radius: 10px; /* Zaokrągla wszystkie 4 rogi o 10 pikseli */
}

```

### Koło / Elipsa (wartości w procentach):

Aby stworzyć idealne koło z kwadratowego elementu, używamy wartości `50%`.

```css
.circle {
  width: 100px;
  height: 100px;
  border-radius: 50%; /* Tworzy koło */
}

```

### Określanie poszczególnych rogów:

Możesz podać od 1 do 4 wartości (działają zgodnie z ruchem wskazówek zegara, zaczynając od lewego górnego rogu):

* **1 wartość:** `border-radius: 10px;` (wszystkie rogi)
* **2 wartości:** `border-radius: 10px 20px;` (lewy-górny/prawy-dolny, prawy-górny/lewy-dolny)
* **4 wartości:** `border-radius: 10px 20px 30px 40px;` (lewy-górny, prawy-górny, prawy-dolny, lewy-dolny)

Możesz też użyć dedykowanych właściwości:

* `border-top-left-radius`
* `border-top-right-radius`
* `border-bottom-right-radius`
* `border-bottom-left-radius`

---

## 2. Wielkości bloków (Wymiary)

Każdy element blokowy ma określoną szerokość i wysokość.

### Podstawowe właściwości:

* `width` – szerokość elementu.
* `height` – wysokość elementu.
* `max-width` / `max-height` – maksymalna szerokość/wysokość (przydatne w RWD – responsywnym projektowaniu).
* `min-width` / `min-height` – minimalna szerokość/wysokość.

### Popularne jednostki:

| Jednostka | Opis |
| --- | --- |
| `px` | Piksele – stała wielkość (np. `200px`). |
| `%` | Procenty – wielkość względem rodzica (np. `50%`). |
| `vw` | Viewport Width – procent szerokości okna przeglądarki. |
| `vh` | Viewport Height – procent wysokości okna przeglądarki. |

### ⚠️ BARDZO WAŻNE: Model Pudełkowy (Box Model) i `box-sizing`

Domyślnie w CSS dodanie `padding` (marginesu wewnętrznego) lub `border` (obramowania) powiększa całkowity rozmiar elementu. Aby tego uniknąć, stosujemy:

```css
* {
  box-sizing: border-box;
}

```

* **`content-box` (domyślne):** Całkowita szerokość = `width` + `padding` + `border`.
* **`border-box` (zalecane):** `width` to ostateczna szerokość (padding i border "wchodzą" do środka i nie powiększają pudełka).

---

## 3. Cienie bloków (`box-shadow`)

Właściwość `box-shadow` pozwala dodać cień do elementu, co nadaje mu efekt głębi (tzw. efekt 3D).

### Składnia:

```css
box-shadow: [przesunięcie-X] [przesunięcie-Y] [rozmycie] [rozmiar-cienia] [kolor];

```

### Przykład:

```css
.card {
  box-shadow: 5px 10px 15px 0px rgba(0, 0, 0, 0.3);
}

```

**Co oznaczają poszczególne wartości w powyższym przykładzie?**

1. `5px` – przesunięcie w osi X (w prawo; wartość ujemna przesunie w lewo).
2. `10px` – przesunięcie w osi Y (w dół; wartość ujemna przesunie w górę).
3. `15px` – promień rozmycia (blur). Im więcej, tym cień jest bardziej miękki i rozmyty. `0` to ostry cień.
4. `0px` – rozprzestrzenianie (spread). Ile cień ma urosnąć.
5. `rgba(0, 0, 0, 0.3)` – kolor cienia (tutaj czarny z 30% przezroczystością).

### Cień wewnętrzny (`inset`):

Jeśli dodasz słowo kluczowe `inset` na początku lub na końcu, cień pojawi się wewnątrz elementu.

```css
.pressed-button {
  box-shadow: inset 2px 2px 5px black;
}

```
