"""
作者   ：bjx
创建时间   ：2020/11/3  2:17 下午 
文件名称   ：字母异位词分组.PY
开发工具   ：PyCharm
"""
'''
lst =  ["eat", "tea", "tan", "ate", "nat", "bat"]
dct = {}
for i in lst:
	key = str(sorted(i))#将每一个字母进行拆分，形成一个list
	if key not in dct.keys():
		dct[key] = [i]
	else:
		dct[key].append(i)
print(dct)
res = [val for val in dct.values()]
print(res)
'''



lst =  ["eat", "tea", "tan", "ate", "nat", "bat"]
dct = {}
for word in lst:
	key = ''.join(sorted(word))
	# 注意get的用法，第二个参数表示key不存在时的默认值
	dct[key] = dct.get(key,[]) + [word]
res = [val for val in dct.values()]
print(res)