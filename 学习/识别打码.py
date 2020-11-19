"""
作者   ：bjx
创建时间   ：2020/11/19  11:37 下午 
文件名称   ：识别打码.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import pytesseract
from PIL import Image
image = Image.open(r'/Users/baijinxing/Documents/public_files/timg.jpeg')
text = pytesseract.image_to_string(image)
print(text)