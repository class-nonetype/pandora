
from app.models.functions.get_path import get_path


import os
import logging




def get_logger(path : str) -> logging.Logger:

    logger = logging.getLogger('logger')
    log_file_path = get_path(os.path.join(path, 'LOG.log'))
                             
    logging.basicConfig(
        filename    = log_file_path,
        level       = logging.DEBUG,
        encoding    = 'utf-8',
        format      = '%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt     = '%Y-%m-%d %H:%M:%S',
    )

    log_formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(log_formatter)

    logger.addHandler(console_handler)
    logger.info('Logger instanciado.')