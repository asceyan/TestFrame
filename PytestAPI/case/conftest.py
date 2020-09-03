import pytest
from common.com_base import BaseInterface

"""
    用例前置、后置操作
"""


@pytest.fixture(scope='session')
def login_fixture():
    bi = BaseInterface()
    r = bi.login(user="test2")
    token = r['body']['token']
    print('\n用例的前置操作')
    yield token
    print('\n用例的后置操作')