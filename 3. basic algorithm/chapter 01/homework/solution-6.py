# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    接收一个正整数n, 计算1~n中所有奇数的平方和
"""

def f(n: int) -> int:
    res = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            res += i*i
    return res

print(f(1))
print(f(2))
print(f(4))