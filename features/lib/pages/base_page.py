from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self,driver):
        self.driver=driver
    def get_element(self,*loc):
        return self.driver.find_element(By.ID,*loc)
    #打开网页
    def get_url(self,url):
        self.driver.get(url)
    #获取title
    def get_title(self):
        title=self.driver.title
        return title