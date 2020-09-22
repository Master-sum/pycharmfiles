import requests
from bs4 import BeautifulSoup
#将session存储起来以便访问网页
session = requests.Session()

#登陆用户名、密码

params = {'fm-login-id':'13225926431','fm-login-password':'Bjx7948640'}

#携带密码进行登陆网站
s = session.post("https://login.taobao.com/member/login.jhtml",params)
#获取cookie
cookie_all = s.cookies.get_dict()

print(s)
print(cookie_all)

responce = requests.get("https://login.taobao.com/member/login.jhtml")
print(responce)

