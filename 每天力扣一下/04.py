"""
作者   ：bjx
创建时间   ：2020/11/13  11:59 上午 
文件名称   ：04.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
st = "abcabcbb"
L = []
def add(st):
    if len(st)>1:
        l = ''
        j = 0
        for i in st:
          if i not in l:
                l += i
                j += 1
          else:
             L.append(l)
             print(j)
             st = st[j:]
             add(st)
    else:
        return 0

add(st)
num_l = list(set(L))
print(num_l)
data = num_l[:-1]

print("最大子串{}长度{}".format(max(data),len(max(data))))