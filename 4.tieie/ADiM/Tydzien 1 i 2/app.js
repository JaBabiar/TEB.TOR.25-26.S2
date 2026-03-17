let oceny = [1,5,4,2,4]
let suma = 0
let i = 0 
oceny.forEach(el => { // = > 
    suma += el
    i += 1
});

console.log(suma)

// Obiekty 
let obiekt1 = {
  "nazwa_szkoly": "TEB Edukacja",
  "miasto": "Torun",
  "klasy": [
    {
      "symbol": "4TP",
      "profil": "Technik Programista",
      "uczniowie": [
        {
          "imie": "Jan",
          "nazwisko": "Kowalski"
        },
      ]
    }
  ]
}
console.log(obiekt1.klasy[0])


let dane = []

function skrypt1() {
    let imie = document.getElementById("imie").value
    let wiek = document.getElementById("wiek").value
    let nazwisko = document.getElementById("nazwisko").value
    let output = document.getElementById("out")
    if(!imie || !nazwisko || !wiek){ return }
    output.textContent = `Czytelnik ${nazwisko} został dodany`
    // "Ala Ma psa a Pies ma ale"
    // slice <0;2)
    let kod =  imie.slice(0,2)+ nazwisko.slice(0,2) + wiek.slice(2,)
    kod = kod.toLowerCase()
    osoba = [imie,nazwisko,kod]
    dane.push(osoba)

    console.table(dane)
    skrypt2(imie,nazwisko)
}
function skrypt2(imie, nazwisko){
    let listaCzytelnikow = document.getElementById("listaCzytelnikow")
    listaCzytelnikow.innerHTML += "<li>" + imie + " "+ nazwisko + "</li>"
}

let paliow = document.getElementById("paliow").value
paliwo = parseFloat(paliow)