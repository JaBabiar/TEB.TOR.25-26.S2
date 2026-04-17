# Kartkówka: PHP i Baza Danych

plik `index.php` należe zapisać w folderze C:\xampp\htdocs\imie_nazwisko\

---

## 📝 Zadanie do wykonania

Stwórz plik o nazwie **index.php**. Skrypt ma połączyć się z bazą danych, wyświetlić listę osób, a na końcu dodać nowego użytkownika.

---

### 1. Połączenie z bazą (2 punkty)

* [ ] Połącz się z bazą o nazwie: **egzamin2**
* [ ] Dane serwera: **localhost**, użytkownik **root**, brak hasła.
* [ ] **Zabezpieczenie:** Jeśli połączenie się nie uda, wyświetl komunikat o błędzie i zatrzymaj skrypt (użyj `die`).

### 2. Pobieranie danych (2 punkty)

* [ ] Napisz zapytanie **SELECT**, które pobierze kolumny: **username**, **email**, **passwd**.
* [ ] Dane pobierz z tabeli o nazwie: **users**.
* [ ] Wykonaj to zapytanie w kodzie PHP.

### 3. Struktura strony HTML (2 punkty)

* [ ] Stwórz poprawną strukturę dokumentu **HTML5**.
* [ ] **Dostępność (WCAG):** Ustaw język strony na polski (`lang="pl"`) oraz dodaj tytuł strony w znaczniku `<title>`.

### 4. Wyświetlanie wyników (2 punkty)

* [ ] Wewnątrz sekcji `<body>` użyj pętli **while**.
* [ ] Pobieraj wiersze jako **tablicę**.
* [ ] Wyświetl dane w formacie: **login - email - hasło**.
* [ ] Po każdym wierszu dodaj znacznik nowej linii: `<br />`.

### 5. Dodawanie danych i zamknięcie (2 punkty)

* [ ] Pod kodem HTML stwórz **3 zmienne** z dowolnymi danymi nowego użytkownika.
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
CREATE DATABASE IF NOT EXISTS egzamin2 COLLATE utf8mb4_polish_ci;
USE egzamin2;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    passwd VARCHAR(255)
);

INSERT INTO users (username, email, passwd) VALUES
('AnnaKowalska', 'anna@example.pl', 'haslo123'),
('JanNowak', 'jan@example.pl', 'qwerty');

```