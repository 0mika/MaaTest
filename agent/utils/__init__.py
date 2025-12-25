try:
    from .logger import *
except Exception as e:
    logger.exception("agent运行过程中发生异常:{e}")
