set PYTHON=.\venv\Scripts\python.exe 
@REM venv\Scripts\python.exe -m pyinstaller --onefile main.py --name "WebSocket Server"
pyinstaller --onefile main.py --name "WebSocket Server"
IF EXIST dist (
    copy /Y wstest.html dist\
)