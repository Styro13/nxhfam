"""Logging configuration for the bot."""

import logging
from logging.handlers import TimedRotatingFileHandler


def setup_logger(name: str = "aegis", log_file: str = "aegis.log") -> logging.Logger:
    """Configure and return a logger.

    Parameters
    ----------
    name: str
        Name of the logger to create.
    log_file: str
        File path where logs should be written.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(log_file, when="midnight", backupCount=7)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
