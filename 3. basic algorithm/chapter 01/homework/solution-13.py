# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    逆置列表
"""
from collections.abc import Sequence

def rf1(l: Sequence) -> Sequence:
    left, right = 0, len(l)-1
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return l

l = [1, 2, 3, 4, 8, 10]
rf1(l)
print(l)

def rf2(l: Sequence) -> Sequence:
    # rf2 会生成一个新的列表
    return l[::-1]

print(rf1(l))