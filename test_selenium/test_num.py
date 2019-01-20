import pytesseract
from PIL import Image
img_code = Image.open("D:/sheshui/0.png")
text = pytesseract.image_to_string(img_code)
# text=pytesseract.image_to_string(image ,lang='chi_sim')
# text = pytesseract.image_to_string(img_code)
print(text)