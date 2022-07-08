#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 读取Excel内容，实现文件驱动自动化执行
import openpyxl
# import pytest as pytest


def read_Excel():
    excel = openpyxl.load_workbook('./data/api_cases.xlsx')
    sheet = excel['Sheet1']
    list_tuple = []
    # 逐行读取Excel数据
    for value in sheet.values:
        # 判断当前行第一列的值，是否是数字编号
        if type(value[0]) is int:
            # 将元组装载进list
            list_tuple.append(value)
    return list_tuple

# @pytest.mark.parametrize('data',read_Excel())
# def test01(data):
#     print(data[0])
#     print(data[1])
#
# if __name__ == '__main__':
#     pytest.main(['-s','excel_read.py'])