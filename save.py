import requests
headers ={
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}
try:
    i = requests.get("http://imgg.xinfutv.com/2019/01/18/1.jpg", headers=headers, timeout=20)
    print("222")
    print(i.status_code)
    with open(r"/Users/baijinxing/Documents/pycharmfiles/1.jpg", 'wb') as f:

        f.write(i.content)
        f.close()
except requests.HTTPError as f:
    print(f)