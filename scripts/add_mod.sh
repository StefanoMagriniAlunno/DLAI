#!/bin/bash

###############################################################
# This script adds a module to the project.
#
# Params: $0 <module_name> <parent_module>
#       - module_name: the name of the module to add
#       - parent_module: the name of the parent module
#
#   Note: the module is added to the sources directory
#         as a submodule of the parent module.
###############################################################

function show_help {
    echo -e " This script adds a module to the project."
    echo -e " "
    echo -e " Params: \$0 <module_name> <parent_module>"
    echo -e "       - module_name: the name of the module to add"
    echo -e "       - parent_module: the name of the parent module"
    echo -e " "
    echo -e "   Note: the module is added to the sources directory"
    echo -e "         as a submodule of the parent module."
}
if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

# riceve in input il nome del modulo e il nome del modulo padre
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <module_name> <parent_module>"
    exit 1
fi

MODULE=$1
PARENT_MODULE=$2

# cerco la directory sources/{PARENT_MODULE} e se non esiste lancio un'eccezione
if [ ! -d "sources/$PARENT_MODULE" ]; then
    echo "ERROR: sources/$PARENT_MODULE not found."
    exit 1
fi

# se non esiste il modulo allora lo creo
if [ ! -d "sources/$PARENT_MODULE/$MODULE" ]; then
    # prendo da templates la directory _sources e la copio in sources/{PARENT_MODULE}
    if ! cp -r templates/_sources sources/"$PARENT_MODULE" ; then
        echo "ERROR: An error occurred while copying the directory _sources to sources/$PARENT_MODULE."
        exit 1
    fi
    # rinomino la cartella _sources in {MODULE}
    if ! mv sources/"$PARENT_MODULE"/_sources sources/"$PARENT_MODULE"/"$MODULE" ; then
        echo "ERROR: An error occurred while renaming the directory example to $MODULE."
        exit 1
    fi
    # se $MODULE è diverso da example:
    if [ "$MODULE" != "example" ]; then
        # cambio nome al file example.py in {MODULE}.py
        if ! mv sources/"$PARENT_MODULE"/"$MODULE"/example.py sources/"$PARENT_MODULE"/"$MODULE"/"$MODULE".py ; then
            echo "ERROR: An error occurred while renaming the file example.py to $MODULE.py."
            exit 1
        fi
        # cambio il nome del modulo usato in __init__.py
        # sostituisco l'espressione example in {MODULE}
        if ! sed -i s/example/"$MODULE"/g sources/"$PARENT_MODULE"/"$MODULE"/__init__.py ; then
            echo "ERROR: An error occurred while renaming the module in __init__.py."
            exit 1
        fi
    fi
fi

# riporto in scripts/events/history.log il comando eseguito
echo "add mod $MODULE to $PARENT_MODULE" >> scripts/events/history.log

python3 assets/finish_scripts.py

echo "Module $MODULE added successfully"
