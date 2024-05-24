import logging
logging.basicConfig(filemode= "mylogs.log", level= logging.DEBUG)
logger = logging.getLogger()
logger.info("info")
logger.debug("debug")
