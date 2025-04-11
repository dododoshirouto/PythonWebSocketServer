IF NOT EXIST venv (
    python -m venv venv
)

set PYTHON=.\venv\Scripts\python.exe

IF NOT EXIST _activate.bat (
    echo venv\Scripts\activate > _activate.bat
)

IF NOT EXIST main.py (
    echo # > main.py
)

IF NOT EXIST _build.bat (
    echo set PYTHON=venv\Scripts\python.exe > _build.bat
    echo %PYTHON% -m pyinstaller --onefile main.py >> _build.bat
)

IF NOT EXIST requirements.txt (
    echo # > requirements.txt
)

%PYTHON% -m pip install --upgrade pip
%PYTHON% -m pip install -r requirements.txt
