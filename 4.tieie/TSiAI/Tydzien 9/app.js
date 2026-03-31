function randomDiceNumber(min, max){
    let rand = Math.random() * (max-min) + min
    let trueRand = Math.round(rand)
    return trueRand

    // 1. Losujemy od 0 do 1 
    // mnożymy ją przez 5
    // dodajemy 1 
    // Math.random() zwraca liczbe od 0 do 1 
}
let listaWynikow = []

for (let i = 0; i < 10; i++) {
    listaWynikow.push(randomDiceNumber(1,6))
}

console.log("Tablica kości: " + listaWynikow)
