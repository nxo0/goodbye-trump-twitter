import logging
import coloredlogs


formatter = "[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)"

Logger = logging.getLogger()


coloredlogs.install(level='DEBUG', logger=Logger, fmt=formatter)


Logger.debug('Logger loaded')
