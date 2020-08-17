# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    分析函数体内是如何修改Sequence参数的值的
    默认情况下List里存的是指针, 这里相当于将l[i]指针指向了一个新的值
"""
from dis import dis
from typing import Sequence
def f(l: Sequence):
    for i in range(len(l)):
        l[i] *= 2

l = [1, 2, 3, 4]
f(l)
print(l)
print(dis(f))