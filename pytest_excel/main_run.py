#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import os

if __name__ == '__main__':
    # 生成报告的数据源
    pytest.main(['./case/test_Excel.py','--alluredir','./result','--clean-alluredir'])
    # 基于数据源去生成报告
    os.system('allure serve result')