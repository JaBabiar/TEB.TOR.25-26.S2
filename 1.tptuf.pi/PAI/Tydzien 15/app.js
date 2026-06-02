/*
Metoda szybsza bez pobierania elementów formularza osobno,
sprawdza stan całego bloku

function handleFormSubmit() {
    event.preventDefault()
    let formChild = event.target.children
    console.log(formChild.nick.value)
    console.log(formChild.klasa.value)
}
formChild - Pobrane z target dzieci formularza
formChild.id_dziecka.value - pobiera wartość danego pola input

*/

const mainForm = document.getElementById("mainForm")
const nick = document.getElementById("nick")
const klasa = document.getElementById("klasa")
const listaGraczy = document.getElementById("listaGraczy")

mainForm.addEventListener("submit", function(e){
    e.preventDefault()
    console.dir(this)
    if(!nick.value || !klasa.value){
        console.error("Niedałesdanych")
        return
    }

    listaGraczy.innerHTML += "<li>"+ nick.value+"</li>"
})


