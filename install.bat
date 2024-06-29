@echo off

REM Inizializza le variabili
set python_cmd=python
set pip_version=24.1.1
set virtualenv_version=20.26.3

REM Controlla se è stato fornito un argomento
if "%~1" neq "" (
    set python_cmd=%~1\python.exe
)

REM Aggiorno pip a %pip_version%
%python_cmd% -m pip install --upgrade pip==%pip_version% --quiet --no-warn-script-location
if errorlevel 1 (
    echo ERROR: An error occurred while installing pip %pip_version%
    %python_cmd% assets/finish_error.py
    exit /b 1
)

REM Installo con pip virtualenv %virtualenv_version%
%python_cmd% -m pip install --user virtualenv==%virtualenv_version% --quiet --no-warn-script-location
if errorlevel 1 (
    echo ERROR: An error occurred while installing virtualenv %virtualenv_version%
    %python_cmd% assets/finish_error.py
    exit /b 1
)

REM Inizializzo la repository
%python_cmd% -m virtualenv .venv --pip=%pip_version%
if errorlevel 1 (
    echo ERROR: An error occurred while creating .venv
    %python_cmd% assets/finish_error.py
    exit /b 1
)

echo SUCCESS: environment created
echo Installing base package, wait a few minutes...

REM Cambio il path di python
.venv\Scripts\python.exe -m pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo ERROR: An error occurred while installing requirements.txt
    .venv\Scripts\python.exe assets/finish_error.py
    exit /b 1
)

.venv\Scripts\pre-commit.exe install --quiet
if errorlevel 1 (
    echo ERROR: An error occurred while installing pre-commit-config.yaml
    .venv\Scripts\python.exe assets/finish_error.py
    exit /b 1
)

.venv\Scripts\pre-commit.exe install-hooks --quiet
if errorlevel 1 (
    echo ERROR: An error occurred while installing hooks
    .venv\Scripts\python.exe assets/finish_error.py
    exit /b 1
)

REM Aggiungo le cartelle che potrebbero non esserci
md builds data data\out data\images data\audios data\videos data\db libs logs scripts scripts\events temp tools tests
type nul > scripts\events\history.log
type nul > logs\user.log
type nul > logs\dev.log

echo SUCCESS: base package installed
echo Installing custom packages, wait a few minutes...

REM Installo i pacchetti dinamici per il progetto
.venv\Scripts\invoke.exe install > packages.log
if errorlevel 1 (
    echo ERROR: An error occurred while installing packages
    .venv\Scripts\python.exe assets/finish_error.py
    exit /b 1
)

.venv\Scripts\invoke.exe download > downloads.log
if errorlevel 1 (
    echo ERROR: An error occurred while downloading data
    .venv\Scripts\python.exe assets/finish_error.py
    exit /b 1
)

echo SUCCESS: custom packages installed

REM Preparo builds
make --silent

REM Preparo scripts
xcopy templates\_scripts_windows\* scripts\ /s /e /y

REM Controllo la repository
.venv\Scripts\pre-commit.exe run --all-files

REM Finish
.venv\Scripts\python.exe assets/finish_install.py
echo You can now run the project with:
echo Please, activate the environment:
echo     .venv\Scripts\activate

exit /b 0
