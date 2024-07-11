#!/bin/bash

# Inizializza le variabili
python_cmd="python3"
pip_version="24.1.1"  # usato sia dall'utente per installare virtualenv, sia dall'ambiente stesso per installare i pacchetti
virtualenv_version="20.26.3"


# Controlla se è stato fornito un argomento
if [ $# -eq 1 ]; then
    # La path passata è quella di python
    python_cmd=$1
fi

# controllo il sistema
# Che sia linux ubuntu 22.04
if [ "$(lsb_release -si)" != "Ubuntu" ]; then
    echo -e "\e[31mERROR\e[0m: This script is only for Ubuntu"
    exit 1
fi
if [ "$(lsb_release -sr)" != "22.04" ]; then
    echo -e "\e[31mWARNING\e[0m: This script is only for Ubuntu 22.04"
fi
# Che python_cmd sia python3.10.12
if ! "$python_cmd" -c "import sys; print(sys.version_info[:3])" | grep -q "(3, 10, 12)"; then
    echo -e "\e[31mERROR\e[0m: This script is only for Python 3.10.12"
    exit 1
fi
# Che python_cmd abbia il modulo pip
if ! "$python_cmd" -m pip --version > /dev/null 2>&1; then
    echo -e "\e[31mERROR\e[0m: This script is only for Python with pip"
    # Tento di risolvere il problema senza l'uso di sudo
    if ! "$python_cmd" -m ensurepip --default-pip > /dev/null 2>&1; then
        echo -e "\e[31mERROR\e[0m: An error occurred while installing pip"
        # Tento un secondo metodo senza ensurepip
        if ! curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py > /dev/null 2>&1; then
            echo -e "\e[31mERROR\e[0m: An error occurred while downloading get-pip.py"
            exit 1
        fi
        if ! "$python_cmd" get-pip.py > /dev/null 2>&1; then
            echo -e "\e[31mERROR\e[0m: An error occurred while installing pip"
            exit 1
        fi
        # Rimuovo il file get-pip.py
        rm get-pip.py
    fi
fi
# Che ci sia git-all
if ! dpkg -l | grep -q "git-all"; then
    echo -e "\e[31mERROR\e[0m: This script is only for Ubuntu with git-all"
    exit 1
fi



# aggiorno pip a $pip_version
if ! "$python_cmd" -m pip install --upgrade pip=="$pip_version" --no-warn-script-location > /dev/null 2>&1; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing pip$pip_version"
    exit 1
fi

# installo con pip virtualenv $virtualenv_version
if ! "$python_cmd" -m pip install --user virtualenv=="$virtualenv_version" --no-warn-script-location > /dev/null 2>&1; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing virtualenv$virtualenv_version"
    exit 1
fi

# inizializzo la repository
if ! "$python_cmd" -m virtualenv .venv --pip="$pip_version"; then
    echo -e "\e[31mERROR\e[0m: An error occurred while creating .venv"
    exit 1
fi

echo -e "\e[32mSUCCESS\e[0m: environment created"
echo -e "\e[35mInstalling base package, wait a few minutes...\e[0m"

# nuova path per l'ambiente creato
python3_cmd=".venv/bin/python3"

if ! "$python3_cmd" -m pip install -r requirements.txt --quiet; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing requirements.txt"
    "$python3_cmd" assets/finish_error.py
    exit 1
fi
# eseguibili particolari dell'ambiente creato
pre_commit_cmd=".venv/bin/pre-commit"
invoke_cmd=".venv/bin/invoke"
sphinx_cmd=".venv/bin/sphinx-build"

if ! "$pre_commit_cmd" install > /dev/null 2>&1; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing pre-commit-config.yaml"
    "$python3_cmd" assets/finish_error.py
    exit 1
fi
if ! "$pre_commit_cmd" install-hooks > /dev/null 2>&1; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing hooks"
    "$python3_cmd" assets/finish_error.py
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
mkdir -p "scripts"
mkdir -p "scripts/events"
mkdir -p "temp"
mkdir -p "cache"
mkdir -p "documents/_build"
mkdir -p "documents/_static"
mkdir -p "documents/_templates"
mkdir -p "documents/builds"
touch "scripts/events/history.log"
touch "logs/dev.log"

mkdir -p "tools"
mkdir -p "tests"


echo -e "\e[32mSUCCESS\e[0m: base package installed"
echo -e "\e[35mInstalling custom packages, wait a few minutes...\e[0m"

# installo i pacchetti dinamici per il progetto
if ! "$invoke_cmd" install 2> packages.log; then
    echo -e "\e[31mERROR\e[0m: An error occurred while installing packages"
    "$python3_cmd" assets/finish_error.py
    exit 1
fi
if ! "$invoke_cmd" download 2> downloads.log; then
    echo -e "\e[31mERROR\e[0m: An error occurred while downloading data"
    "$python3_cmd" assets/finish_error.py
    exit 1
fi

echo -e "\e[32mSUCCESS\e[0m: custom packages installed"
echo -e "\e[35mBuild libraries and documentation...\e[0m"

# preparo builds
if ! make --silent; then
    echo -e "\e[31mERROR\e[0m: An error occurred while compiling libraries"
    "$python3_cmd" assets/finish_error.py
    exit 1
fi

# generazione della documentazione
if ! "$sphinx_cmd" -b html documents documents/_build/html; then
    echo -e "\e[31mERROR\e[0m: An error occurred while making documentation"
    "$python3_cmd" assets/finish_error.py
    exit 1
fi

echo -e "\e[32mSUCCESS\e[0m"

# controllo la repository
"$pre_commit_cmd" run --all-files

# finish
"$python3_cmd" assets/finish_install.py
echo "You can now run the project with:"
echo "Please, activate the environment:"
echo "    source .venv/bin/activate"

exit 0
