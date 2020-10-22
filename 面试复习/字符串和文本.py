"""
作者   ：bjx
创建时间   ：2020/10/22  3:27 下午 
文件名称   ：字符串和文本.PY
开发工具   ：PyCharm
"""
"""
#分隔符拆分
import re
lin = 'aabhba xnsnxjs nxsnsjn,xbsbxs;xsxs  s'
str1 = re.split(r'[;,\s]\s*',lin)#匹配；，空白
print(str1)#['aabhba', 'xnsnxjs', 'nxsnsjn', 'xbsbxs', 'xsxs', 's']
#检查文件拓展名startswith,endswith
#不区分大小写查询，替换
text = "tetpython PYTHONhell PYthonhi"
new_text = re.findall('python',text,re.IGNORECASE)#不区分大小写查找
print(new_text)#['python', 'PYTHON', 'PYthon']
new_sub = re.sub('python','hello',text,re.IGNORECASE)#不区分大小写替换
print(new_sub)#tethello PYTHONhell PYthonhi
s = text.replace('hell','hello')#旧的替换新的
print(s)#tetpython PYTHONhello PYthonhi
#文本对齐ljust(),rjust(),center()
text1 = 'hello world'
l = text1.rjust(20,'=')#20个字符其他用=表示
print(l)#=========hello world
"""
#格式化%d %s {}.format()
s ="cdmcdk{}".format('s')
print(s)
class info:
    def __init__(self,name,n):
        self.name = name
        self.n = n
a = info('ss',11)
s1 = "cdcd{name}wdw{n}".format_map(vars(a))
s_new = "cdcd{name}wdw{n}".format(name='ss',n = 11)
print(s_new)
print(s1)
#当n为空时format_map和format不能使用,需要重写__missing__
class sub1(dict):
    def __missing__(self, key):
        return '{'+key+'}'
sub1(name='www')
s1_new = "cdcd{name}wdw{n}".format_map(sub1(vars()))
print(s1_new)