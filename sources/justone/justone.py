# Description: JustOne game implementation.
import random
from abc import abstractmethod
from logging import Logger
from typing import List, Set, Tuple

import jellyfish
from common import LogBase
from nltk.corpus import wordnet


class Player(LogBase):
    """Player interface class
    This class is an abstract class that defines the interface of the player.
    Its methods must be implemented by the subclasses.

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
    This class is responsible for managing the game. It receives the players and
    plays the game.

    """

    def __init__(self, players: List[Player], log: Logger):
        """Constructor of the class

        :emphasis:`params`
            - :attr:`players` (List[Player]): list of players objects
            - :attr:`log` (Logger): logger object

        :emphasis:`raise`:
            - :exc:`AssertionError` if the players are less than 2

        """
        super().__init__(log)
        assert len(players) >= 2, "The number of players must be at least 2"
        self.players = players

    def __del__(self):
        return super().__del__()

    def play(self, n_turns: int) -> Tuple[List[Tuple[str, Set[str], str]], int]:
        """Play the game

        :emphasis:`params`
            - :attr:`n_turns` (int): number of turns

        :emphasis:`returns`
            - :emphasis:`solution` (List[Tuple[str, Set[str], str]]): list of solutions
                - :emphasis:`str`: secret word
                - :emphasis:`Set[str]`: list of hints
                - :emphasis:`str`: answer
            - :emphasis:`wins` (int): number of wins

        :emphasis:`raise`
            - :exc:`ValueError` if n_turns is negative.

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

        :emphasis:`params`
            - :attr:`secret_word` (str): secret word
            - :attr:`hints` (List[str]): list of hints

        :emphasis:`returns`
            - :emphasis:`Set[str]`: list of words

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
