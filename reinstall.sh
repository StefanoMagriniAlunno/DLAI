#!/bin/bash

# elimino la vecchia cartella .venv
if ! rm -rf .venv; then
    echo "ERROR: An error occurred while removing .venv"
    exit 1
fi

# ripeto l'installazione
if ! ./install.sh; then
    echo "ERROR: An error occurred while installing"
    exit 1
fi
