@echo off
REM ###############################################################
REM # This script removes a module from the project.
REM #
REM # Params: %0 <path_to_module>
REM #       - path_to_module: the path to the module to remove
REM #
REM #   Note: the module is removed from the sources directory.
REM ###############################################################

:show_help
echo This script removes a module from the project.
echo.
echo Params: %0 ^<path_to_module^>
echo       - path_to_module: the path to the module to remove
echo.
echo Note: the module is removed from the sources directory.
goto :eof

if "%~1"=="" (
    call :show_help
    exit /b 0
)

REM Leggo il parametro con il path del modulo da rimuovere
set "MODULE_PATH=%~1"

REM Se il modulo non esiste in sources lancio un'eccezione
if not exist "sources\%MODULE_PATH%" (
    echo ERROR: sources\%MODULE_PATH% not found.
    .venv\Scripts\python.exe assets\finish_error.py
    exit /b 1
)

REM Rimuovo il modulo
rd /s /q "sources\%MODULE_PATH%"
if errorlevel 1 (
    echo ERROR: An error occurred while removing the module from sources.
    .venv\Scripts\python.exe assets\finish_error.py
    exit /b 1
)

REM Riporto in scripts\events\history.log il comando eseguito
echo rem mod %MODULE_PATH%>> scripts\events\history.log

REM Eseguo lo script di completamento
.venv\Scripts\python.exe assets\finish_scripts.py

echo Module %MODULE_PATH% removed successfully
exit /b 0
