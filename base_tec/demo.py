#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jsonpath as jsonpath
import requests
# 接口请求的模拟

# 接口的地址
url = 'http://39.98.138.157:5000/api/login'

# 接口请求的参数
data = {
    "password":"123456",
    "username":"admin"
}

# 接口请求
response = requests.post(url=url,json=data)

# 输出响应结果
print(response.text)
# 返回的是一个json，json是一种特殊的字符串类型
print(type(response.text))

# 结果检查（断言），返回dict字典类型的结果
print(response.json())
print(type(response.json()))
result = response.json()
msg_value = result['msg']
print(msg_value)

assert "success" == msg_value
# 嵌套字典，{key:{key:value, key:{key:value}}}
name_value = response.json()['info']['name']
print(name_value)

# jsonpath库，简化取值操作
# jsonpath获取数据的表达式：成功则返回list,失败则返回false
# jsonpath接收的必须是dict类型的数据
# value = jsonpath.jsonpath(response.json(),'$.adress.city')
value = jsonpath.jsonpath(response.json(),'$..city')
print(value)
a = value[0]
print(a)

