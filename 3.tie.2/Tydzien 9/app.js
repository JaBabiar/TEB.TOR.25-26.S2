function jakasaNaszaFunkcja(){
    // let nazwaZmiennej = document.getElementById("ID_INPUTA")
    // pobiera to element HTML do zmiennej sp
    // Element HTML posiada funkcje oraz dane zapisywane 
    // np sp.textContent - tekst w danym bloku, sp.value - wartość inputa
    let sp = document.getElementById("sp")
    let sk = document.getElementById("sk")
    // ! - negacja !prawda = fałsz 
    // && - AND oba warunki muszą zostać spełnione 
    // || - OR jeden z warunków musi zostać spełniony 
    if(!sp.value || !sk.value){
        //wypisze w konsoli na czerowono
        console.error("Brak wymaganych danych")
        return // zakończy działanie funkcji z powodu błędu 
    }
    // edytuje zmienną output z parametrem textContent ustawiając ją na 
    // dynamiczne generowany tekst 
    output.textContent = "Pociąg jedzie z " + sp.value + " do " + sk.value
}

///Warunek mniejsze i większe 
// if (ocena.value => 1 && ocena.value <= 6)