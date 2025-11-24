@echo off
cd ../Exercice4 - WebSocket


echo " ____  _____ ______     _______ ____"  
echo "/ ___|| ____|  _ \ \   / / ____|  _ \ "
echo "\___ \|  _| | |_) \ \ / /|  _| | |_) |"
echo " ___) | |___|  _ < \ V / | |___|  _ < "
echo "|____/|_____|_| \_\ \_/  |_____|_| \_\"
echo.
echo server started at http://127.0.0.1:8000
echo.
uvicorn main:app --reload --host 127.0.0.1 --port 8000
