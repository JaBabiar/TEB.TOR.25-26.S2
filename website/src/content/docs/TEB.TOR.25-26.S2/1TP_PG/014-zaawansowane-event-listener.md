---
title: Zaawansowane opcje EventListener
description: Najważniejsze nasłuchiwacze w JS oraz logika działania
sidebar:
  label: 14. AddEventListener
---

## Wykorzystanie EventListener 

Metode addEvent Listener wykorzystuje się na wszystkich blokach html by aktywować skrypt pisany w js po jakimś zdarzeniu np.

```js
const przycisk = document.getElementById("formSubmitBtn")

przycisk.addEventListener("click", function(e){
    
})
```

## Najważniejsze Zdarzenia 

**Myszy** 

- `click` - Po kliknięciu
- `dblclick` - Podwójne kliknięcie
- `mousover` - Po najechaniu myszką na obszar
- `mouseout` - po wyjechaniu myszką poza obszar
**Klawiatury**

**Okna**

