# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    接收长度为n的两个整数数组a和b, 返回a和b的点积数组(不加总)
"""

def f(a:list, b:list) -> list:
    return [a[i]*b[i] for i in range(len(a))]

a = [1, 2, 3]
b = [8, 18, 28]
print(f(a, b))

def f2(a: list, b: list) -> list:
    return [x*y for x,y in zip(a, b)]
print(f2(a, b))