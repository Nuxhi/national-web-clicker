from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import random

#resolve the issue of unique id for each websocket connection

class Client:

    id_counter = 0
    websocket_id_map = {}

    def __init__(self):
        
        #Gestion de l'identifiant unique
        Client.id_counter += 1
        self.id = Client.id_counter
        self.webscoket = random.randint(1, 10000)
        Client.websocket_id_map[self.id] = self.webscoket

clients = []
for _ in range(5):
    client = Client()
    clients.append(client)
    print(f"Client ID: {client.id}, WebSocket ID: {client.webscoket}")


print(Client.websocket_id_map)
print(Client.websocket_id_map.values())