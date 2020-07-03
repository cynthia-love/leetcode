# -*- coding: utf-8 -*-

#  Author: Cynthia

"""
    有道翻译
    一般前端和后端交互用POST(只请求不交互用GET), 所以利用浏览器的审查元素-Network, 找到Method为Post的一般为接口
"""

"""
    分析Headers:
    
    1. General
    Remote Address: 10.10.10.54:8080, 服务器ip和端口, 未必是请求链接对应的ip, 还可能是代理服务器ip
    Request URL: http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule, 真正的请求链接
    Request Method: POST
    Status Code: 200 OK, 返回状态码
    Referrer Policy: no-referrer-when-downgrade, 当发生降级（比如从 https:// 跳转到 http:// ）时，不传递 Referrer 报头
    
    2. Request Headers
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8  # 上送的data必须符合的格式, 要urlencode
    Content-Length: 260
    Cookie: xxxxxxx
    Host: fanyi.youdao.com, 请求的域名
    Origin: http://fanyi.youdao.com
    Proxy-Connection: keep-alive
    Referer: http://fanyi.youdao.com/, 当用户在浏览器上点击一个链接时，会产生一个 HTTP 请求，用于获取新的页面内容，而在该请求的报头中，会包含一个 Referrer，用以指定该请求是从哪个页面跳转页来的，常被用于分析用户来源等信息
    User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36, 用于判断用户身份
    X-Requested-With: XMLHttpRequest
    (如果不手动改User-Agent, 会被定义为Python-urllib/3.x; 可以强制改以实现身份隐藏的作用)
    
    3. Query String Parameters
    smartresult=dict&smartresult=rule, 一般是直接以?附到http地址后面的参数
    
    4. Form Data, post请求的上送参数列表
    i: 小甲鱼, 待翻译内容
    from: AUTO
    to: AUTO, 自动识别源和目标语言
    smartresult: dict
    client: fanyideskweb
    salt: 15887557422418
    sign: e53569a92688535bece52fc99cedfadc
    ts: 1588755742241
    bv: 54005c0ddc47d3a4f8a58b098803c921
    doctype: json
    version: 2.1
    keyfrom: fanyi.web
    action: FY_BY_REALTlME
    
    5. Response Headers
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: application/json; charset=utf-8
    Date: Wed, 06 May 2020 09:02:22 GMT
    Server: nginx
    Transfer-Encoding: chunked
    Vary: Accept-Encoding
    X-Cache: MISS from netentsec-nps-10.10.10.54
    
    6. Response
    {
        "translateResult":[
            [{"tgt":"The little turtle","src":"小甲鱼"}]
        ],
        "errorCode":0,
        "type":
        "zh-CHS2en"
    }
"""
from urllib import request
from urllib import parse
import json

# urllib的网络请求函数不显示区分get和post, data为None就是get, 传了data就是post
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

content = input("请输入待翻译的内容(中/英): ")

data = {
    "i": content,
    "doctype": "json",
    "from": "AUTO",
    "to": "AUTO"
}

response = request.urlopen(url, parse.urlencode(data).encode("utf-8"))
html = response.read().decode("utf-8")
# 注意, 字符串在python内部是unicode编码, 如果要把返回的数据转成其他编码, 需要先用utf-8解码成字符串, 再encode成另一种编码

body = json.loads(html)
print("翻译结果为: {}".format(body["translateResult"][0][0]['tgt']))


