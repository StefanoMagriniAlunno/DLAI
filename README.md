# DLAI

## Come installare questa repository

La repository suppone l'uso di python3.8.10
~~~bash
    # mettersi nella directory dove si vuole scaricare la cartella con dentro la repository
    git clone https://github.com/StefanoMagriniAlunno/DLAI  # sarà necessario autenticarsi
    cd DLAI  # entrare nella cartella
    # settare la branch interessata, ad esempio:
    git checkout just-one
    git branch  # verificare che sia corretta la branch
    # installare il software e seguire le sue indicazioni
    ./install.sh
~~~

## Contenuti base per la repository

**install.sh**
Questo file script bash permette di installare automaticamente i pacchetti utili per la repository e per il programma.
Farà uso dei file "requirements.txt" e tasks.py per conoscere quali pacchetti installare.

**requirements.txt**
Elenco dei pacchetti utili per la repository, è stato generato nel seguente modo
~~~bash
    # usando python3.8.10
    python3 -m venv venv
    source venv/bin/activate
    pip3 install pip==24.1.1
    pip3 install invoke pre-commit pytest jupyter sphinx
    pip3 install flake8 doc8 mypy black autoflake isort shellcheck-py
    pip3 freeze > requirements.txt
    deactivate
    rm -r venv
~~~
Quindi i pacchetti che contiene sono:
-   **invoke** : utile per l'installazione di pacchetti tramite python
-   **pre-commit** : usato per analizzare il codice prima di committare, serve per evitare commit di codice non funzionante
-   **pytest** : utile per compiere e monitorare test
-   **jupyter** : utile nella documentazione interattiva
-   **sphinx** : utile per creare la documentazione

**tasks.py**
Questo script di python è incaricato nella costruzione automatica della repository, in particolare:

-   installa i pacchetti utili per il software (consultare la task "install"), producendo il file "packages.log" con il log dell'installazione
-   aziona eventuali makefile

**resinstall.sh**
Questo script permette di reinstallare la repository, servirà abbandonare l'ambiente prima di eseguire lo script:
~~~bash
    deactivate
    ./reinstall.sh
~~~

## pre-commit
Le fasi di pre-commit servono a tenere sicura la repository da modifiche indegne:
1. **end-of-file-fixer** : controlla la riga di fine file
2. **mixed-line-ending** : controlla se la riga di fine file è conforme con il sistema operativo (Linux/MacOS: \n, Windows \r\n)
3. **check-yaml** : controlla i file yaml
4. **check-json** : controlla i file json
5. **check-docstring-first** : controlla che la documentazione sia inserita in modo corretto nel codice
6. **sort-simple-yaml** : formatta i file yaml
7. **pretty-format-json** : formatta i file json
8. **flake8** : controlla lo stile di codice Python secondo lo standard PEP8
9. **doc8** : controlla che la documentazione rispetti lo standard
10. **autoflake** : rimuove importazioni inutili
11. **isort** : riordina le importazioni
12. **shellcheck** : controlla file shell e bash
13. **mypy** : verifiche statiche di tipizzazione
14. **black** : formatta il codice python
Per eseguire un test al volo senza effettivamente committare, è possibile eseguire:
~~~bash
    pre-commit run --all-files
~~~

## Directory
Le cartelle principali di questa repository sono:
**documents**: documentazione
**scripts**: script della repository (per una corretta gestione)
**source**: codice sorgente
**builds**: build per le librerie in fase di installazione (**libs** custodisce le librerie)
**templates**: formati base di file usati da scripts e documents

### Directory ignorate
Le directory ignorate sono quelle che possono servire localmente e sono:
**data**: container di eventuali input e output
**logs**: log desiderato per i moduli
**temp**: file temporanei generati durante l'esecuzione del codice ed eliminabili

### Cartelle non ignorate
**tests**: ambiente per preparare test per il codice
**tools**: programmi utili per la progettazione, ma scollegati con il resto del codice


## Uso della repository

### script ausiliari

In **scripts** si possono trovare degli script utili per un corretto uso della repository, vanno chiamati dalla directory del progetto. Chiamandoli senza argomenti verrà illustrato come si usano e i loro effetti.

**add_lib.sh**: aggiunge una libreria in builds

**add_mod.sh**: aggiunge un modulo in sources

**rem_lib.sh**: rimuove una libreria da builds

**rem_mod.sh**: rimuove un modulo da sources

### Semplice guida di github per apportare modifiche

Prima di cominciare la propria sessione di modifiche eseguire "git pull". Questo comando può prevenire di modificare codice già non aggiornato. Se tuttavia ci sono già delle modifiche è sconsigliato eseguire questa istruzione.

~~~bash
git checkout nome_repository  # utile per cambiare branch
git branch  # informa l'utente della branch corrente
git status  # informa l'utente dello stato della branch corrente

git add .  # aggiunge le modifiche fatte ad un elenco (quindi questo comando può essere eseguito molteplici volte)
git commit -m "messaggio..."  # avvia il pre-commit e in caso di successo viene concesso il commit
# un errore di commit è aver eseguito commit senza aver eseguito prima: git add .
# se non si supera un test, riprovare:
# > git add .
# > git commit -m "messaggio..."

# se il problema persiste, correggere il codice in funzione degli errori rilevati
git pull  # si confronta il codice corrente della repository con quello del commit
# questa fase può fornire errori più o meno difficili da affrontare
# in genere sono incoerenze tra le modifiche effettuate e la repository pubblicata
git push  # si pubblica la repository, attenzione MAI eseguire git push oltrepassando git pull
~~~

## Funzionalità

Le funzionalità base della repository sono custodite nel modulo **common**

### logger

logger è il modulo della repository che gestisce i log del progetto, produce due tipi di log: *user.log* e *dev.log*.
Questi file devono già esistere, inoltre è possibile fornire proprie directory e quindi creare log che non verranno sovrascritti.

<img src="assets/log_policy.png" title="Schema policy di log" style="zoom:100%;" />

### tmpmng

tmpmng è il modulo della repository che gestisce i file temporanei del progetto.
