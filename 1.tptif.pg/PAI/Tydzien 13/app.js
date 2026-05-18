const karty = document.querySelectorAll('.colorCard')
const checkboxy = document.querySelectorAll("input[type='checkbox']")
console.dir(checkboxy)

karty.forEach(karta => {
    karta.dataset.counter = 0
    karta.addEventListener('click', function(){
        karta.dataset.counter++
        karta.textContent = karta.dataset.counter
        console.log(karta)
    })
});