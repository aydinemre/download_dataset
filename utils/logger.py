import logging
from logging.handlers import RotatingFileHandler


def get_logger(name='logs'):
    logger = logging.getLogger(name)

    logger.setLevel('DEBUG')

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(name)s %(message)s '
        '[in %(pathname)s:%(lineno)d]')

    # StreamHandler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel('DEBUG')

    """
    # RotatingFileHandler
    logger_handler = RotatingFileHandler('logs/{}.log'.format(name), maxBytes=1 * 1024 * 1024)
    logger_handler.setLevel('DEBUG')
    logger_handler.setFormatter(formatter)
    """
    if not logger.handlers:
        # logger.addHandler(logger_handler)
        logger.addHandler(stream_handler)

    return logger
