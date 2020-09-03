# -*- coding: utf-8 -*-
import unittest, time
from common.browser_engine import BrowserEngine
from page_object.baidu_page import BaiDuObject
from BeautifulReport import BeautifulReport
stime = time.strftime("%Y%m%d%H%M%S")


class BaiDuCase(unittest.TestCase):
    """baidu 搜索用例demo"""

    @classmethod
    def setUpClass(cls):
        """前置操作：启动driver"""
        browser = BrowserEngine()
        cls.driver = browser.open_browser()
        cls.BD = BaiDuObject(cls.driver)

    @classmethod
    def tearDownClass(cls):
        """后置操作：关闭浏览器"""
        cls.BD.quit_browser()

    def setUp(self):
        """每个用例开始前，执行一次"""
        pass

    def tearDown(self):
        """每个用例结束后，执行一次"""
        pass

    def save_img(self,img_name):
        """保存错误截图的方法"""
        self.BD.get_windows_img(img_name)

    @BeautifulReport.add_test_img(stime)
    def test_search_python(self):
        """case:百度搜索python官网，搜索成功"""
        self.BD.search_python()
        self.save_img(stime)    # 截图
        assert self.BD.assert_text()

    @BeautifulReport.add_test_img(stime)
    def test_search_python_error(self):
        """case:百度搜索python官网，搜索成功"""
        self.BD.search_python()
        self.save_img(stime)    # 截图
        assert not self.BD.assert_text()



if __name__ == '__main__':
    unittest.main()
