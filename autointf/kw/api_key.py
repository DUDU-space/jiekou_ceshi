#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    接口关键字驱动类，用于提供自动化接口测试的关键字方法
"""
import json
import jsonpath
import requests

class Apikey:
    # 基于jsonpath获取数据的关键字，用于提取所需要的内容
    def get_text(self,data,key):
        # loads将json格式的内容转换为字典格式
        # dumps将字典格式的内容转换为json格式
        dict_data = json.loads(data)
        value_list = jsonpath.jsonpath(dict_data,key)
        return value_list[0]

    # get请求的封装
    def get(self,url,params=None,**kwargs):
        return requests.get(url=url,params=params,**kwargs)

    # post请求的封装
    def post(self,**kwargs):
        return requests.post(**kwargs)

if __name__ == '__main__':
    # 实例化对象
    ak1 = Apikey()
    url = 'http://39.98.138.157:5000/api/login'

    # 接口请求的参数
    data = {
        "password": "123456",
        "username": "admin"
    }
    res = ak1.post(url=url,json=data)
    print(res.text)
