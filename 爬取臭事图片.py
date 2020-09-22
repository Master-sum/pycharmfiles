"""
作者   ：bjx
创建时间   ：2020/9/18  11:07 上午 
文件名称   ：爬取臭事图片.PY
开发工具   ：PyCharm
"""
#爬取图片1、获取页面信息2、匹配图片连接3、保存图片
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import requests
from lxml import etree
import urllib.request,re
#请求头
headers ={
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
#获取图片url
def get_url():
    i = 1
    #创建一个list存放图片连接
    list_src = []
    list_url = []
    start_url = "https://www.qiushibaike.com/imgrank/"
    add = urllib.request.Request(url=start_url, headers=headers)
    html = urlopen(url=add,timeout=10)
    bs = BeautifulSoup(html.read(), 'html.parser')
    page = bs.find_all(class_=re.compile("next"))
    page = page[0]
    #if page.text is not None:
    for i in range(1,14):
        one_url = "https://www.qiushibaike.com/imgrank"+"/page/{}/".format(i)
        add1 = urllib.request.Request(url=one_url, headers=headers)
        html1 = urlopen(url=add1, timeout=10)
        bs1 = BeautifulSoup(html1.read(), 'html.parser')
        page1 = bs1.find_all("img",src=re.compile(r"//(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"))
        for i in range(len(page1)):
            c_url = page1[i]
            clear_url = "https:"+str(c_url['src'])
            list_src.append(clear_url)
            print(list_src)
        list_url+=page1

    else:
        print("总共%d"%len(list_src))
    #获取总共的页面数
    print(set(list_src))
    #对列表进行去重
    list_src = list(set(list_src))
    #返回list
    return list_src




#下载图片
def download(list_src):
    #保存路径
    path = r"/Users/baijinxing/Documents/pycharmfiles/img"

    for i in range(len(list_src)):
        # 请求图片
        files = requests.get(list_src[i], headers=headers, timeout=20)
        #利用上下文进行存储
        with open(path+"/{}.jpg".format(i),'wb') as f:
            f.write(files.content)

    f.close()




if __name__ == "__main__":
    url = get_url()
    download(url)