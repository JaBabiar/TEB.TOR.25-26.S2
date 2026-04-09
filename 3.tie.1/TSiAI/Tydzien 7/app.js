/*
document.getElementById("submit").addEventListener("click", function() {
    if(
        !document.getElementById("name").value ||
        !document.getElementById("email").value ||
        !document.getElementById("pwd").value
    ){
        console.error("Błąd Rejestracji")
        return
    }

    console.log(
        document.getElementById("name").value + " " +
        document.getElementById("email").value + " " +
        document.getElementById("pwd").value
    )
}) */
let submit = document.getElementById('submit')
let userName = document.getElementById("name")
let email = document.getElementById("email")
let pwd = document.getElementById("pwd")

submit.addEventListener("click", function(){
    if(!pwd.value || !userName.value || !email.value){
        console.error("Błąd Rejestracji")
        return
    }
    console.log(
        userName.value + " " +
        email.value + " " +
        pwd.value 
    )

})