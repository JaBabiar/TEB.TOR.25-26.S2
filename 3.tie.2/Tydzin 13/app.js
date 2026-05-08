let teraz = new Date()
let kiedys = new Date(teraz.getTime())
// metody setter i getter
kiedys.setDate(teraz.getDate() + 4)
console.log(kiedys)
// przekształcamy milisekundy na dni 
// 1s = 1000ms ...
console.log( (kiedys - teraz) / (1000 * 60 * 60 * 24))

// Nazwy dni/ miesięcy 

let miesiace = [
    "Styczen", "Luty", "Marzec", "Kwiecien", 
    "Maj", "Czerwiec", "Lipiec", "Sierpien",
    "Wrzesien", "Pazdziernik", "Listopad", "Grudzien",
]
console.log(miesiace[teraz.getMonth()])

// dni zaczynamy od niedzieli (system amerykanski)
let dzien = [
    "Niedziela", "Poniedziałek", 
    "Wtorek", "Środa",
    "Czwartek", "Piątek", "Sobota"
]
console.log(dzien[teraz.getDay()])

// pobieranie danty z html i sprawdzenie ile dni do wakacji
const poleDaty = document.getElementById("poleDaty")

poleDaty.addEventListener("change", function(){
    let odKiedy = new Date(poleDaty.value)
    // ustawiamy godzine na 0000 utc 
    odKiedy.setHours(0,0,0,0)
    const wakacje = new Date("06.26.2026")
    let doWakacji = wakacje - odKiedy
    console.log(doWakacji / (1000 * 60 * 60 * 24))
})