const blok1 = document.getElementById("blok1")
const blok2 = document.getElementById("blok2")
const blok3 = document.getElementById("blok3")
const blok4 = document.getElementById("blok4")

const bloki = document.querySelectorAll("body > div")
bloki.forEach(blok => {
    blok.addEventListener("click", function(){
        console.dir(blok.dataset)
    })
});

