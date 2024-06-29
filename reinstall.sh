#!/bin/bash

# Inizializza le variabili
python_path=""

# Controlla se è stato fornito un argomento
if [ $# -eq 1 ]; then
    python_path="$1"
fi

# elimino la vecchia cartella .venv
if ! rm -rf .venv; then
    echo -e "\e[31mERROR\e[0m: An error occurred while removing .venv"
    exit 1
fi

# ripeto l'installazione
echo -e "\e[35mInstall repo with path $python_path, wait a few minutes...\e[0m"
./install.sh "$python_path"
