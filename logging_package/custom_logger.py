import logging
import inspect


def custom_logging(log_level):

    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel('DEBUG')

    file_handler = logging.FileHandler("{0}.log".format(logger_name), mode='w')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%d-%m-%Y %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


