let teraz = new Date()
let wakacje = new Date("2026-06-26")
console.dir(teraz)
console.log(wakacje)
// poda nam różnice w ms
console.log( (wakacje - teraz) / (1000 * 60 * 60 * 24))

// Dzień miesiąca
console.log(teraz.getDate())

// Dzień tygodnia 
// get cos lub set cos 
console.log(teraz.getDay())
console.log(teraz.getMonth())
console.log(teraz.getFullYear())
console.log(teraz.getTimezoneOffset())
console.log("UTC ???")
teraz.setMinutes(teraz.getMinutes() + 45)

console.log(teraz.getUTCHours())
console.log(teraz.getHours())

const miesiace = ["St.", "Lu.", "Mar.", "Kw.", "Maj", "Cze." ]
const dni = [
    "Niedziela",
    "Poniedziałek",
    "Wtorek",
    "Środa",
    "Czwartek",
    "Piątek",
    "Sobota",
]
let dostawa = teraz
dostawa.setDate(teraz.getDate() + 32)
console.log("dostawa: " + dostawa.getDate() + " " + miesiace[dostawa.getMonth()])

const dzienLocal = document.getElementById("dzien-local")
dzienLocal.addEventListener("change", function(){
    let dateLocal = new Date(dzienLocal.value)
    console.log(dzienLocal.value)
    console.log(dateLocal)

})