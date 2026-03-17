let elementy = ["element723", "element2", "element63", "elem2", "elem231", "elem54"];
console.log(elementy[0])
console.log(elementy.length + " Ilosc elementów")
elementy.push("element4") // dodaje na konice
elementy.pop() // usuwa ostatni element



// Usuwanie Elementu 
let t = elementy.indexOf("element2")
elementy.splice(t,1) // wytnij ze środka
console.dir(elementy)

console.log(elementy.join("-"))
// <0;1)
elementy.slice(0,1)
console.log(elementy.slice(0,1))

elementy.sort()
console.log(elementy)

// Wypisywanie Elementów w HTML
let output = document.getElementById("out")

for(let i =0; i<elementy.length; i++){
    console.log(i)
    
    output.innerHTML += "<div class=card>" + elementy[i]+"</div>"
}
