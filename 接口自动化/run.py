import time
import xlrd
import requests
import json
from xlutils.copy import copy
import os
"""
1、读取Excel数据
2、读取测试用例直到最后一个测试用例的数据
①、读取url，data数据
②、判断接口方法（get，post）
③、根据②请求接口并传参
④、获取数据并判断A的值是否等于B
是:测试用例通过，在result写入Pass
否:测试用例不通过，在result写入Error
⑤、保存文件并以时间为文件名

"""
class excel_operation():

    def excel_read(self):
        data_table = xlrd.open_workbook("request_case.xls")
        table_number = 0
        try:
            table = data_table.sheets()[table_number]
        except:
            print("table_number填写数据错误")
        nrows = table.nrows  # 获取行数
        ncols = table.ncols  # 获取列数

        data_value = table.row_values(0)#获取第一行的标题
        case_id = data_value.index('case_id')
        title = data_value.index('title')
        url = data_value.index('url')
        data = data_value.index('data')
        method = data_value.index('method')
        judge = data_value.index('judge')
        value = data_value.index('value')
        result = data_value.index('result')

        for i in range(1,nrows):#从第一个用例开始执行到最后一个用例
            case = table.row_values(i)#第一个开始到最后一个用例的数据
            if case[method] == 'post':
                if case[data] != 'None':
                    case_data = json.loads(case[data])#将文件data数据改为list类型
                    try:
                        request = requests.post(url=case[url], data=case_data)

                        if request.json()[case[judge]] == bool(case[value]):
                            print("第", i, "条测试用例通过")
                            excel_operation.excel_write(x=i, y=result)
                        else:
                            print("第", i, "条测试用例失败")
                            excel_operation.excel_write(x=i, y=result, result_txt='Error')
                    except:
                        print("第", i, "条测试用例请求失败！！！")

                elif case[data] == 'None':
                        excel_operation.excel_write(x=i, y=result, result_txt='Skip')
                else:
                    print("警告：运行接口测试用例停止，请检查原因！！！")

            elif case[method] == 'get':
                try:
                    r = requests.get(url=case[url], data=case[data])

                    if r.status_code == case[judge]:
                        print("第", i, "条测试用例通过")
                        excel_operation.excel_write(x=i, y=result)
                    else:
                        print("第", i, "条测试用例失败")
                        excel_operation.excel_write(x=i, y=result, result_txt='Error')
                except:
                    print("第",i,"条测试用例请求失败！！！")
            else:
                print("警告：运行接口测试用例停止，请检查原因！！！")

    def excel_write(x=0, y=0,result_txt='Pass'):
        """
        :param x:文件行数
        :param y:文件列数
        :result_txt:写入单元格的文本
        :return:
        """
        now = time.strftime("%Y-%m-%d")#获取当前日期
        test_case_ = os.path.dirname(os.path.realpath('run.py'))#找到runall.py所在路径
        test_report = os.path.join(test_case_, "reports")  # 测试报告所在路径
        path_name = test_report+ "\\" + now + '-request_case.xls'#测试报告保存的路径
        pata_Once = test_case_ + '\\request_case.xls'

        read_excel = xlrd.open_workbook("request_case.xls")
        workbook = copy(read_excel)
        sheet = workbook.get_sheet(0)#获取第几个表的数据
        sheet.write(x, y, result_txt)#在X行Y列写入文本
        try:
            workbook.save(pata_Once)
            workbook.save(path_name)
        except:
            print("警告：出现错误！！！请排查原因！！！")


if __name__ == '__main__':
    excel_operation().excel_read()
