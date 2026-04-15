const output = document.getElementById("out")
const mainForm = document.getElementById("mainForm")
const subForm = document.getElementById("subForm")

subForm.addEventListener("submit", function(e){
    e.preventDefault()
    const r = document.getElementById("red")
    const g = document.getElementById("green")
    const b = document.getElementById("blue")

    document.body.style.backgroundColor = `rgb(${r.value}, ${g.value}, ${b.value})`

})

function klik(){
    const kolor = document.getElementById("kolor")
    output.textContent = `Zmieniono kolor tekstu na ${kolor.value}`
    output.style.color = kolor.value
    //document.body.style.backgroundColor = kolor.value
    mainForm.style.boxShadow = "0px 0px 4px #000"
    mainForm.style.borderRadius = "10px"
    mainForm.style.width = "fit-content"
}