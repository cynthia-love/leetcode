# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    利用randint实现shuffle
"""
"""
    思路: [8, 7, 1, 2, 4], index为0-4
    第一个位置从5个里随机一个
    第二个位置从剩下的4个里随机一个
    这不就是A(5, 5)吗(排列)
"""
from typing import Sequence
from random import randint
from itertools import permutations, combinations

l = [8, 7, 1, 2, 4]
# 先试一下库函数permutations, 得到所有排列, 然后从里面随机选
print(list(permutations(l, 5)))
print(list(combinations(l, 4)))

def f(l: Sequence):
    for i in range(len(l)-1):
        # 确定了从0到倒数第2个元素, 那整个序列也就确定了
        j = randint(i, len(l)-1)
        # 0的时候在0-4里随机, 1的时候在1-4里随机
        # 确定了要填的元素之后, 和坑位互换元素
        l[i], l[j] = l[j], l[i]
f(l)
print(l)
