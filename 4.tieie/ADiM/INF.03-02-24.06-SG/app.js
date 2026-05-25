const chat = document.getElementById("chat");
const msg = document.getElementById("messageInput");
const replies = [
    "Hej, świetnie!",
    "Nie mogę się doczekać!",
    "Co jeszcze planujemy?",
    "Może później?",
    "Dobra decyzja!",
    "Zgadza się.",
    "Brzmi dobrze.",
    "Ciekawy pomysł!",
    "Spróbujmy!"
];

function sendMessage(){
    chat.innerHTML += `<div class='message jolanta'> 
    <img src='Krzysiek.jpg' alt='Jolanta Nowak'> <p>
    ${msg.value} </p> </div>`
}

function generateRandomReply(){
    const randomNumber = Math.floor(Math.random() * replies.length);
    chat.innerHTML += `<div class='message krzysztof'> 
    <img src='Krzysiek.jpg' alt='Krzysztof Łukasiński'> <p>
    ${replies[randomNumber]} </p> </div>`
}