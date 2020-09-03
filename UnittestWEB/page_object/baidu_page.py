import time

from common.browser_engine import BrowserEngine as BE
from common.base_page import BasePage


"""
    保存页面元素数据
"""


class BaiDuObject(BasePage):
    """通过继承BasePage，来直接操作元素"""
    # 搜索框
    search_box = ('id','kw')
    # 百度一下按键
    baidu_button = ('id','su')

    result = ('xpath','/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/h3/a[1]/em')

    def search_python(self,text='python官网'):
        self.send(self.search_box,text=text)
        self.click(self.baidu_button)

    def result_text(self):
        return self.get_text(self.result)

    def assert_text(self):
        return self.assert_text_equal(self.result,'python官网')


if __name__ == '__main__':
    brow = BE()
    driver = brow.open_browser()
    bd = BaiDuObject(driver)
    # 添加会员操作
    bd.search_python()
    assert bd.result_text()
    print(bd.result_text())
    print(bd.assert_text())
