import time
import pytest
import os
from config.config import REPORT_PATH
from common.com_shell import Shell


class Run:

    def __init__(self):
        # 报告文件文件夹，防止生成的报告内容叠加
        now_time = time.strftime('%m%d%H%M%S', time.localtime())
        mkdir = os.path.join(REPORT_PATH, 'report-' + now_time)
        self.result_path = os.path.join(mkdir, 'result')
        self.report_path = os.path.join(mkdir, 'allure_report')

    def run_case(self):
        # 执行测试
        args = ['-s', "--alluredir", F"{self.result_path}"]
        pytest.main(args)
        # 生成测试报告
        cmd = F"allure generate {self.result_path} -o {self.report_path} --clean"
        Shell().invoke(cmd)


if __name__ == '__main__':
    Run().run_case()

