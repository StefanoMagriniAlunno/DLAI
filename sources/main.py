# Description: Main file of the project. Not change its path!


from common import Logger
from game import JustOne
from game.human import Human


def main(log: Logger) -> None:
    """Main function of the project

    Params
    ---
        log (Logger): logger object

    Raise
    ---
        - TypeError: If the players are less than 2 (fatal)
    """
    try:
        game = JustOne([Human("Alice", log), Human("Bob", log)], log)
    except TypeError as e:
        log.fatal(e)

    # simulo una partita
    game.play(2)


if __name__ == "__main__":

    main(Logger())
