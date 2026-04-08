# INF 03 - JS na Egzamin

## Podstawowe typy zmiennych

### String (tekstowa)

> *Podczas pobierania danych z HTML każda zmienna jest brana jako tekstowa

#### Podstawowe Operacje

```javascript
let zmiennaTekstowa = "Lorem Ipsum"

zmiennaTekstowa[0] // Wypisze litere na podanym indeksie (licząc od zera), 0 = L, 1 = o...
zmiennaTekstowa + zmiennaTekstowa // Wypisze zmienne obok siebie jako jeden tekst "Lorem IpsumLorem Ipsum"
zmiennaTekstowa + "tekst" // Zadziała w ten sam sposób

```

#### Podstawowe Funkcje

```Javascript
let zmiennaTekstowa = "Lorem Ipsum"

zmiennaTekstowa.toLowerCase() // Wypisze wszystko z małej litery
zmiennaTekstowa.toUpperCase() // Wypisze wszystko wielkimi literami


```

### INT i Float (Numeryczne)

```javascript
let number = 8


```

## Pętle For i While

## pobieranie danych z formularza

## Wypisanie danych do HTML

Wypisanie danych naszego skryptu do pliku html może odbyć się na dwa sposoby `.textContent` oraz `.innerHTML`
na potrzeby egzaminu łatwiejszą metodą będzie `.innerHTML` ze względu na to że interpretuje ona kod HTML jako osobne elementy więc `"<p> lorem </p>"` doda nam paragraf z tekstem lorem. W przypadku `.textContent` nie zostanie dodany nowy element tylko wypisane zostanie wszystko dosłownie

> *innerHTML jest odradzane ze względu na bezpieczeństwo, w momencie gdy użytkownik ma kontrole nad wypisanimi danymi jest on w stanie wkleić na stronę niechciane skrypty lub wykraść dane

## Edycja Stylów za pomocą JS

do edycji styl za pomocą js można podejść za pomocą dwóch metod, pierwszą z nich jest edycja bezpośrednia,
na elemencie za pomocą `element.style.parametrcss`, jest ona najbardziej specyficzną metodą co oznacza że będzie zawsze działałą i będzie brana pod uwagę ponad style klas, drugą opcją jest dodanie klasy, daje to nam więcej kontroli ze względu na to że nie musimy zmieniać całego kotu js, wystarczy wprowadzenie zmian w css, lecz jest to kosztem specyficzności, jeżeli coś zostanie ustalone na elemencie wtedy style klas nie będą działały poprawnie 

```javascript
let jakisElement = document.getElementById("ID Elementu")

jakisElementy.style.background = "blue" // zmienniamy kolor tła na niebieski
jakisElement.style.fontFamily = "Comic Sans MS" // zmieniamy czcionkę na Comic Sans 


jakisElement.addClass("klasa") // Dodamy klase css do elementu 
jakisElement.removeClass("klasa") // Usuniemy klase z Elementu 
jakisElement.toggleClass("kalsa") //klasa css zostanie usunięta lub dodana


```
