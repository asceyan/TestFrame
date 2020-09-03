#coding:utf-8
import os
from BeautifulReport import BeautifulReport
from common.utility import Utility as utit
from config.config import REPORT_PATH,CASE_PATH
import unittest
import time

t = time.strftime("%Y-%m-%d %H:%M:%S")
report_title = 'WebUI自动化测试报告' + time.strftime("%Y%m%d_%H%M%S.html")
repath = os.path.join(REPORT_PATH, report_title)


if __name__ == '__main__':
    desc = 'UIAutoTestCase'
    test_suite = unittest.defaultTestLoader.discover(CASE_PATH, pattern="test*.py",top_level_dir=None)
    BeautifulReport(test_suite).report(filename=report_title,
                                       description=desc,
                                       log_path=REPORT_PATH)
    # try:
    #     utit.send_email(repath)
    # except Exception as err:
    #     print(err)


