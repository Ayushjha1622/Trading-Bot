from core.logger import Logger

logger = Logger.get_logger(__name__)


def main():
    logger.info("Trading Bot Started")
    logger.warning("This is a warning")
    logger.error("This is an error")


if __name__ == "__main__":
    main()