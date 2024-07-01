# This file contains the logger class, which is used to log messages to a file.
import inspect
from abc import ABC
from datetime import datetime


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
        - fatal(message): Logs a message with tag [FATAL]
        - info(message): Logs a message with tag [INFO]
        - warning(message): Logs a message with tag [WARNING]
        - error(message): Logs a message with tag [ERROR]
    """

    def __init__(self, user: str = "logs/user.log", dev: str = "logs/dev.log"):
        """This function initializes the Logger class.

        Params
        ---
            - user (str, optional):
                path for the user's log. Defaults to "logs/user.log".
            - dev (str, optional):
                path for the developer's log. Defaults to "logs/dev.log".

        Usage
        ---
            >>> from common import Logger
            >>> log = Logger()
        """
        print("Logger.__init__")
        # pulisco i file
        with open(user, "w") as f:
            f.write("")
        with open(dev, "w") as f:
            f.write("")
        self.user = user
        self.dev = dev

    def __del__(self):
        print("Logger.__del__")

    def trace(self, message: str = ""):
        """This function logs a message with tag [TRACE].

        Params
        ---
            message (str, optional): massage to log. Defaults to ''.

        Usage
        ---
            >>> from common import Logger
            >>> log = Logger()
            >>> log.trace('This is a trace message')
        """
        # frame delle chiamate
        frame = inspect.currentframe()
        outer_frame = inspect.getouterframes(frame)
        # prendo il nome del file e il numero di riga
        file_name = outer_frame[1].filename
        line_no = outer_frame[1].lineno
        # scrivo il messaggio nel file
        eyes_char = "\U0001F440"
        with open(self.dev, "a", encoding="utf-8") as f:
            f.write(
                f"{datetime.now()} | TRACE {eyes_char}  | "
                + f"{file_name} {line_no} :: {message}\n"
            )

    def debug(self, message: str = ""):
        """This function logs a message with tag [DEBUG].

        Params
        ---
            message (str, optional): massage to log. Defaults to ''.

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
        with open(self.dev, "a", encoding="utf-8") as f:
            f.write(
                f"{datetime.now()} | DEBUG {stethoscope_symbol} | "
                + f"{file_name} {line_no} :: {message}\n"
            )

    def fatal(self, message: str):
        """This function logs a message with tag [FATAL].

        Params
        ---
            message (str): massage to log.

        Usage
        ---
            >>> try:
            >>>     # some code that raise Exception
            >>> except Exception as e:
            >>>     log.fatal(str(e))

        Note: kill the program with exit() function.
        """
        # frame delle chiamate
        frame = inspect.currentframe()
        outer_frame = inspect.getouterframes(frame)
        # prendo il nome del file e il numero di riga
        file_name = outer_frame[1].filename
        line_no = outer_frame[1].lineno
        # scrivo il messaggio nel file
        collision_symbol = "\U0001F4A5"
        with open(self.dev, "a", encoding="utf-8") as f:
            f.write(
                f"{datetime.now()} | FATAL {collision_symbol}  | "
                + f"{file_name} {line_no} :: {message}\n"
            )
        print("\033[91m" + "EMERGENCY! FATAL ERROR!" + "\033[0m")
        exit(1)

    def info(self, message: str):
        """This function logs a message with tag [INFO].

        Params
        ---
            message (str): massage to log.

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
        with open(self.user, "a", encoding="utf-8") as f:
            f.write(
                f"{datetime.now()} | INFO  {eyes_symbol}  | "
                + f"{file_name} {line_no} :: {message}\n"
            )

    def warning(self, message: str):
        """This function logs a message with tag [WARNING].

        Params
        ---
            message (str): massage to log.

        Usage
        ---
            >>> try:
            >>>     # some code that raise Exception
            >>> except Exception as e:
            >>>     log.warning(str(e))
            >>>     # do something
            >>>     # continue the program
        """
        # frame delle chiamate
        frame = inspect.currentframe()
        outer_frame = inspect.getouterframes(frame)
        # prendo il nome del file e il numero di riga
        file_name = outer_frame[1].filename
        line_no = outer_frame[1].lineno
        # scrivo il messaggio nel file
        bell_symbol = "\U0001F514"
        with open(self.user, "a", encoding="utf-8") as f:
            f.write(
                f"{datetime.now()} | WARN  {bell_symbol}  | "
                + f"{file_name} {line_no} :: {message}\n"
            )

    def error(self, message: str):
        """This function logs a message with tag [ERROR].

        Params
        ---
            message (str): massage to log.

        Usage
        ---
            >>> try:
            >>>     # some code that raise Exception
            >>> except Exception as e:
            >>>     log.error(str(e))
            >>>     # do something
            >>>     reise e
        """
        # frame delle chiamate
        frame = inspect.currentframe()
        outer_frame = inspect.getouterframes(frame)
        # prendo il nome del file e il numero di riga
        file_name = outer_frame[1].filename
        line_no = outer_frame[1].lineno
        # scrivo il messaggio nel file
        collision_symbol = "\U0001F4A5"
        with open(self.user, "a", encoding="utf-8") as f:
            f.write(
                f"{datetime.now()} | ERROR {collision_symbol} | "
                + f"{file_name} {line_no} :: {message}\n"
            )


class LoggerSupport(ABC):
    """This abstract class is used as a support for the logger.

    Attributes
    ---
        log (Logger): The logger object.

    """

    def __init__(self, log: Logger):
        self.log = log
        log.trace(f"{self.__class__.__name__}.__init__")

    def __del__(self):
        self.log.trace(f"{self.__class__.__name__}.__del__")
