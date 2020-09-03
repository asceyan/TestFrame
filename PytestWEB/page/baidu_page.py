import allure
from common.com_browser import BrowserEngine as BE
from common.com_base import BasePage


"""
    保存页面元素数据
"""


class BaiDuObject(BasePage):
    """通过继承BasePage类，来直接操作元素"""
    # 搜索框
    search_box = ('id','kw')
    # 百度一下按键
    baidu_button = ('id','su')
    # 搜索结果
    result = ('xpath','/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/h3/a[1]/em')

    @allure.step('搜索框输入文本：python官网-点击搜索按钮')
    def search_python(self,text='python官网'):
        self.send_text(text=text)
        self.click_button()

    @allure.step('搜索框输入文本：python官网')
    def send_text(self,text='python官网'):
        self.send(self.search_box,text=text)

    @allure.step('点击搜索按钮')
    def click_button(self):
        self.click(self.baidu_button)

    def result_text(self):
        return self.get_text(self.result)

    @allure.step('得到搜索结果')
    def assert_element(self):
        return self.is_element_exist(self.result)


if __name__ == '__main__':
    brow = BE()
    driver = brow.open_browser()
    bd = BaiDuObject(driver)
    # 添加会员操作
    bd.search_python()
    assert bd.result_text()
    print(bd.result_text())
    print(bd.assert_element())
