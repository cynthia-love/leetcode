# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    求一个序列负索引对应的正索引
    0  1  2  3  4  5
    -6 -5 -4 -3 -2 -1
"""
from collections.abc import Sequence
def f(l:Sequence, i: int) -> int:

    if 0 <= i <= len(l) - 1:
        return i - len(l)
    if -len(l) <= i <= -1:
        return i + len(l)
    raise IndexError(i)

l = [1, 2, 3, 4, 5, 6]
# print(f(l, 0), f(l, 5), f(l, 6))
print(f(l, -1), f(l, -6), f(l, -7))