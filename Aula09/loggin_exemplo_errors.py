from loguru import logger

logger.debug("Um aviso para eu no futuro")
logger.info("Informação importante do processo")
logger.warning("Um aviso para algo que vai parar de funcionar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu algo que abortou a aplicação")