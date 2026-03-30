# Formularze w JS 

## Typy inputów

| TYP     | Co pobiera | Obsługa w JS |
| ----------- | ----------- | ------- |
| `type="text"` | Zwykły tekst podany przez osobe dodatkowo jako tekst pobieramy typy: email, tel.password| zmienna.value |
| `type="number"` | Pobiera cyfre | `parseInt(zmienna.value) lub parseFloat(...)`|
| `type="checkbox"` | Pobiera wartość zaznaczenia | `zmienna.checked` True albo False |
|`type="radio"`| Pobiera element zaznaczony | `zmienna.value` |
|`type="color"`| Pobiera wartość koloru w hex| `zmienna.value` |
|`type="date"`| Pobiera date |`zmienna.value` |  
|`type="range"`| Pobiera wartość z przedziału min max | parseInt lub ParseFloat |
|`type="submit"`| Wysyła akcje submit formularza | - |
## Schemat label

blok label służy do opisywania bloków input by user mógł wiedzieć co wpisać w dany input, po kliknięciu w label aktywuje się podpisany pod niego input

```html 
<label for="ID_Inputa"> tekst labela </label>
<input type="text" name="nazwa dla przeglądarki do rozpoznania" id="ID_Inputa">
```

## Obsługa zdarzeń
### Schemat 1 
```html
<form id="formId">
    <input type="text" id="tekst" name="tekst">
    <input type="submit" id="submit" name="submit" value="submit">
    <!-- lub <button> submit </button>-->
</form>

<script>
    let form = document.getElementById("loginForm")

    form.addEventListener("submit", function(e){
        e.preventDefault()
    })
<script>

```
### Schemat 2 
```html
<form>
    <input type="text" id="tekst" name="tekst">
    <button type="button" id="formSubmit"> Submit </button>
</form>

<script>
let btn = document.getElementById("formSubmit")

btn.addEventListener("click", function(){
    // kod
})
</script>
``` 