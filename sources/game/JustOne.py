# Description: JustOne implementation


class JustOne:
    """Environment that manage the game

    Attributes
    ---
        - self.players (list): list of callable objects

    Methods
    ---

    """

    def __init__(self, players: list):
        """Initialisation of the game

        Params
        ---
            - players (list): list of players

        Raise
        ---
            - TypeError: If the parameters are not a list of objects
              with attributes __call__ and answer

        Usage
        ---
            >>> game = JustOne([])
        """

        for obj in players:
            if not hasattr(obj, "__call__"):
                raise TypeError("Must have __call__ attribute")
            if not hasattr(obj, "answer"):
                raise TypeError("Must have answer attribute")

        # TODO: bisogna copiare i giocatori!
        self.players: list = players

    def run(self):
        # pesca una parola W
        # sceglie un giocatore A (che dovrà indovinare la parola)
        # __call__ su tutti gli altri giocatori con la parola W
        # bot sulle parole per fornire un set finale da dare ad A
        # answer su A con l'elenco delle parole
        # se la parola è indovinata ritorna 'win'
        # altrimenti 'lose'
        pass
