#!/bin/bash

# aggiorno pip a 24.1
if ! pip install --upgrade pip==24.1 --no-warn-script-location; then
    echo "ERROR: An error occurred while installing pip24.1"
    exit 1
fi

# installo con pip virtualenv
if ! pip install --user virtualenv==20.26.3 --no-warn-script-location; then
    echo "ERROR: An error occurred while installing virtualenv20.26.3"
    exit 1
fi

# inizializzo la repository
"$HOME"/.local/bin/virtualenv .venv
# shellcheck source=/dev/null
if ! source .venv/bin/activate; then
    echo "ERROR: An error occurred while opening .venv"
    exit 1
fi
if ! pip install -r requirements.txt; then
    echo "ERROR: An error occurred while installing requirements.txt"
    exit 1
fi
if ! pre-commit install; then
    echo "ERROR: An error occurred while installing pre-commit-config.yaml"
    exit 1
fi
if ! pre-commit install-hooks; then
    echo "ERROR: An error occurred while installing hooks"
    exit 1
fi
deactivate

# installo i pacchetti dinamici per il progetto
# shellcheck source=/dev/null
if ! source .venv/bin/activate && invoke install | tee packages.log; then   # shellcheck disable=SC1091
    echo "ERROR: An error occurred while installing packages"
    exit 1
fi
deactivate

# preparo builds
make

# aggiungo le cartelle che potrebbero non esserci
mkdir -p "builds"
mkdir -p "data"
mkdir -p "data/out"
mkdir -p "data/images"
mkdir -p "data/audios"
mkdir -p "data/videos"
mkdir -p "data/db"
mkdir -p "logs"
mkdir -p "scripts/events"
mkdir -p "temp"
touch "scripts/events/history.log"
touch "logs/user.log"
touch "logs/dev.log"

mkdir -p "tools"
mkdir -p "tests"

# finish
python3 assets/finish_install.py
echo "You can now run the project with:"
echo "Please, activate the environment:"
echo "    source .venv/bin/activate"
