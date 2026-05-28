// Pobranie elementów HTML do JS 
const film = document.getElementById("film")
const liczbaOs = document.getElementById("liczbaOs")
const out = document.getElementById("out")

// Funkcja onclick podpięta w html <element onclick=""> </element>
function handleLoginBtn(){
    const liczbaOsInt = parseInt(liczbaOs.value)
    if(!film.value || !liczbaOs.value){
        //wypisywanie błędu
        console.error("Podaj Dane")
        //zakończenie działania funkcji
        return
    }
    out.textContent = "koszt: " + (liczbaOsInt * 23.99).toFixed(2) + " Za film " + film.value

}                                                                            