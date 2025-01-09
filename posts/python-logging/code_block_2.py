import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING) # Only WARNING and above are logged


logger.debug('This debug message will be ignored.')
logger.warning('This warning message will be logged.')
