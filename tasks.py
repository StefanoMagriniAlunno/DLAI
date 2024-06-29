# flake8: noqa

from invoke import task


@task
def install(ctx):
    """Installa più pacchetti definiti in una lista."""
    packages = [
        # "package1",
        # "package2",
        # "package3",
    ]
    for package in packages:
        ctx.run(f".venv/bin/python3 -m pip install {package}")


@task
def download(ctx):
    """Download a file from a URL."""
    # lista di URL con destinazione rispetto ./data
    # url = "https://the/url/to/download"
    # path = "path/to/file/realtive/to/data/folder"
    # ctx.run(f'wget {url} -O ./data/{path}')
