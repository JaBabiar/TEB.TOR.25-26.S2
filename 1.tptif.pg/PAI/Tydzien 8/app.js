/* loginForm.addEventListener("submit", () => {
    ..
    })
*/
let form = document.getElementById("loginForm")
console.log(form)

form.addEventListener("submit", function(e) {
    e.preventDefault()
    let login = document.getElementById("login")
    let pwd = document.getElementById("pwd")

    console.log(login.value, pwd.value)
})

 