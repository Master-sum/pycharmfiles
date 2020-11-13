"""
作者   ：bjx
创建时间   ：2020/11/6  12:23 上午 
文件名称   ：test_file.PY
开发工具   ：PyCharm
"""
#模块级别的初始化清除
def setup_module():
    print("————初始化模块————")

def teardown_module():
    print("————清除模块")

class Test:
    @classmethod
    def setup_class(cls):
        print("————初始化类————")
    @classmethod
    def teardown_class(cls):
        print("————清除类")
    def test_01(self):
        print("111")

    def test_02(self):
        print("111")

