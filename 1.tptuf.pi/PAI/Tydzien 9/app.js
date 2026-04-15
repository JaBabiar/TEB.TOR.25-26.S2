let random = Math.random() * (6-1) + 1
let randInt = Math.round(random)


console.log(randInt);
// losowa liczba z przedziału <0;1>
// jeżeli zrobimy * max nasz przedział będzie wyglądał tak 
// < 0*max ; 1*max >
// aby dodać minimalną 
// dodajemy min do naszej losowej liczby czyli
// < 0 * max + min ; 1*max+min >
// odejmujy jeden od maksymalnej aby otrzymać liczbe maksymalną w przypadku 1
// < 0 * (max-min) - mnożenie przez 0 zawsze będzie równe 0, dodajemy minimalną
// aby otrzymać <min; 1*(max-min) + min>
// przykład od 10 do 15 
// < 0 * (15-10) + 10 ; 1 * (15-10) + 10 > 
// < 10; 15 >
// 2 opcja 

function generujCyfre(min, max){
    let random = Math.random() * (max-min+1) + min
    return Math.floor(random)
}

// Pętle For
// for (definicja zmiennej, Warunek wykonania, edycja zmiennej) 
for(let i = 1; i<=3; i++){
    console.log("Uczen " + i + " otrzymał ocene: "+ generujCyfre(1,100));
}


let ZestawKomputerowy = ["Myszka MSI", "Klawiatura MSI", "Monitor MSI", "Słuchawki MSI"]

for(let i = 1; i <= 3; i++){
    let random = generujCyfre(0,ZestawKomputerowy.length-1)
    let wylosowane = ZestawKomputerowy[random]
    console.log("Miejsce " + i + " Otrzyma " + wylosowane)
}

let kolory = ["♠", "♥", "♦", "♣"]
let karty = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

function losujKarte(){
    let kolor = kolory[generujCyfre(0,kolory.length-1)]
    let karta = karty[generujCyfre(0,karty.length-1)]

    let kolorSpan = document.getElementById("kolor")
    let wartoscSpan = document.getElementById("wartosc")

    kolorSpan.textContent = kolor
    wartoscSpan.textContent = karta
    return kolor + " " + karta
}
losujKarte()


