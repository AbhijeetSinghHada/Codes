import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s: %(lineno)d]: %(message)s',
                    level=logging.DEBUG,
                    filename='logs.txt')
logger = logging.getLogger(__name__)

logger.info("This is just info nothing will print")
logger.warning("This will surely print")

logger.critical("A Critical  Error has occured")