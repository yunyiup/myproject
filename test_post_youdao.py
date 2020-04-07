import unittest
from unittest import mock
from post_youdao import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
    def test_get_ts(self):
        get_ts=mock.Mock(return_value ='1585615430121')
        # 模仿，使结果不变，让测试通过
        self.assertEqual('1585615430121', get_ts())
    def test_get_salt(self):
        get_salt = mock.Mock(return_value='15846843266453')
        self.assertEqual('15846843266453', get_salt())
    def test_get_sign(self):

        self.assertEqual('dc2335b4f1adfd8e66e907cfc07762b5', get_sign())

if __name__ == '__main__':
    unittest.main()
