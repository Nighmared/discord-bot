"""
defines custom pretty formatter for logs and provides methods to initialize a logger using
said formatter
"""
import logging

DEFAULT = "\033[0m"
BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"


IMPORTS = ()
logger = logging.getLogger("botlogger")


def get_ready():
    """
    initializes custom logging formatter
    """
    for handler in logger.handlers:
        logger.removeHandler(handler)

    fhandler = logging.FileHandler("bot.log", mode="a")
    formatter = BotFormatter(
        fmt="%(asctime)s [%(levelname)s][%(filename)s] %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    logger.setLevel(logging.INFO)


class BotFormatter(logging.Formatter):
    """Custom formatter for prettier logging
    even has colors"""

    def __init__(
        self, fmt: str, datefmt: str, style: str = "%", validate: bool = ...
    ) -> None:
        logging.Formatter.__init__(
            self, fmt=fmt, datefmt=datefmt, style=style, validate=validate
        )

        self.debug_formatter = logging.Formatter(
            fmt=BLUE + fmt + DEFAULT, datefmt=datefmt
        )
        self.info_formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        self.warning_formatter = logging.Formatter(
            fmt=YELLOW + fmt + DEFAULT, datefmt=datefmt
        )
        self.error_formatter = logging.Formatter(
            fmt=MAGENTA + fmt + DEFAULT, datefmt=datefmt
        )
        self.crit_formatter = logging.Formatter(
            fmt=RED + fmt + DEFAULT, datefmt=datefmt
        )
        self.formatters = (
            None,
            self.debug_formatter,
            self.info_formatter,
            self.warning_formatter,
            self.error_formatter,
            self.crit_formatter,
        )

    def format(self, record: logging.LogRecord) -> str:
        return logging.Formatter.format(
            self.formatters[int(record.levelno / 10)], record
        )
