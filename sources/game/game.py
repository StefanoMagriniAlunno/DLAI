# Description: JustOne implementation
from typing import List, Tuple

from common import Logger

from .player import Player


class JustOne:
    """Environment that manage the game

    Attributes
    ---
        - self.players (list): list of callable objects

    Methods
    ---

    """

    def __init__(self, players: List[Player], logger: Logger):
        """Constructor of the class

        Params
        ---
            - players (List[Player]): list of players objects
            - logger (Logger): logger object

        Raise
        ---
            - TypeError: If the players are less than 2

        Usage
        ---
            >>> game = JustOne([player1, player2], logger)
        """
        # set del logger
        self.logger = logger
        self.logger.trace("JustOne.__init__")
        logger.debug("Players: {}".format([str(player) for player in players]))

        # raise
        if len(players) < 2:
            raise TypeError("Must have at least 2 player")

        # init
        self.players = players
        logger.info("Game JustOne started")

    def __del__(self):
        self.logger.trace("JustOne.__del__")

    def __call__(self, n_turns: int) -> Tuple[dict]:
        for _ in range(n_turns):
            # pesca una parola W
            pass
        # # sceglie un giocatore A (che dovrà indovinare la parola)
        # # hint su tutti gli altri giocatori con la parola W
        # # bot sulle parole per fornire un set finale da dare ad A
        # # answer su A con l'elenco delle parole
        # # aggiunge il report del turno: ('parola', [parole], 'risposta')
        raise NotImplementedError("JustOne.__call__ is not implemented!")
