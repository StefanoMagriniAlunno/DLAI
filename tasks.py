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
        # "numpy",
        # "pandas plotly",
        # "matplotlib",
        # "seaborn",
        # "scikit-learn",
        # "torch torchvision torchaudio",
        "nltk",
        "jellyfish",
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

    directory = os.path.join(os.getcwd(), r".venv/share/nltk_data")
    nltk.download("wordnet", prefix=directory, quiet=True)
    nltk.download("words", prefix=directory, quiet=True)
    nltk.download("punkt", prefix=directory, quiet=True)
