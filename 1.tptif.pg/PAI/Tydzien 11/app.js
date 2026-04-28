let iin = document.getElementById("iin");
let email = document.getElementById("email");
let sport = document.getElementById("sport");

function jakasFunkcjaJol() {
    console.log("---Rejestracja---");

    if(!iin.value || !email.value || !sport.value){
        console.error("!!!!!Nie podano wszystkich danych!!!!!");
        return;
    }
    console.log("Imie i Nazwisko: " + iin.value);
    console.log("Email: " + email.value);
    console.log("Sport: " + sport.value);

    // tego niżej nie będzie 
    iin.value = ""
    email.value = ""
    sport.value = ""

}