let teraz = new Date();
let kiedys = new Date("20 May 2026")
teraz.setTime
const dniTygodnia =
[
    "Niedziela",
    "Poniedziałek",
    "Wtorek",
    "Środa",
    "Czwartek",
    "Piątek",
    "Sobota",
]
let dzien = teraz.getDay()
console.log(dniTygodnia[dzien])
console.log(teraz.toTimeString())
let konwersja = (kiedys - teraz)
konwersja /= 1000 * 60 * 60* 24


let newDate = new Date(teraz)
newDate.setFullYear(teraz.getFullYear() + 10)

console.log(newDate.toDateString())

const obraz = document.getElementById("lala")
console.dir(obraz)