from util.read_ini import ReadIni
from selenium import webdriver
class FindElement():
    def __init__(self,driver):
        # self.driver=webdriver.Chrome()
        self.driver=driver
        self.read_ini=ReadIni()
    def get_element(self,key):
        data=self.read_ini.get_value(key)
        by=data.split(':')[0]
        value=data.split(':')[1]
        # print(by,value)
        try:
            if by=='id':
                return self.driver.find_element_by_id(value)
            elif by=='className':
                return self.driver.find_element_by_class_name(value)
            elif by=='xpath':
                return self.driver.find_element_by_xpath(value)
            elif by=='name':
                return self.driver.find_element_by_name(value)
        except:
            return None
if __name__ == '__main__':
    fin=FindElement()
    fin.get_element('user_name')