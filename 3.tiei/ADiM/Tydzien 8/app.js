const login = document.getElementById('login')
const pwd = document.getElementById('pwd')
const submitForm = document.getElementById('submitForm')

submitForm.addEventListener("submit", function(e){
    e.preventDefault()
    if(!login.value || !pwd.value){
        console.error("Brak danych");
        return
    }

    if(login.value == "Admin" && pwd.value == "123"){
        console.log("Zalogowano")
    }
})

function clickAction(){
    if(!login.value || !pwd.value){
        console.error("Brak danych");
        return
    }

    if(login.value == "Admin" && pwd.value == "123"){
        console.log("Zalogowano")
    }
}