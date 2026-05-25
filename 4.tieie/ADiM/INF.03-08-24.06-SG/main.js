const bloki = document.querySelectorAll(".bloki")

function pokazBlok(blok){
    bloki.forEach(blok => {
        blok.style.display = "none"
    });
    const aktywnyBlok = document.getElementById(blok)
    aktywnyBlok.style.display = "block"
}

/*
function pokazBlok(blok) {
    const bloki = ["blok1", "blok2", "blok3"] definicja bloków zamiast querySelectora
    bloki.forEach(id => {
        document.getElementById(id).style.display = "none"
    })
    const wybranyBlok = document.getElementById(blok)
    wybranyBlok.style.display = "block";
}

*/