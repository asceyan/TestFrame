# -*- coding: utf-8 -*-
import pytest
from common.com_browser import BrowserEngine
from page.baidu_page import BaiDuObject

"""
    项目全局配置
    用例前置操作：启动driver
    用例后置操作：关闭浏览器
"""


@pytest.fixture(scope='session')
def get_driver():
    browser = BrowserEngine()
    driver = browser.open_browser()
    bd = BaiDuObject(driver)
    yield bd
    # 后置操作：关闭浏览器
    bd.quit_browser()


# 登陆fixture 示例
# @pytest.fixture(scope='session')
# def login(get_driver):
#     driver = get_driver
#     bd = BaiDuObject(driver)
#     bd.login()
#     return driver
