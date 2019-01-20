from selenium import webdriver
from util.findelement import FindElement
import time
#二次封装webdriver
class ActionMethod:
    def __init__(self):
        pass
        # self.driver=webdriver.Chrome()
        # time.sleep(2)
        # self.driver.maximize_window()
    def open_browser(self,browser):
        if browser=='ie':
            self.driver = webdriver.Ie()
            self.driver.maximize_window()
        elif browser=='firebox':
            self.driver=webdriver.Firefox()
            self.driver.maximize_window()
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
    def get_url(self,url):
        self.driver.get(url)
    #获取元素
    def get_element(self,key):
        find_element=FindElement(self.driver)
        element=find_element.get_element(key)
        return element
    #输入元素
    def element_send_keys(self,value,key):
        #value和key的参数位置很重要，跟keyword_case里面的run_method相对应
        self.get_element(key).send_keys(value)
    #点击元素
    def click_element(self,key):
        self.get_element(key).click()
    #等待
    def sleep_time(self):
        time.sleep(2)
    #关闭浏览器
    def close_browser(self):
        self.driver.quit()
    #获取title
    def get_title(self):
        title=self.driver.title
        return title
if __name__ == '__main__':
    run=ActionMethod()
    run.close_browser()