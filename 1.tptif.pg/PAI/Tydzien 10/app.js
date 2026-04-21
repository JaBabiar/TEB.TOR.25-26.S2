//const blokStylowy = document.getElementById("blokStylowy")
const topBar = document.getElementById("top")
//blokStylowy.style.width = "6.7rem"
//blokStylowy.style.height = "6.7rem"
//blokStylowy.style.background = "#f0f"
//blokStylowy.classList.add("grid-view")
//blokStylowy.classList.remove("remove")

document.addEventListener("scroll", function(event){
    let scrollTop = document.scrollingElement.scrollTop
    if(scrollTop > 40){
        topBar.classList.add("sticky")
    } else { 
        topBar.classList.remove("sticky")
    }
})

document.addEventListener("blur", function(event){
    document.body.style.backgroundColor = "#67676767"
})

document.addEventListener("focus", function(event){
    document.body.style.backgroundColor = "#fff"
})