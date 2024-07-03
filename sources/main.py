# Description: Main file of the project. Not change its path!


from common import main
from justone import JustOne
from justone.human import Human

if __name__ == "__main__":

    logger = main()

    game = JustOne(
        [
            Human("Alice", logger),
            Human("Bob", logger),
            Human("Carl", logger),
            Human("David", logger),
        ],
        logger,
    )
    game.play(2)

    del game
    del logger
