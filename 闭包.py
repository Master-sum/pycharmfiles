"""
作者   ：bjx
创建时间   ：2020/9/19  4:26 下午 
文件名称   ：闭包.PY
开发工具   ：PyCharm
"""
# d = {'约炮女神阿朱露天片外流超大尺度狂野豪放': 'https://www.mzitu.com/248214', '午夜台球室的诱惑享受陆萱萱特殊服务': 'https://www.mzitu.com/248132'}
def te():
    d = {'约炮女神阿朱露天片外流超大尺度狂野豪放': 'https://www.mzitu.com/248214', '午夜台球室的诱惑享受陆萱萱特殊服务': 'https://www.mzitu.com/248132'}
    return d
# print("字典值 : %s" %  d.items())
def get_save_img(dict):
    # dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
    print('解包字典:')
    for key, value in dict.items():
        print(key + ':' + str(value))
t = te()
get_save_img(t)