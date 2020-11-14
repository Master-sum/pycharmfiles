"""
作者   ：bjx
创建时间   ：2020/11/13  11:38 下午 
文件名称   ：06.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
'''
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
输入: "cbbd"
输出: "bb"
'''
#使用两个指针，第一个指针确定第一个位置，第二个指针就扫描之后的子串
string = input("输入:")
#转换list方便比较
s_l = list(string)
#两个for循环进行定位操作
for i in range(len(string)):
    for j in range(i,len(string)):
        #判断这两个值相等，但是位置不相等
        if s_l[i] == s_l[j] and i != j:
            print(string[i:j+1])
        else:
            continue