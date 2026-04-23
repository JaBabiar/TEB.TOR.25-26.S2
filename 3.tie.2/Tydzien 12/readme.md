# Zadanie do wykonania na lekcji 

## HTML 
stwórz formularz który zawiera parametry bloku 
- Szerokość
- Wysokość
- kolor
- tekst
Wszystkie jako `type=text` by ułatwić 
po czym dodaj przcisk z akcją `onclick` oraz pusty div z id `blok stylowany`
```html
    <label for="szer"></label>
    <input type="text" name="szer" id="szer">

    <button  onclick="handleOnClick()"> tekst</button>
    <div id=""></div>
```

## JS 

- Po kliknięciu w przcisk odpala się funkcja
- Funkcja pobiera parametry z naszych bloków 
- następnie ustawiamy na podstawie podanych bloków style dla `blokStylowany`


```js
    let div = document.getElementById("")
    let szer= document.getElementById("szer")
    function handleOnClick(){
        div.style.width = szer.value
    }

    
```