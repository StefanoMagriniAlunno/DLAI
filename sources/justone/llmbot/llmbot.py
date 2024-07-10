# Description: Human player definition
from logging import Logger
from typing import Set

import torch
from justone import Player
from torch import device
from transformers import GPT2LMHeadModel, GPT2Tokenizer


class LLMbot(Player):

    def __init__(
        self,
        logger: Logger,
        model_path: str,
        device: device = torch.device("cpu"),
    ):
        super().__init__(logger)
        if model_path is None:
            # carico il modello pre-addestrato di default
            self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
            self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def __del__(self):
        super().__del__()

    def hint(self, word: str) -> str:
        raise NotImplementedError

    def answer(self, words: Set[str]) -> str:
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError
