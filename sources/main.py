# Description: Main file of the project. Not change its path!

from common import Logger
from game import JustOne


def main(logger: Logger):
    try:
        JustOne([], logger)
    except TypeError as e:
        logger.fatal(e)
        return


if __name__ == "__main__":
    log = Logger()
    main(log)
