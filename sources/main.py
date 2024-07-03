# Description: Main file of the project. Not change its path!


import common
from game import JustOne
from game.human import Human

if __name__ == "__main__":

    logger = common.main()

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

    del logger
