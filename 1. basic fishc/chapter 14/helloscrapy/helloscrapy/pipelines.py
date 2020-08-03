# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from collections import OrderedDict
class HelloscrapyPipeline:
    def process_item(self, item, spider):

        # 如果要插入数据库, sql语句也在这里写, 注意先在__init__里建立数据库连接
        od = OrderedDict()
        od["title"] = item["title"]
        od["link"] = item["link"]
        od["desc"] = item["desc"]
        return od  # 别忘了最后这句return, 因为pipeline未必只有一个
