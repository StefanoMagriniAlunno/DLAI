import os
import tempfile
from typing import IO


class Temp:
    """Temp class
    This class creates a temporary file in the specified directory.

    Attributes
    ---
        directory (str): The directory where the temporary file is created.

    Usage
    ---
        >>> from common import Temp
        >>> tmp = Temp()
        >>> file = tmp()
    """

    def __init__(self, directory: str = "./temp"):
        """Constructor of the class

        Params
        ---
            directory (str, optional):
                directory with the temporary files. Defaults to "./temp".

        Raises
        ---
            FileNotFoundError: directory not found.
        """
        print("Temp.__init__")
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")
        self.directory = directory

    def __call__(self) -> IO[bytes]:
        temp_file = tempfile.NamedTemporaryFile(dir=self.directory)
        return temp_file

    def __del__(self):
        print("Temp.__del__")
