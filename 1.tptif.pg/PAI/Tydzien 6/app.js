let ilosc = document.getElementById("ilosc")
let output = document.getElementById("output")
let waluta = document.getElementById('waluta')

console.dir(ilosc)
/*
element.addEventListener("jakas_akcja", () => {
        ...kod
    })


*/
ilosc.addEventListener("input", () => {
    obliczWaluty()
});

waluta.addEventListener("change", () => {
    obliczWaluty()
})

function obliczWaluty(){
    let przelicznik = 0
    switch (waluta.value) {
        case "eur":
            przelicznik = 7.92
            break;
        case "usd":
            przelicznik = 6.90
            break;
        case "pln":
            przelicznik = 1.85
            break;
    }
    let wynik = (ilosc.value * przelicznik)
    output.textContent = `${ilosc.value} ${waluta.value} jest rowne ${wynik} CNY`
}