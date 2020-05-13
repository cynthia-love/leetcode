# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    编译
"""

# 像是match, search, findall等如果不想每次都传入正则表达式, 也可以编译一下后, 用得到的对象代替re
import re

pattern = re.compile(r"\b\d{3}\b")

print(pattern.search("1234 1243 333"))  # 333

# 和直接用search等函数一样, 编译也支持各种标志

pattern = re.compile(r".", re.S)   # .能匹配到换行符
print(pattern.search("\naa"))  # \n

pattern = re.compile(r"abcA", re.I)  # 不区分大小写
print(pattern.search("abca"))  # abca

pattern = re.compile(r"^abc$", re.M)  # 多行匹配, 即^和$不在要求完整字符串的首尾, 某一行的首尾符合要求也可以
print(pattern.search("ab\nac\nabc"))  # abc