# flake8: noqa

import os
import sys

from invoke import task  # type: ignore


@task
def install(ctx):
    """Installa più pacchetti definiti in una lista."""
    # NOTE: lista di pacchetti da installare
    # packages = [
    #     "pacchetto1",
    #     "pacchetto2 pacchetto3",
    #     ...
    # ]
    packages = [
        # "numpy",
        # "pandas plotly",
        # "matplotlib",
        # "seaborn",
        # "scikit-learn",
        "colorama",
        "nltk jellyfish",
        "transformers",
        "torch torchvision torchaudio",
    ]
    for package in packages:
        ctx.run(f"{sys.executable} -m pip install {package}")


@task
def download(ctx):
    """Download a file from a URL."""
    # url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    # path = "db/words_alpha.txt"
    #
    # if unix_like:
    #     # Unix-like system
    #     ctx.run(f"curl -o ./data/{path} {url}")
    # else:
    #     # Windows system
    #     ctx.run(
    #        f"powershell -Command (New-Object Net.WebClient).DownloadFile('{url}', './data/{path}')"
    #     )

    import nltk

    nltk.download(
        "wordnet",
        download_dir=os.path.join(os.getcwd(), r"data/db/nltk_data"),
        quiet=True,
    )

    from transformers import GPT2PreTrainedModel, GPT2Tokenizer

    GPT2Tokenizer.from_pretrained(
        "gpt2",
        cache_dir=os.path.join(os.getcwd(), r"data/db/gpt2/tokenizer"),
    )
    GPT2PreTrainedModel.from_pretrained(
        "gpt2",
        cache_dir=os.path.join(os.getcwd(), r"data/db/gpt2/model"),
    )
