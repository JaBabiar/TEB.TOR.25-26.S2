
# Kartkówka: PHP i Baza Danych (Poprawa)

plik `index.php` należy zapisać w folderze C:\xampp\htdocs\imie_nazwisko\

---

## 📝 Zadanie do wykonania

Stwórz plik o nazwie **index.php**. Skrypt ma połączyć się z bazą danych, wyświetlić listę pracowników, a na końcu dodać nową osobę.

---

### 1. Połączenie z bazą (2 punkty)

* [ ] Połącz się z bazą o nazwie: **firma_db**
* [ ] Dane serwera: **localhost**, użytkownik **root**, brak hasła.
* [ ] **Zabezpieczenie:** Jeśli połączenie się nie uda, wyświetl komunikat o błędzie i zatrzymaj skrypt (użyj `die`).

### 2. Pobieranie danych (2 punkty)

* [ ] Napisz zapytanie **SELECT**, które pobierze kolumny: **imie**, **nazwisko**, **stanowisko**.
* [ ] Dane pobierz z tabeli o nazwie: **pracownicy**.
* [ ] Wykonaj to zapytanie w kodzie PHP.

### 3. Struktura strony HTML (2 punkty)

* [ ] Stwórz poprawną strukturę dokumentu **HTML5**.
* [ ] **Dostępność (WCAG):** Ustaw język strony na polski (`lang="pl"`) oraz dodaj tytuł strony w znaczniku `<title>`.

### 4. Wyświetlanie wyników (2 punkty)

* [ ] Wewnątrz sekcji `<body>` użyj pętli **while**.
* [ ] Pobieraj wiersze jako **tablicę**.
* [ ] Wyświetl dane w formacie: **imię - nazwisko - stanowisko**.
* [ ] Po każdym wierszu dodaj znacznik nowej linii: `<br />`.

### 5. Dodawanie danych i zamknięcie (2 punkty)

* [ ] Pod kodem HTML stwórz **3 zmienne** z dowolnymi danymi nowego pracownika.
* [ ] Napisz i wykonaj zapytanie **INSERT INTO**, które doda te dane do bazy.
* [ ] na końcu **zamknij połączenie** z bazą

---

## 📊 Punktacja (Max: 10 punktów)

| Procenty | Punkty | Ocena |
| :--- | :--- | :--- |
| **95% i więcej** | 9.5 – 10 pkt | **5** (bardzo dobry) |
| **85% – 94%** | 8.5 – 9 pkt | **4** (dobry) |
| **80% – 84%** | 8 pkt | **3** (dostateczny) |
| **75% – 79%** | 7.5 pkt | **2** (dopuszczający) |
| **Poniżej 75%** | 0 – 7 pkt | **1** (niedostateczny) |

---

## 🛠️ Instrukcja dla bazy danych (SQL)

Uruchom poniższy kod w phpMyAdmin przed kartkówką:

```sql
CREATE DATABASE IF NOT EXISTS firma_db COLLATE utf8mb4_polish_ci;
USE firma_db;

CREATE TABLE IF NOT EXISTS pracownicy (
    id INT AUTO_INCREMENT PRIMARY KEY,
    imie VARCHAR(50),
    nazwisko VARCHAR(50),
    stanowisko VARCHAR(100)
);

INSERT INTO pracownicy (imie, nazwisko, stanowisko) VALUES
('Piotr', 'Zalewski', 'Kierownik'),
('Katarzyna', 'Wiśniewska', 'Księgowa');

```

| Funkcja biblioteki `mysqli` | Zwracana wartość |
| --- | --- |
| `mysqli_connect(serwer, użytkownik, hasło, nazwa_bazy)` | ID połączenia lub `FALSE`, gdy wystąpi niepowodzenie |
| `mysqli_select_db(id_polaczenia, nazwa_bazy)` | `TRUE`/`FALSE` w zależności od stanu operacji |
| `mysqli_error(id_polaczenia)` | Tekst komunikatu błędu |
| `mysqli_close(id_polaczenia)` | `TRUE`/`FALSE` w zależności od stanu operacji |
| `mysqli_query(id_polaczenia, zapytanie)` | Wynik zapytania |
| `mysqli_fetch_row(wynik_zapytania)` | Tablica numeryczna odpowiadająca wierszowi zapytania |
| `mysqli_fetch_array(wynik_zapytania)` | Tablica zawierająca kolejny wiersz z wyniku zapytania lub `FALSE`, jeżeli nie ma więcej wierszy |
| `mysqli_num_rows(wynik_zapytania)` | Liczba wierszy w podanym zapytaniu |
| `mysqli_num_fields(wynik_zapytania)` | Liczba kolumn w podanym zapytaniu |
| `isset($zmienna)` | `TRUE`/`FALSE` w zależności od tego, czy `$zmienna` istnieje |