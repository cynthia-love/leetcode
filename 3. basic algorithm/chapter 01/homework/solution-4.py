# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    接收正整数n, 返回1~n的平方和
"""
def f(n: int) -> int:
    # x*x for x in range(1, n+1)不加[]为generator
    return sum(x*x for x in range(1, n+1))

print(f(10))
print(f(2))

def f2(n: int) -> int:
    res = 0
    for each in range(1, n+1):
        res += each * each
    return res

print(f(10))
print(f(2))