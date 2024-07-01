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
        ctx.run(r"./.venv/bin/python3" + f"-m pip install {package}")


@task
def download(ctx, unix_like=False):
    """Download a file from a URL."""
    pass