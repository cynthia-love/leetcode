# -*- coding: utf-8 -*-
# Author: Cynthia

"""
     爬取贴吧图片
"""
import os
import re
from os import path
from urllib import request
from urllib import parse
from urllib import error

"""
url = "https://tieba.baidu.com/p/6658627051"

res = request.urlopen(url, timeout=30).read()  # timeout单位秒

# 目标: <img class="BDE_Image" src="http://xxx/xxx.jpg" size="391900" changedsize="true" width="560" height="365">
# 要提取url, 名字, width, height
# 办法1, beautifulsoup
from bs4 import BeautifulSoup
bs = BeautifulSoup(res, "html.parser")
imgs = bs.find_all(attrs={"class": "BDE_Image"})

for tag in imgs:
    print(tag)
    print(tag["height"], tag["width"], tag["src"])
    url_pic = tag["src"]
    file_pic = "data/" + path.basename(tag["src"])

    res_pic = request.urlopen(url_pic).read()
    with open(file_pic, "wb") as f:
        f.write(res_pic)

"""
# 办法2, 正则, 不需要索引位置, 用findall就行, 不用finditer
# 另外, 由于findall不会返回整串只会返回子组, 想获取整串可以在最外面加括号
try:
    os.mkdir("data")
except FileExistsError:
    pass

url = "https://tieba.baidu.com/p/6658627051"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}
req = request.Request(url=url, headers=head)
res = request.urlopen(req).read().decode("utf-8")
# print(res)
# 对于这种大段正则匹配, 最难处理的是正则的贪婪非贪婪问题
# 注意这里的*, +后面的?, 表示非贪婪
# 另外, 注意这里的>, 不要写/>; (bs里打印的元素都带/, 那是处理过的, 不是原始网页返回的字符串)
imgs = re.findall(r'<img.*?class="BDE_Image".*?src="(.*?/([a-z0-9]+?.jpg))".*?>', res)
for item in imgs:
    print(item)
    req_pic = request.Request(url=item[0], headers=head)
    res_pic = request.urlopen(req_pic).read()
    with open("data/"+item[1]+".jpg", "wb") as f:
        f.write(res_pic)


