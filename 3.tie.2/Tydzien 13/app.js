function wyslijGre(){
    const wydawca = document.getElementById("wydawca")
    const rok_wydania = document.getElementById("rok_wydania")
    const nazwa_gry = document.getElementById("nazwa_gry")

    if(!wydawca.value || !rok_wydania.value || !nazwa_gry.value){
        console.error("skibid");
        return
    }

    console.log(wydawca + rok_wydania + nazwa_gry)
}
