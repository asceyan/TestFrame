# -*- coding: utf-8 -*-
from nb_log import LogManager
from config.config import LOG_PATH,LOG_FILE_NAME

"""
    封装第三方类 nb_log，具体配置看根目录下nb_log_config.py
"""


def use_logger(log_name):
    logger = LogManager(log_name).get_logger_and_add_handlers(is_add_stream_handler=True,
                                                                  log_filename=LOG_FILE_NAME,
                                                                  log_path=LOG_PATH)
    return logger
