/*function klik(){
    if (
        !document.getElementById("name").value ||
        !document.getElementById("pwd").value||
        !document.getElementById("email").value

    ) {
        console.error("Brak danych!")
        return
    }

    console.log(
        document.getElementById("name").value + 
        document.getElementById("pwd").value + 
        document.getElementById("email").value
    )
}*/

let userName = document.getElementById("name")
let pwd = document.getElementById("pwd")
let email = document.getElementById("email") 

function klik(){
    if(!userName.value || !pwd.value || !email.value){
        console.error("Błąd")
        return
    }

    console.log(userName.value + pwd.value + email.value)
}