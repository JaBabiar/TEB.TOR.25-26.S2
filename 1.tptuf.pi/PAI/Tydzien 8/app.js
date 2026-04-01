let form = document.getElementById("formLogin");

function nazwaFunkcji(e) {
    e.preventDefault();
    console.log("Formularz został wysłany");

    let name = document.getElementById("name").value;
    let date = document.getElementById("date").value;
    // || - operator logiczny OR, zwraca true jeśli przynajmniej jeden z operandów jest prawdziwy
    // "" - pusty string, wartość falsy (fałszywa) w JavaScript, oznacza brak tekstu
    // && - operator logiczny AND, zwraca true tylko jeśli oba operandy są prawdziwe
    // ! - operator logiczny NOT, zwraca true jeśli operand jest falsy, a false jeśli operand jest truthy
    if (name == "" || date == "") {
        console.error("Nie podano imienia lub daty");
        return false
    }
    
    
    
    console.log(name + " Ur. " + date);
    return false
}
// https://github.com/JaBabiar/TEB.TOR.25-26.S2