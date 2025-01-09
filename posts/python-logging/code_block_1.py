import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('my_app.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug('This debug message goes to the file.')
logger.info('So does this info message.')