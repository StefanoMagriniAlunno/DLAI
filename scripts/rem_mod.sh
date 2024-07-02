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
    echo -e " Params: \$0 <module_name> <parent_module>"
    echo -e "       - module_name: the name of the module to remove"
    echo -e "       - parent_module: the name of the parent module"
    echo -e " "
    echo -e "   Note: the module is removed from the sources directory."
}
if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

# leggo il parametro con il path del modulo da rimuovere
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <module_name> <parent_module>"
    exit 1
fi

MODULE_PATH=sources/$2/$1

# Se il modulo non esiste in sources lancio un'eccezione
if [ ! -d "$MODULE_PATH" ]; then
    echo -e "\e[31mERROR\e[0m: sources/$MODULE_PATH not found."
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

# Rimuovo il modulo
if ! rm -rf "$MODULE_PATH"; then
    echo -e "\e[31mERROR\e[0m: An error occurred while removing the module from sources."
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

# Rimuovo il modulo da documents/$MODULE_PATH"
if ! rm -rf documents/"$MODULE_PATH"; then
    echo -e "\e[31mERROR\e[0m: An error occurred while removing the module from documents."
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

# riporto in scripts/events/history.log il comando eseguito
echo "rem mod $1 $2" >> scripts/events/history.log

.venv/bin/python3 assets/finish_scripts.py

echo "Module $1 removed successfully"

exit 0
