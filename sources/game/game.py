# Description: JustOne game implementation.
import random
from abc import abstractmethod
from logging import Logger
from typing import List, Set, Tuple

import jellyfish
from common import LogBase
from nltk.corpus import wordnet


class Player(LogBase):
    """Player interface

    Methods
    ~~~~~~~

        - hint(word: str) -> str: get a hint from the player

        - answer(words: Set[str]) -> str: get an answer from the player

        - __str__() -> str: get the string representation of the player

    """

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def hint(self, word: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def answer(self, words: Set[str]) -> str:
        raise NotImplementedError


class JustOne(LogBase):
    """Environment that manage the game

    Attributes
    ~~~~~~~~~~

        players (List[Player]): list of callable objects

    Methods
    ~~~~~~~

        - bot(hints: List[str]) -> List[str]: bot function

        - play(n_turns: int) -> Tuple[List[Tuple[str, Set[str], str]], int]: play the game

    """

    def __init__(self, players: List[Player], log: Logger):
        """Constructor of the class

        Params
        ~~~~~~

            - players (List[Player]): list of players objects

            - log (Logger): logger object

        Raise
        ~~~~~

            AssertionError: If the players are less than 2

        """
        super().__init__(log)
        assert len(players) >= 2, "The number of players must be at least 2"
        self.players = players

    def __del__(self):
        return super().__del__()

    def play(self, n_turns: int) -> Tuple[List[Tuple[str, Set[str], str]], int]:
        """Play the game

        Params
        ~~~~~~

            n_turns (int): number of turns

        Returns
        ~~~~~~~

            Tuple[List[Tuple[str, Set[str], str]], int]: list of solutions and number of wins:

                - solution (List[Tuple[str, Set[str], str]]): list of solutions:

                    - str: secret word

                    - Set[str]: list of hints

                    - str: answer

                - wins (int): number of wins

        Raise
        ~~~~~

            ValueError: If n_turns is negative.

        """

        if n_turns < 0:
            raise ValueError(f"Required n_turns >= 0 but n_turns={n_turns}")

        solution: List[Tuple[str, Set[str], str]] = []
        for _ in range(n_turns):
            w: str = random.choice(list(wordnet.words()))
            A = random.choice(self.players)
            hints = [p.hint(w) for p in self.players if p != A]
            words = self.bot(w, hints)
            ans = A.answer(words)
            solution.append((w, words, ans))
        return solution, sum([1 for w, _, ans in solution if w == ans])

    def bot(self, secret_word: str, hints: List[str]) -> Set[str]:
        """Bot function

        Params
        ~~~~~~

            - secret_word (str): secret word

            - hints (List[str]): list of hints

        Return
        ~~~~~~

            Set[str]: list of words

        """
        hints_filtered = [hint for hint in hints if hint in wordnet.words()]
        hints_filtered = [
            hint
            for hint in hints_filtered
            if jellyfish.nysiis(hint) != jellyfish.nysiis(secret_word)
        ]
        hints_filtered = [
            hint
            for hint in hints_filtered
            if wordnet.morphy(hint) != wordnet.morphy(secret_word)
        ]
        lemmas = [wordnet.morphy(hint) for hint in hints_filtered]
        return set(
            [hint for hint in hints_filtered if lemmas.count(wordnet.morphy(hint)) == 1]
        )
