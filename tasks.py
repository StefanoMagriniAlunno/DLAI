from invoke import task


@task
def install(ctx):
    """Installa più pacchetti definiti in una lista.
    Parameters
        - **ctx**: contesto
    Usage
        ~~~bash
            invoke tasks.py
        ~~~
        oppure
        ~~~python3
            install(ctx)
        ~~~
    """
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
        ctx.run(f"pip install {package}")

@task
def download(ctx):
    """Download a file from a URL.

    Usage
    ---
        invoke tasks.py download --url https://www.google.com
    """
    # lista di URL con destinazione rispetto ./data
    # url = "https://the/url"
    # path = "path/to/file"
    # ctx.run(f"wget {url} -O ./data/{path}")
