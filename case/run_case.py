import os
import unittest
class RunCase(unittest.TestCase):
    def test_case(self):
        #os.getcwd()获取当前路径，第二个参数，case这个参数表示当前路径的包名,可以不用写
        case_path=os.path.join(os.getcwd())
        #'unittest_*.py'代表以这个命名的py文件都会执行
        suite=unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)
if __name__ == '__main__':
    unittest.main()