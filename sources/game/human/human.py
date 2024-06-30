# Description: Human player definition
from typing import Set

from common import Logger
from game import Player


class Human(Player):
    def __init__(self, name: str, log: Logger):
        super().__init__(log)
        self.name = name

    def hint(self, word: str) -> str:
        return input("{} insert HINT for word {}: ".format(self, word))

    def answer(self, words: Set[str]) -> str:
        return input("{} insert ANSWER for words {}: ".format(self, words))

    def __str__(self):
        return self.name
