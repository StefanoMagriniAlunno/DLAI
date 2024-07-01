#!/bin/bash

###############################################################
# This script adds a library to the project.
#
# Params: $0 <library_name>
#       - library_name: the name of the library to add
#
#   Note: the library is added to the builds directory,
#         the makefile is updated to build the library and
#         run the local makefile to build the library.
###############################################################

function show_help {
    echo -e " This script adds a library to the project."
    echo -e " "
    echo -e " Params: \$0 <library_name>"
    echo -e "       - library_name: the name of the library to add"
    echo -e " "
    echo -e "   Note: the library is added to the builds directory,"
    echo -e "         the makefile is updated to build the library and"
    echo -e "         run the local makefile to build the library."
}
if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

# riceve in input il nome della libreria
if [ $# -ne 1 ]; then
    echo "Usage: $0 <library_name>"
    exit 1
fi

# nome della libreria
LIBRARY_NAME=$1

# se la libreria non esiste
if [ ! -d "builds/$LIBRARY_NAME" ]; then
    # creo una copia della directory templates/_builds in builds chiamata $LIBRARY_NAME (invece di _builds)
    if ! cp -r templates/_builds builds/"$LIBRARY_NAME"; then
        echo -e "\e[31mERROR\e[0m: An error occurred while copying the directory templates/_builds to builds/$LIBRARY_NAME"
        .venv/bin/python3 assets/finish_error.py
        exit 1
    fi
fi

# se nel makefile non vi è occorrenza di
# make -C builds/$LIBRARY_NAME build
if ! grep -q "make -C builds/$LIBRARY_NAME build" "makefile"; then
    # aggiungo in makefile le righe per l'installazione automatica della libreria
    echo -e "\tmake -C builds/$LIBRARY_NAME build" >> "./makefile"
    echo -e "\tmv builds/$LIBRARY_NAME/local_lib.so libs/$LIBRARY_NAME.so" >> "./makefile"
fi

if ! make -C builds/"$LIBRARY_NAME" build -s; then
    echo -e "\e[31mERROR\e[0m: An error occurred while building the library $LIBRARY_NAME"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi
if ! mv builds/"$LIBRARY_NAME"/local_lib.so libs/"$LIBRARY_NAME".so; then
    echo -e "\e[31mERROR\e[0m: An error occurred while moving the library $LIBRARY_NAME.so to libs"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

# riporto in scripts/events/history.log il comando eseguito
echo "add lib $LIBRARY_NAME" >> scripts/events/history.log

.venv/bin/python3 assets/finish_scripts.py

echo "Library $LIBRARY_NAME built successfully"

exit 0
