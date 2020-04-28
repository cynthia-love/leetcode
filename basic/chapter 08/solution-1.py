# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    永久存储
"""

"""
    文件
"""

f1 = open("data.txt", "r")
print(f1.read(7))  # 按照指定长度读入字符串, 不指定大小则读入全部