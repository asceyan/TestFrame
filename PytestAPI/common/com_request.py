# -*- coding: utf-8 -*-
import os,time
import random
from requests_toolbelt import MultipartEncoder
import requests
import urllib3
from common.com_nblog import use_logger
logger = use_logger('Request')
# 忽略InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
    通过requests.Session()自动管理会话；
    封装request的get、post请求；
    将接口的相应内容装入response_dicts并返回
"""


class Request:
    def __init__(self):
        self.s = requests.Session()
        # 模拟真机访问接口
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)\
                          Chrome/67.0.3396.99 Safari/537.36",
        }
        self.s.headers.update(headers)

    def get_request(self, url, data=None, header=None):
        """Get请求"""
        try:
            if data is None:
                response = self.s.get(url=url, headers=header)
                logger.info(f'发送request请求成功！method：get, url:{url}, headers={header}, data:为空')
                print('request data is None!')
            else:
                response = self.s.get(url=url, params=data, headers=header)
                logger.info(f'发送request请求成功！method：get, url:{url}, headers={header}, data:{data}')

        except requests.RequestException as e:
            logger.error(f'发送request请求失败！ RequestException url:', url)
            raise e

        # 接口响应时间，单位毫秒
        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        # 创建一个字典 接收response响应内容
        response_dicts = dict()
        response_dicts['status_code'] = response.status_code
        try:
            response_dicts['response_body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['response_body'] = ''
        response_dicts['response_text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        logger.info(f"接口响应成功！,响应内容:{response_dicts}")
        return response_dicts

    def post_request(self, url, data=None, json=None, header=None):
        """Post请求"""
        try:
            if not data is None:
                response = self.s.post(url=url, data=data, headers=header)
                logger.info(f'发送request请求成功！method：get, url:{url}, headers={header}, data:{data}')
            elif not json is None:
                response = self.s.post(url=url, json=json, headers=header)
                logger.info(f'发送request请求成功！method：get, url:{url}, headers={header}, data:{data}')
            else:
                response = self.s.post(url=url, headers=header)
                logger.info(f'发送request请求成功！method：get, url:{url}, headers={header}, data:为空')
                print('request data is None!')
        except requests.RequestException as e:
            logger.error(f'发送request请求失败！ RequestException url:', url)
            raise e

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        logger.info(f"接口响应成功！,响应内容:{response_dicts}")
        return response_dicts

    def post_request_multipart(self, url, data=None, header=None, file_parm=None, file=None, f_type=None):
        """
        提交Multipart/form-data 格式的Post请求
        m = MultipartEncoder(fields={'a':'1','b':'2','c' :('filename',open('file.py','rb'),'jmage/png')})
        r = requests.post(url,data=m,headers={'Content-Type':m.content_type})
        """
        try:
            if data is None:
                response = self.s.post(url=url, headers=header)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type

                m = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = m.content_type
                response = self.s.post(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def put_request(self, url, data=None, header=None):
        """
        Put请求
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = self.s.put(url=url, headers=header)
            else:
                response = self.s.put(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts
