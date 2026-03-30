let kolor = document.getElementById("kolor")
let div = document.getElementById("jakisDiv")
// dla ambitnych kolor.addEventListener("change", (event) =>{
// ...
//})
kolor.addEventListener("change", function(event){
    console.log(event)
    div.style.background = kolor.value
})

div.addEventListener("mouseenter", function(){
    div.classList.add("show-border")
})
div.addEventListener("mouseleave", function(){
    div.classList.remove("show-border")
})


/// Testowanie Trybu ciemnego
let btn = document.getElementById("btn")
let body = document.getElementById("canvas")

btn.addEventListener("click", function(){
    body.classList.toggle("darkmode")
    if(btn.textContent == "tryb ciemny"){
        btn.textContent = "tryb jasny"
    } else {
        btn.textContent = "tryb ciemny"
    }
})