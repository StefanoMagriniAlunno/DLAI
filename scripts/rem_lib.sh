#!/bin/bash

###############################################################
# This script removes a library from the project.
#
# Params: $0 <library_name>
#       - library_name: the name of the library to remove
#
#   Note: the library is removed from the builds directory,
#         the makefile is updated to remove the library and
#         the library is removed from the libs directory.
###############################################################

function show_help {
    echo -e " This script removes a library from the project."
    echo -e " "
    echo -e " Params: \$0 <library_name>"
    echo -e "       - library_name: the name of the library to remove"
    echo -e " "
    echo -e "   Note: the library is removed from the builds directory,"
    echo -e "         the makefile is updated to remove the library and"
    echo -e "         the library is removed from the libs directory."
}
if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

# leggo il parametro con il nome della libreria da rimuovere
if [ $# -ne 1 ]; then
    echo "Usage: $0 <library_name>"
    exit 1
fi

# nome della libreria
LIBRARY_NAME=$1

# rimuovo la cartella builds/$LIBRARY_NAME
if ! rm -rf builds/"$LIBRARY_NAME"; then
    echo -e "\e[31mERROR\e[0m: An error occurred while removing the directory builds/$LIBRARY_NAME"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

# rimuovo ogni occorrenza di
# make -C builds/prova build
# mv builds/prova/local_lib.so libs/prova.so
# da makefile
if ! sed -i "/make -C builds\/$LIBRARY_NAME build/d" makefile; then
    echo -e "\e[31mERROR\e[0m: An error occurred while removing make -C builds/$LIBRARY_NAME build from makefile"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi
if ! sed -i "/mv builds\/$LIBRARY_NAME\/local_lib.so libs\/$LIBRARY_NAME.so/d" makefile; then
    echo -e "\e[31mERROR\e[0m: An error occurred while removing mv builds/$LIBRARY_NAME/local_lib.so libs/$LIBRARY_NAME.so from makefile"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

# rimuovo la libreria da libs
if ! rm -f libs/"$LIBRARY_NAME".so; then
    echo -e "\e[31mERROR\e[0m: An error occurred while removing the library $LIBRARY_NAME.so from libs"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

# riporto in scripts/events/history.log il comando eseguito
echo "rem lib $LIBRARY_NAME" >> scripts/events/history.log

.venv/bin/python3 assets/finish_scripts.py

echo "Library $LIBRARY_NAME removed successfully"
