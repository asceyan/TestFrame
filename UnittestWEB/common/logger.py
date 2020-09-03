import logging
import time
from config.config import LOG_PATH

"""
    封装日志模块
"""
class Logger(object):
    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件,将日志存入到指定的文件中
        :param logger:
        """

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        log_name = LOG_PATH + time.strftime('%Y%m%d%H%M%S.logs')
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)

        #ch.setLevel(logging.ERROR)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        # self.logger.addHandler(ch)

    def getlog(self):
        return self.logger



if __name__ == '__main__':
    log_name = LOG_PATH + time.strftime('%Y%m%d%H%M%S.logs')
    print(log_name)

