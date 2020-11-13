"""
作者   ：bjx
创建时间   ：2020/11/5  7:56 下午 
文件名称   ：pytest_file.PY
开发工具   ：PyCharm
"""
import pytest

@pytest.mark.webtest
def test_send_http():
    pass # perform some webtest test for your app

def test_something_quick():
    pass

def test_another():
    pass

class TestClass:
    def test_method(self):
        print("12121")

if __name__ == "__main__":
    pytest.main(["-s", "test_server.py", "-m=webtest"])
