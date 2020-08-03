# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Beautiful Soup
    一个专门用于处理html或xml格式文件的库
"""
import re
from urllib import request
from urllib import error
from bs4 import BeautifulSoup

url = "http://baike.baidu.com/view/284853.html"

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    "Referer": "http://www.baidu.com"
}

req = request.Request(url=url, headers=head)

try:

    res = request.urlopen(req).read()

    # 参数1为待分析文件(html/xml), 参数2为指定解析器
    soup = BeautifulSoup(res, "html.parser")

    # 读取所有包含关键字view的链接
    # 可以根据属性去找, href=xxx, xxx可以是完整字符串, 也可以是正则, 注意是正则的时候不包括外边的双引号""
    # soup.find_all(href=re.compile(r".*view.*")); 首参数还可以是方法; 注意是方法的时候参数是标签对象
    # 这里只能用x.has_attr("href")判断属性是否存在, 不能用python自带的 in 什么的; 标签属性访问这块什么时候.什么时候[]有点迷
    # python里对象的attr是用.访问的, 对应__getattribute__, __setattr__等; 容器里的元素才是用[]访问, 对应__getitem__
    # 而这里, 标签的属性attr是用[]访问, 对应has_attr等; 标签里的子标签却反而是用.访问的.children
    for each in soup.find_all(lambda x: x.has_attr("href") and "view" in x["href"]):
        print(each)
        # <a href="/wikicategory/view?categoryName=恐龙大全" target="_blank">恐龙百科</a>
        # 注意这里返回的是一个完整元素
        print(each.text, each["href"])  # 锁定 /view/10812319.htm, 下一级元素用.访问, 属性用[]访问

    # 注意用group的时候得用finditer, 不能用finall; findall会直接返回匹配到的串, 且不返group(0)对应的完整串(要么就在最外层再包一个())
    # 另外, 由于返回的html是一个大str, 不要轻易用.*匹配, 会匹配过头, 最好用\S, 避免超过空格往后匹配
    for each in re.finditer(r"(href=\"(\S*view\S*)\")", res.decode("utf-8")):
        print(each.group(0), each.groups())  # group(0)是完整匹配到的, groups()返回的是group(1), group(2)..., 不包括group(0)

    # 可以看一下findall, ('href="/view/10812319.htm"', '/view/10812319.htm'), 只包括group(1), group(2)...的; 如果外层不加(),
    # 这里只会拿到/view/10812319.htm
    # 用findall有findall的好处, 正则写好了可以直接拿到想要的内容(把这部分内容用()括起来)
    for each in re.findall(r"(href=\"(\S*view\S*)\")", res.decode("utf-8")):
        print(each)

    # 自己写re不如beautifulsoup, 不过re更灵活, 如果是查找具有某一模式的字符串, re比beautifulsoup好用
    # <a class="lock-lemma" href="/view/10812319.htm" nslog-type="10003105" target="_blank" title="锁定"><em class="aaa"></em>锁定</a>
    # 像是这种复杂标签情况, 自己写很难把'锁定'提取出来, BeautifulSoup则可以先定位到标签后, 再去拿标签的属性和子标签, 比如锁定对应子标签.text

except (error.HTTPError, error.URLError) as e:
    print("请求失败", e)




