from PIL import Image
import pytesseract
from selenium import webdriver
from util.ShowapiRequest import  ShowapiRequest
import time
from selenium.common.exceptions import NoSuchElementException
class GetCode:
    def __init__(self,driver):
        # self.driver=webdriver.Chrome()
        # self.driver.get("http://www.5itest.cn/register")
        # self.driver.maximize_window()
        # time.sleep(3)
        self.driver = driver
    #使用pytesseract去获取图片里面的验证码
    def get_text(self,file_name):
        self.get_code_image(file_name)
        img_code = Image.open(file_name)
        time.sleep(2)
        text = pytesseract.image_to_string(img_code)
        print(text)
        time.sleep(2)
        return text
    def get_code_image(self,file_name):
        # 点击换一个
        self.driver.find_element_by_id("getcode_num").click()
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))
        #一定要根据电脑分辨率来设置剪切后的图片，不然识别不出来
        img_res=img.resize((1366,768))
        img_res.save(file_name)
        time.sleep(2)
    #解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name) #文件上传时设置
        res = r.post()
        time.sleep(1)
        text = res.json()['showapi_res_body']
        # print(text)
        code = text['Result']
        print(code)
        time.sleep(2)
        return code
    def login_pass(self):
        file_name="D:/sheshui/0.png"
        num = "01552513"
        num = int(num)
        for nums in range(num,num+200,1):
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[1]/td[2]/input").clear()
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[2]/td[2]/input").clear()
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[3]/td[2]/input").clear()
            # 验证码
            text=self.get_text(file_name)
            # print(type(text))
            code=self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[3]/td[2]/input")
            code.click()
            time.sleep(2)
            code.send_keys(text)
            time.sleep(1)
            # 流水号
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[1]/td[2]/input").send_keys(nums)
            # print("第%d次的流水号" % nums)
            # 密码
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[2]/td[2]/input").send_keys("199261")
            # 提交
            code.click()
            self.driver.find_element_by_xpath("//*[@id='mytable']/tbody/tr[4]/td[2]/button").click()
            time.sleep(1)
            c="//*[@id='mytable']/tbody/tr[4]/td[1]"
            if self.source_element(c):
                print("流水号为：{}".format(nums),"验证码为：".format(text))
                break
            else:
                # self.driver.refresh()
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
    run=GetCode()
    run.code_online("../image/imooc.png")