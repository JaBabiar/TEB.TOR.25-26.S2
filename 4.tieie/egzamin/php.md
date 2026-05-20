# PHP Egzamin

## Spis Treści – PHP (INF.03)

### 🧱 Część 1: Fundamenty (Podstawy działania)

* [1. Jak działa PHP? (Gdzie jesteśmy?)](#dzial-php-1)
* [2. Zmienne (Dolar rządzi) i Wyświetlanie (echo)](#dzial-php-2)
* [3. Typy danych i Łączenie tekstów (Kropka!)](#dzial-php-3)

### 🌍 Część 2: Komunikacja ze stroną

* [4. Tablice Superglobalne (Dane, które latają w tle)](#dzial-php-4)
* [5. Sprawdzanie danych (isset i empty)](#dzial-php-5)
* [6. Zabezpieczenie przed "Klątwą F5" (Dublowanie formularza)](#dzial-php-6)
* [7. Szukanie błędów (Magia var_dump)](#dzial-php-7)

---

## 🧱 <a id="dzial-php-1"></a> 1. Jak działa PHP? (Gdzie jesteśmy?)

W JavaScript budowaliśmy interakcję **w przeglądarce** użytkownika. PHP działa zupełnie inaczej – wykonuje się **na serwerze**, zanim strona w ogóle trafi do użytkownika.

> ⚠️ **ZAPAMIĘTAJ:** Użytkownik nigdy nie widzi Twojego kodu PHP! Kiedy kliknie "Pokaż źródło strony", zobaczy tylko czysty HTML, który Twój kod PHP wygenerował.

Aby kod PHP zadziałał, musisz zapisać plik z rozszerzeniem `.php` i umieścić go na serwerze (np. w folderze `htdocs` programu XAMPP). Cały kod zawsze zamykamy w specjalnych klamrach:

```php
<?php
    // Tutaj dzieje się magia na serwerze
?>

## 2. Zmienne i Wyświetlanie
W PHP każda zmienna musi zaczynać się od znaku dolara `$`. Nie używamy słów `let` ani `const` jak we frontendzie.

```php
$imie = "Jan";
$punkty = 10;
```

### Wyświetlanie na ekranie (echo)

To odpowiednik `innerHTML` z JavaScriptu, ale o wiele prostszy. `echo` po prostu "wypluwa" tekst prosto do pliku HTML, z którym jest połączony.

```php
echo "Witaj na mojej stronie!";
echo "<h1>Możesz tu wpisywać tagi HTML!</h1>";
```

## 3. Typy Danych i łączenie tekstów

*BŁĄD EGZAMINACYJNY*: W JavaScript łączyliśmy teksty i zmienne za pomocą plusa (+). W PHP do klejenia (konkatenacji) zawsze używamy kropki (.)

```php
$imie = "Anna";

// ŹLE (wywali błąd): 
// echo "Cześć " + $imie; 

// DOBRZE:
echo "Cześć " . $imie . ", jak się masz?";
```

## 4. Tablice Superglobalne

Tablice superglobalne to specjalne, wbudowane w PHP zmienne, które są dostępne zawsze i wszędzie. Odpowiadają za przenoszenie informacji lub odbieranie ich od użytkownika. Zawsze piszemy je wielkimi literami i zaczynamy od $_.

* `$_POST` – Odbiera dane z formularzy (gdzie daliśmy method="post"). Danych nie widać w pasku adresu przeglądarki. Zawsze używaj do haseł, logowania i przesyłania wrażliwych danych
* `$_GET`- Odbiera dane prosto z paska adresu (np. strona.php?id=5). Idealne do wyszukiwarek, filtrowania i stronowania (paginacji).
* `$_COOKIE` – Zapisują małe informacje bezpośrednio na komputerze użytkownika. Częsty motyw na INF.03 do sprawdzania, czy ktoś odwiedza stronę po raz pierwszy.
* `$_SESSION` – Działa podobnie jak ciastka, ale dane zapisywane są bezpiecznie na serwerze i znikają po zamknięciu przeglądarki. Podstawa do systemów logowania. (Wymaga wpisania session_start(); na samej górze pliku!)

### Gotowe rozwiązanie do odbierania danych

Mamy w HTML pole: `<input type="text" name="login">`. W PHP "łapiemy" to po atrybucie name.

```php
$wpisanyLogin = $_POST['login'];
echo "Twój login to: " . $wpisanyLogin;
```

## 5. Sprawdzanie Danych

Zanim przetworzysz formularz, musisz sprawdzić, czy użytkownik w ogóle go wysłał i czy czegoś nie pominął. Używamy do tego dwóch funkcji:

* `isset(zmienna)` – Sprawdza, czy zmienna w ogóle istnieje (np. czy przycisk wyślij został kliknięty).
* `empty(zmienna)` – Sprawdza, czy pole jest puste (czy ktoś nic nie wpisał)

### Zabezpieczenie

Odrzucamy błędy na samym początku

```php
// 1. Sprawdzamy, czy w ogóle kliknięto przycisk wysyłania
if (!isset($_POST['przycisk_wyslij'])) {
    return; // Wychodzimy, czekamy na akcję użytkownika
}

// 2. Pobieramy dane
$imie = $_POST['imie'];

// STRAŻNIK: Sprawdzamy, czy pole imie jest puste
if (empty($imie)) {
    echo "Błąd: Wypełnij pole imię!";
    return; // Przerywamy działanie skryptu
}

//  GŁÓWNY KOD
echo "Witaj " . $imie . "!";
```

## 6. Zabezpieczenie przed ponownym wysłaniem tego samego formularza przy odświeżaniu

Wyobraź sobie: Wypełniasz formularz, klikasz "Wyślij". Skrypt dodaje Cię do bazy. Po chwili z przyzwyczajenia wciskasz F5 (Odśwież). Przeglądarka znów wysyła ten sam formularz i nagle w bazie mamy dwóch identycznych użytkowników.
Zwykłe czyszczenie tablicy przez unset($_POST) tutaj nie zadziała. Kiedy PHP skończy pracę (np. doda dane do bazy), musimy natychmiast wyrzucić użytkownika na czystą stronę. Dzięki temu przy odświeżeniu załaduje tylko pustą stronę, a nie formularz.
PHP

```php

if (isset($_POST['wyslij'])) {
    $imie = $_POST['imie'];
    
    // --> Tutaj zapytanie do bazy danych (np. INSERT INTO) <--
    
    // MAGIA: Po wykonaniu zadania przeładuj stronę na "czysto"
    header("Location: index.php"); 
    
    // Zawsze po header() dajemy exit(), aby zatrzymać stary skrypt
    exit(); 
}

```

## 7. Szukanie błędów

Kiedy odbierasz tablice z formularza lub wyciągasz dane z bazy i coś nie działa, Twoim najlepszym przyjacielem jest var_dump(). Funkcja ta wyrzuca na ekran absolutnie wszystko, co PHP wie o danej zmiennej – typ, długość i zawartość.

Użycie var_dump() zaraz po napisaniu zapytania do bazy (np. po INSERT) to rewelacyjny sposób na sprawdzenie, co kryje się w zmiennych. Co najważniejsze – nie musisz się przejmować kasowaniem tego przed oddaniem pracy. Jeśli zostawisz var_dump w kodzie, nie stracisz za to ani jednego punktu na egzaminie! Najważniejsze, aby główna mechanika skryptu zadziałała.

## 8. Ciasteczka w praktyce (`setcookie`) – Egzaminacyjny Pewniak

W dziale 4 uczyliśmy się, że tablica `$_COOKIE` służy do *odczytywania* ciastek. Ale jak je upiec (stworzyć), zanim strona trafi do użytkownika? To jedno z najczęściej powtarzających się zadań na arkuszach INF.03!

Do tworzenia ciasteczek służy wbudowana funkcja `setcookie()`.

> ⚠️ **ZŁOTA ZASADA (Pułapka!):** Funkcja `setcookie()` musi zostać wywołana **ZANIM** na ekranie pojawi się jakikolwiek kod HTML czy tekst (nawet zwykła spacja przed tagiem `<?php` może wywalić błąd!). Ciasteczka to techniczne nagłówki strony, a serwer musi je wysłać w pierwszej kolejności.

### ⚙️ Budowa funkcji

Schemat jest zawsze taki sam: `setcookie( "nazwa_ciastka" , "Wartość" , czas_wygasniecia );`

Najwięcej problemów na egzaminie sprawia **czas**. W PHP aktualny czas pobieramy funkcją `time()` (zwraca obecny moment w sekundach). Jeśli chcemy, by ciastko żyło przez 1 dzień, musimy do obecnego czasu dodać 24 godziny przeliczone na sekundy (60 sekund *60 minut* 24 godziny = 86400).

### 💻 Gotowiec na egzamin: "Witaj po raz pierwszy!"

Ten schemat pojawia się na egzaminach jak bumerang. Logika jest prosta: sprawdzamy, czy ciastko istnieje. Jeśli nie – tworzymy je i witamy nowego gościa. Jeśli już jest – wyświetlamy inny komunikat.

```php
<?php
// 1. Sprawdzamy, czy ciastko o nazwie "odwiedziny" NIE istnieje
if (!isset($_COOKIE['odwiedziny'])) {
    
    // 2. Skoro nie istnieje, to je tworzymy (pieczemy)!
    // Dodajemy 86400 sekund (czyli 1 pełny dzień) do obecnego czasu
    setcookie("odwiedziny", "tak", time() + 86400);
    
    // 3. Wyświetlamy komunikat dla nowego gościa
    echo "Witaj na naszej stronie po raz pierwszy!";
    
} else {
    
    // 4. Jeśli ciastko już jest na komputerze użytkownika (bo wszedł tu wczoraj)
    echo "Witaj ponownie! Miło Cię znów widzieć.";
    
}
?>
```

## 10. Inicjalizacja połączenia (`mysqli_connect`)

Przed wykonaniem jakiejkolwiek operacji na danych, należy nawiązać połączenie z serwerem bazy. Służy do tego funkcja `mysqli_connect()`, która przyjmuje cztery podstawowe argumenty konfiguracyjne. W przypadku standardowego środowiska egzaminacyjnego (np. XAMPP) są to:

1. **Adres serwera:** `"localhost"`
2. **Użytkownik:** `"root"` (domyślny administrator)
3. **Hasło:** `""` (pusty ciąg znaków)
4. **Nazwa bazy danych:** (np. `"sklep_komputerowy"`)

```php
// 1. Inicjalizacja połączenia i przypisanie do identyfikatora (zmiennej)
$con = mysqli_connect("localhost", "root", "", "sklep_komputerowy");

// Zabezpieczenie: Weryfikacja poprawności połączenia (Guard Clause)
if (!$con) {
    // Zatrzymanie skryptu i wyświetlenie komunikatu w przypadku błędu logowania do bazy
    echo "Błąd krytyczny: Odmowa dostępu do serwera bazy danych.";
    return;
}

```

## 11. Wykonywanie zapytań modyfikujących

Dodawanie nowych rekordów (np. wprowadzonych przez formularz rejestracyjny) wymaga przygotowania poprawnej składni SQL i przekazania jej do bazy za pomocą funkcji mysqli_query()

```php
// 1. Odbiór danych wejściowych z tablicy superglobalnej
$imie = $_POST['imie'];
$nazwisko = $_POST['nazwisko'];

// 2. Deklaracja zapytania SQL
// Uwaga: Zmienne tekstowe wewnątrz zapytania SQL muszą być otoczone pojedynczymi apostrofami.
$sql = "INSERT INTO pracownicy (imie, nazwisko) VALUES ('$imie', '$nazwisko')";

// 3. Wykonanie zapytania
$wynik = mysqli_query($con, $sql);

// 4. Weryfikacja statusu operacji
if ($wynik) {
    echo "Operacja zakończona sukcesem. Dodano nowego pracownika.";
} else {
    echo "Wystąpił błąd podczas modyfikacji bazy danych.";
}
```

W przypadku problemów z wykonaniem zapytania INSERT, użyteczne jest zastosowanie funkcji var_dump($sql); w celu zbadania struktury wygenerowanego zapytania. Obecność wywołań diagnostycznych (jak var_dump po dodaniu rekordu) nie skutkuje utratą punktów na egzaminie INF.03, o ile poprawnie zrealizowano logikę dodawania danych.

## 12. Pobieranie danych 

Instrukcja `SELECT` nie zwraca bezpośrednio sformatowanego tekstu, lecz specjalny obiekt reprezentujący zbiór wyników (tzw. result set). Aby przetworzyć te informacje i zaprezentować je w dokumencie HTML, stosuje się iterację – najczęściej z wykorzystaniem pętli while oraz funkcji `mysqli_fetch_array()` (lub `mysqli_fetch_assoc()`).

```php 

// 1. Przygotowanie zapytania pobierającego dane
$sql = "SELECT imie, nazwisko FROM pracownicy";

// 2. Pobranie zbioru wyników
$wynik = mysqli_query($con, $sql);

// 3. Weryfikacja liczby zwróconych rekordów za pomocą mysqli_num_rows()
$liczba_wierszy = mysqli_num_rows($wynik);

if ($liczba_wierszy === 0) {
    echo "Brak danych spełniających kryteria wyszukiwania.";
} else {
    
    // 4. Iteracja po zbiorze wyników
    // Zmienna $wiersz aktualizuje się w każdym przejściu pętli
    while ($wiersz = mysqli_fetch_array($wynik)) {
        // Prezentacja danych w strukturze listy HTML
        echo "<li>Pracownik: " . $wiersz['imie'] . " " . $wiersz['nazwisko'] . "</li>";
    }
    
}

```
## 13. Zamykanie połączenia

```php
// Zakończenie sesji z bazą danych przypisanej do identyfikatora $con
mysqli_close($con);
```