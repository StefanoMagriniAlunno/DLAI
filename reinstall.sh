#!/bin/bash

# Inizializza le variabili
python_path=""

# Controlla se è stato fornito un argomento
if [ $# -eq 1 ]; then
    python_path="$1"
fi

# elimino la vecchia cartella .venv
if ! rm -rf .venv; then
    echo "ERROR: An error occurred while removing .venv"
    exit 1
fi

# ripeto l'instal1lazione
if ! ./install.sh "$python_path"; then
    echo "ERROR: An error occurred while installing"
    exit 1
fi
