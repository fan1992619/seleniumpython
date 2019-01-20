import sys
sys.path.append('D:\PycharmProjects\Web-selenium')
from util.findelement import FindElement
#读取正确的元素和错误的toast元素的类
class RegisterPage(object):
    def __init__(self,driver):
        self.fd=FindElement(driver)
    #获取邮箱元素
    def get_email_element(self):
        return self.fd.get_element("user_email")
    #获取用户名元素
    def get_username_element(self):
        return self.fd.get_element("user_name")
    #获取密码元素
    def get_password_element(self):
        return self.fd.get_element("password")
    #获取验证码元素
    def get_code_element(self):
        return self.fd.get_element("code_text")
    #获取注册按钮元素
    def get_button_element(self):
        return self.fd.get_element("register_button")
    #获取邮箱错误元素
    def get_email_error_element(self):
        return self.fd.get_element("user_email_error")
    #获取用户名错误元素
    def get_name_error_element(self):
        return self.fd.get_element("user_name_error")
    #获取密码错误元素
    def get_password_error_element(self):
        return self.fd.get_element("password_error")
    #获取验证码错误元素
    def get_code_error_element(self):
        return self.fd.get_element("code_text_error")
if __name__ == '__main__':
    run=RegisterPage()
    run.get_email_element()