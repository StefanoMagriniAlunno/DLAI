# Description: Human player definition
import os
from logging import Logger
from typing import Set

import torch
from justone import Player
from transformers import GPT2ForQuestionAnswering, GPT2Tokenizer


class LLMbot(Player):

    def __init__(
        self,
        logger: Logger,
    ):
        super().__init__(logger)

        tokenizer_path = os.path.join(
            os.getcwd(),
            r"data/db/gpt2/tokenizer",
        )
        model_path = os.path.join(
            os.getcwd(),
            r"data/db/gpt2/model",
        )

        tokenizer_config_dir = tokenizer_path
        # scorro tutte le sottodirectory alla ricerca di config.json
        for root, dirs, files in os.walk(
            tokenizer_path
        ):  # pylint: disable=unused-variable
            for file in files:
                if file == "config.json":
                    tokenizer_config_dir = root
                    break
            if tokenizer_config_dir != tokenizer_path:
                break
        if tokenizer_config_dir == tokenizer_path:
            raise FileNotFoundError(f"config.json not found in {tokenizer_path}")
        self.tokenizer = GPT2Tokenizer.from_pretrained(
            tokenizer_config_dir,
        )

        model_config_dir = model_path
        # scorro tutte le sottodirectory (e tutte quelle dentro) alla ricerca di config.json
        for root, dirs, files in os.walk(model_path):  # pylint: disable=unused-variable
            for file in files:
                if file == "config.json":
                    model_config_dir = root
                    break
            if model_config_dir != model_path:
                break
        if model_config_dir == model_path:
            raise FileNotFoundError(f"config.json not found in {model_path}")
        self.model = GPT2ForQuestionAnswering.from_pretrained(
            model_config_dir,
        )

        # inizializzo il modello
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def __del__(self):
        super().__del__()

    def eval(self):
        self.model.eval()

    def hint(self, word: str) -> str:
        # il modello deve produrre una parola, per questo genera token fino ad ottenerne una
        # la generazione è casuale, per questo sceglie un token casuale da un set di possibile token
        # con la distribuzione di probabilità suggerita

        # la frase passata sarà f'{word}?'
        raise NotImplementedError

    def answer(self, words: Set[str]) -> str:
        # il modello deve produrre una parola, per questo genera token fino ad ottenerne una
        # la generazione è casuale, per questo sceglie un token casuale da un set di possibile token
        # con la distribuzione di probabilità suggerita

        # la frase passata sarà ' '.join(words)
        raise NotImplementedError

    def __str__(self):
        return "llmbot"
