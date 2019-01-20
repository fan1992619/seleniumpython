from features.lib.pages.base_page import BasePage
from  selenium.webdriver.common.by import By
class RegisterPage(BasePage):
    def __init__(self,context):
        super(RegisterPage,self).__init__(context.driver)
    def send_useremail(self,useremail):
        self.driver.find_element(By.ID,"register_email").send_keys(useremail)
    def send_username(self,username):
        self.driver.find_element(By.ID,"register_nickname").send_keys(username)
    def send_password(self,password):
        self.driver.find_element(By.ID,"register_password").send_keys(password)
    def send_code(self,code):
        self.driver.find_element(By.ID,"captcha_code").send_keys(code)
    def click_register_button(self):
        self.driver.find_element(By.ID,"register-btn").click()
    def get_code_text(self,codetext):
        return self.driver.find_element(By.ID,"captcha_code-error").text