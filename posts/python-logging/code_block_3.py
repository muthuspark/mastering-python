import logging

try:
    # Some code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("An error occurred:")