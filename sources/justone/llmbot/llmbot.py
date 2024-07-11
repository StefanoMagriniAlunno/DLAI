# Description: Human player definition
import os
from logging import Logger
from typing import Set

import torch
from justone import Player
from transformers import GPT2LMHeadModel, GPT2Tokenizer


class LLMbot(Player):

    def __init__(
        self,
        logger: Logger,
    ):
        super().__init__(logger)
        self.tokenizer = GPT2Tokenizer.from_pretrained(
            os.path.join(os.getcwd(), r"data/db/gpt2/tokenizer"),
        )
        self.model = GPT2LMHeadModel.from_pretrained(
            os.path.join(os.getcwd(), r"data/db/gpt2/HeadModel"),
        )

        # inizializzo il modello
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def __del__(self):
        super().__del__()

    def hint(self, word: str) -> str:
        # il modello deve produrre una parola, per questo genera token fino ad ottenerne una
        # la generazione è casuale, per questo sceglie un token casuale da un set di possibile token
        # con la distribuzione di probabilità suggerita

        # la frase passata sarà f'{word}'
        raise NotImplementedError

    def answer(self, words: Set[str]) -> str:
        # il modello deve produrre una parola, per questo genera token fino ad ottenerne una
        # la generazione è casuale, per questo sceglie un token casuale da un set di possibile token
        # con la distribuzione di probabilità suggerita

        # la frase passata sarà ' '.join(words)
        raise NotImplementedError

    def __str__(self):
        return "llmbot"
