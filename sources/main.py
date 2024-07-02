# Description: Main file of the project. Not change its path!


from common import Logger
from game import JustOne
from game.human import Human

log = Logger()

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
    game.play(-2)
except AssertionError:
    # fix
    try:
        pass
    except Exception as e:
        log.fatal(f"unexpected exception detected: {e}")
    # unsolved
    log.error("AssertionError - unsolved")
    raise
except ValueError:
    # fix
    try:
        game.play(2)
    except Exception as e:
        log.fatal(f"unexpected exception detected: {e}")
    # solved
    log.warning("ValueError - fixed")
except Exception as e:
    log.fatal(f"unexpected exception detected: {e}")

del log
