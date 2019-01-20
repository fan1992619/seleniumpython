from selenium import webdriver
from util.findelement import FindElement
from util.ShowapiRequest import ShowapiRequest
import time
import random
from PIL import Image
class ResgisterFunction():
    def __init__(self,url,i):
        self.driver=self.get_driver(url,i)
        self.find_element=FindElement(self.driver)
    #获取driver，并且打开URL
    def get_driver(self,url,i):
        if i==0:
            driver=webdriver.Chrome()
        elif i==1:
            driver=webdriver.Firefox()
        else:
            driver=webdriver.Ie()
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
        return driver
    #输入用户信息，根据key输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)
    #定位用户信息获取element，传一个key得到平配置文件的by和value的值，并返回元素定位
    def get_user_element(self,key):
        user_element=self.find_element.get_element(key)
        return user_element
    #获取用户名或者邮箱的随机数
    def get_rang_user(self):
        user_info = "".join(random.sample("123456789addft", 6))
        return user_info
    #保存并截取图片
    def get_code_image(self,file_name):
        # 保存打开网页的全部图片
        self.driver.save_screenshot(file_name)
        # 根据配置文件里面的信息定位验证码图片的位置ID
        code_element = self.get_user_element("code_image")
        code_element.click()
        time.sleep(2)
        # code_element.location拿到该图片的左上角的坐标值
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        ig = Image.open(file_name)
        # crop()需要带一个或者两个参数，所以要用两个括号，不然用一个括号会被识别为4个参数
        img = ig.crop((left, top, right, height))
        img.save(file_name)
    #获取图片上面的验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-5", "62626", "d61950be50dc4dbd9969f741b8e730f5")
        r.addBodyPara("img_base64", "")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        print(res.text)
    def main(self):
        user_name_info = self.get_rang_user()
        user_email = user_name_info + "@163.com"
        file_name = "D:\imooc1.png"
        code_text=self.code_online(file_name)
        #以下是根据配置文件输入用户信息
        self.send_user_info("user_email",user_email)
        self.send_user_info("user_name",user_name_info)
        self.send_user_info("password","111111")
        try:
            self.send_user_info("code_text",code_text)
        except:
            self.send_user_info("code_text","52sgh")
            self.driver.save_screenshot("D:\错误的{0}.png".format(self.get_rang_user))
        self.get_user_element("register_button").click()
        time.sleep(3)
        self.driver.quit()
if __name__ == '__main__':
    #通过使用循环来启动不同的浏览器
    for i in range(3):
        run=ResgisterFunction("http://www.5itest.cn/register",i)
        run.main()