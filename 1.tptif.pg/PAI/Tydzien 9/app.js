//let random = Math.random() * (6 - 1) + 1
// Math.random() * (max - min) + min
//let randomInt = Math.round(random)
//console.log(randomInt)
let lista = ["Auto", "Rower", "Autobus"]

function graj(min, max) {
   let wynik = Math.random() * (max - min) + min
   wynik = Math.round(wynik)
   return wynik
}
// for(definicja zmiennej początkowej np let i = 10;
//     warunek wykonania np i < 10; 
//     edycja zmiennej zainicjowanej na początku np. i++)
function gra(iloscPowt){
   for(let i = 1; i < iloscPowt; i++){
      console.log("Uczen: " + i + " Otrzymał ocene " +graj(1,6))
   }
}
gra(10)

let iloscPowtWhile = 10
let i = 1
do {
   console.log(i)
   i++
} while (i < iloscPowtWhile);