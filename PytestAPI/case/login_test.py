from common.com_base import BaseInterface
from common.com_assert import ComAssert
import allure


@allure.feature('登陆接口测试用例')
class TestLogin():
    CA = ComAssert()
    BI = BaseInterface()

    @allure.story('login接口')
    @allure.title('正确账号密码，登陆成功')
    def test_login_success(self):
        """正确账号密码，登陆成功"""
        r = self.BI.login(user='test2',psw='123456')
        status_code = r.get('code')
        response = r.get('body')
        self.CA.assert_code(status_code, 200)
        self.CA.assert_result(response['code'], 0)
        self.CA.assert_result(response['msg'], 'login success!')

    @allure.story('login接口')
    @allure.title('错误密码，登陆失败')
    def test_login_fail(self,login_fixture):
        """错误密码，登陆失败"""
        r = self.BI.login(user='test2',psw='000000')
        status_code = r.get('code')
        response = r.get('body')
        self.CA.assert_code(status_code, 200)
        self.CA.assert_result(response['code'], 3003)
        self.CA.assert_result(response['msg'], '账号或密码不正确')
