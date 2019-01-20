import  unittest
import os
import HTMLTestRunner
#unittest的case必须以test开始
class FirstCase01(unittest.TestCase):
    #每执行一条case，都会先执行一下setUp,和tearDown
    # @classmethod
    # def setUpClass(cls):
    #     #cls 和self没有什么区别。都是传一个对象进去,建议用官方的cls
    #     print("所有case执行之前的前置")
    # @classmethod
    # def tearDownClass(cls):
    #     print("所有case执行之后的后置")
    def setUp(self):
        print("这个case的前置条件")
    def tearDown(self):
        print("这个case的后置条件")

    # @unittest.skip("不执行第1条")
    def testfirst01(self):
        print("11111")
    @unittest.skip("不执行第二条")
    def testfirst02(self):
        print("22222")
    def testfirst03(self):
        print("33333")
if __name__ == '__main__':
    # unittest.main()
    # file_path=os.path.join(os.getcwd()+"/report/"+"first_case.html")
    file_path="../report/first_case.html"
    f=open(file_path,'wb')
    suite=unittest.TestSuite()
    suite.addTest(FirstCase01("testfirst01"))
    suite.addTest(FirstCase01("testfirst02"))
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="这是第一个html测试报告",description=u"乐学网的注册case报告")
    runner.run(suite)