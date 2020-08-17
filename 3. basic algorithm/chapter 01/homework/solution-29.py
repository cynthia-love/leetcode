# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    输出'c', 'a', 't', 'd', 'o', 'g' 所有可能组成的字符串, 不可重复
"""
from itertools import permutations
def f1():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    l_p = permutations(l, len(l))
    for each in l_p:
        print("".join(each))

f1()

# 方法2, 自己实现


