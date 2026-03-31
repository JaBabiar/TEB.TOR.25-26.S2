let tekst = "string"
let cyfra = 3
let bool = true // false 1/0
let lista = [5,6,"jajco",2,1]
let obiekt = {
    "imie": "Jan",
    "nazwisko": "Javascript",
    "oceny": [4,3,2,1]
}
let tekstowaCyfra = "16"

// Operacje na zmiennych 

/// Tekstowe 
console.log(tekst)

//// pobieranie litery 
console.log(tekst[0])

console.log(tekst.toLowerCase())
console.log(tekst.toUpperCase())
console.log(tekst + " to typ danych")
/// cyfry 
console.log(cyfra + cyfra) // +, -, *, %
console.log("Wynik modulo: " + cyfra%2)

console.log(parseFloat(tekstowaCyfra) + parseInt(tekstowaCyfra))
console.log(tekstowaCyfra >= 16)
/// Listy 
console.log(lista[0])
console.log(lista +"przed zmiana"+ lista.pop() + "po zmianie: " + lista)
lista.push("jajko")
console.log(lista)

let index = lista.indexOf("jajco")
lista.splice(index, 1)

// <Index początkowy ; Index Koncowy)`
console.log(lista.slice(0, 3))

///Matematyka 

console.log(lista.length + " Długosc listy")

/// Obiekty
console.log(obiekt.imie + " " + obiekt.nazwisko + "ma oceny: " + obiekt.oceny)

/// Instrukcje warunkowe 

if(tekst == "strng"){
    console.log("Prawda")
} else {
    console.table(obiekt)
}

let out = document.getElementById('output')
console.dir(out)

for (let i = 1; i <= 10; i++) {
    if(i%2==0){
        out.innerHTML += "<span class='big red'>" + i +"</span>";
    } else {
        out.innerHTML += i + " ";
    }
}

console.log("cały out: " + out.textContent)
