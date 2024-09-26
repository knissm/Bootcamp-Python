from loguru import logger
from time_decorator import time_measure_decorator

logger.add("meu_app.log")


@time_measure_decorator
def soma(x, y):
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x+y

soma(1,2)
soma(1,2)