import random
class Manager:

    websocket_id_map = {}

    def __init__(self, uid, websocket):
        # Ajoute une correspondance entre un identifiant et le websocket
        Manager.websocket_id_map[uid] = websocket

    def show_uid(self):
        # Retourne le dictionnaire de toutes les identifiants associés aux websockets
        return Manager.websocket_id_map

    def show_t_uid(self, uid):
        # Retourne le websocket associé à l'identifiant demandé
        return Manager.websocket_id_map[uid]
    


class Client:
    id_counter = 0

    def __init__(self, websocket):
        Client.id_counter += 1                      #incrémentation du compteur pour des id dynamique
        self.id = Client.id_counter                 #attribution d'une id a l'utilisateur
        self.websocket = websocket                  #attribution du websocket
        Manager(self.id, websocket)                 #Manager va créer une correspodance entre Id et Websocket
                                                    #Utile pour le long terme si l'app devient plus grande.

    async def connect(self):
        await self.websocket.accept()               #on établie une connexion
    
    async def disconnect(self):
        await self.websocket.close()                #on ferme la connexion
        Manager.websocket_id_map.pop(self.id, None) #ici le none car on va pas se prendre la tete a chercher le websocket 
        return f"{self.id} déconnecté"              #inutile je crois, mais par principe

def generation_client():
    websocket = random.randint(1, 1000)

user = Client(generation_client())

print(user.id)    
print(user.websocket)

user = Client(generation_client())

print(user.id)    
print(user.websocket)

print(Manager.websocket_id_map)


for ws in Manager.websocket_id_map.values():
    print(ws)