//let data = new Date("312024")
//console.log(data)

let data = document.getElementById("data")
/*
data.addEventListener("change", () => {
    console.log(data.value)
})
*/
data.addEventListener("change", function () {
    let miesiace = ["St", "Luty", "Mar", "Kw", "Maj", "Cze", "Lip"] 
    let dni = ["Nd", "Pon", "Wt", "Śr", "Czw.", "Pt", "Sob"]
    let czas = new Date(data.value)
    console.log(czas)
    console.log(czas.getFullYear())
    console.log(miesiace[czas.getMonth()])
    console.log(czas.getDate())
})
