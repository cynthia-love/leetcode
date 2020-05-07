# -*- coding; utf-8 -*-
# Author: Cynthia

"""
    设置代理
"""


import json
import time
from urllib import request
from urllib import error
from urllib import parse

# 配置代理参数
proxy_handler = request.ProxyHandler({
    "http": "10.10.10.54:8080",
    "https": "10.10.10.54:8080"
})
# 根据代理参数构建url打开器
proxy_request = request.build_opener(proxy_handler)


url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# 头部基本是写死的
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    "Referer": "http://fanyi.youdao.com"
}

req = request.Request(url=url, headers=head)
# req.add_header("Referer", "http://fanyi.youdao.com")  # 不用在这里加, 在前面head那全都写了就行

# 报文体模板
body = {
    "i": "",
    "doctype": "json",
    "from": "AUTO",
    "to": "AUTO"
}

while True:
    body["i"] = "西瓜"

    try:
        # res = request.urlopen(req, data=parse.urlencode(body).encode("utf-8")).read().decode("utf-8")
        # url, data, 超时时间什么的基本和默认的request.urlopen都一样
        res = proxy_request.open(req, data=parse.urlencode(body).encode("utf-8")).read().decode("utf-8")

        res = json.loads(res)
        print(res)

    except (error.HTTPError, error.URLError) as e:
        print("请求失败: {}, 5s后继续尝试".format(e))

    except json.JSONDecodeError as e:
        print("JSON解析失败: {}".format(e))

    time.sleep(5)


