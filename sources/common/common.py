import logging
import os
import tempfile
from logging import Logger
from typing import IO

logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), r"../../logs/dev.log"),
    filemode="w",
    format="%(asctime)-16s | %(processName)-16s %(threadName)-16s | %(levelname)-8s | %(pathname)s %(lineno)d : %(message)s",
    datefmt="%Y%m%d_%H%M%S",
    level=logging.DEBUG,
)


class LogBase:
    """Base class for logging.
    When inherited, this class logs the initialization and deletion of the class.

    Usage
    ~~~~~

    >>> class my_class(LogBase):
    ...     def __init__(self, logger: Logger):
    ...         super().__init__(logger)
    ...         logger.info("Hello, world!")
    ...     def __del__(self):
    ...         super().__del__()
    ...         logger.info("Goodbye, world!")
    ...
    >>> my_instance = my_class()
    >>> del my_instance
    """

    def __init__(self, logger: Logger):
        logger.debug(f"{self.__class__.__name__}.__init__()")
        self.logger = logger

    def __del__(self):
        self.logger.debug(f"{self.__class__.__name__}.__del__()")


def tempgen(directory: str = "./temp") -> IO[bytes]:
    """This function manage temporary files in a directory

    Params
    ~~~~~~

        directory (str, optional): directory with temporary files. Defaults to "./temp".

    Raises
    ~~~~~~

        Exception: directory not found.

    Returns
    ~~~~~~~

        IO[bytes]: File name of the binary temporary file

    """
    if not os.path.exists(directory):
        raise Exception(f"Directory '{directory}' not found.")
    return tempfile.NamedTemporaryFile(dir=directory)
