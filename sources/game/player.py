# Description: definition of an abstract player
from abc import ABC, abstractmethod
from typing import List

from common import Logger


class Player(ABC):
    @abstractmethod
    def __init__(self, logger: Logger):
        self.logger = logger
        self.logger.trace("Player.__init__")

    def __del__(self):
        self.logger.trace("Player.__del__")

    @abstractmethod
    def hint(self, word: str) -> str:
        pass

    @abstractmethod
    def answer(self, words: List[str]) -> str:
        pass
