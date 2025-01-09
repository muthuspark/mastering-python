import logging

logger = logging.getLogger(__name__)
module_logger = logging.getLogger(__name__ + ".module")

logger.info("Message from parent logger")
module_logger.debug("Message from child logger")
