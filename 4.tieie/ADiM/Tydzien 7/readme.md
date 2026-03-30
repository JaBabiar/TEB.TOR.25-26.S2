# Walidacja Formularzy i Podstawowa Logika Logowania

Na dzisiejszych zajęciach stworzyliśmy prosty panel logowania. Dowiedzieliśmy się, jak połączyć formularz HTML z kodem JavaScript oraz jak sprawdzać (walidować) dane wpisywane przez użytkownika.

---

## 1. Struktura Formularza (HTML)

Nasz plik `index.html` zawiera formularz, który pozwala użytkownikowi wprowadzić dane. Kluczowe elementy to:

* **Pola wprowadzania (`<input>`):** Użyliśmy różnych typów, aby odpowiednio dostosować je do wprowadzanych danych:
  * `type="text"` - dla zwykłego tekstu (login).
  * `type="password"` - ukrywa wpisywane znaki za pomocą kropek/gwiazdek (hasło).
  * `type="number"` - wymusza na przeglądarce klawiaturę numeryczną i pozwala wpisać tylko cyfry (wiek).
* **Przycisk akcji (`<button>`):** Posiada atrybut `onclick="loginUser()"`, który sprawia, że po jego kliknięciu uruchamia się nasza funkcja z pliku JavaScript.

> **💡 Dobra praktyka (Dostępność):** Zauważ, że każdy `<input>` ma przypisany znacznik `<label>` z atrybutem `for`, który dokładnie odpowiada atrybutowi `id` pola. To kluczowy element standardu WCAG. Dzięki temu czytniki ekranu poprawnie odczytują przeznaczenie pola, a kliknięcie w sam tekst etykiety aktywuje pole tekstowe (co bardzo ułatwia korzystanie ze strony na telefonach).

---

## 2. Pobieranie Danych i Sprawdzanie Warunków (JavaScript)

W pliku `app.js` napisaliśmy funkcję `loginUser()`, która weryfikuje wpisane informacje.

### Krok 1: Pobieranie elementów

Na samym początku musimy "złapać" elementy z HTML i zapisać je do zmiennych w JS:

```javascript
let login = document.getElementById('login');
let pwd = document.getElementById('pwd');
let wiek = document.getElementById('wiek');
```

### Narzędzia użyte do walidacji (Operatory logiczne)

Zanim przejdziemy do warunków, podsumujmy operatory, które poznaliśmy:

| Operator / Właściwość | Nazwa | Jak działa w naszym kodzie? |
| :--- | :--- | :--- |
| `!` | **Negacja (NOT)** | Odwraca wartość logiczną. `!login.value` w praktyce sprawdza, czy pole jest **puste**. |
| `\|\|` | **LUB (OR)** | Warunek jest spełniony, jeśli *przynajmniej jedna* strona jest prawdziwa. Użyte do: *jeśli brakuje loginu LUB brakuje hasła*. |
| `&&` | **I (AND)** | Warunek jest spełniony tylko, gdy *obie* strony są prawdziwe. |
| `==` | **Przyrównanie** | Sprawdza, czy wartości po obu stronach są sobie równe. |
| `.length` | **Długość** | Właściwość tekstu. `pwd.value.length > 5` oznacza, że hasło musi mieć minimum 6 znaków. |

### Krok 2: Sprawdzenie pustych pól (Zabezpieczenie)

Instrukcja `if` sprawdza, czy użytkownik ominął któreś z głównych pól:

```javascript
if(!login.value || !pwd.value){
    console.error("Brak wymaganych danych");
    return; // Słowo 'return' natychmiast przerywa działanie całej funkcji!
}
```

### Krok 3: Weryfikacja wieku

Następnie sprawdzamy wiek za pomocą operatora mniejsze lub równe (`<=`). Wyświetlamy proste okienko `alert()`. 
*Pamiętaj: Aby sprawdzić liczbę wpisaną w input, musimy odwołać się do jego właściwości `.value`!*

```javascript
if(wiek.value <= 18){
    alert("Strona przeznaczona dla pełnoletnich");
}
```

### Krok 4: Symulacja logowania

Jeśli powyższe zabezpieczenia nie przerwały funkcji (za pomocą `return`), sprawdzamy czy wpisane dane pasują do naszych wytycznych:

```javascript
if (login.value == "nazwa_konta" && pwd.value.length > 5) {
    console.log("sukces");
}
```
