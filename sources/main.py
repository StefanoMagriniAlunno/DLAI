# Description: Main file of the project. Not change its path!

from common import Logger
from game import JustOne
from game.human import Human
from game.vocabulary import Vocabulary


def main(logger: Logger):
    # creo il vocabolario
    vocab_path = "/db/words_alpha.txt"
    try:
        vocab = Vocabulary(vocab_path, logger)
    except FileNotFoundError as e:
        logger.fatal(e)
        return

    # creo il gioco
    try:
        game = JustOne([Human("Alice", logger), Human("Bob", logger)], vocab, logger)
    except TypeError as e:
        logger.fatal(e)
        return

    # gioco
    ret = game(2)
    logger.info(ret)


if __name__ == "__main__":
    log = Logger()
    main(log)
