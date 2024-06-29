@echo off
REM ###############################################################
REM # This script removes a library from the project.
REM #
REM # Params: %0 <library_name>
REM #       - library_name: the name of the library to remove
REM #
REM #   Note: the library is removed from the builds directory,
REM #         the makefile is updated to remove the library and
REM #         the library is removed from the libs directory.
REM ###############################################################

:show_help
echo This script removes a library from the project.
echo.
echo Params: %0 ^<library_name^>
echo       - library_name: the name of the library to remove
echo.
echo Note: the library is removed from the builds directory,
echo       the makefile is updated to remove the library and
echo       the library is removed from the libs directory.
goto :eof

if "%~1"=="" (
    call :show_help
    exit /b 0
)

REM Nome della libreria
set "LIBRARY_NAME=%~1"

REM Rimuovo la cartella builds\%LIBRARY_NAME%
rd /s /q "builds\%LIBRARY_NAME%"
if errorlevel 1 (
    echo ERROR: An error occurred while removing the directory builds\%LIBRARY_NAME%
    .venv\Scripts\python.exe assets\finish_error.py
    exit /b 1
)

REM Rimuovo occorrenze da makefile
powershell -Command "(Get-Content makefile) -notmatch 'make -C builds/%LIBRARY_NAME% build' -and -notmatch 'mv builds/%LIBRARY_NAME%/local_lib.so libs/%LIBRARY_NAME%.so' | Set-Content makefile"
if errorlevel 1 (
    echo ERROR: An error occurred while removing entries from makefile
    .venv\Scripts\python.exe assets\finish_error.py
    exit /b 1
)

REM Rimuovo la libreria da libs
del "libs\%LIBRARY_NAME%.so"
if errorlevel 1 (
    echo ERROR: An error occurred while removing the library %LIBRARY_NAME%.so from libs
    .venv\Scripts\python.exe assets\finish_error.py
    exit /b 1
)

REM Riporto in scripts\events\history.log il comando eseguito
echo rem lib %LIBRARY_NAME%>> scripts\events\history.log

REM Eseguo lo script di completamento
.venv\Scripts\python.exe assets\finish_scripts.py

echo Library %LIBRARY_NAME% removed successfully
exit /b 0
