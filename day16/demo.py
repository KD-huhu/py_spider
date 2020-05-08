import pytesseract
from PIL import Image

image = Image.open('code.png')
# image.show()
#将彩色图变成灰度图
image = image.convert('L')
# image.show()
#去除干扰线
threshold = 160
table = []
for i in range(256):
    if i <threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
# image.show()

#找到数据集
tesseract_data = '--tessdata-dir E:/Tesseract-OCR/tessdata'
image_str = pytesseract.image_to_string(image,config=tesseract_data)
print(image_str)