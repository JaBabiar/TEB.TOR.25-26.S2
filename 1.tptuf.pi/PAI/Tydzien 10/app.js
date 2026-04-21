
const topNav = document.getElementById("top-nav")

document.addEventListener("scroll", function(event){
    //console.dir(event.target.scrollingElement.scrollTop)
    let scrollTop = event.target.scrollingElement.scrollTop
    // /console.dir(topNav)
    if(scrollTop >= 40){
        topNav.classList.add("sticked")
        // topNav.style.opcjaCSS = "adasds"
    } else {
        topNav.classList.remove("sticked")
    }
})