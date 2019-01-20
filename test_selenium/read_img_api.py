from util.ShowapiRequest import ShowapiRequest
from PIL import Image
im=Image.open("D:/sheshui/0.png")
# image=im.resize((1024,760))
# image.save("D:/imooc1.png")
r = ShowapiRequest("http://www.5itest.cn/register","62626","d61950be50dc4dbd9969f741b8e730f5" )
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"D:/sheshui/0.png") #文件上传时设置
res = r.post()
print(res.text) # 返回信息