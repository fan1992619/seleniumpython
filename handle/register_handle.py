from page.register_page import RegisterPage
# import sys
from util.get_code import GetCode
# # from log.user_log import UserLog
#输入框操作的流程,可以直接调用findelement里面的方法来。也不可以不用，现在这里是单独封装的方法
class RegisterHandle(object):
    def __init__(self,driver):
        self.driver=driver
        self.get_code_text=GetCode(self.driver)
        self.register_p=RegisterPage(self.driver)
    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)
    #输入用户名
    def send_user_name(self,username):
        self.register_p.get_username_element().send_keys(username)
    #输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)
    #输入验证码
    def send_user_code(self,file_name):
        code=self.get_code_text.code_online(file_name)
        self.register_p.get_code_element().send_keys(code)
    #不需要去解析验证码，直接输入
    def send_user_codetext(self,code):
        self.register_p.get_code_element().send_keys(code)
    #获取文字信息
    def get_user_text(self,info,user_info):
        #通过错误的信息来判断
        try:
            if info=="user_email_error":
                #get_attribute("value") value 和text都可以拿到值,使用value一定要有value属性
                text=self.register_p.get_email_error_element().text
            elif info=="user_name_error":
                text =self.register_p.get_name_error_element().text
            elif info=="password_error":
                text =self.register_p.get_password_error_element().text
            elif info=="code_error":
                text =self.register_p.get_code_error_element().text
        except:
            text=None
        return text
    #点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()
    #获取注册按钮文字
    def get_register_text(self):
        self.register_p.get_button_element().get_attribute("value")

