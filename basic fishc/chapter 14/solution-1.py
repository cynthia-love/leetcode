# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    第14章 论一只爬虫的自我修养
"""
"""
    入门
    urllib模块主要分为四部分
    1. urllib.request, 最主要的, 包含对服务器请求的发出, 跳转, 代理, 安全等
    2. urllib.error, 异常处理
    3. urllib.parse, 解析
    4. urllib.robotparser, 解析robots.txt
"""
"""
    编码解疑: 
    ASCII, 8位, 存字母数字够
    GB 2312 等, 由于ASCII无法满足需求, 中国自己搞得
    Unicode, 创建一个足够大的编码, 将所有国家的编码都加进来
    UTF-8, Unicode的一种, 可变长, 根据文本内容选用不同的长度, 比如只有英文, 那8位, 有中文, 虽然还是叫UTF-8, 但实际16位
    
"""

import urllib.request as ur

response = ur.urlopen(url="http://www.fishc.com")

html = response.read().decode("utf-8")

print(html)
