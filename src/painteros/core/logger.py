import logging


def get_logger(name="PainterOS"):
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    return logging.getLogger(name)
