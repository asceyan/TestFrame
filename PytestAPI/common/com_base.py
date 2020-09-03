import os
from common.com_request import Request
"""
    定义接口的基类，封装测试接口
"""


class BaseInterface():

    def __init__(self):
        self.re = Request()

    def login(self,user="test1", psw="123456"):
        '''实现登录'''
        url = os.environ['base-url'] + "/api/v1/login"
        body = {
            "username": user,
            "password": psw
        }
        r = self.re.post_request(url, json=body)
        return r

    def get_info(self,token):
        '''获取个人信息'''
        url = os.environ['base-url'] + "/api/v1/userinfo"

        h = {
            "Authorization": "Token " + token
        }
        r2 = self.re.get_request(url,header=h)
        return r2


if __name__ == '__main__':
    os.environ['base-url'] = 'http://49.235.92.12:6009'
    bi = BaseInterface()
    r = bi.login(user="test2")
    token = r['body']['token']
    print(token)
    r2 = bi.get_info(token)
    print(r2)

