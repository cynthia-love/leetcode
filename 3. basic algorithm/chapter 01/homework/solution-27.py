# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改f函数, 保持其性能, 但按递增顺序产生因子
"""

def f(n: int):
    k = 1
    while k*k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1

    if k*k == n:
        yield k

print(list(f(8)))

def f2(n: int):
    k = 1
    right = []
    while k*k < n:
        if n % k == 0:
            yield k
            right.append(n // k)
        k += 1
    if k*k == n:
        yield k

    for each in right[::-1]:
        yield each

print(list(f2(8)))

