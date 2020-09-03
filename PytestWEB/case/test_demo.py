# -*- coding: utf-8 -*-
import allure
import pytest


@allure.feature('百度搜索测试用例集')
class TestBaiDuSearch():

    @allure.story('百度搜索成功案例')
    def test_search_python(self,get_driver):
        """打开百度搜索python官网，搜索成功"""
        driver = get_driver
        driver.search_python()
        assert driver.assert_element()

    # @allure.story('百度搜索失败案例')
    # def test_search_python_error(self,get_driver):
    #     """case:百度搜索python官网，搜索失败"""
    #     driver = get_driver
    #     driver.search_python()
    #     assert not driver.assert_text()



if __name__ == '__main__':
    pytest.main()