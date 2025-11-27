// URL serveur FastAPI
const API_URL = "http://127.0.0.1:8000";

// Fonction pour mettre à jour l’affichage
function afficherCompteur() {
  fetch(`${API_URL}/GetCompteur`)
    .then(response => response.json())
    .then(data => {
      document.getElementById("valeur").textContent = data.compteur;
    })
  .catch(error => console.error("Erreur:", error));
}

// Appeler afficherCompteur après que le DOM soit chargé pour s'assurer
// que l'élément #valeur existe dans la page
window.addEventListener('DOMContentLoaded', afficherCompteur);

function incrementerCompteur() {
    fetch(`${API_URL}/compteurPlus`,)
    console.log("JS Incrémenté effectué");
    afficherCompteur();
    }

function decrementerCompteur() {
    fetch(`${API_URL}/compteurMoins`)
    console.log("JS Décrémenté effectué");
    afficherCompteur();     
}

setInterval(afficherCompteur, 5000); // polling toutes les 5 secondes