import logging
import os
import tempfile
from logging import Logger
from typing import IO


class LogBase:
    """Base class for logging.
    When inherited, this class logs the initialization and deletion of the class.

    Usage
    ~~~~~

    >>> class my_class(LogBase):
    ...     def __init__(self, logger: Logger):
    ...         super().__init__(logger)
    ...         self.logger.info("Hello, world!")
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


def main() -> Logger:
    """Call this function to get the logger"""
    logging.basicConfig(
        filename=os.path.join(os.path.dirname(__file__), r"../../logs/dev.log"),
        filemode="w",
        format="%(asctime)-16s | %(processName)-16s %(threadName)-16s | %(levelname)-8s | %(pathname)s %(lineno)d : %(message)s",
        datefmt="%Y%m%d_%H%M%S",
        level=logging.DEBUG,
    )
    return logging.getLogger(__name__)


def tempgen(directory: str = "./temp") -> IO[bytes]:
    """This function manage temporary files in a directory

    :params: directory (str, optional): directory with temporary files (default `./temp`).

    :returns: File name of the binary temporary file

    :raise: (Exception) directory not found

    """
    if not os.path.exists(directory):
        raise Exception(f"Directory '{directory}' not found.")
    return tempfile.NamedTemporaryFile(dir=directory)


if __name__ == "__main__":
    """A simple test for this module"""
    logger = main()

    logger.debug("a debug message")
    logger.info("an info")
    logger.warning("a warning")
    logger.error("ops an error :(")
    logger.critical("ouch this is fatal")

    message_in = b"Hi!"
    message_out = b""

    print(f"input message: {message_in!r}")

    with tempgen() as f:
        print(f"temporary file name: {f.name}")
        f.write(message_in)
        f.seek(0)
        message_out = f.read()

    print(f"output message: {message_out!r}")

    del logger
