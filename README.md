# national-web-clicker

Un petit site web dynamique avec un compteur de clics (projet pédagogique).

**Aperçu**

- Site statique servi depuis le dossier `static`.
- Backend possible avec `FastAPI` (fichiers `main.py` dans les exercices).

**Prérequis**

- Python 3.8+ installé
- `pip` disponible

**Installer les dépendances**
Exécuter ces commandes dans PowerShell ou un terminal :

> [!NOTE]
> Si vous souhaitez **gagner** du temps :
> Lancez le fichier `install.cmd` puis `StartProject.cmd`.
> Cela **met à jour** vos dépendances Python, installe les dépendances requises, et lance le serveur ainsi que le client.
> Sinon, suivez le processus suivant :



> [!NOTE]
> Il vous sera nécessaire d'installer les dépendances suivantes :

```powershell
pip install fastapi uvicorn
ou
pip install -r requirements.txt
```
ou sinon lancer le fichier `install.cmd`

**Lancer l'API (si présente)**
Dans le dossier contenant `main.py` (l'application FastAPI) :

```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

L'application sera accessible par défaut sur `http://127.0.0.1:8000` -> [serveur](http://127.0.0.1:8000/).

**Servir les fichiers statiques (UI) localement**
Pour héberger uniquement le dossier `static` sur le port 3000 (exemple) :

```powershell
cd static
python -m http.server 3000
```

sur votre navigateur : `127.0.0.1:3000` -> [LocalHost](http://127.0.0.1:3000/)

> ou sinon lancer le `StartProject.cmd`
> (lancement uniquement du projet en websocket ici)

## ATTENTION CECI EST TRES UTILE : 


**Dépannage / arrêter un serveur bloqué (Windows)**
Si le port (par exemple `8000`) est déjà utilisé :

```powershell
netstat -ano | findstr :8000
# notez le PID retourné, puis
taskkill /PID <pid> /F
```

Remplacez `<pid>` par le numéro de processus trouvé.

**Conseils**

- Utilisez `--reload` avec `uvicorn` uniquement en développement.
- Pour la production, préférez un process manager (par ex. systemd) ou un serveur ASGI complet.
