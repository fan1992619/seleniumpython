import  unittest
#unittest的case必须以test开始
class FirstCase02(unittest.TestCase):
    #每执行一条case，都会先执行一下setUp,和tearDown
    @classmethod
    def setUpClass(cls):
        #cls 和self没有什么区别。都是传一个对象进去,建议用官方的cls
        print("所有case执行之前的前置")
    @classmethod
    def tearDownClass(cls):
        print("所有case执行之后的后置")
    def setUp(self):
        print("这个case的前置条件")
    def tearDown(self):
        print("这个case的后置条件")

    # @unittest.skip("不执行第1条")
    def testfirst1(self):
        print("----------------")
    # @unittest.skip("不执行第二条")
    def testfirst2(self):
        print("=============")
    def testfirst3(self):
        print("-----======")
if __name__ == '__main__':
    unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(FirstCase('testfirst01'))
    # unittest.TextTestRunner.run(suite)