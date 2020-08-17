# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    接收一个整数序列 判断是否存在一对乘积是奇数的互不相同的数
"""
"""
    分析: 乘积是奇数, 那么每一项都是奇数
    相当于判断是否存在两个不同的奇数
"""
from collections.abc import Sequence
def f(l: Sequence) -> bool:
    m = None

    for each in l:
        if each % 2 == 1:
            if not m:
                m = each
            else:
                if m != each:
                    return True
    return False

l = [1, 2, 4, 4, 6, 7]
print(f(l))

