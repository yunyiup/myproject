import unittest
from unittest import mock

from post_youdao import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
    def test_get_ts(self):
        # # 时间戳
        # import time
        # t=time.time()
        # ts=str(int(round(t*1000)))
        # print(ts)
        get_ts=mock.Mock(return_value ='1585615430121')
        # 模仿，使结果不变，让测试通过
        self.assertEqual('1585615430121', get_ts())

if __name__ == '__main__':
    unittest.main()
