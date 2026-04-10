const output = document.getElementById("out")
const mainForm = document.getElementById("mainForm")
function klik(){
    const kolor = document.getElementById("kolor")
    output.textContent = `Zmieniono kolor tekstu na ${kolor.value}`
    output.style.color = kolor.value
    document.body.style.backgroundColor = kolor.value
    mainForm.style.boxShadow = "0px 0px 4px #000"
    mainForm.style.borderRadius = "10px"
    mainForm.style.width = "fit-content"
}