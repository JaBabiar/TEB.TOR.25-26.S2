let loginForm = document.getElementById('loginForm')
let output = document.getElementById("out")


loginForm.addEventListener("submit", (e) => {
    e.preventDefault();

    // Pobieramy dane z formularza 
    let login = document.getElementById('login')
    let pwd = document.getElementById('pwd')

    //Sprawdzamy czy dane isntnieją 
    console.log(login.value + ": Login")
    console.log(pwd.value + ": Password")
    // || - or (lub) 
    // && - and (oraz)
    // ! - Negacja
    if (!login.value || !pwd.value) {
        console.warn("Brak Wszystkichg danych")
        login.style.background = "rgba(255, 0, 0, 0.16)";
        pwd.style.background = "rgba(255, 0, 0, 0.16)"
        return
    }

    if(login.value == "admin" && pwd.value == "admin"){
        output.textContent = "Witaj " + login.value
        loginForm.style.display = "none"
    }
    
})