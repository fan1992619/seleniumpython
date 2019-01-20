from selenium import webdriver
import random
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time
driver=webdriver.Chrome()
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep()
def get_element(id):
    element=driver.find_element_by_id(id)
    return element
def get_rang_user():
    user_info="".join(random.sample("123456789addft","6"))
    return user_info
def get_code_image(file_name):
    #保存打开网页的全部图片
    driver.save_screenshot("file_name")
    # 定位到该图片的id
    code_element = driver.find_element_by_id("getcode_num")
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
    img.save("file_name")
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-5", "62626", "d61950be50dc4dbd9969f741b8e730f5")
    r.addBodyPara("img_base64", "")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", file_name)  # 文件上传时设置
    res = r.post()
    print(res.text)
def run_main():
    user_name_info = get_rang_user()
    user_email = user_name_info+"@163.com"
    file_name = "D:/imooctest.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    driver.quit()
run_main()