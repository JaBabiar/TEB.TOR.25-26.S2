```html

<div id="box">
    Podgląd
</div>

<form>
    <label>Wysokość: <input type="text" placeholder="np. 200px"></label><br>
    <label>Szerokość: <input type="text" placeholder="np. 50%"></label><br>
    <label>Kolor tła: <input type="text" placeholder="np. gold"></label><br>
    <label>Obramowanie: <input type="text" placeholder="np. 5px solid red"></label><br>
    <label>Tekst: <input type="text" placeholder="Wpisz coś..."></label><br>
    
    <button>Zastosuj zmiany</button>
</form>
```

### 2. Zadanie programistyczne (JavaScript)

Napisz w języku JavaScript funkcję o nazwie `aktualizujStyl()`, która zrealizuje poniższe założenia. Pamiętaj, aby podpiąć wywołanie tej funkcji pod zdarzenie kliknięcia przycisku (np. używając `addEventListener` z pominięciem domyślnego wysyłania formularza).

* **Krok 1: Pobranie danych**
    Pobierz aktualne wartości ze wszystkich pięciu pól tekstowych w formularzu. *(Wskazówka: musisz dobrać odpowiednie selektory DOM do obejścia braku identyfikatorów w znacznikach input).*
* **Krok 2: Aplikacja stylów (CSS)**
    Zaaplikuj pobrane wartości do elementu o identyfikatorze `#box`. Wykorzystaj właściwość `.style`, aby zmienić odpowiednie reguły wizualne: wysokość, szerokość, kolor tła oraz obramowanie.
* **Krok 3: Aktualizacja treści**
    Podmień domyślną treść tekstową wyświetlaną wewnątrz elementu `#box` na tę, która została wpisana przez użytkownika w ostatnim polu formularza.

