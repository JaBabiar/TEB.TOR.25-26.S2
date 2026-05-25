---
title: Interakcja ze Stroną (HTML i DOM)
description: Manipulacja dokumentem HTML, obsługa zdarzeń, przełączanie klas CSS oraz praca z polami wyboru na egzaminie INF.03.
sidebar:
  label: 3. DOM i Zdarzenia
---

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

### 🎨 KROK 3: Zmiana wyglądu (Stylów CSS) z poziomu JS
Zamiast pisać myślniki (jak w CSS: `background-color`), w JavaScript łączymy słowa i piszemy drugie z dużej litery (tzw. camelCase: `backgroundColor`).

```javascript
poleWyniku.style.backgroundColor = "red"; // Zmienia tło na czerwone
poleWyniku.style.fontSize = "20px";       // Zmienia wielkość czcionki
```

---

## 🖱️ Zdarzenia (Events) – Jak strona reaguje na użytkownika
Zdarzenia to sygnały, które przeglądarka wysyła, gdy coś się dzieje na stronie (ktoś kliknął, wpisał tekst, najechał myszką). Nasz kod JavaScript może tych sygnałów **nasłuchiwać** i na nie reagować.

### 🌟 Najważniejsze Zdarzenia (Lista Przebojów)
Oto zdarzenia, które najczęściej pojawiają się na egzaminach i w codziennej pracy:

**Zdarzenia Myszy:**
- `click` – Pojedyncze kliknięcie (najpopularniejsze).
- `dblclick` – Podwójne kliknięcie.
- `mouseenter` / `mouseleave` – Reagują, gdy kursor "wchodzi" na element i z niego "schodzi" (nowocześniejsze wersje `mouseover` i `mouseout`).

**Zdarzenia Klawiatury (Ważne dla dostępności - WCAG!):**
- `keydown` – Użytkownik wciska klawisz (np. przydatne do zrobienia sterowania w prostej grze).
- `keyup` – Użytkownik puszcza klawisz (często używane do sprawdzania hasła na żywo, zaraz po wpisaniu literki).

**Zdarzenia Formularzy:**
- `focus` – Użytkownik wszedł w pole tekstowe (np. kliknął w nie, żeby zacząć pisać).
- `blur` – Użytkownik wyszedł z pola tekstowego.
- `input` – Reaguje na **każdą** zmianę w polu tekstowym w czasie rzeczywistym (lepsze niż `keyup` dla formularzy).
- `change` – Reaguje na zmianę, ale dopiero po zatwierdzeniu (np. po wybraniu innej opcji z rozwijanej listy `<select>`).

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

---

## 👗 Nowoczesna zmiana wyglądu (`classList`)

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

:::caution[Ważne]
W nawiasach wpisujemy samą nazwę klasy, **BEZ kropki na początku!**
:::

### 💻 Gotowiec na egzamin: Przycisk zmiany motywu
Poniżej bardzo popularne zadanie – przycisk, który po kliknięciu zmienia całą stronę w tryb przyjazny dla osób niedowidzących, a po ponownym kliknięciu wraca do normalnego wyglądu. Z użyciem `toggle` to banalnie proste!

```javascript
function zmienMotyw() {
    // 1. Łapiemy całe ciało strony (tag <body>)
    const strona = document.getElementById("cialo-strony");

    // 2. Używamy przełącznika! 
    // Jedna linijka kodu załatwia nam sprawdzanie, czy klasa już tam jest.
    strona.classList.toggle("wysoki-contrast");
}
```

**Dlaczego warto to stosować na INF.03?**
1. Kod JS jest krótki i czysty.
2. Wygląd (CSS) i działanie (JS) są od siebie oddzielone.
3. Zrobienie trybu "Dark Mode" lub "Wysoki Kontrast" zajmuje dosłownie jedną linijkę, a bardzo często pojawia się w arkuszach egzaminacyjnych.

---

## ☑️ Pola wyboru (Checkboxy i Radio) – `.checked`
Kiedy masz do czynienia z kwadratowym okienkiem do zaznaczania (Checkbox) lub okrągłym polem wyboru (Radio), nie interesuje Cię to, co jest w nim napisane. Interesuje Cię tylko jedno: **Czy jest zaznaczone, czy nie?**

Do sprawdzania tego używamy właściwości **`.checked`** (z ang. _zaznaczony_). Zwraca ona nam tylko dwie odpowiedzi:
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

:::tip[Dlaczego o tym pamiętać?]
Wielu zdających próbuje pobrać `.value` z checkboxa, co prowadzi do błędów w obliczeniach (często zwraca po prostu słowo "on"). Użycie `.checked` gwarantuje poprawną, matematyczną logikę i daje pewne punkty na egzaminie!
:::