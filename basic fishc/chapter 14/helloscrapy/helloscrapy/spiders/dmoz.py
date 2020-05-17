# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    dmoz spider
"""
import scrapy

class dmoz(scrapy.Spider):
    name = 'dmoz'
    # scrapy会为start_urls中的每个url都创建一个Request对象, 并将parser()方法指定为回调函数
    start_urls = [
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/'
    ]
    allowed_domains = ["dmoztools.net"]   # 不在此域中的url不会访问

    # 注意这里的parser, 每个初始url返回response后都会调这个方法; 如果有多个url
    # 可以通过response.url区分是哪个url返回的, 以进行不同的处理逻辑
    def parse(self, response):
        print(response)
        source_url = response.url
        file_name = source_url.split("/")[-2]  # 一般url最后会带一个/
        with open("data/"+file_name, "wb") as f:
            f.write(response.body)
