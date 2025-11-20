# national-web-clicker
a dynamic website with a useless click counter


> [!NOTE]
> Il vous sera néssaisaire d'installer les dépendances suivante :

```
-> pip install FastApi
-> Pip install Uvicorn
```

Pour lancer le programme : 
dans le dossier concerner lancer un terminal 

> cd $RepositoryFiles
> **Uvicorn main:app --reload**

> maintenant lancer un serveur qui va héberger le site web
> python -m http.serve
> sur votre navigateur : 127.0.0.1:3000 [LocalHost](http://127.0.0.1:3000/)

> [!CAUTION]
> Le serveur peux rencontrer des instabilités pendant les phases de dévelopmenet 
> En cas derreur voici comment se sortir de cette situation de terminal invinsible

dans un cmd :
```
-> netstat -ano | findstr :8000
-> taskkill /PID <pid> /F
```



