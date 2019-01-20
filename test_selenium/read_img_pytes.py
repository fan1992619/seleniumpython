from PIL import Image
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from util.get_code import GetCode
class Sheshui():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.bjsat.gov.cn/bjsat/office/jsp/ssjb/query.jsp")
        time.sleep(5)
        self.driver.maximize_window()
    def open_url(self,file_name):
        # 点击换一个
        self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[3]/td[2]/a").click()
        # 保存打开网页的全部图片
        self.driver.save_screenshot(file_name)
        # 定位到该图片的id
        code_element = self.driver.find_element_by_id("safecode")
        code_element.click()
        time.sleep(2)
        # code_element.location拿到该图片的左上角的坐标值
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        ig = Image.open("file_name")
        # crop()需要带一个或者两个参数，所以要用两个括号，不然用一个括号会被识别为4个参数
        img = ig.crop((left, top, right, height))
        img_size = img.resize((1366, 768))
        img_size.save("file_name")
    def login_pass(self):
        file_name="D:/sheshui/0.png"
        getcode=GetCode(self.driver)
        num = "01552490"
        num = int(num)
        for nums in range(num,num+200,1):
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[1]/td[2]/input").clear()
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[2]/td[2]/input").clear()
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[3]/td[2]/input").clear()
            # 点击换一个
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[3]/td[2]/a").click()
            # 验证码
            text = getcode.code_online(file_name)
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[3]/td[2]/input").send_keys(text)
            # 流水号
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[1]/td[2]/input").send_keys(nums)
            print("第%d次的流水号" % nums)
            # 密码
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[2]/td[2]/input").send_keys("199261")
            # 提交
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[4]/td[2]/button").click()
            time.sleep(2)
            c="//*[@id='mytable']/tbody/tr[4]/td[1]"
            if self.source_element(c):
                print("流水号为：{}".format(nums),"验证码为：".format(text))
                break
            else:
                continue
            num = num + 1
    def source_element(self,c):
        try:
            flag_source=None
            #flag_source一定要放在里层先定义，不然会报错“local variable 'flag_source' referenced before assignment”,因为后面的判断接收不到该判断
            source=self.driver.page_source
            if c in source:
                return True
        except(NoSuchElementException):
            flag_source=False
        finally:
            return flag_source
if __name__ == '__main__':
    run=Sheshui()
    run.login_pass()
