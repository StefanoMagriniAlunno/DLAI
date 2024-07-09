from logging import Logger
from typing import Set

from justone import Player


class Supervisor(Player):

    def __init__(self, log: Logger):
        super().__init__(log)

    def __del__(self):
        super().__del__()

    def hint(self, word: str) -> str:  # noqa
        raise NotImplementedError

    def answer(self, words: Set[str]) -> str:  # noqa
        raise NotImplementedError

    def __str__(self):
        return ""
