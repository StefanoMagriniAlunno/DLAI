Common module
=============

Introduction
------------

This module provides a set of classes that are commonly used in the project.
The module is divided into two files: logger.py and tempgen.py
This module is defined in branch master, so it is available in all branches.

**logger.py**

This file contains the Logger class, which is used to log events in the project
in two specific files: 'usr.log' and 'dev.log'.

**tempgen.py**

This file contains the TempGen class, which is used to generate temporary files
in the project folder: 'temp'.

Dependencies
~~~~~~~~~~~~

This module depends on the following modules:

* **inspect** used in logger.py to get the name of the calling function.

* **abc.ABC** used in logger.py to define the LoggerSupport class as an
* abstract class.

* **datetime.datetime** used in logger.py to get the current date and time.

* **os** used in tempgen.py to check if the folder 'temp' exists.

* **tempfile** used in tempgen.py to create temporary files.

Contents
--------

Defined Types
~~~~~~~~~~~~~

Logger
^^^^^^

This class is used to log events in the project in two specific files:
'usr.log' and 'dev.log'. In particular the class manages the following
log levels:

* **trace** used to log trace events in the 'dev.log' file.

* **debug** used to log debug events in the 'dev.log' file.

* **fatal** used to log info events in the 'fatal.log' file.

* **info** used to log info events in the 'usr.log' file.

* **warning** used to log warning events in the 'usr.log' file.

* **error** used to log error events in the 'usr.log' file.

When the Logger class is instantiated, it creates the 'usr.log' and 'dev.log'
files in the project folder 'logs'. In addition, the Logger print its
initialization, finalization and exception in the console.

.. code-block:: python

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
            frame = inspect.currentframe()
            outer_frame = inspect.getouterframes(frame)
            file_name = outer_frame[1].filename
            line_no = outer_frame[1].lineno
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
            frame = inspect.currentframe()
            outer_frame = inspect.getouterframes(frame)
            file_name = outer_frame[1].filename
            line_no = outer_frame[1].lineno
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
                >>>     try:
                >>>         # do something to recover
                >>>     except Exception as e:
                >>>         log.fatal("")

            Note: kill the program with exit() function.
            """
            frame = inspect.currentframe()
            outer_frame = inspect.getouterframes(frame)
            file_name = outer_frame[1].filename
            line_no = outer_frame[1].lineno
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
            frame = inspect.currentframe()
            outer_frame = inspect.getouterframes(frame)
            file_name = outer_frame[1].filename
            line_no = outer_frame[1].lineno
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
            """
            frame = inspect.currentframe()
            outer_frame = inspect.getouterframes(frame)
            file_name = outer_frame[1].filename
            line_no = outer_frame[1].lineno
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
                >>>     log.error(f"unexpected error {e}")
            """
            frame = inspect.currentframe()
            outer_frame = inspect.getouterframes(frame)
            file_name = outer_frame[1].filename
            line_no = outer_frame[1].lineno
            collision_symbol = "\U0001F4A5"
            with open(self.user, "a", encoding="utf-8") as f:
                f.write(
                    f"{datetime.now()} | ERROR {collision_symbol} | "
                    + f"{file_name} {line_no} :: {message}\n"
                )

LoggerSupport
^^^^^^^^^^^^^

This class is used to define the Logger class as an abstract class.
In particular, the class defines methods for logging the initialization
and finalization automatically. It is important call
**super().__init__()** and **super().__del__()** in the
**__init__** and **__del__** methods of the derived class:

.. code-block:: python

    class my_class(LoggerSupport):
        def __init__(self, log: Logger):
            super().__init__(log)

        def __del__(self):
            super().__del__()

Source code:

.. code-block:: python

    class LoggerSupport(ABC):
        """This abstract class is used as a support for the logger.

        Attributes
        ---
            log (Logger): The logger object.

        """

        def __init__(self, log: Logger):
            log.trace(f"{self.__class__.__name__}.__init__")
            self.log = log

        def __del__(self):
            self.log.trace(f"{self.__class__.__name__}.__del__")


TempGen
^^^^^^^

This class is used to generate temporary files in the project folder: 'temp'.
In particular, an object of this class is a generator that creates names for temporary files.

Source code:

.. code-block:: python

    class TempGen:
        """TempGen class
        This class creates a temporary file in the specified directory.

        Attributes
        ---
            directory (str): The directory where the temporary file is created.

        Usage
        ---
            >>> from common import TempGen
            >>> tmp = TempGen()
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
            print("TempGen.__init__")
            if not os.path.exists(directory):
                raise FileNotFoundError(f"Directory '{directory}' not found.")
            self.directory = directory

        def __call__(self) -> IO[bytes]:
            temp_file = tempfile.NamedTemporaryFile(dir=self.directory)
            return temp_file

        def __del__(self):
            print("TempGen.__del__")

Usage Examples
--------------

Esempi di utilizzo del modulo e delle sue funzioni.

Example1
~~~~~~~~

Descrizione e codice di esempio1.

Example2
~~~~~~~~

Descrizione e codice di esempio2.

Notes
-----

Note aggiuntive e commenti sul modulo.

References
----------

Riferimenti e link utili.
