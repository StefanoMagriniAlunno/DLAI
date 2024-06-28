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
        print("Player: {}".format(self.name))
        return input("Insert hint for word {}: ".format(word))

    def answer(self, words: List[str]) -> str:
        print("Player: {}".format(self.name))
        return input("Insert answer for words {}: ".format(words))
