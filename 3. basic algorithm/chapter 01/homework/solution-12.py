# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    利用randrange实现自己的choice函数
    注意randrange是前闭后开, 和range一样
"""
import random
from collections.abc import Sequence

def f(l: Sequence) -> object:
    return l[random.randrange(len(l))]

l = [8, 100, 2, -1, 4]
print(f(l))