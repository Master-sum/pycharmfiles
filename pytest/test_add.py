"""
作者   ：bjx
创建时间   ：2020/10/29  11:46 上午 
文件名称   ：test_add.PY
开发工具   ：PyCharm
"""

# file_name: test_add.py
#!/usr/bin/env python
# coding=utf-8
import pytest
#!/usr/bin/env python
# coding=utf-8
import pytest
class TestDemo1:
    # 定义参数列表
    list_a = [1, 2, 3]

    # 定义固件名is_success，并设置返回值
    @pytest.fixture(params=list_a)
    def is_success(self, request):
        return request.param

    # 在测试方法中传入固件名
    @pytest.mark.success
    def test_success(self, is_success):
        assert is_success == 1