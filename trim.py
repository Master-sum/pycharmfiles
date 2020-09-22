"""
作者   ：bjx
创建时间   ：2020/8/24  11:04 下午 
文件名称   ：trim.PY
开发工具   ：PyCharm
"""
def trim(s):
    if s[:1] == ' ':
        s = s[1:]
    if s[-1:] == ' ':
        s = s[:-1]

    return len(s)
print(trim(" ncd "))
