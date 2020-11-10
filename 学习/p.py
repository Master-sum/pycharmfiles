"""
作者   ：bjx
创建时间   ：2020/11/9  4:39 下午 
文件名称   ：p.PY
开发工具   ：PyCharm
"""

#python实现，找出文件夹下所有图片文件。
import os
from pathlib import Path
#遍历
path = Path("路径")
#判断是否存在文件夹
try:
    path1 = path.resolve()
    for flie in os.listdir(path): #1
        # 判断
        if flie.endswith('jpg') or flie.endswith('png'):  # 2
            print(flie)
except Exception as e:
    print(e)

#