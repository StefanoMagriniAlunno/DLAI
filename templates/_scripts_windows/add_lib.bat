@echo off
REM ###############################################################
REM # This script adds a library to the project.
REM #
REM # Params: %0 <library_name>
REM #       - library_name: the name of the library to add
REM #
REM #   Note: the library is added to the builds directory,
REM #         the makefile is updated to build the library and
REM #         run the local makefile to build the library.
REM ###############################################################

:show_help
echo This script adds a library to the project.
echo.
echo Params: %0 ^<library_name^>
echo       - library_name: the name of the library to add
echo.
echo Note: the library is added to the builds directory,
echo       the makefile is updated to build the library and
echo       run the local makefile to build the library.
goto :eof

if "%~1"=="" (
    call :show_help
    exit /b 0
)

REM Nome della libreria
set "LIBRARY_NAME=%~1"

REM Se la libreria non esiste
if not exist "builds\%LIBRARY_NAME%" (
    REM Creo una copia della directory templates\_builds in builds chiamata %LIBRARY_NAME%
    xcopy templates\_builds builds\%LIBRARY_NAME% /i /s /e /y
    if errorlevel 1 (
        echo ERROR: An error occurred while copying the directory templates\_builds to builds\%LIBRARY_NAME%
        .venv\Scripts\python.exe assets\finish_error.py
        exit /b 1
    )
)

REM Se nel makefile non vi è occorrenza di make -C builds\%LIBRARY_NAME% build
findstr /c:"make -C builds\%LIBRARY_NAME% build" makefile >nul
if errorlevel 1 (
    echo    make -C builds\%LIBRARY_NAME% build>> makefile
    echo    move /y builds\%LIBRARY_NAME%\local_lib.so libs\%LIBRARY_NAME%.so>> makefile
)

REM Compilo la libreria
make -C builds\%LIBRARY_NAME% build -s
if errorlevel 1 (
    echo ERROR: An error occurred while building the library %LIBRARY_NAME%
    .venv\Scripts\python.exe assets\finish_error.py
    exit /b 1
)

REM Sposto la libreria compilata
move /y builds\%LIBRARY_NAME%\local_lib.so libs\%LIBRARY_NAME%.so
if errorlevel 1 (
    echo ERROR: An error occurred while moving the library %LIBRARY_NAME%.so to libs
    .venv\Scripts\python.exe assets\finish_error.py
    exit /b 1
)

REM Riporto in scripts\events\history.log il comando eseguito
echo add lib %LIBRARY_NAME%>> scripts\events\history.log

REM Eseguo lo script di completamento
.venv\Scripts\python.exe assets\finish_scripts.py

echo Library %LIBRARY_NAME% built successfully
exit /b 0
