import logging
import sys

logger = logging.getLogger(__name__)


def main():
    logger.info("Hello World")


def setup_logger():
    """Setup default logging formatter and level."""
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    formatter = logging.Formatter("%(levelname)s %(asctime)s %(name)s: %(message)s")
    s_handler = logging.StreamHandler(sys.stdout)
    s_handler.setFormatter(formatter)

    params = {"level": logging.DEBUG, "handlers": [s_handler]}
    logging.basicConfig(**params)


if __name__ == "__main__":
    try:
        setup_logger()
        main()

    except KeyboardInterrupt:
        logger.info("Caught keyboard interrupt")
    except Exception as err:
        logger.error(err, exc_info=True)
    finally:
        logger.info("Exiting...")
