# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    输入三个整数a, b, c, 判断是否存在关系: a+b=c, a=b-c, a*b=c
"""

a = int(input())
b = int(input())
c = int(input())

def f(a: int , b: int, c: int) -> bool:
    return a+b == c or a == b-c or a*b == c

print(f(a, b, c))