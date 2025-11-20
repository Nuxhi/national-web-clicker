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
compteur = 50 #on met la valeur du compteur a 0 a chauqe démarage du serveur




#################################################
# Classe utilse a la gestion du chat, Id, Ws
#################################################

class Manager:

    websocket_id_map = {}

    def __init__(self, uid, websocket):
        # Ajoute une correspondance entre un identifiant et le websocket
        Manager.websocket_id_map[uid] = websocket

    #actuellement inutile
    def show_t_uid(self, uid):
        # Retourne le websocket associé à l'identifiant demandé
        return Manager.websocket_id_map[uid]
    


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


##route system
@app.get("/")
async def get():
    return "/go to 127.0.0.1:3000, si vous n'etes pas membre du system vous n'avez rien a faire ici ♥"

@app.get("/test")
async def get_count():
    return "+0+ = otot ɐ etet"


##Route compteur
@app.get("/GetCompteur")
def get_compteur():
    '''
    Permet de mettre a jours la valeur du compteur
    enlever le system du polling !!!! 
    '''
    global compteur
    return {"compteur": compteur}


@app.get("/compteurPlus")
async def lire_compteur_plus():
    '''
    incrémente le compteur de 1
    '''
    global compteur
    compteur += 1
    for uid,ws in Manager.websocket_id_map.items():
        try:
            await ws.send_text(json.dumps({"type": "compteur", "value": compteur}))
        except:
            pass
    # broadcast aux clients connectés
    # on envoie un JSON indiquant le type "compteur"
    return {"compteur": compteur}


@app.get("/compteurMoins")
async def compteur_moins():
    '''
    décrémente le compteur de 1
    '''
    global compteur
    compteur -= 1
    return {"compteur": compteur}



@app.websocket("/ws")
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


