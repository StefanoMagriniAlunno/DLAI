# flake8: noqa

from invoke import task  # type: ignore


@task
def install(ctx, unix_like=False):
    """Installa più pacchetti definiti in una lista."""
    # NOTE: lista di pacchetti da installare
    # packages = [
    #     "pacchetto1",
    #     "pacchetto2 pacchetto3",
    #     ...
    # ]
    packages = [
        "numpy",
        "pandas plotly",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "torch torchvision torchaudio",
        "nltk",
        "fuzzywuzzy python-Levenshtein",
    ]
    for package in packages:
        if unix_like:
            # Unix-like system
            ctx.run(f".venv/bin/python3 -m pip install {package}")
        else:
            # Windows system
            ctx.run(f".venv\Scripts\python.exe -m pip install {package}")


@task
def download(ctx, unix_like=False):
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
    import os

    import nltk

    if not os.path.exists(r"data/db/nltk_data"):
        os.makedirs(r"data/db/nltk_data")
    wordnet_path = os.path.join(os.getcwd(), r"data/db/nltk_data/wordnet")
    words_path = os.path.join(os.getcwd(), r"data/db/nltk_data/words")
    punkt_path = os.path.join(os.getcwd(), r"data/db/nltk_data/punkt")
    nltk.data.path.append(wordnet_path)
    nltk.data.path.append(words_path)
    nltk.data.path.append(punkt_path)
    nltk.download("wordnet", download_dir=wordnet_path, quiet=True)
    nltk.download("words", download_dir=words_path, quiet=True)
    nltk.download("punkt", download_dir=punkt_path, quiet=True)
