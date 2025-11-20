from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


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





@app.get("/")
async def get():
    return HTMLResponse(html)

@app.get("/test")
async def get_count():
    return "+0+ = otot ɐ etet"

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
