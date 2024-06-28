# Description: Human player definition
from typing import List

from common import Logger
from game import Player


class Human(Player):
    def __init__(self, name: str, logger: Logger):
        super().__init__(logger)
        self.name = name
        self.logger.info("Human player created")

    def hint(self, word: str) -> str:
        return input("{} insert HINT for word {}: ".format(self, word))

    def answer(self, words: List[str]) -> str:
        return input("{} insert ANSWER for words {}: ".format(self, words))

    def __str__(self):
        return self.name
