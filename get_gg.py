import requests
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
headers ={
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}
def get(url):

    #解析URL
    try:
     html = urlopen(url)
    except HTTPError as e:
        print(e)
     #解析网页
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        page = bs.find_all('a', href=re.compile(r"(\d+.html)"))

        b = []
        for i in page:
            print(str(i))
            a = re.compile(r"href=.(\S+).html")
            t = a.findall(str(i))
            b.append(t[0])


        print(11)
    except ArithmeticError as e:
        print(e)
    #返回所有的URL
    b = set(b)
    print(b)
    return b
def one_url(b):
    #获取所有图片的URL
    t = 0
    #遍历所有的URL
    for i in b:
        u = i+".html/"
        t = t+1
        print(t)
        try:
            html = urlopen(u)
            bs = BeautifulSoup(html.read(),'html.parser')
            page_all = bs.find_all(class_ = 'pagelist')
            print(page_all)
            #list转换str
            page_str = ''.join('%s' %id for id in page_all)
            print(page_str)
            #正则匹配出页数
            page = re.compile(r"https://www.taotuxp.com/\d+.html/(\d+)")
            page_date = page.findall(page_str)
            print(page_date)
            page_list = len(page_date)+1
            print(page_list)
            for j in range(1,page_list):
                print("进入for")
                url = "{}{}".format(u,j)
                print(url)
                html = urlopen(url)
                bs = BeautifulSoup(html.read(),'html.parser')
                img_list = bs.find_all(id = 'post_content')
                print(img_list)
                img_str = ''.join('%s' % id for id in img_list)
                print(img_str)
                # 正则匹配出页数
                img = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', img_str)
                for k in range(len(img)):

                    #保存照片
                    try:
                        i = requests.get(img[k], headers=headers, timeout=20)
                        print("222")
                        print(i.status_code)
                        with open(r"/Users/baijinxing/Documents/pycharmfiles/img/{}{}{}.jpg".format(t,j,k), 'wb') as f:

                            f.write(i.content)
                            f.close()
                    except requests.HTTPError as f:
                        print(f)

        except ArithmeticError as e:
            print("w"+e)




if __name__ == "__main__":
    url = "https://www.taotuxp.com/"
    one = get(url)
    one_url(one)
