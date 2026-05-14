function klikPrzycisk(){
    // Pobieranie Elementów 
    let login =  document.getElementById("login")
    let pwd = document.getElementById("pwd")
    let wiek = document.getElementById("wiek")

    // Sprawdzenie czy elementy nie istnieją 
    if(!login.value || !pwd.value || !wiek.value){
        // wypisze error w konsoli
        console.error("Brak Wszystkich danych")
        return // zakończy działanie funkcji
    }

    console.log("Login: " + login.value)
    console.log("Password: " + pwd.value)
    console.log("Age: " + wiek.value)

}