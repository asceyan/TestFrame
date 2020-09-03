# -*- coding: UTF-8 -*-
import yaml
import os
import smtplib,time
import email.mime.multipart
import email.mime.text
from config.config import ReadConfig
from email.mime.application import MIMEApplication

"""
    封装公共功能，例如：发送邮件，读取yaml文件
"""


t = time.strftime("%Y-%m-%d %H:%M:%S")
email_subject = 'WEB自动化测试已完成'
email_content = '''WEB UI自动化测试已完成. 时间：%s''' %t


class Utility():
    rf = ReadConfig()

    @classmethod
    def send_email(cls,repath,
                   smtp_host='smtp.qq.com',
                   smtp_port=465,
                   subject=email_subject,
                   content=email_content):
        """
        :param smtp_host: 域名
        :param smtp_port: 端口
        :param sendAddr: 发送邮箱
        :param password: 邮箱密码
        :param recipientAddrs: 发送地址
        :param repath: 附件地址
        :param subject: 标题
        :param content: 内容
        :return: 无
        """
        sendAddr = cls.rf.sender
        receiverAddrs = cls.rf.receiver
        password = cls.rf.password

        msg = email.mime.multipart.MIMEMultipart()
        msg['from'] = sendAddr
        msg['to'] = receiverAddrs
        msg['subject'] = subject
        content = content
        txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
        msg.attach(txt)
        # 添加附件地址
        part = MIMEApplication(open(repath, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename="UI自动化测试报告.html")  # 发送文件名称
        msg.attach(part)
        try:
            smtpSSLClient = smtplib.SMTP_SSL(smtp_host, smtp_port)  # 实例化一个SMTP_SSL对象
            loginRes = smtpSSLClient.login(sendAddr, password)  # 登录smtp服务器
            print(f"登录结果：loginRes = {loginRes}")  # loginRes = (235, b'Authentication successful')
            if loginRes and loginRes[0] == 235:
                print(f"登录成功，code = {loginRes[0]}")
                smtpSSLClient.sendmail(sendAddr, receiverAddrs, str(msg))
                smtpSSLClient.quit()
                print('发送邮件成功')
            else:
                print(f"登陆失败，code = {loginRes[0]}")
        except Exception as e:
            print(f"发送失败，Exception: e={e}")


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在！')
        self.list_data =[]
        self._data = None

    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf,'r') as f:
                self._data = yaml.load(f)
                for v in self._data.values():
                    self.list_data.append(v)
        return self.list_data
