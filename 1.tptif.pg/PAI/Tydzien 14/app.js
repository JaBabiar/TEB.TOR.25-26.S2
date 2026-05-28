let czyJedynka = false
window.addEventListener("blur", function(e){
    console.log(e)
})
window.addEventListener("focus", funkcjaFocus)


window.addEventListener("resize", function(e){
    console.log(e)
    //prompt("Zostaw Te Strone w spokoju")
})

function funkcjaFocus(){
    if(!czyJedynka){
        //alert("No to masz jedynke za to")
        czyJedynka = true
    }
    console.warn("Otrzymano jedynke")
}

document.addEventListener("DOMContentLoaded", function(){
    //let wiek = zapytajWiek()
    //let imie = zapytajImie()
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


const blok = document.getElementById("blok")
const tip = document.getElementById("tip")

blok.addEventListener("click", function(){
    console.dir(this)
    this.style.width = this.clientWidth + 100 + "px"
})
blok.addEventListener("dblclick", function(){
    this.style.width = this.clientWidth - 100 + "px"
})
blok.addEventListener("mouseover", function(){
    this.style.transform = "scale(1.1)"
    tip.style.display = "block"

})
blok.addEventListener("mouseout", function(){
    this.style.transform = "scale(1)"
    tip.style.display = "none"
})