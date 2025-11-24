// URL serveur FastAPI
const API_URL = "http://127.0.0.1:8000";

// Création lien de connexions au WebSocket
var wsCompteur = new WebSocket("ws://localhost:8000/ws");
var wsChat = new WebSocket("ws://localhost:8000/tchat");

//TOUT CE QUI CONCERNE LE COMPTEUR
wsCompteur.onmessage = function (event) {
  document.getElementById("Compteur").textContent = event.data;
};

function incrementerCompteur() {
  wsCompteur.send("+");
}

function decrementerCompteur() {
  wsCompteur.send("-");
}

//TOUT CE QUI CONCERNE LE CHAT
wsChat.onmessage = function (event) {
  var messages = document.getElementById("message-du-chat");
  var message = document.createElement("li");
  var content = document.createTextNode(event.data);
  message.appendChild(content);
  messages.appendChild(message);
};

function sendMessage(event) {
  var input = document.getElementById("TextMessage");
  wsChat.send(input.value);
  input.value = "";
  event.preventDefault();
}
