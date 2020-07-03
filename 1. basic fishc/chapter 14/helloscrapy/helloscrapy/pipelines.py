# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from collections import OrderedDict
class HelloscrapyPipeline:
    def process_item(self, item, spider):
        od = OrderedDict()
        od["title"] = item["title"]
        od["link"] = item["link"]
        od["desc"] = item["desc"]
        return od
