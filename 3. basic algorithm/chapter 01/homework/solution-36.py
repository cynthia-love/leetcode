# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    输入一个由空格分隔的单次列表, 输出每个单词出现的次数
"""
from collections import defaultdict
def f(s):
    d = defaultdict(int)
    ss = s.split(" ")
    for each in ss:
        d[each] += 1
    return d

print(f("hello world hahah hello"))