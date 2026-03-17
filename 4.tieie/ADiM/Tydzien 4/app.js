function loginUser(){
    let login = document.getElementById("login")
    let pwd = document.getElementById("pwd")
    let rm = document.getElementById("rm")
    let output = document.getElementById("out")
    if(rm.checked){
        console.log("Dodano ciasteczka")
    }

    if(login.value == "Adrian" && pwd.value == "mango67"){
        output.textContent = "Witaj " + login.value  
    } else{
        output.textContent = "Błędne Dane"
    } 
}

document.addEventListener('submit', (e) =>{
    e.preventDefault()
})