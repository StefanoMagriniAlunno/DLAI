@echo off
REM ###############################################################
REM # This script adds a module to the project.
REM #
REM # Params: %0 <module_name> <parent_module>
REM #       - module_name: the name of the module to add
REM #       - parent_module: the name of the parent module
REM #
REM #   Note: the module is added to the sources directory
REM #         as a submodule of the parent module.
REM ###############################################################

:show_help
echo This script adds a module to the project.
echo.
echo Params: %0 ^<module_name^> ^<parent_module^>
echo       - module_name: the name of the module to add
echo       - parent_module: the name of the parent module
echo.
echo Note: the module is added to the sources directory
echo       as a submodule of the parent module.
goto :eof

if "%~1"=="" (
    call :show_help
    exit /b 0
)

REM Riceve in input il nome del modulo e il nome del modulo padre
if "%~2"=="" (
    echo Usage: %0 ^<module_name^> ^<parent_module^>
    exit /b 1
)

set "MODULE=%~1"
set "PARENT_MODULE=%~2"

REM Cerco la directory sources\%PARENT_MODULE% e se non esiste lancio un'eccezione
if not exist "sources\%PARENT_MODULE%" (
    echo ERROR: sources\%PARENT_MODULE% not found.
    .venv\Scripts\python.exe assets\finish_error.py
    exit /b 1
)

REM Se non esiste il modulo allora lo creo
if not exist "sources\%PARENT_MODULE%\%MODULE%" (
    REM Copio da templates la directory _sources in sources\%PARENT_MODULE%
    xcopy templates\_sources sources\%PARENT_MODULE% /i /s /e /y
    if errorlevel 1 (
        echo ERROR: An error occurred while copying the directory _sources to sources\%PARENT_MODULE%.
        .venv\Scripts\python.exe assets\finish_error.py
        exit /b 1
    )

    REM Rinomino la cartella _sources in %MODULE%
    rename sources\%PARENT_MODULE%\_sources %MODULE%
    if errorlevel 1 (
        echo ERROR: An error occurred while renaming the directory _sources to %MODULE%.
        .venv\Scripts\python.exe assets\finish_error.py
        exit /b 1
    )

    REM Se %MODULE% è diverso da example
    if /i not "%MODULE%"=="example" (
        REM Cambio nome al file example.py in %MODULE%.py
        rename sources\%PARENT_MODULE%\%MODULE%\example.py %MODULE%.py
        if errorlevel 1 (
            echo ERROR: An error occurred while renaming the file example.py to %MODULE%.py.
            .venv\Scripts\python.exe assets\finish_error.py
            exit /b 1
        )

        REM Cambio il nome del modulo usato in __init__.py
        REM Sostituisco l'espressione example in %MODULE%
        powershell -Command "(Get-Content sources\%PARENT_MODULE%\%MODULE%\__init__.py) -replace 'example', '%MODULE%' | Set-Content sources\%PARENT_MODULE%\%MODULE%\__init__.py"
        if errorlevel 1 (
            echo ERROR: An error occurred while renaming the module in __init__.py.
            .venv\Scripts\python.exe assets\finish_error.py
            exit /b 1
        )
    )
)

REM Riporto in scripts\events\history.log il comando eseguito
echo add mod %MODULE% to %PARENT_MODULE%>> scripts\events\history.log

REM Eseguo lo script di completamento
.venv\Scripts\python.exe assets\finish_scripts.py

echo Module %MODULE% added successfully
exit /b 0
