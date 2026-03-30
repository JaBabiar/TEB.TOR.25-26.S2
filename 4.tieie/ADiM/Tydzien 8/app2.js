let listaDanych = ["Valorant","CS2","Brawl Stars","League of Legends","Fortnite"]

// Podstawowe Operacje

console.log(listaDanych)
// Out: Valorant
console.log(listaDanych.length)
//
console.log(listaDanych.pop())
// usuwa ostatni element i wypisuje go 
console.log(listaDanych.push("PUBG"))
//
// Usuwanie Elementu z listy 
let ie = listaDanych.indexOf("Brawl Stars")
if (ie < 0 ){
    console.error("Brak Słowa W Słowniku")
    //throw new Error("Brak słowa w Słowniku");
    
}
console.log(listaDanych.splice(ie,1)) // usuwa Brawl Stars
// splice (index elemntu usuwanego, liczba elementow do usuniecia od tego indeksu)
console.log(listaDanych)
// przedział slice działa jak <-2; -1)
console.log(listaDanych.slice(-3, -1))
