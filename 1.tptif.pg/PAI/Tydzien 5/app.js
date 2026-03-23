function obliczCyfry() {
    let dodaj = document.getElementById('dodawanie')
    let odejmij = document.getElementById('odejmowanie')
    let mnoz = document.getElementById('mnozenie')
    let dziel = document.getElementById('dzielenie')

    if (dodaj.checked == true) {
        console.log(dodaj.value)
    }
    if (odejmij.checked == true) {
        console.log(odejmij.value)
    }
    if (mnoz.checked == true) {
        console.log(mnoz.value)
    }
    if (dziel.checked == true) {
        console.log(dziel.value)
    }


    console.dir()
    //let polaRadio = document.querySelectorAll('input[name="typ"]')
    //polaRadio.forEach(pole => {
    //    if (pole.checked == true) {
    //        console.log(pole.value)
    //    }
    //});
    
    //console.log('%O', polaRadio)
}