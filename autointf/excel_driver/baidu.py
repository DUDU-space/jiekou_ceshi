#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
url = 'https://www.baidu.com'
content = input('请输入您想查询的词：')
param = {
    'wd': content,
    'pn': 0
}
response = requests.get(url=url,params=param)
ctx = response.content
b = response.status_code

print(ctx)
print(b)