# This file contains the logger class, which is used to log messages to a file.
import inspect
from abc import ABC
from datetime import datetime
from typing import IO


class Logger:
    """This class is used to log messages to a file.
    The format of the log message is as follows:
        date time | tag | file_name line_number :: message

    Attributes
    ---
        - user (str): The path to the log file with tag
            [INFO], [WARNING], [ERROR].
        - dev (str): The path to the log file with tag
            [TRACE], [DEBUG], [FATAL].

    Methods
    ---
        - trace(message): Logs a message with tag [TRACE]
        - debug(message): Logs a message with tag [DEBUG]
        - info(message): Logs a message with tag [INFO]
        - warning(message): Logs a message with tag [WARNING]
        - error(message): Logs a message with tag [ERROR]
        - fatal(message): Logs a message with tag [FATAL]
    """

    def __init__(self, user: str = "logs/user.log", dev: str = "logs/dev.log"):
        """This function initializes the Logger class.

        Params
        ---
            user (str, optional):
                path for the user's log. Defaults to "./logs/user.log".
            dev (str, optional):
                path for the developer's log. Defaults to "./logs/dev.log".

        Reises
        ---
            FileNotFoundError: If the files are not found.

        Usage
        ---
            >>> from common import Logger
            >>> log = Logger()
        """
        print("common | Logger :: __init__")
        try:
            self.user: IO[str] = open(user, "w")
            self.dev: IO[str] = open(dev, "w")
        except FileNotFoundError:
            print("Error opening files.")
            return

    def trace(self, message: str = ""):
        """This function logs a message with tag [TRACE].

        Params
        ---
            message (str, optional): massage to log. Defaults to ''.

        Raise
        ---
            Exception: If the message cannot be written to the file.

        Usage
        ---
            - >> from common import Logger
            - >> log = Logger()
            - >> log.trace('This is a trace message')
        """
        # frame delle chiamate
        frame = inspect.currentframe()
        outer_frame = inspect.getouterframes(frame)
        # prendo il nome del file e il numero di riga
        file_name = outer_frame[1].filename
        line_no = outer_frame[1].lineno
        # scrivo il messaggio nel file
        eyes_char = "\U0001F440"
        try:
            self.dev.write(
                f"{datetime.now()} | TRACE {eyes_char}  | "
                + f"{file_name} {line_no} :: {message}\n"
            )
        except Exception as e:
            print(e)

    def debug(self, message: str = ""):
        """This function logs a message with tag [DEBUG].

        Params
        ---
            message (str, optional): massage to log. Defaults to ''.

        Raise
        ---
            Exception: If the message cannot be written to the file.

        Usage
        ---
            >>> from common import Logger
            >>> log = Logger()
            >>> log.debug('This is a debug message')
        """
        # frame delle chiamate
        frame = inspect.currentframe()
        outer_frame = inspect.getouterframes(frame)
        # prendo il nome del file e il numero di riga
        file_name = outer_frame[1].filename
        line_no = outer_frame[1].lineno
        # scrivo il messaggio nel file
        stethoscope_symbol = "\U0001FA7A"
        try:
            self.dev.write(
                f"{datetime.now()} | DEBUG {stethoscope_symbol}  | "
                + f"{file_name} {line_no} :: {message}\n"
            )
        except Exception as e:
            print(e)

    def fatal(self, message: str):
        """This function logs a message with tag [FATAL].

        Params
        ---
            message (str): massage to log.

        Raise
        ---
            Exception: If the message cannot be written to the file.

        Usage
        ---
            >>> from common import Logger
            >>> log = Logger()
            >>> log.fatal('This is a fatal message')
        """
        # frame delle chiamate
        frame = inspect.currentframe()
        outer_frame = inspect.getouterframes(frame)
        # prendo il nome del file e il numero di riga
        file_name = outer_frame[1].filename
        line_no = outer_frame[1].lineno
        # scrivo il messaggio nel file
        collision_symbol = "\U0001F4A5"
        try:
            self.dev.write(
                f"{datetime.now()} | FATAL {collision_symbol}  | "
                + f"{file_name} {line_no} :: {message}\n"
            )
        except Exception as e:
            print(e)

    def info(self, message: str):
        """This function logs a message with tag [INFO].

        Params
        ---
            message (str): massage to log.

        Raise
        ---
            Exception: If the message cannot be written to the file.

        Usage
        ---
            >>> from common import Logger
            >>> log = Logger()
            >>> log.info('This is an info message')
        """
        # frame delle chiamate
        frame = inspect.currentframe()
        outer_frame = inspect.getouterframes(frame)
        # prendo il nome del file e il numero di riga
        file_name = outer_frame[1].filename
        line_no = outer_frame[1].lineno
        # scrivo il messaggio nel file
        eyes_symbol = "\U0001F440"
        try:
            self.user.write(
                f"{datetime.now()} | INFO  {eyes_symbol}  | "
                + f"{file_name} {line_no} :: {message}\n"
            )
        except Exception as e:
            print(e)

    def warning(self, message: str):
        """This function logs a message with tag [WARNING].

        Params
        ---
            message (str): massage to log.

        Raise
        ---
            Exception: If the message cannot be written to the file.

        Usage
        ---
            >>> from common import Logger
            >>> log = Logger()
            >>> log.warning('This is a warning message')
        """
        # frame delle chiamate
        frame = inspect.currentframe()
        outer_frame = inspect.getouterframes(frame)
        # prendo il nome del file e il numero di riga
        file_name = outer_frame[1].filename
        line_no = outer_frame[1].lineno
        # scrivo il messaggio nel file
        bell_symbol = "\U0001F514"
        try:
            self.user.write(
                f"{datetime.now()} | WARN  {bell_symbol}  | "
                + f"{file_name} {line_no} :: {message}\n"
            )
        except Exception as e:
            print(e)

    def error(self, message: str):
        """This function logs a message with tag [ERROR].

        Params
        ---
            message (str): massage to log.

        Raise
        ---
            Exception: If the message cannot be written to the file.

        Usage
        ---
            >>> from common import Logger
            >>> log = Logger()
            >>> log.error('This is an error message')
        """
        # frame delle chiamate
        frame = inspect.currentframe()
        outer_frame = inspect.getouterframes(frame)
        # prendo il nome del file e il numero di riga
        file_name = outer_frame[1].filename
        line_no = outer_frame[1].lineno
        # scrivo il messaggio nel file
        collision_symbol = "\U0001F4A5"
        try:
            self.user.write(
                f"{datetime.now()} | ERROR {collision_symbol}  | "
                + f"{file_name} {line_no} :: {message}\n"
            )
        except Exception as e:
            print(e)

    def __del__(self):
        print("common | Logger :: __del__")
        self.user.close()
        self.dev.close()


class LoggerSupport(ABC):
    """This class is used as a support for the logger.

    Attributes
    ---
        - logger (Logger): The logger object.

    """

    def __init__(self, logger: Logger):
        self.logger = logger
        logger.trace(f"{self.__class__.__name__}.__init__")

    def __del__(self):
        self.logger.trace(f"{self.__class__.__name__}.__del__")
