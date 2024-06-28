# Description: definition of an abstract player
from abc import abstractmethod
from typing import List

from common import LoggerSupport


class Player(LoggerSupport):
    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def hint(self, word: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def answer(self, words: List[str]) -> str:
        raise NotImplementedError
