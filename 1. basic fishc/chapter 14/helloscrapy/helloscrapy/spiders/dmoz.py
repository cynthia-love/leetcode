# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    dmoz spider
"""
import scrapy
from helloscrapy.items import HelloscrapyItem


class dmoz(scrapy.Spider):
    name = 'dmoz'
    # scrapy会为start_urls中的每个url都创建一个Request对象, 并将parser()方法指定为回调函数
    # 注意这个start_urls是写在parse外面的
    start_urls = [
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/'
    ]
    allowed_domains = ["dmoztools.net"]  # 不在此域中的url不会访问

    # 注意这里的parser, 每个初始url返回response后都会调这个方法; 如果有多个url
    # 可以通过response.url区分是哪个url返回的, 以进行不同的处理逻辑
    # 启动爬虫时, Scrapy为Spider的start_urls属性中的每个url创建了Request对象，
    # 并将 parse 方法作为回调函数(callback)赋值给了requests,而requests对象经过调度器的调度，
    # 执行生成response对象并送回给parse() 方法进行解析

    def parse(self, response):
        # print(response.body)
        source_url = response.url
        file_name = source_url.split("/")[-2]  # 一般url最后会带一个/
        with open("data/" + file_name, "wb") as f:
            f.write(response.body)

        """
        res, items = [], response.xpath('//div[@class="title-and-desc"]')
        for item in items:
            t = HelloscrapyItem()
            t['title'] = item.xpath('a/div/text()').extract()[0].strip()
            t['link'] = item.xpath('a/@href').extract()[0].strip()
            t['desc'] = item.xpath('div/text()').extract_first().strip()
            res.append(t)
        return res
        """
        # 除了生成一个全的item list, 还可以用yield
        items = response.xpath('//div[@class="title-and-desc"]')
        for each in items:
            t = HelloscrapyItem()
            t['title'] = each.xpath('a/div/text()').extract()[0].strip()
            t['link'] = each.xpath('a/@href').extract()[0].strip()
            t['desc'] = each.xpath('div/text()').extract_first().strip()
            yield t

        url = "xxxx"  # 从页面里提取下一页的地址
        yield scrapy.Request(url, callback=self.parse)

        # 这里yield有两种类型, 引擎会自己判断类型确定是作为item出来还是作为请求发给调度器
