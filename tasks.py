# flake8: noqa

from invoke import task


@task
def install(ctx):
    """Installa più pacchetti definiti in una lista."""
    packages = [
        "torch torchvision torchaudio",
        "numpy",
        "pandas",
        "scipy",
        "scikit-learn",
        "matplotlib",
        "plotly",
        "seaborn",
    ]
    for package in packages:
        ctx.run(f".venv/bin/python3 -m pip install {package}")


@task
def download(ctx):
    """Download a file from a URL."""
    # lista di URL con destinazione rispetto ./data
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    path = "db/words_alpha.txt"
    ctx.run(f"wget {url} -O ./data/{path}")
