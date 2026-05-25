let czyJedynka = false
window.addEventListener("blur", function(e){
    console.log(e)
})
window.addEventListener("focus", funkcjaFocus)


window.addEventListener("resize", function(e){
    console.log(e)
    prompt("Zostaw Te Strone w spokoju")
})

function funkcjaFocus(){
    if(!czyJedynka){
        alert("No to masz jedynke za to")
        czyJedynka = true
    }
    console.warn("Otrzymano jedynke")
}

document.addEventListener("DOMContentLoaded", function(){
    let wiek = zapytajWiek()
    let imie = zapytajImie()
    if(wiek < 18){
        document.body.style.background = "red"
    }
})

function zapytajWiek() {
    return parseInt(prompt("Ile Masz Lat"))
}

function zapytajImie() {
    return prompt("Jakie twoje imie? ")
}