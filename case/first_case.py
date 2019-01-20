import sys
sys.path.append('D:\PycharmProjects\Web-selenium')
# import traceback
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import HTMLTestRunner
import unittest
import os
import time
# #放以后的case
class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_log = UserLog()
        cls.log = cls.user_log.get_log()
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.driver.maximize_window()
        time.sleep(5)
        self.login=RegisterBusiness(self.driver)
        self.log.info("test_first")
        # self.file_name="../image/imooc.png"
        self.file_name="12345"
    def tearDown(self):
        #python3里面捕获异常的方法
        #self._outcome.errors:表示去捕获异常
        #self._testMethodName表示每条case执行后
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                file_path="../report/{0}.png".format(case_name)
                self.driver.save_screenshot(file_path)
        self.driver.quit()
    @classmethod
    def tearDownClass(cls):
        cls.user_log.close_log()
    def test_login_email_error(self):
        email_error=self.login.login_email_error('340','fan199261','111111',self.file_name)
        print(email_error)
        #通过assert判断是否为error
        self.assertFalse(email_error,"这条case执行了，邮箱没有通过检测")
    def test_login_username_error(self):
        username_error=self.login.login_name_error('fan1992618@163.com','dsfgdf','111111',self.file_name)
        print(username_error)
        self.assertFalse(username_error)
        #通过assert判断是否为error
    def test_login_code_error(self):
        code_error=self.login.login_code_error('fan1992618@163.com','fan1992618','111111',self.file_name)
        self.assertTrue(code_error)
    def test_login_password_error(self):
        password_error=self.login.login_password_error('fan1992618@163.com','fan1992618','11',self.file_name)
        self.assertTrue(password_error)
    def test_login_succes(self):
        self.login.user_base('fan1992618@163.com','fan1992618','111111',self.file_name)
        succes=self.login.register_succes()
        self.assertTrue(succes)
if __name__ == '__main__':
    # unittest.main()
    file_path="D:\PycharmProjects\Web-selenium\\report\\first_case.html"
    f=open(file_path,'wb')
    suite=unittest.TestSuite()
    suite.addTest(FirstCase("test_login_email_error"))
    suite.addTest(FirstCase("test_login_username_error"))
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="这是第一个html测试报告",description=u"乐学网的注册case报告")
    runner.run(suite)