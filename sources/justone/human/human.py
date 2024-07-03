# Description: Human player definition
from logging import Logger
from typing import Set

from colorama import Fore, Style
from justone import Player


class Human(Player):
    """Human player class
    This class represents a human player. It implements the Player interface.
    """

    def __init__(self, name: str, log: Logger):
        """Create a human player

        :emphasis:`params`
            - :attr:`name` (str): The name of the player
            - :attr:`log` (Logger): The logger to use

        """
        super().__init__(log)
        self.name = name

    def __del__(self):
        super().__del__()

    def hint(self, word: str) -> str:
        """Get a hint from the player"""
        return input(
            Fore.BLUE
            + f"{self}"
            + Style.RESET_ALL
            + " insert "
            + Style.BRIGHT
            + "HINT"
            + Style.RESET_ALL
            + " for word "
            + Fore.MAGENTA
            + word
            + ": "
            + Style.RESET_ALL
        )

    def answer(self, words: Set[str]) -> str:
        """Get an answer from the player"""
        return input(
            Fore.BLUE
            + f"{self}"
            + Style.RESET_ALL
            + " insert "
            + Style.BRIGHT
            + "ANSWER"
            + Style.RESET_ALL
            + " for words "
            + Fore.MAGENTA
            + " ".join(words)
            + ": "
            + Style.RESET_ALL
        )

    def __str__(self):
        return self.name
