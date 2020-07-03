# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    根据用户输入去查询百度百科对应词条有多少个义项, 二次请求, 然后打印出来每个的副标题(若有)
"""
from urllib import request
from urllib import parse
from urllib import error
from bs4 import BeautifulSoup
import re

def main():
    try:
        url = "https://baike.baidu.com/item/{}"
        word = input("请输出待搜索的词项: ")
        # 由于word可能是汉语词, 需要对其进行编码; parse.urlencode对dict类型的data进行编码, parse.qutoe对单个字符串编码
        # 注意只对单个单词编码, 而不要对整个url编码, 不然: / 什么的都变了网址就无法访问了
        res = request.urlopen(url.format(parse.quote(word))).read()

        # BeautifulSoup的输入参数可以直接是返回的二进制流, 不需要decode
        soup = BeautifulSoup(res, "html.parser")

        if soup.h2:
            # strip可以过滤多个字符, 直接传入字符串形式就行, 会自动拆成单个字符去strip
            print("默认项的副标题为: "+soup.h2.text.strip("（ ）")+", 其它项的副标题如下: ")
        # 这里h2是很里层的标签, 一样可以直接通过root级的.直接找到
        # 先找到所有的义项; 注意按属性查找时, 如果是class的话, 由于class是保留字,
        # 不能直接用class="xxxx"的形式得这么写attrs={"class": "xxx"}
        meanings = soup.find_all(href=re.compile(r"/item/.*/.*#viewPageContent"))
        for item in meanings:
            # 注意这里的text, 隔级也能找到<li><span>hello</span></li>
            # li的text也能找到hello
            # 本例中, 找到标签后直接.text就能列出要想要的副标题
            # 不过这里为了演示二次跳转, 再访问一层拿h2显示
            url2 = "https://baike.baidu.com"+item["href"]
            res2 = request.urlopen(url2).read()
            soup2 = BeautifulSoup(res2, "html.parser")
            if soup2.h2:
                print(soup2.h2.text.strip("（ ）")+": "+url2)

    except (error.URLError, error.HTTPError) as e:
        print("访问失败: ", e)

if __name__ == "__main__":
    main()