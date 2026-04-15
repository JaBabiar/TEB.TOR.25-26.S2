## Zadanie 1 - Counter z useRef (3 pkt)

### Stwórz komponent Counter, który:

- wyświetla licznik i przyciski "+"/"-"
- używa useState do przechowywania wartości
- używa useRef do zapisania poprzedniej wartości i- wyświetlenia jej pod spodem ("Poprzednia: X")
- używa useEffect, aby aktualizować ref przy każdej- zmianie count

## Zadanie 2 - Input z auto-focus i logowaniem (3 pkt)

###Stwórz komponent SearchBox, który:

- ma pole input powiązane ze stanem (useState)
- automatycznie fokusuje pole po załadowaniu (useRef + useEffect)
- po naciśnięciu Enter wypisuje wartość w konsoli i czyści input
- wyświetla liczbę znaków poniżej pola

## Zadanie 3 - Fetch danych z useEffect (4 pkt)

### Stwórz komponent UserLoader, który:

- po załadowaniu pobiera dane z `https://jsonplaceholder.typicode.com/users/1`
- zapisuje wynik w stanie (useState)
- wyświetla loading/error/name w zależności od stanu zapytania
- używa cleanup function w useEffect, aby obsłużyć odmontowanie komponentu
