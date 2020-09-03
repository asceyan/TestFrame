# 配置全局的fixture
import os
import pytest


def pytest_addoption(parser):
    """
    添加pytest命令行参数--base-url
    action='store' 固定写法
    default='****'  设置默认值
    help='****'  帮助信息
    终端执行pytest默认使用pytest.ini上的配置的url，
    可以通过pytest --base_url='***'来直接执行修改后的测试环境
    """
    parser.addoption('--base-url',
                     action='store',
                     default='base-url=http://49.235.92.12:6009',
                     help='base-url option：url地址')


# autouse=True 不需要调用就可以自动执行
@pytest.fixture(scope='session',autouse=True)
def base_url_fixture(request):
    """
    fixture中设置base-url，用例中不需要调用fixture
    注意：环境变量只能通过pytest执行
    """
    os.environ['base-url'] = request.config.getoption("--base-url")

