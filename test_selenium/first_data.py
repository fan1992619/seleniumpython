import sys
sys.path.append('D:\PycharmProjects\Web-selenium')
# import traceback
from business.register_business import RegisterBusiness
from selenium import webdriver
# from log.user_log import UserLog
import HTMLTestRunner
import unittest
from util.excel_util import ExcelUtil
import os
import time
import ddt
#类开始的前面要引入数据驱动ddt
ex=ExcelUtil()
data=ex.get_data()
@ddt.ddt
class FirstCase3(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.driver.maximize_window()
        time.sleep(5)
        self.login=RegisterBusiness(self.driver)
        self.file_name="../image/imooc.png"
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
    '''
    当用excel来执行数据驱动的时候就不用该内容了
    #@ddt.data创建数据结构
    @ddt.data(
        ['23','fan1992','111111','../image/imooc.png','user_email_error','请输入有效的电子邮件'],
        ['23sdfsd', 'fan1992', '111111', '../image/imooc.png', 'user_email_error', '请输入有效的电子邮件'],
        ['23sdfsd@qq.com', 'fan1992', '111111', '../image/imooc.png', 'user_email_error', '请输入有效的电子邮件']
    )
    #@ddt.unpack解析数据结构
    @ddt.unpack
    '''
    '''(*data)代表取本地的data数据'''
    @ddt.data(*data)
    def test_register_case(self,data):
        print(data)
        #这个表示给list添加元素，data拿出来的值是一个list
        email, username, password, code, assertCode, assertText=data
        email_error=self.login.register_function(email,username,password,code,assertCode,assertText)
        #通过assert判断是否为error
        self.assertFalse(email_error,"这条case执行了，邮箱没有通过检测")
if __name__ == '__main__':
    # unittest.main()
    file_path="../report/first_case.html"
    f=open(file_path,'wb')
    suite=unittest.TestLoader().loadTestsFromTestCase(FirstCase3)
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='test first result',description="数据驱动的报告")
    runner.run(suite)