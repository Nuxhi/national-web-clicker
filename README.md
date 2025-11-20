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
> Il vous sera nécessaire d'installer les dépendances suivantes :

```powershell
pip install fastapi uvicorn
```

Si vous préférez, créez un fichier `requirements.txt` contenant :

```text
fastapi
uvicorn
```

et installez avec :

```powershell
pip install -r requirements.txt
```

**Lancer l'API (si présente)**
Dans le dossier contenant `main.py` (l'application FastAPI) :

```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

L'application sera accessible par défaut sur `http://127.0.0.1:8000`.

**Servir les fichiers statiques (UI) localement**
Pour héberger uniquement le dossier `static` sur le port 3000 (exemple) :

```powershell
cd static
python -m http.server 3000
```

sur votre navigateur : 127.0.0.1:3000 [LocalHost](http://127.0.0.1:3000/)

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
