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
        "tqdm",
    ]
    for package in packages:
        ctx.run(f"pip install {package}")
