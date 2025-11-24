from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:3000"] pour limiter
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#L'IP DU SERVEUR DOIT ETRE http://127.0.0.1:8000
compteur = 0 #on met la valeur du compteur a 0 a chauqe démarage du serveur
clients = set()

###################################################
##  NNote POUR MOI MEME :                     ##
# il y'a 2 systèmes de websocket dans ce code :
# - un pour le compteur (route /ws)
# - un pour le tchat (route /tchat)
# CEPENDANT LA GESTION ET LE MANGEMENT DES DEUX SYSTEMES
# SONT INDEPENDANT Lun DE L'AUTRE.
# IL FAUT DONC BIEN FAIRE ATTENTION A NE PAS MELANGER
# C'EST CATASTROPHIQUE !!!!!!!!!!!!
###################################################



##################################################
# SYSTEM DE TCHAT WEBSOCKET POUR APPRRENDRE      #
##################################################

#################################################
# Classe utilse a la gestion du chat, Id, Ws
#################################################

class Manager:

    websocket_id_map = {}

    def __init__(self, uid, websocket):
        # Ajoute une correspondance entre un identifiant et le websocket
        Manager.websocket_id_map[uid] = websocket


###########################################################
#SI MANAGER EST DETRUIT PLUS RIEN NE FONCTIONNE !!!!!!!!!!!
###########################################################

class Client:
    id_counter = 0

    def __init__(self, websocket: WebSocket):
        Client.id_counter += 1                      #incrémentation du compteur pour des id dynamique
        self.id = Client.id_counter                 #attribution d'une id a l'utilisateur
        self.websocket = websocket                  #attribution du websocket
        Manager(self.id, websocket)  #/!\           #Manager va créer une correspodance entre Id et Websocket
                                                    #Utile pour le long terme si l'app devient plus grande.

    async def connect(self):
        await self.websocket.accept()               #on établie une connexion
    
    async def disconnect(self):
        try:
            await self.websocket.close()
        except:
            pass  # ignore si websocket déjà fermé  

        Manager.websocket_id_map.pop(self.id, None)
        return f"{self.id} déconnecté {Manager.websocket_id_map.values()}"





###################
# route du serveur 
###################

################################
## EXERCICE WEBSOCKET
################################

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    global compteur
    await ws.accept()
    clients.add(ws)

    # envoie la valeur actuelle
    await ws.send_text(str(compteur))

    try:
        while True:
            msg = await ws.receive_text()

            if msg == "+":
                compteur += 1
            elif msg == "-":
                compteur -= 1

            await broadcast()

    except WebSocketDisconnect:
        clients.discard(ws)


################################
## BONUS POUR APPRENDRE
################################

##route system
@app.get("/")
async def get():
    return "/go to 127.0.0.1:3000, si vous n'etes pas membre du system vous n'avez rien a faire ici ♥ ps : +0+ = otot ɐ etet"

@app.websocket("/tchat")
async def websocket_endpoint(websocket: WebSocket):
    user = Client(websocket)                #on créer un objet user de la classe Client
    await user.connect()                    #on demande a la classe d'établie une connexion
    

    #/!\ attention, aucune gestion de suppresion de websocket mort présent dans le code
    #alors on ignore les erreurs d'envoi afin d'éviter le crash du serveur

    for ws in Manager.websocket_id_map.values():      #on notifie tous les clients connectés qu'un nouveau client est connecté
        await ws.send_text(f"client {user.id} connecté")
    

    #Gestion de l'envoie de message
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast à tous
            for ws in Manager.websocket_id_map.values():
                 await ws.send_text(f"Client {user.id} : {data}")
                    
    except WebSocketDisconnect:
        
        message = await user.disconnect()
        # Notifier tous les autres clients de la déconnexion
        for ws in Manager.websocket_id_map.values():
            await ws.send_text(message)

        print(message)


async def broadcast():
    """Envoie la valeur du compteur à tous les clients."""
    for ws in list(clients):
        try:
            await ws.send_text(str(compteur))
        except:
            clients.discard(ws)

