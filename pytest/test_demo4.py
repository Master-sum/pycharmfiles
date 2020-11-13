"""
作者   ：bjx
创建时间   ：2020/10/29  8:33 下午 
文件名称   ：test_demo4.PY
开发工具   ：PyCharm
"""
import pytest


class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
