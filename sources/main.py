# Description: Main file of the project. Not change its path!


from common import Logger
from game import JustOne
from game.human import Human


def main(log: Logger) -> None:
    """Main function of the project

    Params
    ---
        log (Logger): logger object

    """
    try:
        game = JustOne(
            [
                Human("Alice", log),
                Human("Bob", log),
                Human("Carl", log),
                Human("David", log),
            ],
            log,
        )
        game.play(2)
    except AssertionError as e:
        log.fatal(e)


if __name__ == "__main__":

    main(Logger())
