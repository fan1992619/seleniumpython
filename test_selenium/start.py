from selenium import webdriver
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
# EC.visibility_of_element_located 判断传入的元素是否可见
driver=webdriver.Ie()
driver.get("http://www.bjsat.gov.cn/bjsat/office/jsp/ssjb/query.jsp")
time.sleep(3)
#窗口最大化
driver.maximize_window()
print(EC.title_contains("注册"))
element=driver.find_element_by_class_name("controls")
loctor=(By.CLASS_NAME,"controls")
WebDriverWait(driver,1).until(EC.visibility_of_element_located(loctor))
email_element=driver.find_element_by_id("register_email")
print(email_element.get_attribute("placeholder"))
email_element.send_keys("fan192619@163.com")
print(email_element.get_attribute("value"))
driver.find_element_by_id("register_nickname").send_keys("fan1992619")
driver.find_element_by_id("register_password").send_keys("111111")
#保存打开网页的全部图片
driver.save_screenshot("D:/imooc.png")
#定位到该图片的id
code_element=driver.find_element_by_id("getcode_num")
code_element.click()
time.sleep(2)
# code_element.location拿到该图片的左上角的坐标值
left=code_element.location['x']
top=code_element.location['y']
right=code_element.size['width']+left
height=code_element.size['height']+top
ig=Image.open("D:/imooc.png")
#crop()需要带一个或者两个参数，所以要用两个括号，不然用一个括号会被识别为4个参数
img=ig.crop((left,top,right,height))
img.save("D:/imooc1.png")
driver.find_element_by_id("captcha_code").send_keys("5621")
driver.find_element_by_id("register-btn").click()
driver.quit()