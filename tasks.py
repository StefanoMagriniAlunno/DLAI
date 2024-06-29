# flake8: noqa

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
    packages = []
    for package in packages:
        ctx.run(f".venv/bin/python3 -m pip install {package}")


@task
def download(ctx):
    """Download a file from a URL."""
    # NOTE: lista di url da scaricare
    # url = "https://example.com/file.txt"
    # path = "path/to/file.txt"
    # ctx.run(f"wget {url} -O ./data/{path}")
    # ...
