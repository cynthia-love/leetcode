# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    minmax(data), 返回序列中最小和最大数
    不可以用内置函数
    序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置
    所以可以直接用x[i]获取值
"""
# abc, abstract base class
from collections.abc import Sequence
def minmax(data: Sequence) -> bool:
    v_min, v_max = data[0], data[0]
    for each in data:
        if each < v_min: v_min = each
        if each > v_max: v_max = each

    return v_min, v_max

print(minmax([1]))
print(minmax([1, 2, 3, 4, 8, -1]))