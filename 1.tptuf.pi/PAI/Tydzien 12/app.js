const teraz = new Date()
const wakacje = new Date("06/26/2026")
//const wakacjeLepsze = new Date("2026-05-12")
//wakacjeLepsze.setHours(0)
console.dir(wakacje)
//console.dir(wakacjeLepsze)
console.dir(teraz)
teraz.setMinutes(teraz.getMinutes() + 45*3 + 10*2)
console.dir(teraz)
console.log(Math.ceil((wakacje - teraz)/ (1000 * 60 * 60 * 24) ))
// Date != Day 
// Dzien miesiąca
console.log(teraz.getDate())
// dzien tygodnia liczony od 0 gdzie 0 = Niedziela
console.log(teraz.getDay())
// miesiące tak samo wypisywane od 0 
console.log(teraz.getMonth())

const dniTygodnia =[
    "Niedziela",
    "Poniedziałek",
    "Wtorek",
    "Środa",
    "Czwartek",
    "Piątek",
    "Sobota",
]

console.log("Dziś jest: "+ dniTygodnia[teraz.getDay()])
