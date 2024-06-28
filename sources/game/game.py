# Description: JustOne implementation
import random
from typing import List, Tuple

from common import Logger, LoggerSupport

from .player import Player
from .vocabulary import Vocabulary


class JustOne(LoggerSupport):
    """Environment that manage the game

    Attributes
    ---
        - self.players (List[Player]): list of callable objects
        - self.vocab (Vocabulary): vocabulary object

    Methods
    ---
        - bot(hints: List[str]) -> List[str]: bot function

    """

    def __init__(self, players: List[Player], vocab: Vocabulary, logger: Logger):
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
        super().__init__(logger)

        # raise
        if len(players) < 2:
            raise TypeError("Must have at least 2 player")

        # init
        self.players = players
        self.vocab = vocab

    def __call__(self, n_turns: int) -> Tuple[List[Tuple[str, List[str], str]], int]:
        solution: List[Tuple[str, List[str], str]] = []
        for _ in range(n_turns):
            # pesca una parola W
            w = self.vocab.sample()
            # sceglie un giocatore A (che dovrà indovinare la parola)
            A = random.choice(self.players)
            # hint su tutti gli altri giocatori con la parola W
            hints = [p.hint(w) for p in self.players if p != A]
            # bot sulle parole per fornire un set finale da dare ad A
            words = self.bot(hints)
            # answer su A con l'elenco delle parole
            ans = A.answer(words)
            # confronto w e ans
            solution.append((w, words, ans))
        # ritorno solution, numero di vincite
        return solution, sum([1 for w, _, ans in solution if w == ans])

    def bot(self, hints: List[str]) -> List[str]:
        """Bot function

        Params
        ---
            - hints (List[str]): list of hints

        Return
        ---
            - List[str]: list of words

        Usage
        ---
            >>> game.bot(["hint1", "hint2"])
        """
        # prende l'intersezione di tutte le parole in hints
        return list(set.intersection(*[set(h.split()) for h in hints]))
