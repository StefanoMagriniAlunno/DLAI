Common module
=============

Introduction
------------

This module provides a set of classes that are commonly used in the project.
It is available in all branches since it is defined in the `master` branch.

Dependencies
~~~~~~~~~~~~

This module depends on the following Python standard libraries:

- :mod:`logging` used to define the `logger` variable.
- :mod:`os` used to check if the `temp` directory exists.
- :mod:`tempfile` used to create a new temporary file.
- :mod:`typing` used to provide type hinting for temporary files.

Contents
--------

.. automodule:: common
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

Usage
-----

log manager
~~~~~~~~~~~

The log file is `log/dev.log` and the format of log is:

TIME | PROCESS THREAD | LEVEL | PATH LINE : MEASSAGE

We can use the following levels of logger:
- DEBUG: level 0

- INFO: level 1

- WARNING: level 2

- ERROR: level 3

- CRITICAL: level 4

1. simple warning
+++++++++++++++++

.. code-block:: python

   try:
      raise ValueError('')
   except ValueError as e:
      logger.warning(f'ValueError {e} catched')
   except Exception as e:
      logger.error(f'Unknown Error {e}')
      raise

2. simple error
+++++++++++++++

.. code-block:: python

   try:
      raise ValueError('')
   except ValueError as e:
      logger.error(f'ValueError {e}')
      raise
   except Exception as e:
      logger.error(f'Unknown Error {e}')
      raise

3. simple critical
++++++++++++++++++

.. code-block:: python

   try:
      raise ValueError('')
   except ValueError as e:
      logger.warning(f'ValueError {e} catched')
      try:
         raise an Exception
      except Exception:
         logger.critical(f'An error occurred while recovering ValueError {e}')
         exit(1)
      logger.info(f'ValueError {e} recovered')
   except Exception as e:
      logger.error(f'Unknown Error {e}')
      raise
