# Description: Human player definition
from logging import Logger
from typing import Set

from colorama import Fore, Style
from game import Player


class Human(Player):
    """Human player class

    Attributes
    ~~~~~~~~~~

        name (str): The name of the player

    Methods
    ~~~~~~~

        hint(word: str) -> str: Get a hint from the player
        answer(words: Set[str]) -> str: Get an answer from the player
        __str__() -> str: Get the string representation of the player

    """

    def __init__(self, name: str, log: Logger):
        """Create a human player

        Params
        ~~~~~~

            name (str): The name of the player
            log (Logger): The logger to use

        """
        super().__init__(log)
        self.name = name

    def __del__(self):
        super().__del__()

    def hint(self, word: str) -> str:
        """Get a hint from the player

        Params
        ~~~~~~

            word (str): The word to get a hint for

        Returns
        ~~~~~~~

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
        """Get an answer from the player

        Params
        ~~~~~~

            words (Set[str]): The words to get an answer for

        Returns
        ~~~~~~~

            str: The answer

        """
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
