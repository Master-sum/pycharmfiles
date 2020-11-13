"""
作者   ：bjx
创建时间   ：2020/10/28  6:20 下午
文件名称   ：test_file.PY
开发工具   ：PyCharm
"""
#获取news.163.com的新闻标题并保存至Excel，结果发到171394733@qq.com上
import requests
import json
import pandas as pd
data1 = []
#从js文件中获取json数据，这里举个例子要闻的标题
for i in range(1,4):
    if i <=1:
       url = "https://temp.163.com/special/00804KVA/cm_yaowen20200213.js?callback=data_callback"
    else:
        url = "https://temp.163.com/special/00804KVA/cm_yaowen20200213_0{}.js?callback=data_callback".format(i)
    headers ={
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    response = requests.get(url= url,headers=headers)
    data = response.text
    print(data)
    data_new = data[14:-1]
    j = json.loads(data_new)
    for i in range(len(j)):
        t = j[i]
        title = t['title']
        data1.append(title)

print(data1)
title1 = ['标题']
#进行读取数据写入到csv
number = pd.DataFrame(columns=title1,data=data1)
number.to_csv("/Users/Documents/files/t1.csv")
