# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    修改User-Agent
    request.urlopen()第一个参数既可以是url, 也可是Request对象
    由于urlopen没有head参数, 要想添加head, 只能用方式2
"""

from urllib import request
from urllib import parse
from urllib import error
import json

content = input("请输入待翻译的内容: ")

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}
# 通过UA只能一定程度上隐藏身份, 为了避免服务器直接封禁IP, 可以选择延迟提交时间或者直接使用代理

body = {
    "i": content,
    "doctype": "json",
    "from": "AUTO",
    "to": "AUTO"
}

# 注意data才需要urlencode和encode, headers不需要
req = request.Request(url=url, data=parse.urlencode(body).encode("utf-8"), headers=head)
req.add_header("Referer", "http://fanyi.youdao.com")  # header也可以这么动态加

try:

    res = request.urlopen(req).read().decode("utf-8")

    res = json.loads(res)

    print("翻译结果为: {}".format(res["translateResult"][0][0]['tgt']))

except (error.HTTPError, error.URLError) as e:
    print("请求失败", e)


