# national-web-clicker
a dynamic website with a useless click counter

pip install FastApi
Pip install Uvicorn

CD repo
Uvicorn main:app --reload

en cas de crash :
dans un cmd : netstat -ano | findstr :8000
puis taskkill /PID <pid> /F

start index.html hors host a static server for the page
python -m http.serve and start 127.0.0.1:3000

