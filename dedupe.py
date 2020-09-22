"""
作者   ：bjx
创建时间   ：2020/9/7  12:11 上午 
文件名称   ：dedupe.PY
开发工具   ：PyCharm
"""
#怎样在一个序列上面保持元素顺序的同时消除重复的值？
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            # yield item
            seen.add(item)
    print(seen)

items =  [1, 5, 2, 1, 9, 1, 5, 10]
dedupe(items)
#针对字典上去重
def dedict(items,key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        print(key(item))
        if val not in seen:
            seen.add(val)
    print(seen)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
dedict(a, key=lambda d: (d['x'],d['y']))