#!/bin/bash

# Inizializza le variabili
python_cmd="python3"
pip_version="24.1.1"  # usato sia dall'utente per installare virtualenv, sia dall'ambiente stesso per installare i pacchetti
virtualenv_version="20.26.3"


# Controlla se è stato fornito un argomento
if [ $# -eq 1 ]; then
    # La path passata è quella di python
    python_cmd="$1"/bin/python3
fi

# aggiorno pip a $pip_version
if ! "$python_cmd" -m pip install --upgrade pip=="$pip_version" --no-warn-script-location > /dev/null 2>&1; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing pip$pip_version"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

# installo con pip virtualenv $virtualenv_version
if ! "$python_cmd" -m pip install --user virtualenv=="$virtualenv_version" --no-warn-script-location > /dev/null 2>&1; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing virtualenv$virtualenv_version"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

# inizializzo la repository
if ! "$python_cmd" -m virtualenv .venv --pip="$pip_version"; then
    echo -e "\e[31mERROR\e[0m: An error occurred while creating .venv"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

echo -e "\e[32mSUCCESS\e[0m: environment is ready"
echo -e "\e[35mInstalling repository packages, wait a few minutes...\e[0m"

# cambio il path di python3
if ! .venv/bin/python3 -m pip install -r requirements.txt --quiet; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing requirements.txt"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi
if ! .venv/bin/pre-commit install > /dev/null 2>&1; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing pre-commit-config.yaml"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi
if ! .venv/bin/pre-commit install-hooks > /dev/null 2>&1; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing hooks"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

# aggiungo le cartelle che potrebbero non esserci
mkdir -p "builds"
mkdir -p "data"
mkdir -p "data/out"
mkdir -p "data/images"
mkdir -p "data/audios"
mkdir -p "data/videos"
mkdir -p "data/db"
mkdir -p "libs"
mkdir -p "logs"
mkdir -p "scripts/events"
mkdir -p "temp"
touch "scripts/events/history.log"
touch "logs/user.log"
touch "logs/dev.log"

mkdir -p "tools"
mkdir -p "tests"

# preparo builds
make --silent

echo -e "\e[32mSUCCESS\e[0m: Repository is ready"
echo -e "\e[35mInstalling software packages, wait a few minutes...\e[0m"

# installo i pacchetti dinamici per il progetto
if ! .venv/bin/invoke install > packages.log; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing packages"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi
if ! .venv/bin/invoke download > downloads.log; then
    echo -e "\e[31mERROR\e[0m: An error occurred while downloading data"
    .venv/bin/python3 assets/finish_error.py
    exit 1
fi

# finish
.venv/bin/python3 assets/finish_install.py
exit 1
echo "You can now run the project with:"
echo "Please, activate the environment:"
echo "    source .venv/bin/activate"

exit 0
