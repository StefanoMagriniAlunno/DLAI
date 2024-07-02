# Description: Human player definition
from typing import Set

from colorama import Fore, Style
from common import Logger
from game import Player


class Human(Player):
    def __init__(self, name: str, log: Logger):
        super().__init__(log)
        self.name = name

    def hint(self, word: str) -> str:
        """Get a hint from the player

        Args:
            word (str): The word to get a hint for

        Returns:
            str: The hint
        """
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
