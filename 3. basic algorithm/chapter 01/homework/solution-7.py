# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    利用解析语法和内置sum, 计算1~n的所有奇数的平方和
"""
def f(n: int) -> int:
    return sum(x*x for x in range(1, n+1) if x % 2 == 1)

print(f(1))
print(f(2))
print(f(4))