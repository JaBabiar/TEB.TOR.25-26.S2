
//pobranie przycisków wyboru postaci
const buttons = document.querySelectorAll(".champ-btn");
// pobranie bloków po id
const selectedName = document.querySelector("#selected-name")
const selectedTitle = document.querySelector("#selected-title")
const champSplash = document.querySelector("#champ-splash")

buttons.forEach(btn =>{
    btn.addEventListener('click', function(){
        //pobranie danych z data- w przycisku
        let champName = btn.dataset.name;
        let champTitle = btn.dataset.title;
        let champImg = btn.dataset.image;
        let sound = btn.dataset.audio

        new Audio(sound).play()
        //zmiana tekstu w polu wybranej postaci
        selectedName.textContent = champName;
        selectedTitle.textContent = champTitle;
        //zmiana obrazu oraz tekstu alt 
        champSplash.src = champImg
        champSplash.alt = "Portret " + champName
        champSplash.style.display = "block"
    })
})