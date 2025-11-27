@echo off
cd ../Exercice4 - WebSocket/static

echo "  ____ _     ___ _____ _   _ _____ "
echo " / ___| |   |_ _| ____| \ | |_   _|"
echo "| |   | |    | ||  _| |  \| | | |  "
echo "| |___| |___ | || |___| |\  | | |  "
echo " \____|_____|___|_____|_| \_| |_|  "
echo.
echo client started at http://127.0.0.1:3000
echo.
start http://127.0.0.1:3000
python -m http.server 3000
