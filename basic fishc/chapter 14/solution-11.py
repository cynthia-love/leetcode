# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    异常处理
"""

# URLError, 当urlopen无法处理一个响应的时候
# 比如没有网络连接, 服务器连接失败, 找不到指定的服务器

from urllib import request
from urllib import error
try:
    res = request.urlopen("https://www.ajkfhafwkjqh.com")
    print(res)
except error.URLError as e:
    print(e)  # <urlopen error Tunnel connection failed: 503 Service Unavailable>


# HTTPError, 是URLError的子类, 可以这么理解, URLError是压根没收到回应
# 而HTTPError则是有响应, 只是这种响应不是正常的响应, 服务器告诉你有问题
# 由于HTTPError, 是URLError的子类, 写except的时候放URLError上面
"""
常见状态码:(100-299表示成功, 300-399表示重定向, python自动处理, 400-599表示出了问题, 需要我们自己处理)
100, 应当继续发送请求
101, 应当换一种协议
200, OK
201, Created, 服务器创建了一个新的资源, 其uri已经随location头信息返回
202, Accepted, 请求已接收, 但尚未开始处理

4xx, 客户端错误(即出错原因在发请求方, 或者说, 服务器能明确处理的各种错误)
400, bad request, 请求包含语法错误
403, 拒绝
404, 请求的资源在服务器上找不到

5xx, 服务器错误(服务器在处理请求的过程中有错误发生)
500, internal server error, 服务器遇到了一个未曾预料到的状况
502, bad gateway(网关从上游服务器收到无效响应)
503, service unavailable(由于维护等暂时无法处理请求)
504, gateway timeout(网关未在有效时间内从上游服务器拿到响应)

"""

try:
    res = request.urlopen("http://www.ajkfhafwkjqh.com")
    print(res)
except error.HTTPError as e:
    print(e)  # HTTP Error 503: Service Unavailable
    print(e.code)  # 503
    print(e.headers)
    print(e.read())  # 对于HTTPError, 服务器一般会对应返回一个错误页面, 所以HTTPError也是有read()等方法的
except error.URLError as e:
    print(e)