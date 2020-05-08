from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open(r'1.jpg'))
print(text)