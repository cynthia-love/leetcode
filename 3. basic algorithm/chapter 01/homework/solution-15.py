# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    接收一个数字序列, 并判断是否所有数字都互不相同
"""

from typing import Sequence

def f(l: Sequence) -> bool:
    h = set(l)

    return len(l) == len(h)

print(f([1, 2,3 , 4, 8.1]))
print(f([1,2, 3, 8, 1.1, -1.2, 1.1]))