"""
作者   ：bjx
创建时间   ：2020/11/10  5:31 下午 
文件名称   ：mumu.PY
开发工具   ：PyCharm
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from appium import webdriver

disired_caps = {
  "platformName": "Android",
  "deviceName": "emulator-5554",
  "appPackage": "com.taobao.taobao",
  "appActivity": "com.taobao.tao.TBMainActivity",
  "noReset":True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",disired_caps)
driver.implicitly_wait(5)
time.sleep(5)
driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='芭芭农场']").click()
time.sleep(15)
print("122233")

driver.tap([(0,62),(1170,1872)],500)
print("1222")
