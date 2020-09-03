# -*- coding: utf-8 -*-
from common.com_nblog import use_logger
"""
    自定义assert，模仿unittest断言方式
        类型
        assertEqual = []  # 判断两个参数相等：first == second
        assertNotEqual = []  # 判断两个参数不相等：first ！= second
        assertTrue = []  # 判断是否为真：expr is True
        assertFalse = []  # 判断是否为假：expr is False
        assertIn = []  # 判断是字符串是否包含：member in container
        assertNotIn = []  # 判断是字符串是否不包含：member not in container
        assertIsNone = []  # 判断是否为None：obj is None
        assertIsNotNone = []  # 判断是否不为None：obj is not None
"""
# 导入日志模块
logger = use_logger('ComAssert')


class ComAssert():

    def assertEqual(self,actual=None,expect=None):
        try:
            assert actual == expect
            return True
        except Exception as e:
            print(e)
            logger.error(F"assertEqual判断失败，预期结果：{expect}，实际结果：{actual}")
            raise (F"assertEqual判断失败，预期结果：{expect}，实际结果：{actual}")

    def assertNotEqual(self,actual=None,expect=None):
        try:
            assert actual != expect
            return True
        except Exception as e:
            logger.error(F"assertNotEqual判断失败，预期结果：{expect}，实际结果：{actual}")
            raise (F"assertNotEqual判断失败，预期结果：{expect}，实际结果：{actual}")

    def assertIn(self,actual=None,expect=None):
        try:
            assert str(actual) in str(expect)
            return True
        except Exception as e:
            logger.error(F"assertIn判断失败，预期结果：{expect}，实际结果：{actual}")
            raise (F"assertIn判断失败，预期结果：{expect}，实际结果：{actual}")

    def assertNotIn(self,actual=None,expect=None):
        try:
            assert str(actual) not in str(expect)
            return True
        except Exception as e:
            logger.error(F"assertNotIn判断失败，预期结果：{expect}，实际结果：{actual}")
            raise (F"assertNotIn判断失败，预期结果：{expect}，实际结果：{actual}")

    def assertTrue(self,actual=None):
        try:
            assert actual is True
            return True
        except Exception as e:
            logger.error(F"assertTrue判断失败，实际结果：{actual}")
            raise (F"assertTrue判断失败，实际结果：{actual}")

    def assertFalse(self,actual=None):
        try:
            assert actual is False
            return True
        except Exception as e:
            logger.error(F"assertFalse判断失败，实际结果：{actual}")
            raise (F"assertFalse判断失败，实际结果：{actual}")

    def assertIsNone(self,actual=None):
        try:
            assert actual is None
            return True
        except Exception as e:
            logger.error(F"assertIsNone判断失败，实际结果：{actual}")
            raise (F"assertIsNone判断失败，实际结果：{actual}")

    def assertIsNotNone(self,actual=None):
        try:
            assert actual is not None
            return True
        except Exception as e:
            logger.error(F"assertIsNotNone判断失败，实际结果：{actual}")
            raise (F"assertIsNotNone判断失败，实际结果：{actual}")

    def assertLess(self,actual):
        try:
            assert actual is not None
            return True
        except Exception as e:
            logger.error(F"assertIsNotNone判断失败，实际结果：{actual}")
            raise (F"assertIsNotNone判断失败，实际结果：{actual}")

    def assert_result(self,assert_type="assertEqual",actual=None,expect=None):
        """
        根据assert_type调用对应的assert方法
        :param assert_type: 默认assertEqual
        :param actual: 实际结果
        :param expect: 预期结果
        :return: bool
        """
        try:
            if assert_type == "assertEqual":
                return self.assertEqual(actual,expect)
            elif assert_type == "assertNotEqual":
                return self.assertNotEqual(actual,expect)
            elif assert_type == "assertTrue":
                return self.assertTrue(actual)
            elif assert_type == "assertFalse":
                return self.assertFalse(actual)
            elif assert_type == "assertIn":
                return self.assertIn(actual,expect)
            elif assert_type == "assertNotIn":
                return self.assertNotIn(actual,expect)
            elif assert_type == "assertIsNone":
                return self.assertIsNone(actual)
            elif assert_type == "assertIsNotNone":
                return self.assertIsNotNone(actual)
        except Exception as e:
            print(e)
            logger.error(F"出现了非法的assert_type或者比较结果False：{assert_type}")
            raise (F"出现了非法的assert_type或者比较结果False：{assert_type}")

    def assert_code(self,status_code,expect):
        """
        判断response.status_code是否如预期
        """
        try:
            return self.assertEqual(status_code,expect)
        except Exception as e:
            print(e)
            logger.error(F"status_code判断失败，预期值：{expect}, 实际值：{status_code}")
            raise (F"status_code判断失败，预期值：{expect}, 实际值：{status_code}")


if __name__ == '__main__':
    ca = ComAssert()
    ep = True
    ac = False
    n = None
    a = ca.assert_result('assertIsNone',None)
    print(a)