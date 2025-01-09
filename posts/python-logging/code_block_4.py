import logging


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) #only INFO and above to console
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
