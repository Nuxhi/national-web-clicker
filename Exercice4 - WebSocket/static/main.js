// URL serveur FastAPI
const API_URL = "http://127.0.0.1:8000";

// Création lien de connexions au WebSocket
var wsCompteur = new WebSocket("ws://localhost:8000/ws");
var wsChat = new WebSocket("ws://localhost:8000/tchat");

//TOUT CE QUI CONCERNE LE COMPTEUR
wsCompteur.onmessage = function (event) {
  document.getElementById("Compteur").textContent = event.data;
  //A chaque fois qu'un message est reçu du serveur, on met à jour le contenu
  //de l'élément HTML avec l'ID "Compteur"
};

function incrementerCompteur() {
  wsCompteur.send("+");
  //ici on envoie le message "+" au serveur via le WebSocket
  //il va ensuite vérifié une condition puis faire le traitement
}

function decrementerCompteur() {
  wsCompteur.send("-");
  //ici on envoie le message "-" au serveur via le WebSocket
  //il va ensuite vérifié une condition puis faire le traitement
}

//TOUT CE QUI CONCERNE LE CHAT
wsChat.onmessage = function (event) {
  var messages = document.getElementById("message-du-chat");
  var message = document.createElement("li");
  var content = document.createTextNode(event.data);
  message.appendChild(content);
  messages.insertBefore(message, messages.firstChild);
  //Ajouter le nouveau message en haut de la liste (messages récents au bas, anciens au haut)

  // Limiter à 50 messages maximum
  while (messages.children.length > 11) {
    messages.removeChild(messages.lastChild);
    //Si plus de 50 messages, supprimer les plus anciens
  }
};

function sendMessage(event) {
  var input = document.getElementById("TextMessage");
  wsChat.send(input.value);
  input.value = "";

  //ici on envoie le contenu de l'input au serveur via le WebSocket
  //il va ensuite diffusé le message à tous les clients connectés au WebSocket
  //on met une valeur par défaut "" dans l'input après envoi
}
