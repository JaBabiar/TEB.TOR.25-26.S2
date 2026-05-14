const listaZadan = document.getElementById("listaZadan")
const zadanie = document.getElementById("zadanie")
function dodajZadanie() {
    listaZadan.innerHTML += 
    `
    <div>
    <p>${zadanie.value}</p> 
    <button onclick="usunElement(${listaZadan.children.length})">Wykonane</button>
    </div>
    `
}

function usunElement(id){
  const elem =  listaZadan.children[id]
  elem.style.textDecoration = "line-through"
}