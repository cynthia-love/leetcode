# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    可选参数
"""

def f(a, b, c, d=0):
    print(a, b, c, d)

# 第一种写法比第二种简洁
def f2(a, b, c, d=None):
    if d is None:
        print(a, b, c, 0)
    else:
        print(a, b, c, d)

f(1, 2, 3)
f(1, 2, 3, 8)
f2(1, 2, 3)
f2(1, 2, 3, 8)