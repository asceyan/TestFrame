from selenium import webdriver
from common.logger import Logger
from config.config import CONFIG_FILE
from config.config import ReadConfig
logger = Logger(logger='BrowserEngine').getlog()


class BrowserEngine():
    def open_browser(self):
        """
        从config文件中读取browser、url并驱动相应浏览器
        :return: self.driver
        """
        browser = ReadConfig().browser
        logger.info("检查并选择 浏览器: %s ." % browser)
        url = ReadConfig().server_url
        logger.info("检查并选择 url: %s" % url)

        if browser == 'Firefox':
            self.driver = webdriver.Firefox()
            logger.info('启动Firefox浏览器...')

        elif browser == 'Chrome':
            self.driver = webdriver.Chrome()
            logger.info('启动Chrome浏览器...')

        elif browser == 'IE':
            self.driver = webdriver.Ie()
            logger.info('启动IE浏览器...')

        else:
            logger.error('浏览器启动失败，请检查 %s 文件...'%CONFIG_FILE)
            raise Exception('浏览器启动失败，请检查 %s 文件...'%CONFIG_FILE)

        self.driver.get(url)
        logger.info('打开 url : %s' % url)
        self.driver.maximize_window()
        logger.info("最大化窗口...")
        self.driver.implicitly_wait(5)
        logger.info("设置隐式等待时间5s...")
        return self.driver



if __name__ == '__main__':
    be = BrowserEngine()
    be.open_browser()
