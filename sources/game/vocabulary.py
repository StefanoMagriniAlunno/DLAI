# Description: Vocabulary implementation
import os
import random

from common import Logger, LoggerSupport


class Vocabulary(LoggerSupport):
    """Vocabulary class

    Attributes
    ---
        - self.words (list): list of words
        - self.path (str): path of the file
        - self.mode (str): mode of the vocabulary
    """

    def __init__(self, path: str, logger: Logger):
        """Constructor of the class

        Params
        ---
            - path (str): Path of the file (respect data)
            - logger (Logger): Logger object

        Raise
        ---
            - FileNotFoundError: If the file is not found

        Usage
        ---
            >>> vocab = Vocabulary("path/to/file", "ram", logger)
        """
        super().__init__(logger)

        if not os.path.exists("./data" + path):
            raise FileNotFoundError(f"{'./data' + path} not found")

        with open("./data" + path, "r") as f:
            self.words_set = set(f.read().split("\n"))
            self.words_list = list(self.words_set)

    def __getitem__(self, index: int) -> str:
        return self.words_list[index]

    def __len__(self) -> int:
        return len(self.words_list)

    def __iter__(self):
        for word in self.words_list:
            yield word

    def __contains__(self, word: str) -> bool:
        return word in self.words_set

    def sample(self) -> str:
        return random.choice(self.words_list)
