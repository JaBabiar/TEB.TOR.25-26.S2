const chatForm = document.getElementById("chatForm");
const chatContainer = document.getElementById("chatContainer");
const msg = document.getElementById("wiadomosc");
const losoweTekstyNaPodryw = ["Świetnie!",
                            "Kto gra główną rolę?",
                            "Lubisz filmy Tego reżysera?",
                            "Będę 10 minut wcześniej",
                            "Może kupimy sobie popcorn?",
                            "Ja wolę Colę",
                            "Zaproszę jeszcze Grześka",
                            "Tydzień temu też byłem w kinie na Diunie",
                            "Ja funduję bilety"]

chatForm.addEventListener("submit", function(event){
    event.preventDefault()
    //console.log(event)
    if(!msg.value){
        console.error("Łubudubu");
        return
    }

    chatContainer.innerHTML += "<div class='chat-block'> " + msg.value+ "</div>"
})