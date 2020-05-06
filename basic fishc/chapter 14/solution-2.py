# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    下载一张图片
"""

from urllib import request
from urllib.error import URLError

try:
    response = request.urlopen("http://placekitten.com/g/200/300")
    print(response.geturl())  # 返回请求的url
    print(response.getcode())  # HTTP状态码
    print(response.info())  # 各种头部信息

    # 把返回的二进制流存成图片
    with open("data/cat.jpg", "wb") as f:
        f.write(response.read())

except URLError as e:
    print(e)