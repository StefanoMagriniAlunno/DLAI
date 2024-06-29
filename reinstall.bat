@echo off

REM Inizializza le variabili
set "python_path="

REM Controlla se è stato fornito un argomento
if "%~1" neq "" (
    set "python_path=%~1"
)

REM Elimino la vecchia cartella .venv
rmdir /s /q .venv
if errorlevel 1 (
    echo ERROR: An error occurred while removing .venv
    exit /b 1
)

REM Ripeto l'installazione
echo Install repo with path %python_path%, wait a few minutes...
call install.bat "%python_path%"
if errorlevel 1 (
    echo ERROR: An error occurred while reinstalling the repository
    exit /b 1
)

exit /b 0
