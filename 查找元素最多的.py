"""
作者   ：bjx
创建时间   ：2020/9/7  12:39 上午 
文件名称   ：查找元素最多的.PY
开发工具   ：PyCharm
"""
#怎样找出一个序列中出现次数最多的元素呢？
#1、简单的遍历全部
def s_list(words):
    item = {}

    word = set(words)
    word = list(word)
    print(word)
    for i in range(len(word)):
        sum = 0
        for j in range(len(words)):
            if word[i] == words[j]:
                sum += 1
        #此处是将key与value当成键值对插入中item
        key = word[i]
        value = sum
        item[key] = value
    print(item)

    max_value = max(zip(item.values(),item.keys()))
    print(max_value)


words = [ 'look', 'into', 'my', 'eyes', 'look', 'into',\
          'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the',\
          'eyes', 'not', 'around', 'the', 'eyes', "don't", \
          'look', 'around', 'the', 'eyes', 'look', 'into', \
          'my', 'eyes', "you're", 'under' ]
s_list(words)