// URL serveur FastAPI
const API_URL = "http://127.0.0.1:8000";

// Appeler afficherCompteur après que le DOM soit chargé pour s'assurer
// que l'élément #valeur existe dans la page
window.addEventListener("DOMContentLoaded", afficherCompteur);

// Fonction pour mettre à jour l’affichage
function afficherCompteur() {
  fetch(`${API_URL}/GetCompteur`)
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("compteur").textContent = data.compteur;
      console.log("JS Affichage effectué");
    })
    .catch((error) => console.error("Erreur:", error));
}

function incrementerCompteur() {
  fetch(`${API_URL}/compteurPlus`);
  console.log("JS Incrémenté effectué");
  afficherCompteur();
}

function decrementerCompteur() {
  fetch(`${API_URL}/compteurMoins`);
  console.log("JS Décrémenté effectué");
  afficherCompteur();
}

//TOUT CE QUI CONCERNE LE CHAT
var ws = new WebSocket("ws://localhost:8000/ws");
ws.onmessage = function (event) {
  var messages = document.getElementById("message-du-chat");
  var message = document.createElement("li");
  var content = document.createTextNode(event.data);
  message.appendChild(content);
  messages.appendChild(message);
};

function sendMessage(event) {
  var input = document.getElementById("TextMessage");
  ws.send(input.value);
  input.value = "";
  event.preventDefault();
}
