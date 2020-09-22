"""
作者   ：bjx
创建时间   ：2020/9/21  3:52 下午 
文件名称   ：爬取mzitu.PY
开发工具   ：PyCharm
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib,re,requests,time,threading,os
#请求头
headers ={
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "cookie":"Hm_lvt_cb7f29be3c304cd3bb0c65a4faa96c30=1600674669; Hm_lpvt_cb7f29be3c304cd3bb0c65a4faa96c30=1600685822; views=6",
    "Referer": "{}"

}
#获取图片URL
def get_url(num):
    dict_url = {}
    for j in range(1,num+1):
        time.sleep(2)
        try:
            start_url =  "https://www.mzitu.com/page/{}/".format(j)
            add = urllib.request.Request(url=start_url, headers=headers)
            html = urlopen(url=add, timeout=10)
            bs = BeautifulSoup(html.read(),'html.parser')
            #查找ul标签下的span的标签
            list_ul = bs.find('ul',id='pins').find_all('span')
            # list_ul = list(set(list_ul_more))
            p = re.compile(r'[\u4e00-\u9fa5+]')
            href_url = re.compile(r'https://www.mzitu.com/\d+')
            for i in range(len(list_ul)):
                text = re.findall(p,str(list_ul[i]))
                url = re.findall(href_url,str(list_ul[i]))
                result = ''.join(text)
                if len(url) != 0:
                    url = url[0]
                    key = result
                    value = url
                    dict_url[key] = value
        except ArithmeticError as e:
            print("w" + e)

    print(dict_url)
    return dict_url
#获取最大页码
def get_next_page():
    try:
        start_url = "https://www.mzitu.com"
        add = urllib.request.Request(url=start_url, headers=headers)
        html = urlopen(url=add, timeout=10)
        bs = BeautifulSoup(html.read(), 'html.parser')
        page_max = bs.find('div',class_ = 'nav-links').find_all('a')
        next_page = re.compile(r'https://www.mzitu.com/page/(\d+)')
        next_page_url = re.findall(next_page, str(page_max[-2]))
        return int(next_page_url[0])
    except ArithmeticError as e:
        print("w" + e)


#保存图片
def get_save_img(dict):
    print('解包字典:')
    for key, value in dict.items():
        #调用get_img_src(img_url)
        total_src = get_img_src(value)
        # 保存路径
        path = r"/Users/baijinxing/Documents/pycharmfiles/img"
        #创建文件夹
        os.makedirs(path+"/{}".format(key))
        #最终目录路径
        path_later = path+"/{}".format(key)

        for i in range(len(total_src)):
            print("*"*40)
            print(total_src[i])
            # 请求图片
            try:
                files = requests.get(total_src[i], headers=headers, timeout=20)
                # 利用上下文进行存储
                with open(path_later + "/{}_{}.jpg".format(key,i), 'wb') as f:
                    f.write(files.content)
                    print("保存成功")

                    f.close()
            except requests.HTTPError as f:
                print(f)

#获取图片的src
def get_img_src(img_url):

    total_src = []
    add = urllib.request.Request(url=img_url, headers=headers)
    html = urlopen(url=add, timeout=10)
    bs = BeautifulSoup(html.read(), 'html.parser')
    #获取图片张数
    page_num = bs.find('div',class_ = 'pagenavi').find_all('span')
    page_re = re.compile(r'<span>(\d+)</span>')
    page_max = re.findall(page_re,str(page_num))
    page_max_int = int(page_max[-1])
    for i in range(1,page_max_int+1):
        page_url_img = img_url + "/{}".format(i)
        headers1 = {
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "cookie": "Hm_lvt_cb7f29be3c304cd3bb0c65a4faa96c30=1600674669; Hm_lpvt_cb7f29be3c304cd3bb0c65a4faa96c30=1600685822; views=6",
            "Referer": "{}".format(page_url_img)

        }
        add1 = urllib.request.Request(url=page_url_img, headers=headers1)
        html1 = urlopen(url=add1, timeout=10)
        bs1 = BeautifulSoup(html1.read(), 'html.parser')
        #获取图片src
        img_src_text = bs1.find('div',class_ = 'main-image').find_all('img')
        img_re = re.compile(r'src=\"([^\"]*?)\"')
        img_src = re.findall(img_re,str(img_src_text))
        print(img_src[0])
        total_src.append(img_src[0])
    return total_src

    #引入多线程
a = get_next_page()
b = get_url(a)
time.sleep(3)
get_save_img(b)