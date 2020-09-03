# -*- coding: utf-8 -*-
import time
from nb_log import LogManager
from config.Config import LOG_PATH

"""
    封装第三方类 nb_log，具体配置看根目录下nb_log_config.py
"""

log_file = LOG_PATH + time.strftime('%Y%m%d%H%M%S.logs')
def use_logger(log_name):
    logger = LogManager(log_name).get_logger_and_add_handlers(is_add_stream_handler=True,
                                                                  log_filename=log_file,
                                                                  log_path=LOG_PATH)
    return logger
