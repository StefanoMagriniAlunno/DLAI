#!/bin/bash

###############################################################
# This script removes a module from the project.
#
# Params: $0 <path_to_module>
#       - path_to_module: the path to the module to remove
#
#   Note: the module is removed from the sources directory.
###############################################################

function show_help {
    echo -e " This script removes a module from the project."
    echo -e " "
    echo -e " Params: \$0 <path_to_module>"
    echo -e "       - path_to_module: the path to the module to remove"
    echo -e " "
    echo -e "   Note: the module is removed from the sources directory."
}
if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

# leggo il parametro con il path del modulo da rimuovere
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_module>"
    exit 1
fi

MODULE_PATH=$1

# Se il modulo non esiste in sources lancio un'eccezione
if [ ! -d "sources/$MODULE_PATH" ]; then
    echo "ERROR: sources/$MODULE_PATH not found."
    exit 1
fi

# Rimuovo il modulo
if ! rm -rf sources/"$MODULE_PATH"; then
    echo "ERROR: An error occurred while removing the module from sources."
    exit 1
fi

# riporto in scripts/events/history.log il comando eseguito
echo "rem mod $MODULE_PATH" >> scripts/events/history.log

python3 assets/finish_scripts.py

echo "Module $MODULE_PATH removed successfully"
