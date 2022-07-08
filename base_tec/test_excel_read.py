#!/usr/bin/env python
# -*- coding: utf-8 -*-
import openpyxl

excel = openpyxl.load_workbook('../autointf/data/api_cases.xlsx')
sheet = excel['Sheet1']
print(sheet)
print(sheet.values)

n = 0
# 读取excel内容，实现文件驱动自动化执行
# 逐行循环读取Excel数据
for value in sheet.values:
    n = n + 1
    print(n)