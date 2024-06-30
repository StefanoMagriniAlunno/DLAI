# Description: JustOne game implementation.
import random
from abc import abstractmethod
from typing import List, Set, Tuple

from common import Logger, LoggerSupport
from fuzzywuzzy import fuzz
from nltk.corpus import wordnet


class Player(LoggerSupport):
    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def hint(self, word: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def answer(self, words: Set[str]) -> str:
        raise NotImplementedError


class JustOne(LoggerSupport):
    """Environment that manage the game

    Attributes
    ---
        - self.players (List[Player]): list of callable objects

    Methods
    ---
        - bot(hints: List[str]) -> List[str]: bot function

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
        super().__init__(logger)

        # raise
        if len(players) < 2:
            raise TypeError("Must have at least 2 player")

        # init
        self.players = players

    def __del__(self):
        return super().__del__()

    def __call__(self, n_turns: int) -> Tuple[List[Tuple[str, Set[str], str]], int]:
        solution: List[Tuple[str, Set[str], str]] = []
        for _ in range(n_turns):
            # pesca una parola W dal vocabolario di nltk
            w: str = random.choice(wordnet.words())
            # sceglie un giocatore A (che dovrà indovinare la parola)
            A = random.choice(self.players)
            # hint su tutti gli altri giocatori con la parola W
            hints = [p.hint(w) for p in self.players if p != A]
            # bot sulle parole per fornire un set finale da dare ad A
            words = self.bot(w, hints)
            # answer su A con l'elenco delle parole
            ans = A.answer(words)
            # confronto w e ans
            solution.append((w, words, ans))
        # ritorno solution, numero di vincite
        return solution, sum([1 for w, _, ans in solution if w == ans])

    def bot(self, secret_word: str, hints: List[str]) -> Set[str]:
        """Bot function

        Params
        ---
            - hints (List[str]): list of hints

        Return
        ---
            - Set[str]: list of words

        Usage
        ---
            >>> game.bot(["hint1", "hint2"])
        """
        # primo filtro: elimino gli hint che non sono nel dizionario
        hints_filtered = [hint for hint in hints if hint in wordnet.words()]
        # secondo filtro: elimino gli hint che hanno un fonema simile a quello di secret_word
        hints_filtered = [
            hint
            for hint in hints_filtered
            if fuzz.nysiis(hint) != fuzz.nysiis(secret_word)
        ]
        # terzo filtro: elimino gli hint che hanno un lemma simile a quello di secret_word
        hints_filtered = [
            hint
            for hint in hints_filtered
            if wordnet.morphy(hint) != wordnet.morphy(secret_word)
        ]

        # trasformo tutti gli hint rimasti in una lista di lemmi
        lemmas = [wordnet.morphy(hint) for hint in hints_filtered]

        # restituisco gli hint cui lemma ricorre una sola volta e non è None
        return set(
            [hint for hint in hints_filtered if lemmas.count(wordnet.morphy(hint)) == 1]
        )
