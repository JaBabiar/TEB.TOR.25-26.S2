let obrazy = document.querySelectorAll(".zdj")
const mainObraz = document.getElementById("mainObraz")

//obrazy.forEach(element => {
//    element.addEventListener("click", function(){
//        mainObraz.src = this.src
//    })
//});

function choiceImg(imgSrc) {
    console.log(imgSrc) 

    
    let img = document.getElementById("choiceImg");
    if (imgSrc == "1m.bmp") {
        img.src = "1d.bmp";
    } else {
        img.src = "2d.bmp";
    }
}
