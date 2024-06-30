# Description: Main file of the project. Not change its path!


from common import Logger
from game import JustOne
from game.human import Human


def main(logger: Logger) -> None:
    """Main function of the project

    Params
    ---
        logger (Logger): logger object

    Raise
    ---
        - TypeError: If the players are less than 2 (fatal)
    """
    try:
        JustOne([Human("Alice", logger), Human("Bob", logger)], logger)
    except TypeError as e:
        logger.fatal(e)


if __name__ == "__main__":

    try:
        log = Logger()
        main(log)
    except FileNotFoundError:
        print("Error opening files.")
    finally:
        del log
