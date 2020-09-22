"""
作者   ：bjx
创建时间   ：2020/9/17  7:48 下午 
文件名称   ：boss_selenium.PY
开发工具   ：PyCharm
"""
#利用selenium进行爬取boss方案一
from selenium import webdriver#导入库
import time
path = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(path)#声明浏览器
url = 'https://www.zhipin.com/'
browser.get(url)#打开浏览器预设网址
input = browser.find_element_by_class_name("ipt-search")
input.send_keys("python")
time.sleep(2)
input.clear()
button = browser.find_element_by_class_name("btn btn-search")
button.click()
print(browser.page_source)#打印网页源代码


