function jakasaNaszaFunkcja(){
    // let nazwa_zmiennej = 
    // document.getElememtById() -- Pobiera cały element HTML wraz z jego parametrami takimi jak .textContent
    let sp = document.getElementById("sp")
    let sk = document.getElementById("sk")
    let output = document.getElementById("output")
    // ! - negacja
    // !sp.value - sprawdzenei czy wartość jest pusta
    // console.error("") - wipisze w konsoli przeglądarki
    // && - And (i) || - Or (lub)
    if(!sp.value && !sk.value){
        console.error("Błędne dane");
        return // kończy działanie funkcji 
    }
    //można zastąpić innerText/innerHTML
    output.textContent = "Pociąg jedzie z " + sp.value + " do " + sk.value
    if(sk.value == "Torun"){
        output.textContent = "Witaj w Domu"
    }
}