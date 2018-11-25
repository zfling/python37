import unittest

class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('1')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('')
        print('22')
        pass

    @classmethod
    def tearDownClass(self):
    # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
         print('4444')
    @classmethod
    def setUpClass(self):
    # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('333')

    def test_a_run(self):
        self.assertEqual(1, 1)  # 测试用例
        
    def test_b_run(self):
        self.assertEqual(2, 2)  # 测试用例
        
    def test_c_run(self):
        self.assertEqual(3, 3)  # 测试用例
        
if __name__ == '__main__':
    unittest.main(verbosity = 2)#运行所有的测试用例
