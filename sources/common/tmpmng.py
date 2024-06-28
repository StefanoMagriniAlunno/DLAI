import os
import tempfile
from typing import IO


class tmpmng:
    """tmpmng class
    This class creates a temporary file in the specified directory.

    Attributes
    ---
        - directory (str): The directory where the temporary file is created.

    Usage
    ---
        - >> from tmpmng import tmpmng
        - >> tmpgen = tmpmng()
        - >> file = tmpgen()
    """

    def __init__(self, directory: str = "./temp"):
        print("common | tmpmng :: __init__")
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")
        self.directory = directory

    def __call__(self) -> IO[bytes]:
        temp_file = tempfile.NamedTemporaryFile(dir=self.directory)
        return temp_file

    def __del__(self):
        print("common | tmpmng :: __del__")
