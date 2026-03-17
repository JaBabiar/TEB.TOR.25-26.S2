function loginUser(){
    let login = document.getElementById('login')
    let pwd = document.getElementById('pwd')
    let wiek = document.getElementById('wiek')

    if(!login.value || !pwd.value){
        console.error("Brak wymaganych danych")
    /*login.style.background = !login.value ?? 'red'
        pwd.style.background = !pwd.value ?? 'red' */
        return
    }
    if(wiek <= 18){
        alert("Strona przeznaczona dla pełnoletnich")
    }
    if (login.value == "nazwa_konta" && pwd.value.length > 5) {
        console.log("sukces")
    }
}