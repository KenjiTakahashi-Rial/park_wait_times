import logging
from types import ModuleType

DEFAULT_FORMAT: str = "%(asctime)s %(levelname)s %(message)s"
DEFAULT_LEVEL: int = logging.INFO
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_logger() -> ModuleType:
    logging.basicConfig(
        format=DEFAULT_FORMAT,
        level=logging.INFO,
        datefmt=DEFAULT_DATE_FORMAT,
    )
    return logging
