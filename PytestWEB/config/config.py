# -*- coding: utf-8 -*-
import os,time
from configparser import ConfigParser
"""
    定义全局变量，文件路径等参数
"""

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_PATH, 'config','config.ini')
CASE_PATH = os.path.join(BASE_PATH,'case','')
DATA_PATH = os.path.join(BASE_PATH, 'data','')
LOG_PATH = os.path.join(BASE_PATH, 'logs','')
REPORT_PATH = os.path.join(BASE_PATH, 'report','')
SCREENSHOTS_PATH = os.path.join(BASE_PATH, 'img','')
LOG_FILE_NAME = LOG_PATH + time.strftime('%Y%m%d%H%M%S.logs')



class ReadConfig:
    # titles:
    TITLE_SERVER = "testServer"
    TITLE_BROWSER = "browserType"
    TITLE_EMAIL = "sendEmail"
    # values:
    # [testServer]
    VALUE_URL = "URL"
    VALUE_RECEVICE_ADDR = "receiveAddr"
    # [browserType]
    VALUE_BROWSER = 'browserName'
    # [loginCookie]
    VALUE_COOKIE = 'cookieValue'
    # [Email]
    VALUE_SEND_ADDR = "sendAddr"
    VALUE_PASSWORD = "password"

    def __init__(self):
        self.config = ConfigParser()
        if not os.path.exists(CONFIG_FILE):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(CONFIG_FILE, encoding='utf-8')
        self.server_url = self.get_conf(self.TITLE_SERVER, self.VALUE_URL)
        self.browser = self.get_conf(self.TITLE_BROWSER, self.VALUE_BROWSER)
        self.sender = self.get_conf(self.TITLE_EMAIL, self.VALUE_SEND_ADDR)
        self.receiver = self.get_conf(self.TITLE_EMAIL, self.VALUE_RECEVICE_ADDR)
        self.password = self.get_conf(self.TITLE_EMAIL, self.VALUE_PASSWORD)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(CONFIG_FILE, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(CONFIG_FILE, "w+") as f:
            return self.config.write(f)



if __name__ == '__main__':
    rc = ReadConfig
