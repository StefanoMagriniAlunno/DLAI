# Main file of the project. Not change its path!
from common import main

if __name__ == "__main__":
    logger = main()

    logger.info("Hello World!")

    del logger
