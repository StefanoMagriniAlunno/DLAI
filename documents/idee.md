# Idee progetto JustOne

**osservazini**
    - JustOne ammette una strategia vincente: ogni giocatore collega una parola univocamente ad un'altra, affinché alla parole del gioco siano collegate parole distinte per giocatori distinti. In questo modo scelta una parola ogni giocatore propone la sua parola valida e il giocatore interrogato la riconoscerà perché sa i collegamenti. Nota: non è necessario che le parole collegate abbiano un collegamente semantico con la parola originale.
    - Se tutti i giocatori seguissero la stessa strategia allora non è possibile scegliere la parola deterministicamente perché altrimenti tutte le parole fornite sarebbero annullate poiché uguali. In questo caso una buona strategia è far sì che per una parola pescata si scelga casualmente una parola da un set prestabilito, la probabilità che almeno una parola passi è tanto alta quanto vasto è questo set.
    - Onde evitare che i set non siano semanticamente simili alla parola pescata si può usare un linguaggio naturale preaddestrato (come GPT) come membro del gioco (non a priori noto agli altri giocatori).
    - Si può provare ad aumentare la complessità del gioco aumentando la quantità delle parole pescabili o riducendo quelle note.

**I giocatori**
    - un giocatore con 2 reti neurali: hint e answer:
        - hint: prende in input una parola e produce una parola suggerimento
        - answer: prende una lista di suggerimenti (non per forza con quantità prefissata) e prova a scoprire la parola originale
    - un giocatore può essere GPT che aiuta a mantenere la semantica.
    - un giocatore umano

**L'addestramento**
    - Reinforcement learning -> fine tuning / tuning (dipende dal giocatore)







note di implementazione:
l'addestramento passa attrevo una simulazione del gioco che avviene su CPU (a causa del fatto che le parole sono su RAM)
per questa ragione abbiamo una coda di processi che sono quelli del batch, la cpu cercherà di smaltirli il più possibile registrando quindi la loss risultante.
al termine su gpu avviene l'aggiornamento dei parametri.
