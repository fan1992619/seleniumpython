#coding=utf-8
from selenium import webdriver
from handle.register_handle import RegisterHandle
from selenium import webdriver
#执行操作的业务层，判断输入的内容是否正确。
class RegisterBusiness:
    def __init__(self,driver):
        # self.driver=webdriver.Chrome()
        # self.driver.get("http://www.5itest.cn/register")
        self.register_h=RegisterHandle(driver)
    def user_base(self,email,name,password,file_name):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        # self.register_h.send_user_code(file_name)
        self.register_h.send_user_codetext(file_name)
        self.register_h.click_register_button()
    def register_function(self,email,username,password,file_name,assertCode,assertText):
        self.user_base(email,username,password,file_name)
        if self.register_h.get_user_text("user_email_error","请输入有效的电子邮件")==None:
            print("邮箱检验不成功true")
            return True
        else:
            print("false")
            return False
    def login_email_error(self,email,name,password,file_name):
        #如果出现没有错误的toast，代表没有检验成功
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text("email_error","请输入有效的电子邮件")==None:
            print("邮箱检验不成功")
            return True
        else:
            return False
    def login_name_error(self, email, name, password, file_name):
        # 如果出现没有错误的toast，代表没有检验成功
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("name_error", "字符长度必须大于等于4，一个中文字算2个字符") == None:
            print("用户名检验不成功")
            return True
        else:
            return False
    def login_password_error(self, email, name, password, file_name):
        # 如果出现没有错误的toast，代表没有检验成功
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("code_error", "最少需要输入 5 个字符") == None:
            print("最少需要输入 5 个字符")
            return True
        else:
            return False
    def login_code_error(self, email, name, password, file_name):
        # 如果出现没有错误的toast，代表没有检验成功
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("password_error", "验证码错误") == None:
            print("最少需要输入 5 个字符")
            return True
        else:
            return False
    def register_succes(self):
        if self.register_h.get_register_text()==None:
            return True
        else:
            return False
if __name__ == '__main__':
    run=RegisterBusiness()
    run.login_email_error("fan1992169@163.com",'rfajsfks','666666','23453')